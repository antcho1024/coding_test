n= int (input())
m = int(input())
str = input()

# 50점 (시간 오래 걸림)
# p='I'
# for _ in range(n):
#     p +="OI"
# cnt =0
# while p in str:
#     cnt +=1
#     index = str.find(p)
#     str = str[index+1:]
# print(cnt)

answer, i, cnt = 0, 0, 0
while i < m-1:
    if str[i:i+3] == 'IOI':
        cnt +=1
        i+=2
        if cnt ==n:
            answer+=1
            cnt-=1
    else:
        i+=1
        cnt=0
print(answer)