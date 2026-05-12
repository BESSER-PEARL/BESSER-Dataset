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
Heat_Sensors_Actor = Class(name="Heat_Sensors_Actor")
Door_Sensors_Actor = Class(name="Door_Sensors_Actor")
Window_Sensors_Actor = Class(name="Window_Sensors_Actor")
Water_Sensors_Actor = Class(name="Water_Sensors_Actor")
Movement_Sensors_Actor = Class(name="Movement_Sensors_Actor")
User_Actor = Class(name="User_Actor")
Fire_Brigades_Actor = Class(name="Fire_Brigades_Actor")
Police_Station_Actor = Class(name="Police_Station_Actor")
Home_Safety_and_Security_System_Component = Class(name="Home_Safety_and_Security_System_Component")
mypackage_MyClass = Class(name="mypackage_MyClass")
mypackage_MyClass2 = Class(name="mypackage_MyClass2")
Idle = Class(name="Idle")
Smoke_Alarm_Activated = Class(name="Smoke_Alarm_Activated")
Fire_Alarm_Activated = Class(name="Fire_Alarm_Activated")
Detect_Smoke_external = Class(name="Detect_Smoke_external")
Detect_Excess_Heat_external = Class(name="Detect_Excess_Heat_external")
Smart_Sensor_Actor = Class(name="Smart_Sensor_Actor")
Smoke_Sensors_Actor = Class(name="Smoke_Sensors_Actor")
Detect_Water_external = Class(name="Detect_Water_external")
Stop_the_Alarm_external = Class(name="Stop_the_Alarm_external")
Change_Settings_external = Class(name="Change_Settings_external")
Enable_Disable_the_Burglar_Sensor_s__external = Class(name="Enable_Disable_the_Burglar_Sensor_s__external")
Reset_Alarm_s__external = Class(name="Reset_Alarm_s__external")
Receive_Fire_Alarm_Call_and_Handle_external = Class(name="Receive_Fire_Alarm_Call_and_Handle_external")
Receive_Burglar_Alarm_Call_and_Handle_external = Class(name="Receive_Burglar_Alarm_Call_and_Handle_external")
Send_Sensor_Type_Code_external = Class(name="Send_Sensor_Type_Code_external")
Monitor_Door_external = Class(name="Monitor_Door_external")
Monitor_Window_external = Class(name="Monitor_Window_external")
Detect_Movement_external = Class(name="Detect_Movement_external")

# Heat_Sensors_Actor class attributes and methods

# Door_Sensors_Actor class attributes and methods

# Window_Sensors_Actor class attributes and methods

# Water_Sensors_Actor class attributes and methods

# Movement_Sensors_Actor class attributes and methods

# User_Actor class attributes and methods

# Fire_Brigades_Actor class attributes and methods

# Police_Station_Actor class attributes and methods

# Home_Safety_and_Security_System_Component class attributes and methods

# mypackage_MyClass class attributes and methods

# mypackage_MyClass2 class attributes and methods

# Idle class attributes and methods

# Smoke_Alarm_Activated class attributes and methods

# Fire_Alarm_Activated class attributes and methods

# Detect_Smoke_external class attributes and methods

# Detect_Excess_Heat_external class attributes and methods

# Smart_Sensor_Actor class attributes and methods

# Smoke_Sensors_Actor class attributes and methods

# Detect_Water_external class attributes and methods

# Stop_the_Alarm_external class attributes and methods

# Change_Settings_external class attributes and methods

# Enable_Disable_the_Burglar_Sensor_s__external class attributes and methods

# Reset_Alarm_s__external class attributes and methods

# Receive_Fire_Alarm_Call_and_Handle_external class attributes and methods

# Receive_Burglar_Alarm_Call_and_Handle_external class attributes and methods

# Send_Sensor_Type_Code_external class attributes and methods

# Monitor_Door_external class attributes and methods

# Monitor_Window_external class attributes and methods

# Detect_Movement_external class attributes and methods

# Relationships
Smoke_Sensors_Detect_Smoke: BinaryAssociation = BinaryAssociation(
    name="Smoke_Sensors_Detect_Smoke",
    ends={
        Property(name="detect_Smoke0", type=Detect_Smoke_external, multiplicity=Multiplicity(0, 1)),
        Property(name="smoke_Sensors1", type=Smoke_Sensors_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Heat_Sensors_Detect_Excess_Heat: BinaryAssociation = BinaryAssociation(
    name="Heat_Sensors_Detect_Excess_Heat",
    ends={
        Property(name="detect_Excess_Heat2", type=Detect_Excess_Heat_external, multiplicity=Multiplicity(0, 1)),
        Property(name="heat_Sensors3", type=Heat_Sensors_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Movement_Sensors_Detect_Movement: BinaryAssociation = BinaryAssociation(
    name="Movement_Sensors_Detect_Movement",
    ends={
        Property(name="detect_Movement8", type=Detect_Movement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="movement_Sensors9", type=Movement_Sensors_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Water_Sensors_Detect_Water: BinaryAssociation = BinaryAssociation(
    name="Water_Sensors_Detect_Water",
    ends={
        Property(name="detect_Water10", type=Detect_Water_external, multiplicity=Multiplicity(0, 1)),
        Property(name="water_Sensors11", type=Water_Sensors_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Stop_the_Alarm: BinaryAssociation = BinaryAssociation(
    name="User_Stop_the_Alarm",
    ends={
        Property(name="stop_the_Alarm12", type=Stop_the_Alarm_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Change_Settings: BinaryAssociation = BinaryAssociation(
    name="User_Change_Settings",
    ends={
        Property(name="change_Settings14", type=Change_Settings_external, multiplicity=Multiplicity(0, 1)),
        Property(name="user15", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Enable_Disable_the_Sensor_s_: BinaryAssociation = BinaryAssociation(
    name="User_Enable_Disable_the_Sensor_s_",
    ends={
        Property(name="enable_Disable_the_Sensor_s_16", type=Enable_Disable_the_Burglar_Sensor_s__external, multiplicity=Multiplicity(0, 1)),
        Property(name="user17", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Reset_Burglar_Alarm: BinaryAssociation = BinaryAssociation(
    name="User_Reset_Burglar_Alarm",
    ends={
        Property(name="reset_Burglar_Alarm18", type=Reset_Alarm_s__external, multiplicity=Multiplicity(0, 1)),
        Property(name="user19", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Receive_Fire_Alarm_Fire_Brigades: BinaryAssociation = BinaryAssociation(
    name="Receive_Fire_Alarm_Fire_Brigades",
    ends={
        Property(name="fire_Brigades20", type=Fire_Brigades_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="receive_Fire_Alarm21", type=Receive_Fire_Alarm_Call_and_Handle_external, multiplicity=Multiplicity(0, 1))
    }
)
Receive_Burglar_Call_Police_Station: BinaryAssociation = BinaryAssociation(
    name="Receive_Burglar_Call_Police_Station",
    ends={
        Property(name="police_Station22", type=Police_Station_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="receive_Burglar_Call23", type=Receive_Burglar_Alarm_Call_and_Handle_external, multiplicity=Multiplicity(0, 1))
    }
)
Smart_Sensor_Send_Sensor_Type_Code: BinaryAssociation = BinaryAssociation(
    name="Smart_Sensor_Send_Sensor_Type_Code",
    ends={
        Property(name="send_Sensor_Type_Code24", type=Send_Sensor_Type_Code_external, multiplicity=Multiplicity(0, 1)),
        Property(name="smart_Sensor25", type=Smart_Sensor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
MyClass_MyClass2: BinaryAssociation = BinaryAssociation(
    name="MyClass_MyClass2",
    ends={
        Property(name="myClass226", type=mypackage_MyClass2, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass27", type=mypackage_MyClass, multiplicity=Multiplicity(0, 1))
    }
)
Door_Sensors_Monitor_Door: BinaryAssociation = BinaryAssociation(
    name="Door_Sensors_Monitor_Door",
    ends={
        Property(name="monitor_Door4", type=Monitor_Door_external, multiplicity=Multiplicity(0, 1)),
        Property(name="door_Sensors5", type=Door_Sensors_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Window_Sensors_Monitor_Window: BinaryAssociation = BinaryAssociation(
    name="Window_Sensors_Monitor_Window",
    ends={
        Property(name="monitor_Window6", type=Monitor_Window_external, multiplicity=Multiplicity(0, 1)),
        Property(name="window_Sensors7", type=Window_Sensors_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_hOaKkL1kEeedTfUoC_GfaA",
    types={Heat_Sensors_Actor, Door_Sensors_Actor, Window_Sensors_Actor, Water_Sensors_Actor, Movement_Sensors_Actor, User_Actor, Fire_Brigades_Actor, Police_Station_Actor, Home_Safety_and_Security_System_Component, mypackage_MyClass, mypackage_MyClass2, Idle, Smoke_Alarm_Activated, Fire_Alarm_Activated, Detect_Smoke_external, Detect_Excess_Heat_external, Smart_Sensor_Actor, Smoke_Sensors_Actor, Detect_Water_external, Stop_the_Alarm_external, Change_Settings_external, Enable_Disable_the_Burglar_Sensor_s__external, Reset_Alarm_s__external, Receive_Fire_Alarm_Call_and_Handle_external, Receive_Burglar_Alarm_Call_and_Handle_external, Send_Sensor_Type_Code_external, Monitor_Door_external, Monitor_Window_external, Detect_Movement_external},
    associations={Smoke_Sensors_Detect_Smoke, Heat_Sensors_Detect_Excess_Heat, Movement_Sensors_Detect_Movement, Water_Sensors_Detect_Water, User_Stop_the_Alarm, User_Change_Settings, User_Enable_Disable_the_Sensor_s_, User_Reset_Burglar_Alarm, Receive_Fire_Alarm_Fire_Brigades, Receive_Burglar_Call_Police_Station, Smart_Sensor_Send_Sensor_Type_Code, MyClass_MyClass2, Door_Sensors_Monitor_Door, Window_Sensors_Monitor_Window},
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