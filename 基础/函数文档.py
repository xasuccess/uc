#函数文档
#函数文档的作用是对当前函数提供使用相关的参考信息
#文档的写法
def stu(name,age,*args):
	"这是一个介绍文档"
	print("随便打印点什么")
	
help(stu)

stu.__doc__