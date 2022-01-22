the_file = open('mbox-short.txt')

"""
Gets each email address from the text
"""
# for line in the_file:
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print(line)

#another way to do the same:

# for line in the_file:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

"""
Counting the lines
"""
# count = 0
# for line in the_file:
#     count = count + 1
# print('Line count: ', count)

"""
1) How many characters
2) Print first 20 characters
"""
# inp = the_file.read()
# print(len(inp))

# print(inp[:20])

