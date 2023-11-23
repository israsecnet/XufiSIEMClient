import socket
import requests
import psutil
import uuid
import platform, json


'''
    ONLY FOR WINDOWS
    
    Extracts Local IP, External IP, Hostname, Users, and MAC
'''

def get_local_ip():
    local_ip = socket.gethostbyname(socket.gethostname())
    return local_ip

def get_external_ip():
    try:
        response = requests.get("https://httpbin.org/ip")
        external_ip = response.json()["origin"]
    except requests.RequestException:
        external_ip = "Not available"
    return external_ip

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_users():
    users = [user.name for user in psutil.users()]
    return users

def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    return mac

def get_os_info():
    os_info = platform.system()
    os_version = platform.version()
    return f"{os_info} {os_version}"

def main():
    local_ip = get_local_ip()
    external_ip = get_external_ip()
    hostname = get_hostname()
    users = get_users()
    mac_address = get_mac_address()
    os_info = get_os_info()
    nd = {
        "Local IP": local_ip,
        "External IP": external_ip,
        "Hostname": hostname,
        "Users": users,
        "MAC Address": mac_address,
        "OS": os_info
    }
    with open('AgentOverview.json', 'w') as json_file:
        json.dump(nd, json_file, indent=4)
