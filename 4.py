import time

num_subjects = int(input("Enter the number of subjects:"))

grades = []

for i in range(num_subjects):
    grade = float(input(f"Enter the grade for {i + 1} "))
    if grade > 20:
        print("Invalid Grade")
        time.sleep(1)  
        exit() 
    grades.append(grade)

average = sum(grades) / num_subjects


if average < 12:
    letter_grade = 'F'
elif average < 15:
    letter_grade = 'C'
elif average < 18:
    letter_grade = 'B'
else:
    letter_grade = 'A'

# نمایش نتیجه
print(f"Final grade: {average:.2f} and letter grade: {letter_grade}")