from typing import NamedTuple


class Coordinates(NamedTuple):
    lat: float
    lon: float


    def __str__(self) -> str:
        ns = 'N' if self.lat > 0 else 'S'
        we = 'E' if self.lon > 0 else 'W'
        return f'{abs(self.lat):.1f}*{ns} {abs(self.lon):.1f}*{we}'
    

moscow = Coordinates(43.13, 14.23)
print(moscow._asdict)
print()