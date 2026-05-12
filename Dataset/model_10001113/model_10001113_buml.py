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

# Enumerations
Kitchen: Enumeration = Enumeration(
    name="Kitchen",
    literals={
            
    }
)

CustomerType: Enumeration = Enumeration(
    name="CustomerType",
    literals={
            
    }
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
Class_ = Class(name="Class")
Customer = Class(name="Customer")

# Manager class attributes and methods

# Waiter class attributes and methods

# Chef class attributes and methods
Chef_kitchenStation: Property = Property(name="kitchenStation", type=Kitchen)
Chef.attributes={Chef_kitchenStation}

# Staff class attributes and methods
Staff_staff_Id: Property = Property(name="staff_Id", type=StringType)
Staff_name: Property = Property(name="name", type=StringType)
Staff_jobType: Property = Property(name="jobType", type=IntegerType)
Staff_contact: Property = Property(name="contact", type=StringType)
Staff.attributes={Staff_jobType, Staff_contact, Staff_staff_Id, Staff_name}

# RMS class attributes and methods
RMS_bookings: Property = Property(name="bookings", type=StringType)
RMS.attributes={RMS_bookings}

# Report class attributes and methods
Report_orders: Property = Property(name="orders", type=StringType)
Report_totalSales: Property = Property(name="totalSales", type=StringType)
Report_profit: Property = Property(name="profit", type=StringType)
Report.attributes={Report_orders, Report_profit, Report_totalSales}

# Booking class attributes and methods
Booking_booking_Id: Property = Property(name="booking_Id", type=StringType)
Booking_type: Property = Property(name="type", type=IntegerType)
Booking_name: Property = Property(name="name", type=StringType)
Booking_contact: Property = Property(name="contact", type=StringType)
Booking_date: Property = Property(name="date", type=StringType)
Booking_reservedTables: Property = Property(name="reservedTables", type=StringType)
Booking.attributes={Booking_reservedTables, Booking_date, Booking_booking_Id, Booking_contact, Booking_name, Booking_type}

# Table class attributes and methods
Table_table_Id: Property = Property(name="table_Id", type=StringType)
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_occupied: Property = Property(name="occupied", type=BooleanType)
Table_specialRequest: Property = Property(name="specialRequest", type=StringType)
Table_order: Property = Property(name="order", type=StringType)
Table_customerDetail: Property = Property(name="customerDetail", type=Customer)
Table.attributes={Table_specialRequest, Table_table_Id, Table_order, Table_numSeats, Table_occupied, Table_customerDetail}

# Order class attributes and methods
Order_order_Id: Property = Property(name="order_Id", type=StringType)
Order_foodOrdered: Property = Property(name="foodOrdered", type=Food)
Order.attributes={Order_foodOrdered, Order_order_Id}

# Food class attributes and methods
Food_price: Property = Property(name="price", type=StringType)
Food_type: Property = Property(name="type", type=IntegerType)
Food_prepared: Property = Property(name="prepared", type=BooleanType)
Food_food_Id: Property = Property(name="food_Id", type=StringType)
Food_name: Property = Property(name="name", type=StringType)
Food_description: Property = Property(name="description", type=StringType)
Food_served: Property = Property(name="served", type=BooleanType)
Food.attributes={Food_price, Food_description, Food_served, Food_type, Food_food_Id, Food_prepared, Food_name}

# Class class attributes and methods

# Customer class attributes and methods
Customer_numFemale: Property = Property(name="numFemale", type=IntegerType)
Customer_numMale: Property = Property(name="numMale", type=IntegerType)
Customer_type: Property = Property(name="type", type=CustomerType)
Customer.attributes={Customer_numMale, Customer_numFemale, Customer_type}

# Relationships
accesses: BinaryAssociation = BinaryAssociation(
    name="accesses",
    ends={
        Property(name="is_accesses_by12", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="accesses13", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Table_Customer: BinaryAssociation = BinaryAssociation(
    name="Table_Customer",
    ends={
        Property(name="customer14", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="has15", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
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
    name="_86ed8c8b_f745_4f2c_8d50_37a081a22ea0",
    types={Manager, Waiter, Chef, Staff, RMS, Report, Booking, Table, Order, Food, Class_, Customer, Kitchen, CustomerType},
    associations={accesses, Table_Customer, Order_Food, Order_Table, Table_Booking, RMS_Booking, Staff_RMS, Report_RMS},
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