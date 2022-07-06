# def add(*args):
#     return sum(args)
# print(add(10,20,30,40))
# def max_fun(*args):
#     return max(args)
# print(max_fun(1,2,3,4,5,))
# def min_fun(*args):
#     return min(args)
# print(min_fun(8,1,4,6,7))



def add_nums(**kwargs):
    print(sum([v for k,v in kwargs.items()]))
    print(sum([v for v in kwargs.values()]))
    print([k for k in kwargs.keys()])
add_nums(n1=10,n2=20,n3=30)