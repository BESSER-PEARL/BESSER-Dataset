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
IoT_based_Smart_Resort_System = Class(name="IoT_based_Smart_Resort_System")
Sensor = Class(name="Sensor")
Motion_Sensor = Class(name="Motion_Sensor")
MoistureSensor = Class(name="MoistureSensor")
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
Door = Class(name="Door")
Fans = Class(name="Fans")
Gardening = Class(name="Gardening")
Light = Class(name="Light")
HomeAppliances = Class(name="HomeAppliances")
User_Home_Owner = Class(name="User_Home_Owner")
Security_Guard_Police = Class(name="Security_Guard_Police")
SolarPanel = Class(name="SolarPanel")

# IoT_based_Smart_Resort_System class attributes and methods
IoT_based_Smart_Resort_System_Status: Property = Property(name="Status", type=BooleanType)
IoT_based_Smart_Resort_System_Update: Property = Property(name="Update", type=FloatType)
IoT_based_Smart_Resort_System.attributes={IoT_based_Smart_Resort_System_Update, IoT_based_Smart_Resort_System_Status}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorType, Sensor_SensorID}

# Motion_Sensor class attributes and methods

# MoistureSensor class attributes and methods

# Home_Security_System class attributes and methods
Home_Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Home_Security_System.attributes={Home_Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Door class attributes and methods
Door_DoorID: Property = Property(name="DoorID", type=IntegerType)
Door.attributes={Door_DoorID}

# Fans class attributes and methods
Fans_FANID: Property = Property(name="FANID", type=IntegerType)
Fans.attributes={Fans_FANID}

# Gardening class attributes and methods
Gardening_GID: Property = Property(name="GID", type=IntegerType)
Gardening.attributes={Gardening_GID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# HomeAppliances class attributes and methods
HomeAppliances_HAID: Property = Property(name="HAID", type=IntegerType)
HomeAppliances.attributes={HomeAppliances_HAID}

# User_Home_Owner class attributes and methods
User_Home_Owner_UserID: Property = Property(name="UserID", type=IntegerType)
User_Home_Owner.attributes={User_Home_Owner_UserID}

# Security_Guard_Police class attributes and methods
Security_Guard_Police_sgpID: Property = Property(name="sgpID", type=IntegerType)
Security_Guard_Police.attributes={Security_Guard_Police_sgpID}

# SolarPanel class attributes and methods
SolarPanel_SPID: Property = Property(name="SPID", type=IntegerType)
SolarPanel.attributes={SolarPanel_SPID}

# Relationships
HomeTheatre_Speakers: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Speakers",
    ends={
        Property(name="speakers0", type=Fans, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre1", type=HomeAppliances, multiplicity=Multiplicity(1, 9999))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system2", type=IoT_based_Smart_Resort_System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone3", type=Gardening, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert4", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System5", type=Home_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system6", type=IoT_based_Smart_Resort_System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor7", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system8", type=IoT_based_Smart_Resort_System, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre9", type=HomeAppliances, multiplicity=Multiplicity(1, 9999))
    }
)
HomeAppliances_Light: BinaryAssociation = BinaryAssociation(
    name="HomeAppliances_Light",
    ends={
        Property(name="HomeAppliances_Light_010", type=Light, multiplicity=Multiplicity(0, 1)),
        Property(name="HomeAppliances_Light_111", type=HomeAppliances, multiplicity=Multiplicity(1, 9999))
    }
)
HomeAppliances_Door: BinaryAssociation = BinaryAssociation(
    name="HomeAppliances_Door",
    ends={
        Property(name="HomeAppliances_Door_012", type=Door, multiplicity=Multiplicity(0, 1)),
        Property(name="HomeAppliances_Door_113", type=HomeAppliances, multiplicity=Multiplicity(1, 9999))
    }
)
User_Home_Owner_Alert: BinaryAssociation = BinaryAssociation(
    name="User_Home_Owner_Alert",
    ends={
        Property(name="User_Home_Owner_Alert_014", type=Alert, multiplicity=Multiplicity(1, 1)),
        Property(name="User_Home_Owner_Alert_115", type=User_Home_Owner, multiplicity=Multiplicity(1, 1))
    }
)
Security_Guard_Police_Alert: BinaryAssociation = BinaryAssociation(
    name="Security_Guard_Police_Alert",
    ends={
        Property(name="Security_Guard_Police_Alert_016", type=Alert, multiplicity=Multiplicity(1, 1)),
        Property(name="Security_Guard_Police_Alert_117", type=Security_Guard_Police, multiplicity=Multiplicity(1, 1))
    }
)
IoT_based_Smart_Resort_System_SolarPanel: BinaryAssociation = BinaryAssociation(
    name="IoT_based_Smart_Resort_System_SolarPanel",
    ends={
        Property(name="IoT_based_Smart_Resort_System_SolarPanel_018", type=SolarPanel, multiplicity=Multiplicity(1, 9999)),
        Property(name="IoT_based_Smart_Resort_System_SolarPanel_119", type=IoT_based_Smart_Resort_System, multiplicity=Multiplicity(1, 1))
    }
)
IoT_based_Smart_Resort_System_Home_Security_System: BinaryAssociation = BinaryAssociation(
    name="IoT_based_Smart_Resort_System_Home_Security_System",
    ends={
        Property(name="IoT_based_Smart_Resort_System_Home_Security_System_020", type=Home_Security_System, multiplicity=Multiplicity(1, 1)),
        Property(name="IoT_based_Smart_Resort_System_Home_Security_System_121", type=IoT_based_Smart_Resort_System, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_674dfb1b_b5ca_4e09_9ca5_9b9118e204e3",
    types={IoT_based_Smart_Resort_System, Sensor, Motion_Sensor, MoistureSensor, Home_Security_System, Alert, Door, Fans, Gardening, Light, HomeAppliances, User_Home_Owner, Security_Guard_Police, SolarPanel},
    associations={HomeTheatre_Speakers, MicroPhone_System, Home_Security_System_Alert, Sensor_System, HomeTheatre_System, HomeAppliances_Light, HomeAppliances_Door, User_Home_Owner_Alert, Security_Guard_Police_Alert, IoT_based_Smart_Resort_System_SolarPanel, IoT_based_Smart_Resort_System_Home_Security_System},
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