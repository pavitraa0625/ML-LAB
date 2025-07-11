import random 
import statistics 
lists = []
for _ in range(25):
    lists.append(random.randint(1,10))
means = statistics.mean(lists)
print(f"Mean: {means}")
mode = statistics.mode(lists)
print(f"Mode: {mode}")
median = statistics.median(lists)
print(f"Median: {median}")