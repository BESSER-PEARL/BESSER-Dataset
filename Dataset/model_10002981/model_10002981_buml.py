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
Staff = Class(name="Staff")
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
Booking.attributes={Booking_booking_id, Booking_email_id, Booking_endTime, Booking_startTime, Booking_contact_no, Booking_reservedTables, Booking_date, Booking_customer_name}

# Table class attributes and methods
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_table_id: Property = Property(name="table_id", type=StringType)
Table_avaliable: Property = Property(name="avaliable", type=BooleanType)
Table.attributes={Table_numSeats, Table_avaliable, Table_table_id}

# Staff class attributes and methods
Staff_staffId: Property = Property(name="staffId", type=StringType)
Staff_name: Property = Property(name="name", type=StringType)
Staff_type: Property = Property(name="type", type=StringType)
Staff.attributes={Staff_name, Staff_type, Staff_staffId}

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
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="Table_Booking_08", type=Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="reservedBy9", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f1ac8606_7970_4903_9443_09bb8827128c",
    types={ReservationManagementSystem, Booking, Table, Staff, StaffUI, CustomerUI},
    associations={Staff_StaffUI, Staff_ReservationManagementSystem, CustomerUI_ReservationManagementSystem, ReservationManagementSystem_Booking, Table_Booking},
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