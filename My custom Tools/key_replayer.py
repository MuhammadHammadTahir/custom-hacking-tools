import keyboard
import pyfiglet

print(pyfiglet.figlet_format("Key Replayer \n by HammadTahir"))
print("A simple tool to record and replay keyboard events.\n")

print("Recording ...... Press 'Enter' to finish.")
keys = keyboard.record(until="enter")
if keys and keys[-1].name == 'enter':
    keys = keys[:-1]

print("Recording finished. Playing back the recorded keys...")
keyboard.play(keys)