students = []
attendance = []

n = int(input("Enter number of students: "))

# Enter student names
for i in range(n):
    name = input("Enter student name: ")
    students.append(name)

present = 0
absent = 0

# Mark attendance
for i in range(n):
    while True:
        status = input(
            f"Is {students[i]} Present or Absent (P/A): "
        ).strip().lower()

        if status == "p":
            attendance.append("Present")
            present += 1
            break

        elif status == "a":
            attendance.append("Absent")
            absent += 1
            break

        else:
            print("Invalid input! Please enter P or A.")

# Display attendance report
print("\n" + "=" * 35)
print("       STUDENT ATTENDANCE REPORT")
print("=" * 35)

for i in range(n):
    print(f"{students[i]:<20} - {attendance[i]}")

print("=" * 35)
print("Total Students  =", n)
print("Total Present   =", present)
print("Total Absent    =", absent)
print("=" * 35)