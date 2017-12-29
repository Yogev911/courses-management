import urllib, json
url = "https://yogev-test1.herokuapp.com/getjson"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
