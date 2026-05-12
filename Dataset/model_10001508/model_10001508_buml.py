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
String: Enumeration = Enumeration(
    name="String",
    literals={
            
    }
)

# Classes
Event = Class(name="Event")
Ticket = Class(name="Ticket")
User = Class(name="User")
Date = Class(name="Date")
User__4 = Class(name="User__4")
Event__ = Class(name="Event__")

# Event class attributes and methods
Event_type: Property = Property(name="type", type=StringType)
Event_time: Property = Property(name="time", type=StringType)
Event_participantCount: Property = Property(name="participantCount", type=IntegerType)
Event_placeName: Property = Property(name="placeName", type=StringType)
Event_image: Property = Property(name="image", type=StringType)
Event_id: Property = Property(name="id", type=String)
Event_participants: Property = Property(name="participants", type=StringType)
Event_location: Property = Property(name="location", type=StringType)
Event_organizator: Property = Property(name="organizator", type=User)
Event_discussion: Property = Property(name="discussion", type=StringType)
Event_about: Property = Property(name="about", type=StringType)
Event.attributes={Event_type, Event_participantCount, Event_organizator, Event_about, Event_image, Event_id, Event_participants, Event_location, Event_placeName, Event_time, Event_discussion}

# Ticket class attributes and methods
Ticket_id: Property = Property(name="id", type=StringType)
Ticket_event: Property = Property(name="event", type=Event)
Ticket.attributes={Ticket_id, Ticket_event}

# User class attributes and methods
User_tickets: Property = Property(name="tickets", type=StringType)
User_id: Property = Property(name="id", type=StringType)
User_name: Property = Property(name="name", type=StringType)
User_birthdate: Property = Property(name="birthdate", type=Date)
User_gender: Property = Property(name="gender", type=StringType)
User_userImage: Property = Property(name="userImage", type=StringType)
User_friends: Property = Property(name="friends", type=StringType)
User_events: Property = Property(name="events", type=Event__)
User_password: Property = Property(name="password", type=StringType)
User_company: Property = Property(name="company", type=StringType)
User_selfDescription: Property = Property(name="selfDescription", type=StringType)
User.attributes={User_company, User_events, User_selfDescription, User_userImage, User_tickets, User_password, User_id, User_friends, User_gender, User_name, User_birthdate}

# Date class attributes and methods

# User__4 class attributes and methods

# Event__ class attributes and methods

# Relationships
Ticket_Event: BinaryAssociation = BinaryAssociation(
    name="Ticket_Event",
    ends={
        Property(name="event20", type=Event, multiplicity=Multiplicity(1, 1)),
        Property(name="ticket1", type=Ticket, multiplicity=Multiplicity(1, 9999))
    }
)
Ticket_User: BinaryAssociation = BinaryAssociation(
    name="Ticket_User",
    ends={
        Property(name="user2", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="ticket3", type=Ticket, multiplicity=Multiplicity(1, 9999))
    }
)
Event_User: BinaryAssociation = BinaryAssociation(
    name="Event_User",
    ends={
        Property(name="user4", type=User, multiplicity=Multiplicity(1, 9999)),
        Property(name="event5", type=Event, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_BnTWwMJCEeeEXb8Dudo6PQ",
    types={Event, Ticket, User, Date, User__4, Event__, String},
    associations={Ticket_Event, Ticket_User, Event_User},
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