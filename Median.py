def MedianOf(arr):
    N = len(arr)
    if N % 2 ==0:
        z = N // 2
        e = arr[z]
        print(e)
        y = arr[z-1]
        meidan = (e + y) / 2
        print(meidan)
    else:
        z = N // 2
        print(arr[z])


arr = [2,5,1,7]
arr.sort()
MedianOf(arr)