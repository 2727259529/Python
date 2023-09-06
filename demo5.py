d={}
l=[]
t=()
print(d)
print(l)
print(t)
d={'a':10,'name':'zsy',2:30}
print(d[2])
d=dict((('a',40),('b',50),('c',60)))
d = dict(a=300,b=400,c=500,name='zsy')
print(d)
print(d['a'])
d['d']=1000
print(d)
del d['b']
print(d)
d['a']=3000
print(d)
print('name' in d)
d.clear()
print(d)
d['a']=1000
print(d)
print(d.get('b',200))
d.update({'a':400,'b':500,'c':600})
print(d.items())
print(d.keys())
print(d.values())
d.pop('c')
print(d)
keys=['A','b','c']
d=dict.fromkeys(keys,'OK')
print(d)
name = 'zsy'
age = 20 
print('i am %s'%(name,age))