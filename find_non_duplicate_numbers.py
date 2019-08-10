def single_number(numbers):
    d = {}
    for n in numbers:
        if d.get(n) is None:
            d[n] = 1
        else:
            d[n] += 1
    for k, v in d.items():
        if v == 1:
            return k
    raise 'no single counts found :('


assert single_number([4, 3, 2, 4, 1, 3, 2]) == 1
