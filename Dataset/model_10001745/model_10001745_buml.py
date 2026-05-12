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
Gas_SmokeSensor = Class(name="Gas_SmokeSensor")
TemperatureSensor = Class(name="TemperatureSensor")
MobileApp = Class(name="MobileApp")
CountSensor = Class(name="CountSensor")
Arduino = Class(name="Arduino")
Web = Class(name="Web")
Fire_Alarm_System__Component = Class(name="Fire_Alarm_System__Component")
Building_Owner__Actor = Class(name="Building_Owner__Actor")
Fire_Department__Actor = Class(name="Fire_Department__Actor")
Sensors_Actor = Class(name="Sensors_Actor")
Notify_User_of_fire_external = Class(name="Notify_User_of_fire_external")
Add_new_alarm_external = Class(name="Add_new_alarm_external")
Close_Alarm_external = Class(name="Close_Alarm_external")
Sense_and_Update_Data_external = Class(name="Sense_and_Update_Data_external")
View_sensors_data_external = Class(name="View_sensors_data_external")

# Firebase class attributes and methods

# Sensor class attributes and methods

# Gas_SmokeSensor class attributes and methods

# TemperatureSensor class attributes and methods

# MobileApp class attributes and methods

# CountSensor class attributes and methods

# Arduino class attributes and methods

# Web class attributes and methods

# Fire_Alarm_System__Component class attributes and methods

# Building_Owner__Actor class attributes and methods

# Fire_Department__Actor class attributes and methods

# Sensors_Actor class attributes and methods

# Notify_User_of_fire_external class attributes and methods

# Add_new_alarm_external class attributes and methods

# Close_Alarm_external class attributes and methods

# Sense_and_Update_Data_external class attributes and methods

# View_sensors_data_external class attributes and methods

# Relationships
Sensor_System: BinaryAssociation = BinaryAssociation(
    name="Sensor_System",
    ends={
        Property(name="sensor1", type=Sensor, multiplicity=Multiplicity(1, 9999)),
        Property(name="system0", type=Arduino, multiplicity=Multiplicity(1, 1))
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
        Property(name="Firebase_Web_06", type=Web, multiplicity=Multiplicity(0, 1)),
        Property(name="Firebase_Web_17", type=Firebase, multiplicity=Multiplicity(0, 1))
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
        Property(name="close_Alarm14", type=Close_Alarm_external, multiplicity=Multiplicity(0, 1)),
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

# Domain Model
domain_model = DomainModel(
    name="_SVaK4PXNEemEXt2Xl4w_3Q",
    types={Firebase, Sensor, Gas_SmokeSensor, TemperatureSensor, MobileApp, CountSensor, Arduino, Web, Fire_Alarm_System__Component, Building_Owner__Actor, Fire_Department__Actor, Sensors_Actor, Notify_User_of_fire_external, Add_new_alarm_external, Close_Alarm_external, Sense_and_Update_Data_external, View_sensors_data_external},
    associations={Sensor_System, Home_Security_System_System, Arduino__Firebase, Firebase_Web, Building_Owner__Sense_and_Update_Data, Fire_Department__Notify_User, Building_Owner__Add_Alarm, Building_Owner__Close_Alarm, Sensors_Sense_and_Update_Data, Building_Owner__View_Data},
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