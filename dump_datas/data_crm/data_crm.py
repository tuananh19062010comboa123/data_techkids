# react_native : course van nhu cu

# {"_id":{"$oid":"5c3b73f960530235bc5bbe99"},"name":"code for teens basics","encodeName":"C4TB","maxSession":20,"searchString":"code for teens basics into c4tb 20","createdAt":{"$date":"2019-01-13T17:23:05.315Z"},"updatedAt":{"$date":"2019-01-13T17:23:05.315Z"}}
# {"_id":{"$oid":"5c3b74a3a286e41b70e61b13"},"name":"Code For Everyone","encodeName":"C4E","maxSession":20,"searchString":"code for everyone c4e 20","createdAt":{"$date":"2019-01-13T17:25:55.865Z"},"updatedAt":{"$date":"2019-01-13T17:25:55.865Z"}}
# {"_id":{"$oid":"5c4037c93988e7002c023124"},"name":"TestCourse","encodeName":"TC","maxSession":24,"searchString":"testcourse tc 24","createdAt":{"$date":"2019-01-17T08:07:37.271Z"},"updatedAt":{"$date":"2019-01-17T08:07:37.271Z"}}
# {"_id":{"$oid":"5c46d14e732563002cf0e118"},"name":"Ezi For Today","encodeName":"EFT","maxSession":29,"searchString":"ezi for today eft 99","createdAt":{"$date":"2019-01-22T08:16:14.712Z"},"updatedAt":{"$date":"2019-01-22T08:16:14.712Z"}}
# {"_id":{"$oid":"5c509ce95e35a4002ce0ef3d"},"name":"Code For Teen","encodeName":"C4T","maxSession":16,"searchString":"code for teen c4t 16","createdAt":{"$date":"2019-01-29T18:35:21.685Z"},"updatedAt":{"$date":"2019-01-29T18:35:21.685Z"}}
# {"_id":{"$oid":"5c6a817297b109002c9d2ba8"},"name":"Web Fullstack","encodeName":"web","maxSession":10,"searchString":"web fullstack web 10","createdAt":{"$date":"2019-02-18T09:57:06.256Z"},"updatedAt":{"$date":"2019-02-18T09:57:06.256Z"}}
# {"_id":{"$oid":"5c6be30488af82002c25d8aa"},"name":"Code for teen advance","encodeName":"C4TA","maxSession":24,"searchString":"code for teen advance c4ta 24","createdAt":{"$date":"2019-02-19T11:05:40.733Z"},"updatedAt":{"$date":"2019-02-19T11:05:40.733Z"}}
# {"_id":{"$oid":"5c6bef858c40ce002cfac6d6"},"name":"Code Intensive","encodeName":"CI","maxSession":24,"searchString":"code intensive ci 24","createdAt":{"$date":"2019-02-19T11:59:01.852Z"},"updatedAt":{"$date":"2019-02-19T11:59:01.852Z"}}

from mongoengine import *
from bson import ObjectId

connect("KidsManagementNew")

# model registrations
class Registrations(Document):
    meta = {
        "strict": False
    }
    _id = StringField()
    code = IntField()
    course = StringField()
    kid = StringField()
    connectBy = StringField()
    method = StringField()
    

    def json(self):
        return {
            "_id": self._id,
            "code": self.code,
            "course": self.course,
            "kid": self.kid,
            "connectBy": self.connectBy,
            "method": self.method
        }

# model coursedescriptions : khoa hoc
class Coursedescriptions(Document):
    meta = {
        "strict": False
    }
    _id = StringField()
    slug = StringField()
    name = StringField()

    def json(self):
        return {
            "_id": self._id,
            "slug": self.slug,
            "name": self.name,
        }


# list_registrationss
list_registrations = [{
    "_id": u._id,
    "code": u.code,
    "course": u.course,
    "kid": u.kid,
    "connectBy": u.connectBy,
    "method": u.method
  
}
    for u in Registrations.objects]
# print((list_registrations[0]) )
# print(type(list_registrationss))

# list_registrationss
list_coursedescriptions = [{
    "_id": u._id,
    "slug": u.slug,
    "name": u.name,
}
    for u in Coursedescriptions.objects]

# print(list_registrations[0])


list_web = [] #ObjectId("58e917726146810803094d3e")
list_c4e = [] #ObjectId("58e917b16146810803094e0e")
list_ci = [] #ObjectId("594cc56616a035b2d91480c3")
list_reactNative = [] #ObjectId("5a1f5540298dbbb98b4c144f")
list_c4tA = [] #ObjectId("5a218996d1e413678b6edc5d")
list_c4Teen = [] #ObjectId("5b0e540fa019bf74f666c91f")

import logging as data_not_same_course

LOG_USER = "data_not_same_course.log"
data_not_same_course.basicConfig(handlers=[data_not_same_course.FileHandler(LOG_USER, 'w', 'utf-8')],
                             level=data_not_same_course.INFO,
                             format='%(asctime)s %(message)s',
                             datefmt='%d/%m/%Y %H:%M:%S')

# print(len(list_registrations))
for i in range(len(list_registrations)):
    if str(list_registrations[i]["course"])== "58e917726146810803094d3e":
        new_course = '5c6a817297b109002c9d2ba8'
        list_registrations[i]["course"] = ObjectId(new_course)

        list_web.append(list_registrations[i])

    if str(list_registrations[i]["course"])== "58e917b16146810803094e0e":
        new_course = '5c3b74a3a286e41b70e61b13'
        list_registrations[i]["course"] = ObjectId(new_course)

        list_c4e.append(list_registrations[i])

    if str(list_registrations[i]["course"])== "594cc56616a035b2d91480c3":
        new_course = '5c6bef858c40ce002cfac6d6'
        list_registrations[i]["course"] = ObjectId(new_course)

        list_ci.append(list_registrations[i])

    if str(list_registrations[i]["course"])== "5a1f5540298dbbb98b4c144f":#ko co new_course
        # new_course = '5a1f5540298dbbb98b4c144f'
        # list_registrations[i]["course"] = repr(ObjectId(new_course))

        list_reactNative.append(list_registrations[i])

    if str(list_registrations[i]["course"])== "5a218996d1e413678b6edc5d":
        new_course = '5c6be30488af82002c25d8aa'
        list_registrations[i]["course"] = ObjectId(new_course)

        list_c4tA.append(list_registrations[i])

    if str(list_registrations[i]["course"])== "5b0e540fa019bf74f666c91f":
        new_course = '5c509ce95e35a4002ce0ef3d'
        # list_registrations[i]["course"] = repr(ObjectId(new_course))
        list_registrations[i]["course"] = ObjectId(new_course)
        list_c4Teen.append(list_registrations[i])    


list_old_course = []
list_old_course.append("58e917726146810803094d3e")
list_old_course.append("58e917b16146810803094e0e")
list_old_course.append("594cc56616a035b2d91480c3")
list_old_course.append("5a1f5540298dbbb98b4c144f")
list_old_course.append("5a218996d1e413678b6edc5d")
list_old_course.append("5b0e540fa019bf74f666c91f")

check = 0 
for i in range(len(list_registrations)):
    # print(str(list_registrations[i]["course"]))
    x = str(list_registrations[i]["course"]
    if x != "58e917726146810803094d3e" and x != "58e917b16146810803094e0e" and x != "594cc56616a035b2d91480c3" and x != "5a1f5540298dbbb98b4c144f" and x != "5a218996d1e413678b6edc5d" and x != "5b0e540fa019bf74f666c91f":
        check +=  1
        # break
print(check)

# 58aa95be40455f0930c389dc 184 
#58aa95b540455f0930c389db 46
#58e917616146810803094cf5 79

# data_not_same_course.info(f" vitri= {i} ,kid_Id= {str(list_registrations[i]['kid'])}")
# print(type(list_old_course[5]))

# print(len(list_web))341
# print(len(list_c4e))580
# print(len(list_ci))259
# print(len(list_reactNative))58
# print(len(list_c4tA))88
# print(len(list_c4Teen))111


# print(341+580+259+58+88+111) 1437

    #ahihi
# new_course = '5c6a817297b109002c9d2ba8'
# list_web[0]["course"] = repr(ObjectId(new_course)) 
# print(list_web[0])
# print(repr(ObjectId(list_web[1]["course"])))

# print(list_c4tA[1])

list_final = []
list_final.extend(list_web)
list_final.extend(list_c4e)
list_final.extend(list_ci)
list_final.extend(list_reactNative)
list_final.extend(list_c4tA)
list_final.extend(list_c4Teen)

# print(len(list_final))
# print(list_final[0])
import collections
# import logging as data_crm_sameId

# LOG_USER = "data_crm_sameId.log"
# data_crm_sameId.basicConfig(handlers=[data_crm_sameId.FileHandler(LOG_USER, 'w', 'utf-8')],
#                              level=data_crm_sameId.INFO,
#                              format='%(asctime)s %(message)s',
#                              datefmt='%d/%m/%Y %H:%M:%S')

# for i in range(len(list_final)):
#     j = i+1
#     count = 0
#     for j in range(len(list_final)):
#         if str(list_final[j]["_id"]) == str(list_final[i]["_id"]):
#             id = str(list_final[i]["_id"]) 
#             count += 1
#             data_crm_sameId.info(f" vitri= {i} ,id= {id} ,count = {count}")
#     if i == 5: 
#         break


#tim nhung thang trung nhau

# class Kids(Document):
#     meta = {
#         "strict": False
#     }
#     _id = StringField()
#     registrations = StringField()
#     mail = StringField()
#     combo = StringField()
#     dob = DateField()

#     def json(self):
#         return {
#             "_id": self._id,
#             "registrations": self.registrations,
#             "mail": self.mail,
#             "combo": self.combo,
#             "dob": self.dob,
#         }
# from datetime import date
# list_kids = [{
#     "_id": u._id,
#     "registrations": u.registrations,
#     "mail": u.mail,
#     "combo": u.combo,
#     "dob": u.dob
# }
#     for u in Kids.objects(dob__lte=date.max)]
# # print(list_kids[0])
# # print(len(list_kids))

from collections import Counter

list_kid = []
for i in range(len(list_final)):
    list_kid.append(str(list_final[i]["kid"]))
# print(list_kid[5])
x = Counter(list_kid)

# data_crm_sameId.info(f" data = {x}")
data_kid = dict(x)
count = 0

sameKid_list = []# list kid_Id trung nhau 
for k,v in enumerate(data_kid.items()):
    if (v[1]) > 1 :
        count += 1
        sameKid_list.append(v[0])
        # print(k,": ",v)
    # break
# print(count)
# print(len(sameKid_list))

# print(type(sameKid_list[0]) ) str


                                # nhung thang chi hoc 1 khoa 
# co 429 thang ghi trung <==> 191 thang hoc 2 khoa tro len 
list_kid_one_coure = []
for i in range(len(list_final)):
    if str(list_final[i]["kid"]) not in sameKid_list : 

        list_kid_one_coure.append(list_final[i])

# print(len(list_kid_one_coure))
# print(list_kid_one_coure[100])

list_registrations_one_coure = []

for i in range(len(list_kid_one_coure)):
    data_final = {
        "_id": list_kid_one_coure[i]["_id"],
        "code": list_kid_one_coure[i]["code"],
        "utm_campaign": "",
        "utm_medium": "",
        "utm_source": "",
        "depositRecords": [
            {
                "money":0,
                "time": "null"#
            }
        ],
        "sentEmails": [
            {
                "email": "",
                "time": "null"#
            }
        ],
        "courses":[
            {   
                "course":list_kid_one_coure[i]["course"],
                "admissionState": {
                    "state": "km-menu-filterbar-admissionStatus-notyet",
                    "note": "",
                    "classroom": "null" #ObjectId("lmClasses")
                },
                "depositState": {
                    "state":"km-menu-filterbar-depositstatus-notyet",
                    "favorable": 0,
                    "total": 0,
                    "paid": 0
                },
                "comment": {
                    "note": "",
                    "noteSales": ""
                },
                "testResultState": {
                    "state": "km-menu-filterbar-testresultstatus-notyet",
                    "secondChange": "",
                    "time": "null",#
                    "record": "null"#
                },
                "testState": {
                    "state": "km-menu-filterbar-teststatus-cantcontact",
                    "notePc": "",
                    "noteInterview": "",
                    "scheduleTest": "",
                    "time":"null",#
                },
                "docileFeeState": {
                    "state": "km-menu-filterbar-docilefeestate-notyet",
                    "total": 0,
                    "note": ""
                },
            }
        ],
        "method" : list_kid_one_coure[i]["method"],
        "connectBy": list_kid_one_coure[i]["connectBy"],
        "invites":0,
        "parent": "null",#
        "kid":"null",#
        "inviteCode":0,
        "deactivated": False,
        "time": "null",#
        "studyStatus": {
            "status": "notStartedYet",
            "message": ""
        }
    }    
    list_registrations_one_coure.append(data_final)


# print(len(list_registrations_one_coure))
# print(list_registrations_one_coure[0])

data_final = {
    "code": 0,
    "utm_campaign": "",
    "utm_medium": "",
    "utm_source": "",
    "depositRecords": [
        {
            "money":0,
            "time": "null"#
        }
    ],
    "sentEmails": [
        {
            "email": "",
            "time": "null"#
        }
    ],
    "courses":[
        {   
            "course":"null",#id
            "admissionState": {
                "state": "km-menu-filterbar-admissionStatus-notyet",
                "note": "",
                "classroom": "null" #ObjectId("lmClasses")
            },
            "depositState": {
                "state":"km-menu-filterbar-depositstatus-notyet",
                "favorable": 0,
                "total": 0,
                "paid": 0
            },
            "comment": {
                "note": "",
                "noteSales": ""
            },
            "testResultState": {
                "state": "km-menu-filterbar-testresultstatus-notyet",
                "secondChange": "",
                "time": "null",#
                "record": "null"#
            },
            "testState": {
                "state": "km-menu-filterbar-teststatus-cantcontact",
                "notePc": "",
                "noteInterview": "",
                "scheduleTest": "",
                "time":"null",#
            },
            "docileFeeState": {
                "state": "km-menu-filterbar-docilefeestate-notyet",
                "total": 0,
                "note": ""
            },
         }
    ],
    "method" : "Registration by Website",
    "connectBy": "connectBy",
    "invites":0,
    "parent": "null",#
    "kid":"null",#
    "inviteCode":0,
    "deactivated": False,
    "time": "null",#
    "studyStatus": {
        "status": "notStartedYet",
        "message": ""
    }

}

              # no chac
#   courses: [courseDetailSchema],

#   timestamps: true

#   time: {
#     type: Date,
#     require: [true, "Registration record time required!"],
#     default: new Date().toISOString()
#   },


# newdata_regis = {
#     "_id": ,
#     "kid": , 
#     "courses":[
#         {
#             "course": ,
#         }
#     ]
# }

# print(list_final[0])

# for i in range(len(list_final))

list_save_data_final = []
def handle_same_data_kid(kid_id):
    #ahihi

    # kid_id = "59a81952298dbbb98b4c0c8f"
    list_fixcoures = []
    for i in range(len(list_final)):
        if str(list_final[i]["kid"]) ==  kid_id:
            list_fixcoures.append(list_final[i])
            # print(list_final[i])
    

    # print(len(list_fixcoures))
    # courses = []
    list_courses = []
    for i in range(len(list_fixcoures)):
        # courses.append(list_fixcoures[i]["course"])
        course = {
            "course" : list_fixcoures[i]["course"]
        }
        # courses.append(course)

        course_data = {   
                "course":list_fixcoures[i]["course"],
                "admissionState": {
                    "state": "km-menu-filterbar-admissionStatus-notyet",
                    "note": "",
                    "classroom": "null" #ObjectId("lmClasses")
                },
                "depositState": {
                    "state":"km-menu-filterbar-depositstatus-notyet",
                    "favorable": 0,
                    "total": 0,
                    "paid": 0
                },
                "comment": {
                    "note": "",
                    "noteSales": ""
                },
                "testResultState": {
                    "state": "km-menu-filterbar-testresultstatus-notyet",
                    "secondChange": "",
                    "time": "null",#
                    "record": "null"#
                },
                "testState": {
                    "state": "km-menu-filterbar-teststatus-cantcontact",
                    "notePc": "",
                    "noteInterview": "",
                    "scheduleTest": "",
                    "time":"null",#
                },
                "docileFeeState": {
                    "state": "km-menu-filterbar-docilefeestate-notyet",
                    "total": 0,
                    "note": ""
                },
            }  
        list_courses.append(course_data)

    # new_data_registrations = {
    #         "_id": list_fixcoures[0]["_id"],
    #         "kid": list_fixcoures[0]["kid"], 
    #         "courses": courses
    #         }
    # print(new_data_registrations)
    data_final = {
        "_id": list_fixcoures[0]["_id"],
        "code": list_kid_one_coure[0]["code"],
        "utm_campaign": "",
        "utm_medium": "",
        "utm_source": "",
        "depositRecords": [
            {
                "money":0,
                "time": "null"#
            }
        ],
        "sentEmails": [
            {
                "email": "",
                "time": "null"#
            }
        ],
        "courses":list_courses,
        "method" : list_fixcoures[0]["method"],
        "connectBy": list_fixcoures[0]["connectBy"],
        "invites":0,
        "parent": "null",#
        "kid":list_fixcoures[0]["kid"],
        "inviteCode":0,
        "deactivated": False,
        "time": "null",#
        "studyStatus": {
            "status": "notStartedYet",
            "message": ""
        }
    }    
    list_save_data_final.append(data_final)
    # print(list_save_data_final[0]["courses"])
    # print(list_save_data_final[0])



# handle_same_data_kid("59658fca94c2fb4733b8f039")

for i in range(len(sameKid_list)):
    handle_same_data_kid(sameKid_list[i])

# print(len(list_save_data_final))
# print(list_save_data_final[0])


list_final_nal = []
list_final_nal.extend(list_registrations_one_coure)
list_final_nal.extend(list_save_data_final)
# print(len(list_final_nal))
# print(len(list_final)-1199)
# print(429-191)

# f = open("registrations_data.txt", "w")
# f.write(f"{list_final_nal}")
