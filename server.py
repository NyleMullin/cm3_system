# Python program to write JSON
# to a file
import json
import subprocess

def SystemServer():
    while True:
        cmd = "hostname -I | cut -d' ' -f1"
        IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
        IP = IP.rstrip('\n')

        cmd = 'cut -f 1 -d " " /proc/loadavg'
        CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
        CPU = CPU.rstrip('\n')

        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
        MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
        Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = "ip addr show $(awk 'NR==3{print $1}' /proc/net/wireless | tr -d :) | awk '/ether/{print $2}'"
        MAC = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = "hostnamectl | grep hostname | awk '{print $2,$3}'"
        Hostname = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = "sudo netstat -tuwanp4 | awk '{print $4}' | grep ':' | cut -d ':' -f 2 | sort | uniq"
        Ports = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = "iwconfig wlan0 | grep Freq | awk '{print $2,$3}' | cut -d':' -f2"
        Freq = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = """iwconfig wlan0 | grep ESSID | awk '{print $4}' | cut -d'"' -f2"""
        SSID = subprocess.check_output(cmd, shell=True).decode("utf-8")

        cmd = "who | wc -l"
        Clients = subprocess.check_output(cmd, shell=True).decode("utf-8")

        # Data to be written
        data = {
            "system":{
                "CPU": CPU,
                "Mem": MemUsage,
                "Disk": Disk,
                "Hostname": Hostname,
            },
            "network":{
                "IP": IP,
                "MAC": MAC,
                "SSID": SSID,
                "Ports": Ports,
                "Freq": Freq,
                "Clients": Clients,
            },
            "link":{
                "Connected": False,
                "Strength": False,
            },
            "battery":{
                "Charging": False,
                "Percentage": False,
                "TTC": False,
                "TTD": False,
                "Volt": False,
            },
            "mapping":{
                "Running": False,
                "Style": False,
                "Tileset": False,
            },
            "Systemlog":{
                "Systemlog": False,
            },
        }

        with open('state.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    SystemServer()
