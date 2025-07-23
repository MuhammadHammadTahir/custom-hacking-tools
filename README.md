# 🔧 CUSTOM-HACKING-TOOLS

A custom-built collection of Python-based hacking tools crafted to automate and enhance security assessments — including enumeration, brute force, JWT forging, network recon & exploitation — enabling security professionals to perform tasks more effectively and efficiently.

> ⚙️ **Fast Performance:** Built using multithreading for speed  
> 🧪 **Project-Origin:** Originally developed for a personal penetration testing project  
> 🚀 **Open Source:** Now shared for learning, ethical use, and collaboration

---

## 📚 Table of Contents

- [Overview](#overview)  
- [Tools Included](#tools-included)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Testing](#testing)  
- [Disclaimer](#disclaimer)  

---

## 🧠 Overview

**CUSTOM-HACKING-TOOLS** is a versatile collection of Python scripts designed to automate and streamline security-related tasks for red team operations and penetration testers.

These tools cover:
- 🔍 Subdomain/Directory Enumeration
- 🔑 Brute Force (SSH/Web/Custom)
- 🌐 Network & Port Scanning
- 🧾 JWT Forging
- 🖥️ Keylogging
- ⚙️ Service Fingerprinting

All tools are written in Python and leverage **multi-threading** to significantly reduce runtime and improve performance during scans and attacks.

---

## 🧰 Tools Included

| Script                  | Purpose |
|------------------------|---------|
| `Enumdir.py`           | Directory enumeration |
| `EnumSubdom.py`        | Subdomain enumeration |
| `dnsenumsubdom.py`     | DNS-based subdomain discovery |
| `NetScanner.py`        | Basic network scanner for live hosts|
| `portscanner.py`       | Multi-threaded port scanner |
| `scanner.py`           | Vernability scanning utility |
| `service_detector.py`  | Detect running services on open ports |
| `SSH_Brute_Force.py`   | SSH brute force login |
| `brute_force.py`       | General brute force script |
| `brute_force_2.py`     | Variation of brute force attack |
| `hash_cracker.py`      | Crack hashes using a wordlist |
| `jwt_forge.py`         | Create/forge JWTs manually |
| `keylogger_server.py`  | Server to receive keylogger data |
| `keyloggar.py`         | Lightweight keylogger |
| `key_replayer.py`      | Replay captured keystrokes |
| `downloader.py`        | Remote file downloader |
| `downloaded_file`      | File used for testing download functionality |
| `hak5.txt`, `wordlist2.txt` | Wordlists for cracking/brute force |

---

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure you have the following installed:

- Python 3.x
- Git
- [Optional] `venv` for isolated environments

---

### 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/custom-hacking-tools.git
Navigate to the project directory:

cd custom-hacking-tools
Install required dependencies:

pip install -r requirements.txt
Note: Most tools rely only on built-in Python libraries. If a specific tool requires additional modules, it will be mentioned in the script comments.

💡 Usage
Each tool can be executed individually:

python3 tool_name.py

python3 portscanner.py
You can edit the files directly to modify target IPs, ports, and settings as needed.

🧪 Testing
You can test tools locally using:

Vulnerable VMs (e.g., Metasploitable2, DVWA)

Custom-built test environments

Important: Never test these tools against unauthorized systems or networks. Use only in controlled and legal environments.

⚠️ Disclaimer
This project is provided for educational and ethical penetration testing purposes only.

❌ I do not condone illegal activities.

✅ Always seek permission before testing or scanning any systems.

By using this toolset, you agree to take full responsibility and ensure ethical usage.
