# L5

"""讀取文字檔案 - 請打開Thonny一起做"""

"""第二步：撰寫 .py 程式"""
# 建立變量 file
# 用 open() 開啟文字檔 datafile.txt，讀取模式
file = open("________", ___)
# 用 .read() 讀取文檔內容
content = file.______
# 用 .close() 關閉文檔
file.________
# 列印內容和內容類型
print(content)
print(______content__)


"""第三步：更多讀取方式"""
file = open("datafile.txt", ___)
# 用 .readline() 讀取文檔內容
line1 = file._________
line2 = file._________
line3 = file._________
# 關閉文檔
file._______

file = open("datafile.txt", ___)
# 用 .readlines() 讀取文檔內容
content_2 = file.___________
# 關閉文檔
file._______


"""寫入文字檔案 - 請打開Thonny一起做"""

"""第二步：覆寫文檔內容"""
# 建立想寫入的內容變量
content_1 = "Python is the best !"

# 用 open() 開啟 output.txt，覆寫模式 “w”
file = _____"output.txt", ____

# 用 .write() 寫入文檔內容
file.write(_________)

# 用 .close() 關閉文檔
file._______


"""第三步：添加文檔內容"""
# 建立想寫入的內容變量（列表）
content_2 = ["apple \n",
             "banana \n",
             "cherry \n"]

# 用 with...as 開啟 output.txt，添加模式 “a”
____ open(____________) __ ____:
    # 用 .writelines() 寫入每行內容
    file.________content_2_

