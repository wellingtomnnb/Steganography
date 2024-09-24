FROM python:3.9

WORKDIR /app

COPY ./app /app/app
COPY ./data /app/data
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# iniciando a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
