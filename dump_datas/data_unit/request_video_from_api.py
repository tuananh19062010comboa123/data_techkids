import requests
import json
def get_video_from_api():
    cred = {
        "email": "ed.techkidsvn@gmail.com",
        "password": "tradethecol@thanhcong",
        "returnSecureToken": True,
    }
    token = requests.post(
        "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyDCr7hmxHj8p8XYS5RJDCARR-uN5pRos68", data=cred)
    token = token.json()["idToken"]
    # print(token)
    s = requests.Session()
    data = json.dumps({"token": token})
    headers = {'Content-type': 'application/json'}

    # dev
    # auth = s.post("https://tk-lms-dev.herokuapp.com/api/v1/auth",
    #             data=data, headers=headers)
        # product
    auth = s.post("https://lm.techkids.vn/api/v1/auth",
                data=data, headers=headers)

    # print(auth.json())
    # dev
    # videos_list = s.get("https://tk-lms-dev.herokuapp.com/api/v1/researcher/videos?_start=0&_end=824",headers=headers)
        # product
    videos_list = s.get("https://lm.techkids.vn/api/v1/researcher/videos?_start=0&_end=824",headers=headers)

    # print(videos_list.json())
    videos_list = list(videos_list.json())
    # print(type(videos_list))
    # print(len(videos_list))
    # print(videos_list[0])
    return videos_list

# x = get_video_from_api()
# print(x[0])
# get_video_from_api()