#type（查看类型的数据）语句,内置函数，可以查看数据属于什么类型，例如可以查看int，float，bool，
from types import NoneType

print(type("hello"))
print(type(10))
print(type(3.14))

print(type(True))
print(type(False))
print(type(None))

num = -100
print(type(num))

#isinstance(数据，类型),一个bool值，判断数据是否是指定类型，如果是就是True，如果不是就是False
num = 5
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))
print(isinstance(num,str))
print(isinstance(num,NoneType))

#字符串 单引号可和双引号可以定义短句 三引号可以换行
s1 = "hello"
s2 = 'Python'
s3 = """
尊敬的教授：
    您好，
    很高兴能听你的讲课，
    每节课都受益匪浅，
    每节课都想说要不您还是说韩语吧，您的英语一般人真的听不懂！
"""
print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

print(isinstance("hello",int))
print(isinstance('Python',float))
print(isinstance( """
尊敬的教授：
    您好，
    很高兴能听你的讲课，
    每节课都受益匪浅，
    每节课都想说要不您还是说韩语吧，您的英语一般人真的听不懂！
""",str))

print(isinstance(s1,int))
print(isinstance(s2,int))
print(isinstance(s3,str))

#转译在单引号前边加"\"就好了, \n用来换行, \t是缩进相当于缩进
print('It\'s my girlfriend')

msg1 = 'It\'s my girlfriend'
print(msg1)

msg2 = "hello就是\"您好\"的意思"
print(msg2)

msg3 = '我喜欢的女生姓江\n她是一个很有趣的女生'
print(msg3)

msg4 = '\t我喜欢的女生姓江\n\t她是一个很有趣的女生'
print(msg4)

# +用来拼接，只能拼接两个字符串，无法将非字符串和字符串拼接
slogan = "我是leo"",""我要成为AI领域的专家"
print(slogan)
slogan1 = "我是leo" + "," + "要成为AI领域的专家"
print(slogan1)

s1 = '努力学习'
s2 = '超越自己'
print("我是Leo" + "，" + "我会" + s1 + "并且" + s2 + "。")

#将int类型的数字转为字符串str（数字）
name = '我是leo，'
age = 26
pro = '我学习人工智能专业，'
will = '我希望成为这个领域的专家'
print(name + "我今年" + str(age) + "岁" + pro + will )

#通过占位符 %s 去替换 %表示我要占位， s表示将变量转为字符串放入占位的位置

a1 = 'be good man'
a2 = 'be rich man'
print("I am leo : %s %s" %(a1,a2))

name = '我是leo，'
age = 26
pro = '我学习人工智能专业，'
will = '我希望成为这个领域的专家'
print(" %s我今年%s岁%s %s " %(name,age,pro,will))

#可以用 {} 来占位替换，在语句前要加 f ，例如 print(f" {name1}我今年{age1}岁，{pro1}{will1}。 ")
name1 = '我是leo，'
age1 = 26
pro1 = '我学习人工智能专业，'
will1 = '我希望成为这个领域的专家'
print(f" {name1}我今年{age1}岁，{pro1}{will1}。 ")
