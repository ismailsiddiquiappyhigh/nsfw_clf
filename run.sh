set -m

python3 main.py &

ollama serve &

ollama run llama2:7b-chat --keepalive 999999m --verbose

jupyter notebook --config=jupyter.py --NotebookApp.token= --NotebookApp.password=

fg %1
