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
Manager = Class(name="Manager")
Hotels = Class(name="Hotels")
Rooms = Class(name="Rooms")
Guest = Class(name="Guest")
City = Class(name="City")
Payment = Class(name="Payment")
User = Class(name="User")

# Manager class attributes and methods
Manager_Name: Property = Property(name="Name", type=StringType)
Manager_ID: Property = Property(name="ID", type=IntegerType)
Manager_Phn_no_: Property = Property(name="Phn_no_", type=Manager)
Manager_Address: Property = Property(name="Address", type=StringType)
Manager.attributes={Manager_Address, Manager_Phn_no_, Manager_Name, Manager_ID}

# Hotels class attributes and methods
Hotels_id: Property = Property(name="id", type=IntegerType)
Hotels_name: Property = Property(name="name", type=IntegerType)
Hotels_location: Property = Property(name="location", type=IntegerType)
Hotels.attributes={Hotels_id, Hotels_location, Hotels_name}

# Rooms class attributes and methods
Rooms_id: Property = Property(name="id", type=IntegerType)
Rooms_name: Property = Property(name="name", type=StringType)
Rooms_room_description: Property = Property(name="room_description", type=StringType)
Rooms_price: Property = Property(name="price", type=IntegerType)
Rooms.attributes={Rooms_price, Rooms_name, Rooms_id, Rooms_room_description}

# Guest class attributes and methods
Guest_Nmae: Property = Property(name="Nmae", type=StringType)
Guest_id: Property = Property(name="id", type=IntegerType)
Guest_Phone_no_: Property = Property(name="Phone_no_", type=IntegerType)
Guest_address: Property = Property(name="address", type=StringType)
Guest.attributes={Guest_id, Guest_Nmae, Guest_address, Guest_Phone_no_}

# City class attributes and methods
City_city: Property = Property(name="city", type=StringType)
City_id: Property = Property(name="id", type=IntegerType)
City.attributes={City_id, City_city}

# Payment class attributes and methods
Payment_amount: Property = Property(name="amount", type=IntegerType)
Payment_card_no: Property = Property(name="card_no", type=IntegerType)
Payment_cvv: Property = Property(name="cvv", type=IntegerType)
Payment_card_type: Property = Property(name="card_type", type=StringType)
Payment_password: Property = Property(name="password", type=IntegerType)
Payment.attributes={Payment_card_type, Payment_card_no, Payment_amount, Payment_password, Payment_cvv}

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User_phn_no: Property = Property(name="phn_no", type=IntegerType)
User_id: Property = Property(name="id", type=IntegerType)
User_mail_id: Property = Property(name="mail_id", type=StringType)
User_address: Property = Property(name="address", type=StringType)
User_password: Property = Property(name="password", type=IntegerType)
User.attributes={User_address, User_Name, User_id, User_phn_no, User_mail_id, User_password}

# Relationships
City_Hotels: BinaryAssociation = BinaryAssociation(
    name="City_Hotels",
    ends={
        Property(name="hotels0", type=Hotels, multiplicity=Multiplicity(0, 1)),
        Property(name="city1", type=City, multiplicity=Multiplicity(1, 1))
    }
)
Hotels_Rooms: BinaryAssociation = BinaryAssociation(
    name="Hotels_Rooms",
    ends={
        Property(name="rooms2", type=Rooms, multiplicity=Multiplicity(0, 1)),
        Property(name="hotels3", type=Hotels, multiplicity=Multiplicity(0, 1))
    }
)
Rooms_Guest: BinaryAssociation = BinaryAssociation(
    name="Rooms_Guest",
    ends={
        Property(name="guest4", type=Guest, multiplicity=Multiplicity(0, 1)),
        Property(name="rooms5", type=Rooms, multiplicity=Multiplicity(0, 1))
    }
)
Guest_Payment: BinaryAssociation = BinaryAssociation(
    name="Guest_Payment",
    ends={
        Property(name="payment6", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="guest7", type=Guest, multiplicity=Multiplicity(0, 1))
    }
)
Hotels_Guest: BinaryAssociation = BinaryAssociation(
    name="Hotels_Guest",
    ends={
        Property(name="guest8", type=Guest, multiplicity=Multiplicity(0, 1)),
        Property(name="hotels9", type=Hotels, multiplicity=Multiplicity(0, 1))
    }
)
User_Guest: BinaryAssociation = BinaryAssociation(
    name="User_Guest",
    ends={
        Property(name="guest10", type=Guest, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Payment: BinaryAssociation = BinaryAssociation(
    name="Manager_Payment",
    ends={
        Property(name="payment12", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="manager13", type=Manager, multiplicity=Multiplicity(0, 1))
    }
)
Manager_Guest: BinaryAssociation = BinaryAssociation(
    name="Manager_Guest",
    ends={
        Property(name="guest14", type=Guest, multiplicity=Multiplicity(0, 1)),
        Property(name="manager15", type=Manager, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_jp4NENBgEeeLcIicqHdTUQ",
    types={Manager, Hotels, Rooms, Guest, City, Payment, User},
    associations={City_Hotels, Hotels_Rooms, Rooms_Guest, Guest_Payment, Hotels_Guest, User_Guest, Manager_Payment, Manager_Guest},
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