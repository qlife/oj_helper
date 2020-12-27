# More than 2 lines will result in 0 score. Do not leave a blank line also

for i in range(1, int(input())+1):
    print(sep='', *([j for j in range(1, i)] + [i] + [k for k in range(i - 1, 0, -1)]))


    # print(''.join(map(str,[j for j in range(1, i)] + [i] + [k for k in range(i-1, 0, -1)])))