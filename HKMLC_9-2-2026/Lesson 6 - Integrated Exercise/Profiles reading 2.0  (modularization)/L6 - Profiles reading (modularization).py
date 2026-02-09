# L6 - Profiles reading 2.0 (modularization)
# L6 - 個人檔案讀取 2.0 (模組化設計)

# 初始化變量
names = ['Alan', 'Ben', 'Cindy', 'Daisy']
genders = []
ages = []

# trimG():將性別一欄無關的資訊刪掉
def trimG(gender):
    # 使用.strip()移除不要的字符
    gender = gender.strip('Gender: ')
    gender = gender._____('\n')
    return _______
    
# trimA():將年齡一欄無關的資訊刪掉+轉換成int()
def trimA(age):
    # 使用.strip()移除不要的字符
    age = age.______('Age: ')
    age = age.______(____)
    # 使用int()轉化類型
    age = ______
    return _______

# swap():將一張列表內的兩個項目對調
def swap(list, large, small):
    # 使用temp幫助進行對調
    temp = __________
    list[large] = ___________
    list[small] = ___________
    # 回傳已更改的列表
    _____________

# 用for name in names和'.txt'讀取不同人檔案
for name in names:
    with open(____ + '.txt', 'r') as file:
        # 使用.readline()從行讀取性別和年齡內容
        gender = file.readline()
        age = file.___________
        
        # 使用.append()直接添加trimG()和trimA()回傳
        genders._______(trimG(gender))
        ages.append(______________)

print('Original:')
print(names)
print(genders)
print(ages)


# 冒泡排序法 Bubble sort
for i in range(___, len(ages)-1):
    for j in range(0, ________________):
        # 用年齡(age)比較
        if ages[_] > ages[j+1]:
            # 調用swap()更改names, genders, ages列表排序
            names = swap(_____, j, ___)
            genders = swap(________, ___, j+1)
            ages = _____________________

print('Sorted by age in acsending:')
print(names)
print(ages)
print(genders)
