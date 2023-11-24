import itertools

def longestPalindrome(s):
    # 팰린드롬 판별 및 투포인터 확장
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    # 해당 사항이 없을 때 빠르게 리턴
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    for i in range(len(s) - 1):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result

    # 문자열 길이가 1이거나 s를 거꾸로 했을 때 같다면 바로 리턴
    # if(len(s) < 2 or s == s[::-1]):
    #     return s
    
    # 조합을 이용해 문자들을 뽑음
    # strs = [list(itertools.combinations(s, i+1)) for i in range(len(s))]
    # 튜플을 배열로 변경
    # strs = [[list(j) for j in i] for i in strs]
    
    # palindrome_list=[]
    # for i in range(len(strs)):
    #     for j in range(len(strs[i])):
    #         word = "".join(strs[i][j])
    #         if(word == word[::-1]):
    #             palindrome_list.append(word)
    
    # return max(palindrome_list, key=len)

print(longestPalindrome("aacabdkacaa"))