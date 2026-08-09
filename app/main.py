from app.models.student import Student
from app.repositories.student_repository import StudentRepository


def main():
    repository = StudentRepository()

    student = Student(
        name="Al Amin",
        email="alamin@example.com",
        age=23,
        department="CSE",
    )
    student2 = Student(
        name="Habib",
        email="alamin@example.com",
        age=24,
        department="CSE",
    )

    repository.create(student)
    repository.create(student2)

    print("Student created successfully!")


if __name__ == "__main__":
    main()
