__author__ = 'chintanpanchamia'

a = [1.5,8.44,2,6.9,5.5]
key = 2
pointer = 0
for i in a:
    if(i == key):
        pointer = a.index(i)
    print pointer