# Проект парсинга pep

## Описание проекта

Проект представляет собой парсер документаци Python

## Функционал проекта

Пользователь может получить данные о всех PEP (Номер, название и статус), а так же данные о количестве PEP в каждом статусе и общее количество PEP.

## Инструкция по запуску проекта

Для проекта к запуску необходимо создать вируальное окружение:

```python
# windows
python -m venv venv

# linux
python3 -m venv venv
```

после чего активировать его и установить необходимые зависимости

```python
# windows
source venv/scripts/activate
pip install -r requirements.txt

# linux
~ bin/scripts/activate
pip install -r requirements.txt
```

Для запуска необходимо запустить "паука" scrapy

```python
scrapy crawl pep
```

Результат, в формате csv будет сохарнён в папке results.