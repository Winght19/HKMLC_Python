# L4.2 - question + answer
marks = [77, 80, 95, 79, 100, 34, 62, 81]
print("Marks:", marks)

# linear search 3.0
target = int(input())
index = -1
for i in range(0, len(mark)):
    if target == mark[i]:
        index = i
        print(i)
if index == -1:
    print("No result is found.")
