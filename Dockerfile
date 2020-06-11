FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /blog

COPY Pipfile Pipfile.lock /blog/
RUN pip install pipenv && pipenv install --system

COPY django_blog_api .
