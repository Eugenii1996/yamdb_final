# yamdb_final

![yamdb_workflow](https://github.com/Eugenii1996/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Разработчик:

 - [Мирошниченко Евгений](https://github.com/Eugenii1996)

### О проекте:

Проект YaMDb представляет собой платформу по сбору отзывов пользователей на опубликованные произведения.
Предоставляет клиентам доступ к базе данных.
Данные передаются в формате JSON.
В реализации проекта применена архитектура REST API.
Примененные библиотеки:
 - requests 2.26.0
 - asgiref 3.2.10
 - Django 2.2.16
 - django-filter 2.4.0
 - djangorestframework 3.12.4
 - djangorestframework_simplejwt 5.1.0
 - gunicorn 20.0.4
 - psycopg2-binary 2.8.6
 - PyJWT 2.1.0
 - pytz 2020.1
 - sqlparse 0.3.1
 - pytest 6.2.4
 - pytest-django 4.4.0
 - pytest-pythonpath 0.7.3

### Установка Docker на Windows:

Установите подсистему Linux (WSL2) следуя [инструкции](https://docs.microsoft.com/ru-ru/windows/wsl/install)
Установочный файл можно скачать с [официального сайта](https://www.docker.com/products/docker-desktop/)

### Клонировать репозиторий c GitHub:

```bash
git clone git@github.com:Eugenii1996/yamdb_final.git
```

### Шаблон наполнения env-файла:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DJANGO_ALLOWED_HOSTS=51.250.110.130
```

### Команды для Docker:

Сборка образа и запуск контейнера выполняется из директории с файлом docker-compose.yaml командой:

```bash
docker-compose up -d
```

Остановить собранные контейнеры:

```bash
docker-compose down -v
```

Команды внутри контейнера:

  - Выполнение миграций:

```bash
docker-compose exec web python manage.py migrate
```

  - Создание суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

  - Загрузка статики:

```bash
docker-compose exec web python manage.py collectstatic --no-input 
```

### Ссылка на развернутый и запущенный проект:

http://51.250.110.130/

### Как наполнить базу данных:

Описание API доступно по ссылке http://localhost/redoc/ при запуске приложения в контейнере