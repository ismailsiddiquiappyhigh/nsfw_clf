import warnings
warnings.filterwarnings('ignore')
import io
import base64, time
import traceback
from PIL import Image
from typing import List
from json import dumps
from pydantic import BaseModel, Field
from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.exceptions import RequestValidationError

app = FastAPI()

class Input(BaseModel):
    inp_text: str
    model : str

from ollama import Client
client = Client(host='http://localhost:11434')

@app.post("/clf_text")
def generator(input: Input):
    try:
        srt = time.time()
        
        system = 'Tell the given text/prompt is NSFW or not. If its NSFW then say "Yes" otherwise say "No" only. Your answer should be accurate and no explaination.'

        response = client.generate(
            model=input.model,
            prompt=input.inp_text,
            system=system, 
            keep_alive = 99999999999
        )
        
        print('Total Time: ', time.time()-srt)
        
        response_ = {'result': response['response']}
    
    except Exception as e:
        request_body = dumps(input.dict(), default=str)
        print('Error on Request:')
        print(request_body)
        print('---'*25)
        response_ = "Internal Server Error: " + str(e)
        traceback_message = traceback.format_exc()
        print(traceback_message)
        return Response(content=dumps(response_, default=str), headers={"Content-Type": "application/json"}, status_code=500)
    
    return Response(content=dumps(response_, default=str), headers={"Content-Type": "application/json"})