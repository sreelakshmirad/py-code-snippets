# Lambda functions

# lambda arguments: expression


def double(x):
    return x * 2


# y = lambda x : x *2
# print(y)
# print(double)

# print(y(6))



# def add(x,y):
#     return x + y

# y = lambda x, y : x+y
# print(y(6,5))


# def max(x,y):
#     if x >y :
#         return x
#     else :
#         return y

# y =  lambda x,y : x if x > y else y 

# print(y(6,5))




tables = [lambda x: x*10 for x in range(1, 11)]
 
for table in tables:
    print(table)



# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
# final_list = list(filter(lambda x: (x%2 != 0) , li))
# print(final_list)



# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
# final_list = list(map(lambda x: x*2, li))
# print(final_list)



import functools

lis = [ 1 , 3, 5, 6, 2, ]
 
print (functools.reduce(lambda a,b : a if a > b else b,lis))