from database.models import People


async def paste_to_db(session_maker, data):
    async with session_maker() as session:
        async with session.begin():
            for item in data:
                if item is not None:
                    person = People()
                    for key, value in item.items():
                        setattr(person, key, value)
                    session.add(person)
