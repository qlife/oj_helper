A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

How to handle the divide problem properly

`````python
import math

def solution(X, Y, D):
    way_to_go = Y - X
    m = way_to_go % D
    if m == 0:
        return way_to_go // D
    else:
        return math.floor(way_to_go / D) + 1
`````

Problem: 再次沒有考慮到 degrenerated cases

Using total sum

1. PermMissingElem
Find the missing element in a given permutation.

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

`````python

def solution(A):
    n = len(A)
    if n == 0:
        return 1
    
    sum_1 = (1 + (n+1)) * (n+1) // 2
    sum_2 = sum(A)
    return abs(sum_2 - sum_1)
`````

Prefix / suffix sum

A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].

Scratch
·····
3 1 2 4 3

i=1     2      3      4      

3       3+1    3+1+2 3+1+2+4
1+2+4+3 2+4+3  4+3   4

-1000 1000

-1000
-1000
·····

`````python
def solution(A):
    sum_A = sum(A)
    prefix_sum = [A[0]]
    suffix_sum = [sum_A-A[0]]
    #for i in range(1, len(A)):
    for i in range(1, len(A)-1):
        prefix_sum.append(prefix_sum[-1] + A[i])
        suffix_sum.append(suffix_sum[-1] - A[i])
        # print(prefix_sum, suffix_sum)
    
    min_diff = 1e10
    for i in range(0, len(A)-1):
        diff = abs(prefix_sum[i] - suffix_sum[i])
        if diff < min_diff:
            min_diff = diff

    return min_diff 
`````
FrogRiverOne
Find the earliest time when a frog can jump to the other side of a river.
Task description
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
`````python
def solution(X, A):
    # write your code in Python 3.6
    S = set([])
    S_ans = frozenset([a for a in range(1, X+1)])
    for i in range(0, len(A)):
        S.add(A[i])

        if S_ans <= S:
            return i
    else:
        return -1
`````


Tasks Details

Easy
1. PermCheck
Check whether array A is a permutation.

Task description
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].

`````python
def solution(A):
    N = len(A)
    sumA = sum(A)
    # Checking sum
    if sumA != ((1+N)*N)/2:
        return 0

    sortedA = sorted(A)
    if sortedA[0] != 1:
        # lacking 1
        return 0

    for i in range(1, N):
        if (sortedA[i] - sortedA[i-1]) > 1:
            return 0
    else:
        return 1
`````

Test Cases
`````
[1]
[100000000]
[1,2,2,2,3]
[1,1,1,1,1]
[5, 100000000]
[2,3,4]
`````

`````python

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lenNums = len(nums)
        counts = [0] * lenNums
        for i in range(0, lenNums):
            cntI = 0
            for j in range(i, lenNums):
                if nums[i] > nums[j]:
                    cntI += 1
            counts[i] = cntI
        
        return counts
`````

1. CountDiv
Compute number of integers divisible by k in range [a..b].

Task description
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

None

A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.
Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

`````python
def solution(S, P, Q):

    imF = {'A':1, 'C':2, 'G':3, 'T':4}

    # map the nucleotides into the index within the list
    nuIdx = {'A':0, 'C':1, 'G':2, 'T':3}
    M=[[0, 0, 0, 0]]
    M[0][nuIdx[S[0]]] += 1
   
    for i in range(1, len(S)):
        nextList = [0] * 4
        for j in range(0, 4):
            nextList[j] = M[i-1][j]
        
        idx = nuIdx[S[i]]
        nextList[idx] += 1
        M.append(nextList)

    print(M)

    res = []
    for k in range(0, len(P)):
        pk = P[k]
        qk = Q[k]

        if pk == qk:
            res.append(imF[S[pk]])
            continue
        else:
            # Subtract on the prefix sum of M[pk] and M[qk]
            # Now we have the amounts of nucleotides in between [pk, qk]
            # Checking the existences of any nucleotides from 'A' -> 'C' -> 'G' -> 'T'
            # if found, the minimum impact factor has been decided.

            # See the 'else' parts. Let's why we dicussion pk==0 cases here
            if pk == 0:
                temp = M[qk]
            else:
                # if we subtract M[pk][l], we lost the information contains in M[pk] ..
                temp = [M[qk][l] - M[pk-1][l] for l in range(0, 4)]
            print(temp)
            for l2 in range(0, 4):
                if temp[l2] > 0:
                    # imF == (nuIdx + 1) for all nucleotides
                    res.append(l2+1)
                    break

    return res
`````

`````
["GCGCGC", [1,3], [2, 4]]
["CAGCCTA", [2,5,0],[4,5,6]]
["ATTTATTTTTTTTTTTTT",[0,5],[1,8]
`````

A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

A[0] = 0
A[1] = 1
A[2] = 0
A[3] = 1
A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

class Solution { public int solution(int[] A); }

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

A[0] = 0
A[1] = 1
A[2] = 0
A[3] = 1
A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.

scratch

`````text
A   [0]      [1]     [2]   [3]        [4]
    0        1        0     1         1

0s  1        1        2     2         2
`````

We are recording 'how many zero's in front of the element, including the element itself.
Then sum up the value of 1's counts.

0 car cannot pass with any 0 cars
1 car cannot pass with the 1 cars

Therefore, only consider any 0 appear prior a 1.

`````python
def solution(A):
    cntOfZero = [0]
    for i in range(1, len(A)):
        if A[i-1] == 1:
            cntOfZero.append(cntOfZero[-1])
        else:  # A[i-1] == 0
            cntOfZero.append(1 + cntOfZero[-1])
    
    #print(cntOfZero)

    res = 0
    for j in range(1, len(A)):
        if A[j] == 1:
            res += cntOfZero[j]
    
        if res > 1_000_000_000:
          return -1
    return res
`````
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

A[0] = -3
A[1] = 1
A[2] = 2
A[3] = -2
A[4] = 5
A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

A[0] = -3
A[1] = 1
A[2] = 2
A[3] = -2
A[4] = 5
A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].

Solution

After sorting, the first three elements sortedA[0..2] will have `10` different cases, as 
some of the combinations was conflicts to the assumption of a sorted array, e.g. `[-,0,+]`.

We are finding a triplet that has maximal value, which means:

`````text
+ +  +
+ - -
0 * to anything
- - -  hopless cases
`````
Therefore, we may pick the first and the last three elements and cover all these possible cases.

`````python
def solution(A):
    sA = sorted(A, reverse=True)

    if sA[0] > 0:
        return max(sA[0] * sA[1] * sA[2], sA[0] * sA[-2] * sA[-1])
    else: # sA[0] <= 0
        return max(sA[0] * sA[1] * sA[2], sA[-3] * sA[-2] * sA[-1])
`````

`````text
[2,3,4,0,0,-5]
[1,0,3,0,0,-5]
[1,-2,3,1,1,-5]
[2,0,0,-2,-2,-2]
[2,-4,-4]
[0,0,0,-1,-2,-3]
[0,-1,-2,-3]
[-1,-1,-1]
`````

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

`````python
# O(nlgn) solution
def solution(A):
    s = frozenset([a for a in A if a > 0])

    if len(s) == 0:
        return 1
    else:
        m = max(s)

    # t = SET({ 1, .. , M, (M+1) })
    t = frozenset(range(1, m+2))
    d = t - s
    return min(d)
`````

The latest test datasets.

`````text
[-1000, -3, -2, -1, 0, 1, 2, 5, 9]
[-1000, 1000]
[-1000]
[-1000, 0]
[0, 0, 0]
[-1000, -999, 0]
[1, 2, 3]
[2, 5, 8]
list(range(2, 10001))
(list(range(1, 10000))
`````

Previously used datasets. Looks like I've not catch the points.

`````text
[-352, 53, -439, 215, 977, -352, 623, -349, 878, 413, 839, 707, -265, 275, 587, 800, 314, 215, -628, -727, 623, -766, -379, 770, -907, 524, 581, 866, -193, 962, 176, 920, 47, 431, 785, -787, 494, -598, 905, -40, -598, 764, -451, -79, -979, 260, 338, -22, 383, -970, -79, 611, 188, -367, 776, -931, -625, -319, -637, -244, 356, -883, -346, 965, 902, -526, 629, 14, -424, -871, -157, 218, -616, -586, 416, -46, 461, -976, -7, -511, 851, -952, -610, -121, 626, -286, -658, -484, -865, 878, 848, 722, 653, -550, -991, -649, -961, 365, 116, -139]
[-4, -2,0,1]
[0,0,0,0,0]
[-8, 6, -7]
[-3,-2,-1,0,7]
[-3,-2,-1,0,1]
[-1999, 1]
[-199, 2]
[-3,-2,-1,1,2,3]
[-10000]
[100000]
[0]
[1]
[2]
`````

An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

A[0] = 3    A[1] = 4    A[2] =  3
A[3] = 2    A[4] = 3    A[5] = -1
A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

A[0] = 3    A[1] = 4    A[2] =  3
A[3] = 2    A[4] = 3    A[5] = -1
A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

`````python
def solution(A):
    n = len(A)
    # Handle extremely small cases
    if n == 1:
        return 0
    elif n == 0 or n == 2:
        return -1

    leader = -(2**32)-1
    sSeq = sorted(A)
    # Pick the candidates of leader from non-decreasing seqeuences
    candi = sSeq[n // 2]
    count = 0
    for i in range(0, n):
        if sSeq[i] == candi:
            count += 1
    
    if count > (n // 2):
        # Now we are sure the candidate is the leader of A
        leader = candi

        # As what the problem asing, finding the index
        for j in range(0, n):
            if A[j] == leader:
                return j
    else:
        # the candidates is not a leader, return -1
        return -1
`````

`````text
[]
[-1000000]
[1,2]
[1,2,1]
`````

NumberOfDiscIntersections
Compute the number of intersections in a sequence of discs.

Task description
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

A[0] = 1
A[1] = 5
A[2] = 2
A[3] = 1
A[4] = 4
A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].

Solution


`````python
def solution(A):
    events = []
    for i, r in enumerate(A):
        # Enter the disk range!
        events.append((i-r, 1))
        # Leave the disk range!
        events.append((i+r, -1))

    # x[0] small to big
    # x[1] beginning should be in front of the endpoints
    events.sort(key=lambda x: (x[0], -x[1]))
    # print(events)

    intersections, active_circles = 0, 0
    for _, delta in events:
        # if the delta > 0, then count the sum in
        # otherwise, don't count it.
        # 
        # This is the branchless code:
        # intersections += active_circles * (delta > 0)
        if delta > 0:
            intersections += active_circles

        # Update the active_circles
        active_circles += delta
        if intersections > 10e6:
            return -1
    return intersections
`````

A solution from [http://www.lucainvernizzi.net/blog/2014/11/21/codility-beta-challenge-number-of-disc-intersections/] 

Take away: usage of assert and * (+1 | -1)

`````python

def solution(A):
    events = []
    for i, a in enumerate(A):
        events += [(i-a, +1), (i+a, -1)]
    events.sort(key=lambda x: (x[0], -x[1]))
    intersections, active_circles = 0, 0
    for _, circle_count_delta in events:
        intersections += active_circles * (circle_count_delta > 0)
        active_circles += circle_count_delta
        if intersections > 10E6:
            return -1
    return intersections


if __name__ == '__main__':
    print 'Start tests..'
    assert solution([1, 5, 2, 1, 4, 0]) == 11
    assert solution([]) == 0
    assert solution([0,1]) == 1
    assert solution([0, 0]) == 0
    assert solution([1,0,0,3]) == 4
    print 'Ok!'
`````