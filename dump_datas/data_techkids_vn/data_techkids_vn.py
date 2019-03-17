# https://tk-tkvn-service.herokuapp.com/api-explorer/#/BlogCategories/post_admin_blogCategories

import mysql.connector
from bson import ObjectId
import logging as techkids_vn

import requests
import json


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
auth = s.post("https://tk-tkvn-service.herokuapp.com/api/v1/auth",
              data=data, headers=headers)
print(auth.json())
# https://tk-tkvn-service.herokuapp.com/api/v1/admin/users?_start=0&_end=300

get_data = s.get(
    "https://tk-tkvn-service.herokuapp.com/api/v1/admin/users?_start=0&_end=300", headers=headers)
get_data = list(get_data.json())
# print(len(get_data))
# print(get_data[0])
# email
# _id
_id = ""
for item in get_data:
    if item["email"] == "ed.techkidsvn@gmail.com":
        # print(item)
        _id = item["_id"]

# print(_id)


cnx = mysql.connector.connect(user='root', password='tuananh',
                              host='127.0.0.1',
                              database='techkids',
                              auth_plugin='mysql_native_password')


sql_select_Query = "select * from wp_posts where post_status = 'publish'"
cursor = cnx .cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows in python_developers is - ", cursor.rowcount)
# print(type(records))
# get category

# query_get_category = """
#         SELECT DISTINCT techkids.wp_users.ID,techkids.wp_posts.ID,techkids.wp_terms.term_id,techkids.wp_terms.name,techkids.wp_posts.post_title,techkids.wp_posts.post_name,techkids.wp_posts.post_content
#         FROM techkids.wp_posts, techkids.wp_terms,techkids.wp_term_taxonomy,techkids.wp_term_relationships,techkids.wp_users
#         WHERE techkids.wp_posts.post_status = "publish"
#             AND techkids.wp_term_relationships.term_taxonomy_id = techkids.wp_term_taxonomy.term_taxonomy_id
#             AND techkids.wp_term_taxonomy.term_id = techkids.wp_terms.term_id
#             AND techkids.wp_term_relationships.object_id = techkids.wp_posts.ID
#             AND techkids.wp_posts.post_author = techkids.wp_users.ID
#         ORDER BY techkids.wp_posts.ID;
#         """
query_get_category = """
    SELECT DISTINCT (techkids.wp_posts.post_name),techkids.wp_posts.post_title,techkids.wp_posts.post_content ,techkids.wp_posts.ID
	FROM techkids.wp_posts, techkids.wp_terms,techkids.wp_term_taxonomy,techkids.wp_term_relationships,techkids.wp_users 
	WHERE techkids.wp_posts.post_status = "publish" 
		AND techkids.wp_term_relationships.term_taxonomy_id = techkids.wp_term_taxonomy.term_taxonomy_id 
		AND techkids.wp_term_taxonomy.term_id = techkids.wp_terms.term_id 
		AND techkids.wp_term_relationships.object_id = techkids.wp_posts.ID
	ORDER BY techkids.wp_posts.ID;
        """


cursor_category = cnx .cursor()
cursor_category.execute(query_get_category)
category_records = cursor_category.fetchall()
# print("Total category: ", cursor_category.rowcount)

# print(category_records[0])
# category_list = []
# for i in range(len(category_records)):
#     # print(records[i][1])
#     if category_records[i][3] != "Uncategorized":
#        category_list.append(category_records[i])

# print(len(category_list))
# print(category_list[0])
category_list = category_records

new_data_list = []
for i in range(len(category_list)):
    data = {
        "post_id": category_list[i][3],
        "title": category_list[i][1],
        "slug": category_list[i][0],
        "shortDescription": "",
        "content": category_list[i][2],
        "categories": [],
        "tags": [],
        "author": _id,
        "featuredImage": "",
        "seo": {
            "title": category_list[i][1],
            "description": "",
            "keywords": "",
            "focusKeyword": "",
        }
    }
    new_data_list.append(data)
# print("ahihi: ", len(new_data_list))
# print("post_id: ",new_data_list[0]["post_id"])


query_get_wp_postmeta = """
    SELECT techkids.wp_postmeta.post_id,techkids.wp_postmeta.meta_key,techkids.wp_postmeta.meta_value
    FROM techkids.wp_postmeta
    where techkids.wp_postmeta.meta_key ='_thumbnail_id';
        """

postmeta = cnx .cursor()
postmeta.execute(query_get_wp_postmeta)
postmeta_records = postmeta.fetchall()
# print("Total postmeta: ", postmeta.rowcount)

postmeta_list = postmeta_records
# print(len(postmeta_list))

new_postmeta_list = []
for i in range(len(postmeta_list)):
    data_postmeta = {
        "post_id": postmeta_list[i][0],
        "meta_key": postmeta_list[i][1],
        "meta_value": postmeta_list[i][2],
    }
    new_postmeta_list.append(data_postmeta)

# print(len(new_postmeta_list))
# print(new_postmeta_list[0])

query_get_wp_post_parent = """
    SELECT techkids.wp_posts.post_parent,techkids.wp_posts.guid,techkids.wp_posts.post_mime_type
    FROM techkids.wp_posts
    where techkids.wp_posts.post_mime_type = 'image/jpeg' ;
        """

wp_post_parent = cnx .cursor()
wp_post_parent.execute(query_get_wp_post_parent)
wp_post_parent = wp_post_parent.fetchall()


# cnx.close()

wp_post_parent_list = wp_post_parent
# print(len(wp_post_parent_list))

new_wp_post_parent_list = []
for i in range(len(wp_post_parent_list)):
    data_post_parent = {
        "post_parent": wp_post_parent_list[i][0],
        "guid": wp_post_parent_list[i][1],
        "post_mime_type": wp_post_parent_list[i][2],
    }
    new_wp_post_parent_list.append(data_post_parent)

# print(len(new_wp_post_parent_list))
# print(new_wp_post_parent_list[0])


# xu ly link image
wp_post_link_image_list = []

for i in range(len(new_postmeta_list)):
    image_list = []
    for z in range(len(new_wp_post_parent_list)):

        if new_postmeta_list[i]["post_id"] == new_wp_post_parent_list[z]["post_parent"]:
            # print(new_wp_post_parent_list[z]["post_parent"])
            image_list.append(new_wp_post_parent_list[z]["guid"])

    if len(image_list) > 0:
        data_image = {
            "post_id": new_postmeta_list[i]["post_id"],
            "link_image": image_list
        }
        wp_post_link_image_list.append(data_image)

    # if i == 10:
    #     break
# print("wp_post_link_image_list : ", len(wp_post_link_image_list))
# print(wp_post_link_image_list[0])


# map link image into post
for i in range(len(new_data_list)):
    for k in range(len(wp_post_link_image_list)):
        if new_data_list[i]["post_id"] == wp_post_link_image_list[k]["post_id"]:
            new_data_list[i]["featuredImage"] = wp_post_link_image_list[k]["link_image"]

# print("new_data_list : ",len(new_data_list))
# print(new_data_list[0])


# handle seo description

query_get_wp_post_meta_description = """
    SELECT techkids.wp_postmeta.post_id,techkids.wp_postmeta.meta_key,techkids.wp_postmeta.meta_value
    FROM techkids.wp_postmeta
    where techkids.wp_postmeta.meta_key ='_yoast_wpseo_metadesc';
        """

cursor_description = cnx .cursor()
cursor_description.execute(query_get_wp_post_meta_description)
wp_post_description = cursor_description.fetchall()

wp_post_meta_description_list = wp_post_description

new_postmeta_description_list = []
for i in range(len(wp_post_meta_description_list)):
    data_postmeta_description = {
        "post_id": wp_post_meta_description_list[i][0],
        "meta_key": wp_post_meta_description_list[i][1],
        "meta_value": wp_post_meta_description_list[i][2],
    }
    new_postmeta_description_list.append(data_postmeta_description)


# print("wp_post_meta_description_list : ",len(new_postmeta_description_list))
# print(new_postmeta_description_list[0])

for i in range(len(new_data_list)):
    for k in range(len(new_postmeta_description_list)):
        if new_data_list[i]["post_id"] == new_postmeta_description_list[k]["post_id"]:
            new_data_list[i]["seo"]["description"] = new_postmeta_description_list[k]["meta_value"]

# print("new_data_list : ",len(new_data_list))
# print(new_data_list[0])

# handle category
# query_handle_category = """
#     SELECT DISTINCT (techkids.wp_posts.post_name) ,techkids.wp_posts.ID,techkids.wp_terms.term_id
# 	FROM techkids.wp_posts, techkids.wp_terms,techkids.wp_term_taxonomy,techkids.wp_term_relationships,techkids.wp_users
# 	WHERE techkids.wp_posts.post_status = "publish"
# 		AND techkids.wp_term_relationships.term_taxonomy_id = techkids.wp_term_taxonomy.term_taxonomy_id
# 		AND techkids.wp_term_taxonomy.term_id = techkids.wp_terms.term_id
# 		AND techkids.wp_term_relationships.object_id = techkids.wp_posts.ID
# 	ORDER BY techkids.wp_posts.ID;
#         """

# cursor_handle_category = cnx .cursor()
# cursor_handle_category.execute(query_handle_category)
# wp_post_category = cursor_handle_category.fetchall()

# wp_post_category_list = wp_post_category


# new_wp_post_category_list = []
# for i in range(len(wp_post_category_list)):
#     data_category = {
#         "post_name": wp_post_category_list[i][0],
#         "post_id": wp_post_category_list[i][1],
#         "category_id": wp_post_category_list[i][2],
#     }
#     new_wp_post_category_list.append(data_category)
# print(len(new_wp_post_category_list))
# print(new_wp_post_category_list[0])


# for i in range(len(new_data_list)):
#     list_category_id = []
#     for x in range(len(new_wp_post_category_list)):
#         if new_data_list[i]["post_id"] == new_wp_post_category_list[x]["post_id"]:
#             list_category_id.append(
#                 new_wp_post_category_list[x]["category_id"])
#     if len(list_category_id) > 1:
#         new_data_list[i]["categories"] = list_category_id


# print(new_data_list[0])


# print(len(new_data_list))
# list_data_final = []
# for i in range(len(new_data_list)):
#     data_end = {
#         "title": new_data_list[i]["title"],
#         "slug": new_data_list[i]["slug"],
#         "shortDescription": "",
#         "content": new_data_list[i]["content"],
#         "categories": new_data_list[i]["categories"],
#         "tags": [],
#         "author": new_data_list[i]["author"],
#         "featureImage": new_data_list[i]["featureImage"],
#         "seo": {
#             "title": new_data_list[i]["title"],
#             "description": new_data_list[i]["seo"]["description"],
#             "keywords": "",
#             "focusKeyword": "",
#         }

#     }
#     list_data_final.append(data_end)
# # print(len(list_data_final))
# print(list_data_final[len(list_data_final)-1]["title"])



cnx.close()
get_data_post = s.get(
    "https://tk-tkvn-service.herokuapp.com/api/v1/admin/blogPosts?_start=0&_end=300", headers=headers)
get_data_post = list(get_data_post.json())



# print("get_data_post : ",len(get_data_post))
# print(get_data_post[1])

# for i in range(len(get_data_post)):
#     print(get_data_post[i]["featureImage"])
# count = 0
for i in range(len(get_data_post)):
    for z in range(len(new_data_list)):
        if get_data_post[i]["slug"] == new_data_list[z]["slug"]:
            # count += 1
            # image = {
            #     "featureImage" : new_data_list[z]["featureImage"]
            # }
           
            if len(new_data_list[z]['featuredImage']) == 0:
                get_data_post[i]['featuredImage'] = []
                # print("[] : ",get_data_post[i]['featureImage'])

            else :
                get_data_post[i]['featuredImage'] = new_data_list[z]['featuredImage']

                get_data_post[i]["seo"]["title"] = new_data_list[z]["seo"]["title"]
                get_data_post[i]["seo"]["description"] = new_data_list[z]["seo"]["description"]
                # if len(get_data_post[i]['featureImage']) == 0:
                #     print(get_data_post[i]['featureImage'])


# for i, v in enumerate(get_data_post):
#     print(i,v["featuredImage"])

    # break
# print(get_data_post[2])

# print(get_data_post[i]['featureImage'][0])

# for i in range(len(get_data_post)):
#     print(get_data_post[i]["featureImage"])

# print(get_data_post[10])
# for i in range(len(get_data_post)):
#     if get_data_post[i]["slug"] == "7-xu-huong-cong-nghe-nam-2017":
#         print(get_data_post[i])

        # print("count : ",count)
        # for i in range(len(get_data_post)):
        #     if get_data_post[i]["seo"]["description"] != "":
        #         count += 1

        # print("len get_data_post : ",len(get_data_post))

        # print(get_data_post[0])

        # for i in range(len(new_data_list)):
        #     if len(new_data_list[i]["featureImage"]) > 1:
        #         print(new_data_list[i]["post_id"])
        #         print(new_data_list[i]["featureImage"])
        #         print(len(new_data_list[i]["featureImage"]))
        #         break

        # print(new_postmeta_list[0]["meta_value"])
        # print(new_wp_post_parent_list[0]["post_parent"])

        # for i in range(len(new_postmeta_list)):
        #     for z in range(len(new_wp_post_parent_list)):

        #         if int(new_postmeta_list[i]["post_id"])  == int(new_wp_post_parent_list[z]["post_parent"]):
        #             print(new_wp_post_parent_list[z]["post_parent"])

        #     if i == 10:
        #         break


# log
LOG_TECHKIDS_VN = "techkids_vn.log"
techkids_vn.basicConfig(handlers=[techkids_vn.FileHandler(LOG_TECHKIDS_VN, 'w', 'utf-8')],
                        level=techkids_vn.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
# print(unit_list[0])
for i, v in enumerate(get_data_post):
    _id = v["_id"]
    print("_id: " ,_id)
    print(v["slug"])
    # print(v)
    post = s.put(f"https://tk-tkvn-service.herokuapp.com/api/v1/admin/blogPosts/{_id}",
                 data=json.dumps(v), headers=headers)
    # print(v['title'])
    print(post.text)

    if post.status_code not in [200, 201, 202]:
        techkids_vn.info(f"{i} +  {post.text}")
        break
    # break

# featureImage

# title --> title
# slug --> post name
