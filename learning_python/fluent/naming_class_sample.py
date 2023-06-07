from typing import NamedTuple


class City(NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]


def match_asian_cities():
    result = []
    for city in cities:
        match city:
            case City('Asia', name=_name, country=c):
                result.append(_name)
    return result

print(match_asian_cities())
