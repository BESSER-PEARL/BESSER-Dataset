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
Invoice = Class(name="Invoice")
Order = Class(name="Order")
Product = Class(name="Product")
Chef = Class(name="Chef")
StaffUI = Class(name="StaffUI")
Cart = Class(name="Cart")
Registration = Class(name="Registration")
User = Class(name="User")

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
Booking.attributes={Booking_date, Booking_customer_name, Booking_startTime, Booking_booking_id, Booking_reservedTables, Booking_endTime}

# Table class attributes and methods
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_table_id: Property = Property(name="table_id", type=StringType)
Table_avaliable: Property = Property(name="avaliable", type=BooleanType)
Table.attributes={Table_avaliable, Table_table_id, Table_numSeats}

# Invoice class attributes and methods
Invoice_invoice_id: Property = Property(name="invoice_id", type=StringType)
Invoice_orders: Property = Property(name="orders", type=StringType)
Invoice.attributes={Invoice_orders, Invoice_invoice_id}

# Order class attributes and methods
Order_order_id: Property = Property(name="order_id", type=StringType)
Order_foodList: Property = Property(name="foodList", type=StringType)
Order.attributes={Order_order_id, Order_foodList}

# Product class attributes and methods
Product_food_id: Property = Property(name="food_id", type=StringType)
Product_name: Property = Property(name="name", type=StringType)
Product_price: Property = Property(name="price", type=FloatType)
Product_Note: Property = Property(name="Note", type=StringType)
Product.attributes={Product_price, Product_food_id, Product_Note, Product_name}

# Chef class attributes and methods

# StaffUI class attributes and methods

# Cart class attributes and methods
Cart_Product: Property = Property(name="Product", type=Product)
Cart.attributes={Cart_Product}

# Registration class attributes and methods
Registration_Password: Property = Property(name="Password", type=StringType)
Registration_Last_Name: Property = Property(name="Last_Name", type=StringType)
Registration_Gender: Property = Property(name="Gender", type=StringType)
Registration_First_Name: Property = Property(name="First_Name", type=StringType)
Registration_attribute5: Property = Property(name="attribute5", type=StringType)
Registration_UserName: Property = Property(name="UserName", type=StringType)
Registration_Email: Property = Property(name="Email", type=StringType)
Registration_attribute: Property = Property(name="attribute", type=StringType)
Registration.attributes={Registration_Gender, Registration_UserName, Registration_Last_Name, Registration_Password, Registration_attribute, Registration_attribute5, Registration_Email, Registration_First_Name}

# User class attributes and methods
User_User_Name: Property = Property(name="User_Name", type=StringType)
User_Passowrd: Property = Property(name="Passowrd", type=StringType)
User.attributes={User_User_Name, User_Passowrd}

# Relationships
Product_Cart: BinaryAssociation = BinaryAssociation(
    name="Product_Cart",
    ends={
        Property(name="product11", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="cart10", type=Cart, multiplicity=Multiplicity(1, 1))
    }
)
ReservationManagementSystem_Booking: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Booking",
    ends={
        Property(name="booking0", type=Booking, multiplicity=Multiplicity(0, 9999)),
        Property(name="ReservationManagementSystem_Booking_11", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1))
    }
)
ReservationManagementSystem_Report: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Report",
    ends={
        Property(name="generates2", type=Invoice, multiplicity=Multiplicity(0, 9999)),
        Property(name="reservationManagementSystem3", type=ReservationManagementSystem, multiplicity=Multiplicity(1, 1))
    }
)
Table_Order: BinaryAssociation = BinaryAssociation(
    name="Table_Order",
    ends={
        Property(name="has4", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="table5", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="Table_Booking_06", type=Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="reservedBy7", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Food: BinaryAssociation = BinaryAssociation(
    name="Order_Food",
    ends={
        Property(name="orde8", type=Product, multiplicity=Multiplicity(1, 9999)),
        Property(name="has9", type=Order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fb9353a2_bd5c_47a5_bc2d_28f756ed59c8",
    types={ReservationManagementSystem, Booking, Table, Invoice, Order, Product, Chef, StaffUI, Cart, Registration, User},
    associations={Product_Cart, ReservationManagementSystem_Booking, ReservationManagementSystem_Report, Table_Order, Table_Booking, Order_Food},
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