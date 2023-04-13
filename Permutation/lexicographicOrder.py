"""
How it works:
 step 1 find the largest index_1, such a[index_1]<a[index_1 +1], if no such index exists, ths permutation is the last one
 step 2 find the largest index_2, such index_2 > index_1 and a[index_2] > a[index_1]
 step 3 swap a[index_1] and a[index_2]
 step 4 sort the substring from index_1(original) + 1 to end (revese order as the step 1, 2, and 3 sort the order to descending)
"""
"""
Pro:
Iterable, result in lexicographical order
Con:
Not work for non lexicographical arr
"""
"""
Example: original array "ABCDEF"
current permutation "DCFEBA"
step 1 index_1 is 1 (C)
step 2 index_2 is 3 (E)
step 3 swap "DEFCBA" (subarray after index_1 is descending)
step 4 sort (or reverse) "DEABCF"
"""
