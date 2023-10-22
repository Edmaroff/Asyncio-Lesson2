from database.models import Base


async def create_tables(engine):
    """
    Создает таблицы в БД.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables(engine):
    """
    Удаляет таблицы из БД.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
