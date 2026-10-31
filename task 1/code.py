 University Scholarship Allocation System

students = []
n = int(input("Enter number of students: "))

# Collect student information
for i in range(n):

    print("\nEnter details of Student", i + 1)

    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")

    aggregate = float(input("Enter Aggregate Marks: "))

    subject1 = float(input("Enter Subject 1 Marks: "))
    subject2 = float(input("Enter Subject 2 Marks: "))
    subject3 = float(input("Enter Subject 3 Marks: "))

    attendance = float(input("Enter Attendance Percentage: "))
    income = float(input("Enter Annual Family Income: "))

    # Check eligibility
    if (aggregate >= 75 and
        subject1 >= 60 and
        subject2 >= 60 and
        subject3 >= 60 and
        attendance >= 85 and
        income <= 250000):

        students.append({
            "id": sid,
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "subject_total": subject1 + subject2 + subject3,
            "income": income
        })

        print("Eligible for Scholarship")

    else:
        print("Not Eligible for Scholarship")


# Sort eligible students using tie-breaking rules
students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        -s["subject_total"],
        s["income"],
        s["id"]
    )
)

# Scholarship allocation
seats = int(input("\nEnter Available Scholarship Seats: "))

print("\n========== SCHOLARSHIP RESULTS ==========")

if len(students) == 0:
    print("No eligible students found.")

else:
    print("Rank  ID  Name       Marks  Attendance  Income  Status")

    for rank, s in enumerate(students, start=1):

        if rank <= seats:
            status = "Selected"
        else:
            status = "Waiting List"

        print(
            rank,
            s["id"],
            s["name"],
            s["aggregate"],
            s["attendance"],
            s["income"],
            status
        )

print("\nTotal Eligible Students:", len(students))
print("Scholarship Seats:", seats)

print("\nProgram Completed!")

