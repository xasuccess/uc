# input的作用是
# 1. 在屏幕上输出括号内的字符串
# 2. 接受用户输入的内容并返回到程序
# 3. input返回的内容一定是字符串类型
gender = input("请输入性别：")
print("您输入的性别是: {0}".format(gender))
if gender == "男":
    print("来，我们一起敲代码")
elif gender == "女":
    print("我们一起学猫叫，一起喵喵喵喵")
else:
    print("滚蛋")