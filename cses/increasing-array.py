def solution():
    n = int(input())
    nums = list(map(int, input().split()))

    diff = 0
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            diff += abs(nums[i-1] - nums[i])
            nums[i] = nums[i-1]

    print(diff)


if __name__ == '__main__':
    solution()
