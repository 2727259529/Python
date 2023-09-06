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