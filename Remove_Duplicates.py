# Approach 1

def removeDupl(arr):
    N = len(arr)
    s1 = set()
    for i in range(N):
        s1.add(arr[i])
    print(list(s1))



arr = [1,1,2,2,2,3,3]
removeDupl(arr)


# Approach 2 


def RemoveDup(nums):
    j = 0
    N = len(nums)
    for i in range(1 , N):
        if arr[i] != arr[j]:
            arr[j+1] = arr[i]
            j +=1
    
    return j+1

arr = [1,1,2,2,2,3,3]
ans =RemoveDup(arr)
print(ans)
for i in range(ans):
    print(arr[i] , end=' ')