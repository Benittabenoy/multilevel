class Staff(object):

    id:int
    name:str
    role:str

    def __init__(self,*args,**kwargs):
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
            return self.name
User=Staff(id=100,name="anju",role="admin")
print(User)
