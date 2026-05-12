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
SYSTEM = Class(name="SYSTEM")
POLICE_DEPARTMENT = Class(name="POLICE_DEPARTMENT")
HOME_SECURITY = Class(name="HOME_SECURITY")
OWNER = Class(name="OWNER")
HARDWARE = Class(name="HARDWARE")

# SYSTEM class attributes and methods

# POLICE_DEPARTMENT class attributes and methods

# HOME_SECURITY class attributes and methods

# OWNER class attributes and methods

# HARDWARE class attributes and methods

# Relationships
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart0", type=POLICE_DEPARTMENT, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser1", type=OWNER, multiplicity=Multiplicity(1, 1))
    }
)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="select_home_security2", type=SYSTEM, multiplicity=Multiplicity(1, 1)),
        Property(name="select_values3", type=OWNER, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="check_status4", type=HOME_SECURITY, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=SYSTEM, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart6", type=POLICE_DEPARTMENT, multiplicity=Multiplicity(1, 1)),
        Property(name="account7", type=HOME_SECURITY, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items8", type=HARDWARE, multiplicity=Multiplicity(1, 1)),
        Property(name="sc9", type=POLICE_DEPARTMENT, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0eca168e_1dd6_49cb_a962_82fc0cf1c5eb",
    types={SYSTEM, POLICE_DEPARTMENT, HOME_SECURITY, OWNER, HARDWARE},
    associations={WebUser_ShoppingCart, WebUser_Customer, Customer_Account, Account_ShoppingCart, ShoppingCart_LineItem},
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