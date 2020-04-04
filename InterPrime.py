# Taking the input from user
n=int(input())
c=0
l1=[]
for i in reversed(range(2,n)):
    x=i
    for j in reversed(range(2,x)):
        if((x%j)!=0):
            c+=1
    if c==(x-2):
        l1.append(x)
    c=0           
l2=[]
for i in reversed(range(n+1,2*n-1)):
    y=i
    for j in reversed(range(2,y)):
        if((y%j)!=0):
            c+=1
    if c==(y-2):
        l2.append(y)
    c=0
l2.reverse()
#print(l1,l2)
# Displaying the output only if the prime numbers are equidistance
for i in range(len(l1)):
    for j in range(len(l2)):
        if (n-l1[i])==(l2[j]-n):
            print(l1[i],l2[j])
