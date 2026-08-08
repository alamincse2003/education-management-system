from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Student:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    email: str = ""
    age: int = 0
    department: str = ""
    created_at: datetime = field(default_factory=datetime.now)
