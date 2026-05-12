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
Order_management_System = Class(name="Order_management_System")
Class_ = Class(name="Class")
Order = Class(name="Order")
Reservation = Class(name="Reservation")
Foods = Class(name="Foods")
Staff = Class(name="Staff")

# Order_management_System class attributes and methods
Order_management_System_Orderlist: Property = Property(name="Orderlist", type=Class_)
Order_management_System.attributes={Order_management_System_Orderlist}

# Class class attributes and methods

# Order class attributes and methods
Order_Orderlist: Property = Property(name="Orderlist", type=Class_)
Order_Amount: Property = Property(name="Amount", type=Class_)
Order_customername: Property = Property(name="customername", type=Class_)
Order_customer_address: Property = Property(name="customer_address", type=Class_)
Order_customerphone: Property = Property(name="customerphone", type=Class_)
Order_customer_email: Property = Property(name="customer_email", type=Class_)
Order.attributes={Order_Amount, Order_customer_address, Order_customername, Order_customer_email, Order_Orderlist, Order_customerphone}

# Reservation class attributes and methods
Reservation_seats: Property = Property(name="seats", type=Class_)
Reservation_table: Property = Property(name="table", type=Class_)
Reservation.attributes={Reservation_table, Reservation_seats}

# Foods class attributes and methods
Foods_Foodname: Property = Property(name="Foodname", type=Class_)
Foods_Catogory: Property = Property(name="Catogory", type=Class_)
Foods_price: Property = Property(name="price", type=Class_)
Foods_Ready: Property = Property(name="Ready", type=BooleanType)
Foods.attributes={Foods_Catogory, Foods_price, Foods_Ready, Foods_Foodname}

# Staff class attributes and methods
Staff_staffid: Property = Property(name="staffid", type=Class_)
Staff_name: Property = Property(name="name", type=Class_)
Staff.attributes={Staff_staffid, Staff_name}

# Relationships
Staff_Order_management_System: BinaryAssociation = BinaryAssociation(
    name="Staff_Order_management_System",
    ends={
        Property(name="Staff_Order_management_System_00", type=Order_management_System, multiplicity=Multiplicity(0, 1)),
        Property(name="staff1", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Order_management_System_Order: BinaryAssociation = BinaryAssociation(
    name="Order_management_System_Order",
    ends={
        Property(name="Order_management_System_Order_02", type=Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="Order_management_System_Order_13", type=Order_management_System, multiplicity=Multiplicity(0, 1))
    }
)
Order_Reservation: BinaryAssociation = BinaryAssociation(
    name="Order_Reservation",
    ends={
        Property(name="reservation4", type=Reservation, multiplicity=Multiplicity(0, 1)),
        Property(name="order5", type=Order, multiplicity=Multiplicity(1, 9999))
    }
)
Order_Foods: BinaryAssociation = BinaryAssociation(
    name="Order_Foods",
    ends={
        Property(name="foods6", type=Foods, multiplicity=Multiplicity(1, 9999)),
        Property(name="order7", type=Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_uUddIOVsEeekKLRLyKXO4Q",
    types={Order_management_System, Class_, Order, Reservation, Foods, Staff},
    associations={Staff_Order_management_System, Order_management_System_Order, Order_Reservation, Order_Foods},
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