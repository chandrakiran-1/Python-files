num=[1,2,3,4,5]
print("original list :", num)
# indexing
print("\nIndexing Example: ")
print(num[0])
print(num[1])
# concatination
print("\nConcatination Example:")
print(num +[6,7])
print(num)
# membership
print(3 in num)
print(20 in num)
print(num[1:3])
print(num[-1])
#repition
print(num * 2)
#length
print(len(num))
num.insert(2,29)
print(num)
popped=num.pop()
print(popped)
num.reverse()
print(num)
num.sort()
print(num)
for values in num:
        print(values)
