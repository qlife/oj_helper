import random


def gen_random_list(length, start=0, stop=100_000, step=1):
    """
    Codility sees toe accept less than 500 elements, which means one cannot rely
    on the their online IDE to test against the large dataset.

    To copy to the clipboard, try:

    import pyperclip
    pyperclip.copy(str(list_and_whatever))
    """
    return [random.randrange(start, stop, step) for i in range(0, length)]


def gen_substring(src: str) -> int:
    l = len(src)
    res = 0
    for i in range(l):
        for j in range(i, l):
            print(src[i:j+1])
            res += 1

    return res



