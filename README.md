# Restaurant API

Это проект API для бронирования столиков в ресторане, созданный с использованием Django и PostgreSQL, с развертыванием через Docker.

## Описание

API позволяет:
- Просматривать и управлять столиками.
- Создавать, удалять и просматривать брони на столики.
- Проверку на пересечение времени бронирования для столиков.

## Требования

- Docker
- Docker Compose

## Установка и запуск

1. **Клонировать репозиторий:**

```bash
git clone https://github.com/yourusername/restaurant-api.git
cd restaurant-api
```

2. **Создать файл `.env`** в корне проекта с переменными для базы данных (или используйте свой `.env` файл):

```env
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432
```

3. **Запустить контейнеры:**

```bash
docker-compose up --build
```

4. **Доступ к приложению:**
   - API будет доступен на [http://localhost:8000](http://localhost:8000).
   - База данных PostgreSQL доступна на порту `5432`.

5. **Миграции:**
   Чтобы применить миграции базы данных, выполни:

```bash
docker-compose exec web python manage.py migrate
```

6. **Создание суперпользователя:**
   Для создания суперпользователя выполните:

```bash
docker-compose exec web python manage.py createsuperuser
```

## Структура проекта

- `backend/` — исходный код приложения Django.
- `docker-compose.yml` — конфигурация для запуска сервисов через Docker.
- `.env` — переменные окружения для конфигурации базы данных.
- `requirements.txt` — список зависимостей Python.
