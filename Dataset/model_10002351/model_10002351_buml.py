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
Person = Class(name="Person")
employee = Class(name="employee")
doctor = Class(name="doctor")
nurse = Class(name="nurse")
It = Class(name="It")
Receptionist = Class(name="Receptionist")
Patient = Class(name="Patient")
Room = Class(name="Room")
appointment = Class(name="appointment")

# Person class attributes and methods
Person_name: Property = Property(name="name", type=StringType)
Person_age: Property = Property(name="age", type=IntegerType)
Person.attributes={Person_name, Person_age}

# employee class attributes and methods
employee_Salary: Property = Property(name="Salary", type=IntegerType)
employee_password: Property = Property(name="password", type=StringType)
employee_department: Property = Property(name="department", type=StringType)
employee_id: Property = Property(name="id", type=StringType)
employee.attributes={employee_id, employee_password, employee_department, employee_Salary}

# doctor class attributes and methods
doctor_weekappointment: Property = Property(name="weekappointment", type=StringType)
doctor_patient: Property = Property(name="patient", type=StringType)
doctor.attributes={doctor_weekappointment, doctor_patient}

# nurse class attributes and methods
nurse__rom: Property = Property(name="_rom", type=Room)
nurse.attributes={nurse__rom}

# It class attributes and methods
It_password: Property = Property(name="password", type=StringType)
It.attributes={It_password}

# Receptionist class attributes and methods

# Patient class attributes and methods
Patient_illness: Property = Property(name="illness", type=StringType)
Patient_id: Property = Property(name="id", type=StringType)
Patient__doc: Property = Property(name="_doc", type=doctor)
Patient__nur: Property = Property(name="_nur", type=nurse)
Patient.attributes={Patient__doc, Patient_id, Patient__nur, Patient_illness}

# Room class attributes and methods
Room_num: Property = Property(name="num", type=IntegerType)
Room_capasittity: Property = Property(name="capasittity", type=IntegerType)
Room_patients: Property = Property(name="patients", type=StringType)
Room_room_type: Property = Property(name="room_type", type=StringType)
Room_available: Property = Property(name="available", type=BooleanType)
Room.attributes={Room_num, Room_room_type, Room_available, Room_capasittity, Room_patients}

# appointment class attributes and methods
appointment_day: Property = Property(name="day", type=IntegerType)
appointment_hour: Property = Property(name="hour", type=IntegerType)
appointment_minute: Property = Property(name="minute", type=IntegerType)
appointment_duration: Property = Property(name="duration", type=IntegerType)
appointment.attributes={appointment_duration, appointment_hour, appointment_day, appointment_minute}

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
    name="ab19c32d_18c2_4c68_9f1a_d26cf0046c81",
    types={Person, employee, doctor, nurse, It, Receptionist, Patient, Room, appointment},
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