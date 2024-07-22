# Assignment 1:

import sys

directory_containing_files = "C://Users//sajid//Downloads//PythonCourse-master//PythonCourse-master//6.File IO and Exception Handling in Python//project_files" #sys.argv[1]
words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]
directory_containing_files = sys.argv[1]
words_to_aggregate = sys.argv[2:]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:

words_and_counts = {}

for word in words_to_aggregate:
    count = 0
    for path, folder_names, file_names in os.walk(directory_containing_files):
        for file_name in file_names:
            file = os.path.join(path, file_name)
            with open(file, "r") as a_file:
                for line in a_file:
                    if re.search(word, line):
                        word_list = re.findall(word, line)
                        count += len(word_list)
    words_and_counts[word] = count

print(words_and_counts)













































#Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)