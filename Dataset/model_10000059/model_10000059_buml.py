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
BookingController = Class(name="BookingController")
Table = Class(name="Table")
OrderController = Class(name="OrderController")
Membership_Card = Class(name="Membership_Card")
AdminController = Class(name="AdminController")
processQuery = Class(name="processQuery")
Login = Class(name="Login")

# BookingController class attributes and methods
BookingController_BookingID: Property = Property(name="BookingID", type=IntegerType)
BookingController_CustomerName: Property = Property(name="CustomerName", type=StringType)
BookingController_Phone: Property = Property(name="Phone", type=StringType)
BookingController_TableNo: Property = Property(name="TableNo", type=StringType)
BookingController_Date: Property = Property(name="Date", type=StringType)
BookingController_Time: Property = Property(name="Time", type=StringType)
BookingController.attributes={BookingController_BookingID, BookingController_TableNo, BookingController_Phone, BookingController_Date, BookingController_Time, BookingController_CustomerName}

# Table class attributes and methods
Table_TableNo: Property = Property(name="TableNo", type=StringType)
Table_Occupied: Property = Property(name="Occupied", type=BooleanType)
Table.attributes={Table_TableNo, Table_Occupied}

# OrderController class attributes and methods
OrderController_OrderID: Property = Property(name="OrderID", type=IntegerType)
OrderController_Date: Property = Property(name="Date", type=StringType)
OrderController_UserID: Property = Property(name="UserID", type=IntegerType)
OrderController_OrderTotal: Property = Property(name="OrderTotal", type=StringType)
OrderController.attributes={OrderController_OrderID, OrderController_UserID, OrderController_OrderTotal, OrderController_Date}

# Membership_Card class attributes and methods
Membership_Card_LoyaltyID: Property = Property(name="LoyaltyID", type=IntegerType)
Membership_Card_Discount: Property = Property(name="Discount", type=IntegerType)
Membership_Card.attributes={Membership_Card_LoyaltyID, Membership_Card_Discount}

# AdminController class attributes and methods
AdminController_UserID: Property = Property(name="UserID", type=IntegerType)
AdminController_UserName: Property = Property(name="UserName", type=StringType)
AdminController_UserLevel: Property = Property(name="UserLevel", type=IntegerType)
AdminController.attributes={AdminController_UserID, AdminController_UserLevel, AdminController_UserName}

# processQuery class attributes and methods

# Login class attributes and methods
Login_LoyaltyID: Property = Property(name="LoyaltyID", type=IntegerType)
Login_Discount: Property = Property(name="Discount", type=IntegerType)
Login.attributes={Login_Discount, Login_LoyaltyID}

# Relationships
Order_Table: BinaryAssociation = BinaryAssociation(
    name="Order_Table",
    ends={
        Property(name="is_ordered_by0", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="has1", type=OrderController, multiplicity=Multiplicity(1, 1))
    }
)
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="reserved2", type=BookingController, multiplicity=Multiplicity(1, 1)),
        Property(name="is_reserved_by3", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Membership_Card: BinaryAssociation = BinaryAssociation(
    name="Order_Membership_Card",
    ends={
        Property(name="membership_Card4", type=Membership_Card, multiplicity=Multiplicity(0, 1)),
        Property(name="order5", type=OrderController, multiplicity=Multiplicity(0, 9999))
    }
)
processQuery_AdminPanel: BinaryAssociation = BinaryAssociation(
    name="processQuery_AdminPanel",
    ends={
        Property(name="adminPanel6", type=AdminController, multiplicity=Multiplicity(0, 1)),
        Property(name="processQuery7", type=processQuery, multiplicity=Multiplicity(0, 1))
    }
)
processQuery_Booking: BinaryAssociation = BinaryAssociation(
    name="processQuery_Booking",
    ends={
        Property(name="booking8", type=BookingController, multiplicity=Multiplicity(0, 1)),
        Property(name="processQuery9", type=processQuery, multiplicity=Multiplicity(0, 1))
    }
)
processQuery_Order: BinaryAssociation = BinaryAssociation(
    name="processQuery_Order",
    ends={
        Property(name="order10", type=OrderController, multiplicity=Multiplicity(0, 1)),
        Property(name="processQuery11", type=processQuery, multiplicity=Multiplicity(0, 1))
    }
)
Login_processQuery: BinaryAssociation = BinaryAssociation(
    name="Login_processQuery",
    ends={
        Property(name="processQuery12", type=processQuery, multiplicity=Multiplicity(0, 1)),
        Property(name="login13", type=Login, multiplicity=Multiplicity(0, 1))
    }
)
processQuery_Table: BinaryAssociation = BinaryAssociation(
    name="processQuery_Table",
    ends={
        Property(name="table14", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="processQuery15", type=processQuery, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0877c0da_9e98_42d6_87a9_063942ac640f",
    types={BookingController, Table, OrderController, Membership_Card, AdminController, processQuery, Login},
    associations={Order_Table, Table_Booking, Order_Membership_Card, processQuery_AdminPanel, processQuery_Booking, processQuery_Order, Login_processQuery, processQuery_Table},
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