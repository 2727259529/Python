# 注释
## 单行注释
以#号打头表示单行注释
## 多行注释
使用3个单引号表示多行注释
# 变量
## 作用
程序处理数据是用以保存数据
## 特点
1. 无需声明变量可以直接赋值
2. 数据类型可以动态改变
3. 命名规则：  
	3.1 必须已字母或者下划线开头  
	3.2 不能和python关键字冲突
## 输出函数（print）
	name = 'zsy'
	print('my name is ',name)
# 数据类型
## 整形
1. 十进制：正常的数字
2. 二进制：以0b或者0B开头的整数就是二进制数值
3. 八进制：以0o或者0O开头的整数就是八进制数值
4. 十六进制： 以0x或0X开头的整数就是十六进制数值  
   （10-15分别以a-f来表示）
## 浮点型：用以保存带有小数点的数值。
1. 十进制表示
2. 科学技术法表示（5.21e2 表示5.21\*10的二次方）
## 字符串：
### 定义：有单引号或双引号包含起来的零或多个字符对应的数据即为字符串
### 转义字符：将一些特殊的字符进行转义，例如：
	\b 退格符
	\n 换行符
	\r 回车符
	\t 制表符
	\" 双引号
	\' 单引号
	\\ 反斜杠
### 拼接字符串：+号即可
	s1='aaa'
	s2='bbb'
	s3=s1+s2
	print(s3)
	结果为:aaabbb
	
	**str()/repr()函数** python不允许字符串直接拼接数值
	必须将数值转化为字符串后进行拼接，使用str()函数即可
	i=5.23e2
	s='1000'
	s1=s+str(i)
	
### 用户输入函数input()
	a=input("your name:\n")
	print(a,type(a))

### 长字符串
	使用3个单引号或双引号包裹的字符被称为长字符串
	
## 字符串的深入引用

### 格式化（%）
	name='zsy'
	age=20
	print('my name is',name,'and i am',age,'year old')
	print('my name is %s, i am %s year old' %(name,age))
	print('my name is {},i am {} year old.'.format(name,age))
	print(f'my name is {name},i am {age} year old.')
	
### 使用索引获取字串(前开后闭)
	s = 'mynameisharry'
	print(len(s))
	print(s\[2:6])
	print(s\[3:])
	print(s\[:5])
	
### 使用in判断是否包含字串
	s = 'mynameisharry'
	print('name'in s)

### 大小写相关
	所有首字母大写：title()
	全部大写：upper()
	全部小写：lower()
	实例:
	s='my name is zsy'
	print(s.title())
	print(s.upper())
	s='MY NAME IS ZSY'
	print(s.lower())
	
	de ='awfawfawf@dq.com'
	ue ='awFawfawf@dq.com'
	print(de.upper() == ue.upper())

### 去空格
	去掉两头的空格：strip()
	去掉左侧的空格：lstrip()
	去掉右侧的空格：rstrip()
	实例：
	s= '   This IS A test string   '
	print(s.strip(),len(s.strip()))
	print(s.lstrip(),len(s.lstrip()))
	print(s.rstrip(),len(s.rstrip()))
	
	de ='awfawfawf@dq.com'
	ue ='  awFawfawf@dq.com'
	print(de.lower().strip()==ue.lower().strip())

### 查找/替换	
	以指定的子串开头：startswith()
	以指定的字串结尾：endswith()
	查找子串，如果找到，返回对应子串的索引，否则返回-1：find()
	查找子串，如果找到，返回对应子串的索引，否则抛出ValueError异常：index()
	使用字串替换字符串中对应的字串：replace()
	实例：
	s='This, is, a, test string'
	print(s.startswith('This'))
	print(s.endswith('ing'))
	print(s.find('test'))
	print(s.find('Test'))
	print(s.index('Test'))  尽量不要使用这个，避免报错。
	print('-'*20)
	print(s.replace('test','good'))
	
### 分割/连接
	将字符串使用指定的分隔符割成多个字符串：split()
	将多个字符串使用指定的连接符拼接成新的字符串：join()
	实例：
	L =\['A','B','C','D']
	print(','.join(L))
	print(L.split(','))