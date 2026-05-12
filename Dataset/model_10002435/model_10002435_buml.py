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
Account = Class(name="Account")
Customer = Class(name="Customer")
Order = Class(name="Order")
Shopping_Cart = Class(name="Shopping_Cart")
Item = Class(name="Item")

# Account class attributes and methods
Account_Username: Property = Property(name="Username", type=StringType)
Account_Password: Property = Property(name="Password", type=IntegerType)
Account.attributes={Account_Password, Account_Username}

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_emailAddress: Property = Property(name="emailAddress", type=StringType)
Customer_DOB: Property = Property(name="DOB", type=StringType)
Customer_cellNo: Property = Property(name="cellNo", type=FloatType)
Customer_Gender: Property = Property(name="Gender", type=StringType)
Customer.attributes={Customer_Gender, Customer_cellNo, Customer_name, Customer_emailAddress, Customer_DOB}

# Order class attributes and methods
Order_quantity: Property = Property(name="quantity", type=IntegerType)
Order_price: Property = Property(name="price", type=Item)
Order.attributes={Order_price, Order_quantity}

# Shopping_Cart class attributes and methods
Shopping_Cart_cartId: Property = Property(name="cartId", type=StringType)
Shopping_Cart.attributes={Shopping_Cart_cartId}

# Item class attributes and methods
Item_productId: Property = Property(name="productId", type=StringType)
Item_price: Property = Property(name="price", type=FloatType)
Item_colour: Property = Property(name="colour", type=StringType)
Item_size: Property = Property(name="size", type=StringType)
Item.attributes={Item_size, Item_colour, Item_price, Item_productId}

# Relationships
User_Myprofile: BinaryAssociation = BinaryAssociation(
    name="User_Myprofile",
    ends={
        Property(name="myprofile0", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post2", type=Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="user3", type=Account, multiplicity=Multiplicity(1, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login4", type=Item, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=Account, multiplicity=Multiplicity(0, 1))
    }
)
Orders_Friend: BinaryAssociation = BinaryAssociation(
    name="Orders_Friend",
    ends={
        Property(name="friend6", type=Shopping_Cart, multiplicity=Multiplicity(1, 9999)),
        Property(name="orders7", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Shopping_Cart_Login: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Login",
    ends={
        Property(name="Shopping_Cart_Login_08", type=Item, multiplicity=Multiplicity(1, 9999)),
        Property(name="Shopping_Cart_Login_19", type=Shopping_Cart, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b338556b_2b87_41d0_a0f6_743c31d1918d",
    types={Account, Customer, Order, Shopping_Cart, Item},
    associations={User_Myprofile, User_Post, User_Login, Orders_Friend, Shopping_Cart_Login},
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