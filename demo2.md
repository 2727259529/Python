# 字节串
原始的二进制数据
##字符串和字节串的相互转换
	1. 字符串——>字节串：三种方式
	1.1 如果字符串内容都是ASCII字符，可以通过在字符串前面添加b来构筑字节串
	1.2 调用bytes()函数构筑，默认‘utf-8’字符集
	1.3 调用字符串自身的encode()方法将字符串按照指定的字符集转换为字节串，如不指定，默认‘utf-8’
	2. 字节串——>字符串
		调用字节串自身的decode(0方法将其解码成字符串，可以指定对应解码字符集，默认utf-8
	3. 实例：
		b1 = bytes()
		b2 = b''
		b3 = b'hello'
		print(b3)
		print(b3[0])
		print(b3[2:4])
		b4 = bytes('我喜欢Python编程', encoding='utf-8')
		print(b4)
		b5 = 'Python很有趣哦！'.encode('utf-8')
		print(b5)
		st = b5.decode('utf-8')
		print(st)	