fname = input("Enter file name: ")
fh = open(fname)
new_list = []
lst = list()
for line in fh:
    for word in line.split():
        if word.strip() not in new_list:
            new_list.append(word.strip())
new_list.sort()
print(new_list)
