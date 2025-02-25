import requests

srv = "http://127.0.0.1:5000"

print("Creating account 'elaina' with password 'abc123'")
print(requests.post(srv + "/create", json = {
    'username': 'elaina',
    'password': 'abc123',
}).json())
print("")

print("Logging in to account 'elaina' with password 'abc123'")
print(requests.post(srv + "/login", json = {
    'username': 'elaina',
    'password': 'abc123',
}).json())
print("")

print("Changing password for account 'elaina' to 'pineapple'")
print(requests.post(srv + "/change", json = {
    'username': 'elaina',
    'password': 'abc123',
    'new_password': 'pineapple',
}).json())
print("")

print("Logging in to account 'elaina' with *old* password 'abc123'")
print(requests.post(srv + "/login", json = {
    'username': 'elaina',
    'password': 'abc123',
}).json())
print("")

print("Logging in to account 'elaina' with new password 'pineapple'")
print(requests.post(srv + "/login", json = {
    'username': 'elaina',
    'password': 'pineapple',
}).json())
print("")

print("Creating account 'joe' with password 'apple'")
print(requests.post(srv + "/create", json = {
    'username': 'joe',
    'password': 'apple',
}).json())
print("")

print("Logging in to account 'joe' with password 'apple'")
print(requests.post(srv + "/login", json = {
    'username': 'joe',
    'password': 'apple',
}).json())
print("")
