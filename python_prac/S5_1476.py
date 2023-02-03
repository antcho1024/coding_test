e=15
s=28
m=19
x,y,z = map(int, input().split())
year =1
while 1:
    if (year-x)%e ==0 and (year-y)%s==0 and (year-z)%m==0 : break
    year +=1
print(year)
