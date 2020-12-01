FROM python:3-slim

RUN apt-get update && apt-get install -y nut-client && \
    pip install --no-cache-dir paho-mqtt && \
    mkdir -p /opt/app/conf

WORKDIR /opt/app

ADD ups-mqtt.py ./

CMD ["python", "-u", "ups-mqtt.py"]
