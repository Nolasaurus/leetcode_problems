class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int):

        soldiers = dict()
        ix = 0
        for row in mat:

            soldiers[ix] = sum(row)
            ix += 1

        ## sort dictionary by value
        weak_sorted =  {k: v for k, v in sorted(soldiers.items(), key=lambda item: item[1])}
        weakest = []

        for i in range(k):
            weakest.append(list(weak_sorted.keys())[i])

        return weakest

test = Solution()
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
corr = [2,0,3]

print(test.kWeakestRows(mat, k))

"""
You are given an m x n binary matrix mat of 1's 
(representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's
 in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of
 soldiers in row j.
Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the
 matrix ordered from weakest to strongest.
"""