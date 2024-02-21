FROM python:3.10.9-alpine3.17
RUN mkdir /opt/demo && chmod 777 /opt/demo
WORKDIR /opt/demo
COPY ["generator/*", "./"]
ENTRYPOINT ["python"]
CMD ["test_next_random_num.py"]
