#
# from modlue_b.asd import *
#
# #类实例化
# phone1=product("大红")
# #获取变量
# phone1.color
# phone1.size
# #调用方法
# phone1.call("雷阳洪")


# #json 转字典
# import json
# j ='''
# {"name":"小明"
# "sex":"未知"
# }
# '''
# d = json.loads(j)
# d["sex"]="男"
# print(d)
import os
try:
    os.mkdir("507.py")
except:
    print("已存在")
else:
    print("创建成功")
finally:
    print("创建结束")

