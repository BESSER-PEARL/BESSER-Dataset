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
Hotel_System_Component = Class(name="Hotel_System_Component")
Check_in_Guest_UseCase = Class(name="Check_in_Guest_UseCase")
Check_out_Guest_UseCase = Class(name="Check_out_Guest_UseCase")
View_Month_s_Statistics_UseCase = Class(name="View_Month_s_Statistics_UseCase")
Register_as_new_customer_UseCase = Class(name="Register_as_new_customer_UseCase")
Look_up_Reservation_UseCase = Class(name="Look_up_Reservation_UseCase")
Guest_Actor = Class(name="Guest_Actor")
Receptionist_Actor = Class(name="Receptionist_Actor")
Hotel_Manager_Actor = Class(name="Hotel_Manager_Actor")
Guest = Class(name="Guest")
Reservation = Class(name="Reservation")
Room = Class(name="Room")
inte = Class(name="inte")
Make__Reservation_external = Class(name="Make__Reservation_external")

# Hotel_System_Component class attributes and methods

# Check_in_Guest_UseCase class attributes and methods

# Check_out_Guest_UseCase class attributes and methods

# View_Month_s_Statistics_UseCase class attributes and methods

# Register_as_new_customer_UseCase class attributes and methods

# Look_up_Reservation_UseCase class attributes and methods

# Guest_Actor class attributes and methods

# Receptionist_Actor class attributes and methods

# Hotel_Manager_Actor class attributes and methods

# Guest class attributes and methods
Guest_Name: Property = Property(name="Name", type=StringType)
Guest_Address: Property = Property(name="Address", type=StringType)
Guest.attributes={Guest_Name, Guest_Address}

# Reservation class attributes and methods
Reservation_Reservation_id: Property = Property(name="Reservation_id", type=IntegerType)
Reservation_Start: Property = Property(name="Start", type=StringType)
Reservation_End: Property = Property(name="End", type=StringType)
Reservation.attributes={Reservation_Start, Reservation_Reservation_id, Reservation_End}

# Room class attributes and methods
Room_Number: Property = Property(name="Number", type=IntegerType)
Room_Guests: Property = Property(name="Guests", type=IntegerType)
Room.attributes={Room_Guests, Room_Number}

# inte class attributes and methods

# Make__Reservation_external class attributes and methods

# Relationships
Guest_Make__Reservation: BinaryAssociation = BinaryAssociation(
    name="Guest_Make__Reservation",
    ends={
        Property(name="make__Reservation0", type=Make__Reservation_external, multiplicity=Multiplicity(0, 1)),
        Property(name="guest1", type=Guest_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Check_in_Guest: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Check_in_Guest",
    ends={
        Property(name="check_in_Guest2", type=Check_in_Guest_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist3", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Check_out_Guest: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Check_out_Guest",
    ends={
        Property(name="check_out_Guest4", type=Check_out_Guest_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist5", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Hotel_Manager_View_Month_s_Statistics: BinaryAssociation = BinaryAssociation(
    name="Hotel_Manager_View_Month_s_Statistics",
    ends={
        Property(name="view_Month_s_Statistics6", type=View_Month_s_Statistics_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="hotel_Manager7", type=Hotel_Manager_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Guest_Reservation: BinaryAssociation = BinaryAssociation(
    name="Guest_Reservation",
    ends={
        Property(name="reservation8", type=Reservation, multiplicity=Multiplicity(0, 1)),
        Property(name="guest9", type=Guest, multiplicity=Multiplicity(1, 9999))
    }
)
Reservation_Room: BinaryAssociation = BinaryAssociation(
    name="Reservation_Room",
    ends={
        Property(name="room10", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="reservation11", type=Reservation, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e9bc574e_4929_46c4_8169_2e30fe912372",
    types={Hotel_System_Component, Check_in_Guest_UseCase, Check_out_Guest_UseCase, View_Month_s_Statistics_UseCase, Register_as_new_customer_UseCase, Look_up_Reservation_UseCase, Guest_Actor, Receptionist_Actor, Hotel_Manager_Actor, Guest, Reservation, Room, inte, Make__Reservation_external},
    associations={Guest_Make__Reservation, Receptionist_Check_in_Guest, Receptionist_Check_out_Guest, Hotel_Manager_View_Month_s_Statistics, Guest_Reservation, Reservation_Room},
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