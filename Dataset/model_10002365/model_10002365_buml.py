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
ReservationManagementSystem = Class(name="ReservationManagementSystem")
Booking = Class(name="Booking")
Table = Class(name="Table")
Report = Class(name="Report")
Order = Class(name="Order")
Food = Class(name="Food")
Staff = Class(name="Staff")
Waiter = Class(name="Waiter")
Chef = Class(name="Chef")
StaffUI = Class(name="StaffUI")
CustomerUI = Class(name="CustomerUI")

# ReservationManagementSystem class attributes and methods
ReservationManagementSystem_bookings: Property = Property(name="bookings", type=StringType)
ReservationManagementSystem.attributes={ReservationManagementSystem_bookings}

# Booking class attributes and methods
Booking_booking_id: Property = Property(name="booking_id", type=IntegerType)
Booking_date: Property = Property(name="date", type=DateType)
Booking_startTime: Property = Property(name="startTime", type=StringType)
Booking_endTime: Property = Property(name="endTime", type=StringType)
Booking_reservedTables: Property = Property(name="reservedTables", type=StringType)
Booking_customer_name: Property = Property(name="customer_name", type=StringType)
Booking_contact_no: Property = Property(name="contact_no", type=IntegerType)
Booking_email_id: Property = Property(name="email_id", type=StringType)
Booking.attributes={Booking_endTime, Booking_startTime, Booking_contact_no, Booking_customer_name, Booking_booking_id, Booking_email_id, Booking_reservedTables, Booking_date}

# Table class attributes and methods
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_table_id: Property = Property(name="table_id", type=StringType)
Table_avaliable: Property = Property(name="avaliable", type=BooleanType)
Table.attributes={Table_numSeats, Table_table_id, Table_avaliable}

# Report class attributes and methods
Report_report_id: Property = Property(name="report_id", type=StringType)
Report_orders: Property = Property(name="orders", type=StringType)
Report.attributes={Report_orders, Report_report_id}

# Order class attributes and methods
Order_order_id: Property = Property(name="order_id", type=StringType)
Order_foodList: Property = Property(name="foodList", type=StringType)
Order.attributes={Order_order_id, Order_foodList}

# Food class attributes and methods
Food_food_id: Property = Property(name="food_id", type=StringType)
Food_name: Property = Property(name="name", type=StringType)
Food_price: Property = Property(name="price", type=FloatType)
Food_prepared: Property = Property(name="prepared", type=BooleanType)
Food_served: Property = Property(name="served", type=BooleanType)
Food.attributes={Food_food_id, Food_served, Food_name, Food_prepared, Food_price}

# Staff class attributes and methods
Staff_staffId: Property = Property(name="staffId", type=StringType)
Staff_name: Property = Property(name="name", type=StringType)
Staff_type: Property = Property(name="type", type=StringType)
Staff.attributes={Staff_name, Staff_staffId, Staff_type}

# Waiter class attributes and methods

# Chef class attributes and methods

# StaffUI class attributes and methods

# CustomerUI class attributes and methods

# Relationships
Staff_StaffUI: BinaryAssociation = BinaryAssociation(
    name="Staff_StaffUI",
    ends={
        Property(name="Staff_StaffUI_00", type=StaffUI, multiplicity=Multiplicity(0, 9999)),
        Property(name="accesses1", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
Staff_ReservationManagementSystem: BinaryAssociation = BinaryAssociation(
    name="Staff_ReservationManagementSystem",
    ends={
        Property(name="reservationManagementSystem2", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="interacts3", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
CustomerUI_ReservationManagementSystem: BinaryAssociation = BinaryAssociation(
    name="CustomerUI_ReservationManagementSystem",
    ends={
        Property(name="CustomerUI_ReservationManagementSystem_04", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="interacts5", type=CustomerUI, multiplicity=Multiplicity(0, 9999))
    }
)
ReservationManagementSystem_Booking: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Booking",
    ends={
        Property(name="booking6", type=Booking, multiplicity=Multiplicity(0, 9999)),
        Property(name="ReservationManagementSystem_Booking_17", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1))
    }
)
ReservationManagementSystem_Report: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Report",
    ends={
        Property(name="generates8", type=Report, multiplicity=Multiplicity(0, 9999)),
        Property(name="reservationManagementSystem9", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1))
    }
)
Table_Order: BinaryAssociation = BinaryAssociation(
    name="Table_Order",
    ends={
        Property(name="has10", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="table11", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="Table_Booking_012", type=Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="reservedBy13", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Food: BinaryAssociation = BinaryAssociation(
    name="Order_Food",
    ends={
        Property(name="orde14", type=Food, multiplicity=Multiplicity(1, 9999)),
        Property(name="has15", type=Order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ac06486d_0fbf_4dfb_b283_357c77d8c832",
    types={ReservationManagementSystem, Booking, Table, Report, Order, Food, Staff, Waiter, Chef, StaffUI, CustomerUI},
    associations={Staff_StaffUI, Staff_ReservationManagementSystem, CustomerUI_ReservationManagementSystem, ReservationManagementSystem_Booking, ReservationManagementSystem_Report, Table_Order, Table_Booking, Order_Food},
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