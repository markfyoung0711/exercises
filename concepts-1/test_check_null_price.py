import pandas as pd
from checks import check_null_price


def test_check_null_price():
    row1 = [1, 2, 3, 4, 5]
    row2 = [
        3,
        4,
        5,
        6,
    ]
    columns = ["id", "field2", "field3", "field4", "price"]
    df = pd.DataFrame(data=[row1, row2], columns=columns)
    breakpoint()

    results = check_null_price(vendor=["bloomberg"], descriptors=["id"], df=df)
    assert results == 1
