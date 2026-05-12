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
Event = Class(name="Event")
User = Class(name="User")
EventType = Class(name="EventType")
Registration = Class(name="Registration")

# Event class attributes and methods
Event_EventId: Property = Property(name="EventId", type=IntegerType)
Event_Address: Property = Property(name="Address", type=StringType)
Event_CurrentNumberOfPlayers: Property = Property(name="CurrentNumberOfPlayers", type=IntegerType)
Event_MaxNumberOfPlayers: Property = Property(name="MaxNumberOfPlayers", type=IntegerType)
Event_DateTime: Property = Property(name="DateTime", type=StringType)
Event_Description: Property = Property(name="Description", type=StringType)
Event_attribute: Property = Property(name="attribute", type=StringType)
Event.attributes={Event_EventId, Event_DateTime, Event_Description, Event_Address, Event_CurrentNumberOfPlayers, Event_attribute, Event_MaxNumberOfPlayers}

# User class attributes and methods
User_UserId: Property = Property(name="UserId", type=IntegerType)
User_Email: Property = Property(name="Email", type=StringType)
User_Login: Property = Property(name="Login", type=StringType)
User_Password: Property = Property(name="Password", type=StringType)
User_PhoneNumber: Property = Property(name="PhoneNumber", type=StringType)
User_DateOfBirth: Property = Property(name="DateOfBirth", type=StringType)
User.attributes={User_Email, User_Password, User_Login, User_PhoneNumber, User_UserId, User_DateOfBirth}

# EventType class attributes and methods
EventType_Type: Property = Property(name="Type", type=StringType)
EventType_EventTypeId: Property = Property(name="EventTypeId", type=IntegerType)
EventType.attributes={EventType_EventTypeId, EventType_Type}

# Registration class attributes and methods

# Relationships
User_Registration: BinaryAssociation = BinaryAssociation(
    name="User_Registration",
    ends={
        Property(name="registrations0", type=Registration, multiplicity=Multiplicity(0, 9999)),
        Property(name="user1", type=User, multiplicity=Multiplicity(1, 1))
    }
)
EventType_Event: BinaryAssociation = BinaryAssociation(
    name="EventType_Event",
    ends={
        Property(name="events2", type=Event, multiplicity=Multiplicity(0, 9999)),
        Property(name="event_type3", type=EventType, multiplicity=Multiplicity(1, 1))
    }
)
Event_Registration: BinaryAssociation = BinaryAssociation(
    name="Event_Registration",
    ends={
        Property(name="registrations4", type=Registration, multiplicity=Multiplicity(0, 9999)),
        Property(name="event5", type=Event, multiplicity=Multiplicity(1, 1))
    }
)
User_Event: BinaryAssociation = BinaryAssociation(
    name="User_Event",
    ends={
        Property(name="events6", type=Event, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_nagKUMTAEeeWu_SLkciAbg",
    types={Event, User, EventType, Registration},
    associations={User_Registration, EventType_Event, Event_Registration, User_Event},
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