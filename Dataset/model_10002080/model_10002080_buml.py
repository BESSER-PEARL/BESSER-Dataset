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
Emergency_Services_Actor = Class(name="Emergency_Services_Actor")
Window_Sensor_Actor = Class(name="Window_Sensor_Actor")
Door_Sensor_Actor = Class(name="Door_Sensor_Actor")
Movement_Sensor_Actor = Class(name="Movement_Sensor_Actor")
Smoke_Sensor_Actor = Class(name="Smoke_Sensor_Actor")
Heat_Sensor_Actor = Class(name="Heat_Sensor_Actor")
Police_Actor = Class(name="Police_Actor")
Fire_Brigade_Actor = Class(name="Fire_Brigade_Actor")
Alarm_System_Component = Class(name="Alarm_System_Component")
T = Class(name="T")
Call_Fire_Brigade_external = Class(name="Call_Fire_Brigade_external")
Detect_Movement_external = Class(name="Detect_Movement_external")
Detect_Smoke_external = Class(name="Detect_Smoke_external")
Detect_Heat_external = Class(name="Detect_Heat_external")

# Emergency_Services_Actor class attributes and methods

# Window_Sensor_Actor class attributes and methods

# Door_Sensor_Actor class attributes and methods

# Movement_Sensor_Actor class attributes and methods

# Smoke_Sensor_Actor class attributes and methods

# Heat_Sensor_Actor class attributes and methods

# Police_Actor class attributes and methods

# Fire_Brigade_Actor class attributes and methods

# Alarm_System_Component class attributes and methods

# T class attributes and methods

# Call_Fire_Brigade_external class attributes and methods

# Detect_Movement_external class attributes and methods

# Detect_Smoke_external class attributes and methods

# Detect_Heat_external class attributes and methods

# Relationships
Call_Fire_Brigade_Emergency_Services: BinaryAssociation = BinaryAssociation(
    name="Call_Fire_Brigade_Emergency_Services",
    ends={
        Property(name="emergency_Services0", type=Emergency_Services_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="call_Fire_Brigade1", type=Call_Fire_Brigade_external, multiplicity=Multiplicity(0, 1))
    }
)
Window_Sensor_Detect_Movement: BinaryAssociation = BinaryAssociation(
    name="Window_Sensor_Detect_Movement",
    ends={
        Property(name="detect_Movement2", type=Detect_Movement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="window_Sensor3", type=Window_Sensor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Door_Sensor_Detect_Movement: BinaryAssociation = BinaryAssociation(
    name="Door_Sensor_Detect_Movement",
    ends={
        Property(name="detect_Movement4", type=Detect_Movement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="door_Sensor5", type=Door_Sensor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Movement_Sensor_Detect_Movement: BinaryAssociation = BinaryAssociation(
    name="Movement_Sensor_Detect_Movement",
    ends={
        Property(name="detect_Movement6", type=Detect_Movement_external, multiplicity=Multiplicity(0, 1)),
        Property(name="movement_Sensor7", type=Movement_Sensor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Smoke_Sensor_Detect_Smoke: BinaryAssociation = BinaryAssociation(
    name="Smoke_Sensor_Detect_Smoke",
    ends={
        Property(name="detect_Smoke8", type=Detect_Smoke_external, multiplicity=Multiplicity(0, 1)),
        Property(name="smoke_Sensor9", type=Smoke_Sensor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Heat_Sensor_Detect_Heat: BinaryAssociation = BinaryAssociation(
    name="Heat_Sensor_Detect_Heat",
    ends={
        Property(name="detect_Heat10", type=Detect_Heat_external, multiplicity=Multiplicity(0, 1)),
        Property(name="heat_Sensor11", type=Heat_Sensor_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_nIm3ILiNEee7sYPkE4_GPA",
    types={Emergency_Services_Actor, Window_Sensor_Actor, Door_Sensor_Actor, Movement_Sensor_Actor, Smoke_Sensor_Actor, Heat_Sensor_Actor, Police_Actor, Fire_Brigade_Actor, Alarm_System_Component, T, Call_Fire_Brigade_external, Detect_Movement_external, Detect_Smoke_external, Detect_Heat_external},
    associations={Call_Fire_Brigade_Emergency_Services, Window_Sensor_Detect_Movement, Door_Sensor_Detect_Movement, Movement_Sensor_Detect_Movement, Smoke_Sensor_Detect_Smoke, Heat_Sensor_Detect_Heat},
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