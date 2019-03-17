from mongoengine import *

connect("lms-dev")
# Videos

class Video(Document):
    meta = {
        "strict": False
    }
    _id = StringField()
    title = StringField()
    videoId = StringField()

    def json(self):
        return {
            "_id": self._id,
            "title": self.title,
            "videoId": self.videoId,
        }

# def get_video_dev_list():
#     video_dev_list = [{
#         "_id": u._id,
#         "title": u.title,
#         "videoId": u.videoId,
#     }
#         for u in Video.objects]
#     return video_dev_list

# print(video_dev_list[0])
# x = get_video_dev_list()
# print(len(x))
