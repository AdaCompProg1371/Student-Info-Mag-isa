# Prompt student data

Student_Name = input("Student Name:")
ID_Number = input("ID Number:")
Course_Section = input("Course and Section:")

# Insert grades per quarter
first_grade = int(input("First Grade:"))
second_grade = int(input("Second Grade:"))
third_grade = int(input("Third Grade:"))
fourth_grade = int(input("Fourth Grade:"))

# Get average grade
AVE = (first_grade + second_grade + third_grade + fourth_grade) / 4
print("final:",  AVE)
