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



