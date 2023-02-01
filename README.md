<h1 align="center">Система транзакций</h1>

## Запуск проекта

[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) и [Docker Compose](https://docs.docker.com/compose/install/linux/) должны быть предварительно установлены. Склонируй репозиторий и перейди в папку с проектом:

```
git clone https://github.com/Tizoner/transaction-system.git && cd transaction-system
```

Затем запусти все сервисы проекта одной командой:

```
docker compose up
```

После этого по адресу [/docs/](http://localhost:8000/docs/) становится доступна документация разработанного API в формате OpenApi.
По адресу [/admin/](http://localhost:8000/admin/) можно попасть в админ панель. Аккаунт администратора будет создан автоматически на основе данных из **`envs/web.env`** файла.

## Использованные технологии

- Язык программирования [Python](https://www.python.org) &nbsp;`3.10`
- Веб-фреймворк [Django](https://www.djangoproject.com) &nbsp;`4.1`
- REST фреймворк [DRF](https://www.django-rest-framework.org) &nbsp;`3.14`
- СУБД [PostgreSQL](https://www.postgresql.org) &nbsp;`15`
- Распределенная очередь задач [Celery](https://docs.celeryq.dev) &nbsp;`5.2`
- Брокер сообщений [Redis](https://redis.io) &nbsp;`7.0`
- Платформа контейнеризации [Docker](https://www.docker.com) &nbsp;`20.10`

## Примечание

Файлы **`envs/web.env`**, **`envs/db.env`** содержат примеры значений используемых переменных окружения, поэтому эти файлы не были добавлены в .gitignore.
