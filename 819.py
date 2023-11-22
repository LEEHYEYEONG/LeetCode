# import re

# def mostCommonWord(paragraph, banned):
#     # 특수문자 공백으로 치환
#     paragraph = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower()
#     #new_str = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", str)
#     # 다중 공백을 제거하고 1개의 공백만 남기기
#     paragraph = ' '.join(paragraph.split())
#     print(paragraph)
#     # 공백을 기준으로 word_list 생성
#     word_list = [i for i in paragraph.split(" ")]
#     word_num_list = [[i, word_list.count(i)] for i in set(word_list) if i not in banned]
#     max_num = max([i[1] for i in word_num_list])
#     max_word = [i[0] for i in word_num_list if i[1] == max_num]
#     return max_word[0]

import collections
import re

def mostCommonWord(paragraph, banned):
	words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
		
	counts = collections.Counter(words)
	return counts.most_common(1)[0][0]
    
print(mostCommonWord(paragraph = "L, P! X! C; u! P? w! P. G, S? l? X? D. w? m? f? v, x? i. z; x' m! U' M! j? V; l. S! j? r, K. O? k? p? p, H! t! z' X! v. u; F, h; s? X? K. y, Y! L; q! y? j, o? D' y? F' Z; E? W; W' W! n! p' U. N; w? V' y! Q; J, o! T? g? o! N' M? X? w! V. w? o' k. W. y, k; o' m! r; i, n. k, w; U? S? t; O' g' z. V. N? z, W? j! m? W! h; t! V' T! Z? R' w, w? y? y; O' w; r? q. G, V. x? n, Y; Q. s? S. G. f, s! U? l. o! i. L; Z' X! u. y, Q. q; Q, D; V. m. q. s? Y, U; p? u! q? h? O. W' y? Z! x! r. E, R, r' X' V, b. z, x! Q; y, g' j; j. q; W; v' X! J' H? i' o? n, Y. X! x? h? u; T? l! o? z. K' z' s; L? p? V' r. L? Y; V! V' S. t? Z' T' Y. s? i? Y! G? r; Y; T! h! K; M. k. U; A! V? R? C' x! X. M; z' V! w. N. T? Y' w? n, Z, Z? Y' R; V' f; V' I; t? X? Z; l? R, Q! Z. R. R, O. S! w; p' T. u? U! n, V, M. p? Q, O? q' t. B, k. u. H' T; T? S; Y! S! i? q! K' z' S! v; L. x; q; W? m? y, Z! x. y. j? N' R' I? r? V! Z; s, O? s; V, I, e? U' w! T? T! u; U! e? w? z; t! C! z? U, p' p! r. x; U! Z; u! j; T! X! N' F? n! P' t, X. s; q'", banned = ["m","i","s","w","y","d","q","l","a","p","n","t","u","b","o","e","f","g","c","x"]))