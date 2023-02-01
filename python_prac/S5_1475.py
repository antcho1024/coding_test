nums = input()
ps = [0,0,0,0,0,0,0,0,0,0]
for i in nums:
    ps[int(i)] +=1
ps[6] = int((ps[6]+ps[9])/2+0.5)
ps[9]=0
ps.sort(reverse=True)
print(ps[0])