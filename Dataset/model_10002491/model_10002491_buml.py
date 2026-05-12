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
CustomerUI = Class(name="CustomerUI")
Restaurants = Class(name="Restaurants")
Customer = Class(name="Customer")

# ReservationManagementSystem class attributes and methods
ReservationManagementSystem_bookings: Property = Property(name="bookings", type=StringType)
ReservationManagementSystem.attributes={ReservationManagementSystem_bookings}

# Booking class attributes and methods
Booking_b_id: Property = Property(name="b_id", type=IntegerType)
Booking_date: Property = Property(name="date", type=DateType)
Booking_startTime: Property = Property(name="startTime", type=StringType)
Booking_endTime: Property = Property(name="endTime", type=StringType)
Booking_reservedTables: Property = Property(name="reservedTables", type=StringType)
Booking_customer_name: Property = Property(name="customer_name", type=StringType)
Booking_contact_no: Property = Property(name="contact_no", type=IntegerType)
Booking_email_id: Property = Property(name="email_id", type=StringType)
Booking.attributes={Booking_contact_no, Booking_reservedTables, Booking_email_id, Booking_endTime, Booking_startTime, Booking_date, Booking_customer_name, Booking_b_id}

# Table class attributes and methods
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_table_id: Property = Property(name="table_id", type=StringType)
Table_avaliable: Property = Property(name="avaliable", type=BooleanType)
Table.attributes={Table_avaliable, Table_table_id, Table_numSeats}

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
Food.attributes={Food_served, Food_price, Food_name, Food_prepared, Food_food_id}

# CustomerUI class attributes and methods

# Restaurants class attributes and methods
Restaurants_r_ID: Property = Property(name="r_ID", type=IntegerType)
Restaurants_r_name: Property = Property(name="r_name", type=StringType)
Restaurants_r_address: Property = Property(name="r_address", type=StringType)
Restaurants_r_contact: Property = Property(name="r_contact", type=IntegerType)
Restaurants_r_cuisine: Property = Property(name="r_cuisine", type=StringType)
Restaurants.attributes={Restaurants_r_ID, Restaurants_r_contact, Restaurants_r_address, Restaurants_r_name, Restaurants_r_cuisine}

# Customer class attributes and methods
Customer_c_id: Property = Property(name="c_id", type=IntegerType)
Customer_c_name: Property = Property(name="c_name", type=StringType)
Customer_c_address: Property = Property(name="c_address", type=StringType)
Customer_c_email: Property = Property(name="c_email", type=StringType)
Customer_c_mobile: Property = Property(name="c_mobile", type=IntegerType)
Customer.attributes={Customer_c_email, Customer_c_name, Customer_c_address, Customer_c_mobile, Customer_c_id}

# Relationships
CustomerUI_ReservationManagementSystem: BinaryAssociation = BinaryAssociation(
    name="CustomerUI_ReservationManagementSystem",
    ends={
        Property(name="CustomerUI_ReservationManagementSystem_00", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="interacts1", type=CustomerUI, multiplicity=Multiplicity(0, 9999))
    }
)
ReservationManagementSystem_Booking: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Booking",
    ends={
        Property(name="booking2", type=Booking, multiplicity=Multiplicity(0, 9999)),
        Property(name="ReservationManagementSystem_Booking_13", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1))
    }
)
ReservationManagementSystem_Report: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Report",
    ends={
        Property(name="generates4", type=Report, multiplicity=Multiplicity(0, 9999)),
        Property(name="reservationManagementSystem5", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1))
    }
)
Table_Order: BinaryAssociation = BinaryAssociation(
    name="Table_Order",
    ends={
        Property(name="has6", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="table7", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="Table_Booking_08", type=Restaurants, multiplicity=Multiplicity(1, 1)),
        Property(name="reservedBy9", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Food: BinaryAssociation = BinaryAssociation(
    name="Order_Food",
    ends={
        Property(name="orde10", type=Food, multiplicity=Multiplicity(1, 9999)),
        Property(name="has11", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Restaurants_Booking2: BinaryAssociation = BinaryAssociation(
    name="Restaurants_Booking2",
    ends={
        Property(name="booking12", type=Booking, multiplicity=Multiplicity(0, 1)),
        Property(name="restaurants13", type=Restaurants, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b99c4430_9f8c_4332_8879_95909be22ca7",
    types={ReservationManagementSystem, Booking, Table, Report, Order, Food, CustomerUI, Restaurants, Customer},
    associations={CustomerUI_ReservationManagementSystem, ReservationManagementSystem_Booking, ReservationManagementSystem_Report, Table_Order, Table_Booking, Order_Food, Restaurants_Booking2},
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