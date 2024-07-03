import itertools
import time

from my_timer import Timer, cm_timer, dec_timer


def solve(x, y, z, n):
    """First solver for doing product of 3 lists"""
    list_x = list(range(0, x + 1))
    list_y = list(range(0, y + 1))
    list_z = list(range(0, z + 1))
    result = ([x, y, z] for x in list_x for y in list_y for z in list_z)
    return result


def solve2(x, y, z, n):
    """2nd solver using itertools product - it is faster"""
    # use itertools
    result = (
        list(a)
        for a in itertools.product(range(0, x + 1), range(0, y + 1), range(0, z + 1))
    )
    return result


@dec_timer
def dec_solve(x, y, z, n):
    return solve(x, y, z, n)


@dec_timer
def dec_solve2(x, y, z, n):
    return solve2(x, y, z, n)


if __name__ == "__main__":
    x = int(input("input x: "))
    y = int(input("input y: "))
    z = int(input("input z: "))
    n = int(input("input n: "))
    result_2 = solve2(int(x), int(y), int(z), int(n))
    result_1 = solve(int(x), int(y), int(z), int(n))

    with Timer("timing filtering sum != n"):
        result_21 = (a for a in result_2 if sum(a) != n)

    with cm_timer("context mgr no class"):
        result_21 = (a for a in result_2 if sum(a) != n)

    start = time.time()
    result_21 = (a for a in result_2 if sum(a) != n)
    print(f"trial: {time.time() - start:.06f} seconds")

    # this is what takes a long time for large quantities of x, y, z (e.g. 1000 each will end up taking tons of memory)
    with Timer("list reveal from generator"):
        result_21 = list(result_21)
