# Python program to merge overlapping Intervals in
# O(n Log n) time and O(1) extra space


def mergeIntervals(arr):
    # Sorting based on the increasing order
    # of the start intervals (sfirst element of each interval)
    arr.sort(key=lambda x: x[0])
    
    # Stores index of last element
    # in output array (modified arr[])
    index = 0

    # Traverse all input Intervals starting from
    # second interval
    for i in range(1, len(arr)):

        # If this is not first Interval and overlaps
        # with the previous one, Merge previous and
        # current Intervals
        if (arr[index][1] >= arr[i][0]):
            arr[index][1] = max(arr[index][1], arr[i][1])
        else:
            index = index + 1
            arr[index] = arr[i]

    print("The Merged Intervals are :", end=" ")
    for i in range(index+1):
        print(arr[i])


arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
mergeIntervals(arr)
arr = [[1, 3], [2, 4], [6, 8], [9, 10]]
mergeIntervals(arr)