FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./
ADD . .

RUN set -ex \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# RUN python3 manage.py collectstatic --noinput

EXPOSE 8080

CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "demo.wsgi:application"]

# FROM python:3.9.0-alpine
# WORKDIR /usr/src/app
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .