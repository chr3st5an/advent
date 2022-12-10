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

from typing import List
from functools import reduce


def load_data() -> List[str]:
    with open("data/input-day-3.txt") as f:
        return f.read().splitlines()


def char_to_num(char: str) -> int:
    return ord(char) - (38 if char.isupper() else 96)


def sum_of_priorities() -> int:
    sum_ = 0

    for rucksack in load_data():
        a, b = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
        sum_ += char_to_num([*(set(a) & set(b))][0])

    return sum_


def three_elf_group() -> int:
    sum_ = 0
    data = load_data()

    for i in range(3, len(data) + 1, 3):
        common = reduce(lambda x, y: set(x) & set(y), data[i - 3:i])
        sum_ += char_to_num(list(common)[0])

    return sum_


if __name__ == "__main__":
    print(sum_of_priorities())  # Answer 1
    print(three_elf_group())  # Answer 2
