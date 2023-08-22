FROM nvidia/cuda:11.3.0-devel-ubuntu20.04

WORKDIR /usr/src/app

RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 python3-pip python3-opencv python3-dev

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x \
    gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    libglib2.0-dev libgstrtspserver-1.0-dev gstreamer1.0-rtsp

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt