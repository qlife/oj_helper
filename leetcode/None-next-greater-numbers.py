def solution(nums):
    """
    The most fundamental form of monotonic stack
    :param nums: input arrays
    :return: next greater numers of nums[i] in nums
    """
    st = []
    ns = len(nums)
    res = []
    for i in range(ns-1, -1, -1):

        # We are interesting in "next greater elements"
        # Therefore, we put element backward.
        # Just like we process postfix expression forward
        #
        # if stack is non-empty
        #    and the stack top is less or equal the nums[i]
        #    THEN we are not interesting in it.

        while st and st[-1] <= nums[i]:
            st.pop()

        # Now the stack top is the next-greater.
        # If stack is empty, then none of next-greater of nums[i] is ever existed
        if st:
            res.insert(0, st[-1])
        else:
            res.insert(0, -1)

        # Special Q:
        # if we have nums = [2, 4, 3, 7, 2, 9] for i, when i = 1 ?
        # stack should be [9, 7], then top is 7

        # push nums[i] for the next iteration
        st.append(nums[i])

    return res


if __name__ == '__main__':
    # [4,2,4,-1,-1]
    print(solution([2, 1, 2, 4, 3]))
    # [4, 7, 7, 9, 9, -1]
    print(solution([2, 4, 3, 7, 2, 9]))
