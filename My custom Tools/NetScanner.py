from scapy.all import *
import sys, threading, pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("NetScanner \n by HammadTahir")
    print(banner)
    print("A simple tool to scan networks for live hosts.\n")

def scan_network(interface, network, broadcast_MAC):

    print(f"Scanning network {network} on interface {interface}...")

    packet = Ether(dst=broadcast_MAC) / ARP(pdst=network)
    ans, unans = srp(packet, iface=interface, timeout=2, verbose=False)

    for sent, received in ans:
        print (received.sprintf(r"%Ether.src% - %ARP.psrc%")) 
    
    


def main():
    if(len(sys.argv) != 3):
        print("Usage: python NetScanner.py <interface> <network/subnet> ")
        sys.exit(1)
    else:
        print_banner()
        interface = sys.argv[1]
        network = sys.argv[2]
        broadcast_MAC = "ff:ff:ff:ff:ff:ff"
        try:
            scan_network(interface, network, broadcast_MAC)
        except Exception as e:
            print(f"[!] Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()