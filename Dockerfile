FROM python:3.9-slim

WORKDIR /app
COPY . /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir pipenv && pipenv install --deploy --system

EXPOSE 5000

CMD ["python", "app.py"]

