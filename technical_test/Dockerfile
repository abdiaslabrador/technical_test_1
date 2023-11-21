FROM python:3.12.0
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY . ./code

COPY requirements.txt /code/requirements.txt

RUN python -m pip install -r /code/requirements.txt