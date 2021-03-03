def solution(nums, target, triplets):
    nums.sort()

    def find_all_triplets(nums, target, triplets=[], curr_comb=[], begin=0):
        if len(curr_comb) == 3:
            triplets.append(curr_comb.copy())
            return

        i = begin
        # Cond.1  i < len(nums)   Cond.2 nums[i] <= target, thus, meaning full to put into solution
        while i < len(nums) and nums[i] <= target:
            curr_comb.append(nums[i])
            find_all_triplets(nums, target-nums[i], triplets, curr_comb, i + 1)
            curr_comb.pop()
            i = i + 1

    find_all_triplets(nums, target, triplets)


if __name__ == '__main__':
    nums = [2, 7, 4, 9, 5, 1, 3]  # 1 2 3 4 5 7 9
    target = 10
    triplets = []

    solution(nums, target, triplets)
    print(triplets)
    # [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 7], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5]]
