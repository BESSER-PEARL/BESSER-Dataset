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
Smart_mirror = Class(name="Smart_mirror")
Sensor = Class(name="Sensor")
FireAlarm_Sensor = Class(name="FireAlarm_Sensor")
Motion_Sensor = Class(name="Motion_Sensor")
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
Door_Sensor = Class(name="Door_Sensor")
Camera = Class(name="Camera")
Voice_control = Class(name="Voice_control")
Light = Class(name="Light")
HomeAutomation = Class(name="HomeAutomation")
Newsfeed = Class(name="Newsfeed")

# Smart_mirror class attributes and methods
Smart_mirror_Status: Property = Property(name="Status", type=BooleanType)
Smart_mirror_Update: Property = Property(name="Update", type=FloatType)
Smart_mirror_PhoneConnect: Property = Property(name="PhoneConnect", type=BooleanType)
Smart_mirror_Display_newsfeed: Property = Property(name="Display_newsfeed", type=Newsfeed)
Smart_mirror_security: Property = Property(name="security", type=Home_Security_System)
Smart_mirror.attributes={Smart_mirror_security, Smart_mirror_Status, Smart_mirror_Update, Smart_mirror_Display_newsfeed, Smart_mirror_PhoneConnect}

# Sensor class attributes and methods
Sensor_SensorName: Property = Property(name="SensorName", type=IntegerType)
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor.attributes={Sensor_SensorName, Sensor_SensorID}

# FireAlarm_Sensor class attributes and methods
FireAlarm_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
FireAlarm_Sensor.attributes={FireAlarm_Sensor_SmokeAlarm}

# Motion_Sensor class attributes and methods

# Home_Security_System class attributes and methods
Home_Security_System_UserID: Property = Property(name="UserID", type=IntegerType)
Home_Security_System.attributes={Home_Security_System_UserID}

# Alert class attributes and methods
Alert_AlertID: Property = Property(name="AlertID", type=IntegerType)
Alert.attributes={Alert_AlertID}

# Door_Sensor class attributes and methods
Door_Sensor_DoorID: Property = Property(name="DoorID", type=IntegerType)
Door_Sensor.attributes={Door_Sensor_DoorID}

# Camera class attributes and methods
Camera_CameraID: Property = Property(name="CameraID", type=IntegerType)
Camera.attributes={Camera_CameraID}

# Voice_control class attributes and methods
Voice_control_MicID: Property = Property(name="MicID", type=StringType)
Voice_control.attributes={Voice_control_MicID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# HomeAutomation class attributes and methods
HomeAutomation_Lights: Property = Property(name="Lights", type=StringType)
HomeAutomation_Apllicances: Property = Property(name="Apllicances", type=StringType)
HomeAutomation.attributes={HomeAutomation_Lights, HomeAutomation_Apllicances}

# Newsfeed class attributes and methods
Newsfeed_Email: Property = Property(name="Email", type=StringType)
Newsfeed_News: Property = Property(name="News", type=StringType)
Newsfeed_Weather: Property = Property(name="Weather", type=StringType)
Newsfeed_Calendar: Property = Property(name="Calendar", type=StringType)
Newsfeed_Phone: Property = Property(name="Phone", type=StringType)
Newsfeed.attributes={Newsfeed_Email, Newsfeed_Weather, Newsfeed_Phone, Newsfeed_News, Newsfeed_Calendar}

# Relationships
Sensor_Door: BinaryAssociation = BinaryAssociation(
    name="Sensor_Door",
    ends={
        Property(name="door0", type=Door_Sensor, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor1", type=Sensor, multiplicity=Multiplicity(1, 1))
    }
)
Door_Camera: BinaryAssociation = BinaryAssociation(
    name="Door_Camera",
    ends={
        Property(name="camera2", type=Camera, multiplicity=Multiplicity(0, 9999)),
        Property(name="door3", type=Door_Sensor, multiplicity=Multiplicity(1, 1))
    }
)
MicroPhone_System: BinaryAssociation = BinaryAssociation(
    name="MicroPhone_System",
    ends={
        Property(name="system4", type=Smart_mirror, multiplicity=Multiplicity(1, 1)),
        Property(name="microPhone5", type=Voice_control, multiplicity=Multiplicity(1, 9999))
    }
)
Home_Security_System_Alert: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_Alert",
    ends={
        Property(name="alert6", type=Alert, multiplicity=Multiplicity(0, 1)),
        Property(name="home_Security_System7", type=Home_Security_System, multiplicity=Multiplicity(0, 1))
    }
)
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system8", type=Smart_mirror, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor9", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system10", type=Smart_mirror, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre11", type=HomeAutomation, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system12", type=Smart_mirror, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System13", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)
Smart_mirror_Voice_control2: BinaryAssociation = BinaryAssociation(
    name="Smart_mirror_Voice_control2",
    ends={
        Property(name="voice_control214", type=Newsfeed, multiplicity=Multiplicity(0, 1)),
        Property(name="smart_mirror15", type=Smart_mirror, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_98b763f5_7b88_4085_982e_b6f6d5a5af0d",
    types={Smart_mirror, Sensor, FireAlarm_Sensor, Motion_Sensor, Home_Security_System, Alert, Door_Sensor, Camera, Voice_control, Light, HomeAutomation, Newsfeed},
    associations={Sensor_Door, Door_Camera, MicroPhone_System, Home_Security_System_Alert, Sensor_System, HomeTheatre_System, Home_Security_System_System, Smart_mirror_Voice_control2},
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