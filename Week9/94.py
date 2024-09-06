name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
email_dict = dict()
for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        temp_var = line.split()[1]
        if temp_var not in email_dict:
            email_dict[temp_var] = 1
        elif temp_var in email_dict:
            email_dict[temp_var] = email_dict[temp_var] + 1
print(max(email_dict, key=email_dict.get), max(email_dict.values()))
