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

for i in range(1,9):
    print(i, end=" ")
print("")

for j in range(1,6):
    num = input("{0}、随便输入些啥：".format(j))
    if num == "A":
        print("good")
    elif num == "丁灵":
        print("{0}他是个帅哥".format(num))
        break  #break终止函数
    else:
        print("bad")

help(input)