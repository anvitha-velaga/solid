d={}
n=int(input("enter num of users:"))
for i in range(1,n+1):
    value=list(map(int,input().split()))
    d[f"user{i}"]=value
#for key,value in d.items():
   # print(key,'->',value)
print(d)