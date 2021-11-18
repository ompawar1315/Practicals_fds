n=int(input("Enter number of roll numbers: "))
s=[]
for i in range(n):
    r=int(input(f"Enter roll numbers: "))
    s.append(r)
def bin_search(arr, x):
    low = 0
    high = len(arr)- 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low)// 2
        if arr[mid]<x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def fib_search(arr,k):
    b=0
    a=1
    f=b+a
    while(f<n):
        b=a
        a=f
        f=b+a
    key=-1
    while(f>1):
        i=min(key+b,n-1)
        if(arr[i]<k):
            f=a
            a=b
            b=f-a
            key=i
        elif(arr[i]>k):
            f=b
            a=a-b
            b=f-a
        else:
            return i
        if(a and arr[key+1]==k):
            return key+1
    
        return -1

def lin_search(a,k):
    for i in range(n):
        if a[i]==k:
            return i
    return -1

def sen_search(arr,k):
    arr.append(k)
    index = 0
    while True:
        if arr[index] == k:
            break
        index = index + 1
    return index    
    
f=int(input("Enter element to be found using binary search: "))
binary=bin_search(s,f)
print("The element is found at: ",binary)
fib=int(input("Enter element to be found using fib search: "))
fib=fib_search(s,fib)
print("The element is found at: ",fib)
l=int(input("Enter element to be found using linear search: "))
lin=lin_search(s,l)
print("The element is found at: ",lin)
sen=int(input("Enter element to be found using sentinel search: "))
se=sen_search(s,sen)
print("The element is found at: ",se)
