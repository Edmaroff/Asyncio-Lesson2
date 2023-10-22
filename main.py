import asyncio
from datetime import datetime

import aiohttp
from more_itertools import chunked
from tqdm import tqdm

from database.creation import create_tables, drop_tables
from database.engine import async_engine, async_session
from database.queries import paste_to_db
from swapi.async_swapi import get_person

BASE_URL = "https://swapi.dev/api/"
CHUNK_SIZE = 10


async def main():
    # Удаляет таблицы
    await drop_tables(async_engine)
    # Создает таблицы
    await create_tables(async_engine)

    async with aiohttp.ClientSession() as session:
        for people_id_chunk in tqdm(
            chunked(range(1, 100), CHUNK_SIZE), desc="Processing chunks"
        ):
            coroutines = [
                get_person(people_id, session) for people_id in people_id_chunk
            ]
            result = await asyncio.gather(*coroutines)
            asyncio.create_task(paste_to_db(async_session, result))

    tasks_to_await = asyncio.all_tasks() - {asyncio.current_task()}
    await asyncio.gather(*tasks_to_await)


if __name__ == "__main__":
    start = datetime.now()
    asyncio.run(main())
    print(datetime.now() - start)
