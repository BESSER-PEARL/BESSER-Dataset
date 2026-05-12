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

# Classes
Person = Class(name="Person", is_abstract=True)
employee = Class(name="employee", is_abstract=True)
doctor = Class(name="doctor")
nurse = Class(name="nurse")
It = Class(name="It")
Patient = Class(name="Patient")
Room = Class(name="Room")
appointment = Class(name="appointment")
MainWindow = Class(name="MainWindow")

# Person class attributes and methods
Person_name: Property = Property(name="name", type=StringType)
Person_age: Property = Property(name="age", type=IntegerType)
Person.attributes={Person_name, Person_age}

# employee class attributes and methods
employee_password: Property = Property(name="password", type=StringType)
employee_department: Property = Property(name="department", type=StringType)
employee.attributes={employee_password, employee_department}

# doctor class attributes and methods
doctor_weekappointment: Property = Property(name="weekappointment", type=StringType)
doctor_patient: Property = Property(name="patient", type=StringType)
doctor.attributes={doctor_patient, doctor_weekappointment}

# nurse class attributes and methods
nurse__rom: Property = Property(name="_rom", type=Room)
nurse.attributes={nurse__rom}

# It class attributes and methods
It_password: Property = Property(name="password", type=StringType)
It_name: Property = Property(name="name", type=StringType)
It.attributes={It_name, It_password}

# Patient class attributes and methods
Patient_disease: Property = Property(name="disease", type=StringType)
Patient_duration: Property = Property(name="duration", type=IntegerType)
Patient_room: Property = Property(name="room", type=IntegerType)
Patient_hasdoc: Property = Property(name="hasdoc", type=BooleanType)
Patient_hasroom: Property = Property(name="hasroom", type=BooleanType)
Patient.attributes={Patient_duration, Patient_room, Patient_hasdoc, Patient_disease, Patient_hasroom}

# Room class attributes and methods
Room_num: Property = Property(name="num", type=IntegerType)
Room_capasittity: Property = Property(name="capasittity", type=IntegerType)
Room_patients: Property = Property(name="patients", type=StringType)
Room_room_type: Property = Property(name="room_type", type=StringType)
Room_available: Property = Property(name="available", type=BooleanType)
Room__nurs: Property = Property(name="_nurs", type=nurse)
Room.attributes={Room_num, Room_capasittity, Room__nurs, Room_room_type, Room_available, Room_patients}

# appointment class attributes and methods
appointment_day: Property = Property(name="day", type=IntegerType)
appointment_hour: Property = Property(name="hour", type=IntegerType)
appointment_minute: Property = Property(name="minute", type=IntegerType)
appointment_duration: Property = Property(name="duration", type=IntegerType)
appointment_title: Property = Property(name="title", type=StringType)
appointment.attributes={appointment_day, appointment_hour, appointment_duration, appointment_minute, appointment_title}

# MainWindow class attributes and methods
MainWindow__logicdoc: Property = Property(name="_logicdoc", type=doctor)
MainWindow__logininit: Property = Property(name="_logininit", type=It)
MainWindow__Loginnurs: Property = Property(name="_Loginnurs", type=employee)
MainWindow_roomss: Property = Property(name="roomss", type=StringType)
MainWindow_nursess: Property = Property(name="nursess", type=StringType)
MainWindow_doctorss: Property = Property(name="doctorss", type=StringType)
MainWindow_patientss: Property = Property(name="patientss", type=StringType)
MainWindow_itss: Property = Property(name="itss", type=StringType)
MainWindow_UI: Property = Property(name="UI", type=StringType)
MainWindow.attributes={MainWindow_UI, MainWindow__Loginnurs, MainWindow_roomss, MainWindow__logininit, MainWindow_patientss, MainWindow__logicdoc, MainWindow_doctorss, MainWindow_itss, MainWindow_nursess}

# Relationships
Room__Patient: BinaryAssociation = BinaryAssociation(
    name="Room__Patient",
    ends={
        Property(name="patient0", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="room1", type=Room, multiplicity=Multiplicity(0, 1))
    }
)
nurse_Room: BinaryAssociation = BinaryAssociation(
    name="nurse_Room",
    ends={
        Property(name="room2", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="nurse3", type=nurse, multiplicity=Multiplicity(0, 1))
    }
)
Patient__doctor: BinaryAssociation = BinaryAssociation(
    name="Patient__doctor",
    ends={
        Property(name="doctor4", type=doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="patient_25", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_YdcWAOEYEee1VcqWCkiVQg",
    types={Person, employee, doctor, nurse, It, Patient, Room, appointment, MainWindow},
    associations={Room__Patient, nurse_Room, Patient__doctor},
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