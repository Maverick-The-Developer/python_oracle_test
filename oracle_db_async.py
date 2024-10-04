import oracledb

async def execute_sql_async(sql: str):
    db_user = "system"
    db_password = "oracle"
    db_host = "localhost"
    db_port = "1521"
    db_service_name = "oradb19c"

    connection = await oracledb.connect_async(
        user=db_user,
        password=db_password,
        dsn=f"{db_host}:{db_port}/{db_service_name}"
    )
    connection.autocommit = True
    res = await connection.execute(sql)

    return ["done async"] if res is None else res.fetchall()
