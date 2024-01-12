import requests

# Replace these variables with your actual AlienVault OTX API key and the IP address you want to query
api_key = ""
ip_address = ""
sections = ["reputation", "geo", 'malware', 'url_list', 'passive_dns']  # Replace with the desired section

for section in sections:
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip_address}/{section}"
    headers = {'X-OTX-API-KEY': api_key}
    response = requests.get(url, headers=headers)
    print(f"Results for {section}:\n")
    print(response.text)
    print("\n")