# coding:utf-8

name=raw_input()
print name
a = 123 # a是整数
print a
a = 'ABC' # a变为字符串
print a
if isinstance(a,str):#判定是不是字符串
    print True

classmates = ['Michael', 'Bob', 'Tracy']
len(classmates)#list个数
classmates[0]
classmates.append('Adam')#有序，添加到元素末尾
classmates.pop()#末尾的元素，也可以指定位置
classmates[1] = 'Sarah'
#取前N个元素，也就是索引为0-(N-1)的元素
r=[]
for i in range(3):
    r.append(classmates[i])

classmates[0:3]#取前3个元素
classmates[-2:]#倒数切片
classmates[:]#复制list

for x, y,s in [(1, 1,4), (2, 4,7), (3, 9,10)]:
    print x, y,s

[x * x for x in range(1, 11)]
[m + n for m in 'ABC' for n in 'XYZ']
import os
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录
[s.lower() for s in classmates]
isinstance(x, str)


classmates = ('Michael', 'Bob', 'Tracy')#tuple有序数组,不可变
t = ('a', 'b', ['A', 'B'])#tuple包含list,变的是list数组

age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'

#把每个元素代入变量x
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

#生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

#raw_input读取默认为字符串
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'

'''
dict字典，key-value,索引表页码查找，key唯一并且不可变
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
d['Adam'] = 67
'Thomas' in d#key是否存在
d.get('Thomas')
d.get('Thomas', -1)
d.pop('Bob')
for k, v in d.iteritems():
    print k, '=', v

[k + '=' + bytes(v) for k, v in d.iteritems()]



"""
set key的集合,无对应的value
"""
s = set([1, 2, 3])
s = set([1, 1, 2, 2, 3, 3])#自动过滤重复元素
s.add(4)
s.remove(4)
'''
set可以看成数学意义上的无序和无重复元素的集合,可以做数学意义上的交集、并集等操作
'''
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
set([2, 3])
s1 | s2
set([1, 2, 3, 4])

'''
str是不变对象,指向的b才是Abc
'''
a = 'abc'
b = a.replace('a', 'A')


def enroll(name, gender,age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender

enroll('Sarah', 'F')
#默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#generator生成器,为了节省内存，我们不必要把所有数据加载，通过生成器推算出后续元素,yield关键字
g = (x * x for x in range(10))
for n in g:
    print n
'''
斐波那契
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

fib(6)#输出斐波那契数列的前N个数

def is_odd(n):
    return n % 2 == 1

filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

def not_empty(s):
    return s and s.strip()

filter(not_empty, ['A', '', 'B', None, 'C', '  '])