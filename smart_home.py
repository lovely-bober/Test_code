import requests

domoticz_url = "http://127.0.0.1:8080/json.htm"
idx = 4
command = input("On or Off: ").strip().capitalize() # Use "On" to turn on and "Off" to turn off

#Parameters for the lamp
params = {
    "type": "command",
    "param": "switchlight",
    "idx": idx,
    "switchcmd": command
}

auth = ('admin', 'domoticz') # Username and password

response = requests.get(domoticz_url, params=params, auth=auth)

print("Status code:", response.status_code)
print(response.json())