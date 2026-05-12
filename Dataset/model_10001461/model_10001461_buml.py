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
Login = Class(name="Login")
Customer = Class(name="Customer")
Admin = Class(name="Admin")
ShoppingCart = Class(name="ShoppingCart")

# Login class attributes and methods
Login_email: Property = Property(name="email", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_email, Login_password}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_sem: Property = Property(name="sem", type=StringType)
Customer_branch: Property = Property(name="branch", type=StringType)
Customer_password: Property = Property(name="password", type=StringType)
Customer_phone: Property = Property(name="phone", type=IntegerType)
Customer.attributes={Customer_phone, Customer_branch, Customer_password, Customer_email, Customer_name, Customer_sem}

# Admin class attributes and methods
Admin_email: Property = Property(name="email", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_password, Admin_email}

# ShoppingCart class attributes and methods
ShoppingCart_cartID: Property = Property(name="cartID", type=IntegerType)
ShoppingCart_productID: Property = Property(name="productID", type=IntegerType)
ShoppingCart_quantity: Property = Property(name="quantity", type=IntegerType)
ShoppingCart_dateAdded: Property = Property(name="dateAdded", type=StringType)
ShoppingCart.attributes={ShoppingCart_dateAdded, ShoppingCart_quantity, ShoppingCart_productID, ShoppingCart_cartID}

# Relationships
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="Customer_ShoppingCart_00", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="Customer_ShoppingCart_11", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_89lkwMUiEeeWu_SLkciAbg",
    types={Login, Customer, Admin, ShoppingCart},
    associations={Customer_ShoppingCart},
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