def calculate_grade(average_marks):
    if average_marks >= 90:
        return "A+"
    elif average_marks >= 80:
        return "A"
    elif average_marks >= 70:
        return "B"
    elif average_marks >= 60:
        return "C"
    elif average_marks >= 50:
        return "D"
    else:
        return "F"

def calculate_marksheet(subjects):
    total_marks = sum(subjects)
    average_marks = total_marks / len(subjects)
    grade = calculate_grade(average_marks)
    return total_marks, average_marks, grade

def main():
    print("Enter marks for 5 subjects:")

    subjects = []
    for i in range(5):
        subject_marks = float(input(f"Enter marks for subject {i + 1}: "))
        subjects.append(subject_marks)

    total_marks, average_marks, grade = calculate_marksheet(subjects)

    
    print("\nMarksheet:")
    print("-----------")
    print("Subject-wise marks:", subjects)
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()