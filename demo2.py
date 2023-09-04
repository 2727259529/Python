s1 =bytes('周生岩',encoding='utf-8')
s2 =bytes('aasdfgh',encoding='utf-8')
#s2=b'scafw'
#print(s1)
#print(s2)
s1 = '周生岩'.encode('utf-8')
s2 = '周生岩'.encode('gbk')
print(s1)
print(s2)
s1=s1.decode('utf-8')
print(s1)
#运算符
i = 10
i=i+5
i+=5
i-=5
i*=2
print(i)
x=10
y=3
print(x/y)
print(x//y)
x=25
y=3
print(x%y)
print(y**2)
print(y**4)
a=True
b=False
print(a and b)
print(a or b)
print(not a)
c='ok'if a else 'NOt ok'
print(c)
s='This is a test string'
print('is' in s)
