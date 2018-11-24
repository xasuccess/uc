a=[1,22,2,69999]
print(type(a))   #打印参数类型
def fun(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    else:
        return fun(a-2) + fun(a-1)

for a in range(1,10):
    if fun(a)<6:
        if fun(a)%2 == 1:
            print(fun(a), end=" ")
    else:
        print(fun(a), end=" ")
print(type(fun(a)))

for a in range(1,10):
    if fun(a)<99:
        if fun(a)%2 == 1:
            print(fun(a), end=" ")

print(type(fun(a)))