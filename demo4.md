# 序列
	指的是包含多项数据的数据结构，序列包含多个
	数据项，可以通过索引来访问数据项
	Python常见的序列包括：字符串，列表，元组
## 列表
### 创建
	方式一： [2,4,6,4,7]
	方式二：list()函数将元组，区间（range）转换
	为列表
	t = (1, 2, 3)
	l = list(t)
	print(l)
	l = list(range(10, 20))
	print(l)
### 追加元素
	追加单个元素
		append():元素追加至最后
		insert():指定插入元素的索引位置
		实例：
		t = (1,2,3,4)
		li=list(t)
		l1.append(7)
		print(l1)
		li.insert(2,10)
		print(li)
	追加多个元素：
		extend():追加列表/元组
		实例：
		l = [1, 2]
		l1 = [3, 4,5]
		t = (10, 20)
		l.extend(l1)
		print(l)
		l.extend(t)
		print(l)
### 删除元素 del
	实例：
	del l1[2]
	print(l1)
	del l1[5:8]
	print(l1)
### 修改元素
	通过获取列表索引对应的元素，直接赋值即可实现
	元素值的修改   实例：
	l1[0]=9
	print(l1)
### 其他方法
	count():统计元素的个数
	index():获取元素的索引值
	pop():弹出元素（最后一个元素）
	reverse():翻转列表
	sort():排序
## 元组创建
	方式一： （1，4，4，7，5，5，5）
	方式二：tuple()函数将列表、区间（range）转换为元组
	实例：
	l = [1, 2, 3]
	t = tuple(l)
	print(t)
	t = tuple(range(1, 10)) 
	print(t)
## 列表和元组的区别：
	列表可以动态变化（新增，修改，删除数据项）
	元组不可以