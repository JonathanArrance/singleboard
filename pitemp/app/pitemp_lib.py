#lib file for pitemp
import subprocess
import settings
import logging
import ssl
import paho.mqtt.client as paho

class pitemp():
	
	def __init__(self):
		self.client = paho.Client()
		self.client.tls_set(settings.SSLCERT)
		self.client.tls_insecure_set(True)
		try:
			self.client.connect(settings.MQTTBROKER, settings.MQTTPORT, 60)
			self.client.loop_start()
		except Exception as e:
			logging.error(e)
			logging.error("Could not connect to the MQTT Broker")

	def list_nics(self):
		#return list of nic cards
		try:
			proc = subprocess.Popen("sudo ls -I br* -I lo -I vir* /sys/class/net/", stdout=subprocess.PIPE, shell=True)
			(output,err) = proc.communicate()
			output = str(output).strip().split()
		except Exception as e:
			output = []

		return output

	def get_nic_ip_info(self,nic):
		try:
			proc = subprocess.Popen("ip addr | grep '%s' -A2 | grep 'inet' | head -1 | awk '{print $2}' | cut -f1  -d'/'"%nic, stdout=subprocess.PIPE, shell=True)
			(output,err) = proc.communicate()
			ip = str(output.decode('ascii').strip())
		except Exception as e:
			ip = e

		try:
			proc2 = subprocess.Popen("/sbin/ip route | awk '/default/ { print $3 }'", stdout=subprocess.PIPE, shell=True)
			(output2,err2) = proc2.communicate()
			gateway = str(output2.decode('ascii').strip())
		except Exception as e:
			gateway = e

		return {'ip':ip,'gateway':gateway}


	def send_mqtt(self):
		#send a mesage to the MQTT broker, pub
		
		
	def recieve_mqtt(self):
		#get a message to the MQTT broker, sub 
		pass

