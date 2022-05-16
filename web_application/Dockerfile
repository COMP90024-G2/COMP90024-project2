FROM python:3

ADD  . /

RUN /bin/sh -c 'pip install -r requirements.txt && python3 preprocess_json.py'

CMD ["gunicorn", "run:app", "-c", "./gunicorn.conf.py"]