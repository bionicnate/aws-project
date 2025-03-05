# Workflow

## Provision VMs
    1. Created 3 AWS EC2 instances, 3 GCE VMs
        1. AWS needs a keypair to connect
        2. modified the sg inbound/outbound to accept TCP:22 
        3. added the AWS key to "authorized_hosts" in GCP for ease of use
    
## Install K3s & Docker w/Ansible
    1. ran a simple ping module and checked i could access over ssh
        1. made a vars file to differentiate master and node for k3s
            1. specify which hosts with --limit "*master" or "*nodes"
        2. realized i had to add the .pem to every playbook so i added a line in ansible.cfg "private_key_file = ~/.ssh/ec2.pem" 
    2. Grabbed previous created ansible playbook to install k3s
        1. ran into an issue where apt did not exist, the AMI used yum as a package manager whereas my GCP vm had apt
        2. plugged the script into gemini to configure playbook for conditional package manager between yum and apt
    3. 