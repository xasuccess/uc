# 定义一个函数
# 只是定义不会执行
# def关键字，后面跟随一个空格，最后冒号
# 函数所有代码缩进
def fun():
    print('我是一个函数')
    print("可以随便定义些么")
    print("然后可以运行")


print("测试下吧")
fun()


def hello(person):
    print("{0},你好呀".format(person))


hello("DL")
hello("d")


def hello(person):
    print("{0},你怎么啦".format(person))
    return "我已经和{0}打招呼了，{0}不理睬我".format(person)
    print("随便打些什么测试下")


hello("p")
print(hello("p"))
