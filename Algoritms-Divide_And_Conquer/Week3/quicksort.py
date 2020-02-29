# Quick Sort chooses a random pivot number and moves all elements that are smaller than it
# to the left and values larger to the right. 
# By using two variables to keep track of where the last smallest value is and one to traverse the array.
# Once it reaches the end of the array, the pivot value should swap with the "right-most" smaller value.
def QuickSort(nums):
    comparisons = QuickSortHelp(nums, 0, len(nums))
    return nums, comparisons

def QuickSortHelp(nums, low, high):
    comparisons = 0
    if(low < high):
        pivot_location, comparisons = Partition(nums, low, high)
        comparisons += QuickSortHelp(nums, low, pivot_location)
        comparisons += QuickSortHelp(nums, pivot_location + 1, high)
    return comparisons

def Partition(nums, low, high):
    #pivot = ChoosePivot(nums, low, high)
    pivot = low
    i = low + 1
    comparisons = high - low - 1
    for j in range(low + 1, high):
        if nums[j] < nums[pivot]:
            Swap(nums, i, j)
            i += 1
    Swap(nums, i - 1, pivot)
    return i - 1, comparisons

def Swap(arr, first, last):
    temp = arr[first];
    arr[first] = arr[last];
    arr[last] = temp;

# Take the three indices and swap values so that the value in the middle of the array is the median of values
# Swap middle value with first element so we can have pivot at the beginning on the list
def ChoosePivot(arr, first, last):
    position = 0
    mid = int((first + last) / 2);
    if arr[first] < arr[last]:
        if arr[first] > arr[mid]:
            position = first
        elif arr[mid] > arr[last]:
            position = last
        else:
            position = mid
    else:
        if arr[first] < arr[mid]:
            position = first
        elif arr[mid] < arr[last]:
            position = last
        else:
            position = mid
    return position
list = [4,5,2,3,1]
QuickSort(list)