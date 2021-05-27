# FROM tiangolo/uwsgi-nginx-flask:python2.8
FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update

RUN apt-get install -y build-essential postgresql-server-dev-all

RUN pip install psycopg2

COPY . /app

WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]
