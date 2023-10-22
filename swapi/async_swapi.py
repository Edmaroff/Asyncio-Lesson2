import asyncio


async def get_person(person_id, session):
    response = await session.get(f"https://swapi.dev/api/people/{person_id}/")
    json = await response.json()
    try:
        selected_keys = [
            "birth_year",
            "eye_color",
            "films",
            "gender",
            "hair_color",
            "height",
            "homeworld",
            "mass",
            "name",
            "skin_color",
            "species",
            "starships",
            "vehicles",
        ]

        selected_data = {key: json[key] for key in selected_keys}
        selected_data["people_id"] = person_id

        keys_to_update = ["homeworld", "films", "species", "starships", "vehicles"]
        for characteristic in keys_to_update:
            selected_data[characteristic] = await get_characteristic_person(
                session,
                selected_data[characteristic],
                key="title" if characteristic == "films" else "name",
            )
            if characteristic == "homeworld":
                selected_data[characteristic] = selected_data[characteristic][0]

        return selected_data
    except KeyError:
        # print(f"{person_id= } не найден")
        return None


async def get_characteristic_titles(session, url, key):
    response = await session.get(url)
    json = await response.json()
    return json[key]


async def get_characteristic_person(session, url_list, key):
    if isinstance(url_list, str):
        url_list = [url_list]
    coroutines = [get_characteristic_titles(session, url, key) for url in url_list]
    person_names_films = await asyncio.gather(*coroutines)
    return person_names_films
