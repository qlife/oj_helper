def find_all_triplet(nums, target, solution_set, curr_set, begin):
    if len(curr_set) == 3:
        solution_set.append(curr_set.copy())
        print(curr_set)
        return

    i = begin
    while i < len(nums) and nums[i] <= target:
        curr_set.append(nums[i])
        find_all_triplet(nums, target-nums[i], solution_set, curr_set, i + 1)
        curr_set.pop()    # pop last
        i += 1


if __name__ == '__main__':
    array = [2, 7, 4, 9, 5, 1, 3]  # 1 2 3 4 5 7 9
    x = 10
    sol_set = []
    array.sort()
    find_all_triplet(array, x, sol_set, [], 0)
    print(sol_set)

