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
MicroPhone = Class(name="MicroPhone")
Light = Class(name="Light")
Start_Of_Day = Class(name="Start_Of_Day")
End_Of_Day = Class(name="End_Of_Day")
TV = Class(name="TV")
HomeTheatre = Class(name="HomeTheatre")
HouseHolds = Class(name="HouseHolds")
Entertainment = Class(name="Entertainment")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Status, System_Update}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorID, Sensor_SensorType}

# FireAlarm_Sensor class attributes and methods
FireAlarm_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
FireAlarm_Sensor_DispenseSprinkler: Property = Property(name="DispenseSprinkler", type=BooleanType)
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

# MicroPhone class attributes and methods
MicroPhone_MicID: Property = Property(name="MicID", type=StringType)
MicroPhone.attributes={MicroPhone_MicID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# Start_Of_Day class attributes and methods
Start_Of_Day_SOT: Property = Property(name="SOT", type=IntegerType)
Start_Of_Day.attributes={Start_Of_Day_SOT}

# End_Of_Day class attributes and methods
End_Of_Day_EOT: Property = Property(name="EOT", type=IntegerType)
End_Of_Day.attributes={End_Of_Day_EOT}

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
HouseHolds.attributes={HouseHolds_DishWasher, HouseHolds_Alarm, HouseHolds_TimeID, HouseHolds_Coffee, HouseHolds_WashingMachine}

# Entertainment class attributes and methods
Entertainment_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
Entertainment.attributes={Entertainment_DeviceID}

# Relationships
HomeTheatre_Entertainment: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Entertainment",
    ends={
        Property(name="entertainment28", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre29", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
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
HouseHolds_Start_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_Start_Of_Day",
    ends={
        Property(name="start_Of_Day8", type=Start_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds9", type=HouseHolds, multiplicity=Multiplicity(0, 1))
    }
)
HouseHolds_End_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_End_Of_Day",
    ends={
        Property(name="end_Of_Day10", type=End_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds11", type=HouseHolds, multiplicity=Multiplicity(0, 1))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system12", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone13", type=MicroPhone, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert14", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System15", type=Home_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system16", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor17", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds18", type=HouseHolds, multiplicity=Multiplicity(0, 1)),
        Property(name="system19", type=System, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system20", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre21", type=HomeTheatre, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system22", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System23", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)
TV_Entertainment: BinaryAssociation = BinaryAssociation(
    name="TV_Entertainment",
    ends={
        Property(name="entertainment24", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="tV25", type=TV, multiplicity=Multiplicity(1, 9999))
    }
)
Speakers_Entertainment: BinaryAssociation = BinaryAssociation(
    name="Speakers_Entertainment",
    ends={
        Property(name="entertainment26", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="speakers27", type=Speakers, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0f3bc4a0_cb0c_412d_be47_d3b53c063030",
    types={System, Sensor, FireAlarm_Sensor, Motion_Sensor, PressureSensor, Home_Security_System, Alert, Door, Camera, Speakers, MicroPhone, Light, Start_Of_Day, End_Of_Day, TV, HomeTheatre, HouseHolds, Entertainment},
    associations={HomeTheatre_Entertainment, Sensor_Door, Door_Camera, HomeTheatre_TV, HomeTheatre_Speakers, HouseHolds_Start_Of_Day, HouseHolds_End_Of_Day, MicroPhone_System, Home_Security_System_Alert, Sensor_System, System_HouseHolds, HomeTheatre_System, Home_Security_System_System, TV_Entertainment, Speakers_Entertainment},
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