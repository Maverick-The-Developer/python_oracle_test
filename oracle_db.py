import oracledb

def get_connection():
    db_user = "system"
    db_password = "oracle"
    db_host = "localhost"
    db_port = "1521"
    db_service_name = "oradb19c"

    #oracledb.init_oracle_client(lib_dir="./lib/instantclient_23_3_mac")
    connection = oracledb.connect(
        user=db_user,
        password=db_password,
        dsn=f"{db_host}:{db_port}/{db_service_name}"
    )

    return connection

def get_cursor(connection):
    return connection.cursor()

def execute_query(cursor, sql):
    cursor.execute(sql)
    if cursor.description:
        return cursor.fetchall()
    return ["done"]

def close_connection(connection):
    connection.close()

def execute_sql(sql):
    connection = get_connection()
    cursor = get_cursor(connection)
    result = execute_query(cursor, sql)
    close_connection(connection)
    return result