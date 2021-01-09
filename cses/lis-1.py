def LIS(array):
    n = len(array)
    lis_len = [1] * n
    for k in range(n):
        # array[k] is a LIS of length 1
        lis_len[k] = 1
        for i in range(k+1):
            if array[i] < array[k]:
                # Either
                #       the currently known LIS ended at k        is longer
                #   OR  the LIS ended at array[i] plus array[k]   is longer
                lis_len[k] = max(lis_len[k], lis_len[i] + 1)
    print(lis_len)
    return max(lis_len)


if __name__=='__main__':
    l = LIS([6,2,5,1,7,4,8,3])
    print(l)