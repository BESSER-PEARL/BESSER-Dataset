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
Restaurant_Reservation_System = Class(name="Restaurant_Reservation_System")
Booking = Class(name="Booking")
Table = Class(name="Table")
Reservation_status = Class(name="Reservation_status")
Staff = Class(name="Staff")
Administrator = Class(name="Administrator")
Restaurant_owner = Class(name="Restaurant_owner")
Management_UI = Class(name="Management_UI")
CustomerUI = Class(name="CustomerUI")
List__ = Class(name="List__")
List_re_ = Class(name="List_re_")
List_reservation_ = Class(name="List_reservation_")

# Restaurant_Reservation_System class attributes and methods
Restaurant_Reservation_System_bookings: Property = Property(name="bookings", type=StringType)
Restaurant_Reservation_System_Menu: Property = Property(name="Menu", type=StringType)
Restaurant_Reservation_System.attributes={Restaurant_Reservation_System_Menu, Restaurant_Reservation_System_bookings}

# Booking class attributes and methods
Booking_booking_id: Property = Property(name="booking_id", type=IntegerType)
Booking_date: Property = Property(name="date", type=DateType)
Booking_startTime: Property = Property(name="startTime", type=StringType)
Booking_endTime: Property = Property(name="endTime", type=StringType)
Booking_reservedTables: Property = Property(name="reservedTables", type=StringType)
Booking_customer_id: Property = Property(name="customer_id", type=StringType)
Booking_Restaurant_id: Property = Property(name="Restaurant_id", type=StringType)
Booking_person: Property = Property(name="person", type=IntegerType)
Booking.attributes={Booking_startTime, Booking_endTime, Booking_reservedTables, Booking_booking_id, Booking_customer_id, Booking_Restaurant_id, Booking_person, Booking_date}

# Table class attributes and methods
Table_quantity: Property = Property(name="quantity", type=IntegerType)
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_table_id: Property = Property(name="table_id", type=StringType)
Table.attributes={Table_quantity, Table_numSeats, Table_table_id}

# Reservation_status class attributes and methods
Reservation_status_report_id: Property = Property(name="report_id", type=StringType)
Reservation_status_reservation: Property = Property(name="reservation", type=List_reservation_)
Reservation_status.attributes={Reservation_status_reservation, Reservation_status_report_id}

# Staff class attributes and methods
Staff_user_id: Property = Property(name="user_id", type=StringType)
Staff_name: Property = Property(name="name", type=StringType)
Staff_type: Property = Property(name="type", type=StringType)
Staff.attributes={Staff_user_id, Staff_type, Staff_name}

# Administrator class attributes and methods
Administrator_user_id: Property = Property(name="user_id", type=IntegerType)
Administrator_email: Property = Property(name="email", type=StringType)
Administrator_user_name: Property = Property(name="user_name", type=StringType)
Administrator.attributes={Administrator_email, Administrator_user_name, Administrator_user_id}

# Restaurant_owner class attributes and methods
Restaurant_owner_user_id: Property = Property(name="user_id", type=StringType)
Restaurant_owner_email: Property = Property(name="email", type=StringType)
Restaurant_owner_username: Property = Property(name="username", type=StringType)
Restaurant_owner.attributes={Restaurant_owner_user_id, Restaurant_owner_username, Restaurant_owner_email}

# Management_UI class attributes and methods

# CustomerUI class attributes and methods

# List__ class attributes and methods

# List_re_ class attributes and methods

# List_reservation_ class attributes and methods

# Relationships
Staff_StaffUI: BinaryAssociation = BinaryAssociation(
    name="Staff_StaffUI",
    ends={
        Property(name="Staff_StaffUI_00", type=Management_UI, multiplicity=Multiplicity(0, 9999)),
        Property(name="accesses1", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
Staff_ReservationManagementSystem: BinaryAssociation = BinaryAssociation(
    name="Staff_ReservationManagementSystem",
    ends={
        Property(name="reservationManagementSystem2", type=Restaurant_Reservation_System, multiplicity=Multiplicity(1, 1)),
        Property(name="interacts3", type=Staff, multiplicity=Multiplicity(0, 9999))
    }
)
CustomerUI_ReservationManagementSystem: BinaryAssociation = BinaryAssociation(
    name="CustomerUI_ReservationManagementSystem",
    ends={
        Property(name="CustomerUI_ReservationManagementSystem_04", type=Restaurant_Reservation_System, multiplicity=Multiplicity(1, 1)),
        Property(name="interacts5", type=CustomerUI, multiplicity=Multiplicity(0, 9999))
    }
)
ReservationManagementSystem_Booking: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Booking",
    ends={
        Property(name="booking6", type=Booking, multiplicity=Multiplicity(0, 9999)),
        Property(name="ReservationManagementSystem_Booking_17", type=Restaurant_Reservation_System, multiplicity=Multiplicity(1, 1))
    }
)
ReservationManagementSystem_Report: BinaryAssociation = BinaryAssociation(
    name="ReservationManagementSystem_Report",
    ends={
        Property(name="generates8", type=Reservation_status, multiplicity=Multiplicity(0, 9999)),
        Property(name="reservationManagementSystem9", type=Restaurant_Reservation_System, multiplicity=Multiplicity(1, 1))
    }
)
Table_Booking: BinaryAssociation = BinaryAssociation(
    name="Table_Booking",
    ends={
        Property(name="Table_Booking_010", type=Booking, multiplicity=Multiplicity(1, 1)),
        Property(name="reservedBy11", type=Table, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9f7eb961_15ef_4658_804c_f0e8b406d5f0",
    types={Restaurant_Reservation_System, Booking, Table, Reservation_status, Staff, Administrator, Restaurant_owner, Management_UI, CustomerUI, List__, List_re_, List_reservation_},
    associations={Staff_StaffUI, Staff_ReservationManagementSystem, CustomerUI_ReservationManagementSystem, ReservationManagementSystem_Booking, ReservationManagementSystem_Report, Table_Booking},
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