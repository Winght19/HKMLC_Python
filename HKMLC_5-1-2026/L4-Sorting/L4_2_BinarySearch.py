# L4.2 - question + answer
marks_2 = [51, 55, 62, 63, 87, 91, 97, 100]

# 目標分數（91分）

# 初始化索引值


# 初始化布林值


# 對分檢索循環
while _____ and _____:
	# 取中間點（整數）
	mid = _______
	# 檢查中間點是否等於目標值
	if marks_2[mid] ________:
		found = True
	else:
		# 如果中間點非目標，更新索引指標範圍
		if _______:
			end = mid - 1
		else:
			_______

# 列印結果
if found == True:
	# 找到的話：中間點就應該等於目標
	print("Found at index", mid)
else:
	# 找不到
	print("Not found")
