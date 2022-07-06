# map -------------|
#                    |======>builtins
# filter-----------|
# reduce
lst = [10, 2, 30, 4]
squares = list(map(lambda n: n ** 2, lst))
cubes = list(map(lambda n: n ** 3, lst))

# map<5 num-1 >5 num+1
# num_out=[num-1 if num<5 else num+1 for num in lst]
# print(num_out)

num_out = list(map(lambda n: n - 1 if n < 5 else n + 1, lst))
print(num_out)
