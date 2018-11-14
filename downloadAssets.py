import requests, config, json, io

payload = {
    "clientSecret": config.accessConfig["clientSecret"],
    "clientId":config.accessConfig["clientId"]
}
#get access token
print("Authenticating..")
res = requests.post(config.accessConfig["authURL"], data=payload)
res.raise_for_status()
accessToken = json.loads(res.text)["accessToken"]
print("Done.")
headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
    }

#Get assets and write them to file
print("Getting assets..")
baseURL = config.accessConfig["restBaseURL"]

res = requests.get(baseURL + 'asset/v1/content/assets', headers=headers)
res.raise_for_status()
print("Done.")

assets = res.text
targetFile = open('assets.json', 'w', encoding="utf-8")
targetFile.write(assets)
targetFile.close()

