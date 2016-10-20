FROM ubuntu:12.04

RUN apt-get update
RUN apt-get install -y python-dev python-pip
 
ADD ./Forecast/ ./
RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install requests
RUN pip install flask 
ENV FLASK_APP=forecast.py
EXPOSE 64000
CMD flask run --host=0.0.0.0 --port=64000