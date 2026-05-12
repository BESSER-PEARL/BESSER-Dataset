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
Book_Room_UseCase = Class(name="Book_Room_UseCase")
Cancel_Reservation_UseCase = Class(name="Cancel_Reservation_UseCase")
Check_In_UseCase = Class(name="Check_In_UseCase")
Check_Out_UseCase = Class(name="Check_Out_UseCase")
Food_Serving_UseCase = Class(name="Food_Serving_UseCase")
Menu_Preparation_UseCase = Class(name="Menu_Preparation_UseCase")
Room_Cleaning_UseCase = Class(name="Room_Cleaning_UseCase")
Hotel_Guest_Actor = Class(name="Hotel_Guest_Actor")
Receptionist_Actor = Class(name="Receptionist_Actor")
Chef_Actor = Class(name="Chef_Actor")
HouseKeeping_Actor = Class(name="HouseKeeping_Actor")
Manager = Class(name="Manager")
Inventory = Class(name="Inventory")
Customer = Class(name="Customer")
Search_Avalibility_UseCase = Class(name="Search_Avalibility_UseCase")

# Book_Room_UseCase class attributes and methods

# Cancel_Reservation_UseCase class attributes and methods

# Check_In_UseCase class attributes and methods

# Check_Out_UseCase class attributes and methods

# Food_Serving_UseCase class attributes and methods

# Menu_Preparation_UseCase class attributes and methods

# Room_Cleaning_UseCase class attributes and methods

# Hotel_Guest_Actor class attributes and methods

# Receptionist_Actor class attributes and methods

# Chef_Actor class attributes and methods

# HouseKeeping_Actor class attributes and methods

# Manager class attributes and methods
Manager_Name: Property = Property(name="Name", type=StringType)
Manager_Id: Property = Property(name="Id", type=IntegerType)
Manager_Phone_No: Property = Property(name="Phone_No", type=IntegerType)
Manager.attributes={Manager_Name, Manager_Phone_No, Manager_Id}

# Inventory class attributes and methods
Inventory_Type: Property = Property(name="Type", type=StringType)
Inventory_Status: Property = Property(name="Status", type=StringType)
Inventory.attributes={Inventory_Status, Inventory_Type}

# Customer class attributes and methods

# Search_Avalibility_UseCase class attributes and methods

# Relationships
Search_Avalibility_Hotel_Guest: BinaryAssociation = BinaryAssociation(
    name="Search_Avalibility_Hotel_Guest",
    ends={
        Property(name="hotel_Guest0", type=Hotel_Guest_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="search_Avalibility1", type=Search_Avalibility_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Book_Room_Hotel_Guest: BinaryAssociation = BinaryAssociation(
    name="Book_Room_Hotel_Guest",
    ends={
        Property(name="hotel_Guest2", type=Hotel_Guest_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="book_Room3", type=Book_Room_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_In_Hotel_Guest: BinaryAssociation = BinaryAssociation(
    name="Check_In_Hotel_Guest",
    ends={
        Property(name="hotel_Guest4", type=Hotel_Guest_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_In5", type=Check_In_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_Out_Hotel_Guest: BinaryAssociation = BinaryAssociation(
    name="Check_Out_Hotel_Guest",
    ends={
        Property(name="hotel_Guest6", type=Hotel_Guest_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_Out7", type=Check_Out_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Food_Serving_Hotel_Guest: BinaryAssociation = BinaryAssociation(
    name="Food_Serving_Hotel_Guest",
    ends={
        Property(name="hotel_Guest8", type=Hotel_Guest_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="food_Serving9", type=Food_Serving_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Room_Cleaning_Hotel_Guest: BinaryAssociation = BinaryAssociation(
    name="Room_Cleaning_Hotel_Guest",
    ends={
        Property(name="hotel_Guest10", type=Hotel_Guest_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="room_Cleaning11", type=Room_Cleaning_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Receptionist_Book_Room: BinaryAssociation = BinaryAssociation(
    name="Receptionist_Book_Room",
    ends={
        Property(name="book_Room12", type=Book_Room_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="receptionist13", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Check_In_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Check_In_Receptionist",
    ends={
        Property(name="receptionist14", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_In15", type=Check_In_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Food_Serving_Chef: BinaryAssociation = BinaryAssociation(
    name="Food_Serving_Chef",
    ends={
        Property(name="chef16", type=Chef_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="food_Serving17", type=Food_Serving_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Menu_Preparation_Chef: BinaryAssociation = BinaryAssociation(
    name="Menu_Preparation_Chef",
    ends={
        Property(name="chef18", type=Chef_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="menu_Preparation19", type=Menu_Preparation_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Room_Cleaning_HouseKeeping: BinaryAssociation = BinaryAssociation(
    name="Room_Cleaning_HouseKeeping",
    ends={
        Property(name="houseKeeping20", type=HouseKeeping_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="room_Cleaning21", type=Room_Cleaning_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Check_Out_Receptionist: BinaryAssociation = BinaryAssociation(
    name="Check_Out_Receptionist",
    ends={
        Property(name="receptionist22", type=Receptionist_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="check_Out23", type=Check_Out_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fd13b14e_e3fa_4ea1_80cc_29451120c400",
    types={Book_Room_UseCase, Cancel_Reservation_UseCase, Check_In_UseCase, Check_Out_UseCase, Food_Serving_UseCase, Menu_Preparation_UseCase, Room_Cleaning_UseCase, Hotel_Guest_Actor, Receptionist_Actor, Chef_Actor, HouseKeeping_Actor, Manager, Inventory, Customer, Search_Avalibility_UseCase},
    associations={Search_Avalibility_Hotel_Guest, Book_Room_Hotel_Guest, Check_In_Hotel_Guest, Check_Out_Hotel_Guest, Food_Serving_Hotel_Guest, Room_Cleaning_Hotel_Guest, Receptionist_Book_Room, Check_In_Receptionist, Food_Serving_Chef, Menu_Preparation_Chef, Room_Cleaning_HouseKeeping, Check_Out_Receptionist},
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