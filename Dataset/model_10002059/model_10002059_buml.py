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
Change_Password_external = Class(name="Change_Password_external")
Enable_Disable_Sensor_external = Class(name="Enable_Disable_Sensor_external")
Change_Settings_external = Class(name="Change_Settings_external")
Set_time_on_burglar_sensors_external = Class(name="Set_time_on_burglar_sensors_external")
Reset_Alarm_external = Class(name="Reset_Alarm_external")
HomeOwner_Actor = Class(name="HomeOwner_Actor")
Smoke_Sensor_Actor = Class(name="Smoke_Sensor_Actor")
Home_safety_and_security_system_Component = Class(name="Home_safety_and_security_system_Component")
T = Class(name="T")
Heat_Sensor_Actor = Class(name="Heat_Sensor_Actor")
Water_Sensor_Actor = Class(name="Water_Sensor_Actor")
Door_Sensor_Actor = Class(name="Door_Sensor_Actor")
Window_Sensor_Actor = Class(name="Window_Sensor_Actor")
Movement_Sensor_Actor = Class(name="Movement_Sensor_Actor")
Detected_external = Class(name="Detected_external")

# Change_Password_external class attributes and methods

# Enable_Disable_Sensor_external class attributes and methods

# Change_Settings_external class attributes and methods

# Set_time_on_burglar_sensors_external class attributes and methods

# Reset_Alarm_external class attributes and methods

# HomeOwner_Actor class attributes and methods

# Smoke_Sensor_Actor class attributes and methods

# Home_safety_and_security_system_Component class attributes and methods

# T class attributes and methods

# Heat_Sensor_Actor class attributes and methods

# Water_Sensor_Actor class attributes and methods

# Door_Sensor_Actor class attributes and methods

# Window_Sensor_Actor class attributes and methods

# Movement_Sensor_Actor class attributes and methods

# Detected_external class attributes and methods

# Relationships
Detected_Water_Sensor: BinaryAssociation = BinaryAssociation(
    name="Detected_Water_Sensor",
    ends={
        Property(name="water_Sensor2", type=Water_Sensor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="detected3", type=Detected_external, multiplicity=Multiplicity(0, 1))
    }
)
Detected_Heat_Sensor: BinaryAssociation = BinaryAssociation(
    name="Detected_Heat_Sensor",
    ends={
        Property(name="heat_Sensor4", type=Heat_Sensor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="detected5", type=Detected_external, multiplicity=Multiplicity(0, 1))
    }
)
HomeOwner_Change_Password: BinaryAssociation = BinaryAssociation(
    name="HomeOwner_Change_Password",
    ends={
        Property(name="change_Password6", type=Change_Password_external, multiplicity=Multiplicity(0, 1)),
        Property(name="homeOwner7", type=HomeOwner_Actor, multiplicity=Multiplicity(0, 1))
    }
)
HomeOwner_Enable_Disable_Sensor: BinaryAssociation = BinaryAssociation(
    name="HomeOwner_Enable_Disable_Sensor",
    ends={
        Property(name="enable_Disable_Sensor8", type=Enable_Disable_Sensor_external, multiplicity=Multiplicity(0, 1)),
        Property(name="homeOwner9", type=HomeOwner_Actor, multiplicity=Multiplicity(0, 1))
    }
)
HomeOwner_Change_Settings: BinaryAssociation = BinaryAssociation(
    name="HomeOwner_Change_Settings",
    ends={
        Property(name="change_Settings10", type=Change_Settings_external, multiplicity=Multiplicity(0, 1)),
        Property(name="homeOwner11", type=HomeOwner_Actor, multiplicity=Multiplicity(0, 1))
    }
)
HomeOwner_Set_time_on_burglar_sensors: BinaryAssociation = BinaryAssociation(
    name="HomeOwner_Set_time_on_burglar_sensors",
    ends={
        Property(name="set_time_on_burglar_sensors12", type=Set_time_on_burglar_sensors_external, multiplicity=Multiplicity(0, 1)),
        Property(name="homeOwner13", type=HomeOwner_Actor, multiplicity=Multiplicity(0, 1))
    }
)
HomeOwner_Reset_Alarm: BinaryAssociation = BinaryAssociation(
    name="HomeOwner_Reset_Alarm",
    ends={
        Property(name="reset_Alarm14", type=Reset_Alarm_external, multiplicity=Multiplicity(0, 1)),
        Property(name="homeOwner15", type=HomeOwner_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Detected_Movement_Sensor: BinaryAssociation = BinaryAssociation(
    name="Detected_Movement_Sensor",
    ends={
        Property(name="movement_Sensor0", type=Movement_Sensor_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="detected1", type=Detected_external, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_m7eqgLTyEee7sYPkE4_GPA",
    types={Change_Password_external, Enable_Disable_Sensor_external, Change_Settings_external, Set_time_on_burglar_sensors_external, Reset_Alarm_external, HomeOwner_Actor, Smoke_Sensor_Actor, Home_safety_and_security_system_Component, T, Heat_Sensor_Actor, Water_Sensor_Actor, Door_Sensor_Actor, Window_Sensor_Actor, Movement_Sensor_Actor, Detected_external},
    associations={Detected_Water_Sensor, Detected_Heat_Sensor, HomeOwner_Change_Password, HomeOwner_Enable_Disable_Sensor, HomeOwner_Change_Settings, HomeOwner_Set_time_on_burglar_sensors, HomeOwner_Reset_Alarm, Detected_Movement_Sensor},
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