FROM python:3.9

WORKDIR /src
COPY requirements.txt /scr
RUN pip install -r requirements.txt
COPY . /src