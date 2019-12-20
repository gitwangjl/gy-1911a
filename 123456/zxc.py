# import json
# j ='''
# {"name":"小明",
# "sex":"未知"
# }
# '''
# d = json.loads(j)
# d["sex"]="男"
# # print(d)
# #
# j = json.dumps(d,ensure_ascii=False)
# print(j)

# import random
# # a = random.randint(1,6)
# # print(a)
#
# b = random.choice("qwertyuiop")
# print(b)
import os
p = os.path.abspath("test2.txt")
print(p)
d = os.path.dirname(p)
print(d)
f = os.path.basename(p)
print(f)

os.mkdir("gy_b")
print("gy_b")