FROM python:3-alpine

ADD . /app

RUN pip install requests

WORKDIR /app

CMD [ "python", "./macAddressAPI.py"]