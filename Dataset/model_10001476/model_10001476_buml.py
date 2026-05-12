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
User = Class(name="User")
Client = Class(name="Client")
Eventhead = Class(name="Eventhead")
Volunteer = Class(name="Volunteer")
Payment = Class(name="Payment")
Event = Class(name="Event")
Refreshment = Class(name="Refreshment")
Weddings = Class(name="Weddings")
Birthday_Parties = Class(name="Birthday_Parties")
Commercial_Events = Class(name="Commercial_Events")
Admin = Class(name="Admin")

# User class attributes and methods
User_username: Property = Property(name="username", type=StringType)
User_fname: Property = Property(name="fname", type=StringType)
User_lname: Property = Property(name="lname", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User.attributes={User_password, User_username, User_lname, User_fname}

# Client class attributes and methods
Client_id: Property = Property(name="id", type=IntegerType)
Client.attributes={Client_id}

# Eventhead class attributes and methods
Eventhead_id: Property = Property(name="id", type=IntegerType)
Eventhead.attributes={Eventhead_id}

# Volunteer class attributes and methods
Volunteer_id: Property = Property(name="id", type=IntegerType)
Volunteer.attributes={Volunteer_id}

# Payment class attributes and methods
Payment_amout: Property = Property(name="amout", type=IntegerType)
Payment_paytype: Property = Property(name="paytype", type=StringType)
Payment_status: Property = Property(name="status", type=StringType)
Payment.attributes={Payment_paytype, Payment_status, Payment_amout}

# Event class attributes and methods
Event_eventid: Property = Property(name="eventid", type=IntegerType)
Event_eventname: Property = Property(name="eventname", type=StringType)
Event_date: Property = Property(name="date", type=IntegerType)
Event_eventhead: Property = Property(name="eventhead", type=Eventhead)
Event_amount: Property = Property(name="amount", type=IntegerType)
Event_eventype: Property = Property(name="eventype", type=StringType)
Event.attributes={Event_eventype, Event_eventname, Event_eventhead, Event_date, Event_amount, Event_eventid}

# Refreshment class attributes and methods

# Weddings class attributes and methods

# Birthday_Parties class attributes and methods

# Commercial_Events class attributes and methods

# Admin class attributes and methods
Admin_username: Property = Property(name="username", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_password, Admin_username}

# Relationships
client_payment: BinaryAssociation = BinaryAssociation(
    name="client_payment",
    ends={
        Property(name="payment20", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="client1", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
takes_part: BinaryAssociation = BinaryAssociation(
    name="takes_part",
    ends={
        Property(name="event2", type=Event, multiplicity=Multiplicity(0, 1)),
        Property(name="client3", type=Client, multiplicity=Multiplicity(0, 1))
    }
)
volunteer_event: BinaryAssociation = BinaryAssociation(
    name="volunteer_event",
    ends={
        Property(name="event4", type=Event, multiplicity=Multiplicity(0, 1)),
        Property(name="volunteer5", type=Volunteer, multiplicity=Multiplicity(0, 1))
    }
)
event_eventhead: BinaryAssociation = BinaryAssociation(
    name="event_eventhead",
    ends={
        Property(name="eventhead26", type=Eventhead, multiplicity=Multiplicity(0, 1)),
        Property(name="event7", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
Event_Refreshment: BinaryAssociation = BinaryAssociation(
    name="Event_Refreshment",
    ends={
        Property(name="refreshment8", type=Refreshment, multiplicity=Multiplicity(0, 1)),
        Property(name="event9", type=Event, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Event: BinaryAssociation = BinaryAssociation(
    name="Admin_Event",
    ends={
        Property(name="event10", type=Event, multiplicity=Multiplicity(0, 1)),
        Property(name="admin11", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9Wg9MNh2EeiA5M_nJapEiA",
    types={User, Client, Eventhead, Volunteer, Payment, Event, Refreshment, Weddings, Birthday_Parties, Commercial_Events, Admin},
    associations={client_payment, takes_part, volunteer_event, event_eventhead, Event_Refreshment, Admin_Event},
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