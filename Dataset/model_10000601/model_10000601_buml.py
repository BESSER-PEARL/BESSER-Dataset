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
Light_Sensor = Class(name="Light_Sensor")
Motion_Sensor = Class(name="Motion_Sensor")
PressureSensor = Class(name="PressureSensor")
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
Microcontroller = Class(name="Microcontroller")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Status, System_Update}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorID, Sensor_SensorType}

# Light_Sensor class attributes and methods
Light_Sensor_DetectLight__: Property = Property(name="DetectLight__", type=IntegerType)
Light_Sensor.attributes={Light_Sensor_DetectLight__}

# Motion_Sensor class attributes and methods

# PressureSensor class attributes and methods

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
HouseHolds_Fan: Property = Property(name="Fan", type=StringType)
HouseHolds_Computer: Property = Property(name="Computer", type=StringType)
HouseHolds_Light: Property = Property(name="Light", type=StringType)
HouseHolds.attributes={HouseHolds_Light, HouseHolds_Computer, HouseHolds_Fan, HouseHolds_TimeID}

# Entertainment class attributes and methods
Entertainment_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
Entertainment.attributes={Entertainment_DeviceID}

# Microcontroller class attributes and methods
Microcontroller_sendData__: Property = Property(name="sendData__", type=StringType)
Microcontroller.attributes={Microcontroller_sendData__}

# Relationships
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system14", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre15", type=HomeTheatre, multiplicity=Multiplicity(0, 1))
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
Sensor_Microcontroller: BinaryAssociation = BinaryAssociation(
    name="Sensor_Microcontroller",
    ends={
        Property(name="microcontroller22", type=Microcontroller, multiplicity=Multiplicity(0, 1)),
        Property(name="sensor23", type=Sensor, multiplicity=Multiplicity(0, 1))
    }
)
Microcontroller_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="Microcontroller_HouseHolds",
    ends={
        Property(name="houseHolds24", type=HouseHolds, multiplicity=Multiplicity(0, 1)),
        Property(name="microcontroller25", type=Microcontroller, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_Door: BinaryAssociation = BinaryAssociation(
    name="Sensor_Door",
    ends={
        Property(name="door0", type=Door, multiplicity=Multiplicity(1, 1)),
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
HouseHolds_Start_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_Start_Of_Day",
    ends={
        Property(name="start_Of_Day6", type=Start_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds7", type=HouseHolds, multiplicity=Multiplicity(0, 1))
    }
)
HouseHolds_End_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_End_Of_Day",
    ends={
        Property(name="end_Of_Day8", type=End_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds9", type=HouseHolds, multiplicity=Multiplicity(0, 1))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system10", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone11", type=MicroPhone, multiplicity=Multiplicity(1, 9999))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds12", type=HouseHolds, multiplicity=Multiplicity(0, 1)),
        Property(name="system13", type=System, multiplicity=Multiplicity(1, 1))
    }
)
Microcontroller_System: BinaryAssociation = BinaryAssociation(
    name="Microcontroller_System",
    ends={
        Property(name="system26", type=System, multiplicity=Multiplicity(0, 1)),
        Property(name="microcontroller27", type=Microcontroller, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_49a00a56_b506_4953_a419_8df1f114e733",
    types={System, Sensor, Light_Sensor, Motion_Sensor, PressureSensor, Door, Camera, Speakers, MicroPhone, Light, Start_Of_Day, End_Of_Day, TV, HomeTheatre, HouseHolds, Entertainment, Microcontroller},
    associations={HomeTheatre_System, TV_Entertainment, Speakers_Entertainment, HomeTheatre_Entertainment, Sensor_Microcontroller, Microcontroller_HouseHolds, Sensor_Door, HomeTheatre_TV, HomeTheatre_Speakers, HouseHolds_Start_Of_Day, HouseHolds_End_Of_Day, MicroPhone_System, System_HouseHolds, Microcontroller_System},
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