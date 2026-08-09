import json
from dataclasses import asdict
from pathlib import Path


class StudentRepository:

    def __init__(self):
        self.file_path = Path(__file__).resolve().parent.parent / "storage" / "students.json"

    def _read_data(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _write_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def _serialize_student(self, student):
        data = asdict(student)

        data["id"] = str(student.id)
        data["created_at"] = student.created_at.isoformat()

        return data

    def create(self, student):
        students = self._read_data()

        students.append(self._serialize_student(student))

        self._write_data(students)

        return student
