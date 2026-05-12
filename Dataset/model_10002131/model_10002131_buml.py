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
Login_UseCase = Class(name="Login_UseCase")
insert_record_UseCase = Class(name="insert_record_UseCase")
generate_report_UseCase = Class(name="generate_report_UseCase")
update_record_UseCase = Class(name="update_record_UseCase")
Logout_UseCase = Class(name="Logout_UseCase")
Admin_Actor = Class(name="Admin_Actor")
Login_UseCase1 = Class(name="Login_UseCase1")
check_details_UseCase = Class(name="check_details_UseCase")
registered_UseCase = Class(name="registered_UseCase")
Name_UseCase = Class(name="Name_UseCase")
Password_UseCase = Class(name="Password_UseCase")
Student_Actor = Class(name="Student_Actor")
delete_record_UseCase = Class(name="delete_record_UseCase")
Admin = Class(name="Admin")
Employee = Class(name="Employee")

# Login_UseCase class attributes and methods

# insert_record_UseCase class attributes and methods

# generate_report_UseCase class attributes and methods

# update_record_UseCase class attributes and methods

# Logout_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# Login_UseCase1 class attributes and methods

# check_details_UseCase class attributes and methods

# registered_UseCase class attributes and methods

# Name_UseCase class attributes and methods

# Password_UseCase class attributes and methods

# Student_Actor class attributes and methods

# delete_record_UseCase class attributes and methods

# Admin class attributes and methods
Admin_username: Property = Property(name="username", type=Admin)
Admin_password: Property = Property(name="password", type=Admin_Actor)
Admin.attributes={Admin_username, Admin_password}

# Employee class attributes and methods
Employee_attribute: Property = Property(name="attribute", type=StringType)
Employee_attribute2: Property = Property(name="attribute2", type=StringType)
Employee_attribute3: Property = Property(name="attribute3", type=StringType)
Employee_attribute31: Property = Property(name="attribute31", type=StringType)
Employee.attributes={Employee_attribute3, Employee_attribute2, Employee_attribute31, Employee_attribute}

# Relationships
Admin__delete_record: BinaryAssociation = BinaryAssociation(
    name="Admin__delete_record",
    ends={
        Property(name="delete_record18", type=delete_record_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin19", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Login: BinaryAssociation = BinaryAssociation(
    name="Admin_Login",
    ends={
        Property(name="login0", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_update_Std: BinaryAssociation = BinaryAssociation(
    name="Admin_update_Std",
    ends={
        Property(name="update_Std2", type=insert_record_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin3", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_update_Rooms: BinaryAssociation = BinaryAssociation(
    name="Admin_update_Rooms",
    ends={
        Property(name="update_Rooms4", type=update_record_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin5", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_generate_invoice: BinaryAssociation = BinaryAssociation(
    name="Admin_generate_invoice",
    ends={
        Property(name="generate_invoice6", type=generate_report_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin7", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_UseCase: BinaryAssociation = BinaryAssociation(
    name="Admin_UseCase",
    ends={
        Property(name="useCase8", type=Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin9", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_registered: BinaryAssociation = BinaryAssociation(
    name="Student_registered",
    ends={
        Property(name="registered10", type=registered_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student11", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Name: BinaryAssociation = BinaryAssociation(
    name="Student_Name",
    ends={
        Property(name="name12", type=Name_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student13", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_Login: BinaryAssociation = BinaryAssociation(
    name="Student_Login",
    ends={
        Property(name="login14", type=Login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="student15", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Student_check_details: BinaryAssociation = BinaryAssociation(
    name="Student_check_details",
    ends={
        Property(name="check_details16", type=check_details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="student17", type=Student_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_q_q5IFhkEem2zdxW8Rsq_g",
    types={Login_UseCase, insert_record_UseCase, generate_report_UseCase, update_record_UseCase, Logout_UseCase, Admin_Actor, Login_UseCase1, check_details_UseCase, registered_UseCase, Name_UseCase, Password_UseCase, Student_Actor, delete_record_UseCase, Admin, Employee},
    associations={Admin__delete_record, Admin_Login, Admin_update_Std, Admin_update_Rooms, Admin_generate_invoice, Admin_UseCase, Student_registered, Student_Name, Student_Login, Student_check_details},
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