import sys

def mergeSort(array):
    if len(array)<2: return array

    mid=len(array)//2
    left=mergeSort(array[:mid])
    right=mergeSort(array[mid:])
    
    merged=[]
    l=r=0
    while l<len(left) and r<len(right):
        if left[l][0]<=right[r][0]:
            merged.append(left[l]); l+=1
        else:
            merged.append(right[r]); r+=1

    merged+=left[l:]; merged+=right[r:]

    return merged

num=int(sys.stdin.readline())

members=[]
for i in range(num):
    inputStr=sys.stdin.readline()
    inputStr=inputStr.replace("\n","")
    age,name=inputStr.split()

    age=int(age)
    members.append((age,name))

sortedMembers=mergeSort(members)
for i in sortedMembers:
    print(i[0],i[1])


