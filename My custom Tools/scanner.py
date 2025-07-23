import requests
import re
import pyfiglet
import threading

def print_banner():
    banner = pyfiglet.figlet_format("Vulnerability Scanner \n by HammadTahir")
    print(banner)
    print("A simple tool to scan for SQL Injection and XSS vulnerabilities.\n")

payloads = {
    "SqlInjection": [
        "'", "' OR '1'='1", "\" OR \"1\"=\"1", "'; --", "' UNION SELECT 1,2,3 --"
    ],
    "XSS": [
        "<script>alert('XSS')</script>", "'><img src=x onerror=alert('XSS')>"
    ]
}

sqlerror = [ "SQL syntax","SQLite3::query():", "MySQL server", "syntax error", "Unclosed quotation mark", "near 'SELECT'",
    "Unknown column", "Warning: mysql_fetch", "Fatal error"]

def scan(vulnerability, payload, para):
    response = requests.get(url , params={f"{para}": payload})
    content = response.text.lower()
    if vulnerability == "SqlInjection" and any(error.lower() in content for error in sqlerror):
        print(f"[+] SQL Injection vulnerability found with payload: {payload}")
    elif vulnerability == "XSS" and payload.lower() in content:
        print(f"[+] XSS vulnerability found with payload: {payload}")

def main():
    print_banner()
    global url
    url = input("Enter the URL to scan (e.g., http://example.com): ")
    para = input("Enter the parameter to test for vulnerabilities (e.g., 'id'): ")
    threads = []
    for verlnerbility, payload_list in payloads.items():
        for payload in payload_list:
            t = threading.Thread(target=scan, args= (verlnerbility, payload, para))
            threads.append(t)
            t.start()
    for thread in threads:
        thread.join() 

if __name__ == "__main__":
    main()