def binarySearch(array,target):
    left=0
    right=len(array)-1
    while left<=right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

if __name__=="__main__":
    array=[10,20,30,40,50,60]
    print(binarySearch(array,50))
    