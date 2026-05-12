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
Users = Class(name="Users")
Customer = Class(name="Customer")
Administrator = Class(name="Administrator")
ShoppingCart = Class(name="ShoppingCart")
Order = Class(name="Order")
ShippingInfo = Class(name="ShippingInfo")
OrderDetails = Class(name="OrderDetails")
Shopping = Class(name="Shopping")

# Users class attributes and methods
Users_UserID: Property = Property(name="UserID", type=StringType)
Users_Password: Property = Property(name="Password", type=StringType)
Users_LoginStatus: Property = Property(name="LoginStatus", type=StringType)
Users_RegisterDate: Property = Property(name="RegisterDate", type=IntegerType)
Users.attributes={Users_LoginStatus, Users_RegisterDate, Users_Password, Users_UserID}

# Customer class attributes and methods
Customer_CustomerName: Property = Property(name="CustomerName", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_Email: Property = Property(name="Email", type=StringType)
Customer_CreditCartInfo: Property = Property(name="CreditCartInfo", type=StringType)
Customer_ShippingInfo: Property = Property(name="ShippingInfo", type=StringType)
Customer_AccountBalance: Property = Property(name="AccountBalance", type=IntegerType)
Customer.attributes={Customer_CustomerName, Customer_AccountBalance, Customer_CreditCartInfo, Customer_Email, Customer_ShippingInfo, Customer_Address}

# Administrator class attributes and methods
Administrator_AdminName: Property = Property(name="AdminName", type=StringType)
Administrator_Email: Property = Property(name="Email", type=StringType)
Administrator.attributes={Administrator_Email, Administrator_AdminName}

# ShoppingCart class attributes and methods
ShoppingCart_CartID: Property = Property(name="CartID", type=IntegerType)
ShoppingCart_ProductID: Property = Property(name="ProductID", type=IntegerType)
ShoppingCart_Quantity: Property = Property(name="Quantity", type=IntegerType)
ShoppingCart_DateAdded: Property = Property(name="DateAdded", type=IntegerType)
ShoppingCart.attributes={ShoppingCart_Quantity, ShoppingCart_CartID, ShoppingCart_DateAdded, ShoppingCart_ProductID}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_DateCreated: Property = Property(name="DateCreated", type=StringType)
Order_DateShipped: Property = Property(name="DateShipped", type=StringType)
Order_CustomerName: Property = Property(name="CustomerName", type=StringType)
Order_CustomerID: Property = Property(name="CustomerID", type=StringType)
Order_Status: Property = Property(name="Status", type=StringType)
Order_ShippingID: Property = Property(name="ShippingID", type=StringType)
Order.attributes={Order_DateShipped, Order_OrderID, Order_CustomerName, Order_ShippingID, Order_Status, Order_CustomerID, Order_DateCreated}

# ShippingInfo class attributes and methods
ShippingInfo_ShippingID: Property = Property(name="ShippingID", type=IntegerType)
ShippingInfo_ShippingType: Property = Property(name="ShippingType", type=StringType)
ShippingInfo_ShippingCost: Property = Property(name="ShippingCost", type=IntegerType)
ShippingInfo_ShippingRegionID: Property = Property(name="ShippingRegionID", type=IntegerType)
ShippingInfo.attributes={ShippingInfo_ShippingRegionID, ShippingInfo_ShippingID, ShippingInfo_ShippingType, ShippingInfo_ShippingCost}

# OrderDetails class attributes and methods
OrderDetails_OrderID: Property = Property(name="OrderID", type=IntegerType)
OrderDetails_ProductID: Property = Property(name="ProductID", type=IntegerType)
OrderDetails_ProductName: Property = Property(name="ProductName", type=StringType)
OrderDetails_Quantity: Property = Property(name="Quantity", type=IntegerType)
OrderDetails_UnitCost: Property = Property(name="UnitCost", type=IntegerType)
OrderDetails_SubTotal: Property = Property(name="SubTotal", type=IntegerType)
OrderDetails.attributes={OrderDetails_SubTotal, OrderDetails_OrderID, OrderDetails_ProductID, OrderDetails_Quantity, OrderDetails_ProductName, OrderDetails_UnitCost}

# Shopping class attributes and methods
Shopping_Name: Property = Property(name="Name", type=StringType)
Shopping_Location: Property = Property(name="Location", type=StringType)
Shopping_Identity: Property = Property(name="Identity", type=IntegerType)
Shopping.attributes={Shopping_Name, Shopping_Location, Shopping_Identity}

# Relationships
Customer_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Customer_ShoppingCart",
    ends={
        Property(name="shoppingCart0", type=ShoppingCart, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer1", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer3", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Order_ShippingInfo: BinaryAssociation = BinaryAssociation(
    name="Order_ShippingInfo",
    ends={
        Property(name="shippingInfo4", type=ShippingInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="order5", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Order_OrderDetails: BinaryAssociation = BinaryAssociation(
    name="Order_OrderDetails",
    ends={
        Property(name="has_a6", type=OrderDetails, multiplicity=Multiplicity(1, 1)),
        Property(name="order7", type=Order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_nAwJQBlREeig8qiayYYCew",
    types={Users, Customer, Administrator, ShoppingCart, Order, ShippingInfo, OrderDetails, Shopping},
    associations={Customer_ShoppingCart, Customer_Order, Order_ShippingInfo, Order_OrderDetails},
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