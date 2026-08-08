from app.models.student import Student


def main():
    student = Student(
        name="Al Amin",
        email="alamin@example.com",
        age=23,
        department="CSE",
    )

    print(student)


if __name__ == "__main__":
    main()
