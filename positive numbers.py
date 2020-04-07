a=[]
b=[]
n=int(input())
#n is the no. of elements in the list
#a is the list we get from the user
#b is the list with positive numbers
for i in range(n):
    a.append(int(input()))
for i in a:
    if i>0:
        b.append(i)
print(b)
