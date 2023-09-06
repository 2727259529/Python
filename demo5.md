# 字典
## 概念：用于存放键值对的数据
## 声名方式
	1.{'a':100,'b':200}
	2.dict函数
		2.1传入二维列表/元组    dict(('a', 100), ('b', 200), ('c', 300))
								dict(['a', 10], ['b', 20], ['c', 30])
		2.2使用关键字参数
							dict=(a=100,b=200,c=300)
## 基本用法
- 通过key访问value
- 通过key添加key-value
- 通过key删除key-value
- 通过key修改key-value
- 通过key判断对应的元素是否存在

	d = {'a': 100, 'b': 200}   
	print(d['a'])  
	d['c'] = 300  
	print(d)  
	del d['a']  
	print(d)  
	d['b'] = 500  
	print(d)  
	print('c' in d)
## 常用方法
	clear():清空字典
	get():通过key获取value，和[]不同的是，如果
		  key不存在，该方法会返回None（也可指定
		  返回值），而[]会抛出keyError异常
		实例：
				d = {'a':100, 'b':200}
				print(d.get('a'))
				print(d.get('c'))
				print(d.get('c', 300))
				print(d.get('b', 300))
	update():更新对应key对应的value，如果不存在key
			 字典会新增元素
			实例：
				d = {'a':100, 'b':200}
				d.update({'a':300, 'c':400})
				print(d)
	items():返回字典的key-value对
	keys():返回字典的key列表
	values():返回字典的value列表
	pop():弹出key对应的元素，相当于删除
	setdefault():获取元素是指定默认值，如果key存在，正常
				 返回对应的值，不存在则新增元素，并返回
				 对应的默认值
				实例：
					d = {'a':100, 'b':200}
					d.setdefault('a', 400)
					d.setdefault('c', 400)
					print(d)
	fromkeys():通过列表/元组创建字典，key为列表/元组的
				元素，value默认为None，也可以自行指定
				实例：
				keys = ('a', 'b', 'c')
				d = dict.fromkeys(keys)
				print(d)
				d = dict.fromkeys(keys, 'OK')
				print(d)
	格式化字符串：
	s = 'Book name is %(name)s, price is %(price).2f'
	b = {'name': 'Python In Action', 'price': 125.25}
	print(s % b)