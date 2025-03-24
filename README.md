# Ubuntu Hardening

Ansible role to **harden Ubuntu workstations** for cybersecurity competitions.

![Lint](https://github.com/jgordoMsu/ubuntu-hardening/actions/workflows/ansible-lint.yml/badge.svg)

---

## 🔐 Features
- Firewall (UFW) with SSH allowed
- Fail2Ban for brute-force protection
- AppArmor enforced for access control
- Unattended security updates
- Password policy enforcement
- Lynis security audit
- Dynamic host discovery with `nmap`

---

## 📂 Project Structure
```
ubuntu-hardening/
├── dynamic_inventory.py         # Discovers IPs on local subnet
├── playbook.yml                 # Root playbook calling the hardening role
├── roles/
│   └── ubuntu_hardening/        # Main Ansible role
│       ├── tasks/main.yml
│       ├── defaults/main.yml
│       ├── handlers/main.yml
│       └── README.md
├── .github/workflows/ansible-lint.yml  # GitHub Actions workflow
├── .gitignore
└── README.md
```

---

## 🚀 How to Run the Role

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-TEAM/ubuntu-hardening.git
cd ubuntu-hardening
chmod +x dynamic_inventory.py
```

### 2. Install Required Tools (Control Node)
```bash
sudo apt update
sudo apt install -y ansible nmap python3
ansible-galaxy collection install community.general
```

### 3. Run the Playbook
```bash
ansible-playbook playbook.yml -i ./dynamic_inventory.py
```

This will:
- Discover all reachable IPs on your subnet
- Apply security hardening tasks to each Ubuntu host

---

## 🔎 Verification on Target Machines
SSH into any hardened machine and verify:
```bash
sudo ufw status
sudo systemctl status fail2ban
sudo cat /etc/fail2ban/jail.local
sudo cat /var/log/lynis-report.dat
```

---

## 🧪 GitHub Actions Linting
Every push triggers `ansible-lint` via GitHub Actions. 
Check the **Actions tab** in your repo for results.

---

## 🧱 Extend the Role
Optional hardening add-ons:
- Disable USB ports
- Add login banners
- Harden cron jobs and scheduled tasks
- Configure custom auditd rules

