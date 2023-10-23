FROM nginx

WORKDIR /usr/src/app

COPY . /usr/src/app

EXPOSE 80
EXPOSE 443
EXPOSE 8000

ENTRYPOINT ["sudo", "nginx"]