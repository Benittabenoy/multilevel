pattern="ABACCD"
# char_count={}
# for char in pattern:
#     if char in char_count:
#         print(f"first recursive character is {char}")
#         break
#     else:
#         char_count[char]=1
#
# char_count={}
# rec_char=[]
# for char in pattern:
#     if char in char_count:
#         rec_char.append(char)
#     else:
#         char_count[char]=1
# print(rec_char[1],"second recursive char")
char_count={}
rec_char=[]
for char in pattern:
    if char in char_count:
        rec_char.append(char)
    else:
        char_count[char]=1
print(rec_char)