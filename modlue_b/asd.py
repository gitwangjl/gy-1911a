#创建类名prouct
class product():
#定义设置关键字size得默认值
    size="6寸"
#定义color关键字
    def __init__(self,color):
        self.color=color
#定义call
    def call(self,name):
       print(name)
#定义massage
    def send_massage(self):
        print("新信息")
#类实例化
phone1=product("土豪金")
#获取变量
print(phone1.color)
print(phone1.size)
phone1.send_massage()
#调用方法
phone1.call("你好")