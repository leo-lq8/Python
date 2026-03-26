# #获取键盘上输入的数据 s = inpu（）
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
tall = float(input("请输入您的身高："))
wight = float(input("请输入您的体重："))
kpi = wight / tall**2
print(f"您的姓名是{name}\n年龄是{age}岁\n身高{tall}CM\n体重{wight}KG\n体脂率为{kpi}")

#案例：银行卡ATM取款

total = 100000.00
password1 = 9999

password = int(input("请输入您的银行卡密码："))
if password==password1:
        print("密码正确")
        num= float(input("请输入取款金额："))
        balance = total - num
        print(f"取款后银行卡余额为{balance:.2f}元")
else:
        print("密码错误，请重新输入")

