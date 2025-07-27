
# the reduce function is used to reduce the sequenece of an element into a single element. 
# the list can be called with another name not with a variable for the better understanding.

from functools import reduce
mylist=[1,2,3,4,5]
print(reduce(lambda x,y: x*y, mylist))