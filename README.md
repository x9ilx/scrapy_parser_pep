# Проект парсинга pep

## Описание проекта

Проект представляет собой парсер PEP

## Функционал проекта

Пользователь может получить данные о всех PEP (Номер, название и статус), а так же данные о количестве PEP в каждом статусе и общее количество PEP.

## Инструкция по запуску проекта

Для проекта к запуску необходимо создать вируальное окружение в директории проекта:

```bash
# windows
python -m venv venv

# linux
python3 -m venv venv
```

после чего активировать его и установить необходимые зависимости

```bash
# windows
source venv/scripts/activate
pip install -r requirements.txt

# linux
~ bin/scripts/activate
pip install -r requirements.txt
```

Для запуска необходимо запустить "паука" scrapy

```bash
scrapy crawl pep
```

Результат, в формате csv будет сохранён в папке results.

## Пример использования 

для Linux используется "python3" вместо "python", а так же "~", вместо "source"
```bash
# windows
git clone <repository_url>
cd scrapy_parser_pep
python -m venv venv
source venv/script/activate
pip install --upgrade pip
pip install -r requirements.txt
scrapy crawl pep
```

## Иcпользованные технологии
- Scrapy - это бесплатный фреймворк для веб-краулинга находящийся в открытом доступе, который написан на языке программирования Python. Изначально задумывался для веб-скрейпинга, однако также может использоваться для извлечения информации используя API или же как веб краулер общего применения.

## Автор
Бондаренко Владимир Викторович