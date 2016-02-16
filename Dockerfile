FROM ubuntu:14.04
MAINTAINER Igor Rinkovec <igor.rinkovec+github@gmail.com>

RUN apt-get update --fix-missing && apt-get install -y python python-setuptools ghostscript
RUN easy_install pip

WORKDIR /code/

RUN pip install Flask
RUN pip install jinja2

ADD ./code /code/
RUN mkdir /code/generated

EXPOSE 5000
CMD python /code/server.py