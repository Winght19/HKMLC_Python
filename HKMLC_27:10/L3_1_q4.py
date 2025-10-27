"""
expected output:
3
2
5
Volume is: 30 m^3.
"""

"""使用回傳計算體積"""
# 繼續沿用 rectangleArea()
def rectangleArea(length, width):
    …………
# 定義函數 volume()，傳入參數 height、length 、width
def volume(height):
    # 使用 rectangleArea() 回傳的底面積計算體積
    volume = _______ * ________________
    # 回傳體積
    return ________

height = input()
length = _______
width = _______
# 直接使用 volume() 回傳結果
print(f"Volume is: {______________} m^3.")
