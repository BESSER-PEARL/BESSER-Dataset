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
department = Class(name="department")
staff = Class(name="staff")
patient = Class(name="patient")
doctor = Class(name="doctor")
receptionist = Class(name="receptionist")
room = Class(name="room")
test = Class(name="test")
billing = Class(name="billing")
loan = Class(name="loan")
login = Class(name="login")
general = Class(name="general")
private = Class(name="private")

# department class attributes and methods
department_depart_id: Property = Property(name="depart_id", type=StringType)
department_loacation: Property = Property(name="loacation", type=StringType)
department.attributes={department_loacation, department_depart_id}

# staff class attributes and methods
staff_name: Property = Property(name="name", type=StringType)
staff.attributes={staff_name}

# patient class attributes and methods
patient_pid: Property = Property(name="pid", type=StringType)
patient_name: Property = Property(name="name", type=StringType)
patient_phone_no: Property = Property(name="phone_no", type=StringType)
patient_address: Property = Property(name="address", type=StringType)
patient_age: Property = Property(name="age", type=StringType)
patient_room_no: Property = Property(name="room_no", type=StringType)
patient.attributes={patient_phone_no, patient_address, patient_name, patient_room_no, patient_age, patient_pid}

# doctor class attributes and methods
doctor_did: Property = Property(name="did", type=StringType)
doctor_name: Property = Property(name="name", type=StringType)
doctor_dept: Property = Property(name="dept", type=StringType)
doctor_specilization: Property = Property(name="specilization", type=StringType)
doctor_phone_no: Property = Property(name="phone_no", type=StringType)
doctor.attributes={doctor_phone_no, doctor_specilization, doctor_did, doctor_dept, doctor_name}

# receptionist class attributes and methods
receptionist_rid: Property = Property(name="rid", type=StringType)
receptionist_name: Property = Property(name="name", type=StringType)
receptionist.attributes={receptionist_name, receptionist_rid}

# room class attributes and methods
room_room_no: Property = Property(name="room_no", type=StringType)
room.attributes={room_room_no}

# test class attributes and methods
test_disease_name: Property = Property(name="disease_name", type=StringType)
test.attributes={test_disease_name}

# billing class attributes and methods
billing_bill_no: Property = Property(name="bill_no", type=StringType)
billing_patient_name: Property = Property(name="patient_name", type=StringType)
billing_amount: Property = Property(name="amount", type=StringType)
billing.attributes={billing_patient_name, billing_bill_no, billing_amount}

# loan class attributes and methods
loan_patient_name: Property = Property(name="patient_name", type=StringType)
loan_amount: Property = Property(name="amount", type=StringType)
loan.attributes={loan_amount, loan_patient_name}

# login class attributes and methods
login_id: Property = Property(name="id", type=StringType)
login_name: Property = Property(name="name", type=StringType)
login_pass: Property = Property(name="pass", type=StringType)
login.attributes={login_name, login_id, login_pass}

# general class attributes and methods

# private class attributes and methods

# Relationships
department_staff: BinaryAssociation = BinaryAssociation(
    name="department_staff",
    ends={
        Property(name="staff0", type=staff, multiplicity=Multiplicity(1, 9999)),
        Property(name="department1", type=department, multiplicity=Multiplicity(1, 9999))
    }
)
doctor_test: BinaryAssociation = BinaryAssociation(
    name="doctor_test",
    ends={
        Property(name="test2", type=test, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctor3", type=doctor, multiplicity=Multiplicity(1, 1))
    }
)
patient_room: BinaryAssociation = BinaryAssociation(
    name="patient_room",
    ends={
        Property(name="room4", type=room, multiplicity=Multiplicity(1, 1)),
        Property(name="patient5", type=patient, multiplicity=Multiplicity(1, 1))
    }
)
patient_doctor: BinaryAssociation = BinaryAssociation(
    name="patient_doctor",
    ends={
        Property(name="doctor6", type=doctor, multiplicity=Multiplicity(1, 1)),
        Property(name="patient7", type=patient, multiplicity=Multiplicity(1, 9999))
    }
)
patient_billing: BinaryAssociation = BinaryAssociation(
    name="patient_billing",
    ends={
        Property(name="billing8", type=billing, multiplicity=Multiplicity(1, 1)),
        Property(name="patient9", type=patient, multiplicity=Multiplicity(1, 1))
    }
)
receptionist_login: BinaryAssociation = BinaryAssociation(
    name="receptionist_login",
    ends={
        Property(name="login10", type=login, multiplicity=Multiplicity(1, 1)),
        Property(name="receptionist11", type=receptionist, multiplicity=Multiplicity(1, 1))
    }
)
receptionist_billing: BinaryAssociation = BinaryAssociation(
    name="receptionist_billing",
    ends={
        Property(name="billing12", type=billing, multiplicity=Multiplicity(1, 9999)),
        Property(name="receptionist13", type=receptionist, multiplicity=Multiplicity(1, 1))
    }
)
billing_loan: BinaryAssociation = BinaryAssociation(
    name="billing_loan",
    ends={
        Property(name="loan14", type=loan, multiplicity=Multiplicity(1, 1)),
        Property(name="billing15", type=billing, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f0a32a36_a42c_4608_a94d_57dcbb9688f6",
    types={department, staff, patient, doctor, receptionist, room, test, billing, loan, login, general, private},
    associations={department_staff, doctor_test, patient_room, patient_doctor, patient_billing, receptionist_login, receptionist_billing, billing_loan},
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