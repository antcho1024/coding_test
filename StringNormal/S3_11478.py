s = input()
bucket=set()
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        tmp = s[i:j]
        bucket.add(tmp)
print(len(bucket))