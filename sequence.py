# string , list, tuple, range
# common actions = indexing,slicing, length, iteration.
a=[1,2,3,4]
print(a, type(a))
print(a[1])
print(a[0:3])
print(len(a))
for i in range(1,6):
    print(i, end=" ")

x=[2,8,6,4]
print(sorted(x))
list.sort(x)
print(x)