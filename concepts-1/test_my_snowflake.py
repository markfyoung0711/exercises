import json

from my_snowflake import check_connect, connect


def test_my_snowflake():
    # test connectivity
    config = json.loads(open("/Users/markyoung/snowflake-configure.json").read())
    result = check_connect(
        account=config["account"],
        user=config["user"],
        password=config["password"],
        session_parameters=config["session_parameters"],
    )
    assert result[0] == "8.23.5"
    breakpoint()

    # test some SQL
    with connect(
        account=config["account"],
        user=config["user"],
        password=config["password"],
        session_parameters=config["session_parameters"],
    ) as ctx:
        breakpoint()
        print(ctx)
