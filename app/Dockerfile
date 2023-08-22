FROM nvidia/cuda:11.3.0-devel-ubuntu20.04

WORKDIR /usr/src/app

RUN apt-get update &&\
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  python3 python3-pip python3-opencv python3-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt