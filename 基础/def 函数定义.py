def stu(name, age, gender="male"):
	if gender == "male":
		print("{0} is {1} years old, and he is a good student".format(name,age))
	elif gender == "female":
		print("{0} is {1} years old, and she is a good student".format(name, age))
	else:
		print("GG")
		
stu("dd",22,"male")
stu("dd",39,) #gender 值如果不填写，默认定义函数中的值male
stu("de",33,"female")
stu("","","mal")

#普通参数，只按照位置传递，容易出错，可以这么定义

def stu_key(name="no",age=0,addr="no"):
	print("我叫{0},我今年{1}岁了，我住在{2}".format(name,age,addr))
	
stu_key(age=22,name="DL",addr="上海市长宁区")

##收集参数
# 把没有位置，不能和定义时的参数位置相对应的参数，放入一个特定的参数结构中
# 参数名args 不是必须这么写，但是，我们推荐直接用args，约定俗成
# args 之前需要添加*号，*args，收集参数可以和其他参数共存
def stu(*args):
	print("随便打点什么")
	print(type(args))  ##类型是tuple
	for i in args:
		print(i)
stu("dd","werw",33,"社会主义好啊")
stu("dl")

##类似以上 **kwargs 类型是dict，字典的类型是一对一对的
def stu(**kwargs):
	print("随便打印点啥")
	print(type(kwargs))
	for i,j in kwargs.items():  #items???
		print(i,"----",j)
stu(name="dkl",age=109)