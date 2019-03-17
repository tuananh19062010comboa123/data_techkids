import logging as videos_log
import requests
import json
from model import Videos

#login from firebase
cred = {
    "email": "ed.techkidsvn@gmail.com",
    "password": "tradethecol@thanhcong",
    "returnSecureToken": True,
}
token = requests.post(
    "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAcO90C2hCz0QM3gJk1z7_DDgLTVqet-Lo", data=cred)
token = token.json()["idToken"]




list_videos = []

for v in Videos.objects:
  data = {
      "title": v.title,
      "description": v.description,
      "videoInfo": {
          "videoId": v.videoId,
          "type": v.source,
          "duration": v.duration
      },
  }
  if not data["videoInfo"]["type"]:
    data["videoInfo"]["type"] = "youtube"
  elif data["videoInfo"]["type"] == "internal":
    data["videoInfo"]["type"] = "upload"
  list_videos.append(data)



#log
LOG_VIDEOS = "videos.log"
videos_log.basicConfig(filename=LOG_VIDEOS, level=videos_log.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
s = requests.Session()
data = json.dumps({"token": token})
headers = {'Content-type': 'application/json'}
auth = s.post("https://tk-lms-dev.herokuapp.com/api/v1/auth",
              data=data, headers=headers)

for i, v in enumerate(list_videos):
  post = s.post("https://tk-lms-dev.herokuapp.com/api/v1/researcher/videos",
                data=json.dumps(v), headers=headers)
  print("creating", v["title"])
  if post.status_code not in [200, 201, 202]:
    videos_log.error(f"""
    {post.text}
    at video: 
    {i}
    {v["title"]}, 
    {v["videoInfo"]}
    """)
    videos_log.error("-"*100)
