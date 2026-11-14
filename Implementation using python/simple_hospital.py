"""A small classroom demonstration. Data lasts only while the program runs.

Run: python simple_hospital.py
Focus: classes, objects, inheritance, and appointment booking.
"""


# 1. A parent class holds details shared by patients and doctors.
class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# 2. Patient inherits name and phone from Person.
class Patient(Person):
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.medical_notes = []


# 3. Doctor also inherits from Person and adds a specialization.
class Doctor(Person):
    def __init__(self, name, phone, specialization):
        super().__init__(name, phone)
        self.specialization = specialization


# 4. An appointment connects one patient to one doctor.
class Appointment:
    def __init__(self, patient, doctor, time):
        self.patient = patient
        self.doctor = doctor
        self.time = time
        self.status = "Booked"

    def show_details(self):
        print(f"{self.patient.name} -> {self.doctor.name}")
        print(f"Time: {self.time} | Status: {self.status}")

    def complete(self, notes):
        if self.status != "Booked":
            print("This appointment is already completed.")
            return
        self.patient.medical_notes.append(notes)
        self.status = "Completed"
        print("Consultation saved in the patient's medical notes.")


# 5. This function checks whether the doctor is already booked.
def book_appointment(patient, doctor, time, appointments):
    for appointment in appointments:
        if (appointment.doctor == doctor and appointment.time == time
                and appointment.status == "Booked"):
            print("Sorry, this doctor is already booked at that time.")
            return None

    appointment = Appointment(patient, doctor, time)
    appointments.append(appointment)
    print("Appointment booked successfully!")
    return appointment


# A repeatable demonstration that needs no typing of patient details.
def run_demo():
    print("\n--- CLASS DEMONSTRATION ---")
    patient = Patient("Amina", "0700000001")
    doctor = Doctor("Dr. Kamau", "0700000002", "General Medicine")
    appointments = []

    print("\n1. Create a patient and a doctor.")
    print(f"Patient: {patient.name}")
    print(f"Doctor: {doctor.name}, {doctor.specialization}")

    print("\n2. Book an appointment.")
    appointment = book_appointment(patient, doctor, "09:00", appointments)
    appointment.show_details()

    print("\n3. Try booking the same doctor at the same time.")
    book_appointment(patient, doctor, "09:00", appointments)

    print("\n4. Complete the consultation.")
    appointment.complete("Routine consultation completed.")
    appointment.show_details()
    print("Medical notes:", patient.medical_notes)


def main():
    patients = []
    appointments = []
    doctor = Doctor("Dr. Kamau", "0700000002", "General Medicine")

    while True:
        print("\nHOSPITAL MANAGEMENT SYSTEM")
        print("1. Run the class demonstration")
        print("2. Register a patient")
        print("3. Book an appointment")
        print("4. View appointments")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_demo()
        elif choice == "2":
            name = input("Patient name: ").strip()
            phone = input("Phone number: ").strip()
            if not name or not phone:
                print("Please enter both a name and a phone number.")
                continue
            patients.append(Patient(name, phone))
            print("Patient registered!")
        elif choice == "3":
            if not patients:
                print("Please register a patient first using option 2.")
                continue
            for number, patient in enumerate(patients, start=1):
                print(f"{number}. {patient.name}")
            try:
                number = int(input("Choose a patient number: "))
                if number < 1 or number > len(patients):
                    raise ValueError
            except ValueError:
                print("Please enter a patient number from the list.")
                continue
            time = input("Time today (HH:MM, for example 09:00): ").strip()
            # A fixed format makes matching booked times easy to understand.
            if (len(time) != 5 or time[2] != ":"
                    or not time[:2].isdigit() or not time[3:].isdigit()
                    or int(time[:2]) > 23 or int(time[3:]) > 59):
                print("Please use a valid time such as 09:00 or 14:30.")
                continue
            book_appointment(patients[number - 1], doctor, time, appointments)
        elif choice == "4":
            if not appointments:
                print("No appointments yet.")
            for appointment in appointments:
                appointment.show_details()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Please choose 0, 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
