#!/bin/bash -x
openssl req -nodes -newkey rsa:2048 -keyout mqtt_key.key -out mqtt_csr.csr -subj "/C=US/ST=Home/L=HOME/O=Global Security/OU=MQTT Department/CN=nothing.com"
openssl x509 -req -days 365 -in ./mqtt_csr.csr -signkey ./mqtt_key.key -out mqtt_cert.crt
