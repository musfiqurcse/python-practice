import time
# def test(collect):
#     print(collect)

"""
    Before start coding
    Tips1 : Try to be dry Coder(Don't Repeat Yourself)
    Tips2  : Where Your code turns to Spaghetti, Use function to make more reusable

"""
# collection = []
# # for i in range(1,10):
# #     global collection
# #     collection.append(i)
# test(collection)
# car_drivern= 10
# cars = 100
# space_in_a_car = 4.0
# passengers = 90
# drivers = 30
# cars_not_driven = cars  - drivers
# cars_driven = drivers 
# carpool_capacity = cars_driven * space_in_a_car
# average_passengers_per_car = passengers / cars_driven
# types_of_people = 10
# x =f'There are {types_of_people} types of people'
# binary = f'binary'
# do_not = "don't"
# y = f'Those who know {binary} and those who {do_not}'

# print(x)
# print(y)
# print(f'I said: {x}')
# print(f'I also said: "{y}"')
# months = 'Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug'
# print(f'{months}')
# print(f'I like testing. {carpool_capacity,y} not driver101')
# print(y,x)

# # age = input('how old are you \n')

# dic={
#     "lang": "Python"
# }
# print('%(lang)s is fun' % {
#     "lang": "Python"
# })
# usages = {
#     "x":10,
#     "y":20
# }
# print('PRINT x={x} and y = {y}'.format(**usages))
# print(type(dic))

# List, Tuple and Dictionary

# my_list = [99,45,32,65,1,101,31]
# my_list2 =  [34, 23, 67, 100, 88, 2]
# my_list.extend(my_list2)
# print(my_list.sort().reversed())
'''
Start Learning List Comprehension.
:return:
'''

# ======== List Comprehension ==============
# start_time = time.time()

# x = [i for i in range(5000000) if i >50000]
# my_list = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
# my_set = {y for y in my_list}
# print(my_set)
# x =[]
# for i in range(5000000):
#     if i > 50000:
#         x.append(i)
# print(x)
# print("-----%s second ---"%(time.time() - start_time))

#========== Reading File =================

# handle = open('myfile.txt','r')
# for line in handle:
#     print(line)
# while True:
#     data = handle.read(1024)
#     print(data)
#     if not data:
#         break
# handle.close()


#========== Import Module  =================


# from math import sqrt
# print(sqrt(4))

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)

# a = 'Shibly'
# b = 'Nomany'
# many(a,b,name='key', job='programmer')



#========== Function Module  =================

'''
 :params function with params or not run
'''

# def add(a=5 , b=10):
#     print('===test==\n')
#     print((a,b))
#     pass

# add(a=10,b=2)

def function_a():
    global a
    a  = 1
    b = 2
    return a+b

def function_b():
    c=10
    return a+c

print(function_a())
print(function_b())
