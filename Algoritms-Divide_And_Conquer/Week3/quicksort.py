# Quick Sort chooses a random pivot number and moves all elements that are smaller than it
# to the left and values larger to the right. 
# By using two variables to keep track of where the last smallest value is and one to traverse the array.
# Once it reaches the end of the array, the pivot value should swap with the "right-most" smaller value.
def quickSort(nums, pivot):
    comparisons = quickSortHelp(nums, 0, len(nums), pivot)
    return comparisons

def quickSortHelp(nums, low, high, pivot):
    comparisons = 0
    if(low < high):
        pivot_location, comparisons = partition(nums, low, high, pivot)
        comparisons += quickSortHelp(nums, low, pivot_location, pivot)
        comparisons += quickSortHelp(nums, pivot_location + 1, high, pivot)
    return comparisons

def partition(nums, low, high, pivot):
    #pivot = ChoosePivot(nums, low, high
    if pivot == "low":
        i, comparisons = partitionHelp(nums, low, high)
    elif pivot == "high":
        swap(nums, low, high - 1)
        i, comparisons = partitionHelp(nums, low, high)
    else:
        choosePivot(nums, low, high - 1)
        i, comparisons = partitionHelp(nums, low, high)
    return i, comparisons


def swap(arr, first, last):
    temp = arr[first];
    arr[first] = arr[last];
    arr[last] = temp;

def partitionHelp(nums, low, high):
    pivot = low
    i = low
    comparisons = high - low - 1
    for j in range(low, high):
        if nums[j] == nums[pivot]:
            i += 1
            continue
        elif nums[j] < nums[pivot]:
            swap(nums, i, j)
            i += 1
    swap(nums, i - 1, pivot)
    return i - 1, comparisons

# Take the three indices and swap values so that the value in the middle of the array is the median of values
# Swap middle value with first element so we can have pivot at the beginning on the list
def choosePivot(arr, first, last):
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
    swap(arr, first, position)


list = [int(line) for line in open("QuickSort.txt")]
# list = [4,1,2,5,3]
#quickSort(list, "low") 
#quickSort(list, "high") 
quickSort(list, "mid")