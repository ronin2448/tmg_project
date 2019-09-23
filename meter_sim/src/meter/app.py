FROM python:3.8.0b3-alpine3.10
ADD . /tmp/
RUN pip install -r /tmp/requirements.txt
EXPOSE 5000:5000
ENTRYPOINT ["python"]
CMD ["/tmp/app.py"]