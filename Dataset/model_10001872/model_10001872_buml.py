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
Receptionist = Class(name="Receptionist")
Inventory = Class(name="Inventory")
Guest = Class(name="Guest")
Chef = Class(name="Chef")
Rooms = Class(name="Rooms")
Bill = Class(name="Bill")
Housekeeping = Class(name="Housekeeping")
Food = Class(name="Food")

# Manager class attributes and methods
Manager_managerID: Property = Property(name="managerID", type=IntegerType)
Manager_name: Property = Property(name="name", type=StringType)
Manager_phoneNo: Property = Property(name="phoneNo", type=IntegerType)
Manager_branch: Property = Property(name="branch", type=StringType)
Manager.attributes={Manager_branch, Manager_name, Manager_managerID, Manager_phoneNo}

# Receptionist class attributes and methods
Receptionist_rID: Property = Property(name="rID", type=IntegerType)
Receptionist_name: Property = Property(name="name", type=StringType)
Receptionist_phoneNo: Property = Property(name="phoneNo", type=IntegerType)
Receptionist_branch: Property = Property(name="branch", type=StringType)
Receptionist.attributes={Receptionist_name, Receptionist_branch, Receptionist_phoneNo, Receptionist_rID}

# Inventory class attributes and methods
Inventory_type: Property = Property(name="type", type=StringType)
Inventory_status: Property = Property(name="status", type=StringType)
Inventory.attributes={Inventory_type, Inventory_status}

# Guest class attributes and methods
Guest_name: Property = Property(name="name", type=StringType)
Guest_guestID: Property = Property(name="guestID", type=IntegerType)
Guest_address: Property = Property(name="address", type=StringType)
Guest_phoneNo: Property = Property(name="phoneNo", type=IntegerType)
Guest_roomNo: Property = Property(name="roomNo", type=IntegerType)
Guest.attributes={Guest_guestID, Guest_address, Guest_phoneNo, Guest_roomNo, Guest_name}

# Chef class attributes and methods
Chef_chefID: Property = Property(name="chefID", type=IntegerType)
Chef_name: Property = Property(name="name", type=StringType)
Chef_branch: Property = Property(name="branch", type=StringType)
Chef.attributes={Chef_name, Chef_chefID, Chef_branch}

# Rooms class attributes and methods
Rooms_roomNo: Property = Property(name="roomNo", type=IntegerType)
Rooms_type: Property = Property(name="type", type=StringType)
Rooms.attributes={Rooms_type, Rooms_roomNo}

# Bill class attributes and methods
Bill_billNo: Property = Property(name="billNo", type=IntegerType)
Bill_guestID: Property = Property(name="guestID", type=IntegerType)
Bill.attributes={Bill_guestID, Bill_billNo}

# Housekeeping class attributes and methods
Housekeeping_name: Property = Property(name="name", type=StringType)
Housekeeping_hkID: Property = Property(name="hkID", type=IntegerType)
Housekeeping_branch: Property = Property(name="branch", type=StringType)
Housekeeping.attributes={Housekeeping_branch, Housekeeping_name, Housekeeping_hkID}

# Food class attributes and methods
Food_foodID: Property = Property(name="foodID", type=IntegerType)
Food_name: Property = Property(name="name", type=StringType)
Food.attributes={Food_name, Food_foodID}

# Relationships
Chef_Food: BinaryAssociation = BinaryAssociation(
    name="Chef_Food",
    ends={
        Property(name="chef5", type=Chef, multiplicity=Multiplicity(1, 9999)),
        Property(name="food4", type=Food, multiplicity=Multiplicity(1, 9999))
    }
)
Food_Guest: BinaryAssociation = BinaryAssociation(
    name="Food_Guest",
    ends={
        Property(name="guest6", type=Guest, multiplicity=Multiplicity(1, 9999)),
        Property(name="food7", type=Food, multiplicity=Multiplicity(1, 9999))
    }
)
Guest_Rooms: BinaryAssociation = BinaryAssociation(
    name="Guest_Rooms",
    ends={
        Property(name="rooms8", type=Rooms, multiplicity=Multiplicity(1, 9999)),
        Property(name="guest9", type=Guest, multiplicity=Multiplicity(1, 1))
    }
)
Guest_Bill: BinaryAssociation = BinaryAssociation(
    name="Guest_Bill",
    ends={
        Property(name="bill10", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="guest11", type=Guest, multiplicity=Multiplicity(1, 1))
    }
)
Rooms_Housekeeping: BinaryAssociation = BinaryAssociation(
    name="Rooms_Housekeeping",
    ends={
        Property(name="housekeeping12", type=Housekeeping, multiplicity=Multiplicity(1, 1)),
        Property(name="rooms13", type=Rooms, multiplicity=Multiplicity(1, 1))
    }
)
Receptionist_Bill: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Bill",
    ends={
        Property(name="bill14", type=Bill, multiplicity=Multiplicity(1, 1)),
        Property(name="receptionist15", type=Receptionist, multiplicity=Multiplicity(1, 9999))
    }
)
Rooms_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Rooms_Receptionist",
    ends={
        Property(name="receptionist16", type=Receptionist, multiplicity=Multiplicity(1, 9999)),
        Property(name="rooms17", type=Rooms, multiplicity=Multiplicity(1, 9999))
    }
)
Manager_Inventory: BinaryAssociation = BinaryAssociation(
    name="Manager_Inventory",
    ends={
        Property(name="inventory0", type=Inventory, multiplicity=Multiplicity(1, 9999)),
        Property(name="manager1", type=Manager, multiplicity=Multiplicity(1, 1))
    }
)
Manager_Guest: BinaryAssociation = BinaryAssociation(
    name="Manager_Guest",
    ends={
        Property(name="guest2", type=Guest, multiplicity=Multiplicity(1, 9999)),
        Property(name="manager3", type=Manager, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_aqB58LFjEee6S77dw3LIvQ",
    types={Manager, Receptionist, Inventory, Guest, Chef, Rooms, Bill, Housekeeping, Food},
    associations={Chef_Food, Food_Guest, Guest_Rooms, Guest_Bill, Rooms_Housekeeping, Receptionist_Bill, Rooms_Receptionist, Manager_Inventory, Manager_Guest},
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