import requests
import json

#Request broke, needs fixed. I didn't had time this week or I would have.
url = "https://api-hockey.p.rapidapi.com/teams/statistics/"

querystring = {'league':'3', 'season':'2021', 'team':'17'}

headers = {
    'x-rapidapi-host': "api-hockey.p.rapidapi.com",
    'x-rapidapi-key': "42bbe39c4emsh9a4350f5aa4928dp1f553cjsnd3ca22f4590d"
    }

response = requests.get(url, headers=headers, params=querystring).json()

print(response)