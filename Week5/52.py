largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        compare = int(num)
    except:
        print("Invalid input")
    if largest is None:
        largest = compare
    if smallest is None:
        smallest = compare
    if compare > largest:
        largest = compare
        #print(largest)
    if compare < smallest:
        smallest = compare
        #print(smallest)

print("Maximum is", largest)
print("Minimum is", smallest)