lst = (10, 11, 11, 12, 13, 14, 14, 14)
dup_list=[]
for i in range(0,len(lst1)):
    for j in range((i+1),len(lst1)):
        if lst1[i]==lst1[j]:
            dup_list.append(lst1[i])
# print(f"first recur num {dup_list[0]} second recur num {dup_list[1]}")
print(dup_list)
dict={}
for num in lst1:
    if num not in dict:
        dict[num]=1
    else:
        dict[num]+=1
print(dict)