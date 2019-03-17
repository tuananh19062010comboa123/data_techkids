import logging as users_log
import requests
import json
from model import Video

list_users = [{
    "email": u.email,
    "password": "codethechange",
    "name": {
        "firstName": u.lastName,
        "lastName": u.firstName
    },
    "role": "member"}
    for u in Users.objects]


#login from firebase
cred = {
    "email": "ed.techkidsvn@gmail.com",
    "password": "tradethecol@thanhcong",
    "returnSecureToken": True,
}
token = requests.post(
    "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAcO90C2hCz0QM3gJk1z7_DDgLTVqet-Lo", data=cred)

token = token.json()["idToken"]

data = json.dumps({"token": token})#convert dict to json

s = requests.Session()
headers = {'Content-type': 'application/json'}

#login sẵn
auth = s.post("https://tk-id-service-2.herokuapp.com/api/v1/auth",
              data=data, headers=headers)


LOG_USER = "users.log"
users_log.basicConfig(handlers=[users_log.FileHandler(LOG_USER, 'w', 'utf-8')],
                      level=users_log.INFO,
                      format='%(asctime)s %(message)s',
                      datefmt='%d/%m/%Y %H:%M:%S')

for i, v in enumerate(list_users):
  post = s.post("https://tk-id-service-2.herokuapp.com/api/v1/users",
                data=json.dumps(v), headers=headers)
  print("creating", v["name"])
  if post.status_code not in [200, 201, 202]:
    users_log.info(f"""
      {post.text}
      at user: 
      {i}
      {v["email"]}
      {v["name"]["firstName"]} {v["name"]["lastName"]} 
        """)
