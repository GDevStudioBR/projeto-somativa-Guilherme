
FROM python:latest


WORKDIR /app


COPY . .


RUN mkdir -p cartas


CMD ["python", "main.py"]
