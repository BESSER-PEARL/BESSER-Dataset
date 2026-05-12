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
ReservationType: Enumeration = Enumeration(
    name="ReservationType",
    literals={
            
    }
)

Date: Enumeration = Enumeration(
    name="Date",
    literals={
            
    }
)

ReservationType2: Enumeration = Enumeration(
    name="ReservationType2",
    literals={
            
    }
)

# Classes
Waiter = Class(name="Waiter")
Host = Class(name="Host")
Order = Class(name="Order")
Guest = Class(name="Guest")
Kitchen = Class(name="Kitchen")
Reservation = Class(name="Reservation")
Table = Class(name="Table")
Party = Class(name="Party")
Bill = Class(name="Bill")
Payment = Class(name="Payment")
Staff = Class(name="Staff")
Online_Customer = Class(name="Online_Customer")

# Waiter class attributes and methods

# Host class attributes and methods

# Order class attributes and methods

# Guest class attributes and methods
Guest_Name: Property = Property(name="Name", type=StringType)
Guest_Phone: Property = Property(name="Phone", type=StringType)
Guest_Guest_ID: Property = Property(name="Guest_ID", type=StringType)
Guest.attributes={Guest_Guest_ID, Guest_Name, Guest_Phone}

# Kitchen class attributes and methods

# Reservation class attributes and methods
Reservation_Date: Property = Property(name="Date", type=Date)
Reservation_Time: Property = Property(name="Time", type=StringType)
Reservation_ReservationID: Property = Property(name="ReservationID", type=StringType)
Reservation.attributes={Reservation_Date, Reservation_Time, Reservation_ReservationID}

# Table class attributes and methods
Table_Capacity: Property = Property(name="Capacity", type=IntegerType)
Table_TableID: Property = Property(name="TableID", type=StringType)
Table.attributes={Table_Capacity, Table_TableID}

# Party class attributes and methods
Party_Number_of_Guests: Property = Property(name="Number_of_Guests", type=IntegerType)
Party_Number_Of_Adults: Property = Property(name="Number_Of_Adults", type=IntegerType)
Party_Number_Of_Children: Property = Property(name="Number_Of_Children", type=IntegerType)
Party.attributes={Party_Number_Of_Adults, Party_Number_of_Guests, Party_Number_Of_Children}

# Bill class attributes and methods
Bill_TotalAmount: Property = Property(name="TotalAmount", type=IntegerType)
Bill_Tax: Property = Property(name="Tax", type=IntegerType)
Bill_Tip: Property = Property(name="Tip", type=IntegerType)
Bill.attributes={Bill_Tax, Bill_Tip, Bill_TotalAmount}

# Payment class attributes and methods

# Staff class attributes and methods
Staff_Staff_ID: Property = Property(name="Staff_ID", type=StringType)
Staff_Name: Property = Property(name="Name", type=StringType)
Staff_JobType: Property = Property(name="JobType", type=StringType)
Staff_Phone: Property = Property(name="Phone", type=StringType)
Staff.attributes={Staff_JobType, Staff_Phone, Staff_Name, Staff_Staff_ID}

# Online_Customer class attributes and methods

# Relationships
Host_Reservation: BinaryAssociation = BinaryAssociation(
    name="Host_Reservation",
    ends={
        Property(name="reservation0", type=Reservation, multiplicity=Multiplicity(0, 1)),
        Property(name="host1", type=Host, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Order: BinaryAssociation = BinaryAssociation(
    name="Waiter_Order",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter3", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)
Kitchen_Order: BinaryAssociation = BinaryAssociation(
    name="Kitchen_Order",
    ends={
        Property(name="order4", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="kitchen5", type=Kitchen, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Bill: BinaryAssociation = BinaryAssociation(
    name="Waiter_Bill",
    ends={
        Property(name="bill6", type=Bill, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter7", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Table: BinaryAssociation = BinaryAssociation(
    name="Waiter_Table",
    ends={
        Property(name="table8", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter9", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)
Reservation_Table: BinaryAssociation = BinaryAssociation(
    name="Reservation_Table",
    ends={
        Property(name="table10", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation11", type=Reservation, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_29657bf3_760a_4fe8_ae65_41f90851614d",
    types={Waiter, Host, Order, Guest, Kitchen, Reservation, Table, Party, Bill, Payment, Staff, Online_Customer, ReservationType, Date, ReservationType2},
    associations={Host_Reservation, Waiter_Order, Kitchen_Order, Waiter_Bill, Waiter_Table, Reservation_Table},
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