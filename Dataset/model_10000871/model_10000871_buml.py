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
Department = Class(name="Department")
Patient = Class(name="Patient")
Receptionist = Class(name="Receptionist")
Bill = Class(name="Bill")
Treatment = Class(name="Treatment")
Procedure = Class(name="Procedure")

# Doctor class attributes and methods
Doctor_docid: Property = Property(name="docid", type=IntegerType)
Doctor_name: Property = Property(name="name", type=StringType)
Doctor_department: Property = Property(name="department", type=StringType)
Doctor_specialization: Property = Property(name="specialization", type=StringType)
Doctor_phno: Property = Property(name="phno", type=IntegerType)
Doctor_address: Property = Property(name="address", type=StringType)
Doctor_departamentID: Property = Property(name="departamentID", type=IntegerType)
Doctor.attributes={Doctor_name, Doctor_phno, Doctor_specialization, Doctor_department, Doctor_address, Doctor_docid, Doctor_departamentID}

# Department class attributes and methods
Department_id: Property = Property(name="id", type=IntegerType)
Department_name: Property = Property(name="name", type=StringType)
Department.attributes={Department_name, Department_id}

# Patient class attributes and methods
Patient_id: Property = Property(name="id", type=IntegerType)
Patient_name: Property = Property(name="name", type=StringType)
Patient_telno: Property = Property(name="telno", type=IntegerType)
Patient_address: Property = Property(name="address", type=StringType)
Patient_age: Property = Property(name="age", type=IntegerType)
Patient_sex: Property = Property(name="sex", type=StringType)
Patient.attributes={Patient_name, Patient_address, Patient_age, Patient_telno, Patient_sex, Patient_id}

# Receptionist class attributes and methods
Receptionist_id: Property = Property(name="id", type=IntegerType)
Receptionist_attribute2: Property = Property(name="attribute2", type=StringType)
Receptionist.attributes={Receptionist_attribute2, Receptionist_id}

# Bill class attributes and methods
Bill_billno: Property = Property(name="billno", type=StringType)
Bill_patientname: Property = Property(name="patientname", type=StringType)
Bill_amount: Property = Property(name="amount", type=FloatType)
Bill.attributes={Bill_patientname, Bill_amount, Bill_billno}

# Treatment class attributes and methods
Treatment_idTreatment: Property = Property(name="idTreatment", type=IntegerType)
Treatment_idBill: Property = Property(name="idBill", type=IntegerType)
Treatment_patientID: Property = Property(name="patientID", type=IntegerType)
Treatment_procedureID: Property = Property(name="procedureID", type=IntegerType)
Treatment.attributes={Treatment_idTreatment, Treatment_patientID, Treatment_procedureID, Treatment_idBill}

# Procedure class attributes and methods
Procedure_name: Property = Property(name="name", type=StringType)
Procedure_price: Property = Property(name="price", type=IntegerType)
Procedure_idProcedure: Property = Property(name="idProcedure", type=IntegerType)
Procedure.attributes={Procedure_idProcedure, Procedure_name, Procedure_price}

# Relationships
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="patients0", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="doctors1", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Doctor_Department: BinaryAssociation = BinaryAssociation(
    name="Doctor_Department",
    ends={
        Property(name="depmt2", type=Department, multiplicity=Multiplicity(1, 1)),
        Property(name="doctor3", type=Doctor, multiplicity=Multiplicity(1, 9999))
    }
)
Patient_Bill: BinaryAssociation = BinaryAssociation(
    name="Patient_Bill",
    ends={
        Property(name="bill4", type=Bill, multiplicity=Multiplicity(1, 9999)),
        Property(name="pat5", type=Patient, multiplicity=Multiplicity(1, 9999))
    }
)
receptions: BinaryAssociation = BinaryAssociation(
    name="receptions",
    ends={
        Property(name="receptionist6", type=Receptionist, multiplicity=Multiplicity(1, 1)),
        Property(name="p7", type=Patient, multiplicity=Multiplicity(1, 1))
    }
)
manages: BinaryAssociation = BinaryAssociation(
    name="manages",
    ends={
        Property(name="sbill8", type=Bill, multiplicity=Multiplicity(1, 9999)),
        Property(name="receptionist9", type=Receptionist, multiplicity=Multiplicity(1, 9999))
    }
)
Treatment_Patient: BinaryAssociation = BinaryAssociation(
    name="Treatment_Patient",
    ends={
        Property(name="patient10", type=Patient, multiplicity=Multiplicity(0, 1)),
        Property(name="treatment11", type=Treatment, multiplicity=Multiplicity(0, 1))
    }
)
Procedure_Treatment: BinaryAssociation = BinaryAssociation(
    name="Procedure_Treatment",
    ends={
        Property(name="treatment12", type=Treatment, multiplicity=Multiplicity(1, 9999)),
        Property(name="procedure13", type=Procedure, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6a75b6f1_22b0_4916_9555_29c99eab923c",
    types={Doctor, Department, Patient, Receptionist, Bill, Treatment, Procedure},
    associations={Doctor_Patient, Doctor_Department, Patient_Bill, receptions, manages, Treatment_Patient, Procedure_Treatment},
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