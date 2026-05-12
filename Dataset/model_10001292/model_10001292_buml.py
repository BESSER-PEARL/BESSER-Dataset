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
Parking_Space_Type: Enumeration = Enumeration(
    name="Parking_Space_Type",
    literals={
            
    }
)

Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

Enumeration2: Enumeration = Enumeration(
    name="Enumeration2",
    literals={
            
    }
)

Structure_Type: Enumeration = Enumeration(
    name="Structure_Type",
    literals={
            
    }
)

# Classes
Boolean_external = Class(name="Boolean_external")
Parking_Structure = Class(name="Parking_Structure")
Parking_Space = Class(name="Parking_Space", is_abstract=True)
Vehicle_Interface = Class(name="Vehicle_Interface")
Car = Class(name="Car")
Motorbike = Class(name="Motorbike")
Electric = Class(name="Electric")
Convertible = Class(name="Convertible")
Parking_Level = Class(name="Parking_Level")
Class_ = Class(name="Class")
Regular_Space = Class(name="Regular_Space")

# Boolean_external class attributes and methods

# Parking_Structure class attributes and methods
Parking_Structure_City: Property = Property(name="City", type=StringType)
Parking_Structure_Address: Property = Property(name="Address", type=StringType)
Parking_Structure_Type: Property = Property(name="Type", type=Structure_Type)
Parking_Structure.attributes={Parking_Structure_Address, Parking_Structure_City, Parking_Structure_Type}

# Parking_Space class attributes and methods
Parking_Space_Space_Number: Property = Property(name="Space_Number", type=IntegerType)
Parking_Space_Floor_Number: Property = Property(name="Floor_Number", type=Parking_Level)
Parking_Space_Space_Type: Property = Property(name="Space_Type", type=Parking_Space_Type)
Parking_Space.attributes={Parking_Space_Space_Number, Parking_Space_Space_Type, Parking_Space_Floor_Number}

# Vehicle_Interface class attributes and methods

# Car class attributes and methods

# Motorbike class attributes and methods

# Electric class attributes and methods

# Convertible class attributes and methods

# Parking_Level class attributes and methods
Parking_Level_Fl_Number: Property = Property(name="Fl_Number", type=IntegerType)
Parking_Level.attributes={Parking_Level_Fl_Number}

# Class class attributes and methods

# Regular_Space class attributes and methods

# Relationships
Floor_Parking_Spaces: BinaryAssociation = BinaryAssociation(
    name="Floor_Parking_Spaces",
    ends={
        Property(name="Composed_Of0", type=Boolean_external, multiplicity=Multiplicity(0, 9999)),
        Property(name="floor1", type=Parking_Level, multiplicity=Multiplicity(1, 1))
    }
)
Parking_Space_Vehicle: BinaryAssociation = BinaryAssociation(
    name="Parking_Space_Vehicle",
    ends={
        Property(name="vehicle2", type=Vehicle_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="has3", type=Parking_Space, multiplicity=Multiplicity(1, 1))
    }
)
Parking_Structure_Parking_Level: BinaryAssociation = BinaryAssociation(
    name="Parking_Structure_Parking_Level",
    ends={
        Property(name="parking_Level4", type=Parking_Level, multiplicity=Multiplicity(1, 9999)),
        Property(name="has5", type=Parking_Structure, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_9eeb2491_fdd2_4f87_ad64_35be59fe706a",
    types={Boolean_external, Parking_Structure, Parking_Space, Vehicle_Interface, Car, Motorbike, Electric, Convertible, Parking_Level, Class_, Regular_Space, Parking_Space_Type, Enumeration_, Enumeration2, Structure_Type},
    associations={Floor_Parking_Spaces, Parking_Space_Vehicle, Parking_Structure_Parking_Level},
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