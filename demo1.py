# 注释
'''
多行
注释 
三个双引号也型
'''
a = 100
print('a is:',a,'and the type is', type(a))
#print输出函数
a ='harry'
print('now is:',a,'and the type is', type(a))
# 命名规则：必须以字母或下划线开头。不能包含空格。不能是关键字
i=99999999999999999
print('i is',i,type(i))
i=0b10111
print('i is',i)
i=0o54
print(i)
i=0xaf
print(i)
i=10.5
print(i)
i=5.23e2
print(i)
s='1000'
#print(s,type(3))
#s='my name\'s zsy'
#print(s)
#s1=s+str(i)
#print(s1)
#a=input("your name:\n")
#print(a,type(a))
#print(int(a)*2)
print('i am zzsy.\n i am 20years old')
message='''
fqfeqef
fwefawef
WGRwgr
wefW
'''
print(message)
name='zsy'
age=20
print('my name is',name,'and i am',age,'year old')
print('my name is %s, i am %s year old' %(name,age))
print('my name is {},i am {} year old.'.format(name,age))
print(f'my name is {name},i am {age} year old.')
s = 'mynameisharry'
print(len(s))
print(s[2:6])
print(s[3:])
print(s[:5])
#前开后闭
#判断
print('name'in s)
s='my name is zsy'
print(s.title())
print(s.upper())
s='MY NAME IS ZSY'
print(s.lower())
de ='awfawfawf@dq.com'
ue ='awFawfawf@dq.com'
print(de.upper() == ue.upper())
s= '   This IS A test string   '
print(len(s))
print(s.strip(),len(s.strip()))
print(s.lstrip(),len(s.lstrip()))
print(s.rstrip(),len(s.rstrip()))
de ='awfawfawf@dq.com'
ue ='  awFawfawf@dq.com'
print(de.lower().strip()==ue.lower().strip())
s='This, is, a, test string'
print(s.startswith('This'))
print(s.endswith('ing'))
print(s.find('test'))
print(s.find('Test'))
#print(s.index('Test'))
print('-'*20)
print(s.replace('test','good'))
print(s.split(','))
L =['A','B','C','D']
print(','.join(L))

