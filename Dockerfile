FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime
ENV DEBIAN_FRONTEND=noninteractive

COPY . .
# Run the package installation
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt
RUN curl -fsSL https://ollama.com/install.sh | sh

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
EXPOSE 1417

RUN chmod +x run.sh

CMD ["sh", "-c", "./run.sh"]
