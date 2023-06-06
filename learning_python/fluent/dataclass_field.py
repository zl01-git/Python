from dataclasses import dataclass, field


@dataclass
class ClubManager:
    name: str
    users: list[str] = field(default_factory=list)


someclub = ClubManager('357', ['john', 'wick'])
againsomeclub = ClubManager('654',)

print(someclub, againsomeclub, sep='\n')