# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
val = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    pos = line.find('0')
    val = val + float(line[pos:])
    count = count + 1
final = str(val/count)
print("Average spam confidence: " + final)
