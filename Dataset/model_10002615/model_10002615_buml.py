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
medicine = Class(name="medicine")
Bursar = Class(name="Bursar")
lab = Class(name="lab")
pharmacy = Class(name="pharmacy")

# Doctor class attributes and methods
Doctor_dentist: Property = Property(name="dentist", type=Doctor)
Doctor_women_doctor: Property = Property(name="women_doctor", type=Doctor)
Doctor_normal_doctor: Property = Property(name="normal_doctor", type=Doctor)
Doctor.attributes={Doctor_dentist, Doctor_women_doctor, Doctor_normal_doctor}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_firstname: Property = Property(name="firstname", type=StringType)
Patient_lastname: Property = Property(name="lastname", type=StringType)
Patient_phonenumber: Property = Property(name="phonenumber", type=IntegerType)
Patient_birthyear: Property = Property(name="birthyear", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient_blood_group: Property = Property(name="blood_group", type=IntegerType)
Patient_addr: Property = Property(name="addr", type=StringType)
Patient_email: Property = Property(name="email", type=StringType)
Patient.attributes={Patient_id, Patient_birthyear, Patient_addr, Patient_lastname, Patient_email, Patient_sex, Patient_firstname, Patient_blood_group, Patient_phonenumber}

# Room class attributes and methods
Room_roomno: Property = Property(name="roomno", type=IntegerType)
Room_roomname: Property = Property(name="roomname", type=StringType)
Room.attributes={Room_roomname, Room_roomno}

# Receptionist class attributes and methods
Receptionist_firstname: Property = Property(name="firstname", type=StringType)
Receptionist_lastname: Property = Property(name="lastname", type=StringType)
Receptionist.attributes={Receptionist_lastname, Receptionist_firstname}

# Bill class attributes and methods
Bill_billno: Property = Property(name="billno", type=StringType)
Bill_amount: Property = Property(name="amount", type=FloatType)
Bill.attributes={Bill_billno, Bill_amount}

# medicine class attributes and methods
medicine_id: Property = Property(name="id", type=IntegerType)
medicine_medicine: Property = Property(name="medicine", type=StringType)
medicine_price: Property = Property(name="price", type=IntegerType)
medicine.attributes={medicine_medicine, medicine_price, medicine_id}

# Bursar class attributes and methods
Bursar_firstname: Property = Property(name="firstname", type=StringType)
Bursar_lastname: Property = Property(name="lastname", type=StringType)
Bursar.attributes={Bursar_firstname, Bursar_lastname}

# lab class attributes and methods
lab_results: Property = Property(name="results", type=StringType)
lab_price: Property = Property(name="price", type=IntegerType)
lab.attributes={lab_price, lab_results}

# pharmacy class attributes and methods
pharmacy_medicine: Property = Property(name="medicine", type=StringType)
pharmacy_price: Property = Property(name="price", type=IntegerType)
pharmacy.attributes={pharmacy_medicine, pharmacy_price}

# Relationships
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="bill0", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="pat1", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
receptions: BinaryAssociation = BinaryAssociation(
    name="receptions",
    ends={
        Property(name="receptionist2", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="p3", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
lab_Patient: BinaryAssociation = BinaryAssociation(
    name="lab_Patient",
    ends={
        Property(name="assign4", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="lab5", type=lab, multiplicity=Multiplicity(0, 1))
    }
)
lab_Doctor: BinaryAssociation = BinaryAssociation(
    name="lab_Doctor",
    ends={
        Property(name="assign6", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="lab7", type=lab, multiplicity=Multiplicity(0, 1))
    }
)
pharmacy_Bursar: BinaryAssociation = BinaryAssociation(
    name="pharmacy_Bursar",
    ends={
        Property(name="medicine_cost8", type=Bursar, multiplicity=Multiplicity(0, 1)),
        Property(name="pharmacy9", type=pharmacy, multiplicity=Multiplicity(0, 1))
    }
)
pharmacy_Patient: BinaryAssociation = BinaryAssociation(
    name="pharmacy_Patient",
    ends={
        Property(name="gives_medicine10", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="pharmacy11", type=pharmacy, multiplicity=Multiplicity(0, 1))
    }
)
Patient_Doctor: BinaryAssociation = BinaryAssociation(
    name="Patient_Doctor",
    ends={
        Property(name="doctor12", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="patient13", type=Patient, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c715f949_048a_43ce_ba32_39f4abfce375",
    types={Doctor, Patient, Room, Receptionist, Bill, medicine, Bursar, lab, pharmacy},
    associations={Patient_Bill, receptions, lab_Patient, lab_Doctor, pharmacy_Bursar, pharmacy_Patient, Patient_Doctor},
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