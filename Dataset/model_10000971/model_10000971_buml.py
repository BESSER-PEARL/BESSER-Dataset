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
FireAlarm_Sensor = Class(name="FireAlarm_Sensor")
Motion_Sensor = Class(name="Motion_Sensor")
PressureSensor = Class(name="PressureSensor")
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
Door = Class(name="Door")
Camera = Class(name="Camera")
Speakers = Class(name="Speakers")
Light = Class(name="Light")
TV = Class(name="TV")
HomeTheatre = Class(name="HomeTheatre")
HouseHolds = Class(name="HouseHolds")
Entertainment = Class(name="Entertainment")
Class_ = Class(name="Class")
_unnamed = Class(name="_unnamed")
Symbol_Meaning = Class(name="Symbol_Meaning")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Status, System_Update}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorType, Sensor_SensorID}

# FireAlarm_Sensor class attributes and methods
FireAlarm_Sensor_DispenseSprinkler: Property = Property(name="DispenseSprinkler", type=BooleanType)
FireAlarm_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
FireAlarm_Sensor.attributes={FireAlarm_Sensor_SmokeAlarm, FireAlarm_Sensor_DispenseSprinkler}

# Motion_Sensor class attributes and methods

# PressureSensor class attributes and methods

# Home_Security_System class attributes and methods
Home_Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Home_Security_System.attributes={Home_Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Door class attributes and methods
Door_DoorID: Property = Property(name="DoorID", type=IntegerType)
Door.attributes={Door_DoorID}

# Camera class attributes and methods
Camera_CameraID: Property = Property(name="CameraID", type=IntegerType)
Camera.attributes={Camera_CameraID}

# Speakers class attributes and methods
Speakers_SpeakerID: Property = Property(name="SpeakerID", type=IntegerType)
Speakers.attributes={Speakers_SpeakerID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# TV class attributes and methods
TV_TVID: Property = Property(name="TVID", type=IntegerType)
TV.attributes={TV_TVID}

# HomeTheatre class attributes and methods
HomeTheatre_HTID: Property = Property(name="HTID", type=StringType)
HomeTheatre.attributes={HomeTheatre_HTID}

# HouseHolds class attributes and methods
HouseHolds_TimeID: Property = Property(name="TimeID", type=StringType)
HouseHolds_Coffee: Property = Property(name="Coffee", type=StringType)
HouseHolds_DishWasher: Property = Property(name="DishWasher", type=StringType)
HouseHolds_Alarm: Property = Property(name="Alarm", type=StringType)
HouseHolds_WashingMachine: Property = Property(name="WashingMachine", type=StringType)
HouseHolds.attributes={HouseHolds_TimeID, HouseHolds_DishWasher, HouseHolds_Coffee, HouseHolds_Alarm, HouseHolds_WashingMachine}

# Entertainment class attributes and methods
Entertainment_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
Entertainment.attributes={Entertainment_DeviceID}

# Class class attributes and methods

# _unnamed class attributes and methods

# Symbol_Meaning class attributes and methods
Symbol_Meaning_____: Property = Property(name="____", type=StringType)
Symbol_Meaning.attributes={Symbol_Meaning_____}

# Relationships
Sensor_Door: BinaryAssociation = BinaryAssociation(
    name="Sensor_Door",
    ends={
        Property(name="door0", type=Door, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor1", type=Sensor, multiplicity=Multiplicity(1, 1))
    }
)
Door_Camera: BinaryAssociation = BinaryAssociation(
    name="Door_Camera",
    ends={
        Property(name="camera2", type=Camera, multiplicity=Multiplicity(0, 9999)),
        Property(name="door3", type=Door, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_TV: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_TV",
    ends={
        Property(name="tV4", type=TV, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre5", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Speakers: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Speakers",
    ends={
        Property(name="speakers6", type=Speakers, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre7", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert8", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System9", type=Home_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system10", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor11", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds12", type=HouseHolds, multiplicity=Multiplicity(0, 1)),
        Property(name="system13", type=System, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system14", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre15", type=HomeTheatre, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system16", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System17", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)
TV_Entertainment: BinaryAssociation = BinaryAssociation(
    name="TV_Entertainment",
    ends={
        Property(name="entertainment18", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="tV19", type=TV, multiplicity=Multiplicity(1, 9999))
    }
)
Speakers_Entertainment: BinaryAssociation = BinaryAssociation(
    name="Speakers_Entertainment",
    ends={
        Property(name="entertainment20", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="speakers21", type=Speakers, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Entertainment: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Entertainment",
    ends={
        Property(name="entertainment22", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre23", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7627ca61_8fd2_499b_b017_6a6dec435ec3",
    types={System, Sensor, FireAlarm_Sensor, Motion_Sensor, PressureSensor, Home_Security_System, Alert, Door, Camera, Speakers, Light, TV, HomeTheatre, HouseHolds, Entertainment, Class_, _unnamed, Symbol_Meaning},
    associations={Sensor_Door, Door_Camera, HomeTheatre_TV, HomeTheatre_Speakers, Home_Security_System_Alert, Sensor_System, System_HouseHolds, HomeTheatre_System, Home_Security_System_System, TV_Entertainment, Speakers_Entertainment, HomeTheatre_Entertainment},
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