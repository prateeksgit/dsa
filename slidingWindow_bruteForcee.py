def sldingWindow(arr,k):
    max_sum=0
    length=len(arr)
    for i in range(length-k+1):
        current_sum=0
        for j in range(k):
            current_sum+=arr[i+j]
        max_sum=max(current_sum,max_sum)
    return max_sum



if(__name__=="__main__"):
    arr = [5, 2, -1, 0, 3]
    k = 3
    print(sldingWindow(arr,k))