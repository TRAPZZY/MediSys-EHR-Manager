def draw_bold_ehr():
    bold_ehr = [
        "███████╗██╗  ██╗ ██████╗ ██████╗ ██╗ █████╗ ██╗",
        "██╔════╝██║  ██║██╔═══██╗██╔══██╗██║██╔══██╗██║",
        "███████╗███████║██║   ██║██████╔╝██║███████║██║",
        "╚════██║██╔══██║██║   ██║██╔══██╗██║██╔══██║██║",
        "███████║██║  ██║╚██████╔╝██████╔╝██║██║  ██║██║",
        "╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝",
    ]

    for line in bold_ehr:
        print(line)

# Draw the bold "EHR" art
draw_bold_ehr()

print('   ')
print('CREATED BY TRAPZZY')


import json

# Create a dictionary to simulate patient records
ehr_database = {}

# Function to add a new patient record
def add_patient_record(patient_id, name, dob, diagnosis):
    if patient_id not in ehr_database:
        ehr_database[patient_id] = {
            "Name": name,
            "Date of Birth": dob,
            "Diagnosis": diagnosis,
        }
        print(f"Patient record for {name} added successfully.")
    else:
        print("Patient ID already exists. Use update_patient_record to modify.")

# Function to update an existing patient record
def update_patient_record(patient_id, **kwargs):
    if patient_id in ehr_database:
        patient_record = ehr_database[patient_id]
        for key, value in kwargs.items():
            patient_record[key] = value
        print(f"Patient record for {patient_record['Name']} updated successfully.")
    else:
        print("Patient ID not found. Use add_patient_record to create a new record.")

# Function to retrieve a patient's record
def get_patient_record(patient_id):
    if patient_id in ehr_database:
        return ehr_database[patient_id]
    else:
        print("Patient ID not found.")
        return None

# Function to delete a patient's record
def delete_patient_record(patient_id):
    if patient_id in ehr_database:
        deleted_patient = ehr_database.pop(patient_id)
        print(f"Patient record for {deleted_patient['Name']} deleted successfully.")
    else:
        print("Patient ID not found.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nElectronic Health Records (EHR) Management")
        print("1. Add Patient Record")
        print("2. Update Patient Record")
        print("3. Retrieve Patient Record")
        print("4. Delete Patient Record")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")
            diagnosis = input("Enter Diagnosis: ")
            add_patient_record(patient_id, name, dob, diagnosis)
        elif choice == "2":
            patient_id = input("Enter Patient ID to update: ")
            field = input("Enter field to update (Name, Date of Birth, Diagnosis): ")
            new_value = input(f"Enter new {field}: ")
            update_patient_record(patient_id, **{field: new_value})
        elif choice == "3":
            patient_id = input("Enter Patient ID to retrieve: ")
            patient_record = get_patient_record(patient_id)
            if patient_record:
                print(json.dumps(patient_record, indent=2))
        elif choice == "4":
            patient_id = input("Enter Patient ID to delete: ")
            delete_patient_record(patient_id)
        elif choice == "5":
            print("Exiting EHR Management System.")
            break
        else:
            print("Invalid choice. Please select a valid option.")