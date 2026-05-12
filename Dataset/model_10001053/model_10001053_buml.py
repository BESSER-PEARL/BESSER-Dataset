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
Customer = Class(name="Customer")
Hotel = Class(name="Hotel")
Room = Class(name="Room")
System = Class(name="System")
Normal_class = Class(name="Normal_class")
Business_class = Class(name="Business_class")
Premium_class = Class(name="Premium_class")

# Customer class attributes and methods

# Hotel class attributes and methods

# Room class attributes and methods

# System class attributes and methods

# Normal_class class attributes and methods

# Business_class class attributes and methods

# Premium_class class attributes and methods

# Relationships
Hotel_Room: BinaryAssociation = BinaryAssociation(
    name="Hotel_Room",
    ends={
        Property(name="Have0", type=Room, multiplicity=Multiplicity(1, 9999)),
        Property(name="Hotel_Room_11", type=Hotel, multiplicity=Multiplicity(1, 1))
    }
)
Service_Hotel: BinaryAssociation = BinaryAssociation(
    name="Service_Hotel",
    ends={
        Property(name="Give_Discount2", type=Hotel, multiplicity=Multiplicity(1, 1)),
        Property(name="Service_Hotel_13", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Room: BinaryAssociation = BinaryAssociation(
    name="Customer_Room",
    ends={
        Property(name="Can_Book4", type=Room, multiplicity=Multiplicity(1, 9999)),
        Property(name="Customer_Room_15", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Room2: BinaryAssociation = BinaryAssociation(
    name="Customer_Room2",
    ends={
        Property(name="Customer_Room2_06", type=Room, multiplicity=Multiplicity(1, 1)),
        Property(name="Booked_By7", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
System_Customer: BinaryAssociation = BinaryAssociation(
    name="System_Customer",
    ends={
        Property(name="Registered8", type=Customer, multiplicity=Multiplicity(1, 9999)),
        Property(name="System_Customer_19", type=System, multiplicity=Multiplicity(1, 1))
    }
)
System_Hotel: BinaryAssociation = BinaryAssociation(
    name="System_Hotel",
    ends={
        Property(name="System_Hotel_010", type=Hotel, multiplicity=Multiplicity(1, 9999)),
        Property(name="Have11", type=System, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_8084b94f_e874_43f9_b5cd_f05720781d69",
    types={Customer, Hotel, Room, System, Normal_class, Business_class, Premium_class},
    associations={Hotel_Room, Service_Hotel, Customer_Room, Customer_Room2, System_Customer, System_Hotel},
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