def sliding_window(arr,k):
    max_sum=0
    max_start=0
    length=len(arr)

    #sum of first sub array

    window_sum=sum(arr[:k])
    max_sum=window_sum

    for i in range(length-k):
        window_sum=window_sum-arr[i]+arr[i+k]

        if window_sum>max_sum:
            max_sum=window_sum
            max_start=i+1

    return print(f"Max sum is:{max_sum} and max sum sub array is: {arr[max_start:max_start+k]}")

if(__name__=="__main__"):
    arr = [5, 2, -1, 0, 3]
    k = 3
    sliding_window(arr,k)