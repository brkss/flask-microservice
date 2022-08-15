FROM python:3.9

COPY requirements.txt app/requirements.txt

WORKDIR app

COPY . app/

RUN pip install -r requirements.txt

RUN flask run
