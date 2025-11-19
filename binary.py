a=[1,2,3,4,5]
key=int(input("enter a number :-"))
low=0
high=len(a)-1
flag=False
while low<=high:
        mid=(low+high)//2
        if a[mid]==key:
                    print("element is founded")
                    flag=True
                    break
        elif a[mid]<key:
                low=mid+1
        else: 
                high=mid-1
if flag==False:
        print("element was  not founded !")       