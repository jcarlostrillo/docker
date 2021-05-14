FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY . /app

WORKDIR /app

CMD ["flask", "run", "--host=0.0.0.0"]
