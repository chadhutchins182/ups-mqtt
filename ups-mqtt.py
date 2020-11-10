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

if not os.path.exists('conf/config.ini'):
    shutil.copy('config.ini', 'conf/config.ini')

# Load configuration file
config_dir = os.path.join(os.getcwd(), 'conf/config.ini')
config = ConfigParser(delimiters=('=', ), inline_comment_prefixes=('#'))
config.optionxform = str
config.read(config_dir)

cached_values = {}

base_topic = os.getenv('base_topic', 'home/ups')
if not base_topic.endswith('/'):
    base_topic += '/'

ups_host = os.getenv('ups_hostname', 'localhost')
mqtt_host = os.getenv('mqtt_hostname', 'localhost')
mqtt_port = os.getenv('mqtt_port', 1883)
mqtt_user = os.getenv('mqtt_username', None)
mqtt_password = os.getenv('mqtt_password', None)
interval = os.getenv('interval', 60)

def process():
    ups = subprocess.run(["upsc", "ups@" + ups_host], stdout=subprocess.PIPE)
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
        msgs.append((base_topic + 'lastUpdate', datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S %Z'), 0, True))
        mqtt.multiple(msgs, hostname=mqtt_host, port=mqtt_port, auth={'username': mqtt_user, 'password': mqtt_password})



while True:
    process()
    sleep(interval)
    