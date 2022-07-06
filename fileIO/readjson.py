import json

with open("blogs.json",encoding="utf-8")as f:
    data=json.load(f)
    print(data)
print(len(data))

# number of post by userId=1
postnum=[post for post in data if post["userId"]==1]
print(len(postnum))

# totalnumber of likes for postid 6
total=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(total)

# number post liked by user =2
user_like=len([post for post in data if 2 in post ["liked_by"]])
print(user_like)