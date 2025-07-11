n = int(input("Enter the number of elements in a list"))
li = input("Enter the elements seperated by ,").split(',')
lists = []
for i in range(n):
    lists.append(int(li[i]))
print(lists)
if len(lists)<3:
    print("Range determination not possible")
else:
    maximum = max(lists)
    minimum = min(lists)
    print(f"The range is {maximum - minimum}")