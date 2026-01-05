# L4.2 - question + answer
marks = [77, 80, 95, 79, 100, 34, 62, 81]
print("Marks:", marks)

# bubble sort
for i in range(0, len(marks)-1):
    for j in range(0, len(marks)-1-i):
        if marks[j] > marks[j+1]:
            temp = marks[j]
            marks[j] = marks[j+1]
            marks[j+1] = temp
    
print("Marks:", marks)