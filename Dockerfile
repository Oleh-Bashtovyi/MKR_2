FROM python:3.11.4-slim-buster

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

ENV PORT=8000
EXPOSE $PORT 8000

CMD python manage.py migrate & python manage.py runserver 0.0.0.0:$PORT