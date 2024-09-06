name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
tuple_list = list()
temp_dict = dict()
handle = open(name)
for line in handle:
    if line.startswith("From "):
        temp = line.split()[5]
        temp = temp[0:2]
        temp_dict[temp] = temp_dict.get(temp,0)+1

for value,count in temp_dict.items():
    tuple_list.append((value, count))
tuple_list.sort()
for value, count in tuple_list:
    print(value, count)