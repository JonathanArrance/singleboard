#lib file for pitemp
import subprocess

def list_nics():
	#return list of nic cards
	try:
		proc = subprocess.Popen("sudo ls -I br* -I lo -I vir* /sys/class/net/", stdout=subprocess.PIPE, shell=True)
		(output,err) = proc.communicate()
		output = str(output).strip().split()
	except Exception as e:
		output = []

	return output

def get_nic_ip_info(nic):
	try:
		proc = subprocess.Popen("ip addr | grep '%s' -A2 | grep 'inet' | head -1 | awk '{print $2}' | cut -f1  -d'/'"%nic, stdout=subprocess.PIPE, shell=True)
		(output,err) = proc.communicate()
		ip = str(output).strip()
	except Exception as e:
		ip = e

	try:
		proc2 = subprocess.Popen("/sbin/ip route | awk '/default/ { print $3 }'", stdout=subprocess.PIPE, shell=True)
		(output2,err2) = proc2.communicate()
		gateway = str(output2).strip()
	except Exception as e:
		gateway = e

	return {'ip':ip,'gateway':gateway}
