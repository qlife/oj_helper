def main():
    m = [
        [3, 7, 9, 2, 7],
        [9, 8, 3, 5, 5],
        [1, 7, 9, 8, 5],
        [3, 8, 6, 4, 10],
        [6, 3, 9, 7, 8],
    ]

    # Important pattern!
    s = [[0 for _ in range(5)] for _ in range(5)]

    # Create list by two-fold (*) won't give you similar things.
    s2 = [[0] * 5] * 5

    m[4][2] = 42
    s[4][2] = 42
    s2[4][2] = 42

    print(m)
    print(s)
    print(s2)


"""
When creating a list with copied elements

n * [0] 

All the element is actual a object copy of the object 0.
However, 0 is a primitive object and any modified result in a newly created primitive scalar object.

n * [[ ... ]]

Have no similar effects. In such cases, the newly created 2-dim lists simply copy the list references
for n times, therefore, all the elements still referencing to one identical list.

See https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array dreau 's comment
"""

if __name__ == '__main__':
    main()
