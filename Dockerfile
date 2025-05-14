# Базовый образ
FROM python:3.10-slim

# Установка зависимостей
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Команда по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
