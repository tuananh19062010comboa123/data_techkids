# from mongoengine import *
# import tk_rest
# connect(
#     'diary'
# )


# class note_diary(Document):
#     note_summary = StringField()
#     author_id = StringField()
#     time = StringField()
#     classroom_id = StringField()
#     _id = StringField

#     def json(self):
#         return {
#             "id": self.id,
#             "author_id": self.author_id,
#             "classroom_id": self.classroom_id,
#             "note_summary": self.note_summary,
#         }


# class note_noteprecise(Document):
#     _id = StringField()
#     for_student = StringField()
#     diary_id = StringField()
#     note = StringField()

#     def json(self):
#         return {
#             "id": self.id,
#             "diary_id": self.diary_id,
#             "member_id": self.for_student,
#             "note": self.note
#         }


# # for class diary
# # list_data = [note_diary.json() for note_diary in note_diary.objects ]
# # data = list_data

# # for student diary
# list_data = [note.json() for note in note_noteprecise.objects]

# data = list_data

# t = tk_rest.TKRest("http://localhost:8000/api")

# t.dumpdata.post(data)
# print("saved")
