from typing import List
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases


def rotation_temp(nums: List[int], d: int) -> List[int]:
    """
    Using Temp array

    :type nums: List[int]
    :type d: int
    :rtype List[int]

    Time Complexity: O(n)
    Auxiliary Space: O(d)
    """
    # (i + d) % len(nums)
    # tmp = nums[:d]
    # del nums[:d]
    # return nums + tmp

    d %= len(nums)
    tmp = [0] * len(nums)
    for index, value in enumerate(nums):
        idx = (index + d) % len(nums)
        tmp.insert(idx, value)
    return tmp


def rotation(nums: List[int], d: int) -> List[int]:
    """
    :type nums: List[int]
    :type d: int
    :rtype List[int]

    Time Complexity: O(n)
    Auxiliary Space: O(1)
    """
    d %= len(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = 0, d - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = d, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    return nums


if __name__ == "__main__":
    tests = [
        {
            "input": {"nums": [1, 2, 3, 4, 5, 6, 7], "d": 2},
            "output": [6, 7, 1, 2, 3, 4, 5],
        },
        {
            "input": {"nums": [1, 2, 3, 4, 5, 6, 7], "d": 6},
            "output": [2, 3, 4, 5, 6, 7, 1],
        },
        {
            "input": {"nums": [12, 15, 16, 17, 19, 26, 45], "d": 4},
            "output": [17, 19, 26, 45, 12, 15, 16],
        },
        {
            "input": {"nums": [12, 15, 16, 17, 19, 26, 45], "d": 7},
            "output": [12, 15, 16, 17, 19, 26, 45],
        },
        {"input": {"nums": [-1, -100, 3, 99], "d": 2}, "output": [3, 99, -1, -100]},
    ]

    print(rotation.__doc__)
    print(evaluate_test_cases(rotation, tests, error_only=True))
