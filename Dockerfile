FROM python:3.9

WORKDIR /usr/src/app/bot
COPY requirements.txt /usr/src/app/bot/requirements.txt
RUN pip install -r /usr/src/app/bot/requirements.txt
COPY . /usr/src/app/bot