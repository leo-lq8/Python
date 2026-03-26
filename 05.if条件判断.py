#if判断分数是不是超过680
# score = 700
# if score>680:
#     print("欢迎你来清华读书")
#     print("请享受美好的大学生活吧")
#
#
# total = 100000.0
# password1 = 9999.0
#
# password = int(input("请输入您的银行卡密码："))
# if password==password1:
#         print("密码正确")
#         num= float(input("请输入取款金额："))
#         balance = total - num
#         print(f"取款后银行卡余额为{balance:.2f}元")
# else:
#         print("密码错误，请重新输入")

#账号密码案例
# ok_account = "1"
# ok_password = "888888"
#
# account = input("请输入账号：")
# password = input("请输入密码：")
#
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("欢迎进入B站")
# else:
#     print("登录失败")
#     print("账号或密码错误")



#案例：判断闰年还是非闰年

# year = int(input("请输入一个年份："))
#
# if year%100 > 0 and year%4 == 0 or  year%400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")

#案例：判断正数负数0

# num = float(input("请输入一个数字："))
#
# if num>=0:
#     print(f"{num}是正数")
# elif num<=0:
#     print(f"{num}是一个负数")
# else:
#     print("这个数是0")

#案例：判断三角形是什么三角形，等腰，等边，普通

a = float(input("请输入第一个边的边长："))
b = float(input("请输入第二个边的边长："))
c = float(input("请输入第三个边的边长："))

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("三角形是等边三角形")
    elif a==b  or a == c  or b==c:
        print("三角形是等腰三角形")
    else:
        print("三角形是普通三角形")
else:
    print("不能构成三角形")




























