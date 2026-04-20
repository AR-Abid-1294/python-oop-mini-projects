from patient import *

class Specialization:
    patient_status_numbers = [0, 1, 2]

    def __init__(self, name, max_capacity=10):
        self.name = "Specialization " + name
        self.max_capacity = max_capacity
        self.queue = []

    def isFull(self):
        return len(self.queue) == self.max_capacity

    def addPatient(self, name, status):
        if self.isFull():
            print(f"Apologies, the queue is full for {self.name}.")
            return
        if status not in self.patient_status_numbers:
            print("Invalid status. Status should be 0 (normal), 1 (urgent) or 2 (super-urgent).")
            return
        new_patient = Patient(name, status)
        self.queue.append(new_patient)
        self.queue.sort(key=lambda p:p.status, reverse=True)
        print(f"{new_patient} added to the queue of {self.name}.")

    def retrievePatient(self):
        if len(self.queue) == 0:
            print("The queue is empty.")
            return
        next_patient = self.queue.pop(0)
        print(f"{next_patient.name}, please enter the chamber.")

    def removePatient(self, name):
        for patient in self.queue:
            if patient.name == name:
                self.queue.remove(patient)
                print(patient, f"removed from the queue of {self.name}.")
                return
        else:
            print(f"No patient named {name} found in {self.name}")
            
    def printPatients(self):
        for serial, patient in enumerate(self.queue, start=1):
            print(f"\t{serial}. {patient}")

    def getEmptySlot(self):
        return self.max_capacity - len(self.queue)
            
    def __str__(self):
        return f"There are {len(self.queue)} patients in the queue of {self.name}."
        