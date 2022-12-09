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

from typing import Callable, List, Tuple
import re


#                                  |======= PAIR =======|
#  Assigned sections of the ...
#         ... second Elf                      from - to
#         ... first Elf             from - to   |    |
#                                     |    |    |    |
def load_sample_data() -> List[Tuple[int, int, int, int]]:
    with open("data/input-day-4.txt") as f:
        data = re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", f.read())

    return [tuple(map(int, pair)) for pair in data]


def count_overlapping(where: Callable[..., bool], /) -> int:
    return sum(where(*pair) for pair in load_sample_data())


def pairs_overlap(a: int, b: int, c: int, d: int) -> bool:
    x, y = set(range(a, b + 1)), set(range(c, d + 1))

    return x.issubset(y) or x.issuperset(y)


def ranges_overlap(a: int, b: int, c: int, d: int) -> bool:
    return bool(set(range(a, b + 1)) & set(range(c, d + 1)))


if __name__ == "__main__":
    print(count_overlapping(pairs_overlap))  # Answer 1
    print(count_overlapping(ranges_overlap))  # Answer 2
