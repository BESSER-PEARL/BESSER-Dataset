####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
bo: Enumeration = Enumeration(
    name="bo",
    literals={
            
    }
)

# Classes
patient = Class(name="patient")
int_Interface = Class(name="int_Interface")
doctor = Class(name="doctor")
clinical = Class(name="clinical")
income_manager = Class(name="income_manager")
bank = Class(name="bank")
pharmacy = Class(name="pharmacy")
duties_manager = Class(name="duties_manager")
customer = Class(name="customer")
compuer = Class(name="compuer")
Owner = Class(name="Owner")
kiosk = Class(name="kiosk")
students = Class(name="students")
attendance_manager = Class(name="attendance_manager")
School_administrator = Class(name="School_administrator")
Parents = Class(name="Parents")
teacher = Class(name="teacher")
Passenger = Class(name="Passenger")
booking_clerk = Class(name="booking_clerk")
Groups = Class(name="Groups")
individual = Class(name="individual")
kiosk1 = Class(name="kiosk1")
student = Class(name="student")
Professor = Class(name="Professor")
Register = Class(name="Register")
Billing_system = Class(name="Billing_system")
course = Class(name="course")

# patient class attributes and methods
patient_patient_id: Property = Property(name="patient_id", type=int_Interface)
patient_patient_name: Property = Property(name="patient_name", type=StringType)
patient_disease: Property = Property(name="disease", type=StringType)
patient.attributes={patient_disease, patient_patient_name, patient_patient_id}

# int_Interface class attributes and methods

# doctor class attributes and methods
doctor_doctor_id: Property = Property(name="doctor_id", type=int_Interface)
doctor_doctor_name: Property = Property(name="doctor_name", type=StringType)
doctor_salary: Property = Property(name="salary", type=int_Interface)
doctor_attendance: Property = Property(name="attendance", type=BooleanType)
doctor.attributes={doctor_salary, doctor_doctor_id, doctor_doctor_name, doctor_attendance}

# clinical class attributes and methods
clinical_id: Property = Property(name="id", type=int_Interface)
clinical_name: Property = Property(name="name", type=StringType)
clinical_salary: Property = Property(name="salary", type=int_Interface)
clinical.attributes={clinical_name, clinical_salary, clinical_id}

# income_manager class attributes and methods
income_manager_manager_name: Property = Property(name="manager_name", type=StringType)
income_manager_manager_id: Property = Property(name="manager_id", type=int_Interface)
income_manager_duty_hours: Property = Property(name="duty_hours", type=int_Interface)
income_manager.attributes={income_manager_manager_id, income_manager_manager_name, income_manager_duty_hours}

# bank class attributes and methods
bank_bank_name: Property = Property(name="bank_name", type=StringType)
bank.attributes={bank_bank_name}

# pharmacy class attributes and methods
pharmacy_medicines: Property = Property(name="medicines", type=StringType)
pharmacy_price: Property = Property(name="price", type=int_Interface)
pharmacy.attributes={pharmacy_medicines, pharmacy_price}

# duties_manager class attributes and methods
duties_manager_make_attendence: Property = Property(name="make_attendence", type=BooleanType)
duties_manager.attributes={duties_manager_make_attendence}

# customer class attributes and methods
customer_customer_Id: Property = Property(name="customer_Id", type=int_Interface)
customer_customer_name: Property = Property(name="customer_name", type=StringType)
customer__attr: Property = Property(name="_attr", type=StringType)
customer.attributes={customer__attr, customer_customer_name, customer_customer_Id}

# compuer class attributes and methods

# Owner class attributes and methods
Owner_items: Property = Property(name="items", type=StringType)
Owner_email: Property = Property(name="email", type=StringType)
Owner.attributes={Owner_email, Owner_items}

# kiosk class attributes and methods
kiosk_newsletters: Property = Property(name="newsletters", type=StringType)
kiosk_saving: Property = Property(name="saving", type=int_Interface)
kiosk_discount: Property = Property(name="discount", type=int_Interface)
kiosk.attributes={kiosk_newsletters, kiosk_saving, kiosk_discount}

# students class attributes and methods
students_student_id_: Property = Property(name="student_id_", type=int_Interface)
students_student_name: Property = Property(name="student_name", type=StringType)
students.attributes={students_student_name, students_student_id_}

# attendance_manager class attributes and methods
attendance_manager_identify_students: Property = Property(name="identify_students", type=StringType)
attendance_manager_student_names: Property = Property(name="student_names", type=StringType)
attendance_manager_Excuse_of_Absenties: Property = Property(name="Excuse_of_Absenties", type=StringType)
attendance_manager.attributes={attendance_manager_student_names, attendance_manager_identify_students, attendance_manager_Excuse_of_Absenties}

# School_administrator class attributes and methods

# Parents class attributes and methods

# teacher class attributes and methods

# Passenger class attributes and methods
Passenger_check_in: Property = Property(name="check_in", type=BooleanType)
Passenger_pass: Property = Property(name="pass", type=StringType)
Passenger_baggage: Property = Property(name="baggage", type=int_Interface)
Passenger_id: Property = Property(name="id", type=int_Interface)
Passenger.attributes={Passenger_baggage, Passenger_check_in, Passenger_id, Passenger_pass}

# booking_clerk class attributes and methods

# Groups class attributes and methods
Groups_passenger_amount: Property = Property(name="passenger_amount", type=int_Interface)
Groups_names: Property = Property(name="names", type=StringType)
Groups_id: Property = Property(name="id", type=Passenger)
Groups.attributes={Groups_passenger_amount, Groups_id, Groups_names}

# individual class attributes and methods
individual_pass: Property = Property(name="pass", type=Passenger)
individual.attributes={individual_pass}

# kiosk1 class attributes and methods
kiosk1_check_in: Property = Property(name="check_in", type=Passenger)
kiosk1.attributes={kiosk1_check_in}

# student class attributes and methods
student_student_id: Property = Property(name="student_id", type=int_Interface)
student_student_name: Property = Property(name="student_name", type=StringType)
student_no_of_courses: Property = Property(name="no_of_courses", type=int_Interface)
student.attributes={student_student_id, student_student_name, student_no_of_courses}

# Professor class attributes and methods
Professor_course_name: Property = Property(name="course_name", type=StringType)
Professor_course_id: Property = Property(name="course_id", type=int_Interface)
Professor_professor_name: Property = Property(name="professor_name", type=StringType)
Professor_professor_id: Property = Property(name="professor_id", type=int_Interface)
Professor.attributes={Professor_professor_name, Professor_course_id, Professor_professor_id, Professor_course_name}

# Register class attributes and methods
Register_student_id: Property = Property(name="student_id", type=student)
Register_student_name: Property = Property(name="student_name", type=student)
Register_professer_id: Property = Property(name="professer_id", type=Professor)
Register_professor_name: Property = Property(name="professor_name", type=Professor)
Register_course_id: Property = Property(name="course_id", type=StringType)
Register_course_name: Property = Property(name="course_name", type=StringType)
Register.attributes={Register_student_id, Register_course_id, Register_professer_id, Register_course_name, Register_student_name, Register_professor_name}

# Billing_system class attributes and methods
Billing_system_course_fees: Property = Property(name="course_fees", type=int_Interface)
Billing_system_course_status: Property = Property(name="course_status", type=StringType)
Billing_system.attributes={Billing_system_course_fees, Billing_system_course_status}

# course class attributes and methods
course_course_name: Property = Property(name="course_name", type=StringType)
course_course_id: Property = Property(name="course_id", type=int_Interface)
course_teached_by: Property = Property(name="teached_by", type=StringType)
course_placed_on: Property = Property(name="placed_on", type=StringType)
course.attributes={course_course_name, course_placed_on, course_teached_by, course_course_id}

# Relationships
patient_class_doctor: BinaryAssociation = BinaryAssociation(
    name="patient_class_doctor",
    ends={
        Property(name="doctor0", type=doctor, multiplicity=Multiplicity(1, 9999)),
        Property(name="patient_class1", type=patient, multiplicity=Multiplicity(1, 1))
    }
)
income_manager_bank: BinaryAssociation = BinaryAssociation(
    name="income_manager_bank",
    ends={
        Property(name="bank2", type=bank, multiplicity=Multiplicity(1, 1)),
        Property(name="income_manager3", type=income_manager, multiplicity=Multiplicity(1, 1))
    }
)
patient__pharmacy: BinaryAssociation = BinaryAssociation(
    name="patient__pharmacy",
    ends={
        Property(name="pharmacy4", type=pharmacy, multiplicity=Multiplicity(0, 1)),
        Property(name="patient5", type=patient, multiplicity=Multiplicity(1, 9999))
    }
)
doctor__duties_manager: BinaryAssociation = BinaryAssociation(
    name="doctor__duties_manager",
    ends={
        Property(name="duties_manager6", type=duties_manager, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor7", type=doctor, multiplicity=Multiplicity(1, 9999))
    }
)
clinical__duties_manager: BinaryAssociation = BinaryAssociation(
    name="clinical__duties_manager",
    ends={
        Property(name="duties_manager8", type=duties_manager, multiplicity=Multiplicity(1, 1)),
        Property(name="clinical9", type=clinical, multiplicity=Multiplicity(1, 9999))
    }
)
customer_compuer: BinaryAssociation = BinaryAssociation(
    name="customer_compuer",
    ends={
        Property(name="compuer10", type=compuer, multiplicity=Multiplicity(1, 1)),
        Property(name="customer11", type=customer, multiplicity=Multiplicity(1, 9999))
    }
)
individual__booking_clerk: BinaryAssociation = BinaryAssociation(
    name="individual__booking_clerk",
    ends={
        Property(name="booking_clerk36", type=booking_clerk, multiplicity=Multiplicity(0, 1)),
        Property(name="individual37", type=individual, multiplicity=Multiplicity(0, 1))
    }
)
Groups__booking_clerk: BinaryAssociation = BinaryAssociation(
    name="Groups__booking_clerk",
    ends={
        Property(name="booking_clerk38", type=booking_clerk, multiplicity=Multiplicity(0, 1)),
        Property(name="groups39", type=Groups, multiplicity=Multiplicity(0, 1))
    }
)
kiosk_Passenger: BinaryAssociation = BinaryAssociation(
    name="kiosk_Passenger",
    ends={
        Property(name="passenger40", type=Passenger, multiplicity=Multiplicity(0, 1)),
        Property(name="kiosk41", type=kiosk1, multiplicity=Multiplicity(0, 1))
    }
)
student_course: BinaryAssociation = BinaryAssociation(
    name="student_course",
    ends={
        Property(name="course42", type=course, multiplicity=Multiplicity(1, 9999)),
        Property(name="student43", type=student, multiplicity=Multiplicity(0, 1))
    }
)
student_Professor: BinaryAssociation = BinaryAssociation(
    name="student_Professor",
    ends={
        Property(name="professor44", type=Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="student45", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
student_Register: BinaryAssociation = BinaryAssociation(
    name="student_Register",
    ends={
        Property(name="register46", type=Register, multiplicity=Multiplicity(1, 9999)),
        Property(name="student47", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
Professor_Register: BinaryAssociation = BinaryAssociation(
    name="Professor_Register",
    ends={
        Property(name="register48", type=Register, multiplicity=Multiplicity(1, 9999)),
        Property(name="professor49", type=Professor, multiplicity=Multiplicity(1, 9999))
    }
)
student_Billing_system: BinaryAssociation = BinaryAssociation(
    name="student_Billing_system",
    ends={
        Property(name="billing_system50", type=Billing_system, multiplicity=Multiplicity(0, 1)),
        Property(name="student51", type=student, multiplicity=Multiplicity(1, 9999))
    }
)
compuer_kiosk: BinaryAssociation = BinaryAssociation(
    name="compuer_kiosk",
    ends={
        Property(name="kiosk12", type=kiosk, multiplicity=Multiplicity(1, 1)),
        Property(name="compuer13", type=compuer, multiplicity=Multiplicity(1, 1))
    }
)
customer_kiosk: BinaryAssociation = BinaryAssociation(
    name="customer_kiosk",
    ends={
        Property(name="kiosk14", type=kiosk, multiplicity=Multiplicity(1, 1)),
        Property(name="customer15", type=customer, multiplicity=Multiplicity(1, 9999))
    }
)
Owner_kiosk: BinaryAssociation = BinaryAssociation(
    name="Owner_kiosk",
    ends={
        Property(name="kiosk16", type=kiosk, multiplicity=Multiplicity(1, 1)),
        Property(name="owner17", type=Owner, multiplicity=Multiplicity(1, 1))
    }
)
students_attendance_manager: BinaryAssociation = BinaryAssociation(
    name="students_attendance_manager",
    ends={
        Property(name="attendance_manager18", type=attendance_manager, multiplicity=Multiplicity(1, 1)),
        Property(name="students19", type=students, multiplicity=Multiplicity(1, 9999))
    }
)
attendance_manager_teacher: BinaryAssociation = BinaryAssociation(
    name="attendance_manager_teacher",
    ends={
        Property(name="teacher20", type=teacher, multiplicity=Multiplicity(0, 1)),
        Property(name="attendance_manager21", type=attendance_manager, multiplicity=Multiplicity(0, 1))
    }
)
students_School_administrator: BinaryAssociation = BinaryAssociation(
    name="students_School_administrator",
    ends={
        Property(name="school_administrator22", type=School_administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="students23", type=students, multiplicity=Multiplicity(0, 1))
    }
)
Parents_attendance_manager: BinaryAssociation = BinaryAssociation(
    name="Parents_attendance_manager",
    ends={
        Property(name="attendance_manager24", type=attendance_manager, multiplicity=Multiplicity(0, 1)),
        Property(name="parents25", type=Parents, multiplicity=Multiplicity(0, 1))
    }
)
School_administrator_Parents: BinaryAssociation = BinaryAssociation(
    name="School_administrator_Parents",
    ends={
        Property(name="parents26", type=Parents, multiplicity=Multiplicity(1, 9999)),
        Property(name="school_administrator27", type=School_administrator, multiplicity=Multiplicity(0, 1))
    }
)
School_administrator_attendance_manager: BinaryAssociation = BinaryAssociation(
    name="School_administrator_attendance_manager",
    ends={
        Property(name="attendance_manager28", type=attendance_manager, multiplicity=Multiplicity(0, 1)),
        Property(name="school_administrator29", type=School_administrator, multiplicity=Multiplicity(0, 1))
    }
)
Passenger__booking_clerk: BinaryAssociation = BinaryAssociation(
    name="Passenger__booking_clerk",
    ends={
        Property(name="booking_clerk30", type=booking_clerk, multiplicity=Multiplicity(1, 9999)),
        Property(name="passenger31", type=Passenger, multiplicity=Multiplicity(1, 9999))
    }
)
Passenger_Groups: BinaryAssociation = BinaryAssociation(
    name="Passenger_Groups",
    ends={
        Property(name="groups32", type=Groups, multiplicity=Multiplicity(0, 1)),
        Property(name="passenger33", type=Passenger, multiplicity=Multiplicity(0, 1))
    }
)
individual_Passenger: BinaryAssociation = BinaryAssociation(
    name="individual_Passenger",
    ends={
        Property(name="passenger34", type=Passenger, multiplicity=Multiplicity(0, 1)),
        Property(name="individual35", type=individual, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_d3g8QHozEemKc6sUMthxaw",
    types={patient, int_Interface, doctor, clinical, income_manager, bank, pharmacy, duties_manager, customer, compuer, Owner, kiosk, students, attendance_manager, School_administrator, Parents, teacher, Passenger, booking_clerk, Groups, individual, kiosk1, student, Professor, Register, Billing_system, course, bo},
    associations={patient_class_doctor, income_manager_bank, patient__pharmacy, doctor__duties_manager, clinical__duties_manager, customer_compuer, individual__booking_clerk, Groups__booking_clerk, kiosk_Passenger, student_course, student_Professor, student_Register, Professor_Register, student_Billing_system, compuer_kiosk, customer_kiosk, Owner_kiosk, students_attendance_manager, attendance_manager_teacher, students_School_administrator, Parents_attendance_manager, School_administrator_Parents, School_administrator_attendance_manager, Passenger__booking_clerk, Passenger_Groups, individual_Passenger},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)