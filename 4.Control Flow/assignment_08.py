# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

#Your Code Below:

def sum78(a):
    found7 = False
    found8 = False
    i = 0  # Initialize i to avoid reference before assignment

    # Find the first occurrence of 7
    for i in range(len(a)):
        if a[i] == 7:
            found7 = True
            break

    if found7:
        # Find the first occurrence of 8 after the first 7
        for k in range(i + 1, len(a)):
            if a[k] == 8:
                found8 = True
                break

    if found7 and found8:
        del a[i:k + 1]
        return sum(a)
    else:
        return sum(a)


# Test the function
print(sum78([1, 1, 8, 7, 5, 9, 8, 2]))
print(sum78([1, 2, 2]))
print(sum78([1, 2, 2, 7, 99, 99, 8]))
print(sum78([1, 1, 7, 8, 2]))













#print(sum78([1, 2, 2])) #→ 5
#print(sum78([1, 2, 2, 7, 99, 99, 8])) #→ 5
#print(sum78([1, 1, 7, 8, 2])) #→ 4



























# Solution:

# def sum78(nums):
#     sum = 0
#     inRange = False
#
#     for i in range(len(nums)):
#         if nums[i] == 7:
#             inRange = True
#
#         if not inRange:
#             sum += nums[i]
#
#         if inRange and nums[i] == 8:
#             inRange = False
#
#     return sum