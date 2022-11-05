# Сервис по сбору отзывов на произведения YaMDb

![yamdb_workflow](https://github.com/Eugenii1996/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Разработчик:

 - [Мирошниченко Евгений](https://github.com/Eugenii1996)

### О проекте:

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

Примененные технологии:
 - Python 3
 - Django Rest Framework
 - Docker
 - Git
 - Pytest

### Установка Docker на Windows:

Установите подсистему Linux (WSL2) следуя [инструкции](https://docs.microsoft.com/ru-ru/windows/wsl/install)
Установочный файл можно скачать с [официального сайта](https://www.docker.com/products/docker-desktop/)

### Клонирование репозитория и переход в него в командной строке:

```bash
git clone git@github.com:Eugenii1996/yamdb_final.git
```

```bash
cd yamdb_final
```

### Cоздать и активировать виртуальное окружение:

Виртуальное окружение должно использовать Python 3.7

```bash
pyhton -m venv venv
```

* Если у вас Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Если у вас windows

    ```bash
    source venv/scripts/activate
    ```

### Установка зависимостей из файла requirements.txt:

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
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
