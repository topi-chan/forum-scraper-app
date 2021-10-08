# syntax=docker/dockerfile:1
FROM python:3.10.0-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /code/forum_scraper
COPY requirements.txt /
RUN pip install -r /requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
