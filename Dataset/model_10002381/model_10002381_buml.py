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
Booking.attributes={Booking_contact_no, Booking_customer_name, Booking_startTime, Booking_endTime, Booking_email_id, Booking_reservedTables, Booking_booking_id, Booking_date}

# Table class attributes and methods
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_table_id: Property = Property(name="table_id", type=StringType)
Table_avaliable: Property = Property(name="avaliable", type=BooleanType)
Table.attributes={Table_table_id, Table_numSeats, Table_avaliable}

# CustomerUI class attributes and methods

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
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="Table_Booking_04", type=Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="reservedBy5", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ad4fe914_7a09_4448_81c9_c6cad8275774",
    types={ReservationManagementSystem, Booking, Table, CustomerUI},
    associations={CustomerUI_ReservationManagementSystem, ReservationManagementSystem_Booking, Table_Booking},
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