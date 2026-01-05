# L4.2 - question + answer
marks = [77, 80, 95, 79, 100, 34, 62, 81]
print("Marks:", marks)

# linear search 2.0
target = int(input())
found = False
i = 0
while (i < len(mark)) and (found == False):
    if target == mark[i]:
        found = True
        i = i + 1
print(found)