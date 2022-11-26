import sys

def mergeSort(lis)->list:

    if len(lis)<2: return lis

    mid=len(lis)//2
    left=mergeSort(lis[:mid])
    right=mergeSort(lis[mid:])

    #병합
    merged=[]
    l=0; r=0

    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            merged.append(left[l]); l+=1
        else:
            merged.append(right[r]); r+=1

    merged+=left[l:]
    merged+=right[r:]
    
    return merged

num=int(sys.stdin.readline())
lis=[]
for i in range(num):
    lis.append(int(sys.stdin.readline()))

res=mergeSort(lis)

for j in res:
    print(j)