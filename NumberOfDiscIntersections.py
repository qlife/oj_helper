import itertools
import operator


def solution(a):
    p = sorted(list(enumerate(a)), key=operator.itemgetter(1), reverse=True)
    return p


def main():
    a0 = [1, 5, 2, 1, 4, 0]
    print(solution(a0))


if __name__ == '__main__':
    main()