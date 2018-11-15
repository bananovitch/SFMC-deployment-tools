import requests, config, json, os

# prepare the target directory
if 'assets' not in os.listdir():
    os.makedirs('assets')



#get access token
def getToken(credentials):
   
    payload = {
        "clientSecret": credentials["clientSecret"],
        "clientId":credentials["clientId"]
    }
    
    print("Authenticating..")
    res = requests.post(credentials["authURL"], data=payload)
    res.raise_for_status()
    return json.loads(res.text)["accessToken"]
    print("Done.")



accessToken = getToken(config.home)

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
}

#write all the assets to a file - we might use this file as a backup source
print("Getting assets..")
baseURL = config.home["restBaseURL"]

res = requests.get(baseURL + 'asset/v1/content/assets', headers=headers)
res.raise_for_status()
print("Done.")

assetsJSON = res.text


targetFile = open('assets/assets.json', 'w', encoding="utf-8")
targetFile.write(assetsJSON)
targetFile.close()

print("downloading Cloud Pages..")
assetsList = json.loads(assetsJSON)["items"]
print(str(len(assetsList)) + " assets found.")

#prepare assets to be moved

landingPages = []
templateEmails = []
htmlEmails = []
uncrecognized = []


for asset in assetsList:
    assetType = asset["assetType"]["name"]
    if(assetType == "webpage"):
        landingPages.append(asset)
    elif(assetType == "templatebasedemail"):
        templateEmails.append(asset)
    elif(assetType == "htmlemail"):
        htmlEmails.append(asset)
    else:
        uncrecognized.append(asset)
 
#authenticate in target Business Unit
accessToken = getToken(config.target)

headers = {
    'content-type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
}

print("Target BU access token: " + accessToken)




