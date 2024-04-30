FROM python:3.9

RUN pip install python-telegram-bot==12.8

COPY . /app
COPY .env /app/.env

WORKDIR /app

CMD ["sh", "-c", "export $(xargs < .env) && python main.py"]
