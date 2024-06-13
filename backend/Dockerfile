#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
FROM python:3.8-slim
COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ../app ./app

ENTRYPOINT uvicorn app.app:app --host ${HOST} --port ${PORT}