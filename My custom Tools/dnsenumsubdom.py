import pyfiglet
import dns.resolver
import threading

def print_banner():
    banner = pyfiglet.figlet_format("DNS Enum Subdomains\nby HammadTahir")
    print(banner)
    print("A simple tool to enumerate subdomains using DNS queries.\n")

valid_domains = []

def enumerate_subdomains(target_domain, subdomain_list):
    for subdomain in subdomain_list:
        full_url= f"{subdomain}.{target_domain}"
        print(f"[*] Checking {full_url}")

        try:
            response = dns.resolver.resolve(full_url, 'A')
            if response:
                print(f"[+] Valid subdomain found: {full_url}")
                valid_domains.append(full_url)
        except dns.resolver.NoAnswer:
                pass
        except dns.resolver.NXDOMAIN:
                pass
        except dns.resolver.Timeout:
                pass
        except Exception as e:
            pass
    

def list_chnker(lst, chunk_size=50):
    for i in range (0, len(lst), chunk_size):
        yield lst[i:i+chunk_size]

def main():
    print_banner()
    target_domain = input("Enter the target domain: ")
    subdomain_list = input("Enter the path to the subdomain list file: ")
    list = open(subdomain_list, 'r').readlines()
    list = [x.strip() for x in list if x.strip()]
    threads = []

    for chunk in list_chnker(list, chunk_size=50):
        t = threading.Thread(target=enumerate_subdomains, args=(target_domain, chunk))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    print("\n[+] Valid subdomains found:")
    for domain in valid_domains:
        print(domain)

if __name__ == "__main__":
    main()