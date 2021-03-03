def arithmetic_arranger(problems, show=False):
    # Rule 1
    if len(problems) > 5:
        return '''Error: Too many problems.'''

    info = []

    for problem in problems:
        tokens = problem.split()

        # Rule 2
        sa, operator, sb = tokens
        sa = sa.strip()
        operator = operator.strip()
        sb = sb.strip()
        if operator != '+' and operator != '-':
            return '''Error: Operator must be '+' or '-'.'''

        for c in (sa + sb):
            if c not in string.digits:
                return '''Error: Numbers must only contain digits.'''

        try:
            a = int(sa)
            b = int(sb)
        except:
            return '''Error: Numbers must only contain digits.'''

        if len(sa) > 4 or len(sb) > 4:
            return '''Error: Numbers cannot be more than four digits.'''

        width = max(len(sa), len(sb)) + 2
        result = a + b if operator == '+' else a - b
        info.append((sa, operator, sb, width, str(result)))

    res = [[], [], [], []]

    for i in info:
        w = i[3]
        res0 = i[0].rjust(w)
        res[0].append(res0)

        res1 = i[1] + i[2].rjust(w - 1)
        res[1].append(res1)

        res2 = '-' * w
        res[2].append(res2)

        res3 = i[4].rjust(w)
        res[3].append(res3)

    if not show:
        del res[3]

    arranged_problems = '\n'.join(['    '.join(l) for l in res])
    return arranged_problems