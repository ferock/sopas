FROM gcr.io/google_appengine/python

RUN virtualenv /env

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ADD bdeliveryonline.json /app/bdeliveryonline.json
ENV GOOGLE_APPLICATION_CREDENTIALS /app/bdeliveryonline.json

RUN apt-get install libmysqlclient-dev

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

add . /app

CMD gunicorn  --error-logfile error.log --log-level DEBUG -b :$PORT AquiSopas.wsgi
