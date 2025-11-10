# L4.2 - question + answer
marks_2 = [51, 55, 62, 63, 87, 91, 97, 100]

# 目標分數（91分）
target = 91
# 初始化索引值
start =  ____________________________ 
end = ____________________________
# 初始化布林值
found = ____________________________

# 對分檢索循環
while start <= end and found == False:
	# 取中間點（整數）
	mid = ____________________________
	# 檢查中間點是否等於目標值
	if marks_2[mid] == target:
		found = ____________________________
	else:
		# 如果中間點非目標，更新索引指標範圍
		if target < marks_2[mid]:
			end = ____________________________
		else:
			start = ____________________________

# 列印結果
if found == True:
	# 找到的話：中間點就應該等於目標
	print("Found at index", mid)
else:
	# 找不到
	print("Not found")
