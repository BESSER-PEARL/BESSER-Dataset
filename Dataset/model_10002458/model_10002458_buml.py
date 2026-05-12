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
Speakers = Class(name="Speakers")
MicroPhone = Class(name="MicroPhone")
Heater = Class(name="Heater")
TV = Class(name="TV")
HomeTheatre = Class(name="HomeTheatre")
Entertainment = Class(name="Entertainment")
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

# Speakers class attributes and methods
Speakers_SpeakerID: Property = Property(name="SpeakerID", type=IntegerType)
Speakers.attributes={Speakers_SpeakerID}

# MicroPhone class attributes and methods
MicroPhone_MicID: Property = Property(name="MicID", type=StringType)
MicroPhone.attributes={MicroPhone_MicID}

# Heater class attributes and methods
Heater_Status: Property = Property(name="Status", type=BooleanType)
Heater.attributes={Heater_Status}

# TV class attributes and methods
TV_TVID: Property = Property(name="TVID", type=IntegerType)
TV.attributes={TV_TVID}

# HomeTheatre class attributes and methods
HomeTheatre_HTID: Property = Property(name="HTID", type=StringType)
HomeTheatre.attributes={HomeTheatre_HTID}

# Entertainment class attributes and methods
Entertainment_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
Entertainment.attributes={Entertainment_DeviceID}

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
HomeTheatre_TV: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_TV",
    ends={
        Property(name="tV2", type=TV, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre3", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Speakers: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Speakers",
    ends={
        Property(name="speakers4", type=Speakers, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre5", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system6", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone7", type=MicroPhone, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert8", type=Ingredient_Box, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System9", type=Cooking_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system10", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor11", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system12", type=System, multiplicity=Multiplicity(0, 9999)),
        Property(name="homeTheatre13", type=HomeTheatre, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="Home_Security_System_System_014", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="Cooking_System15", type=Cooking_System, multiplicity=Multiplicity(1, 1))
    }
)
TV_Entertainment: BinaryAssociation = BinaryAssociation(
    name="TV_Entertainment",
    ends={
        Property(name="entertainment16", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="tV17", type=TV, multiplicity=Multiplicity(1, 9999))
    }
)
Speakers_Entertainment: BinaryAssociation = BinaryAssociation(
    name="Speakers_Entertainment",
    ends={
        Property(name="entertainment18", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="speakers19", type=Speakers, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Entertainment: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Entertainment",
    ends={
        Property(name="entertainment20", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre21", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="b557e9e3_85d7_4bb3_aef8_f61ba6e6ffb8",
    types={System, Sensor, Temperature_Sensor, Humidity_Sensor, Cooking_System, Ingredient_Box, Interior_Container, Speakers, MicroPhone, Heater, TV, HomeTheatre, Entertainment, SteamGenerator},
    associations={Sensor_Door, HomeTheatre_TV, HomeTheatre_Speakers, MicroPhone_System, Home_Security_System_Alert, Sensor_System, HomeTheatre_System, Home_Security_System_System, TV_Entertainment, Speakers_Entertainment, HomeTheatre_Entertainment},
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