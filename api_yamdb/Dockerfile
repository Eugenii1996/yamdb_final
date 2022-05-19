FROM python:3.7-slim

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]