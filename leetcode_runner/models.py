class Args:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class TestCase:
    def __init__(self, args: Args, answer):
        self.args = args
        self.answer = answer
