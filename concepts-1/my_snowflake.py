#!/usr/bin/env python
import snowflake.connector


def connect(user, password, account, session_parameters):
    return snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        session_parameters=session_parameters,
    )


def check_connect(user, password, account, session_parameters):
    # Gets the version
    ctx = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        session_parameters=session_parameters,
    )
    cs = ctx.cursor()
    try:
        cs.execute("SELECT current_version()")
        one_row = cs.fetchone()
        print(one_row[0])
    finally:
        cs.close()
    ctx.close()
    return one_row
