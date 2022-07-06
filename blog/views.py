from blog.models import users,posts

session={}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session u must login")
        return  wrapper

# print(users)

# username="akhil"
# password="Password@123"
# # user={"id":1,"username":"akhil","email":akhil@gmail.com","password":password

# for user in users:
#     if user["username"]==Username and user["password"]==password:
#         print("access granted")
#         break
#     else:
#         print("denied")
# user=[user for user in users if user["username"]==username and user["password"]==password]
# if user:
#     print("sucess")
# else:
#     print("failed")
# session={}
def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user =[user for user in users if user["username"]==username and user["password"]==password]
    return user
# print(authenticate(username="akhil",password="password@123"))

# GET
# POST
# PUT/PATCH
# DELETE

class LoginView:

    def post(self,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
          session["user"]=user[0]
        print(session)

class PostListView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        print(kwargs)
        post=kwargs.get("data")
        print(post)


class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts
    #     if "user" in session:
    #         return posts
    #     else:
    # return None
log_in=LoginView()
log_in.post(username="akhil",password="Password@123")
all_post=PostListView()
my_post={
    "title":"hello good morning","content":"mycontent","liked_by":[]
}
 all_post.post(data=my_post)