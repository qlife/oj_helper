def add(x, y):
    """
    Add using half-adder logics
    :param x: positive number or zero
    :param y: positive number or zero
    :return: sum of x and y
    """

    xor_result, carry = 0, 1e9

    # carry bit propagate only if x_i and y_i are both set.
    # And all the carry bit will be shift left for one bit.
    #
    # Eventually, every carry bit will be shifted to match a x_k bit where x_k == 0,
    # then the propagation of the particular carry bit stops.
    # Although the exactly number iteration is case by case, decided by the input x and y.
    while carry > 0:
        xor_result = x ^ y
        carry = (x & y) << 1
        x = xor_result
        y = carry

    return xor_result
