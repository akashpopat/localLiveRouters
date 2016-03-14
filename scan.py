import nmap
import urllib, json


def find_ip_range():
    data = json.loads(urllib.urlopen("http://ip.jsontest.com/").read())
    ip = str(data["ip"])
    return ip[:ip.rfind('.')]+'.*'

def scan_ip_range(ip_range):
    nm = nmap.PortScanner()
    nm.scan(hosts= ip_range,ports='80',arguments='')
    ip_list = []
    for n in nm.all_hosts():
        ip_list.append(str(n))
    return ip_list


print scan_ip_range(find_ip_range())

