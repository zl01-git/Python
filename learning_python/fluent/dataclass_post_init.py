from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
    atlete: bool = field(default=False, repr=False)


@dataclass
class HackerClubMember(ClubMember):
    all_handles = set()
    handle: str = field(default='', repr=False)


    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handles:
            msg = f'handle {self.handle} allready exist'
            raise ValueError(msg)
        cls.all_handles.add(self.handle)


leo = HackerClubMember('leo dicaprio', ['actor'])
rick = HackerClubMember('rick')
morty = HackerClubMember('morty')
# rick_jn = HackerClubMember('rick junior')
print(HackerClubMember.all_handles)