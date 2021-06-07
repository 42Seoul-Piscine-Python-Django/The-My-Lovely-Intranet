FROM python:3.9.5-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 /usr/src/app/manage.py makemigrations
RUN python3 /usr/src/app/manage.py migrate
RUN python3 /usr/src/app/manage.py collectstatic --noinput


CMD ["python", "-m", "gunicorn", "theMyLovelyIntranet.wsgi", "-b" ,"0.0.0.0:8000"]
