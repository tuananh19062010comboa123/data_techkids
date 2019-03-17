import logging as fix_users
import requests
import json
from model import Users


# login
cred = {
    "email": "ed.techkidsvn@gmail.com",
    "password": "tradethecol@thanhcong",
    "returnSecureToken": True,
}
token = requests.post(
    "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAcO90C2hCz0QM3gJk1z7_DDgLTVqet-Lo", data=cred)
token = token.json()["idToken"]
# print(token)
s = requests.Session()
data = json.dumps({"token": token})
headers = {'Content-type': 'application/json'}
auth = s.post("https://tk-id-service-2.herokuapp.com/api/v1/auth",
              data=data, headers=headers)


# search_user = s.get(f"https://tk-id-service-2.herokuapp.com/api/v1/users?q={u.email}")
# admin@gmail.com


list_users = [{
    "email": u.email,
    "password": "codethechange",
    "name": {
        "firstName": u.lastName,
        "lastName": u.firstName
    },
    "role": "member"}

    for u in Users.objects]
        
LOG_USER = "fix_users.log"
fix_users.basicConfig(handlers=[fix_users.FileHandler(LOG_USER, 'w', 'utf-8')],
                             level=fix_users.INFO,
                             format='%(asctime)s %(message)s',
                             datefmt='%d/%m/%Y %H:%M:%S')
for i in range(len(list_users)):
    if i >= 0:
        full_email = list_users[i]["email"]
        email = list_users[i]["email"].split('@')[0]
        # print(email)
        search_user = s.get(
            f"https://tk-id-service-2.herokuapp.com/api/v1/users?q={email}")
        search_user = search_user.json()
        if not search_user : 
            # print("ahihi")
            fix_users.info(f"{full_email}")

        # print(type(search_user))
        # print(search_user)
        else:
            id = search_user[0]["_id"]
            print(id)

            new_data = {
                "email": list_users[i]["email"],
                "password": "codethechange",
                "name": {
                    "firstName": list_users[i]["name"]["firstName"],
                    "lastName": list_users[i]["name"]["lastName"]
                },
                "role": "member"}

            # print(new_data)

            headers = {'Content-type': 'application/json'}
            users = s.put(
                f"https://tk-id-service-2.herokuapp.com/api/v1/users/{id}", data=json.dumps(new_data), headers=headers)
            # print(users.json())

            fix_users.info(f"{id}")

        # if i == 3:
        #     break

# {search_user.text}
#     at user: 
# {v["email"]}
# {v["name"]["firstName"]} {v["name"]["lastName"]} 

# minhduc.096.99@gmail.com

# for i in range(len(list_users)):
#     # email = "trungheo100"
#     email = list_users[i]['email'].split('@')[0]
#     print(email)
#     search_user = s.get(f"https://tk-id-service-2.herokuapp.com/api/v1/users?q={email}")
#     # print(search_user.json())
#     search_user = search_user.json()

#     # id = search_user[0]["_id"]
#     # print(id)
#     # print(search_user)
#     print(search_user)
#     break

# data = {
#     "email": search_user[0]["email"],
#     "password": "codethechange",
#     "name": {
#         "firstName": search_user[0]["name"]["lastName"],
#         "lastName": search_user[0]["name"]["firstName"]
#     },
#     "role": "member"}
# print(data)

# users = s.put(f"https://tk-id-service-2.herokuapp.com/api/v1/users/{id}", data)
# users = list(users.json())


# print(type(users))
# print(users)

# print(users.json()[0])


# fix name


# update user


# https://tk-id-service-2.herokuapp.com/
