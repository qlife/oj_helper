def my_pow(x, y):
    # The order of these case is important.
    # Consider pow(0, 0) == ?
    if y == 0:
        return 1
    elif x == 0 or x == 1 or y == 1:
        return x
    elif y < 0:
        return 1.0 / my_pow(x, -y)
    elif x < 0:
        return (0 - my_pow(-x, y)) if 1 == y % 2 else my_pow(-x, y)

    st = []    # (reminder = 1 or 0, pow = y_i)
    while y > 1:
        # Originally I think it is necessary to store the sequences of (y // 2) on the stack,
        # but it turns out not be used.

        # Deprecated code
        # pair = y % 2, (y // 2)
        # Deprecated code

        r = y % 2
        st.append(r)
        y = y // 2
    # print(st)

    result = x
    while st:
        r = st.pop()
        result = result * result
        if r > 0:
            result *= x

    return result
