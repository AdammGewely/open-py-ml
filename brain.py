"""
Some stuff for machine learning brains.
"""

import difflib


class Brain:
    """
    A brain. An Artificial intelligence (AI)'s data and runner.
    Data: First argument in __init__(), Data is for the training data key/values
    Threshold: Second argument in __init(), Threshold is for the percentage of which the AI finds
    That the data is simular enough to the input string of which it is accepted
    NOTE: This only works with strings now.
    """
    data: dict or None
    threshold: float

    def __init__(self, data: dict or None, threshold: float):
        """
        Initializes a new brain.
        """

        self.data = data
        self.threshold = threshold

    def forward(self, data: str) -> str:
        """
        Gives a string for the Artificial intelligence (AI) to process.
        """

        calc = difflib.get_close_matches(data, self.data.keys(), 1, self.threshold)

        if len(calc) == 0:
            return ""
        else:
            pre_result = calc.pop(0)
            result = ""
            for i in pre_result:
                result += i
            return result
