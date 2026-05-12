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
User = Class(name="User")
Admin = Class(name="Admin")
Shopping_Cart = Class(name="Shopping_Cart")
Orders = Class(name="Orders")
Shipping_Info = Class(name="Shipping_Info")
Order_Details = Class(name="Order_Details")

# Customer class attributes and methods
Customer_Customer_Name: Property = Property(name="Customer_Name", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_Credit_Card_Info: Property = Property(name="Credit_Card_Info", type=IntegerType)
Customer.attributes={Customer_Credit_Card_Info, Customer_email, Customer_Address, Customer_Customer_Name}

# User class attributes and methods
User_User_Id: Property = Property(name="User_Id", type=IntegerType)
User_Password: Property = Property(name="Password", type=IntegerType)
User_Login_Status: Property = Property(name="Login_Status", type=StringType)
User.attributes={User_Login_Status, User_User_Id, User_Password}

# Admin class attributes and methods
Admin_AdminName: Property = Property(name="AdminName", type=StringType)
Admin_email: Property = Property(name="email", type=StringType)
Admin.attributes={Admin_email, Admin_AdminName}

# Shopping_Cart class attributes and methods
Shopping_Cart_Cart_id: Property = Property(name="Cart_id", type=IntegerType)
Shopping_Cart_Product_id: Property = Property(name="Product_id", type=IntegerType)
Shopping_Cart_Quantity: Property = Property(name="Quantity", type=IntegerType)
Shopping_Cart.attributes={Shopping_Cart_Cart_id, Shopping_Cart_Quantity, Shopping_Cart_Product_id}

# Orders class attributes and methods
Orders_Order_id: Property = Property(name="Order_id", type=IntegerType)
Orders_Date_Created: Property = Property(name="Date_Created", type=StringType)
Orders_Date_Shipped: Property = Property(name="Date_Shipped", type=StringType)
Orders_Customer_Id: Property = Property(name="Customer_Id", type=StringType)
Orders_Status: Property = Property(name="Status", type=StringType)
Orders.attributes={Orders_Date_Shipped, Orders_Date_Created, Orders_Order_id, Orders_Customer_Id, Orders_Status}

# Shipping_Info class attributes and methods
Shipping_Info_Shipping_Id: Property = Property(name="Shipping_Id", type=IntegerType)
Shipping_Info_Shipping_Type: Property = Property(name="Shipping_Type", type=StringType)
Shipping_Info.attributes={Shipping_Info_Shipping_Id, Shipping_Info_Shipping_Type}

# Order_Details class attributes and methods
Order_Details_Order_Id: Property = Property(name="Order_Id", type=IntegerType)
Order_Details_Product_Id: Property = Property(name="Product_Id", type=IntegerType)
Order_Details_Product_Name: Property = Property(name="Product_Name", type=StringType)
Order_Details_Quantity: Property = Property(name="Quantity", type=IntegerType)
Order_Details_Sub_Total: Property = Property(name="Sub_Total", type=StringType)
Order_Details_Unicast: Property = Property(name="Unicast", type=StringType)
Order_Details.attributes={Order_Details_Quantity, Order_Details_Order_Id, Order_Details_Unicast, Order_Details_Product_Name, Order_Details_Sub_Total, Order_Details_Product_Id}

# Relationships
Customer_Orders: BinaryAssociation = BinaryAssociation(
    name="Customer_Orders",
    ends={
        Property(name="orders0", type=Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Orders_Shipping_Info: BinaryAssociation = BinaryAssociation(
    name="Orders_Shipping_Info",
    ends={
        Property(name="shipping_Info2", type=Shipping_Info, multiplicity=Multiplicity(0, 1)),
        Property(name="orders3", type=Orders, multiplicity=Multiplicity(0, 1))
    }
)
Orders_Order_Details: BinaryAssociation = BinaryAssociation(
    name="Orders_Order_Details",
    ends={
        Property(name="order_Details4", type=Order_Details, multiplicity=Multiplicity(0, 1)),
        Property(name="orders5", type=Orders, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Cart",
    ends={
        Property(name="shopping_Cart6", type=Shopping_Cart, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ad4618a9_a01d_4997_a9f5_0ef663cb9da0",
    types={Customer, User, Admin, Shopping_Cart, Orders, Shipping_Info, Order_Details},
    associations={Customer_Orders, Orders_Shipping_Info, Orders_Order_Details, Customer_Shopping_Cart},
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