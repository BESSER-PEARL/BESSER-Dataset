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
Customer = Class(name="Customer")
Product = Class(name="Product")
Shopping_Cart = Class(name="Shopping_Cart")
User = Class(name="User")
Order = Class(name="Order")
OrderDetails = Class(name="OrderDetails")
Existing_Customer_Actor = Class(name="Existing_Customer_Actor")
New_Customer_Actor = Class(name="New_Customer_Actor")
Login_UseCase = Class(name="Login_UseCase")
Browse_Categories_UseCase = Class(name="Browse_Categories_UseCase")
Place_Order_UseCase = Class(name="Place_Order_UseCase")
Registration_UseCase = Class(name="Registration_UseCase")
Verify_Password_UseCase = Class(name="Verify_Password_UseCase")
Display_Login_Error_UseCase = Class(name="Display_Login_Error_UseCase")
Product_search_UseCase = Class(name="Product_search_UseCase")
Product_Recommendation_UseCase = Class(name="Product_Recommendation_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
UseCase2_UseCase = Class(name="UseCase2_UseCase")

# Customer class attributes and methods
Customer_CustomerId: Property = Property(name="CustomerId", type=IntegerType)
Customer_Full_Name: Property = Property(name="Full_Name", type=StringType)
Customer_Email_Address: Property = Property(name="Email_Address", type=StringType)
Customer_Password: Property = Property(name="Password", type=StringType)
Customer_Delivery_address: Property = Property(name="Delivery_address", type=StringType)
Customer.attributes={Customer_CustomerId, Customer_Delivery_address, Customer_Full_Name, Customer_Email_Address, Customer_Password}

# Product class attributes and methods
Product_ModelNumber: Property = Property(name="ModelNumber", type=IntegerType)
Product_ModelName: Property = Property(name="ModelName", type=StringType)
Product_UnitCost: Property = Property(name="UnitCost", type=IntegerType)
Product_Description: Property = Property(name="Description", type=StringType)
Product_ProductId: Property = Property(name="ProductId", type=IntegerType)
Product_CategoryId: Property = Property(name="CategoryId", type=IntegerType)
Product.attributes={Product_ModelNumber, Product_CategoryId, Product_ModelName, Product_ProductId, Product_UnitCost, Product_Description}

# Shopping_Cart class attributes and methods
Shopping_Cart_RecordId: Property = Property(name="RecordId", type=IntegerType)
Shopping_Cart_CartId: Property = Property(name="CartId", type=IntegerType)
Shopping_Cart_Quantity: Property = Property(name="Quantity", type=IntegerType)
Shopping_Cart_ProductId: Property = Property(name="ProductId", type=IntegerType)
Shopping_Cart_DateCreated: Property = Property(name="DateCreated", type=IntegerType)
Shopping_Cart.attributes={Shopping_Cart_DateCreated, Shopping_Cart_CartId, Shopping_Cart_RecordId, Shopping_Cart_Quantity, Shopping_Cart_ProductId}

# User class attributes and methods
User_UserId: Property = Property(name="UserId", type=IntegerType)
User_Password: Property = Property(name="Password", type=StringType)
User.attributes={User_Password, User_UserId}

# Order class attributes and methods
Order_OrderId: Property = Property(name="OrderId", type=IntegerType)
Order_CustomerId: Property = Property(name="CustomerId", type=IntegerType)
Order_OrderDate: Property = Property(name="OrderDate", type=StringType)
Order_ShipDate: Property = Property(name="ShipDate", type=StringType)
Order.attributes={Order_OrderId, Order_CustomerId, Order_ShipDate, Order_OrderDate}

# OrderDetails class attributes and methods
OrderDetails_OrderId: Property = Property(name="OrderId", type=IntegerType)
OrderDetails_ProductId: Property = Property(name="ProductId", type=IntegerType)
OrderDetails_Quantity: Property = Property(name="Quantity", type=IntegerType)
OrderDetails_UnitCost: Property = Property(name="UnitCost", type=IntegerType)
OrderDetails.attributes={OrderDetails_Quantity, OrderDetails_UnitCost, OrderDetails_ProductId, OrderDetails_OrderId}

# Existing_Customer_Actor class attributes and methods

# New_Customer_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Browse_Categories_UseCase class attributes and methods

# Place_Order_UseCase class attributes and methods

# Registration_UseCase class attributes and methods

# Verify_Password_UseCase class attributes and methods

# Display_Login_Error_UseCase class attributes and methods

# Product_search_UseCase class attributes and methods

# Product_Recommendation_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# Relationships
Customer_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Cart",
    ends={
        Property(name="Customer_Shopping_Cart_00", type=Shopping_Cart, multiplicity=Multiplicity(1, 1)),
        Property(name="Customer_Shopping_Cart_11", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Order_OrderDetails: BinaryAssociation = BinaryAssociation(
    name="Order_OrderDetails",
    ends={
        Property(name="Order_OrderDetails_02", type=OrderDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="Order_OrderDetails_13", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Product_Order: BinaryAssociation = BinaryAssociation(
    name="Product_Order",
    ends={
        Property(name="Product_Order_04", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="Product_Order_15", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Shopping_Cart_Product: BinaryAssociation = BinaryAssociation(
    name="Shopping_Cart_Product",
    ends={
        Property(name="Shopping_Cart_Product_06", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="Shopping_Cart_Product_17", type=Shopping_Cart, multiplicity=Multiplicity(1, 1))
    }
)
Existing_Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Existing_Customer_Login",
    ends={
        Property(name="login8", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="existing_Customer9", type=Existing_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Existing_Customer_Browse_Products: BinaryAssociation = BinaryAssociation(
    name="Existing_Customer_Browse_Products",
    ends={
        Property(name="browse_Products10", type=Browse_Categories_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="existing_Customer11", type=Existing_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Existing_Customer_Place_Order: BinaryAssociation = BinaryAssociation(
    name="Existing_Customer_Place_Order",
    ends={
        Property(name="place_Order12", type=Place_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="existing_Customer13", type=Existing_Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f490fbc5_a33c_4f7a_bbd3_5588d425e10c",
    types={Customer, Product, Shopping_Cart, User, Order, OrderDetails, Existing_Customer_Actor, New_Customer_Actor, Login_UseCase, Browse_Categories_UseCase, Place_Order_UseCase, Registration_UseCase, Verify_Password_UseCase, Display_Login_Error_UseCase, Product_search_UseCase, Product_Recommendation_UseCase, UseCase_UseCase, UseCase2_UseCase},
    associations={Customer_Shopping_Cart, Order_OrderDetails, Product_Order, Shopping_Cart_Product, Existing_Customer_Login, Existing_Customer_Browse_Products, Existing_Customer_Place_Order},
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