# 📌 api_final_yatube

**Yatube API** — RESTful API для социальной сети блогеров, разработанный с использованием Django и Django REST Framework. Предоставляет возможности для публикации постов, комментирования, подписки на авторов и управления контентом.

---

## 🚀 Возможности

- Регистрация и аутентификация пользователей с использованием JWT-токенов.
- Публикация, редактирование и удаление постов.
- Добавление и управление комментариями к постам.
- Создание и просмотр групп.
- Подписка на других пользователей и управление подписками.
- Просмотр ленты постов от подписанных авторов.

---

## 🛠️ Технологии

- Python 3.7+
- Django 2.2.16
- Django REST Framework
- Simple JWT
- SQLite (по умолчанию)

---

## 📦 Установка и запуск проекта

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/api_final_yatube.git
   cd api_final_yatube
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполните миграции:

   ```bash
   python manage.py migrate
   ```

5. Создайте суперпользователя:

   ```bash
   python manage.py createsuperuser
   ```

6. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

---

## 📚 Документация API

После запуска сервера документация API будет доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

---

## 🔐 Аутентификация

Для получения JWT-токена отправьте POST-запрос на эндпоинт:

```
/api/v1/jwt/create/
```

с телом запроса:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

В ответе вы получите `access` и `refresh` токены. Для доступа к защищённым эндпоинтам необходимо передавать `access` токен в заголовке Authorization:

```
Authorization: Bearer your_access_token
```

---

## 📂 Структура проекта

```
api_final_yatube/
├── manage.py
├── yatube_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
├── requirements.txt
└── README.md
```

---

## 🧪 Примеры запросов

- **Получить список всех постов (GET):**

  ```
  http://127.0.0.1:8000/api/v1/posts/
  ```

- **Создать новый пост (POST):**

  ```
  http://127.0.0.1:8000/api/v1/posts/
  ```

- **Получить список всех групп (GET):**

  ```
  http://127.0.0.1:8000/api/v1/groups/
  ```

- **Подписаться на пользователя (POST):**

  ```
  http://127.0.0.1:8000/api/v1/follow/
  ```

---

## 📝 Лицензия

Этот проект лицензируется под лицензией MIT.