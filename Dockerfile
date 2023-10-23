FROM nginx

WORKDIR /usr/src/app

COPY . /usr/src/app

ENTRYPOINT ["sudo", "nginx"]

EXPOSE 80
EXPOSE 443
EXPOSE 8000