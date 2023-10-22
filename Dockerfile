FROM nginx

WORKDIR /usr/src/app

COPY . /usr/src/app

EXPOSE 80

CMD ["sudo", "nginx"]