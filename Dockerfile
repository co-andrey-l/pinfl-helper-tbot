FROM python:3.9

# Установка зависимостей
RUN pip install python-telegram-bot==12.8

# Копирование исходного кода в контейнер
COPY . /app

# Копирование файла .env в контейнер
COPY .env /app/.env

# Установка рабочей директории
WORKDIR /app

# Команда для запуска приложения с использованием переменных окружения из .env
CMD ["sh", "-c", "export $(xargs < .env) && python main.py"]
