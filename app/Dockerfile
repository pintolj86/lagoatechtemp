FROM python:3.10.0-buster
COPY src/requirements.txt /root/
RUN pip install -r /root/requirements.txt && useradd -m lagoa
ENV HOME=/home/lagoa
USER lagoa
COPY src/app01.py src/wsgi.py src/gunicorn_config.py /home/lagoa/
WORKDIR /home/lagoa/
EXPOSE 8080
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:lagoa", "--reload"]