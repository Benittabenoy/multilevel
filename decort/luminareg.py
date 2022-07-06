# employee,e id,name ,role
class Employee:

    def __init__(self, **kwargs):
        self.e_id = kwargs.get("e_id")
        self.name = kwargs.get("name")
        self.role = kwargs.get("role")

    def __str__(self):
        return self.name


emp = Employee(e_id=298, name="manju", role="hr")
print(emp)


class Department:

    def __init__(self, **kwargs):
        employe = kwargs.get("employe")
        if employe.role == "admin":
            self.dep_name = kwargs.get("dep_name")
            self.employe = kwargs.get("employe")
        else:
            print("no access")

    def __str__(self):
        return self.dep_name


department = Department(dep_name="bca", employe=emp)
print(department)
