FROM python:3.9-slim

WORKDIR /legacy-app

COPY requirements.txt .

RUN pip install -r requirements.txt

#FROM python:3.9-slim AS production

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]