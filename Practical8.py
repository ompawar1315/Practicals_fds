n=int(input("Enter number of roll numbers: "))
s=[]
for i in range(n):
    r=int(input(f"Enter roll number: "))
    s.append(r)
def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1],arr[j]

def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        
def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
def divide(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    flag=True
    while flag==True:
        while(i<=j and arr[i]<=pivot):
            i=i+1
        while(i<=j and arr[j]>=pivot):
            j-=1
        if(j<i):
            flag=False
        else:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[low]
    arr[low]=arr[j]
    arr[j]=temp
    return j
def quicksort(arr,low,high):
    if(low<high):
        d=divide(arr,low,high)
        quicksort(arr,low,d-1)
        quicksort(arr,d+1,high)
        
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge(left)
        merge(right)
        i=j=k=0
        while (i<len(left) and j<len(right)):
            if (left[i]<right[j]):
                arr[k] =left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1
        while i <len(left):
            arr[k] =left[i]
            i=i+1
            k=k+1
  
        while j <len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1

def shellsort(arr,n):
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap=gap//2
            
BubbleSort(s)
print("Roll no sorted by Bubble sort are: ",s)
InsertionSort(s)
print("Roll no sorted by Insertion sort are: ",s)
SelectionSort(s)
print("Roll no sorted by Selection sort are: ",s)
quicksort(s,0,n-1)
print("Roll no sorted by Quick sort are: ",s)
mergesort(s)
print("Roll no sorted by merge sort are: ",s)
shellsort(s,len(s))
print("Roll no sorted using shell sort are: "
