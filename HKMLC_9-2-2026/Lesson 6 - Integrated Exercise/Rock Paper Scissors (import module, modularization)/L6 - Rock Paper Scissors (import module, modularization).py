# L6 - Rock Paper Scissors (import module, random, dictionary, modularization)
# L6 - 包剪揼 (匯入模組, random, 字典, 模組化設計)


# 匯入 random 模組
_______ random


# 函數human_move()：玩家輸入
def human_move():
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    # 使用input()接收玩家輸入，int()轉換成數字
    move = ________________________
    # 回傳move
    return _____


# 函數cpu_move()：電腦隨機出招
def cpu_move():
    # 使用.randint()生成[1至3]的數字
    move = random._______(_, _)
    # 回傳move
    return _____


# 函數match(man, cpu)：決鬥比較玩家(man)和電腦(cpu)輸入
def match(man, cpu):
    # 定義字典變量check，以輸入為鍵值，取用對應內容
    check = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
        }
    # 列印你和電腦出什麼
    print(f"You go {check[___]}, Computer goes {check[___]}")
    
    # 平手條件（兩邊一樣）
    if man == cpu:
        print('Draw')
    
    # 勝出條件
    # (石頭 vs 剪刀) or (布 vs 石頭) or (剪刀 vs 布)
    # (Rock vs Scissors) or (Paper vs Rock) or (Scissors vs Paper)
    if (man == 1 and cpu == 3) or (man == __ and cpu == __) or (man______ and cpu______):
        print('You win')
    
    # 落敗條件
    # (石頭 vs ?) or (? vs 剪刀) or (? vs ?)
    # (Rock vs ?) or (? vs scissors) or (? vs ?)
    if (man == 1 and ________) or (________ and cpu == 3) or (________________):
        print('You lose')
        
# 定義變量you和cpu
# 調用human_move()和cpu_move()，直接用其回傳賦值
___ = human_move()
cpu = ________()
# 調用決鬥函數
______(you, cpu)
