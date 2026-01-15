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
mission_NamedElement = Class(name="mission::NamedElement", is_abstract=True)
mission_Mission = Class(name="mission::Mission")
NamedElement = Class(name="NamedElement")
mission_Task = Class(name="mission::Task", is_abstract=True)
mission_TaskDependency = Class(name="mission::TaskDependency")
mission_Swarm = Class(name="mission::Swarm")
mission_Drone = Class(name="mission::Drone")
mission_Coordinate = Class(name="mission::Coordinate")
mission_ControlTask = Class(name="mission::ControlTask", is_abstract=True)
Task = Class(name="Task")
mission_PolygonTask = Class(name="mission::PolygonTask", is_abstract=True)
mission_PointTask = Class(name="mission::PointTask", is_abstract=True)
mission_LineTask = Class(name="mission::LineTask", is_abstract=True)
mission_Fork = Class(name="mission::Fork")
ControlTask = Class(name="ControlTask")
mission_Join = Class(name="mission::Join")

# mission_NamedElement class attributes and methods
mission_NamedElement_name: Property = Property(name="name", type=StringType)
mission_NamedElement.attributes={mission_NamedElement_name}

# mission_Mission class attributes and methods
mission_Mission_crs: Property = Property(name="crs", type=StringType)
mission_Mission.attributes={mission_Mission_crs}

# NamedElement class attributes and methods

# mission_Task class attributes and methods

# mission_TaskDependency class attributes and methods

# mission_Swarm class attributes and methods

# mission_Drone class attributes and methods
mission_Drone_type: Property = Property(name="type", type=StringType)
mission_Drone_returnHome: Property = Property(name="returnHome", type=BooleanType)
mission_Drone.attributes={mission_Drone_returnHome, mission_Drone_type}

# mission_Coordinate class attributes and methods
mission_Coordinate_latitude: Property = Property(name="latitude", type=FloatType)
mission_Coordinate_longitude: Property = Property(name="longitude", type=FloatType)
mission_Coordinate_altitude: Property = Property(name="altitude", type=FloatType)
mission_Coordinate.attributes={mission_Coordinate_longitude, mission_Coordinate_altitude, mission_Coordinate_latitude}

# mission_ControlTask class attributes and methods

# Task class attributes and methods

# mission_PolygonTask class attributes and methods

# mission_PointTask class attributes and methods

# mission_LineTask class attributes and methods

# mission_Fork class attributes and methods

# ControlTask class attributes and methods

# mission_Join class attributes and methods

# Relationships
tasks0: BinaryAssociation = BinaryAssociation(
    name="tasks0",
    ends={
        Property(name="mission_Task", type=mission_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_Mission", type=mission_Task, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
taskDependencies1: BinaryAssociation = BinaryAssociation(
    name="taskDependencies1",
    ends={
        Property(name="mission_TaskDependency", type=mission_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_Mission2", type=mission_TaskDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
swarm3: BinaryAssociation = BinaryAssociation(
    name="swarm3",
    ends={
        Property(name="mission_Swarm", type=mission_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_Mission4", type=mission_Swarm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
drones5: BinaryAssociation = BinaryAssociation(
    name="drones5",
    ends={
        Property(name="mission_Drone", type=mission_Swarm, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_Swarm6", type=mission_Drone, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
home7: BinaryAssociation = BinaryAssociation(
    name="home7",
    ends={
        Property(name="mission_Coordinate", type=mission_Drone, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_Drone8", type=mission_Coordinate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from11: BinaryAssociation = BinaryAssociation(
    name="from11",
    ends={
        Property(name="mission_Task13", type=mission_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_TaskDependency12", type=mission_Task, multiplicity=Multiplicity(1, 1))
    }
)
to14: BinaryAssociation = BinaryAssociation(
    name="to14",
    ends={
        Property(name="mission_Task16", type=mission_TaskDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_TaskDependency15", type=mission_Task, multiplicity=Multiplicity(1, 1))
    }
)
shell17: BinaryAssociation = BinaryAssociation(
    name="shell17",
    ends={
        Property(name="mission_Coordinate18", type=mission_PolygonTask, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_PolygonTask", type=mission_Coordinate, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
initialPosition19: BinaryAssociation = BinaryAssociation(
    name="initialPosition19",
    ends={
        Property(name="mission_Coordinate21", type=mission_PolygonTask, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_PolygonTask20", type=mission_Coordinate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
point22: BinaryAssociation = BinaryAssociation(
    name="point22",
    ends={
        Property(name="mission_Coordinate23", type=mission_PointTask, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_PointTask", type=mission_Coordinate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
points24: BinaryAssociation = BinaryAssociation(
    name="points24",
    ends={
        Property(name="mission_Coordinate25", type=mission_LineTask, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_LineTask", type=mission_Coordinate, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialPosition26: BinaryAssociation = BinaryAssociation(
    name="initialPosition26",
    ends={
        Property(name="mission_Coordinate28", type=mission_LineTask, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_LineTask27", type=mission_Coordinate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencePosition9: BinaryAssociation = BinaryAssociation(
    name="referencePosition9",
    ends={
        Property(name="mission_Coordinate10", type=mission_ControlTask, multiplicity=Multiplicity(1, 1)),
        Property(name="mission_ControlTask", type=mission_Coordinate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_mission_Mission_NamedElement = Generalization(general=NamedElement, specific=mission_Mission)
gen_mission_Drone_NamedElement = Generalization(general=NamedElement, specific=mission_Drone)
gen_mission_Task_NamedElement = Generalization(general=NamedElement, specific=mission_Task)
gen_mission_ControlTask_Task = Generalization(general=Task, specific=mission_ControlTask)
gen_mission_TaskDependency_NamedElement = Generalization(general=NamedElement, specific=mission_TaskDependency)
gen_mission_PolygonTask_Task = Generalization(general=Task, specific=mission_PolygonTask)
gen_mission_PointTask_Task = Generalization(general=Task, specific=mission_PointTask)
gen_mission_LineTask_Task = Generalization(general=Task, specific=mission_LineTask)
gen_mission_Fork_ControlTask = Generalization(general=ControlTask, specific=mission_Fork)
gen_mission_Join_ControlTask = Generalization(general=ControlTask, specific=mission_Join)

# Domain Model
domain_model = DomainModel(
    name="mission",
    types={mission_NamedElement, mission_Mission, NamedElement, mission_Task, mission_TaskDependency, mission_Swarm, mission_Drone, mission_Coordinate, mission_ControlTask, Task, mission_PolygonTask, mission_PointTask, mission_LineTask, mission_Fork, ControlTask, mission_Join},
    associations={tasks0, taskDependencies1, swarm3, drones5, home7, from11, to14, shell17, initialPosition19, point22, points24, initialPosition26, referencePosition9},
    generalizations={gen_mission_Mission_NamedElement, gen_mission_Drone_NamedElement, gen_mission_Task_NamedElement, gen_mission_ControlTask_Task, gen_mission_TaskDependency_NamedElement, gen_mission_PolygonTask_Task, gen_mission_PointTask_Task, gen_mission_LineTask_Task, gen_mission_Fork_ControlTask, gen_mission_Join_ControlTask},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)