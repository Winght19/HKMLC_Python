# L4.2 - question + answer
marks = [77, 80, 95, 79, 100, 34, 62, 81]
print("Marks:", marks)

# insertion sort
for i in range(1, len(marks)):
    key = marks[i]
    j = i-1
    while j >= 0 and key < marks[j]:
        marks[j+1] = marks[j]
        j = j - 1
    marks[j+1] = key
    
print("Marks:", marks)