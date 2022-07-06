numbers = [12, 13, 14, 15, 16, 17, 18]
for num in numbers:
    if num % 2 == 0:
        print(num)

# for num in numbers:
#       if num>15:
#           print(num+1)
#       elif num<15:
#           print(num-1)
#       elif num==15:
#           print(num)

for num in numbers:
    if num >= 14 and num <= 18:
        count += 1
print(count)

numbers = (-1, 2, 0, 3, 4, 5, -2, 0, 3, -5, 0, 7, 0)
p_count = 0
z_count = 0
n_count = 0
for n in numbers:
    if n > 0:
        p_count += 1
    elif n < 0:
        n_count += 1
    elif n == 0:
        z_count += 1
print(f"+vecount{p_count},negcount{n_count},zerocount{z_count}")
