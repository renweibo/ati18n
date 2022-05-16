FROM python:3.9-slim

COPY requirements.txt .
RUN apt update && apt install -y vim
RUN pip3 install -U -r requirements.txt
RUN pip3 install -U ati18n
CMD ati18n