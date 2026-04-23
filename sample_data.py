
# Sample data to test the grade calculator
sample_students = [
    {
        "name": "Alice Johnson",
        "subjects": {
            "Mathematics": 92,
            "Physics": 88,
            "Chemistry": 76,
            "English": 95,
            "Computer Science": 98
        }
    },
    {
        "name": "Bob Smith",
        "subjects": {
            "Mathematics": 74,
            "Physics": 68,
            "Chemistry": 82,
            "English": 79,
            "Computer Science": 85
        }
    }
]

if __name__ == "__main__":
    from grade_calculator import generate_report
    for student in sample_students:
        generate_report(student["name"], student["subjects"])
