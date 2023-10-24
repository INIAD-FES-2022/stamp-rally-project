FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app
RUN mkdir /var/lib/static
COPY ./stamp/static /var/lib/static
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod 755 /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

EXPOSE 80
EXPOSE 443
EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0", "config.wsgi:application"]