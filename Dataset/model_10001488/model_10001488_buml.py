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
UseCase3_UseCase = Class(name="UseCase3_UseCase")
user = Class(name="user")
Doctor = Class(name="Doctor")
Patient = Class(name="Patient")
Admin = Class(name="Admin")
Insurance = Class(name="Insurance")

# UseCase3_UseCase class attributes and methods

# user class attributes and methods
user_name: Property = Property(name="name", type=StringType)
user_phone_number: Property = Property(name="phone_number", type=IntegerType)
user_address: Property = Property(name="address", type=StringType)
user_email: Property = Property(name="email", type=StringType)
user_password: Property = Property(name="password", type=StringType)
user.attributes={user_password, user_name, user_phone_number, user_address, user_email}

# Doctor class attributes and methods
Doctor_email: Property = Property(name="email", type=StringType)
Doctor_password: Property = Property(name="password", type=StringType)
Doctor.attributes={Doctor_email, Doctor_password}

# Patient class attributes and methods
Patient_email: Property = Property(name="email", type=StringType)
Patient_password: Property = Property(name="password", type=StringType)
Patient.attributes={Patient_email, Patient_password}

# Admin class attributes and methods
Admin_uname: Property = Property(name="uname", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_uname, Admin_password}

# Insurance class attributes and methods
Insurance_email: Property = Property(name="email", type=StringType)
Insurance_password: Property = Property(name="password", type=StringType)
Insurance.attributes={Insurance_email, Insurance_password}

# Relationships
user_Doctor: BinaryAssociation = BinaryAssociation(
    name="user_Doctor",
    ends={
        Property(name="user_Doctor_00", type=Doctor, multiplicity=Multiplicity(0, 1)),
        Property(name="register1", type=user, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Patient: BinaryAssociation = BinaryAssociation(
    name="Doctor_Patient",
    ends={
        Property(name="request_to2", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="checks3", type=Doctor, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Doctor: BinaryAssociation = BinaryAssociation(
    name="Admin_Doctor",
    ends={
        Property(name="Admin_Doctor_04", type=Doctor, multiplicity=Multiplicity(1, 9999)),
        Property(name="accepts5", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Patient: BinaryAssociation = BinaryAssociation(
    name="Admin_Patient",
    ends={
        Property(name="Admin_Patient_06", type=Patient, multiplicity=Multiplicity(1, 9999)),
        Property(name="accepts7", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Admin_user: BinaryAssociation = BinaryAssociation(
    name="Admin_user",
    ends={
        Property(name="Admin_user_08", type=user, multiplicity=Multiplicity(1, 1)),
        Property(name="send_mail9", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Insurance_user: BinaryAssociation = BinaryAssociation(
    name="Insurance_user",
    ends={
        Property(name="user10", type=user, multiplicity=Multiplicity(0, 1)),
        Property(name="insurance11", type=Insurance, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_AP_doBzTEemK4rmwmdOnYw",
    types={UseCase3_UseCase, user, Doctor, Patient, Admin, Insurance},
    associations={user_Doctor, Doctor_Patient, Admin_Doctor, Admin_Patient, Admin_user, Insurance_user},
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