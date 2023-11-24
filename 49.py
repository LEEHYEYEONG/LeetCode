import collections

# def groupAnagrams(strs):
#     # 하나하나 단어 오름차순으로 정렬
#     sorted_str = [sorted(i) for i in strs]
    
#     #2차원 배열 중복 제거 
#     sorted_str = list(set(map(tuple, sorted_str)))

#     # 튜플로 중복을 제거한 sorted_str을 키 값으로 사용
#     dict_str = collections.defaultdict(list)
#     for i in range(len(sorted_str)):
#         dict_str[sorted_str[i]]

#     # 정렬한 결과가 키 값과 같은 경우 딕셔너리에 추가 
#     for i in range(len(strs)):
#         for j in range(len(sorted_str)):
#             if (tuple(sorted(strs[i])) == sorted_str[j]):
#                 dict_str[sorted_str[j]].append(strs[i])
    
#     # 애너그램의 수를 기준으로 정렬
#     answer_list = [i for i in list(dict_str.values())]
#     answer_list = sorted(answer_list, key=len)
    
#     return answer_list

def groupAnagrams(strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
        print(''.join(sorted(word)))

    return list(anagrams.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))