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
Thick_Client_Users = Class(name="Thick_Client_Users")
Internet_Users = Class(name="Internet_Users")
System_User = Class(name="System_User")
User_Admin_Module = Class(name="User_Admin_Module")
End_User = Class(name="End_User")

# Thick_Client_Users class attributes and methods
Thick_Client_Users_Database_Access: Property = Property(name="Database_Access", type=System_User)
Thick_Client_Users_View_User: Property = Property(name="View_User", type=User_Admin_Module)
Thick_Client_Users.attributes={Thick_Client_Users_View_User, Thick_Client_Users_Database_Access}

# Internet_Users class attributes and methods
Internet_Users_Database_Access: Property = Property(name="Database_Access", type=System_User)
Internet_Users.attributes={Internet_Users_Database_Access}

# System_User class attributes and methods
System_User_login: Property = Property(name="login", type=StringType)
System_User_password: Property = Property(name="password", type=StringType)
System_User.attributes={System_User_password, System_User_login}

# User_Admin_Module class attributes and methods
User_Admin_Module_Generate_User: Property = Property(name="Generate_User", type=System_User)
User_Admin_Module_Delete_User: Property = Property(name="Delete_User", type=System_User)
User_Admin_Module_View_User: Property = Property(name="View_User", type=End_User)
User_Admin_Module.attributes={User_Admin_Module_Delete_User, User_Admin_Module_Generate_User, User_Admin_Module_View_User}

# End_User class attributes and methods
End_User_login: Property = Property(name="login", type=StringType)
End_User_password: Property = Property(name="password", type=StringType)
End_User_userType: Property = Property(name="userType", type=StringType)
End_User.attributes={End_User_password, End_User_userType, End_User_login}

# Relationships
WebUser_SecurityServices: BinaryAssociation = BinaryAssociation(
    name="WebUser_SecurityServices",
    ends={
        Property(name="Internet_Users0", type=End_User, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser1", type=Internet_Users, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="Thick_Client_Users2", type=Thick_Client_Users, multiplicity=Multiplicity(1, 1)),
        Property(name="endUser3", type=End_User, multiplicity=Multiplicity(1, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="Account4", type=System_User, multiplicity=Multiplicity(0, 9999)),
        Property(name="Admin5", type=User_Admin_Module, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_86363e69_7e65_4083_9593_f6efc09235e0",
    types={Thick_Client_Users, Internet_Users, System_User, User_Admin_Module, End_User},
    associations={WebUser_SecurityServices, WebUser_Customer, Account_Order},
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