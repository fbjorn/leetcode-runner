# Overview

LeetCode solutions runner

[![PyPI Version](https://img.shields.io/pypi/v/leetcode-runner.svg)](https://pypi.org/project/leetcode-runner)
[![PyPI License](https://img.shields.io/pypi/l/leetcode-runner.svg)](https://pypi.org/project/leetcode-runner)

# Installation

Install it directly into an activated virtual environment:

```text
$ pip install leetcode-runner
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add leetcode-runner
```

# Usage

1. Install the library from PyPi
2. Go to [LeetCode](https://leetcode.com) and pick a problem to solve
3. Copy the title slug from the URL (e.g `is-subsequence`) and execute in your terminal:

   ```shell
   leetcode pull is-subsequence
   ```

It will create a file called `392-is-subsequence.py` and you can start coding straight
away!

```shell
python 392-is-subsequence.py
# or like this, depends on how you manage your python
poetry run python 392-is-subsequence.py

------------------------------
[ FAILED ]
s = "abc", t = "ahbgdc"
Expected: True
Actual  : None
------------------------------
[ FAILED ]
s = "axc", t = "ahbgdc"
Expected: False
Actual  : None

Passed: 0/2
```

By default a method `Solution` doesn't do anything, that's why the answer is None. You
need to actually solve the problem 😉.

Please read the next section to undestand how it works and also check the
[limitations](#limitations) section.

# Usage (manual)

This is a legacy way to work with this library

1. Install the library from PyPi
2. Go to [LeetCode](https://leetcode.com) and pick a problem to solve
3. Open your favourite IDE and import the `leetcode_runner`
4. Copy problem samples into some variable, like a `problem`, and copy the base
   `Solution` class that LeetCode provides
5. `LeetCode(problem, Solution).check()` will run these samples!
6. Pass your own samples into `check` function

```py
from leetcode_runner import LeetCode, TestCase, Args
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
        return [1, 2]

LeetCode(problem, Solution).check()
```

Will print:

```text
------------------------------
[ FAILED ]
nums = [2,7,11,15], target = 9
Expected: [0, 1]
Actual  : [1, 2]
------------------------------
[ OK ]
nums = [3,2,4], target = 6
Expected: [1, 2]
Actual  : [1, 2]
------------------------------
[ FAILED ]
nums = [3,3], target = 6
Expected: [0, 1]
Actual  : [1, 2]

Passed: 1/3
```

Providing custom cases is also possible:

```python

lc = LeetCode(problem, Solution)

lc.check(
    extra_cases=[
        TestCase(args=Args(nums=[0, 1, 2], target=3), answer=[1, 2]),
        # or
        TestCase(Args(nums=[0, 1], target=1), [0, 1])
    ]
)

```

## Code snippet

Just copy & paste this in your IDE and start coding:

```python
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """

"""


class Solution:
    pass


LeetCode(PROBLEM, Solution).check(
    extra_cases=[

    ]
)

```

# Requirements

- Python 3.9+

# Limitations

- This tool uses Leetcode's GraphQL API under the hood, I'm not sure how long will it be
  available for public usage
- This tool can download only public problems. Subscription-based requires
  authentication that is currently not implemented

---

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter)
using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).
