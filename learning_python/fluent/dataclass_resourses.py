from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional
from datetime import date


class ResourceType(Enum):
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """Описание мультемедийного устройства"""
    identifer: str
    title: str = '<untitled>'
    creators: list[str] = field(default_factory=list)
    date_: Optional[date] = None
    type: ResourceType = ResourceType.BOOK
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)


description = 'Improving the design of existing code'
book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition', ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19), ResourceType.BOOK, description, 'EN', ['computer programming', 'OOP'])
book1 = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition', ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19), ResourceType.BOOK, description, 'EN', ['computer programming', 'OOP'])

print(book, book1, sep='\n')