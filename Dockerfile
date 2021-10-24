FROM python:3.8.12-buster

WORKDIR /docker-ims

ADD . /docker-ims

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
