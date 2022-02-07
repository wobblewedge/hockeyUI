import requests

url = "https://api-hockey.p.rapidapi.com/odds/"

querystring = {"game":"1150"}

headers = {
    'x-rapidapi-key': "42bbe39c4emsh9a4350f5aa4928dp1f553cjsnd3ca22f4590d",
    'x-rapidapi-host': "api-hockey.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)