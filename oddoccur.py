def oddocuuring(arr):
    res=0
    for element in arr:
        res=res^element
    return res
arr=[]
n=int(input("enter array size"))
for i in range(n):
    arr.append(int(input("enter element")))
print(oddocuuring(arr))