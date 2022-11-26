#메모리 초과 -> 입력하는 모든 수를 저장하면 안 됨
import sys

num=int(sys.stdin.readline())

#입력 값: 자연수(10,000보다 작음)
lis=[0]*100000 #0이 10000개 있는 리스트 생성 

for i in range(num):
    lis[int(sys.stdin.readline())]+=1

#출력 (print 사용 여부 고려)
for i in range(len(lis)):
    for j in range(lis[i]):
        print(i)