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
System = Class(name="System")
Sensor = Class(name="Sensor")
Temperature_Sensor = Class(name="Temperature_Sensor")
Humidity_Sensor = Class(name="Humidity_Sensor")
Cooking_System = Class(name="Cooking_System")
Ingredient_Box = Class(name="Ingredient_Box")
Interior_Container = Class(name="Interior_Container")
PhoneApplication = Class(name="PhoneApplication")
Heater = Class(name="Heater")
Display = Class(name="Display")
SteamGenerator = Class(name="SteamGenerator")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Update, System_Status}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorID, Sensor_SensorType}

# Temperature_Sensor class attributes and methods
Temperature_Sensor_CurrentValue: Property = Property(name="CurrentValue", type=FloatType)
Temperature_Sensor.attributes={Temperature_Sensor_CurrentValue}

# Humidity_Sensor class attributes and methods
Humidity_Sensor_CurrentValue: Property = Property(name="CurrentValue", type=FloatType)
Humidity_Sensor.attributes={Humidity_Sensor_CurrentValue}

# Cooking_System class attributes and methods

# Ingredient_Box class attributes and methods
Ingredient_Box_BoxID: Property = Property(name="BoxID", type=IntegerType)
Ingredient_Box_WeightValue: Property = Property(name="WeightValue", type=FloatType)
Ingredient_Box.attributes={Ingredient_Box_BoxID, Ingredient_Box_WeightValue}

# Interior_Container class attributes and methods
Interior_Container_WorkMode: Property = Property(name="WorkMode", type=IntegerType)
Interior_Container.attributes={Interior_Container_WorkMode}

# PhoneApplication class attributes and methods

# Heater class attributes and methods
Heater_Status: Property = Property(name="Status", type=BooleanType)
Heater.attributes={Heater_Status}

# Display class attributes and methods

# SteamGenerator class attributes and methods
SteamGenerator_Status: Property = Property(name="Status", type=BooleanType)
SteamGenerator.attributes={SteamGenerator_Status}

# Relationships
Sensor_Door: BinaryAssociation = BinaryAssociation(
    name="Sensor_Door",
    ends={
        Property(name="door0", type=Interior_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor1", type=Sensor, multiplicity=Multiplicity(1, 1))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system2", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone3", type=PhoneApplication, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert4", type=Ingredient_Box, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System5", type=Cooking_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system6", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor7", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system8", type=System, multiplicity=Multiplicity(0, 9999)),
        Property(name="homeTheatre9", type=Display, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="Home_Security_System_System_010", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="Cooking_System11", type=Cooking_System, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_20b48720_2fca_45ed_9c22_954fb8270895",
    types={System, Sensor, Temperature_Sensor, Humidity_Sensor, Cooking_System, Ingredient_Box, Interior_Container, PhoneApplication, Heater, Display, SteamGenerator},
    associations={Sensor_Door, MicroPhone_System, Home_Security_System_Alert, Sensor_System, HomeTheatre_System, Home_Security_System_System},
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