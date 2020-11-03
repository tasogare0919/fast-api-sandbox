FROM python:3.8-alpine

WORKDIR /app

RUN pip install gunicorn falcon

COPY main.py .
EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "main:app"]