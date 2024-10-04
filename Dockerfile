FROM python:3.12-alpine

WORKDIR /app

RUN pip install --no-cache-dir "poetry==1.6.1"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
     && poetry install --no-root

COPY . .env ./

CMD  python manage.py migrate \
     && python manage.py runserver 0.0.0.0:8000