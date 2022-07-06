# class Parent:
#     def phone(self):
#         print("redmi note 6")
#
#     def bike(self):
#         print("passion pro")
#
#
# class child(Parent):
#     pass
#
#
# ch = child()
# ch.phone()
# ch.bike()
# # parent class and child class have same method and signature >> overriding
class Parent:
    def phone(self):
        print("redmi note 6")

    def bike(self):
        print("passion pro")


class child(Parent):
    def phone(self):
        print("iphone 12")

    def bike(self):
        print("duke")


ch = child()
ch.phone()
ch.bike()
# parent class and child class have same method and signature >> overriding
# same method name and differnt parametrs>>overloading