1. Problem Statement
The University Scholarship Allocation System is designed to identify eligible students and allocate scholarships based on their academic performance and financial background.

The system evaluates each applicant using the following criteria:
1. Aggregate Marks: The student must score at least 75% overall.
2. Subject-wise Minimum Marks: The student must score at least 50 marks in every subject.
3. Attendance: The student must have at least 75% attendance.
4. Family Annual Income: The student's family annual income must not exceed ₹2,50,000.
The system ranks all eligible students based on their aggregate marks. If two or more students have equal aggregate marks, the following tie-breaking rules are applied:
- First preference: Higher attendance percentage.
- Second preference: Lower family annual income.
- Third preference: Higher subject-wise minimum score.
Finally, the system displays the list of eligible students in rank order and identifies students who are not eligible.
2. Algorithm
Step 1: Start the program.

Step 2: Get the number of student applicants.

Step 3: Read the following details for each student:
- Student name and roll number.
- Subject marks.
- Attendance percentage.
- Family annual income.
Step 4: Calculate the aggregate percentage of each student.

Step 5: Check eligibility conditions:
- Aggregate marks ≥ 75%.
- Every subject mark ≥ 50.
- Attendance ≥ 75%.
- Annual family income ≤ ₹2,50,000.
Step 6: If all conditions are satisfied, add the student to the eligible list. Otherwise, mark the student as not eligible.

Step 7: Sort eligible students using:
1. Higher aggregate percentage.
2. Higher attendance.
3. Lower annual income.
4. Higher minimum subject mark.
Step 8: Assign ranks to eligible students.

Step 9: Display eligible students with their ranks.

Step 10: Display rejected students and their reasons.

Step 11: Stop the program.
3. Flowchart







studocu.com


Flowchart explanation:
- Start the program.
- Enter student details.
- Calculate aggregate marks.
- Check all scholarship eligibility conditions.
- If eligible, add the student to the eligible list.
- If not eligible, display rejection reasons.
- Rank eligible students according to predefined rules.
- Display the final scholarship allocation list.
- End the program.


5. Sample Input
Enter number of students: 4

Enter details of Student 1
Enter Roll Number: 101
Enter Student Name: Arun
Enter marks in 5 subjects: 85 90 80 88 87
Enter Attendance (%): 90
Enter Annual Family Income: 180000

Enter details of Student 2
Enter Roll Number: 102
Enter Student Name: Banu
Enter marks in 5 subjects: 80 85 90 85 85
Enter Attendance (%): 95
Enter Annual Family Income: 150000

Enter details of Student 3
Enter Roll Number: 103
Enter Student Name: Charan
Enter marks in 5 subjects: 70 65 80 75 70
Enter Attendance (%): 85
Enter Annual Family Income: 200000

Enter details of Student 4
Enter Roll Number: 104
Enter Student Name: Divya
Enter marks in 5 subjects: 90 88 92 85 95
Enter Attendance (%): 80
Enter Annual Family Income: 300000


6. Sample Output
========== SCHOLARSHIP ALLOCATION ==========

Rank  Roll No  Name   Aggregate  Attendance  Income

1     101      Arun   86.00%     90.00%      Rs.180000.00
2     102      Banu   85.00%     95.00%      Rs.150000.00

========== NOT ELIGIBLE STUDENTS ==========

Name: Charan
Reason: Aggregate below 75%

Name: Divya
Reason: Income exceeds Rs. 2,50,000

Program completed.


Mermaid Live Editor: Open Mermaid Editor

8. Expected Result
The University Scholarship Allocation System successfully evaluates students based on academic marks, subject-wise performance, attendance, and family income.

It identifies eligible and ineligible students, ranks eligible applicants according to predefined tie-breaking rules, and displays the final scholarship allocation list.

Conclusion: This Python program makes the scholarship selection process simple, systematic, transparent, and fair by applying the same eligibility conditions and ranking rules to every applicant.
