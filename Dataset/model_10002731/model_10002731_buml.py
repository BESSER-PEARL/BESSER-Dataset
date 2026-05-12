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
Manager = Class(name="Manager")
Waiter = Class(name="Waiter")
Chef = Class(name="Chef")
Staff = Class(name="Staff")
RMS = Class(name="RMS")
Report = Class(name="Report")
Booking = Class(name="Booking")
Table = Class(name="Table")
Order = Class(name="Order")
Food = Class(name="Food")

# Manager class attributes and methods

# Waiter class attributes and methods

# Chef class attributes and methods

# Staff class attributes and methods
Staff_staff_Id: Property = Property(name="staff_Id", type=StringType)
Staff_name: Property = Property(name="name", type=StringType)
Staff_jobType: Property = Property(name="jobType", type=IntegerType)
Staff_contact: Property = Property(name="contact", type=StringType)
Staff.attributes={Staff_jobType, Staff_staff_Id, Staff_name, Staff_contact}

# RMS class attributes and methods
RMS_bookings: Property = Property(name="bookings", type=StringType)
RMS.attributes={RMS_bookings}

# Report class attributes and methods
Report_orders: Property = Property(name="orders", type=StringType)
Report_totalSales: Property = Property(name="totalSales", type=StringType)
Report_profit: Property = Property(name="profit", type=StringType)
Report.attributes={Report_totalSales, Report_profit, Report_orders}

# Booking class attributes and methods
Booking_date: Property = Property(name="date", type=StringType)
Booking_reservedTables: Property = Property(name="reservedTables", type=StringType)
Booking_booking_Id: Property = Property(name="booking_Id", type=StringType)
Booking_type: Property = Property(name="type", type=IntegerType)
Booking_name: Property = Property(name="name", type=StringType)
Booking_contact: Property = Property(name="contact", type=StringType)
Booking.attributes={Booking_contact, Booking_type, Booking_date, Booking_booking_Id, Booking_reservedTables, Booking_name}

# Table class attributes and methods
Table_table_Id: Property = Property(name="table_Id", type=StringType)
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_occupied: Property = Property(name="occupied", type=BooleanType)
Table_specialRequest: Property = Property(name="specialRequest", type=StringType)
Table_order: Property = Property(name="order", type=StringType)
Table.attributes={Table_numSeats, Table_order, Table_table_Id, Table_specialRequest, Table_occupied}

# Order class attributes and methods
Order_order_Id: Property = Property(name="order_Id", type=StringType)
Order_foodOrdered: Property = Property(name="foodOrdered", type=Food)
Order.attributes={Order_order_Id, Order_foodOrdered}

# Food class attributes and methods
Food_food_Id: Property = Property(name="food_Id", type=StringType)
Food_name: Property = Property(name="name", type=StringType)
Food_description: Property = Property(name="description", type=StringType)
Food_price: Property = Property(name="price", type=StringType)
Food_type: Property = Property(name="type", type=IntegerType)
Food_prepared: Property = Property(name="prepared", type=BooleanType)
Food_served: Property = Property(name="served", type=BooleanType)
Food.attributes={Food_prepared, Food_type, Food_served, Food_food_Id, Food_price, Food_name, Food_description}

# Relationships
Order_Food: BinaryAssociation = BinaryAssociation(
    name="Order_Food",
    ends={
        Property(name="has0", type=Food, multiplicity=Multiplicity(1, 9999)),
        Property(name="is_ordered_by1", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Table: BinaryAssociation = BinaryAssociation(
    name="Order_Table",
    ends={
        Property(name="is_ordered_by2", type=Table, multiplicity=Multiplicity(1, 1)),
        Property(name="has3", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="reserved4", type=Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="is_reserved_by5", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)
RMS_Booking: BinaryAssociation = BinaryAssociation(
    name="RMS_Booking",
    ends={
        Property(name="has6", type=Booking, multiplicity=Multiplicity(0, 9999)),
        Property(name="is_in7", type=RMS, multiplicity=Multiplicity(1, 1))
    }
)
Staff_RMS: BinaryAssociation = BinaryAssociation(
    name="Staff_RMS",
    ends={
        Property(name="Staff_RMS_08", type=RMS, multiplicity=Multiplicity(1, 1)),
        Property(name="accesses9", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
Report_RMS: BinaryAssociation = BinaryAssociation(
    name="Report_RMS",
    ends={
        Property(name="generates10", type=RMS, multiplicity=Multiplicity(1, 1)),
        Property(name="is_generated_by11", type=Report, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="d323aca6_30ea_412f_945d_4eb9fadc3eb0",
    types={Manager, Waiter, Chef, Staff, RMS, Report, Booking, Table, Order, Food},
    associations={Order_Food, Order_Table, Table_Booking, RMS_Booking, Staff_RMS, Report_RMS},
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