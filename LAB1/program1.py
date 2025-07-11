lists = [2,7,4,1,3,6]
count = 0
for i in range(len(lists)):
    for j in range(i+1,len(lists)):
        if lists[i]+lists[j]==10:
            print(f"({lists[i]},{lists[j]})")
            count=count+1
print(f"Number of pairs that add up to sum 10 are {count}")