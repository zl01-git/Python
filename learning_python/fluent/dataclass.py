from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = 'N' if self.lat > 0 else 'S'
        we = 'E' if self.lon > 0 else 'W'
        return f'{abs(self.lat):.3f}^{ns} {abs(self.lon):.4f}^{we}'
    
location = Coordinates(43.1, 54.23131231)

print(location.__dataclass_fields__)

