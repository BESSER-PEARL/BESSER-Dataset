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
Docter = Class(name="Docter")
Receptionist = Class(name="Receptionist")
Patients = Class(name="Patients")
Hospital = Class(name="Hospital")

# Docter class attributes and methods
Docter_ID: Property = Property(name="ID", type=IntegerType)
Docter_Name: Property = Property(name="Name", type=StringType)
Docter_Specialization: Property = Property(name="Specialization", type=StringType)
Docter_Rank: Property = Property(name="Rank", type=StringType)
Docter_Salary: Property = Property(name="Salary", type=StringType)
Docter_attribute2: Property = Property(name="attribute2", type=StringType)
Docter.attributes={Docter_Name, Docter_Rank, Docter_Specialization, Docter_ID, Docter_Salary, Docter_attribute2}

# Receptionist class attributes and methods
Receptionist_Employee_ID: Property = Property(name="Employee_ID", type=IntegerType)
Receptionist_Name: Property = Property(name="Name", type=StringType)
Receptionist.attributes={Receptionist_Employee_ID, Receptionist_Name}

# Patients class attributes and methods
Patients_Patient_name: Property = Property(name="Patient_name", type=StringType)
Patients_NIC_NO: Property = Property(name="NIC_NO", type=IntegerType)
Patients_Sickness: Property = Property(name="Sickness", type=StringType)
Patients_Phone_no: Property = Property(name="Phone_no", type=IntegerType)
Patients.attributes={Patients_NIC_NO, Patients_Phone_no, Patients_Sickness, Patients_Patient_name}

# Hospital class attributes and methods
Hospital_HR: Property = Property(name="HR", type=StringType)
Hospital_Operation_Theater: Property = Property(name="Operation_Theater", type=StringType)
Hospital_Cariology: Property = Property(name="Cariology", type=StringType)
Hospital.attributes={Hospital_HR, Hospital_Operation_Theater, Hospital_Cariology}

# Relationships
Docter_Patient: BinaryAssociation = BinaryAssociation(
    name="Docter_Patient",
    ends={
        Property(name="patient0", type=Patients, multiplicity=Multiplicity(1, 9999)),
        Property(name="docter1", type=Docter, multiplicity=Multiplicity(0, 1))
    }
)
Patients_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Patients_Receptionist",
    ends={
        Property(name="receptionist2", type=Receptionist, multiplicity=Multiplicity(0, 1)),
        Property(name="patients3", type=Patients, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lutxUKhNEeeEQN1ZyOr__g",
    types={Docter, Receptionist, Patients, Hospital},
    associations={Docter_Patient, Patients_Receptionist},
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