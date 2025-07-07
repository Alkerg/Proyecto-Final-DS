FROM python:3.9-alpine

WORKDIR /new-microservice

COPY requirements.txt .

RUN pip install -r requirements.txt

#FROM python:3.9-alpine AS production

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]