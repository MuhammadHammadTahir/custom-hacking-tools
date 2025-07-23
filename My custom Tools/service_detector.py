import socket
import threading
import sys
import pyfiglet


open_ports_services = []
def print_banner():
    banner = pyfiglet.figlet_format("PortScanner \n by HammadTahir")
    print(banner)
    print("A simple tool to scan ports on a target host.\n")


def ports_chunker(target_ports, chunk_size=100):
    """Yield successive n-sized chunks from target_ports."""
    for i in range(0, len(target_ports), chunk_size):
        yield target_ports[i:i + chunk_size]

def service_detection(host, port_range):
    for port in port_range:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')

                banner = sock.recv(1024)
                service_info = f"{host}:{port} --> {banner}"
                print(f"[+] {service_info}")
                open_ports_services.append(service_info)
            else:
                print(f"[-]Port {port} is closed")
            sock.close()    
        except Exception as e:
            print(f"Error scanning port {port}: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python PortScanner.py <target_host>")
        sys.exit(1)
    else:
        print_banner()
        target_host =sys.argv[1]
        target_ports = range(1, 65535)

        threads = []
        for chunk in ports_chunker(target_ports, chunk_size=100):
            t = threading.Thread(target=service_detection, args=(target_host, chunk))
            threads.append(t)
            t.start()
        for t in threads:   
            t.join()

        print(f"\n[+] Open ports on {target_host}: {open_ports_services}\n")



if __name__ == "__main__":
    main()
