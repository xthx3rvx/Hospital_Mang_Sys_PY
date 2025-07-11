class Person:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def displayInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def displayInfo(self):
        super().displayInfo()
        print(f"Disease: {self.disease}")

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def displayInfo(self):
        super().displayInfo()
        print(f"Specialization: {self.specialization}")

class Surgeon(Doctor):
    def __init__(self, name, age, specialization, onCallStatus):
        super().__init__(name, age, specialization)
        self.onCallStatus = onCallStatus

    def displayInfo(self):
        super().displayInfo()
        print(f"On Call Status: {'Yes' if self.onCallStatus else 'No'}")

class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def displayInfo(self):
        super().displayInfo()
        print(f"Role: {self.role}")

class Appointment:
    def __init__(self, patientName, doctorName, appointmentTime):
        self.__patientName = patientName
        self.__doctorName = doctorName
        self.__appointmentTime = appointmentTime

    def getPatientName(self):
        return self.__patientName

    def setPatientName(self, name):
        self.__patientName = name

    def getDoctorName(self):
        return self.__doctorName

    def setDoctorName(self, name):
        self.__doctorName = name

    def getAppointmentTime(self):
        return self.__appointmentTime

    def setAppointmentTime(self, time):
        self.__appointmentTime = time

class Billing:
    def generateBill(self, amount=None, days=None):
        if amount is not None and days is not None:
            print(f"Total Bill (Room + Services): {amount * days} RS")
        elif amount is not None:
            print(f"Total Bill (Fixed): {amount} Rs")
        else:
            print("No billing information provided.")

from abc import ABC, abstractmethod

class Department(ABC):
    @abstractmethod
    def departmentInfo(self):
        pass

class Cardiology(Department):
    def departmentInfo(self):
        print("This is the Cardiology Department, handles all heart-related cases.")

if __name__ == "__main__":
    # Testing Inheritance & Polymorphism
    p1 = Patient("Alice", 30, "Flu")
    p1.displayInfo()

    d1 = Doctor("Dr. Smith", 45, "Cardiologist")
    d1.displayInfo()

    s1 = Surgeon("Dr. Grey", 40, "Neurosurgeon", True)
    s1.displayInfo()

    st1 = Staff("Mark", 35, "Receptionist")
    st1.displayInfo()

    # Encapsulation
    appt = Appointment("Alice", "Dr. Smith", "10:00 AM")
    print(f"\nAppointment - Patient: {appt.getPatientName()}, Doctor: {appt.getDoctorName()}, Time: {appt.getAppointmentTime()}")

    # Polymorphism
    bill = Billing()
    bill.generateBill(1500)
    bill.generateBill(1500, 3)

    # Abstraction
    cardio = Cardiology()
    cardio.departmentInfo()
