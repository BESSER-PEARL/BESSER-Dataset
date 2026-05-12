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
Membership_Card = Class(name="Membership_Card")
ViewOrder = Class(name="ViewOrder")
OrderItem = Class(name="OrderItem")
Menu = Class(name="Menu")
Bookings = Class(name="Bookings")
BookedTables = Class(name="BookedTables")

# Users class attributes and methods
Users_UserID: Property = Property(name="UserID", type=IntegerType)
Users_UserName: Property = Property(name="UserName", type=StringType)
Users_UserLevel: Property = Property(name="UserLevel", type=IntegerType)
Users.attributes={Users_UserName, Users_UserID, Users_UserLevel}

# Table class attributes and methods
Table_TableNo: Property = Property(name="TableNo", type=IntegerType)
Table_Occupied: Property = Property(name="Occupied", type=IntegerType)
Table.attributes={Table_Occupied, Table_TableNo}

# Order class attributes and methods
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_Date: Property = Property(name="Date", type=DateType)
Order_UserID: Property = Property(name="UserID", type=IntegerType)
Order_Total: Property = Property(name="Total", type=FloatType)
Order_DicountLvl: Property = Property(name="DicountLvl", type=IntegerType)
Order.attributes={Order_DicountLvl, Order_UserID, Order_Date, Order_OrderID, Order_Total}

# Membership_Card class attributes and methods
Membership_Card_ID: Property = Property(name="ID", type=IntegerType)
Membership_Card_DiscountLVL: Property = Property(name="DiscountLVL", type=IntegerType)
Membership_Card.attributes={Membership_Card_ID, Membership_Card_DiscountLVL}

# ViewOrder class attributes and methods
ViewOrder_getUser: Property = Property(name="getUser", type=IntegerType)
ViewOrder.attributes={ViewOrder_getUser}

# OrderItem class attributes and methods
OrderItem_OrderItemID: Property = Property(name="OrderItemID", type=IntegerType)
OrderItem_OrderID: Property = Property(name="OrderID", type=IntegerType)
OrderItem_ItemName: Property = Property(name="ItemName", type=StringType)
OrderItem_RemaningTime: Property = Property(name="RemaningTime", type=DateType)
OrderItem_Completed: Property = Property(name="Completed", type=IntegerType)
OrderItem.attributes={OrderItem_OrderID, OrderItem_OrderItemID, OrderItem_Completed, OrderItem_RemaningTime, OrderItem_ItemName}

# Menu class attributes and methods
Menu_MenuItem: Property = Property(name="MenuItem", type=StringType)
Menu_Category: Property = Property(name="Category", type=StringType)
Menu_Price: Property = Property(name="Price", type=FloatType)
Menu_Availability: Property = Property(name="Availability", type=IntegerType)
Menu.attributes={Menu_MenuItem, Menu_Availability, Menu_Category, Menu_Price}

# Bookings class attributes and methods
Bookings_BookingID: Property = Property(name="BookingID", type=IntegerType)
Bookings_CustomerName: Property = Property(name="CustomerName", type=StringType)
Bookings_Phone: Property = Property(name="Phone", type=StringType)
Bookings_People: Property = Property(name="People", type=IntegerType)
Bookings_Date: Property = Property(name="Date", type=DateType)
Bookings_Time: Property = Property(name="Time", type=DateType)
Bookings.attributes={Bookings_BookingID, Bookings_Time, Bookings_CustomerName, Bookings_People, Bookings_Date, Bookings_Phone}

# BookedTables class attributes and methods
BookedTables_TableNo: Property = Property(name="TableNo", type=IntegerType)
BookedTables_BookingID: Property = Property(name="BookingID", type=IntegerType)
BookedTables.attributes={BookedTables_TableNo, BookedTables_BookingID}

# Relationships
ViewOrder_OrderItem: BinaryAssociation = BinaryAssociation(
    name="ViewOrder_OrderItem",
    ends={
        Property(name="viewOrder9", type=ViewOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="orderItem8", type=OrderItem, multiplicity=Multiplicity(1, 9999))
    }
)
OrderItem_Order: BinaryAssociation = BinaryAssociation(
    name="OrderItem_Order",
    ends={
        Property(name="order10", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="orderItem11", type=OrderItem, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Users: BinaryAssociation = BinaryAssociation(
    name="Order_Users",
    ends={
        Property(name="users12", type=Users, multiplicity=Multiplicity(1, 1)),
        Property(name="order13", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
BookedTables_Table: BinaryAssociation = BinaryAssociation(
    name="BookedTables_Table",
    ends={
        Property(name="table14", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="bookedTables15", type=BookedTables, multiplicity=Multiplicity(1, 9999))
    }
)
Membership_Card_Order: BinaryAssociation = BinaryAssociation(
    name="Membership_Card_Order",
    ends={
        Property(name="order0", type=Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="membership_Card1", type=Membership_Card, multiplicity=Multiplicity(1, 1))
    }
)
Order_Table: BinaryAssociation = BinaryAssociation(
    name="Order_Table",
    ends={
        Property(name="table2", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="order3", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
Table_Bookings: BinaryAssociation = BinaryAssociation(
    name="Table_Bookings",
    ends={
        Property(name="bookings4", type=Bookings, multiplicity=Multiplicity(1, 1)),
        Property(name="table5", type=BookedTables, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Menu: BinaryAssociation = BinaryAssociation(
    name="Order_Menu",
    ends={
        Property(name="menu6", type=Menu, multiplicity=Multiplicity(1, 1)),
        Property(name="orderItem7", type=OrderItem, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_14c7a15f_b2b4_4f81_8ca1_f1a6517dd8a6",
    types={Users, Table, Order, Membership_Card, ViewOrder, OrderItem, Menu, Bookings, BookedTables},
    associations={ViewOrder_OrderItem, OrderItem_Order, Order_Users, BookedTables_Table, Membership_Card_Order, Order_Table, Table_Bookings, Order_Menu},
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