# Quick Sort chooses a random pivot number and moves all elements that are smaller than it
# to the left and values larger to the right. 
# By using two variables to keep track of where the last smallest value is and one to traverse the array.
# Once it reaches the end of the array, the pivot value should swap with the "right-most" smaller value.
def QuickSort(nums, pivot):
    comparisons = QuickSortHelp(nums, 0, len(nums), pivot)
    return nums, comparisons

def QuickSortHelp(nums, low, high, pivot):
    comparisons = 0
    if(low < high):
        pivot_location, comparisons = Partition(nums, low, high, pivot)
        comparisons += QuickSortHelp(nums, low, pivot_location, pivot)
        comparisons += QuickSortHelp(nums, pivot_location + 1, high, pivot)
    return comparisons

def Partition(nums, low, high, pivot):
    #pivot = ChoosePivot(nums, low, high)
    i = low
    comparisons = high - low - 1
    if pivot == "low":
        pivot = low
        i += 1
        for j in range(low + 1, high):
            if nums[j] < nums[pivot]:
                Swap(nums, i, j)
                i += 1
        Swap(nums, i - 1, pivot)
        return i - 1, comparisons
    elif pivot == "high":
        pivot = high - 1
        for j in range (low, high - 1):
            if nums[j] < nums[pivot]:
                Swap(nums, i, j)
                i += 1
        Swap(nums, i, pivot)
        print(nums)
        return i, comparisons
    else:
        pivot = ChoosePivot(nums, low, high)


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


#list = [int(line) for line in open("QuickSort.txt")]
list = [4,3,2,5,1]
QuickSort(list, "high")
