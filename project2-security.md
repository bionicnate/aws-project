# AWS Project Thread 2: Multi-Cloud K3s Cluster for Secure Operations & Threat Intelligence  

## Scenario: Security Operations & Threat Intelligence Platform  

### Background  
Your company, **Cyber Sentinel Solutions (CSS)**, has been contracted by **Unified Cyber Defense (UCD)** to develop a **self-hosted, multi-cloud security operations platform**. The platform must:  

- **Detect & Monitor Threats** – Deploy a **SIEM** to collect and analyze security logs.  
- **Perform Active Security Testing** – Include **Kali Linux** for penetration testing and adversary emulation.  
- **Secure Internal Communication** – Deploy a **self-hosted encrypted messaging service** for security teams.  
- **Manage Secure Code & Infrastructure** – Include a **self-hosted Git repository** for infrastructure-as-code and automation.  
- **Provide a Unified Dashboard** – Centralized access to security tools via a **browser-based security dashboard**.  

UCD requires this solution to be **deployed across AWS and GCP**, **self-hosted for data privacy**, and **fully automated with Ansible**.  

---

## Project Requirements  

### ✅ Deploy 4-5 Virtual Machines *(via AWS & GCP GUI)*  
- **3 in AWS** (EC2 instances)  
- **1-2 in GCP** (Compute Engine VMs)  

### ✅ Use Ansible to Automate  
- **Install K3s & Docker** on all nodes.  
- **Deploy Kubernetes management tool** in Docker (Rancher, Portainer, or Lens).  
- **Deploy all security services in K3s**.  

### ✅ Deploy & Expose the Following Security Services *(Accessible via Browser)*  
- **Kubernetes Management Tool** *(Rancher, Portainer, or Lens in Docker)*.  
- **Wazuh SIEM** *(Security monitoring, log analysis, and endpoint detection)*.  
- **Kali Linux VM** *(Dedicated penetration testing & adversary emulation environment)*.  
- **Mattermost** *(Self-hosted, encrypted messaging for SOC teams)*.  
- **Forgejo** *(Self-hosted Git repository alternative for security infrastructure-as-code)*.  
- **Ferdium** *(Integrated dashboard for all tools in a single interface)*.  

### ✅ Integrate AWS Services *(Mandatory: EC2, S3, and one additional AWS tool)*  
- **EC2** – Deploy virtual machines for the security operations cluster.  
- **S3** – Secure storage for log data, incident reports, and security documentation.  
- **Third AWS Tool (Choose One)**:  
  - **AWS GuardDuty** – Threat detection and continuous monitoring.  
  - **AWS Security Hub** – Centralized security compliance and event monitoring.  
  - **AWS CloudWatch** – Log monitoring and alerting.  

### ✅ Upload & Access Demo Content  
- **Record a project demo/video** and upload to an **S3 bucket**.  
- **Ensure all security logs, reports, and dashboards are functional**.  

### ✅ *(Optional)* Secure Remote Access with Twingate  
- **If required, implement Twingate for access control**.  

---

## Role of Each Tool  

### **AWS Services**  
- **EC2** – Hosts 3 virtual machines for the security cluster.  
- **S3** – Stores security logs, reports, and penetration testing results.  
- **Third AWS Tool** – Adds **threat detection, monitoring, or compliance functionality** (student’s choice).  

### **Ansible**  
- **Install K3s** on all nodes.  
- **Install Docker** on the machine hosting the Kubernetes management tool.  
- **Deploy Kubernetes management tool** in Docker (Rancher, Portainer, or Lens).  
- **Deploy all security tools** (Wazuh, Kali Linux, Mattermost, Forgejo, Ferdium) in Kubernetes.  

### **Docker**  
- **Runs the Kubernetes management tool** *(Rancher, Portainer, or Lens) in a standalone container*.  

### **Kali Linux** *(Security Testing & Adversary Simulation)*  
- **Performs penetration testing against deployed services**.  
- **Simulates real-world attack scenarios to validate security controls**.  
- **Runs security tools like Metasploit, Nmap, Wireshark, and Burp Suite**.  

### **Ferdium (Security Operations Dashboard)**  
- **Aggregates all security-related services** into a single interface.  
- **Provides a centralized view for SOC analysts** to monitor and manage security incidents.  

---

## Recommended Workflow  
![Multi-Cloud K3s Deployment Workflow](images/project2.png)
```plaintext
1️⃣ Provision AWS EC2 & GCP VMs (via GUI)
2️⃣ Use Ansible to install K3s & Docker
3️⃣ Deploy Kubernetes management tool (Rancher, Portainer, Lens in Docker)
4️⃣ Deploy Wazuh, Kali Linux, Mattermost, Forgejo, and Ferdium in Kubernetes (via Ansible)
5️⃣ Integrate AWS S3 for log storage and security reports
6️⃣ Deploy additional AWS security feature (GuardDuty, Security Hub, or CloudWatch)
7️⃣ Test & verify all security tools via browser
8️⃣ Screen record demo & upload to S3
9️⃣ Secure remote access via Twingate (Optional)
