FROM nginx:latest

COPY ./html /usr/share/nginx/html
COPY ./secure /home/secure
COPY .htpasswd /etc/pwd/.htpasswd

RUN apt-get update && apt-get install -y procps
RUN apt-get install --no-install-recommends -y apache2-utils
RUN mkdir -p /home/app/static
