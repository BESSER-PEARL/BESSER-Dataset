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
MotionSensor = Class(name="MotionSensor")
Security_System = Class(name="Security_System")
Alert = Class(name="Alert")
Curtains = Class(name="Curtains")
Speakers = Class(name="Speakers")
PowerSystem = Class(name="PowerSystem")
Light = Class(name="Light")
Start_Of_Day = Class(name="Start_Of_Day")
End_Of_Day = Class(name="End_Of_Day")
HomeTheatre = Class(name="HomeTheatre")
Kitchen = Class(name="Kitchen")
TechSupport = Class(name="TechSupport")
ROOM = Class(name="ROOM")
UserProfile = Class(name="UserProfile")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Status, System_Update}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorID, Sensor_SensorType}

# MotionSensor class attributes and methods

# Security_System class attributes and methods
Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Security_System.attributes={Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Curtains class attributes and methods
Curtains_CurtaiunID: Property = Property(name="CurtaiunID", type=IntegerType)
Curtains.attributes={Curtains_CurtaiunID}

# Speakers class attributes and methods
Speakers_SpeakerID: Property = Property(name="SpeakerID", type=IntegerType)
Speakers.attributes={Speakers_SpeakerID}

# PowerSystem class attributes and methods
PowerSystem_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
PowerSystem.attributes={PowerSystem_DeviceID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=IntegerType)
Light.attributes={Light_LightID}

# Start_Of_Day class attributes and methods
Start_Of_Day_SOT: Property = Property(name="SOT", type=IntegerType)
Start_Of_Day.attributes={Start_Of_Day_SOT}

# End_Of_Day class attributes and methods
End_Of_Day_EOT: Property = Property(name="EOT", type=IntegerType)
End_Of_Day.attributes={End_Of_Day_EOT}

# HomeTheatre class attributes and methods
HomeTheatre_SSID: Property = Property(name="SSID", type=StringType)
HomeTheatre.attributes={HomeTheatre_SSID}

# Kitchen class attributes and methods
Kitchen_TimeID: Property = Property(name="TimeID", type=StringType)
Kitchen.attributes={Kitchen_TimeID}

# TechSupport class attributes and methods
TechSupport_TechID: Property = Property(name="TechID", type=IntegerType)
TechSupport.attributes={TechSupport_TechID}

# ROOM class attributes and methods
ROOM_RoomID: Property = Property(name="RoomID", type=StringType)
ROOM.attributes={ROOM_RoomID}

# UserProfile class attributes and methods
UserProfile_ProfileID: Property = Property(name="ProfileID", type=IntegerType)
UserProfile.attributes={UserProfile_ProfileID}

# Relationships
Sensor_Door: BinaryAssociation = BinaryAssociation(
    name="Sensor_Door",
    ends={
        Property(name="door0", type=Curtains, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor1", type=Sensor, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_Speakers: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Speakers",
    ends={
        Property(name="speakers2", type=Speakers, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre3", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
HouseHolds_Start_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_Start_Of_Day",
    ends={
        Property(name="start_Of_Day4", type=Start_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds5", type=Kitchen, multiplicity=Multiplicity(0, 1))
    }
)
HouseHolds_End_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_End_Of_Day",
    ends={
        Property(name="end_Of_Day6", type=End_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds7", type=Kitchen, multiplicity=Multiplicity(0, 1))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system8", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone9", type=PowerSystem, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert10", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System11", type=Security_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system12", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor13", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds14", type=Kitchen, multiplicity=Multiplicity(0, 1)),
        Property(name="system15", type=System, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system16", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre17", type=HomeTheatre, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="Home_Security_System_System_018", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="Home_Security_System_System_119", type=Security_System, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5f35ea64_34dc_45c1_9de7_744d6440fce3",
    types={System, Sensor, MotionSensor, Security_System, Alert, Curtains, Speakers, PowerSystem, Light, Start_Of_Day, End_Of_Day, HomeTheatre, Kitchen, TechSupport, ROOM, UserProfile},
    associations={Sensor_Door, HomeTheatre_Speakers, HouseHolds_Start_Of_Day, HouseHolds_End_Of_Day, MicroPhone_System, Home_Security_System_Alert, Sensor_System, System_HouseHolds, HomeTheatre_System, Home_Security_System_System},
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