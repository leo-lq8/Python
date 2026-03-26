# 字面量的写法
print(100)#整数（int）
print(3.14)#小数（float）
print(True)#布尔（bool）
print(False)
print("Hello World")#字符串（str）
print("------------")
print(None)# 空格（NoneType）

# 布尔类类型本质也是整数类型（True-1；False-0）
print(True+1)# 2
print(False-1) # -1

#变量----python动态类型编程语言，一个变量可以存储不同类型的数据（但是在项目开发中，推荐变量只存储一种类型的数据）
num = 1114.1
print(num)

num = num + 1000
print(num)

num = "ok"
print(num)

num = True
print(num)

a = True
print( a )

#案列 课程基础播放量20.7w 每月新增50w 求未来两个月总播放量
base = 20.7
incr = 50
print("未来第一个月的播放总量是：",base + incr)
print("未来第二个月的播放总量是：",base + incr + incr)

#案例升级
base,incr = 20.7,50
print("未来第一个月的播放总量是：",base + incr)
print("未来第二个月的播放总量是：",base + incr + incr)

#标识符
#a-z ，A-Z，“__” ，数字要在名字之后
#变量名 见名知道意思  涉及多个部分用下划线分割（update_name, my_name, user_first_name)
#变量名英文字母全部小写

#案例
a = 10
b = 20
c = a
a = b
b = c
print(a,b)

