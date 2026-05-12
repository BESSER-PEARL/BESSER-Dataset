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
Doctor = Class(name="Doctor")
Patient = Class(name="Patient")
Room = Class(name="Room")
Receptionist = Class(name="Receptionist")
Bill = Class(name="Bill")
appointment = Class(name="appointment")
medicine = Class(name="medicine")
nurse = Class(name="nurse")

# Doctor class attributes and methods
Doctor_docid: Property = Property(name="docid", type=IntegerType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_department: Property = Property(name="department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=IntegerType)
Doctor_address: Property = Property(name="address", type=StringType)
Doctor.attributes={Doctor_department, Doctor_name, Doctor_phno, Doctor_specialization, Doctor_docid, Doctor_address}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_telno: Property = Property(name="telno", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient_roomno: Property = Property(name="roomno", type=IntegerType)
Patient.attributes={Patient_age, Patient_name, Patient_id, Patient_address, Patient_roomno, Patient_sex, Patient_telno}

# Room class attributes and methods
Room_roomno: Property = Property(name="roomno", type=IntegerType)
Room_roomtype: Property = Property(name="roomtype", type=StringType)
Room.attributes={Room_roomtype, Room_roomno}

# Receptionist class attributes and methods
Receptionist_id: Property = Property(name="id", type=IntegerType)
Receptionist_email: Property = Property(name="email", type=StringType)
Receptionist_username: Property = Property(name="username", type=StringType)
Receptionist_password: Property = Property(name="password", type=StringType)
Receptionist.attributes={Receptionist_id, Receptionist_password, Receptionist_email, Receptionist_username}

# Bill class attributes and methods
Bill_billno: Property = Property(name="billno", type=StringType)
Bill_patientname: Property = Property(name="patientname", type=StringType)
Bill_amount: Property = Property(name="amount", type=FloatType)
Bill.attributes={Bill_patientname, Bill_billno, Bill_amount}

# appointment class attributes and methods
appointment_A_no: Property = Property(name="A_no", type=IntegerType)
appointment_time: Property = Property(name="time", type=DateType)
appointment_p_id: Property = Property(name="p_id", type=IntegerType)
appointment_p_name: Property = Property(name="p_name", type=StringType)
appointment_d_name: Property = Property(name="d_name", type=StringType)
appointment.attributes={appointment_p_id, appointment_A_no, appointment_time, appointment_p_name, appointment_d_name}

# medicine class attributes and methods
medicine_m_code: Property = Property(name="m_code", type=IntegerType)
medicine_m_name: Property = Property(name="m_name", type=StringType)
medicine_quantity: Property = Property(name="quantity", type=IntegerType)
medicine_price: Property = Property(name="price", type=FloatType)
medicine.attributes={medicine_quantity, medicine_price, medicine_m_code, medicine_m_name}

# nurse class attributes and methods
nurse_id: Property = Property(name="id", type=IntegerType)
nurse_name: Property = Property(name="name", type=StringType)
nurse_contact: Property = Property(name="contact", type=IntegerType)
nurse_availability: Property = Property(name="availability", type=BooleanType)
nurse.attributes={nurse_contact, nurse_availability, nurse_name, nurse_id}

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patients0", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctors1", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="bill2", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="pat3", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
receptions: BinaryAssociation = BinaryAssociation(
    name="receptions",
    ends={
        Property(name="receptionist4", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="p5", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
manages: BinaryAssociation = BinaryAssociation(
    name="manages",
    ends={
        Property(name="bill6", type=Bill, multiplicity=Multiplicity(0, 9999)),
        Property(name="receptionist7", type=Receptionist, multiplicity=Multiplicity(1, 1))
    }
)
Doctor_appointment: BinaryAssociation = BinaryAssociation(
    name="Doctor_appointment",
    ends={
        Property(name="appointment8", type=appointment, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor9", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
Patient_appointment: BinaryAssociation = BinaryAssociation(
    name="Patient_appointment",
    ends={
        Property(name="appointment10", type=appointment, multiplicity=Multiplicity(0, 1)),
        Property(name="patient11", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Room: BinaryAssociation = BinaryAssociation(
    name="Patient_Room",
    ends={
        Property(name="room12", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="patient13", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)
Bill_medicine: BinaryAssociation = BinaryAssociation(
    name="Bill_medicine",
    ends={
        Property(name="medicine14", type=medicine, multiplicity=Multiplicity(0, 1)),
        Property(name="bill15", type=Bill, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_medicine: BinaryAssociation = BinaryAssociation(
    name="Doctor_medicine",
    ends={
        Property(name="medicine16", type=medicine, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor17", type=Doctor, multiplicity=Multiplicity(0, 1))
    }
)
nurse_Room: BinaryAssociation = BinaryAssociation(
    name="nurse_Room",
    ends={
        Property(name="room18", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="nurse19", type=nurse, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lEv2gAbyEeqFfO0RhT_ZfA",
    types={Doctor, Patient, Room, Receptionist, Bill, appointment, medicine, nurse},
    associations={Doctor_Patient, Patient_Bill, receptions, manages, Doctor_appointment, Patient_appointment, Patient_Room, Bill_medicine, Doctor_medicine, nurse_Room},
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