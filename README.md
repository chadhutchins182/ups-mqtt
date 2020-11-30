# ups-mqtt


<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![CI](https://github.com/chadhutchins182/ups-mqtt/workflows/CI/badge.svg)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/chadhutchins182/ups-mqtt.svg)](https://github.com/chadhutchins182/ups-mqtt/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Docker container for relaying data from a <a href="https://networkupstools.org/">Network UPS Tools</a> server to a mqtt server.
    <br> 
</p>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Tests](#tests)
- [Built Using](#built_using)
- [Authors](#authors)



## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites

1. Docker


#### Systems Tested

1. CentOS 7 Linux


### Installing

Pull from dockerhub 

```shell
docker pull chadhutchins182/ups-mqtt
```

#### Environment Variables

* UPS_HOSTNAME 
* BASE_TOPIC 
* MQTT_HOSTNAME 
* MQTT_PORT 
* MQTT_USERNAME 
* MQTT_PASSWORD 
* INTERVAL

#### Docker run


```shell
docker run -d --name ups-mqtt -e UPS_HOSTNAME \
 -e BASE_TOPIC= \
 -e MQTT_HOSTNAME= \
 -e MQTT_PORT= \
 -e MQTT_USERNAME= \
 -e MQTT_PASSWORD= \
 -e INTERVAL= \
 chadhutchins182/ups-mqtt
```

#### docker-compose.yml

```yml
version: '3.3'
services:
    ups-mqtt:
        container_name: ups-mqtt
        environment:
            UPS_HOSTNAME:
            BASE_TOPIC:
            MQTT_HOSTNAME:
            MQTT_PORT:
            MQTT_USERNAME:
            MQTT_PASSWORD:
            INTERVAL:
        image: chadhutchins182/ups-mqtt
```

## 🔧 Running the tests <a name = "tests"></a>

Currently uses GitHub Actions.

* Docker BuildX


## ⛏️ Built Using <a name = "built_using"></a>

- Python3
- paho.mqtt

## ✍️ Authors <a name = "authors"></a>

- [@dniklewicz](https://github.com/dniklewicz/ups-mqtt) - Original Fork of dniklewicz/ups-mqtt

See also the list of [contributors](https://github.com/chadhutchins182/ups-mqtt/contributors) who participated in this project.