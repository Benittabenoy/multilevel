lst = [2, 3, 4, 6, 5]
lst.sort()
element = 7
low = 0
upp = len(lst) - 1
count=1
while (low < upp):
    cur_sum = lst[low] + lst[upp]
    if element == cur_sum:
        print(f"pairs{lst[upp]},{lst[low]}")
        low += 1
    elif cur_sum > element:
        upp -= 1
    elif cur_sum < element:
        low += 1
    count+1
# count=1
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(f"paris{lst[i]},{lst[j]}")
#
#         count+=1
# print("num iter",count)
