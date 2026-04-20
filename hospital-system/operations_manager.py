from specialization import *

class OperationsManager:
    def __init__(self):
        self.specs = []

    def getSpec(self, spec_name):
        for spec in self.specs:
            if spec.name == "Specialization " + spec_name:
                return spec
        print("No specialization named", spec_name)
        return None

    def printMenu(self):
        print("\nProgram Options")
        messages = [
            "1. Add new specialization",
            "2. Add new patient",
            "3. Print all patients",
            "4. Get next patient",
            "5. Remove a leaving patient",
            "6. End the program"
            ]
        print("\n".join(messages))
        command = input(f"Enter your choice from 1 to {len(messages)}: ")
        return command

    def run(self):
        while True:
            cmnd = self.printMenu()
            if cmnd == '1':
                new_spec_name = input("Enter new specialization name: ").capitalize()
                for spec in self.specs:
                    if spec.name == "Specialization " + new_spec_name:
                        print(spec.name, "is already present. Slots available:", spec.getEmptySlot())
                        break
                else:
                    new_spec = Specialization(new_spec_name)
                    self.specs.append(new_spec)
                    print(new_spec.name, "added")

            elif cmnd == '2':
                spec_name = input("Enter specialization name: ").capitalize()
                spec = self.getSpec(spec_name)
                if spec == None: continue
                patient_name = input("Enter patient name: ").capitalize()
                patient_status = int(input("Enter status (0 normal | 1 urgent | 2 super-urgent): "))
                spec.addPatient(patient_name, patient_status)

            elif cmnd == '3':
                for spec in self.specs:
                    print(spec)
                    spec.printPatients()

            elif cmnd == '4':
                spec_name = input("Enter specialization name: ").capitalize()
                spec = self.getSpec(spec_name)
                if spec == None: continue
                spec.retrievePatient()

            elif cmnd == '5':
                spec_name = input("Enter specialization name: ").capitalize()
                spec = self.getSpec(spec_name)
                if spec == None: continue
                patient_name = input("Enter patient name: ")
                spec.removePatient(patient_name)
                

            elif cmnd == '6':
                print("Hospital closed for today!")
                break