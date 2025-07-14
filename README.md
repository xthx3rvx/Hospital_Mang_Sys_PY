# Hospital_Mang_Sys_PY
🏥 Hospital Management System (Python OOP)

This project is a simple Hospital Management System implemented using Python's Object-Oriented Programming (OOP) concepts. It demonstrates the core OOP principles such as Inheritance, Polymorphism, Encapsulation, and Abstraction through real-world entities like Patient, Doctor, Surgeon, Staff, Appointment, and Billing.

🚀 Features
Class Hierarchies for Person, Patient, Doctor, Surgeon, and Staff

Encapsulation using private attributes and getters/setters (Appointment class)

Polymorphism via method overloading and method overriding (Billing, displayInfo())

Abstraction using Python's ABC module (Department, Cardiology)

Clean and modular code structure for easy understanding and future enhancements

🧱 Class Breakdown

Person: Base class with common attributes like name and age.

Patient: Inherits Person and adds disease info.

Doctor: Inherits Person and adds specialization.

Surgeon: Inherits Doctor and adds on-call status.

Staff: Inherits Person and adds role.

Appointment: Demonstrates encapsulation using private attributes and setter/getter methods.

Billing: Polymorphic method to calculate bills based on arguments.

Department (Abstract Base Class): Forces child classes to implement departmentInfo().

Cardiology: Inherits from Department and provides specific department info.

📘 Concepts Demonstrated
✅ Inheritance

✅ Method Overriding

✅ Method Overloading (simulated via optional arguments)

✅ Encapsulation

✅ Abstraction

✅ Polymorphism
