lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16],
    [80,12]
]

# print  all number > 16
for sub_list in lst:
    for num in sub_list:
        if num > 16:
            print(num)
print(lst)

flatten_list=[]
for sub_list in lst:
    for num in sub_list:
        flatten_list.append(num)
print(max(flatten_list))



