import sys
import asyncio
import aiohttp
from datetime import datetime as dt


async def fetch(session, url):
    sql = '''
    BEGIN
        DBMS_LOCK.SLEEP(2);  -- 2초 대기
        DBMS_OUTPUT.PUT_LINE('Hello from PL/SQL!');
    END;
'''
    # sql = "SELECT * FROM dual"

    async with session.post(
        url=url,
        json={"sql":sql},
    ) as response:
        return await response.text()


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return responses


async def main():
    arg_count = len(sys.argv)
    if (arg_count < 3):
        print("Usage: python test_post_requests.py <async or sync> <count>")
        return

    method = sys.argv[1]
    count =  int(sys.argv[2])
    end_point = "do_sql" if method == "sync" else "do_sql_async"
    urls = [f"http://localhost:8000/{end_point}?seq={seq}" for seq in range(1, count+1)]
    start_time = dt.now()
    retults = await fetch_all(urls)
    end_time = dt.now()
    for i, result in enumerate(retults):
        print(result)
    print(f"Elapsed Time: {end_time - start_time}")


asyncio.run(main())
