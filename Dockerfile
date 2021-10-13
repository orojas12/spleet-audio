# syntax=docker/dockerfile:1

FROM python:3.9

RUN apt update
RUN apt-get -y install ffmpeg
RUN apt-get -y install libsndfile1

WORKDIR /spleet-audio

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
