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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

# Classes
Event = Class(name="Event")
Serie = Class(name="Serie")
Session = Class(name="Session")
SessionType = Class(name="SessionType")
Room = Class(name="Room")

# Event class attributes and methods
Event_id: Property = Property(name="id", type=IntegerType)
Event_acronym: Property = Property(name="acronym", type=StringType)
Event_name: Property = Property(name="name", type=StringType)
Event_edition: Property = Property(name="edition", type=IntegerType)
Event_attribute: Property = Property(name="attribute", type=StringType)
Event.attributes={Event_acronym, Event_edition, Event_attribute, Event_name, Event_id}

# Serie class attributes and methods
Serie_Events: Property = Property(name="Events", type=Event)
Serie.attributes={Serie_Events}

# Session class attributes and methods
Session_id: Property = Property(name="id", type=IntegerType)
Session_start: Property = Property(name="start", type=StringType)
Session_end: Property = Property(name="end", type=StringType)
Session_type: Property = Property(name="type", type=SessionType)
Session_name: Property = Property(name="name", type=StringType)
Session_room: Property = Property(name="room", type=Room)
Session_Events: Property = Property(name="Events", type=Event)
Session.attributes={Session_Events, Session_room, Session_start, Session_name, Session_type, Session_id, Session_end}

# SessionType class attributes and methods
SessionType_id: Property = Property(name="id", type=IntegerType)
SessionType_name: Property = Property(name="name", type=StringType)
SessionType_color: Property = Property(name="color", type=StringType)
SessionType.attributes={SessionType_color, SessionType_name, SessionType_id}

# Room class attributes and methods
Room_id: Property = Property(name="id", type=IntegerType)
Room_name: Property = Property(name="name", type=StringType)
Room.attributes={Room_name, Room_id}

# Domain Model
domain_model = DomainModel(
    name="_YXDscBKNEemZXPSISqszLw",
    types={Event, Serie, Session, SessionType, Room, Enumeration_},
    associations={},
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