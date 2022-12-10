"""
MIT License

Copyright (c) 2022 chr3st5an

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Dict, List, Tuple
import re


# Points per shape
SHAPES: Dict[str, int] = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

RULES: Dict[str, Tuple[str, str, str]] = {
    #         Draws
    #    Loses  |   Wins
    #      |    |    |
    "A": ("Z", "X", "Y"),
    "B": ("X", "Y", "Z"),
    "C": ("Y", "Z", "X"),
}


def load_data() -> List[Tuple[str, str]]:
    """Load the sample data

    Returns
    -------
    List[Tuple[str, str]]
        A list of tuples in each of which the
        first element is the shape of the opponent
        and the second element is the shape of us
    """

    with open("data/input-day-2.txt") as f:
        return re.findall(r"(\w)\s(\w)", f.read())


# Task 1
def calculate_score() -> int:
    return sum(3 * RULES[a].index(b) + SHAPES[b] for a, b in load_data())


# Task 2
def calculate_score_2() -> int:
    return sum(
        3 * (idx := [*SHAPES].index(b)) + SHAPES[RULES[a][idx]]
        for a, b in load_data()
    )


if __name__ == "__main__":
    print(calculate_score())
    print(calculate_score_2())
