from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime as dt
from oracle_db import execute_sql
from oracle_db_async import execute_sql_async

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World"}

class SQLRequest(BaseModel):
    sql: str

@app.post("/do_sql")
def do_sql(seq: str, post_body: SQLRequest):
    started = dt.now()
    print(f"SEQ No. {seq}, Started at {started}")
    result = execute_sql(post_body.sql)
    finished = dt.now()
    elapsed = finished - started
    print(f"SEQ No. {seq}, Finished at {finished}, Elapsed {elapsed}")
    return {"log": f"SEQ:{seq}, Started at {started}, Finished at {finished}, Elapsed {elapsed}", "data": result}

@app.post("/do_sql_async")
async def do_sql_async(seq: str, post_body: SQLRequest):
    started = dt.now()
    print(f"SEQ No. {seq}, Started at {started}")
    result = await execute_sql_async(post_body.sql)
    finished = dt.now()
    elapsed = finished - started
    print(f"SEQ No. {seq}, Finished at {finished}, Elapsed {elapsed}")
    return {"log": f"SEQ:{seq}, Started at {started}, Finished at {finished}, Elapsed {elapsed}", "data": result}