# try=> :block doubtful code
# except=> :block handling code
# raise=>keyword custom error throw
# finally=> :block clean up processing,mandatory process

# num1=int(input("enter number 1"))
# num2=int(input("enter number 2"))

# try:
#     res=num1/num2
#     print(f"result{res}")
# except Exception as e:
#     print(e)
# print("db transaction")
# print("file operation")
#
# lst=[]
# try:
#     print(num1/num2)
#
# except Exception as e:
#     num2=int(input("enter another value num2"))
#     print(num1/num2)
# finally:
#     print("db transaction")
#     print("file operation")


# age=int(input("enter age"))
#
# if (age<18):
#     raise Exception("not eligible for taking booster dose")
# else:
#     print("eligible")


ph_num=(input("enter ph_num"))
if len(ph_num)!=10:
    raise Exception("not valid")
else:
    print("valid")