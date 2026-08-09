from dataclasses import dataclass, field
from datetime import datetime
import uuid

from app.exceptions.student import InvalidStudentError


@dataclass
class Student:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    email: str = ""
    age: int = 0
    department: str = ""
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if not self.name.strip():
            raise InvalidStudentError("Student name cannot be empty")

        if self.age < 0:
            raise InvalidStudentError(
                "Student age cannot be negative"
            )

        if "@" not in self.email:
            raise InvalidStudentError(
                "Student email is invalid"
            )

    def __str__(self):
        return f"{self.name} - {self.email}"

    def __repr__(self):
        return (
            f"Student("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r}, "
            f"age={self.age!r}, "
            f"department={self.department!r}"
            f")"
        )
