import requests

ip = input("Enter an IP address to query: \n")

url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

headers = {"accept": "application/json", "x-apikey": "api-key-here"}

response = requests.get(url, headers=headers)

print(response.text)