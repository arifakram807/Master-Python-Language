# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:

def string_match(str1,str2):
    count=0
    if len(str1)>len(str2):
        l=len(str1)-len(str2)
        for i in range(len(str1) - l-1):
            if (str1[i] == str2[i] and str1[i + 1] == str2[i + 1]):
                count = count + 1
    elif len(str2)>len(str1):
        l=len(str2)-len(str1)
        for i in range(len(str2) - l-1):
            if (str1[i] == str2[i] and str1[i + 1] == str2[i + 1]):
                count = count + 1
    elif len(str2)==len(str1):
        l=len(str1)
        for i in range(l - 1):
            if (str1[i] == str2[i] and str1[i + 1] == str2[i + 1]):
                count = count + 1

    return count
print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))

print(string_match('xxcaazz', 'azbaxx'))




























# Solution
# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     return count
