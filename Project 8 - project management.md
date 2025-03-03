# AWS Project Thread PM: Self-Hosted Project Management & Collaboration Platform for Military Operations

## Background & Military Application

Modern military operations demand seamless coordination, rapid decision-making, and secure communication—even in contested or isolated environments. Command centers and field units require a robust, self-hosted project management solution that ensures operational planning, mission coordination, and real-time collaboration without relying on external networks.

**Military Application Highlights:**
- **Secure Operational Planning:** Provides a self-hosted solution for planning, task assignment, and mission tracking.
- **Enhanced Collaboration:** Offers secure, in-house tools for communication and document management.
- **Resilient Infrastructure:** Operates on multi-cloud platforms (AWS and GCP) to ensure continuity during network disruptions.
- **Operational Efficiency:** Streamlines processes and reduces reliance on external systems.

## Technical Focus & Project Deployment

### Project Overview

This project deploys a Kubernetes-based project management suite distributed across AWS and GCP. Automation is handled via Ansible, and container images are sourced from [linuxserver.io](https://docs.linuxserver.io/images-by-category/).

### What the Project Deploys & How It Works

- **Project Management Application:**  
  - **Redmine** serves as the core tool for task assignment, issue tracking, and reporting.
- **Version Control & Collaboration:**  
  - **Gitea** is deployed for self-hosted Git repository services to manage code and documents.
- **Secure Messaging:**  
  - **Mattermost** offers robust, encrypted communication for teams.
- **Unified Dashboard:**  
  - **Ferdium** aggregates access to all tools into a single interface.

### Deployment Environment & Automation

- **Deployment Locations:**  
  - 4–5 Virtual Machines (3 on AWS EC2 and 1–2 on GCP Compute Engine).
- **Automation:**  
  - **Ansible** installs K3s and Docker on all nodes and deploys a Kubernetes management tool (Rancher, Portainer, or Lens) in a standalone Docker container.

## Role of Each Tool

### **AWS Services**
- **EC2** – Hosts the virtual machines for the project management cluster.
- **S3** – Stores project backups, documents, and demo recordings.
- **CodePipeline (Optional)** – Automates CI/CD for project updates.
- **SNS (Optional)** – Sends real-time alerts for operational events.
- **Lambda (Optional)** – Automates routine tasks like status updates.
- **CloudTrail (Optional)** – Monitors account activity for compliance.

### **Ansible**
- **Install K3s** on all nodes.
- **Install Docker** on the machine hosting the Kubernetes management tool.
- **Deploy Kubernetes management tool** (Rancher, Portainer, or Lens in a standalone Docker container).
- **Deploy all project management tools** (Redmine, Gitea, Mattermost, Ferdium) in Kubernetes.

### **Docker**
- **Runs the Kubernetes management tool** (Rancher, Portainer, or Lens) in a standalone container.

### **Redmine (Project Management Application)**
- **Centralizes task assignment and reporting** for military operations.
- **Tracks mission-critical issues** in a secure environment.
- **Facilitates structured planning** for deployments.

### **Ferdium (Unified Dashboard)**
- **Aggregates all project management services** into a single interface.
- **Provides centralized access** for managing tasks and communications.

## Recommended Workflow

```plaintext
1️⃣ Provision AWS EC2 & GCP VMs (via GUI)
2️⃣ Use Ansible to install K3s & Docker on all nodes
3️⃣ Deploy the Kubernetes management tool (Rancher, Portainer, or Lens) in a standalone Docker container via Ansible
4️⃣ Deploy Redmine, Gitea, Mattermost, and Ferdium in Kubernetes using linuxserver.io container images
5️⃣ Integrate AWS S3 for backups, document storage, and demo recordings
6️⃣ Deploy mandatory AWS services (EC2, S3) and select 3 additional AWS services (e.g., CodePipeline, SNS, Lambda)
7️⃣ Test and verify service accessibility via web browser and secure military networks
8️⃣ Record a project demo/video and upload it to S3
9️⃣ Optionally, secure remote access with Twingate or Tailscale
