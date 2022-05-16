FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN ls -a

RUN pip install -r api_yamdb/requirements.txt

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]