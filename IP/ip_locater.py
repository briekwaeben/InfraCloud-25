import requests
import datetime
print("current date and time:")
print (datetime.datetime.now())
response = requests.get('https://api.myip.com/')
data = response.json()
print(type(data))
print(data)
ip_address = data.get('ip')
country = data.get('country')
country_code = data.get('cc')
print(f"Public IP Address: {ip_address}")
print(f"Country: {country}")
print(f"Country Code: {country_code}")