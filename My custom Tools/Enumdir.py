import sys,requests, threading, pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("EnumDir \n by HammadTahir")
    print(banner)
    print("A simple tool to enumerate directories.\n")


def chunker(wordlist, chunk_size=10):
    """Yield successive n-sized chunks from wordlist."""
    for i in range(0, len(wordlist), chunk_size):
        yield wordlist[i:i+chunk_size]

def check_directory(url, word_list):
    for word in word_list:
        full_url = f"{url}/{word}"
        try: 
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"[+] Directory found: {full_url}")
            elif response.status_code == 403:
                print(f"[-] Forbidden: {full_url}")
            elif response.status_code == 404:
                print(f"[-] Not Found: {full_url}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Error accessing {full_url}: {e}")

def main():
    if len(sys.argv) !=3:
        print("Usage: python EnumDir.py <url> <wordlist_file>")
        sys.exit(1)
    else:
        print_banner()
        url = sys.argv[1]
        wordlist_file = sys.argv[2]
        try:
            with open(wordlist_file, "r") as file:
                wordlist = file.readlines()
                wordlist = [word.strip() for word in wordlist]
        except FileNotFoundError:
            print(f"[!] Wordlist file '{wordlist_file}' not found.")
            sys.exit(1)

        threads = []
        for word_list in chunker(wordlist, chunk_size=10):
            t = threading.Thread(target=check_directory, args=(url, word_list))
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()



if __name__ == "__main__":
    main()
