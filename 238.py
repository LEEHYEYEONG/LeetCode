# Time Limit Exceeded
# def productExceptSelf(nums):
#     answer = []
#     nums_copy = nums[:]

#     for i in nums:
#         nums_copy.pop(nums.index(i))
#         multiple = 1
#         for j in nums_copy:
#             multiple *= j
#         answer.append(multiple) 
#         nums_copy = nums[:]

#     return answer

# Time Limit Exceeded
# import functools 

# def multiply(arr):
#     return functools.reduce(lambda x, y: x * y, arr)

# def productExceptSelf(nums):
#     answer = []
#     nums_copy = nums[:]

#     for i in nums:
#         nums_copy.pop(nums.index(i))
#         answer.append(multiply(nums_copy))
#         nums_copy = nums[:]

#     return answer

# Time Limit Exceeded
# def productExceptSelf(nums):
#     answer = []
#     for i in range(len(nums)):
#         multiple = 1
#         for j in range(len(nums)):
#             if i == j:
#                 continue
#             multiple *= nums[j]
#         answer.append(multiple)
    
#     return answer

# 풀이 1 왼쪽 곱셈 결과에 오른쪽 곱셈 값을 차례대로 곱셈
def productExceptSelf(nums):
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out 

print(productExceptSelf([-1,1,0,-3,3]))