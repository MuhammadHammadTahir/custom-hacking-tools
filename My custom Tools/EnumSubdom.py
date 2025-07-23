import sys
import requests
import pyfiglet
import threading

def print_banner():
    banner = pyfiglet.figlet_format("EnumSubDom \n by HammadTahir")
    print(banner)
    print("A simple tool to enumerate subdomains.\n")

def get_subdomains(protocol ,domain, subdomain_list):
    sub_domains_fond = []
    for subdom in subdomain_list:
        msg = print(f"checking: {subdom}.{domain}")
        if protocol == "http":
            url = f"http://{subdom}.{domain}"
        elif protocol == "https":
            url = f"https://{subdom}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        except Exception as e:
            print(f"[!] Unexpected error: {e}")
        else:
            print(f"[+]subdomain found: {url}")
            sub_domains_fond.append(url)
    if len(sub_domains_fond) > 0:
        print(f"\n[+] Found {len(sub_domains_fond)} subdomains:")
        for sub in sub_domains_fond:
            print(sub)

def sub_domain_chunks(subdomain_list, chunk_size=10):
    #Yield successive n-sized chunks from subdomain_list.
    for i in range(0, len(subdomain_list), chunk_size):
        yield subdomain_list[i:i + chunk_size]    

def main():
    if len(sys.argv) !=4:
        print("Usage: python EnumSubdom.py <protocol> <domain> <subdomain_list_file>")
        sys.exit(1)
    else:
        print_banner()
        protocol = sys.argv[1].lower()
        if protocol not in ["http", "https"]:
            print("Protocol must be either 'http' or 'https'.")
            sys.exit(1)
        domain = sys.argv[2]
        subdomins_file = sys.argv[3]
        try:
            file = open(subdomins_file,"r")
            subdomain_list_dirty = file.readlines()
            subdomain_list_clean = [sub.strip() for sub in subdomain_list_dirty]
            
            threads = []
            for chunk in sub_domain_chunks(subdomain_list_clean, chunk_size=10):
                t = threading.Thread(target=get_subdomains, args=(protocol, domain, chunk))
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()
            get_subdomains(protocol,domain, subdomain_list_clean)
        except FileNotFoundError:
            print(f"File {subdomins_file} not found.")
            sys.exit(1) 

if __name__ == "__main__":
    main()
