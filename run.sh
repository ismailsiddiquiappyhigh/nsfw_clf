set -m

python3 main.py &

ollama serve &

ollama run llama2:7b-chat --keepalive 999999m --verbose

fg %1