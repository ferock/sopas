FROM gcr.io/google_appengine/python

RUN virtualenv /env

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN apt-get install libmysqlclient-dev

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

add . /app

CMD gunicorn  --error-logfile error.log --log-level DEBUG -b :$PORT AquiSopas.wsgi
