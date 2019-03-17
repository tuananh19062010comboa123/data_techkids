import logging as unit_listss
from mongoengine import *
from request_video_from_api import get_video_from_api

import requests
import json
connect("tk-lms")


# Videos
class Videos(Document):
    meta = {
        "strict": False
    }
    _id = StringField()
    title = StringField()
    videoId = StringField()
    source = StringField()

    def json(self):
        return {
            "_id": self._id,
            "title": self.title,
            "videoId": self.videoId,
            "source": self.source,
        }


videos_list = [{
    "_id": u._id,
    "title": u.title,
    "videoId": u.videoId,
    "source": u.source
}
    for u in Videos.objects]

# print(videos_list[0])
# Playlists


class Playlists(Document):
    meta = {
        "strict": False
    }
    title = StringField()
    videos = StringField()
    keyword = StringField()
    typePlaylist = StringField()
    # videos = ListField(ReferenceField(Videos))

    def json(self):
        return {
            "title": self.title,
            "videos": self.videos,
            "keyword": self.keyword,
            "typePlaylist": self.typePlaylist
        }


list_play_lists = [
    {
        "title": u.title,
        "videos": u.videos,
        "keyword": u.keyword,
        "typePlaylist": u.typePlaylist
    }
    for u in Playlists.objects]

# print("list_play_lists : ",len(list_play_lists))

# print(list_play_lists[0])
unit_list = []
for i in range(len(list_play_lists)):
    unit = {
        "title": list_play_lists[i]["title"],  # playlist
        "type": list_play_lists[i]["typePlaylist"],  # playlist
        "description": "from lms",
        "documentRefs": [],
        "exerciseRefs": [],
        "videoRefs": ""
    }
    unit_list.append(unit)

# print(unit_list[0])
video_from_api = get_video_from_api()
# print(video_from_api[0])


# print(list_play_lists[0]["videos"][0].id)

# save_videoId_list = [] # list videoID from vodes lms

# print(len(list_play_lists))
save_videoId_list_final = []
save_id_lms_dev_list_final = []
for i in range(len(list_play_lists)):
    # print(list_play_lists[i]["videos"])
    save_videos_list = list_play_lists[i]["videos"]  # list
    # print(save_videos_list)
    save_videoId_list = []

    save_id_lms_dev_list = []
    for i in range(len(save_videos_list)):
        for k in range(len(videos_list)):  # videos_list

            if str(save_videos_list[i]) == str(videos_list[k]["_id"]):

                # lay ra videoId tu videos_list
                save_videoId_list.append(videos_list[k]["videoId"])

                videoId = videos_list[k]["videoId"]
                # print(videoId)

                # for i in range(len(video_from_api)):
                #     if str(videoId) == str(video_from_api[i]["videoId"]):
                #         #lay ra _id cua video lms-dev
                #         id = video_from_api[i]["_id"]
                #         save_id_lms_dev_list.append(id)
    # save_id_lms_dev_list_final.append(save_id_lms_dev_list)
    save_videoId_list_final.append(save_videoId_list)
    # break
# print(save_videoId_list)

# print(save_videoId_list_final)

unit = {
    "title": "",  # playlist
    "type": "",  # playlist
    "description": "",
    "documentRefs": [],
    "exerciseRefs": [],
    "videoRefs": ""
}


# print(len(save_videoId_list_final))
id_lms_dev_list_final = []
for i in range(len(save_videoId_list_final)):
    # list cua tung thang
    len_of_a_element = save_videoId_list_final[i]
    # print(len_of_a_element)

    id_lms_dev_list = []
    for k in range(len(len_of_a_element)):
        # print(len_of_a_element[k])

        # for l in range(len)
        for l in range(len(video_from_api)):

            if str(video_from_api[l]["videoId"]) == str(len_of_a_element[k]):
                # print(video_from_api[l]["_id"])
                id_lms_dev_list.append(video_from_api[l]["_id"])
                break
    # unit_list[i]["videoRefs"] = id_lms_dev_list
    id_lms_dev_list_final.append(id_lms_dev_list)

    # break

for i in range(len(unit_list)):
    unit_list[i]["videoRefs"] = id_lms_dev_list_final[i]
# print(unit_list[0])
for i in range(len(unit_list)):
    if unit_list[i]["type"] == None : 
        # print(unit_list[i]) 
        unit_list[i]["type"] = "html/css/js"
        # print(unit_list[i]) 
        # break

# print(id_lms_dev_list_final)
# print(len(id_lms_dev_list_final))
# print(save_videoId_list_final[0])

# print(unit_list)


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
auth = s.post("https://lm.techkids.vn/api/v1/auth",
              data=data, headers=headers)
# print(auth.json())
LOG_USER = "unit_listss.log"
unit_listss.basicConfig(handlers=[unit_listss.FileHandler(LOG_USER, 'w', 'utf-8')],
                        level=unit_listss.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
# print(unit_list[0])
for i, v in enumerate(unit_list):
    post = s.post("https://lm.techkids.vn/api/v1/researcher/units",
                  data=json.dumps(v), headers=headers)
    # print("creating", v["title"])
    # unit_listss.info(f"{post.json()}")
    # break
    print(i,v)
    if post.status_code not in [200, 201, 202]:
        unit_listss.info(f"{post.text}")
        # break
    # break