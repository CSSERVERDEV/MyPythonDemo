"""数学题：好事好 + 要做好 = 要做好事,求 “好、事、做、要”的值分别是多少？"""
list1=[0,1,2,3,4,5,6,7,8,9]
for h  in list1:
    for s in list1:
        for z in list1:
            for y in list1:
                if (h*100+s*10+h)+(y*100+z*10+h)==(y*1000+z*100+h*10+s):
                    print(h,s,y,z)

def func(i):
    # 可以把h(好),s(事),z(做),y(要)看作是0000-9999的千、百、十、个位数。
    h, s, z, y = f'{i:04d}'
    # 按照汉字的顺序重新排列变量
    if  int(f'{h}{s}{h}') + int(f'{y}{z}{h}') == int(f'{y}{z}{h}{s}'):
        print(h, s, z, y)

'''f‘{i}’是把整数i转换成一个字符串，:04d是用0补齐四位。然后把这四位数分别赋值给h,s,z,y，这里用了一个解包的技巧，其他语言最少要写四行。'''
    #遍历0000-9999
    for i in range(10000):
        func(i)

"""把问题看成三位数(101-989)加三位数等于四位数，然后通过位数分解这样只需要两重循环。"""
from itertools import product
    print [(x, y, z, f)for (x, y, z, f) in product(*[range(10)] * 4)if (z * 100 + f * 10 + z) + (x * 100 + y * 10 + z) == (x * 1000 + y * 100 + z * 10 + f)]
