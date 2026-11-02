# Hospital Billing and Patient Classification System

# Input patient details
name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

print("\nPatient Types:")
print("1. Regular")
print("2. Insurance")

patient_type = input("Enter patient type (Regular/Insurance): ").strip().lower()

# Input hospital charges
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate billing constraints
if age < 0:
    print("Error: Age cannot be negative.")

elif consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Error: Charges cannot be negative.")

elif patient_type not in ["regular", "insurance"]:
    print("Error: Invalid patient type.")

else:
    # Calculate gross bill
    total_bill = consultation + diagnostic + treatment

    # Determine concession percentage
    concession_rate = 0

    if age >= 60:
        concession_rate = 10

    if patient_type == "insurance":
        concession_rate = max(concession_rate, 15)

    # Maximum concession constraint
    concession_rate = min(concession_rate, 20)

    # Calculate concession and final bill
    concession_amount = total_bill * concession_rate / 100
    final_bill = total_bill - concession_amount

    # Patient classification
    if final_bill > 10000:
        classification = "Category A - High Payment"
    elif final_bill >= 5000:
        classification = "Category B - Medium Payment"
    else:
        classification = "Category C - Low Payment"

    # Display billing summary
    print("\n------ HOSPITAL BILL ------")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Patient Type:", patient_type.capitalize())

    print("\nConsultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)

    print("Gross Bill: Rs.", total_bill)
    print("Concession Rate:", concession_rate, "%")
    print("Concession Amount: Rs.", concession_amount)
    print("Final Payable Amount: Rs.", final_bill)

    print("\nPatient Classification:", classification)

