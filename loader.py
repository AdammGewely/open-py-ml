"""
A Quick way of loading a new brain.
Note that this is used for json files.
"""

import brain
import json


def load(filename: str, threshold: float) -> brain.Brain:
    """
    Loads a new brain from a filename and threshold.
    1st parameter filename: The filename
    2nd parameter threshold: The threshold to set the Brain to
    """

    result: brain.Brain

    with open(filename, "r") as file:
        result = brain.Brain(json.loads(file.read()), threshold)

    if not file.closed:
        file.close()

    return result


def save(ai: brain.Brain, filename: str):
    """
    Saves a brain to a filename.
    1st argument AI: The Brain to save
    2nd argument filename: The filename to save to
    """

    with open(filename, "w") as file:
        file.write(json.dumps(ai.data))

    if not file.closed:
        file.close()
