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
shippingInfo = Class(name="shippingInfo")
Order_Details = Class(name="Order_Details")
Orders = Class(name="Orders")
Shopping_cart = Class(name="Shopping_cart")

# Customer class attributes and methods
Customer_customerName: Property = Property(name="customerName", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_email: Property = Property(name="email", type=StringType)
Customer_creditCardInfo: Property = Property(name="creditCardInfo", type=StringType)
Customer_shippingInfo: Property = Property(name="shippingInfo", type=StringType)
Customer_registration__: Property = Property(name="registration__", type=Customer)
Customer_login__: Property = Property(name="login__", type=Customer)
Customer_search__: Property = Property(name="search__", type=Customer)
Customer.attributes={Customer_registration__, Customer_creditCardInfo, Customer_address, Customer_login__, Customer_email, Customer_shippingInfo, Customer_customerName, Customer_search__}

# User class attributes and methods
User_userId: Property = Property(name="userId", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_loginStatus: Property = Property(name="loginStatus", type=StringType)
User_Logout__: Property = Property(name="Logout__", type=User)
User_Update_Account_Information__: Property = Property(name="Update_Account_Information__", type=User)
User_View_Account_Purchase_History__: Property = Property(name="View_Account_Purchase_History__", type=User)
User.attributes={User_Logout__, User_loginStatus, User_userId, User_password, User_View_Account_Purchase_History__, User_Update_Account_Information__}

# Admin class attributes and methods
Admin_adminName: Property = Property(name="adminName", type=StringType)
Admin_email: Property = Property(name="email", type=StringType)
Admin_attribute: Property = Property(name="attribute", type=StringType)
Admin_Reverse__: Property = Property(name="Reverse__", type=Admin)
Admin_Contact_Us__: Property = Property(name="Contact_Us__", type=Admin)
Admin_Help__: Property = Property(name="Help__", type=Admin)
Admin.attributes={Admin_Help__, Admin_email, Admin_Reverse__, Admin_attribute, Admin_Contact_Us__, Admin_adminName}

# shippingInfo class attributes and methods
shippingInfo_shippingId: Property = Property(name="shippingId", type=IntegerType)
shippingInfo_shippingType: Property = Property(name="shippingType", type=StringType)
shippingInfo_shippingCost: Property = Property(name="shippingCost", type=IntegerType)
shippingInfo_shippingRegionId: Property = Property(name="shippingRegionId", type=IntegerType)
shippingInfo_View_Shipping_Status__: Property = Property(name="View_Shipping_Status__", type=shippingInfo)
shippingInfo.attributes={shippingInfo_View_Shipping_Status__, shippingInfo_shippingCost, shippingInfo_shippingRegionId, shippingInfo_shippingId, shippingInfo_shippingType}

# Order_Details class attributes and methods
Order_Details_orderId: Property = Property(name="orderId", type=IntegerType)
Order_Details_productId: Property = Property(name="productId", type=IntegerType)
Order_Details_productName: Property = Property(name="productName", type=StringType)
Order_Details_quantity: Property = Property(name="quantity", type=IntegerType)
Order_Details_unitCost: Property = Property(name="unitCost", type=IntegerType)
Order_Details_subTotal: Property = Property(name="subTotal", type=IntegerType)
Order_Details_Payment__: Property = Property(name="Payment__", type=Order_Details)
Order_Details_Report_Generation: Property = Property(name="Report_Generation", type=Order_Details)
Order_Details.attributes={Order_Details_productName, Order_Details_productId, Order_Details_Report_Generation, Order_Details_orderId, Order_Details_quantity, Order_Details_Payment__, Order_Details_subTotal, Order_Details_unitCost}

# Orders class attributes and methods
Orders_orderId: Property = Property(name="orderId", type=IntegerType)
Orders_dateCreated: Property = Property(name="dateCreated", type=StringType)
Orders_dateShipped: Property = Property(name="dateShipped", type=StringType)
Orders_customerName: Property = Property(name="customerName", type=StringType)
Orders_customerId: Property = Property(name="customerId", type=StringType)
Orders_status: Property = Property(name="status", type=StringType)
Orders_shippingId: Property = Property(name="shippingId", type=StringType)
Orders.attributes={Orders_dateShipped, Orders_dateCreated, Orders_shippingId, Orders_customerId, Orders_orderId, Orders_status, Orders_customerName}

# Shopping_cart class attributes and methods
Shopping_cart_Checkout__: Property = Property(name="Checkout__", type=Shopping_cart)
Shopping_cart_cartId: Property = Property(name="cartId", type=IntegerType)
Shopping_cart_productId: Property = Property(name="productId", type=IntegerType)
Shopping_cart_quantity: Property = Property(name="quantity", type=IntegerType)
Shopping_cart_date: Property = Property(name="date", type=IntegerType)
Shopping_cart_Add_items_to_shopping_cart__: Property = Property(name="Add_items_to_shopping_cart__", type=Shopping_cart)
Shopping_cart_Delete_from_Shopping_Cart__: Property = Property(name="Delete_from_Shopping_Cart__", type=Shopping_cart)
Shopping_cart_change_to_cart__: Property = Property(name="change_to_cart__", type=Shopping_cart)
Shopping_cart.attributes={Shopping_cart_Add_items_to_shopping_cart__, Shopping_cart_date, Shopping_cart_cartId, Shopping_cart_productId, Shopping_cart_change_to_cart__, Shopping_cart_quantity, Shopping_cart_Delete_from_Shopping_Cart__, Shopping_cart_Checkout__}

# Relationships
Customer_Shopping_cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Shopping_cart",
    ends={
        Property(name="shopping_cart0", type=Shopping_cart, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Orders: BinaryAssociation = BinaryAssociation(
    name="Customer_Orders",
    ends={
        Property(name="orders2", type=Orders, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Orders_shippingInfo: BinaryAssociation = BinaryAssociation(
    name="Orders_shippingInfo",
    ends={
        Property(name="shippingInfo4", type=shippingInfo, multiplicity=Multiplicity(0, 1)),
        Property(name="orders5", type=Orders, multiplicity=Multiplicity(0, 1))
    }
)
Orders_Order_Details: BinaryAssociation = BinaryAssociation(
    name="Orders_Order_Details",
    ends={
        Property(name="order_Details6", type=Order_Details, multiplicity=Multiplicity(0, 1)),
        Property(name="orders7", type=Orders, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="__C2iMPV0EeeL5uCiN2F57w",
    types={Customer, User, Admin, shippingInfo, Order_Details, Orders, Shopping_cart},
    associations={Customer_Shopping_cart, Customer_Orders, Orders_shippingInfo, Orders_Order_Details},
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