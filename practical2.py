Marksofstud=[]
Noofstud=int(input("Enter the no. of students: "))
for i in range(Noofstud):
    marks=int(input(f"Enter marks of student {i+1}:"))
    Marksofstud.append(marks)

def average(Marksofstud):
    sum = 0
    count=0
    for i in range(len(Marksofstud)):
        sum=sum+Marksofstud[i]
        count+=1
        average = sum/count 
    
    print("Total marks of student =",sum)
    print("average marks of student =",average)
average(Marksofstud)

def max():
    max_value = 0 
    if i !=-999:
        for num in Marksofstud:
            if (max_value is None or num > max_value):
                max_value = num
    print('The max marks is:', max_value)

def min():
    mini = Marksofstud[0]
    for i in range(len(Marksofstud)):
        if Marksofstud[i] < mini:
            mini = Marksofstud[i] 
    print("The least marks is: ",mini)
max()
min()

def absentcount(Marksofstud):
    count=0
    for i in range(len(Marksofstud)):
        if Marksofstud[i]==-1:
            count+=1
    print("absent count is: ",count)    
    return(count)
absentcount(Marksofstud)

def maxFrequency(Marksofstud):
    i=0
    Max=0
    for j in Marksofstud:
        if (Marksofstud.index(j)==i):
            print(j,"  ",Marksofstud.count(j))
            if Marksofstud.count(j)>Max:
                Max=Marksofstud.count(j)
                mark=j
        i=i+1
    return(mark,Max)
maxFrequency(Marksofstud)
