def create_actor(**kwargs) -> dict:
    actor = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }

    for key, value in kwargs.items():
        actor[key] = value
    
    return actor


assert create_actor(height=190, movies=['Дедпул', 'Главный герой']) == {
    'name': 'Райан',
    'surname': 'Рейнольдс',
    'age': 46,
    'height': 190,
    'movies': ['Дедпул', 'Главный герой']
}
