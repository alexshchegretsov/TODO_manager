FROM python:3
MAINTAINER Alex Shchegretsov <a.shchegretsov@gmail.com>
WORKDIR /app
COPY ./src/requirements.txt /app
RUN pip install -r requirements.txt
COPY ./src /app

