#!/usr/bin/env python3

import yaml
import json
import os

def load_vms_from_yaml(filepath):
    """Loads VM IPs from a YAML file."""
    try:
        with open(filepath, 'r') as file:
            data = yaml.safe_load(file)
        return data.get('vm_ips', {})
    except FileNotFoundError:
        return {}

def generate_inventory(vms):
    """Generates Ansible inventory from VM IPs."""
    inventory = {
        'all': {
            'hosts': [],
            'vars': {}
        },
        '_meta': {
            'hostvars': {}
        }
    }

    for cloud_provider, hosts in vms.items():
        for hostname, host_data in hosts.items():
            full_hostname = f"{cloud_provider}-{hostname}"
            inventory['all']['hosts'].append(full_hostname)
            inventory['_meta']['hostvars'][full_hostname] = {
                'ansible_host': host_data['ip'],
                'ansible_user': host_data['user']
            }

    return inventory

if __name__ == '__main__':
    vms_filepath = 'vars/vms.yml'
    vms = load_vms_from_yaml(vms_filepath)
    inventory = generate_inventory(vms)

    print(json.dumps(inventory, indent=4))