import requests

#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file
url = "http://0.0.0.0:5000/setjson"
fin = open('/Users/yogev/Desktop/dept_info.json', 'rb')
files = {'file': fin}
try:
    r = requests.post(url, files=files)
    print r.text
finally:
	fin.close()