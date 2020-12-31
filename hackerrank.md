nested-list
import operator
if __name__ == '__main__':
    inlist = []
    lowest, snd_lowest = 1e10, 1e10+1
    for _ in range(int(input())):
        name = input()
        score = float(input())
        inlist.append((name, score))
        if score < lowest:
            snd_lowest = lowest
            lowest = score
        elif score >= lowest and score < snd_lowest:
            snd_lowest = score
    # print(lowest, snd_lowest)
    
    inlist.sort(key=operator.itemgetter(0))
    for n, s in inlist:
        if s == snd_lowest:
            print(n)
    
"""
Failed with these testset
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
"""
    
    
