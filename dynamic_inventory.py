#!/usr/bin/env python3

import subprocess
import json
import socket
import ipaddress

def get_local_subnet():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    subnet = ipaddress.IPv4Network(local_ip + '/24', strict=False)
    return str(subnet)

def discover_hosts(subnet):
    try:
        result = subprocess.run(["nmap", "-sn", subnet], capture_output=True, text=True)
        hosts = []
        for line in result.stdout.splitlines():
            if "Nmap scan report for" in line:
                ip = line.split()[-1]
                hosts.append(ip)
        return hosts
    except Exception as e:
        print(f"Error scanning network: {e}")
        return []

def generate_inventory(hosts):
    inventory = {
        "workstations": {
            "hosts": hosts
        },
        "_meta": {
            "hostvars": {ip: {} for ip in hosts}
        }
    }
    print(json.dumps(inventory, indent=2))

if __name__ == "__main__":
    subnet = get_local_subnet()
    live_hosts = discover_hosts(subnet)
    generate_inventory(live_hosts)
