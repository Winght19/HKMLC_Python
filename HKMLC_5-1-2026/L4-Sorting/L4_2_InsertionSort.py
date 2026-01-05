# L4.2 - question + answer
marks = [77, 80, 95, 79, 100, 34, 62, 81]
print("Marks:", marks)

# insertion sort
for i in range(1, len(marks)):
    key = ______
    j = _____
    while j >= 0 and key < marks[j]:
        marks[j+1] = _______
        j = j - 1
    marks[j+1] = key
    
print("Marks:", marks)