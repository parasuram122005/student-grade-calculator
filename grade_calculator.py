
def get_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C+"
    elif score >= 60: return "C"
    elif score >= 50: return "D"
    else: return "F"

def calculate_gpa(score):
    if score >= 90: return 4.0
    elif score >= 80: return 3.0
    elif score >= 70: return 2.0
    elif score >= 60: return 1.0
    else: return 0.0

def generate_report(student_name, subjects):
    print("\n===== REPORT CARD =====")
    print(f"Student: {student_name}")
    total_gpa = 0
    for subject, score in subjects.items():
        grade = get_letter_grade(score)
        gpa = calculate_gpa(score)
        total_gpa += gpa
        print(f"{subject:<15}: {score} -> {grade}")
    avg_gpa = total_gpa / len(subjects)
    scores = list(subjects.values())
    print(f"\nGPA         : {avg_gpa:.1f} / 4.0")
    print(f"Average     : {sum(scores)/len(scores):.1f}")
    print(f"Highest     : {max(scores)}")
    print(f"Lowest      : {min(scores)}")
    print("=" * 23)

def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ")
    subjects = {}
    while True:
        sub = input("Enter subject name (or 'done' to finish): ")
        if sub.lower() == "done":
            break
        try:
            score = float(input(f"Enter score for {sub}: "))
            subjects[sub] = score
        except ValueError:
            print("Invalid score. Please enter a number.")
    if subjects:
        generate_report(name, subjects)
    else:
        print("No subjects entered.")

if __name__ == "__main__":
    main()
