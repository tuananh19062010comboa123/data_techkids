from mongoengine import *

connect("tk-lms")

class Videos(Document):
  meta = {
      "strict": False
  }
  title = StringField()
  videoId = StringField()
  source = StringField()
  duration = StringField()
  description = StringField()

  def json(self):
    return {
        "title": self.title,
        "videoId": self.videoId,
        "source": self.source,
        "duration": self.duration,
        "description": self.description
    }


class Users(Document):
  meta = {
      "strict": False
  }
  email = StringField()
  firstName = StringField()
  lastName = StringField()
  password = StringField()

  def json(self):
    return {
        "email": self.email,
        "firstName": self.firstName,
        "lastName": self.lastName,
        "password": self.password
    }
# list_users = [{
#     "email": u.email,
#     "password": "codethechange",
#     "name": {
#         "firstName": u.lastName,
#         "lastName": u.firstName
#     },
#     "role": "member"}
#     for u in Users.objects]
# print(list_users[0])

    
# email = "huynhtuanhuy1996@gmail.com"
# # x =  email.find('@')
# # print(x)
# # s = email.slice(x,len(email))
# # print(s)
# x = email.split('@')
# print(x[0])