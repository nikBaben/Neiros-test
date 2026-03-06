FROM python:3.12-slim

WORKDIR /VectorEditor

COPY . /VectorEditor

CMD ["python", "main.py"]