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

from typing import List, Tuple
import re


def load_instructions() -> List[Tuple[int, int, int]]:
    """Parse the instructions from the data file

    Returns
    -------
    :class:`List[Tuple[int, int, int]]`
        A list of tuples where each tuple represents
        an instruction. An instruction consists of
        three numbers: The first number describes
        how many elements shall be moved. The second
        and third number describe (2) from / (3) to
        which stack the elements should be moved.
    """

    with open("data/input-day-5.txt") as f:
        data = re.findall(r"m.*?(\d+).*?(\d+).*?(\d+)", f.read())

    return [tuple(map(int, line)) for line in data]


def load_stacks() -> List[List[str]]:
    """Parse the stacks from the data file

    Returns
    -------
    :class:`List[List[str]]`
        A nested list where each list represents
        the parsed stack with its elements.
    """

    with open("data/input-day-5.txt") as f:
        data = f.read().split("\n\n")[0].splitlines()

    stacks = [list() for _ in range(int(data.pop()[-1]))]

    for line in data:
        for idx, char in enumerate(line[1::4]):
            if char.isalpha():
                stacks[idx].append(char)

    return stacks


def crate_mover(multiple_at_once: bool = False) -> List[List[str]]:
    """Load and execute the instructions on the stacks

    Parameters
    ----------
    multiple_at_once : :class:`bool`
        If elements should be moved all at once
        to a target stack or sequentially at each
        instruction iteration.

    Returns
    -------
    :class:`List[List[str]]`
        The stacks after all instructions got executed.
    """

    stacks = load_stacks()

    for amount, from_, to in load_instructions():
        for _ in range(amount):
            stacks[to - 1].insert(0, stacks[from_ - 1].pop(0))

        if multiple_at_once:
            stacks[to - 1][:amount] = reversed(stacks[to - 1][:amount])

    return stacks


def print_top_of_stacks(stacks: List[List[str]]) -> None:
    print("".join(stack[0] for stack in stacks))


if __name__ == "__main__":
    print_top_of_stacks(crate_mover())  # Answer 1
    print_top_of_stacks(crate_mover(True))  # Answer 2
