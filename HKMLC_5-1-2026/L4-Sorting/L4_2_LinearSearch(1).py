# L4.2 - question + answer
marks = [77, 80, 95, 79, 100, 34, 62, 81]
print("Marks:", marks)

# linear search 1.0
target = int(input())
found = False
for i in range(0, len(mark)):
    if target == mark[i]:
        found = True
print(found)