from typing import List
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases


def findIndex_linear(nums: List[int], target: int) -> int:
    """
    :type nums: List[int]
    :type target: int
    :rtype List[int]

    Time Complexity: O(n)
    Auxiliary Space: O(1)
    """
    for index, value in enumerate(nums):
        if value == target:
            return index
    return -1


def findIndex(nums: List[int], target: int) -> int:
    """
    :type nums: List[int]
    :type target: int
    :rtype List[int]

    Time Complexity: O(log(n))
    Auxiliary Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid

        # left sorted portion
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        # right sorted portion
        else:
            if target < nums[mid] or target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == "__main__":
    tests = [
        {
            "input": {"nums": [5, 6, 7, 8, 9, 10, 1, 2, 3], "target": 3},
            "output": 8,
        },
        {
            "input": {"nums": [5, 6, 7, 8, 9, 10, 1, 2, 3], "target": 30},
            "output": -1,
        },
        {
            "input": {"nums": [30, 40, 50, 10, 20], "target": 10},
            "output": 3,
        },
    ]

    print(findIndex.__doc__)
    print(evaluate_test_cases(findIndex, tests, error_only=True))
