import re

'''
正则表达式复习
'''

s = "T:142906630:RR:0:1:3780:3780:33:4641"
# r = re.search(":(.*?):", s)
# print(r.group(1))
# r = re.search(":*:(.*?):", s)
# print(r.group())
f = re.findall(":(.*?):", s)
print(f)
f = re.search(":(.):", s)
print(f.group())
f = re.findall("\d+", s)
print(f)
w = "221.正常.txt"
d = re.search(r"\d+", w)
print(d.group())

list1 = [1,2,3]
list2 = [1,2,3]
# list3 = [1,2,4]
# li = [list1, list2, list3]
# print(list1==list2)
# print(list1==list3)
# list4 = [1,2,8]
# if list4 not in li:
#     print(23232)
print(min(list2))
print(1000/70>10)