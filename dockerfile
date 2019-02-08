FROM python:3.7.2-alpine3.8

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5050

CMD ["python", "main.py"]