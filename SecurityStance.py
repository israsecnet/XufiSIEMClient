import os
import platform
import socket
import subprocess
import json

def get_system_info():
    system_info = {}
    
    # Basic System Information
    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    # Network Information
    system_info['Hostname'] = socket.gethostname()
    system_info['IP Address'] = socket.gethostbyname(socket.gethostname())

    # User Information
    system_info['User'] = os.getlogin()

    # Security Information
    system_info['Firewall Status'] = check_firewall_status()
    system_info['Antivirus Status'] = check_antivirus_status()

    return system_info

def check_firewall_status():
    if platform.system() == 'Windows':
        cmd = 'netsh advfirewall show allprofiles'
        try:
            firewall_status = subprocess.check_output(cmd, shell=True)
            return firewall_status.decode('utf-8')
        except subprocess.CalledProcessError:
            return "Firewall status could not be determined."
    else:
        return "Firewall status check not supported on this platform."

def check_antivirus_status():
    if platform.system() == 'Windows':
        cmd = 'wmic /namespace:\\\\root\\SecurityCenter2 path AntiVirusProduct get * /format:value'
        try:
            antivirus_info = subprocess.check_output(cmd, shell=True)
            return antivirus_info.decode('utf-8')
        except subprocess.CalledProcessError:
            return "Antivirus status could not be determined."
    else:
        return "Antivirus status check not supported on this platform."

def main():
    system_info = get_system_info()

    # Save system_info to a JSON file
    with open('system_info.json', 'w') as json_file:
        json.dump(system_info, json_file, indent=4)
    
    print("Machine Information from a Security Standpoint saved to system_info.json")
