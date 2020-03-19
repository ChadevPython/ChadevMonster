FROM python:3.8-buster
WORKDIR /usr/src/app
COPY . /usr/src/app
ENV ENVIRONMENT=dev
RUN pip install -r requirements/base.txt
RUN mv config/example-dev.py /usr/src/app/config/dev.py
#RUN ./manage.py create_db
#RUN ./manage.py db upgrade
RUN ls -l /usr/src/app/config/
CMD python run.py