import sys


def maximum_pairwise(nums):
    max_num_1 = max(nums)
    nums.remove(max_num_1)
    max_num_2 = max(nums)
    return max_num_1*max_num_2


if __name__ == "__main__":
    input = sys.stdin.read()
    input_nums = input.split()
    nums = [int(i) for i in input_nums[1:]]
    print(maximum_pairwise(nums))
