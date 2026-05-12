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
Payment = Class(name="Payment")
ShoppingCart = Class(name="ShoppingCart")
Account = Class(name="Account")
User = Class(name="User")
Order = Class(name="Order")
Classes = Class(name="Classes")
Product = Class(name="Product")

# Payment class attributes and methods
Payment_Paytment_type: Property = Property(name="Paytment_type", type=StringType)
Payment.attributes={Payment_Paytment_type}

# ShoppingCart class attributes and methods
ShoppingCart_Update_cart: Property = Property(name="Update_cart", type=DateType)
ShoppingCart.attributes={ShoppingCart_Update_cart}

# Account class attributes and methods
Account_open: Property = Property(name="open", type=DateType)
Account_Valid_invalid: Property = Property(name="Valid_invalid", type=StringType)
Account.attributes={Account_Valid_invalid, Account_open}

# User class attributes and methods
User_login: Property = Property(name="login", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_login, User_password}

# Order class attributes and methods
Order_number: Property = Property(name="number", type=StringType)
Order_Items: Property = Property(name="Items", type=StringType)
Order.attributes={Order_number, Order_Items}

# Classes class attributes and methods
Classes_quantity: Property = Property(name="quantity", type=StringType)
Classes_Name: Property = Property(name="Name", type=StringType)
Classes.attributes={Classes_quantity, Classes_Name}

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_description: Property = Property(name="description", type=StringType)
Product.attributes={Product_name, Product_description}

# Relationships
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="shoppingCart0", type=ShoppingCart, multiplicity=Multiplicity(0, 1)),
        Property(name="webUser1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="cart2", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
        Property(name="account3", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
ShoppingCart_LineItem: BinaryAssociation = BinaryAssociation(
    name="ShoppingCart_LineItem",
    ends={
        Property(name="items4", type=Classes, multiplicity=Multiplicity(1, 1)),
        Property(name="sc5", type=ShoppingCart, multiplicity=Multiplicity(1, 1))
    }
)
Product_LineItem: BinaryAssociation = BinaryAssociation(
    name="Product_LineItem",
    ends={
        Property(name="lineItems6", type=Classes, multiplicity=Multiplicity(0, 9999)),
        Property(name="product7", type=Product, multiplicity=Multiplicity(1, 1))
    }
)
Order_LineItem: BinaryAssociation = BinaryAssociation(
    name="Order_LineItem",
    ends={
        Property(name="items8", type=Classes, multiplicity=Multiplicity(1, 9999)),
        Property(name="order9", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Account_Order: BinaryAssociation = BinaryAssociation(
    name="Account_Order",
    ends={
        Property(name="order10", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="account11", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="order12", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="payment13", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="cf9e1ff3_0d30_425e_b90f_b41f66a762e5",
    types={Payment, ShoppingCart, Account, User, Order, Classes, Product},
    associations={WebUser_ShoppingCart, Account_ShoppingCart, ShoppingCart_LineItem, Product_LineItem, Order_LineItem, Account_Order, Payment_Order},
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