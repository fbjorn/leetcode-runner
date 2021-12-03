# Overview

⚠️ Work in progress

LeetCode solutions runner

[![PyPI Version](https://img.shields.io/pypi/v/leetcode-runner.svg)](https://pypi.org/project/leetcode-runner)
[![PyPI License](https://img.shields.io/pypi/l/leetcode-runner.svg)](https://pypi.org/project/leetcode-runner)

# Usage

```py
from leetcode_runner import LeetCode 
from typing import *

# Copied as is from the LeetCode
problem = """
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return []

LeetCode(problem, Solution).check()
```

Will print:

```text
----------
[ FAILED ]
nums = [2,7,11,15], target = 9
Expected: [0, 1]
Actual  : []
----------
[ FAILED ]
nums = [3,2,4], target = 6
Expected: [1, 2]
Actual  : []
----------
[ FAILED ]
nums = [3,3], target = 6
Expected: [0, 1]
Actual  : []

```

# Setup

## Requirements

* Python 3.9+

## Installation

Install it directly into an activated virtual environment:

```text
$ pip install leetcode-runner
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add leetcode-runner
```


---

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).
