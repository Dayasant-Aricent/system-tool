FROM ubuntu:latest
MAINTAINER Anuyog Chauhan "anuyog.chauhan@aricent.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV http_proxy ""
ENV https_proxy ""
ENTRYPOINT ["python"]
CMD ["system-tools.py"]
