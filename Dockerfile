FROM nginx

WORKDIR /usr/src/app

COPY . /usr/src/app

ENTRYPOINT ["sudo", "nginx"]

EXPOSE 80