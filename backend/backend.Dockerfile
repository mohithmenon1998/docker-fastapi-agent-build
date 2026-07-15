FROM python:3.13.4-slim-bullseye

RUN apt-get update && apt-get install -y curl

# Create python virtual environment
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# FIX: Copies everything from your backend context directly into /app
COPY . .