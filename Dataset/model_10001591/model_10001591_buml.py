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
Guest = Class(name="Guest")
Receptionist = Class(name="Receptionist")
Manager = Class(name="Manager")
Room = Class(name="Room")
Bill = Class(name="Bill")
Inventory = Class(name="Inventory")
Database = Class(name="Database")

# Guest class attributes and methods
Guest_name: Property = Property(name="name", type=StringType)
Guest_id: Property = Property(name="id", type=IntegerType)
Guest_phoneNo: Property = Property(name="phoneNo", type=IntegerType)
Guest_Address: Property = Property(name="Address", type=StringType)
Guest_Room: Property = Property(name="Room", type=IntegerType)
Guest_credit_card: Property = Property(name="credit_card", type=IntegerType)
Guest.attributes={Guest_id, Guest_phoneNo, Guest_Room, Guest_name, Guest_credit_card, Guest_Address}

# Receptionist class attributes and methods
Receptionist_Id: Property = Property(name="Id", type=IntegerType)
Receptionist_name: Property = Property(name="name", type=StringType)
Receptionist.attributes={Receptionist_Id, Receptionist_name}

# Manager class attributes and methods
Manager_id: Property = Property(name="id", type=IntegerType)
Manager_name: Property = Property(name="name", type=StringType)
Manager.attributes={Manager_id, Manager_name}

# Room class attributes and methods
Room_roomNo: Property = Property(name="roomNo", type=IntegerType)
Room_typeOfRoom: Property = Property(name="typeOfRoom", type=StringType)
Room_RatesofRoom: Property = Property(name="RatesofRoom", type=IntegerType)
Room.attributes={Room_roomNo, Room_RatesofRoom, Room_typeOfRoom}

# Bill class attributes and methods
Bill_bill_No: Property = Property(name="bill_No", type=IntegerType)
Bill_GuestName: Property = Property(name="GuestName", type=StringType)
Bill.attributes={Bill_GuestName, Bill_bill_No}

# Inventory class attributes and methods
Inventory_type: Property = Property(name="type", type=StringType)
Inventory_Status: Property = Property(name="Status", type=StringType)
Inventory.attributes={Inventory_Status, Inventory_type}

# Database class attributes and methods
Database_service: Property = Property(name="service", type=StringType)
Database_income: Property = Property(name="income", type=IntegerType)
Database_Details: Property = Property(name="Details", type=StringType)
Database.attributes={Database_service, Database_income, Database_Details}

# Relationships
Guest_Room: BinaryAssociation = BinaryAssociation(
    name="Guest_Room",
    ends={
        Property(name="room0", type=Room, multiplicity=Multiplicity(1, 1)),
        Property(name="guest1", type=Guest, multiplicity=Multiplicity(1, 1))
    }
)
Guest_Bill: BinaryAssociation = BinaryAssociation(
    name="Guest_Bill",
    ends={
        Property(name="bill2", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="guest3", type=Guest, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_Room: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Room",
    ends={
        Property(name="room4", type=Room, multiplicity=Multiplicity(1, 9999)),
        Property(name="receptionist5", type=Receptionist, multiplicity=Multiplicity(1, 9999))
    }
)
Receptionist_Bill: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Bill",
    ends={
        Property(name="bill6", type=Bill, multiplicity=Multiplicity(1, 9999)),
        Property(name="receptionist7", type=Receptionist, multiplicity=Multiplicity(1, 9999))
    }
)
Receptionist_Manager: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Manager",
    ends={
        Property(name="manager8", type=Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="receptionist9", type=Receptionist, multiplicity=Multiplicity(1, 9999))
    }
)
Inventory_Manager: BinaryAssociation = BinaryAssociation(
    name="Inventory_Manager",
    ends={
        Property(name="manager10", type=Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="inventory11", type=Inventory, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_Database: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Database",
    ends={
        Property(name="database12", type=Database, multiplicity=Multiplicity(1, 1)),
        Property(name="receptionist13", type=Receptionist, multiplicity=Multiplicity(1, 9999))
    }
)
Manager_Database: BinaryAssociation = BinaryAssociation(
    name="Manager_Database",
    ends={
        Property(name="database14", type=Database, multiplicity=Multiplicity(1, 1)),
        Property(name="manager15", type=Manager, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_Hs0jELGlEee6S77dw3LIvQ",
    types={Guest, Receptionist, Manager, Room, Bill, Inventory, Database},
    associations={Guest_Room, Guest_Bill, Receptionist_Room, Receptionist_Bill, Receptionist_Manager, Inventory_Manager, Receptionist_Database, Manager_Database},
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