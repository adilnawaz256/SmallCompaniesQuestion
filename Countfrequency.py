#Approch 1  using HashMap or dictionary 
def CountFre(arr):
    dict1 = {}
    for i in range(len(arr)):
        if arr[i] in dict1:
            dict1[arr[i]] +=1
        else:
            dict1[arr[i]] = 1
    for i in dict1:
        print(i, dict1[i])



arr = [10,5,10,15,10,5]
CountFre(arr)

#Approach 2 

print("*****************************")

def CountFrequency(nums):
    N = len(nums)
    vistied = [False] * N
    for i in range(N):
        if vistied[i] == True:
            continue
        count =  1
        for j in range(i+1 , N):
            if nums[i] == nums[j]:
                vistied[j] = True
                count +=1
        print(nums[i] , count)



nums = [10,5,10,15,10,5]
CountFrequency(nums)