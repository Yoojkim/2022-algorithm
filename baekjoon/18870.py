import sys

def mergeSort(array):
    if len(array)<2: return array

    mid=len(array)//2
    left=mergeSort(array[:mid])[0]
    right=mergeSort(array[mid:])[0]

    merged=[]; idx=0; coordinateDict=dict()
    l=r=0
    if left[l]<right[r]:
        merged.append(left[l]); coordinateDict[left[l]]=idx; l+=1
    elif left[l]==right[r]:
        merged.append(left[l]); coordinateDict[left[l]]=idx; l+=1; r+=1
    else:
        merged.append(right[r]); coordinateDict[right[r]]=idx; r+=1

    idx+=1

    while l<len(left) and r<len(right):
        mergedLast=merged[-1]

        if left[l]<right[r]:
            if mergedLast==left[l]:
                l+=1; continue

            merged.append(left[l]); coordinateDict[left[l]]=idx; l+=1; idx+=1

        elif left[l]==right[r]:
            if mergedLast==left[l]:
                l+=1; r+=1; continue

            merged.append(left[l]); coordinateDict[left[l]]=idx; l+=1; r+=1; idx+=1

        else:
            if mergedLast==right[r]:
                r+=1; continue

            merged.append(right[r]); coordinateDict[right[r]]=idx; r+=1 ; idx+=1

    for q in left[l:]:
        merged.append(q); coordinate[q]=idx
        idx+=1

    for p in right[r:]:
        merged.append(p); coordinate[p]=idx
        idx+=1

    return [merged,coordinateDict]

num=int(sys.stdin.readline())
inputStr=sys.stdin.readline().replace("\n","")

inputStrList=inputStr.split()
coordinate=[]

for i in inputStrList:
    coordinate.append(int(i))

sortedCoordinate,coordinateDict=mergeSort(coordinate)

#coordinate, coordinateDict으로 압축 결과 print
for i in coordinate:
    print(coordinateDict[i],end=' ')