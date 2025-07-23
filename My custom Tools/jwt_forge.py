import jwt

payload = {
    "username": "user",
    "admin": 1
}

key = "secret"
token = jwt.encode(payload, key, algorithm="HS256")
print(token)
