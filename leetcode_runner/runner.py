import re


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

    def check(self):
        for input_str, output_str in self.test_cases:
            print("-" * 10)

            expected = self.eval_output(output_str)
            actual = eval(f"self.solution.{self.fn_name}({input_str})")

            if actual != expected:
                print("[ FAILED ]")

            print(input_str)
            print("Expected:", expected)
            print("Actual  :", actual)
