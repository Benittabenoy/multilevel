class course:
    c_id:int
    c_name:str
    c_fee:int
    institution:str
    # def _init_(self,c_id,c_name,c_fee,institution):
    #     self.c_id=c_id
    #     self.c_name=c_name
    #     self.c_fee=c_fee
    #     self.institution=institution
    def __init__(self,**kwargs):
        self.c_id=kwargs.get("c_id")
        self.c_name=kwargs.get("c_name")
        self.c_fee=kwargs.get("c_fee")
        self.institution=kwargs.get("institution")
    def print_course(self):
        print(self.c_id,self.c_name,self.c_fee,self.institution)
p1=course(c_id=10120,c_name="python",c_fee=29500,institution="luminar")
p2=course(c_id=10121,c_name="flutter",c_fee=25000,institution="luminar")
p1.print_course()
p2.print_course()