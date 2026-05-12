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
Null = Class(name="Null")
String = Class(name="String")
Category = Class(name="Category")
Number = Class(name="Number")
Array = Class(name="Array")
Visitor = Class(name="Visitor")
Provider = Class(name="Provider")
Documents = Class(name="Documents")
Print = Class(name="Print")
ArrPrint = Class(name="ArrPrint")
User1 = Class(name="User1")
User = Class(name="User", is_abstract=True)

# Null class attributes and methods

# String class attributes and methods
String_data: Property = Property(name="data", type=String)
String.attributes={String_data}

# Category class attributes and methods
Category_id: Property = Property(name="id", type=StringType)
Category_section: Property = Property(name="section", type=String)
Category_name: Property = Property(name="name", type=String)
Category_parent: Property = Property(name="parent", type=String)
Category.attributes={Category_section, Category_id, Category_parent, Category_name}

# Number class attributes and methods
Number_data: Property = Property(name="data", type=IntegerType)
Number.attributes={Number_data}

# Array class attributes and methods
Array_data: Property = Property(name="data", type=User)
Array.attributes={Array_data}

# Visitor class attributes and methods

# Provider class attributes and methods
Provider_uid: Property = Property(name="uid", type=StringType)
Provider_providerId: Property = Property(name="providerId", type=String)
Provider_email: Property = Property(name="email", type=String)
Provider_displayName: Property = Property(name="displayName", type=String)
Provider_photoURL: Property = Property(name="photoURL", type=String)
Provider.attributes={Provider_displayName, Provider_email, Provider_providerId, Provider_uid, Provider_photoURL}

# Documents class attributes and methods
Documents_file: Property = Property(name="file", type=StringType)
Documents_data: Property = Property(name="data", type=Provider)
Documents_file_name: Property = Property(name="file_name", type=StringType)
Documents_tab_counter: Property = Property(name="tab_counter", type=IntegerType)
Documents.attributes={Documents_file_name, Documents_data, Documents_tab_counter, Documents_file}

# Print class attributes and methods

# ArrPrint class attributes and methods

# User1 class attributes and methods
User1_attribute: Property = Property(name="attribute", type=StringType)
User1.attributes={User1_attribute}

# User class attributes and methods
User_id: Property = Property(name="id", type=StringType)
User_firstName: Property = Property(name="firstName", type=String)
User_lastName: Property = Property(name="lastName", type=String)
User_email: Property = Property(name="email", type=String)
User_phone: Property = Property(name="phone", type=String)
User_address: Property = Property(name="address", type=Documents)
User_photoURL: Property = Property(name="photoURL", type=String)
User.attributes={User_email, User_id, User_photoURL, User_firstName, User_address, User_lastName, User_phone}

# Domain Model
domain_model = DomainModel(
    name="c20421f4_f83b_479b_bc87_a424b0baeb25",
    types={Null, String, Category, Number, Array, Visitor, Provider, Documents, Print, ArrPrint, User1, User},
    associations={},
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