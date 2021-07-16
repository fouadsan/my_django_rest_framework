import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2NDczNTM3LCJqdGkiOiIwM2UwZDMxZjM1N2M0Mzg3YjI2MGM1YzU1NTQ5ZDdjOCIsInVzZXJfaWQiOjF9.qgH34SNh5ANEO29JPAu7I9-_GXGN_ixg6WkgPB_B29Q'
# credentials = {
#     'username': '***',
#     'password': '***'
# }
req = requests.get('http://127.0.0.1:8000/languages/', headers=headers)

print(req.text)
