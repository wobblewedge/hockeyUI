from http import client

conn = client.HTTPSConnection("api-hockey.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-hockey.p.rapidapi.com",
    'x-rapidapi-key': "42bbe39c4emsh9a4350f5aa4928dp1f553cjsnd3ca22f4590d"
    }

conn.request("GET", "/teams/statistics/?league=1&season=2021&team=12", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))