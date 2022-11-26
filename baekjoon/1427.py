import sys

inputStr=sys.stdin.readline()

#개행문자 제거
inputStr=inputStr.replace("\n","")

lis=[]
for i in inputStr: #문자열 가능?
    lis.append(int(i))

#직접 병합정렬 구현하여 사용하기 
def mergeSort(array):
    if len(array)<2: return array

    mid=len(array)//2

    left=mergeSort(array[:mid])
    right=mergeSort(array[mid:])

    merged=[]
    l=r=0
    while l<len(left) and r<len(right):
        if left[l]>=right[r]:
            merged.append(left[l]); l+=1
        else:
            merged.append(right[r]); r+=1

    merged+=left[l:]
    merged+=right[r:]

    return merged

lis=mergeSort(lis)

for i in lis:
    print(i,end='')