# Быстрый старт

## Docker
```bash 
docker compose build
docker compose up
```

## Локальная
### Установка
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Запуск сервера
```bash
python src/Backend/start.py
```
### или
```bash
cd src/Backend
python -m app 
```` 

## Запуск тестов
### Просто запуск тестов
```bash
pytest
```
### Запуск тестов с показом покрытия
```bash
pytest --cov= src/Backend/tests/ 
```
### Запуск тестов с покрытием и выводом в html
```bash
pytest --cov=src/Backend/tests/ --cov-report html --cov-report term

```

# Swagger
## http://127.0.0.1:8000/docs

