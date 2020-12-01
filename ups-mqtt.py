#!/usr/bin/python3
# ups-mqtt.py

import os
import subprocess
import paho.mqtt.publish as mqtt
import time
from time import sleep, localtime, strftime
import datetime
from configparser import ConfigParser
import shutil

cached_values = {}

base_topic = os.environ.get('base_topic', 'home/ups')
if not base_topic.endswith('/'):
    base_topic += '/'

ups_host = os.environ.get('ups_hostname', 'localhost')
mqtt_host = os.environ.get('mqtt_hostname', 'localhost')
mqtt_port = int(os.environ.get('mqtt_port', 1883))
mqtt_user = os.environ.get('mqtt_username', None)
mqtt_password = os.environ.get('mqtt_password', None)
interval = int(os.environ.get('interval', 60))

print("ups_host: ", ups_host)
print("mqtt_host: ", mqtt_host)
print("mqtt_port: ", mqtt_port)
print("mqtt_password: ", mqtt_password)
print("interval: ", interval)


def process():
    ups = subprocess.run(["upsc", ups_host], stdout=subprocess.PIPE)
    lines = ups.stdout.decode('utf-8').split('\n')

    msgs = []

    for line in lines:
        fields = line.split(':')
        if len(fields) < 2:
            continue

        key = fields[0].strip()
        value = fields[1].strip()

        if cached_values.get(key, None) != value:
            cached_values[key] = value
            topic = base_topic + key.replace('.', '/').replace(' ', '_')
            msgs.append((topic, value, 0, True))

        timestamp = time.time()
        msgs.append((base_topic + 'timestamp', timestamp, 0, True))
        msgs.append((base_topic + 'lastUpdate', datetime.datetime.fromtimestamp(
            timestamp).strftime('%Y-%m-%d %H:%M:%S %Z'), 0, True))

        if mqtt_host == None or mqtt_password == None:
            mqtt.multiple(msgs, hostname=mqtt_host, port=mqtt_port)
        else:
            mqtt.multiple(msgs, hostname=mqtt_host, port=mqtt_port, auth={
                          'username': mqtt_user, 'password': mqtt_password})


while True:
    process()
    sleep(interval)
