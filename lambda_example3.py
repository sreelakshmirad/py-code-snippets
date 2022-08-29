y = lambda x : x *2
print(y(6))

y2 = lambda x : y(x* 3)

print(y2(10))


y3 = lambda x : y2(y(x* 3))  *2

print(y3(10))




