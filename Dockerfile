FROM python:slim
RUN apt-get update && yes | apt-get install gcc
RUN pip install bottle redis passlib py-bcrypt
