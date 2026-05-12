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
User = Class(name="User")
Shipping_Info = Class(name="Shipping_Info")
Shopping_Cart = Class(name="Shopping_Cart")
Orders = Class(name="Orders")
Order_Details = Class(name="Order_Details")
Administrator = Class(name="Administrator")
Item = Class(name="Item")
Products = Class(name="Products")
Customer = Class(name="Customer")

# User class attributes and methods
User_User_Id: Property = Property(name="User_Id", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User_loginStatus: Property = Property(name="loginStatus", type=StringType)
User.attributes={User_loginStatus, User_User_Id, User_Password}

# Shipping_Info class attributes and methods
Shipping_Info_Shipping_Id: Property = Property(name="Shipping_Id", type=IntegerType)
Shipping_Info_Shipping_Type: Property = Property(name="Shipping_Type", type=StringType)
Shipping_Info_Shipping_Cost: Property = Property(name="Shipping_Cost", type=IntegerType)
Shipping_Info_ShippingRegionId: Property = Property(name="ShippingRegionId", type=IntegerType)
Shipping_Info.attributes={Shipping_Info_Shipping_Type, Shipping_Info_ShippingRegionId, Shipping_Info_Shipping_Cost, Shipping_Info_Shipping_Id}

# Shopping_Cart class attributes and methods
Shopping_Cart_CartId: Property = Property(name="CartId", type=IntegerType)
Shopping_Cart_productId: Property = Property(name="productId", type=IntegerType)
Shopping_Cart_Quantity: Property = Property(name="Quantity", type=IntegerType)
Shopping_Cart_dateAdded: Property = Property(name="dateAdded", type=IntegerType)
Shopping_Cart.attributes={Shopping_Cart_productId, Shopping_Cart_dateAdded, Shopping_Cart_Quantity, Shopping_Cart_CartId}

# Orders class attributes and methods
Orders_OrderId: Property = Property(name="OrderId", type=IntegerType)
Orders_dateCreated: Property = Property(name="dateCreated", type=StringType)
Orders_Date: Property = Property(name="Date", type=StringType)
Orders_customerName: Property = Property(name="customerName", type=StringType)
Orders_CustomerId: Property = Property(name="CustomerId", type=StringType)
Orders_ShippingId: Property = Property(name="ShippingId", type=StringType)
Orders_status: Property = Property(name="status", type=StringType)
Orders.attributes={Orders_status, Orders_dateCreated, Orders_ShippingId, Orders_CustomerId, Orders_Date, Orders_OrderId, Orders_customerName}

# Order_Details class attributes and methods
Order_Details_orderId: Property = Property(name="orderId", type=IntegerType)
Order_Details_productId: Property = Property(name="productId", type=IntegerType)
Order_Details_productName: Property = Property(name="productName", type=StringType)
Order_Details_quantity: Property = Property(name="quantity", type=IntegerType)
Order_Details_unitcost: Property = Property(name="unitcost", type=IntegerType)
Order_Details_subtotal: Property = Property(name="subtotal", type=IntegerType)
Order_Details.attributes={Order_Details_productId, Order_Details_subtotal, Order_Details_unitcost, Order_Details_orderId, Order_Details_productName, Order_Details_quantity}

# Administrator class attributes and methods
Administrator_adminName: Property = Property(name="adminName", type=StringType)
Administrator_email: Property = Property(name="email", type=StringType)
Administrator.attributes={Administrator_email, Administrator_adminName}

# Item class attributes and methods
Item_name: Property = Property(name="name", type=StringType)
Item_unitcost: Property = Property(name="unitcost", type=IntegerType)
Item_pieceAvailable: Property = Property(name="pieceAvailable", type=IntegerType)
Item.attributes={Item_unitcost, Item_name, Item_pieceAvailable}

# Products class attributes and methods
Products_totral: Property = Property(name="totral", type=IntegerType)
Products_racknumber: Property = Property(name="racknumber", type=IntegerType)
Products.attributes={Products_racknumber, Products_totral}

# Customer class attributes and methods
Customer_customer: Property = Property(name="customer", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_credit_card_info: Property = Property(name="credit_card_info", type=StringType)
Customer_shipping_info: Property = Property(name="shipping_info", type=StringType)
Customer.attributes={Customer_credit_card_info, Customer_customer, Customer_shipping_info, Customer_email, Customer_address}

# Relationships
Customer_User: BinaryAssociation = BinaryAssociation(
    name="Customer_User",
    ends={
        Property(name="user0", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Shopping_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_Cart",
    ends={
        Property(name="shopping_Cart2", type=Shopping_Cart, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Orders: BinaryAssociation = BinaryAssociation(
    name="Customer_Orders",
    ends={
        Property(name="orders4", type=Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Orders_Shipping_Info: BinaryAssociation = BinaryAssociation(
    name="Orders_Shipping_Info",
    ends={
        Property(name="shipping_Info6", type=Shipping_Info, multiplicity=Multiplicity(1, 1)),
        Property(name="orders7", type=Orders, multiplicity=Multiplicity(1, 1))
    }
)
Orders_Order_Details: BinaryAssociation = BinaryAssociation(
    name="Orders_Order_Details",
    ends={
        Property(name="order_Details8", type=Order_Details, multiplicity=Multiplicity(1, 1)),
        Property(name="orders9", type=Orders, multiplicity=Multiplicity(1, 1))
    }
)
Products_Item: BinaryAssociation = BinaryAssociation(
    name="Products_Item",
    ends={
        Property(name="item10", type=Item, multiplicity=Multiplicity(0, 1)),
        Property(name="products11", type=Products, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Products: BinaryAssociation = BinaryAssociation(
    name="Administrator_Products",
    ends={
        Property(name="products12", type=Products, multiplicity=Multiplicity(0, 1)),
        Property(name="Administrator_Products_113", type=Administrator, multiplicity=Multiplicity(0, 1))
    }
)
User_Administrator: BinaryAssociation = BinaryAssociation(
    name="User_Administrator",
    ends={
        Property(name="administrator14", type=Administrator, multiplicity=Multiplicity(0, 1)),
        Property(name="user15", type=User, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Vq6OgK_4Eee6S77dw3LIvQ",
    types={User, Shipping_Info, Shopping_Cart, Orders, Order_Details, Administrator, Item, Products, Customer},
    associations={Customer_User, Customer_Shopping_Cart, Customer_Orders, Orders_Shipping_Info, Orders_Order_Details, Products_Item, Administrator_Products, User_Administrator},
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