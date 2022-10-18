from typing import List

from leetcode_runner import Args, LeetCode, TestCase

from .problems import P1_TWO_SUMS, P10_REGEXP_MATCHING


def test_parse_p1_two_sums():
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            return []

    lc = LeetCode(P1_TWO_SUMS, Solution)
    assert lc.test_cases == [
        ["nums = [2,7,11,15], target = 9", "[0,1]"],
        ["nums = [3,2,4], target = 6", "[1,2]"],
        ["nums = [3,3], target = 6", "[0,1]"],
    ]

    answers = lc.check()
    assert answers == [False, False, False]

    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            return [0, 1]

    lc = LeetCode(P1_TWO_SUMS, Solution)
    answers = lc.check()
    assert answers == [True, False, True]


def test_parse_p10_regexp_matching():
    class Solution:
        def isMatch(self, s: str, p: str) -> bool:
            return True

    lc = LeetCode(P10_REGEXP_MATCHING, Solution)
    assert lc.test_cases == [
        ['s = "aa", p = "a"', "false"],
        ['s = "aa", p = "a*"', "true"],
        ['s = "ab", p = ".*"', "true"],
    ]

    answers = lc.check()
    assert answers == [False, True, True]


def test_extra_examples():
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            return [1, 2]

    lc = LeetCode(P1_TWO_SUMS, Solution)

    answers = lc.check(
        extra_cases=[TestCase(args=Args(nums=[0, 1, 2], target=3), answer=[1, 2])]
    )
    assert answers == [False, True, False, True]
