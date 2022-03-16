from jovian.pythondsa import evaluate_test_case, evaluate_test_cases


def rotation_temp(nums, d):
    """
    Using Temp array

    :type nums: List[int]
    :type d: int
    :rtype List[int]

    Time Complexity: O(n)
    Auxiliary Space: O(d)
    """
    tmp = nums[:d]
    del nums[:d]
    return nums + tmp


if __name__ == "__main__":
    tests = [
        {
            "input": {"nums": [1, 2, 3, 4, 5, 6, 7], "d": 2},
            "output": [3, 4, 5, 6, 7, 1, 2],
        },
        {
            "input": {"nums": [1, 2, 3, 4, 5, 6, 7], "d": 6},
            "output": [7, 1, 2, 3, 4, 5, 6],
        },
        {
            "input": {"nums": [12, 15, 16, 17, 19, 26, 45], "d": 4},
            "output": [19, 26, 45, 12, 15, 16, 17],
        },
        {
            "input": {"nums": [12, 15, 16, 17, 19, 26, 45], "d": 7},
            "output": [12, 15, 16, 17, 19, 26, 45],
        },
    ]

    print(rotation_temp.__doc__)
    print(evaluate_test_cases(rotation_temp, tests, error_only=True))
