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
Firebase = Class(name="Firebase")
Sensor = Class(name="Sensor")
Gas_Smoke_Sensor = Class(name="Gas_Smoke_Sensor")
Temperature_Sensor = Class(name="Temperature_Sensor")
MobileApp = Class(name="MobileApp")
Notification = Class(name="Notification")
Count_Sensor = Class(name="Count_Sensor")
Arduino = Class(name="Arduino")
Fire_Alarm_System__Component = Class(name="Fire_Alarm_System__Component")
Building_Owner__Actor = Class(name="Building_Owner__Actor")
Fire_Department__Actor = Class(name="Fire_Department__Actor")
Sensors_Actor = Class(name="Sensors_Actor")
TurnDownAlarm = Class(name="TurnDownAlarm")
AddAlarm = Class(name="AddAlarm")
ViewTemp_Smoke = Class(name="ViewTemp_Smoke")
Alarm = Class(name="Alarm")
WebPage = Class(name="WebPage")
Notify_User_of_fire_external = Class(name="Notify_User_of_fire_external")
Add_new_alarm_external = Class(name="Add_new_alarm_external")
Disable_detector_external = Class(name="Disable_detector_external")
Sense_and_Update_Data_external = Class(name="Sense_and_Update_Data_external")
View_sensors_data_external = Class(name="View_sensors_data_external")
Set_time_external = Class(name="Set_time_external")

# Firebase class attributes and methods

# Sensor class attributes and methods
Sensor_SensorID: Property = Property(name="SensorID", type=IntegerType)
Sensor_SensorType: Property = Property(name="SensorType", type=IntegerType)
Sensor.attributes={Sensor_SensorType, Sensor_SensorID}

# Gas_Smoke_Sensor class attributes and methods
Gas_Smoke_Sensor_SmokeAlarm: Property = Property(name="SmokeAlarm", type=BooleanType)
Gas_Smoke_Sensor_CheckSmoke: Property = Property(name="CheckSmoke", type=BooleanType)
Gas_Smoke_Sensor.attributes={Gas_Smoke_Sensor_CheckSmoke, Gas_Smoke_Sensor_SmokeAlarm}

# Temperature_Sensor class attributes and methods

# MobileApp class attributes and methods
MobileApp_UserID: Property = Property(name="UserID", type=IntegerType)
MobileApp_AlarmID: Property = Property(name="AlarmID", type=IntegerType)
MobileApp.attributes={MobileApp_AlarmID, MobileApp_UserID}

# Notification class attributes and methods
Notification_TempThreshold: Property = Property(name="TempThreshold", type=FloatType)
Notification_SmokeThreshold: Property = Property(name="SmokeThreshold", type=FloatType)
Notification.attributes={Notification_SmokeThreshold, Notification_TempThreshold}

# Count_Sensor class attributes and methods
Count_Sensor_People_: Property = Property(name="People_", type=IntegerType)
Count_Sensor.attributes={Count_Sensor_People_}

# Arduino class attributes and methods

# Fire_Alarm_System__Component class attributes and methods

# Building_Owner__Actor class attributes and methods

# Fire_Department__Actor class attributes and methods

# Sensors_Actor class attributes and methods

# TurnDownAlarm class attributes and methods

# AddAlarm class attributes and methods
AddAlarm_AlarmName: Property = Property(name="AlarmName", type=StringType)
AddAlarm.attributes={AddAlarm_AlarmName}

# ViewTemp_Smoke class attributes and methods
ViewTemp_Smoke_TempValue: Property = Property(name="TempValue", type=FloatType)
ViewTemp_Smoke_SmokeValue: Property = Property(name="SmokeValue", type=FloatType)
ViewTemp_Smoke.attributes={ViewTemp_Smoke_TempValue, ViewTemp_Smoke_SmokeValue}

# Alarm class attributes and methods
Alarm_AlarmID: Property = Property(name="AlarmID", type=StringType)
Alarm.attributes={Alarm_AlarmID}

# WebPage class attributes and methods
WebPage_People_: Property = Property(name="People_", type=IntegerType)
WebPage_OwnerData: Property = Property(name="OwnerData", type=StringType)
WebPage_SmokeValue: Property = Property(name="SmokeValue", type=FloatType)
WebPage_TempValue: Property = Property(name="TempValue", type=FloatType)
WebPage_HomeLoc: Property = Property(name="HomeLoc", type=StringType)
WebPage.attributes={WebPage_HomeLoc, WebPage_TempValue, WebPage_People_, WebPage_SmokeValue, WebPage_OwnerData}

# Notify_User_of_fire_external class attributes and methods

# Add_new_alarm_external class attributes and methods

# Disable_detector_external class attributes and methods

# Sense_and_Update_Data_external class attributes and methods

# View_sensors_data_external class attributes and methods

# Set_time_external class attributes and methods

# Relationships
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="system0", type=Arduino, multiplicity=Multiplicity(1, 1)),
        Property(name="sensor1", type=Sensor, multiplicity=Multiplicity(0, 9999))
    }
)
Home_Security_System_System: BinaryAssociation = BinaryAssociation(
    name="Home_Security_System_System",
    ends={
        Property(name="Home_Security_System_System_02", type=Firebase, multiplicity=Multiplicity(1, 1)),
        Property(name="Home_Security_System_System_13", type=MobileApp, multiplicity=Multiplicity(1, 1))
    }
)
Arduino__Firebase: BinaryAssociation = BinaryAssociation(
    name="Arduino__Firebase",
    ends={
        Property(name="Arduino__Firebase_04", type=Firebase, multiplicity=Multiplicity(1, 1)),
        Property(name="Arduino__Firebase_15", type=Arduino, multiplicity=Multiplicity(1, 1))
    }
)
Firebase_Web: BinaryAssociation = BinaryAssociation(
    name="Firebase_Web",
    ends={
        Property(name="Firebase_Web_06", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Firebase_Web_17", type=Firebase, multiplicity=Multiplicity(1, 1))
    }
)
Building_Owner__Sense_and_Update_Data: BinaryAssociation = BinaryAssociation(
    name="Building_Owner__Sense_and_Update_Data",
    ends={
        Property(name="sense_and_Update_Data8", type=Notify_User_of_fire_external, multiplicity=Multiplicity(0, 1)),
        Property(name="building_Owner9", type=Building_Owner__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Fire_Department__Notify_User: BinaryAssociation = BinaryAssociation(
    name="Fire_Department__Notify_User",
    ends={
        Property(name="notify_User10", type=Notify_User_of_fire_external, multiplicity=Multiplicity(0, 1)),
        Property(name="fire_Department11", type=Fire_Department__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Building_Owner__Add_Alarm: BinaryAssociation = BinaryAssociation(
    name="Building_Owner__Add_Alarm",
    ends={
        Property(name="add_Alarm12", type=Add_new_alarm_external, multiplicity=Multiplicity(0, 1)),
        Property(name="building_Owner13", type=Building_Owner__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Building_Owner__Close_Alarm: BinaryAssociation = BinaryAssociation(
    name="Building_Owner__Close_Alarm",
    ends={
        Property(name="close_Alarm14", type=Disable_detector_external, multiplicity=Multiplicity(0, 1)),
        Property(name="building_Owner15", type=Building_Owner__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sensors_Sense_and_Update_Data: BinaryAssociation = BinaryAssociation(
    name="Sensors_Sense_and_Update_Data",
    ends={
        Property(name="sense_and_Update_Data16", type=Sense_and_Update_Data_external, multiplicity=Multiplicity(0, 1)),
        Property(name="sensors17", type=Sensors_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Building_Owner__View_Data: BinaryAssociation = BinaryAssociation(
    name="Building_Owner__View_Data",
    ends={
        Property(name="view_Data18", type=View_sensors_data_external, multiplicity=Multiplicity(0, 1)),
        Property(name="building_Owner19", type=Building_Owner__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Notification_Alarm: BinaryAssociation = BinaryAssociation(
    name="Notification_Alarm",
    ends={
        Property(name="Notification_Alarm_020", type=Alarm, multiplicity=Multiplicity(1, 9999)),
        Property(name="Notification_Alarm_121", type=Notification, multiplicity=Multiplicity(1, 1))
    }
)
ViewTemp_Smoke_Alarm: BinaryAssociation = BinaryAssociation(
    name="ViewTemp_Smoke_Alarm",
    ends={
        Property(name="ViewTemp_Smoke_Alarm_022", type=Alarm, multiplicity=Multiplicity(1, 1)),
        Property(name="ViewTemp_Smoke_Alarm_123", type=ViewTemp_Smoke, multiplicity=Multiplicity(1, 1))
    }
)
AddAlarm_Alarm: BinaryAssociation = BinaryAssociation(
    name="AddAlarm_Alarm",
    ends={
        Property(name="AddAlarm_Alarm_024", type=Alarm, multiplicity=Multiplicity(1, 1)),
        Property(name="AddAlarm_Alarm_125", type=AddAlarm, multiplicity=Multiplicity(1, 1))
    }
)
TurnDownAlarm_Alarm: BinaryAssociation = BinaryAssociation(
    name="TurnDownAlarm_Alarm",
    ends={
        Property(name="TurnDownAlarm_Alarm_026", type=Alarm, multiplicity=Multiplicity(1, 1)),
        Property(name="TurnDownAlarm_Alarm_127", type=TurnDownAlarm, multiplicity=Multiplicity(1, 1))
    }
)
Alarm_Mobile_App: BinaryAssociation = BinaryAssociation(
    name="Alarm_Mobile_App",
    ends={
        Property(name="Alarm_Mobile_App_028", type=MobileApp, multiplicity=Multiplicity(1, 1)),
        Property(name="Alarm_Mobile_App_129", type=Alarm, multiplicity=Multiplicity(1, 9999))
    }
)
Building_Owner__Set_Time: BinaryAssociation = BinaryAssociation(
    name="Building_Owner__Set_Time",
    ends={
        Property(name="set_Time30", type=Set_time_external, multiplicity=Multiplicity(0, 1)),
        Property(name="building_Owner31", type=Building_Owner__Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_f2OkMPXQEemEXt2Xl4w_3Q",
    types={Firebase, Sensor, Gas_Smoke_Sensor, Temperature_Sensor, MobileApp, Notification, Count_Sensor, Arduino, Fire_Alarm_System__Component, Building_Owner__Actor, Fire_Department__Actor, Sensors_Actor, TurnDownAlarm, AddAlarm, ViewTemp_Smoke, Alarm, WebPage, Notify_User_of_fire_external, Add_new_alarm_external, Disable_detector_external, Sense_and_Update_Data_external, View_sensors_data_external, Set_time_external},
    associations={Sensor_System, Home_Security_System_System, Arduino__Firebase, Firebase_Web, Building_Owner__Sense_and_Update_Data, Fire_Department__Notify_User, Building_Owner__Add_Alarm, Building_Owner__Close_Alarm, Sensors_Sense_and_Update_Data, Building_Owner__View_Data, Notification_Alarm, ViewTemp_Smoke_Alarm, AddAlarm_Alarm, TurnDownAlarm_Alarm, Alarm_Mobile_App, Building_Owner__Set_Time},
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