# account={"acno":1000,"opening_date":"12-01-2019","type"="savings","pname":"ram"}
# print(account.get("acno"))
# print(account.get("opening_date"))
# print(account.get
# account["balance"]=5000
# print(account)
# account["balance"]+=1000
# print(account)

mobile={"mobile_name":"redminote6","display":"led","price":45000}
print(mobile.get("mobile_name"))
print(mobile.get("display"))
print(mobile.get("price"))
print(mobile.get("mobile_name"))
# if "band" in mobile:
#     mobile["band"]="5g"
# else:
#     mobile["band"]="4g"
mobile["band"]="5g" if "band" in mobile else "4g"

# print(mobile)
if mobile["price"]>40000:
    mobile["price"]-=1000
else:
    mobile["price"]-=500
print(mobile)