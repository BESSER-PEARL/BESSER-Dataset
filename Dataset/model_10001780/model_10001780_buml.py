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
Ticket = Class(name="Ticket")
System = Class(name="System")
Admin = Class(name="Admin")
Flightlist = Class(name="Flightlist")
Timinglist = Class(name="Timinglist")

# User class attributes and methods
User_username: Property = Property(name="username", type=StringType)
User_password: Property = Property(name="password", type=StringType)
User_gender: Property = Property(name="gender", type=StringType)
User_address: Property = Property(name="address", type=StringType)
User_phoneno: Property = Property(name="phoneno", type=IntegerType)
User.attributes={User_username, User_phoneno, User_gender, User_address, User_password}

# Ticket class attributes and methods
Ticket_ticketid: Property = Property(name="ticketid", type=StringType)
Ticket_flightname: Property = Property(name="flightname", type=StringType)
Ticket_passengername: Property = Property(name="passengername", type=StringType)
Ticket_price: Property = Property(name="price", type=IntegerType)
Ticket_source: Property = Property(name="source", type=StringType)
Ticket_destination: Property = Property(name="destination", type=StringType)
Ticket.attributes={Ticket_passengername, Ticket_flightname, Ticket_ticketid, Ticket_source, Ticket_price, Ticket_destination}

# System class attributes and methods
System_name: Property = Property(name="name", type=StringType)
System_id: Property = Property(name="id", type=StringType)
System_session: Property = Property(name="session", type=StringType)
System.attributes={System_session, System_name, System_id}

# Admin class attributes and methods
Admin_adminname: Property = Property(name="adminname", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin_mobile: Property = Property(name="mobile", type=IntegerType)
Admin_type: Property = Property(name="type", type=StringType)
Admin_gender: Property = Property(name="gender", type=StringType)
Admin.attributes={Admin_gender, Admin_type, Admin_adminname, Admin_password, Admin_mobile}

# Flightlist class attributes and methods
Flightlist_name: Property = Property(name="name", type=StringType)
Flightlist_id: Property = Property(name="id", type=StringType)
Flightlist.attributes={Flightlist_id, Flightlist_name}

# Timinglist class attributes and methods
Timinglist_flightname: Property = Property(name="flightname", type=StringType)
Timinglist_time: Property = Property(name="time", type=StringType)
Timinglist_source: Property = Property(name="source", type=StringType)
Timinglist_destination: Property = Property(name="destination", type=StringType)
Timinglist.attributes={Timinglist_destination, Timinglist_flightname, Timinglist_source, Timinglist_time}

# Relationships
Admin_System: BinaryAssociation = BinaryAssociation(
    name="Admin_System",
    ends={
        Property(name="system4", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="maintains5", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
System_Flightlist: BinaryAssociation = BinaryAssociation(
    name="System_Flightlist",
    ends={
        Property(name="has6", type=Flightlist, multiplicity=Multiplicity(1, 1)),
        Property(name="system7", type=System, multiplicity=Multiplicity(1, 1))
    }
)
System_Timinglist: BinaryAssociation = BinaryAssociation(
    name="System_Timinglist",
    ends={
        Property(name="system8", type=Timinglist, multiplicity=Multiplicity(1, 1)),
        Property(name="has9", type=System, multiplicity=Multiplicity(1, 1))
    }
)
User_Ticket: BinaryAssociation = BinaryAssociation(
    name="User_Ticket",
    ends={
        Property(name="books0", type=Ticket, multiplicity=Multiplicity(1, 9999)),
        Property(name="system1", type=User, multiplicity=Multiplicity(1, 9999))
    }
)
User_System: BinaryAssociation = BinaryAssociation(
    name="User_System",
    ends={
        Property(name="system2", type=System, multiplicity=Multiplicity(0, 1)),
        Property(name="visits3", type=User, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_V2TOsLIzEee7sYPkE4_GPA",
    types={User, Ticket, System, Admin, Flightlist, Timinglist},
    associations={Admin_System, System_Flightlist, System_Timinglist, User_Ticket, User_System},
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