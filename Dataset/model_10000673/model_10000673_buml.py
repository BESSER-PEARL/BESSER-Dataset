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
System___mirror = Class(name="System___mirror")
Sensor = Class(name="Sensor")
FireAlarm_Sensor = Class(name="FireAlarm_Sensor")
Motion_Sensor = Class(name="Motion_Sensor")
Door_Sensor = Class(name="Door_Sensor")
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
Door = Class(name="Door")
Camera = Class(name="Camera")
Radio = Class(name="Radio")
Light = Class(name="Light")
Morning = Class(name="Morning")
Evening = Class(name="Evening")
TV = Class(name="TV")
HomeTheatre = Class(name="HomeTheatre")
MyHome = Class(name="MyHome")
Entertainment = Class(name="Entertainment")
Newsfeed = Class(name="Newsfeed")

# System___mirror class attributes and methods
System___mirror_Status: Property = Property(name="Status", type=BooleanType)
System___mirror_Update: Property = Property(name="Update", type=FloatType)
System___mirror_PhoneConnect: Property = Property(name="PhoneConnect", type=BooleanType)
System___mirror_Display_feed: Property = Property(name="Display_feed", type=Newsfeed)
System___mirror_security: Property = Property(name="security", type=Home_Security_System)
System___mirror.attributes={System___mirror_Status, System___mirror_Update, System___mirror_security, System___mirror_PhoneConnect, System___mirror_Display_feed}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorID, Sensor_SensorType}

# FireAlarm_Sensor class attributes and methods
FireAlarm_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
FireAlarm_Sensor.attributes={FireAlarm_Sensor_SmokeAlarm}

# Motion_Sensor class attributes and methods

# Door_Sensor class attributes and methods

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

# Radio class attributes and methods
Radio_RadioID: Property = Property(name="RadioID", type=IntegerType)
Radio.attributes={Radio_RadioID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# Morning class attributes and methods
Morning_Morn: Property = Property(name="Morn", type=IntegerType)
Morning.attributes={Morning_Morn}

# Evening class attributes and methods
Evening_Night: Property = Property(name="Night", type=IntegerType)
Evening.attributes={Evening_Night}

# TV class attributes and methods
TV_TVID: Property = Property(name="TVID", type=IntegerType)
TV.attributes={TV_TVID}

# HomeTheatre class attributes and methods
HomeTheatre_HTID: Property = Property(name="HTID", type=StringType)
HomeTheatre.attributes={HomeTheatre_HTID}

# MyHome class attributes and methods
MyHome_TimeID: Property = Property(name="TimeID", type=StringType)
MyHome_Coffee: Property = Property(name="Coffee", type=StringType)
MyHome_DishWasher: Property = Property(name="DishWasher", type=StringType)
MyHome_Alarm: Property = Property(name="Alarm", type=StringType)
MyHome_WashingMachine: Property = Property(name="WashingMachine", type=StringType)
MyHome.attributes={MyHome_WashingMachine, MyHome_Alarm, MyHome_Coffee, MyHome_TimeID, MyHome_DishWasher}

# Entertainment class attributes and methods
Entertainment_DeviceID: Property = Property(name="DeviceID", type=IntegerType)
Entertainment.attributes={Entertainment_DeviceID}

# Newsfeed class attributes and methods
Newsfeed_Email: Property = Property(name="Email", type=StringType)
Newsfeed_TimeID: Property = Property(name="TimeID", type=StringType)
Newsfeed_News: Property = Property(name="News", type=StringType)
Newsfeed_weather: Property = Property(name="weather", type=StringType)
Newsfeed_Calendar: Property = Property(name="Calendar", type=StringType)
Newsfeed.attributes={Newsfeed_Email, Newsfeed_Calendar, Newsfeed_weather, Newsfeed_TimeID, Newsfeed_News}

# Relationships
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds16", type=MyHome, multiplicity=Multiplicity(0, 1)),
        Property(name="system17", type=System___mirror, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system18", type=System___mirror, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre19", type=HomeTheatre, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system20", type=System___mirror, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System21", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)
TV_Entertainment: BinaryAssociation = BinaryAssociation(
    name="TV_Entertainment",
    ends={
        Property(name="entertainment22", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="tV23", type=TV, multiplicity=Multiplicity(1, 9999))
    }
)
Speakers_Entertainment: BinaryAssociation = BinaryAssociation(
    name="Speakers_Entertainment",
    ends={
        Property(name="entertainment24", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="speakers25", type=Radio, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Entertainment: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Entertainment",
    ends={
        Property(name="entertainment26", type=Entertainment, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre27", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
System___mirror_Newsfeed: BinaryAssociation = BinaryAssociation(
    name="System___mirror_Newsfeed",
    ends={
        Property(name="newsfeed28", type=Newsfeed, multiplicity=Multiplicity(0, 1)),
        Property(name="system___mirror29", type=System___mirror, multiplicity=Multiplicity(1, 1))
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
        Property(name="speakers6", type=Radio, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre7", type=HomeTheatre, multiplicity=Multiplicity(1, 9999))
    }
)
HouseHolds_Start_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_Start_Of_Day",
    ends={
        Property(name="start_Of_Day8", type=Morning, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds9", type=MyHome, multiplicity=Multiplicity(0, 1))
    }
)
HouseHolds_End_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_End_Of_Day",
    ends={
        Property(name="end_Of_Day10", type=Evening, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds11", type=MyHome, multiplicity=Multiplicity(0, 1))
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
        Property(name="system14", type=System___mirror, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor15", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_53f1d7a5_48ce_4abb_aaa9_2e12261a1fbd",
    types={System___mirror, Sensor, FireAlarm_Sensor, Motion_Sensor, Door_Sensor, Home_Security_System, Alert, Door, Camera, Radio, Light, Morning, Evening, TV, HomeTheatre, MyHome, Entertainment, Newsfeed},
    associations={System_HouseHolds, HomeTheatre_System, Home_Security_System_System, TV_Entertainment, Speakers_Entertainment, HomeTheatre_Entertainment, System___mirror_Newsfeed, Sensor_Door, Door_Camera, HomeTheatre_TV, HomeTheatre_Speakers, HouseHolds_Start_Of_Day, HouseHolds_End_Of_Day, Home_Security_System_Alert, Sensor_System},
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