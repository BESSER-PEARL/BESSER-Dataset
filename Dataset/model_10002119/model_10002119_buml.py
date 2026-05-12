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
Chef = Class(name="Chef")
Waiter = Class(name="Waiter")
Customer = Class(name="Customer")
Class_ = Class(name="Class")
Manager = Class(name="Manager")
Actor_Actor = Class(name="Actor_Actor")
Actor2_Actor = Class(name="Actor2_Actor")

# Chef class attributes and methods
Chef_Name: Property = Property(name="Name", type=StringType)
Chef_Address: Property = Property(name="Address", type=StringType)
Chef_Contact: Property = Property(name="Contact", type=IntegerType)
Chef_ID: Property = Property(name="ID", type=IntegerType)
Chef_Domain: Property = Property(name="Domain", type=StringType)
Chef_PersonalInformation: Property = Property(name="PersonalInformation", type=StringType)
Chef.attributes={Chef_Domain, Chef_ID, Chef_Address, Chef_PersonalInformation, Chef_Contact, Chef_Name}

# Waiter class attributes and methods
Waiter_Name: Property = Property(name="Name", type=StringType)
Waiter_ID: Property = Property(name="ID", type=StringType)
Waiter_Address: Property = Property(name="Address", type=StringType)
Waiter_Contact: Property = Property(name="Contact", type=IntegerType)
Waiter_Personal_Information: Property = Property(name="Personal_Information", type=StringType)
Waiter.attributes={Waiter_ID, Waiter_Name, Waiter_Contact, Waiter_Personal_Information, Waiter_Address}

# Customer class attributes and methods
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Contact_Number: Property = Property(name="Contact_Number", type=IntegerType)
Customer_Dishes_Ordered: Property = Property(name="Dishes_Ordered", type=StringType)
Customer_Reservation: Property = Property(name="Reservation", type=BooleanType)
Customer_date: Property = Property(name="date", type=StringType)
Customer_reservedTables: Property = Property(name="reservedTables", type=StringType)
Customer.attributes={Customer_Contact_Number, Customer_reservedTables, Customer_Name, Customer_Reservation, Customer_Dishes_Ordered, Customer_date}

# Class class attributes and methods

# Manager class attributes and methods
Manager_Name: Property = Property(name="Name", type=StringType)
Manager_Address: Property = Property(name="Address", type=StringType)
Manager_ID: Property = Property(name="ID", type=IntegerType)
Manager_Contact: Property = Property(name="Contact", type=IntegerType)
Manager_Personalnformation: Property = Property(name="Personalnformation", type=StringType)
Manager.attributes={Manager_Personalnformation, Manager_Address, Manager_ID, Manager_Name, Manager_Contact}

# Actor_Actor class attributes and methods

# Actor2_Actor class attributes and methods

# Relationships
Waiter_Manager: BinaryAssociation = BinaryAssociation(
    name="Waiter_Manager",
    ends={
        Property(name="manager0", type=Manager, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter1", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Chef: BinaryAssociation = BinaryAssociation(
    name="Waiter_Chef",
    ends={
        Property(name="chef2", type=Chef, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter3", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_Customer: BinaryAssociation = BinaryAssociation(
    name="Waiter_Customer",
    ends={
        Property(name="customer4", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter5", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Manager: BinaryAssociation = BinaryAssociation(
    name="Customer_Manager",
    ends={
        Property(name="manager6", type=Manager, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_pkJqYPV1EemTHo7LQdQL6Q",
    types={Chef, Waiter, Customer, Class_, Manager, Actor_Actor, Actor2_Actor},
    associations={Waiter_Manager, Waiter_Chef, Waiter_Customer, Customer_Manager},
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