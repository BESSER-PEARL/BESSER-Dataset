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
Voter = Class(name="Voter")
DataBase = Class(name="DataBase")
UserAdmin = Class(name="UserAdmin")
SuperAdmin = Class(name="SuperAdmin")
Candidate = Class(name="Candidate")
Integer_AdminID_String_Password_Interface = Class(name="Integer_AdminID_String_Password_Interface")
Integer_AdminID_String_Password2_Interface = Class(name="Integer_AdminID_String_Password2_Interface")

# Voter class attributes and methods
Voter_serialNum: Property = Property(name="serialNum", type=IntegerType)
Voter_password: Property = Property(name="password", type=StringType)
Voter.attributes={Voter_password, Voter_serialNum}

# DataBase class attributes and methods
DataBase_obj1: Property = Property(name="obj1", type=SuperAdmin)
DataBase_obj2: Property = Property(name="obj2", type=UserAdmin)
DataBase_obj3: Property = Property(name="obj3", type=Voter)
DataBase_obj4: Property = Property(name="obj4", type=Candidate)
DataBase.attributes={DataBase_obj4, DataBase_obj2, DataBase_obj3, DataBase_obj1}

# UserAdmin class attributes and methods
UserAdmin_adminID: Property = Property(name="adminID", type=IntegerType)
UserAdmin_password: Property = Property(name="password", type=StringType)
UserAdmin.attributes={UserAdmin_adminID, UserAdmin_password}

# SuperAdmin class attributes and methods
SuperAdmin_adminID: Property = Property(name="adminID", type=IntegerType)
SuperAdmin_password: Property = Property(name="password", type=StringType)
SuperAdmin.attributes={SuperAdmin_password, SuperAdmin_adminID}

# Candidate class attributes and methods

# Integer_AdminID_String_Password_Interface class attributes and methods

# Integer_AdminID_String_Password2_Interface class attributes and methods

# Relationships
DataBase_Voter: BinaryAssociation = BinaryAssociation(
    name="DataBase_Voter",
    ends={
        Property(name="voter0", type=Voter, multiplicity=Multiplicity(0, 1)),
        Property(name="dataBase1", type=DataBase, multiplicity=Multiplicity(0, 1))
    }
)
DataBase_SuperAdmin: BinaryAssociation = BinaryAssociation(
    name="DataBase_SuperAdmin",
    ends={
        Property(name="superAdmin2", type=SuperAdmin, multiplicity=Multiplicity(0, 1)),
        Property(name="dataBase3", type=DataBase, multiplicity=Multiplicity(0, 1))
    }
)
DataBase_UserAdmin: BinaryAssociation = BinaryAssociation(
    name="DataBase_UserAdmin",
    ends={
        Property(name="userAdmin4", type=UserAdmin, multiplicity=Multiplicity(0, 1)),
        Property(name="dataBase5", type=DataBase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_1afc93b4_b112_467d_9f27_bc61a382bb51",
    types={Voter, DataBase, UserAdmin, SuperAdmin, Candidate, Integer_AdminID_String_Password_Interface, Integer_AdminID_String_Password2_Interface},
    associations={DataBase_Voter, DataBase_SuperAdmin, DataBase_UserAdmin},
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