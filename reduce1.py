from functools import reduce
mylist=[1,2,3,4,5]
print('sum=',reduce(lambda x,y:x+y,mylist))
print('max=',reduce(lambda x,y:x if x>y else y,mylist))
print('min=',reduce(lambda x,y:x if x<y else y,mylist))
