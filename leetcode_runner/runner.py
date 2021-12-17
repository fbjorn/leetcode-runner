import re
from typing import List, Optional

from leetcode_runner.log import print_case_summary, print_dashes, print_session_summary
from leetcode_runner.models import TestCase


class LeetCode:
    def __init__(self, problem: str, solution_cls):
        self.solution = solution_cls()
        self.problem = problem
        self.test_cases = self.parse_examples()

    @property
    def fn_name(self):
        attrs = list(vars(self.solution.__class__))
        return [a for a in attrs if not a.startswith("_")][0]

    def parse_examples(self):
        examples = []
        for example in self.problem.split("xampl"):
            match = re.search(
                r"Input:(?P<input>.*)?$\nOutput:(?P<output>.*)?$",
                example,
                flags=re.MULTILINE,
            )
            if match:
                input_str = match.group("input").strip()
                output_str = match.group("output").strip()
                examples.append([input_str, output_str])

        return examples

    @staticmethod
    def eval_output(output: str):
        if output.lower() == "false":
            return False
        if output.lower() == "true":
            return True
        return eval(output)

    def check(self, extra_cases: Optional[List[TestCase]] = None) -> List[bool]:
        extra_cases = extra_cases or []
        results = []

        for input_str, output_str in self.test_cases:
            print_dashes()

            expected = self.eval_output(output_str)
            actual = eval(f"self.solution.{self.fn_name}({input_str})")

            print_case_summary(input_str, actual, expected)
            results.append(actual == expected)

        for test_case in extra_cases:
            print_dashes()
            fn = getattr(self.solution, self.fn_name)
            actual = fn(*test_case.args.args, **test_case.args.kwargs)

            print_case_summary(test_case.args, actual, test_case.answer)
            results.append(actual == test_case.answer)

        print_session_summary(results)
        return results
