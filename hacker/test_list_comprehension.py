# import concurrent.futures
# import itertools
import logging
import time
from collections import namedtuple
from multiprocessing import Pool

import pandas as pd
import pytest
from list_comprehension import solve2
from my_timer import cm_timer

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("test_list_comprehension")


def square(x):
    return x * x


def sum_filter(iterable):
    if sum(iterable) != 3:
        return iterable
    return None


def old_test_solve():

    Config = namedtuple("Config", ["x", "y", "z", "n"])
    test_inputs = []
    # these are the inputs
    for data in [(1, 1, 2, 3), (10, 10, 10, 4), (100, 100, 100, 5)]:
        test_inputs.append(Config._make(data))

    pool_config = [5]
    numchunks = 10

    for numpools in pool_config:
        print(f"\ntesting for number of pools {numpools}")
        for config in test_inputs:
            print(config)
            stats = {}
            stats["pools"] = numpools
            stats["chunks"] = numchunks
            stats["original_size"] = (config.x + 1) * (config.y + 1) * (config.z + 1)
            # first part of solution
            with cm_timer("solve2"):
                result = solve2(config.x, config.y, config.z, config.n)

            with cm_timer("pooled sum"):
                with Pool(numpools) as executor:
                    return list(executor.map(sum_filter, result, chunksize=numchunks))


def pool_test(input, pools, chunksize, description):
    """operate on input (iterable)"""

    print(f"\nTest Description: {description}, pools {pools} chunksize {chunksize}")
    # test function 1 (solve2)
    with cm_timer("pool_test: input generator"):
        result = solve2(input.x, input.y, input.z, input.n)

    # test function 2 (filter)
    with cm_timer("pool_test: filter and instantiate"):
        with Pool(pools) as executor:
            result = executor.map(sum_filter, result, chunksize=chunksize)
            # result = list(filter(lambda x: x is not None, result))
            return result


@pytest.mark.parametrize("execution_number", range(5))
def test_divide(execution_number):
    config_pools = [1, 2]
    # generate test inputs
    Config = namedtuple("Config", ["x", "y", "z", "n"])
    input_collection = []
    # these are the inputs
    # for data in [(1, 1, 2, 3), (10, 10, 10, 4), (100, 100, 100, 5)]:
    for data in [(1, 1, 2, 3), (10, 10, 10, 4)]:
        input_collection.append(Config._make(data))

    stats_results = []
    for pools in config_pools:
        for col in input_collection:
            stats = {}
            original_size = (col.x + 1) * (col.y + 1) * (col.z + 1)
            stats["original_size"] = original_size
            stats["pools"] = pools
            stats["chunks"] = original_size

            start_time = time.time()
            result = pool_test(
                col,
                pools=pools,
                chunksize=original_size,
                description=f"x={col.x}, y={col.y}, z={col.z}, n={col.n}",
            )
            result = (a for a in result if a is not None)
            stats["elapsed_time"] = time.time() - start_time
            stats["result_size"] = len(list(result))
            stats_results.append(stats)

    df = pd.DataFrame(stats_results)
    df.describe()
    df = df.sort_values(by=["elapsed_time"], ascending=True)
    print(f'elapsed_time average: {df["elapsed_time"].mean()}')
