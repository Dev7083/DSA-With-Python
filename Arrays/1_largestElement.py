def largest(arr, n):
    max=0
    for i in range(1,n):
        if(arr[i]>max):
            max=arr[i]
    return max

arr=[1,3,6,12,4,41,6,7]
n=len(arr)

print(f"The largest element in the given array is {largest(arr, n)}.")