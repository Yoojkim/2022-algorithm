import sys

def mergeSort(array):
    if len(array)<2: return array

    mid=len(array)//2
    left=mergeSort(array[:mid])
    right=mergeSort(array[mid:])

    merged=[]
    l=r=0

    if len(left[l])<len(right[r]):
        merged.append(left[l]);l+=1
    elif len(left[l])==len(right[r]):
        if left[l]<right[r]:
            merged.append(left[l]);l+=1
        elif left[l]==right[r]:
            merged.append(left[l]);l+=1;r+=1
        else:
            merged.append(right[r]);r+=1
    else:
        merged.append(right[r]); r+=1

    while l<len(left) and r<len(right):
        last=merged[-1]

        #정렬 기준
        if len(left[l])<len(right[r]):
            if last!=left[l]:
                merged.append(left[l])
            l+=1

        elif len(left[l])==len(right[r]):
            if left[l]<right[r]:
                if last!=left[l]:
                    merged.append(left[l])
                l+=1
            elif left[l]==right[r]:
                if last!=left[l]:
                    merged.append(left[l])
                l+=1;r+=1
            else:
                if last!=right[r]:
                    merged.append(right[r])
                r+=1
        else:
            if last!=right[r]:
                merged.append(right[r])
            r+=1

    merged+=left[l:]; merged+=right[r:]

    return merged

num=int(sys.stdin.readline())
strList=[]
for i in range(num):
    inputStr=sys.stdin.readline().replace("\n","")
    strList.append(inputStr)

sortedStrList=mergeSort(strList)

print('----------------')
for i in sortedStrList:
    print(i)