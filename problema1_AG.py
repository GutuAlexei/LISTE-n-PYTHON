x=[1,2,3,2,-1,6,7,5,10,-11,-43]
print('a)', x)
y=sorted(x)
print('b)',y)
y.sort(reverse=True)
print('c)', y)
print('d)', len(y))
print('e)', max(y))
print('f)', min(y))
print('g)', x + [111])
x[1]=222
print('h)', x)


