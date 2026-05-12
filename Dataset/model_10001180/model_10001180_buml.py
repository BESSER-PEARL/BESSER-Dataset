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
Table = Class(name="Table")
Order = Class(name="Order")
ViewOrder = Class(name="ViewOrder")
OrderList = Class(name="OrderList")
Menu = Class(name="Menu")
Bookings = Class(name="Bookings")
BookedTables = Class(name="BookedTables")
Checkout = Class(name="Checkout")
Membership = Class(name="Membership")

# Users class attributes and methods
Users_UserID: Property = Property(name="UserID", type=IntegerType)
Users_UserName: Property = Property(name="UserName", type=StringType)
Users_UserLevel: Property = Property(name="UserLevel", type=IntegerType)
Users_UserBday: Property = Property(name="UserBday", type=DateType)
Users.attributes={Users_UserBday, Users_UserName, Users_UserLevel, Users_UserID}

# Table class attributes and methods
Table_TableNo: Property = Property(name="TableNo", type=IntegerType)
Table_Occupied: Property = Property(name="Occupied", type=IntegerType)
Table.attributes={Table_Occupied, Table_TableNo}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_UserID: Property = Property(name="UserID", type=IntegerType)
Order_Date: Property = Property(name="Date", type=StringType)
Order_Completed: Property = Property(name="Completed", type=IntegerType)
Order.attributes={Order_OrderID, Order_Date, Order_UserID, Order_Completed}

# ViewOrder class attributes and methods
ViewOrder_getOrderList: Property = Property(name="getOrderList", type=IntegerType)
ViewOrder.attributes={ViewOrder_getOrderList}

# OrderList class attributes and methods
OrderList_OrderItemID: Property = Property(name="OrderItemID", type=IntegerType)
OrderList_OrderID: Property = Property(name="OrderID", type=IntegerType)
OrderList_ItemName: Property = Property(name="ItemName", type=StringType)
OrderList_RemaningTime: Property = Property(name="RemaningTime", type=DateType)
OrderList.attributes={OrderList_ItemName, OrderList_RemaningTime, OrderList_OrderID, OrderList_OrderItemID}

# Menu class attributes and methods
Menu_MenuItem: Property = Property(name="MenuItem", type=StringType)
Menu_Category: Property = Property(name="Category", type=StringType)
Menu_Price: Property = Property(name="Price", type=FloatType)
Menu_Availability: Property = Property(name="Availability", type=IntegerType)
Menu.attributes={Menu_Availability, Menu_Price, Menu_MenuItem, Menu_Category}

# Bookings class attributes and methods
Bookings_BookingID: Property = Property(name="BookingID", type=IntegerType)
Bookings_CustomerName: Property = Property(name="CustomerName", type=StringType)
Bookings_Phone: Property = Property(name="Phone", type=StringType)
Bookings_People: Property = Property(name="People", type=IntegerType)
Bookings_Date: Property = Property(name="Date", type=DateType)
Bookings_Time: Property = Property(name="Time", type=DateType)
Bookings.attributes={Bookings_Date, Bookings_People, Bookings_Phone, Bookings_CustomerName, Bookings_Time, Bookings_BookingID}

# BookedTables class attributes and methods
BookedTables_TableNo: Property = Property(name="TableNo", type=IntegerType)
BookedTables_BookingID: Property = Property(name="BookingID", type=IntegerType)
BookedTables.attributes={BookedTables_BookingID, BookedTables_TableNo}

# Checkout class attributes and methods
Checkout_checkoutID: Property = Property(name="checkoutID", type=IntegerType)
Checkout_checkoutAmount: Property = Property(name="checkoutAmount", type=FloatType)
Checkout.attributes={Checkout_checkoutID, Checkout_checkoutAmount}

# Membership class attributes and methods
Membership_loyaltyID: Property = Property(name="loyaltyID", type=IntegerType)
Membership_discount: Property = Property(name="discount", type=FloatType)
Membership.attributes={Membership_discount, Membership_loyaltyID}

# Relationships
Order_Table: BinaryAssociation = BinaryAssociation(
    name="Order_Table",
    ends={
        Property(name="table0", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="order1", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
Table_Bookings: BinaryAssociation = BinaryAssociation(
    name="Table_Bookings",
    ends={
        Property(name="bookings2", type=Bookings, multiplicity=Multiplicity(1, 1)),
        Property(name="table3", type=BookedTables, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Menu: BinaryAssociation = BinaryAssociation(
    name="Order_Menu",
    ends={
        Property(name="menu4", type=Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="orderItem5", type=OrderList, multiplicity=Multiplicity(1, 9999))
    }
)
ViewOrder_OrderItem: BinaryAssociation = BinaryAssociation(
    name="ViewOrder_OrderItem",
    ends={
        Property(name="orderItem6", type=OrderList, multiplicity=Multiplicity(1, 9999)),
        Property(name="viewOrder7", type=ViewOrder, multiplicity=Multiplicity(1, 1))
    }
)
OrderItem_Order: BinaryAssociation = BinaryAssociation(
    name="OrderItem_Order",
    ends={
        Property(name="order8", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="orderItem9", type=OrderList, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Users: BinaryAssociation = BinaryAssociation(
    name="Order_Users",
    ends={
        Property(name="users10", type=Users, multiplicity=Multiplicity(1, 1)),
        Property(name="order11", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
BookedTables_Table: BinaryAssociation = BinaryAssociation(
    name="BookedTables_Table",
    ends={
        Property(name="table12", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="bookedTables13", type=BookedTables, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Checkout: BinaryAssociation = BinaryAssociation(
    name="Order_Checkout",
    ends={
        Property(name="checkout14", type=Checkout, multiplicity=Multiplicity(1, 1)),
        Property(name="order15", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Membership_Checkout: BinaryAssociation = BinaryAssociation(
    name="Membership_Checkout",
    ends={
        Property(name="checkout16", type=Checkout, multiplicity=Multiplicity(1, 1)),
        Property(name="membership17", type=Membership, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8eb04ccd_d9c8_41f2_a86c_9e6032492a7a",
    types={Users, Table, Order, ViewOrder, OrderList, Menu, Bookings, BookedTables, Checkout, Membership},
    associations={Order_Table, Table_Bookings, Order_Menu, ViewOrder_OrderItem, OrderItem_Order, Order_Users, BookedTables_Table, Order_Checkout, Membership_Checkout},
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