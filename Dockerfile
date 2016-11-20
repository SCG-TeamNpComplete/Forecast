FROM ubuntu:12.04

RUN apt-get update
RUN apt-get install -y python-dev python-pip
 
ADD ./Forecast/ ./
RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install requests
RUN pip install flask
RUN pip install kazoo
RUN pip install uuid
RUN pip install datetime
RUN pip install logging
ENV FLASK_APP=forecast.py
EXPOSE 64000
CMD python forecast.py
