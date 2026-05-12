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
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
Door = Class(name="Door")
WIFI_Sense = Class(name="WIFI_Sense")
LPGControl = Class(name="LPGControl")
Light = Class(name="Light")
Start_Of_Day = Class(name="Start_Of_Day")
End_Of_Day = Class(name="End_Of_Day")
SwitchControl = Class(name="SwitchControl")
HomeControl = Class(name="HomeControl")
HouseHolds = Class(name="HouseHolds")
Entertainment = Class(name="Entertainment")

# System class attributes and methods
System_Status: Property = Property(name="Status", type=BooleanType)
System_Update: Property = Property(name="Update", type=FloatType)
System.attributes={System_Status, System_Update}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorType, Sensor_SensorID}

# FireAlarm_Sensor class attributes and methods
FireAlarm_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
FireAlarm_Sensor_DispenseSprinkler: Property = Property(name="DispenseSprinkler", type=BooleanType)
FireAlarm_Sensor.attributes={FireAlarm_Sensor_SmokeAlarm, FireAlarm_Sensor_DispenseSprinkler}

# Motion_Sensor class attributes and methods

# Home_Security_System class attributes and methods
Home_Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Home_Security_System.attributes={Home_Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Door class attributes and methods
Door_DoorID: Property = Property(name="DoorID", type=IntegerType)
Door.attributes={Door_DoorID}

# WIFI_Sense class attributes and methods
WIFI_Sense_WIFIID: Property = Property(name="WIFIID", type=IntegerType)
WIFI_Sense.attributes={WIFI_Sense_WIFIID}

# LPGControl class attributes and methods
LPGControl_LPGControlID: Property = Property(name="LPGControlID", type=IntegerType)
LPGControl.attributes={LPGControl_LPGControlID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# Start_Of_Day class attributes and methods
Start_Of_Day_SOT: Property = Property(name="SOT", type=IntegerType)
Start_Of_Day.attributes={Start_Of_Day_SOT}

# End_Of_Day class attributes and methods
End_Of_Day_EOT: Property = Property(name="EOT", type=IntegerType)
End_Of_Day.attributes={End_Of_Day_EOT}

# SwitchControl class attributes and methods
SwitchControl_SWITCHID: Property = Property(name="SWITCHID", type=IntegerType)
SwitchControl.attributes={SwitchControl_SWITCHID}

# HomeControl class attributes and methods
HomeControl_HTID: Property = Property(name="HTID", type=StringType)
HomeControl.attributes={HomeControl_HTID}

# HouseHolds class attributes and methods
HouseHolds_TimeID: Property = Property(name="TimeID", type=StringType)
HouseHolds_Coffee: Property = Property(name="Coffee", type=StringType)
HouseHolds_DishWasher: Property = Property(name="DishWasher", type=StringType)
HouseHolds_Alarm: Property = Property(name="Alarm", type=StringType)
HouseHolds_WashingMachine: Property = Property(name="WashingMachine", type=StringType)
HouseHolds.attributes={HouseHolds_Coffee, HouseHolds_DishWasher, HouseHolds_Alarm, HouseHolds_TimeID, HouseHolds_WashingMachine}

# Entertainment class attributes and methods
Entertainment_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
Entertainment.attributes={Entertainment_DeviceID}

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
        Property(name="camera2", type=WIFI_Sense, multiplicity=Multiplicity(0, 9999)),
        Property(name="door3", type=Door, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_TV: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_TV",
    ends={
        Property(name="tV4", type=SwitchControl, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre5", type=HomeControl, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Speakers: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Speakers",
    ends={
        Property(name="speakers6", type=LPGControl, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre7", type=HomeControl, multiplicity=Multiplicity(1, 9999))
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
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert12", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System13", type=Home_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system14", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor15", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds16", type=HouseHolds, multiplicity=Multiplicity(0, 1)),
        Property(name="system17", type=System, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system18", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre19", type=HomeControl, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system20", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System21", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)
TV_Entertainment: BinaryAssociation = BinaryAssociation(
    name="TV_Entertainment",
    ends={
        Property(name="entertainment22", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="tV23", type=SwitchControl, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Entertainment: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Entertainment",
    ends={
        Property(name="entertainment24", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre25", type=HomeControl, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_63e4825f_d2a8_4380_9300_09b3a632dcc3",
    types={System, Sensor, FireAlarm_Sensor, Motion_Sensor, Home_Security_System, Alert, Door, WIFI_Sense, LPGControl, Light, Start_Of_Day, End_Of_Day, SwitchControl, HomeControl, HouseHolds, Entertainment},
    associations={Sensor_Door, Door_Camera, HomeTheatre_TV, HomeTheatre_Speakers, HouseHolds_Start_Of_Day, HouseHolds_End_Of_Day, Home_Security_System_Alert, Sensor_System, System_HouseHolds, HomeTheatre_System, Home_Security_System_System, TV_Entertainment, HomeTheatre_Entertainment},
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