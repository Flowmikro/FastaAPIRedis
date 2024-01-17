FROM python:3.11-alpine

COPY requirements.txt /temp/requirements.txt
COPY . /app

WORKDIR /app

EXPOSE 8000

RUN pip install -r /temp/requirements.txt
