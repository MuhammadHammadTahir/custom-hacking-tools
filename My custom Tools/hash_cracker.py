import hashlib
import pyfiglet
import threading

def print_banner():
    banner = pyfiglet.figlet_format("Hash Cracker \n by HammadTahir")
    print(banner)
    print("A simple tool to crack hashes using a wordlist.\n")

def list_chunker(target_list, chunk_size=100):
    """Yield successive n-sized chunks from target_list."""
    for i in range(0, len(target_list), chunk_size):
        yield target_list[i:i + chunk_size]

def crack_hash(hash_to_crack, wordlist_chunk):
    for word in wordlist_chunk:
        word = word.strip()
        if hashlib.md5(word.encode()).hexdigest() == hash_to_crack:
            print(f"[+] Found: {word} for hash {hash_to_crack}")
            return word
    return None




def main():
    print_banner()
    
    hash_to_crack = input("Enter the hash to crack (MD5): ").strip()
    wordlist_file = input("Enter the path to the wordlist file: ").strip()

    try:
        with open(wordlist_file, 'r') as file:
            wordlist = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {wordlist_file} does not exist.")
        return

    threads = []
    for chunk in list_chunker(wordlist, chunk_size=100):
        t = threading.Thread(target=crack_hash, args=(hash_to_crack, chunk))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Hash cracking process completed.")


if __name__ == "__main__":
    main()