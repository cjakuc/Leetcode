# Function for finding the first
# missing positive number
def firstMissingPositive(arr, n):

    # Loop to traverse the whole array
    for i in range(n):

        # Loop to check boundary
        # condition and for swapping
        while (arr[i] >= 1 and arr[i] <= n
            and arr[i] != arr[arr[i] - 1]):
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp
    breakpoint()
    # Checking any element which
    # is not equal to i + 1
    for i in range(n):
        if (arr[i] != i + 1):
            return i + 1

    # Nothing is present return last index
    return n + 1


# Driver code
if __name__ == '__main__':
    arr = [0, 10, 2, -10, -20]
    n = len(arr)
    ans = firstMissingPositive(arr, n)
    print(ans)