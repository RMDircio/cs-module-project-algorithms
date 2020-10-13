'''
NUMBER ONE:

Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # empty list to store unique element
    unique_num = []
    # loop through list for unique element
    for i in arr:
        # if element is not in list
        if i not in unique_num:
            unique_num.append(i)
    for i in unique_num:
        print i


    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")