import re

name = input("Enter the file to use: ")
if len(name) < 1:
    name = "./regex_sum_2081224.txt"
nums = 0
file = open(name)
for line in file:
    temp = re.findall('[0-9]+', line)
    if len(temp) > 0:
        for i in temp:
            nums = nums + int(i)
print(nums)