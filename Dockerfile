FROM python:3-slim

RUN apt-get update && apt-get install -y nut-client && \
    pip install --no-cache-dir paho-mqtt && \
    mkdir -p /opt/app/conf

WORKDIR /opt/app

ENV ups_hostname=$UPS_HOSTNAME \
    base_topic=$BASE_TOPIC \
    mqtt_hostname=$MQTT_HOSTNAME \
    mqtt_port=$MQTT_PORT \
    mqtt_username=$MQTT_USERNAME \
    mqtt_password=$MQTT_PASSWORD \
    interval=$INTERVAL

ADD ups-mqtt.py ./

CMD ["python", "ups-mqtt.py"]
