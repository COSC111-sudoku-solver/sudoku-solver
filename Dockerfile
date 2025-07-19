FROM ubuntu:latest

RUN apt-get update && apt-get install -y bash python3 python3-pip python3-venv curl git tesseract-ocr libgl1&& apt-get clean && python3 -m venv venv && . ./venv/bin/activate&& pip install sudoku-solver-ocr

ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata

WORKDIR /app

COPY . /app

CMD ["bash"]
