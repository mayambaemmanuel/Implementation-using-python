# Your simple class demonstration

## Run it

Open `simple_hospital.py` in VS Code. Choose **Run Python File in Terminal**, or type this in the terminal:

```powershell
python simple_hospital.py
```

Choose **1** to run the prepared demonstration. Choose **0** to exit.
No database setup or extra Python packages are needed.

## What to say (about two minutes)

"My project is a hospital management system. This simplified version demonstrates its main task: booking a patient with a doctor."

"Person is the parent class. It contains a name and a phone number. Patient and Doctor inherit these details, so I do not have to repeat that code. A patient also has medical notes, and a doctor has a specialization."

"Appointment connects a patient to a doctor at a particular time. It starts with the status Booked."

Now choose option **1**.

"Here I create a patient called Amina and a doctor called Dr. Kamau. These are objects: individual examples of the classes."

"The first booking succeeds. When I try the same time again, the program rejects it because the doctor is already booked. A loop checks existing appointments before creating a new one."

"Finally, the doctor completes the consultation. The program stores the notes in the patient object and changes the appointment status to Completed."

"This classroom version keeps data in lists while it runs. The larger project includes database storage, admissions, billing, and payments."

## Concepts you can explain

| Concept | Example in the code | Simple meaning |
| --- | --- | --- |
| Class | `Patient` | A blueprint for patients |
| Object | `Patient("Amina", "0700000001")` | One actual patient |
| Attribute | `self.name` | A detail stored in an object |
| Method | `complete()` | An action an object performs |
| Inheritance | `Patient(Person)` | Reusing the parent's details |
| Association | `Appointment.patient` | Linking two objects |
| List | `appointments` | Keeping multiple objects together |

`self` means the current object. `__init__` runs when an object is created. `super().__init__` calls the parent class's initializer.

## Scope of this version

This is a small demonstration of the central workflow, not the entire 12-class UML model. It uses four classes. Doctor inherits directly from Person to keep the example short; the full presentation includes Staff between them. Medical notes use a list instead of a separate MedicalRecord class. The manual menu uses one doctor and times for a single day. Closing the program clears its data. The prepared demonstration uses fresh sample objects each time and does not change the manual menu's patient list.
