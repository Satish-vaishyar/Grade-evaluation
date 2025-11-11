import sys

def evaluate_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
    
if len(sys.argv) != 6:
    script_name = sys.argv[0]
    marks1 = int(sys.argv[1])
    marks2 = int(sys.argv[2])
    marks3 = int(sys.argv[3])
    marks4 = int(sys.argv[4])
    marks5 = int(sys.argv[5])

    total_marks = marks1 + marks2 + marks3 + marks4 + marks5
    average_marks = total_marks / 5
    grade = evaluate_grade(average_marks)

    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")
    print(f"Grade: {grade}")