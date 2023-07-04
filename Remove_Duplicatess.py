def RemoveEle(arr):
    dict1 ={}
    for i in range(len(arr)):
        if arr[i] in dict1:
            dict1[arr[i]] +=1
        else:
            dict1[arr[i]] =1
    
    for i in dict1:
        print(i ,end=' ')


arr =[ 4, 3, 9, 2, 4, 1, 10, 89, 34 ]
RemoveEle(arr)