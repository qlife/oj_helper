#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import collections


def main():
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    words = re.sub("[!|?|\'|,|;|.|]", ' ', paragraph).lower().split(' ')
    fwords = [w for w in words if w not in banned and len(w) > 0]
    c = collections.Counter(fwords)

    print(words, fwords)
    print(c)
    print(c.most_common(1))


main()