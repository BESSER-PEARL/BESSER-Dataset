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
Hub_Device = Class(name="Hub_Device")
Sensor = Class(name="Sensor")
Motion_Sensor = Class(name="Motion_Sensor")
PressureSensor = Class(name="PressureSensor")
Home_Security_System = Class(name="Home_Security_System")
Alert = Class(name="Alert")
Door = Class(name="Door")
Camera = Class(name="Camera")
Manager = Class(name="Manager")
Light = Class(name="Light")
Start_Of_Day = Class(name="Start_Of_Day")
End_Of_Day = Class(name="End_Of_Day")
Admin = Class(name="Admin")
Users = Class(name="Users")
Display = Class(name="Display")
Employee = Class(name="Employee")
RFID_Sensor = Class(name="RFID_Sensor")
UDP_Controller = Class(name="UDP_Controller")
UDP_Socket = Class(name="UDP_Socket")
int = Class(name="int")

# Hub_Device class attributes and methods
Hub_Device_Status: Property = Property(name="Status", type=BooleanType)
Hub_Device_Update: Property = Property(name="Update", type=FloatType)
Hub_Device.attributes={Hub_Device_Update, Hub_Device_Status}

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorType, Sensor_SensorID}

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

# Manager class attributes and methods
Manager_MangagerID: Property = Property(name="MangagerID", type=IntegerType)
Manager.attributes={Manager_MangagerID}

# Light class attributes and methods
Light_LightID: Property = Property(name="LightID", type=StringType)
Light.attributes={Light_LightID}

# Start_Of_Day class attributes and methods
Start_Of_Day_SOT: Property = Property(name="SOT", type=IntegerType)
Start_Of_Day.attributes={Start_Of_Day_SOT}

# End_Of_Day class attributes and methods
End_Of_Day_EOT: Property = Property(name="EOT", type=IntegerType)
End_Of_Day.attributes={End_Of_Day_EOT}

# Admin class attributes and methods
Admin_AdminID: Property = Property(name="AdminID", type=IntegerType)
Admin.attributes={Admin_AdminID}

# Users class attributes and methods
Users_HTID: Property = Property(name="HTID", type=StringType)
Users.attributes={Users_HTID}

# Display class attributes and methods
Display_TimeID: Property = Property(name="TimeID", type=StringType)
Display_Coffee: Property = Property(name="Coffee", type=StringType)
Display_DishWasher: Property = Property(name="DishWasher", type=StringType)
Display_Alarm: Property = Property(name="Alarm", type=StringType)
Display_WashingMachine: Property = Property(name="WashingMachine", type=StringType)
Display.attributes={Display_WashingMachine, Display_TimeID, Display_Coffee, Display_Alarm, Display_DishWasher}

# Employee class attributes and methods
Employee_EmployeeID: Property = Property(name="EmployeeID", type=IntegerType)
Employee.attributes={Employee_EmployeeID}

# RFID_Sensor class attributes and methods

# UDP_Controller class attributes and methods
UDP_Controller_ip_session: Property = Property(name="ip_session", type=StringType)
UDP_Controller.attributes={UDP_Controller_ip_session}

# UDP_Socket class attributes and methods
UDP_Socket_socket: Property = Property(name="socket", type=IntegerType)
UDP_Socket.attributes={UDP_Socket_socket}

# int class attributes and methods

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
        Property(name="tV4", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre5", type=Users, multiplicity=Multiplicity(1, 9999))
    }
)
HomeTheatre_Speakers: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_Speakers",
    ends={
        Property(name="speakers6", type=Manager, multiplicity=Multiplicity(0, 1)),
        Property(name="homeTheatre7", type=Users, multiplicity=Multiplicity(1, 9999))
    }
)
HouseHolds_Start_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_Start_Of_Day",
    ends={
        Property(name="start_Of_Day8", type=Start_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds9", type=Display, multiplicity=Multiplicity(0, 1))
    }
)
HouseHolds_End_Of_Day: BinaryAssociation = BinaryAssociation(
    name="HouseHolds_End_Of_Day",
    ends={
        Property(name="end_Of_Day10", type=End_Of_Day, multiplicity=Multiplicity(0, 1)),
        Property(name="houseHolds11", type=Display, multiplicity=Multiplicity(0, 1))
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
        Property(name="system14", type=Hub_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor15", type=Sensor, multiplicity=Multiplicity(1, 9999))
    }
)
System_HouseHolds: BinaryAssociation = BinaryAssociation(
    name="System_HouseHolds",
    ends={
        Property(name="houseHolds16", type=Display, multiplicity=Multiplicity(0, 1)),
        Property(name="system17", type=Hub_Device, multiplicity=Multiplicity(1, 1))
    }
)
HomeTheatre_System: BinaryAssociation = BinaryAssociation(
    name="HomeTheatre_System",
    ends={
        Property(name="system18", type=Hub_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="homeTheatre19", type=Users, multiplicity=Multiplicity(0, 1))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="system20", type=Hub_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="home_Security_System21", type=Home_Security_System, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_NZfyMPH2EemvpsGtKb89OA",
    types={Hub_Device, Sensor, Motion_Sensor, PressureSensor, Home_Security_System, Alert, Door, Camera, Manager, Light, Start_Of_Day, End_Of_Day, Admin, Users, Display, Employee, RFID_Sensor, UDP_Controller, UDP_Socket, int},
    associations={Sensor_Door, Door_Camera, HomeTheatre_TV, HomeTheatre_Speakers, HouseHolds_Start_Of_Day, HouseHolds_End_Of_Day, Home_Security_System_Alert, Sensor_System, System_HouseHolds, HomeTheatre_System, Home_Security_System_System},
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