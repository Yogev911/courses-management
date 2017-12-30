import requests

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
url = "https://shenkar-se.herokuapp.com/setjson"
fin = open('/Users/yogev/Desktop/test1.xls', 'rb')
files = {'file': fin}
try:
    r = requests.post(url, files=files)
    print r.text
finally:
	fin.close()