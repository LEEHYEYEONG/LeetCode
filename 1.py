import itertools

def twoSum(nums, target):
    # combinations을 이용하여 2개를 뽑음
    num_list = list(itertools.combinations(nums, 2))
    
    # 합계가 target과 동일하다면 index 반환
    for i in range(len(num_list)):
        if(sum(num_list[i]) == target):
            # 찾는 값이 동일하다면 찾은 다음 그 다음 인덱스부터 찾도록 
            return [nums.index(num_list[i][0]), nums.index(num_list[i][1], nums.index(num_list[i][0])+1)]

# 풀이 1 브루트 포스로 계산
def twoSum(nums, target):
		for i in range(len(nums)):
				for j in range(i + 1, len(nums)):
						if nums[i] + nums[j] == target:
								return [i, j]

# 풀이 2 in을 이용한 탐색
def twoSum(nums, target):
	for i, n in enumerate(nums):
		complement = target - n
		
		if complement in nums[i + 1:]:
		    return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
		
# 풀이 3 첫 번째 수를 뺀 결과 키 조회
def twoSum(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
	
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
	    if target - num in nums_map and i != nums_map[target - num]:
		    return [i, nums_map[target - num]]

# 풀이 4 조회 구조 개선
def twoSum(nums, target):
	nums_map = {}
	# 하나의 for 문으로 통합
	for i, num in enumerate(nums):
		if target - num in nums_map:
			return [nums_map[target - num], i]
		nums_map[num] = i

# 풀이 5 투 포인터 이용
def twoSum(nums, target):
	left, right = 0, len(nums) - 1
	while not left == right:
		# 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
		if nums[left] + nums[right] < target:
			left += 1
		# 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
		elif nums[left] + nums[right] > target:
			right -= 1
		else:
			return [left, right]
		
        	
        
		
    
         