from decorators import critical_check


@critical_check(vendor=["bloomberg"], descriptors=["id"], message2="now")
def check_null_price(vendor, descriptors, df):
    return df[df["price"].isnull()]
