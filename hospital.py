class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def to_dict(self):
        return {"Name": self.name, "Age": self.age, "Disease": self.disease}


def add_patient(patients, name, age, disease):
    patient = Patient(name, age, disease)
    patients.append(patient.to_dict())


def search_patients_by_disease(patients, disease):
    return [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
patients = []
add_patient(patients, "Alice", 30, "Flu")
add_patient(patients, "Bob", 45, "Diabetes")
add_patient(patients, "Charlie", 35, "Flu")

# Searching for patients by disease
search_disease = "Flu"
result = search_patients_by_disease(patients, search_disease)

# Display the output
print(f"Patients with {search_disease}: {result}")
