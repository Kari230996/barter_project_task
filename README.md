# 📦 Barter Platform — Django REST приложение для обмена товарами

Это веб-приложение на Django, реализующее платформу обмена вещами. Пользователи могут создавать объявления, предлагать обмен, фильтровать предложения, регистрироваться, а также визуально взаимодействовать с сайтом через адаптивный интерфейс.

---

## 🚀 Возможности

* Регистрация и авторизация пользователей
* Создание, редактирование и удаление объявлений
* Прикрепление изображений через ссылки (URL)
* Просмотр всех объявлений и фильтрация по:

  * категории
  * состоянию (новое/б/у)
  * ключевому слову
* Обмен предложениями:

  * выбор своего и чужого товара
  * добавление комментария
  * отслеживание статуса (ожидает, принята, отклонена)
* Модальное окно увеличения изображения и описания при клике
* Адаптивный интерфейс на Bootstrap 5

---

## ⚙️ Установка проекта локально с Docker

### 1. Клонировать репозиторий

```bash
git clone https://github.com/Kari230996/barter_project_task.git
cd barter_project_task
```

### 2. Запуск через Docker
1. Перед запуском переименуйте вручную файл `.env.example` на `.env`
2. Затем откройте `.env` и замените SECRET_KEY на любой другой:
```bash
SECRET_KEY=django-insecure-замените-на-уникальный-ключ
```
3. Сгенерировать новый ключ можно командой на Windows:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```
4. Запускайте проект командой:
```bash
docker-compose up --build
```

### 3. Применить миграции

```bash
docker compose exec web python manage.py migrate
```

### 4. Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```

Проект будет доступен по адресу: [http://localhost:8000](http://localhost:8000)

---

## 🚫 Альтернативный запуск без Docker (необязательно)

1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Выполните миграции и запустите сервер:
```bash
python manage.py migrate
python manage.py runserver
```

## 🛠 Технологии

* Python 3.10+
* Django 5.x
* Django REST Framework
* drf-yasg (Swagger-документация)
* SQLite (по умолчанию)
* Bootstrap 5 (адаптивная верстка)

---

## 🧪 Тестирование

### 📁 Pytest + Django: `tests/test_ads.py`

Запуск всех тестов:

```bash
pytest
```

Тесты покрывают:

* Создание объявления
* Редактирование объявления
* Удаление объявления
* Поиск по ключевому слову
* Создание предложения обмена

---

## 🧾 Документация API

Автоматическая Swagger-документация доступна по адресу:

[http://localhost:8000/swagger/](http://localhost:8000/swagger/)

⚠️ Все эндпоинты API начинаются с префикса `/api/`.  
Пример запроса: `GET http://localhost:8000/api/ads/`

## ✨ Автор

Разработано в рамках тестового задания. Визуальный акцент — простота, чистота и удобство.

---

**📧 Связь:** \karina.apaeva96@gmail.com

---


