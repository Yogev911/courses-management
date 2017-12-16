import requests

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
url = "http://127.0.0.1:8674/compare"
fin = open('/Users/yogev/Desktop/test1.xls', 'rb')
files = {'file': fin}
try:
    r = requests.post(url, files=files)
    print r.text
finally:
	fin.close()