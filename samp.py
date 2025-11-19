# linear search 
arr=[1,2,3,4,5,6]
print(arr)
key=int(input("enter a number:- "))

flag=False
n=len(arr)
for i in range(n):
        if arr[i]==key:
                print("Found",i)
                flag=True
                break
if flag==False:
         print("not found")