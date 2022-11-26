import sys

def mergeSort(array):
    if len(array)<2: return array

    mid=len(array)//2
    left=mergeSort(array[:mid])
    right=mergeSort(array[mid:])

    merged=[] #반환 배열
    l=r=0
    while l<len(left) and r<len(right):
        #y 좌표가 증가하는 순 -> 같으면 x좌표가 증가하는 순서대로
        if left[l][1]<right[r][1]:
            #left가 더 큰 경우
            merged.append(left[l]); l+=1
        elif left[l][1]==right[r][1]:
            #x좌표 증가 순으로
            if left[l][0]<=right[r][0]:
                merged.append(left[l]); l+=1
            else:
                merged.append(right[r]); r+=1
        else:
            #right가 더 큰 경우
            merged.append(right[r]);r+=1

    #left, right 남은 부분 넣기
    merged+=left[l:]; merged+=right[r:]

    return merged

num=int(sys.stdin.readline())
coordinate=[]
for i in range(num):
    inputStr=sys.stdin.readline()
    inputStr=inputStr.replace("\n","")
    x,y=inputStr.split()
    x=int(x); y=int(y)

    coordinate.append((x,y))

sortedCoordinate=mergeSort(coordinate)

for c in sortedCoordinate:
    print(c[0],c[1])