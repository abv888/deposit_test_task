# Быстрый старт

## Docker


## Локальная
```bash
python src/Backend/start.py
```
## или
```bash
cd src/Backend
python -m app 
```` 

## Запуск тестов
### Просто запуск тестов
```bash
pytest
```
### Запуск тестов с показом покрытием
```bash
pytest --cov= src/Backend/tests/ 
```
### Запуск тестов с покрытием и выводом в html
```bash
pytest --cov= src/Backend/tests/ --cov=report hhtml --cov report term

```

# Swagger
## http://127.0.0.1:8000/docs

