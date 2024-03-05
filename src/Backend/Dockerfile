FROM python:3.11
RUN mkdir /code2
WORKDIR /code2
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src ./src
COPY pyproject.toml .
