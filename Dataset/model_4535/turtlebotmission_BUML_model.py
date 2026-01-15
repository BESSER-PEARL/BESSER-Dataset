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
turtlebotmission_TurtleBot = Class(name="turtlebotmission::TurtleBot")
NamedElement = Class(name="NamedElement")
turtlebotmission_Area = Class(name="turtlebotmission::Area")
turtlebotmission_WaypointType = Class(name="turtlebotmission::WaypointType")
turtlebotmission_WayPoint = Class(name="turtlebotmission::WayPoint")
turtlebotmission_Mission = Class(name="turtlebotmission::Mission")
turtlebotmission_NamedElement = Class(name="turtlebotmission::NamedElement", is_abstract=True)
turtlebotmission_ShortestPathTask = Class(name="turtlebotmission::ShortestPathTask")
turtlebotmission_ReturnToStartTask = Class(name="turtlebotmission::ReturnToStartTask")
turtlebotmission_Task = Class(name="turtlebotmission::Task", is_abstract=True)
turtlebotmission_LineTask = Class(name="turtlebotmission::LineTask")
Task = Class(name="Task")

# turtlebotmission_TurtleBot class attributes and methods

# NamedElement class attributes and methods

# turtlebotmission_Area class attributes and methods
turtlebotmission_Area_xmax: Property = Property(name="xmax", type=IntegerType)
turtlebotmission_Area_ymax: Property = Property(name="ymax", type=IntegerType)
turtlebotmission_Area.attributes={turtlebotmission_Area_xmax, turtlebotmission_Area_ymax}

# turtlebotmission_WaypointType class attributes and methods

# turtlebotmission_WayPoint class attributes and methods
turtlebotmission_WayPoint_coord_x: Property = Property(name="coord_x", type=IntegerType)
turtlebotmission_WayPoint_coord_y: Property = Property(name="coord_y", type=IntegerType)
turtlebotmission_WayPoint.attributes={turtlebotmission_WayPoint_coord_y, turtlebotmission_WayPoint_coord_x}

# turtlebotmission_Mission class attributes and methods

# turtlebotmission_NamedElement class attributes and methods
turtlebotmission_NamedElement_name: Property = Property(name="name", type=StringType)
turtlebotmission_NamedElement.attributes={turtlebotmission_NamedElement_name}

# turtlebotmission_ShortestPathTask class attributes and methods

# turtlebotmission_ReturnToStartTask class attributes and methods

# turtlebotmission_Task class attributes and methods

# turtlebotmission_LineTask class attributes and methods

# Task class attributes and methods

# Relationships
area0: BinaryAssociation = BinaryAssociation(
    name="area0",
    ends={
        Property(name="turtlebotmission_Area", type=turtlebotmission_TurtleBot, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_TurtleBot", type=turtlebotmission_Area, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
waypointtypes1: BinaryAssociation = BinaryAssociation(
    name="waypointtypes1",
    ends={
        Property(name="turtlebotmission_WaypointType", type=turtlebotmission_TurtleBot, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_TurtleBot2", type=turtlebotmission_WaypointType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bot_start3: BinaryAssociation = BinaryAssociation(
    name="bot_start3",
    ends={
        Property(name="turtlebotmission_WayPoint", type=turtlebotmission_TurtleBot, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_TurtleBot4", type=turtlebotmission_WayPoint, multiplicity=Multiplicity(1, 1))
    }
)
waypoints5: BinaryAssociation = BinaryAssociation(
    name="waypoints5",
    ends={
        Property(name="turtlebotmission_WayPoint7", type=turtlebotmission_TurtleBot, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_TurtleBot6", type=turtlebotmission_WayPoint, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
missions8: BinaryAssociation = BinaryAssociation(
    name="missions8",
    ends={
        Property(name="turtlebotmission_Mission", type=turtlebotmission_TurtleBot, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_TurtleBot9", type=turtlebotmission_Mission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
waypoints15: BinaryAssociation = BinaryAssociation(
    name="waypoints15",
    ends={
        Property(name="turtlebotmission_WayPoint16", type=turtlebotmission_LineTask, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_LineTask", type=turtlebotmission_WayPoint, multiplicity=Multiplicity(1, 9999))
    }
)
waypoints17: BinaryAssociation = BinaryAssociation(
    name="waypoints17",
    ends={
        Property(name="turtlebotmission_WayPoint18", type=turtlebotmission_ShortestPathTask, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_ShortestPathTask", type=turtlebotmission_WayPoint, multiplicity=Multiplicity(1, 9999))
    }
)
waypointtypes10: BinaryAssociation = BinaryAssociation(
    name="waypointtypes10",
    ends={
        Property(name="turtlebotmission_WaypointType12", type=turtlebotmission_WayPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_WayPoint11", type=turtlebotmission_WaypointType, multiplicity=Multiplicity(1, 9999))
    }
)
task13: BinaryAssociation = BinaryAssociation(
    name="task13",
    ends={
        Property(name="turtlebotmission_Task", type=turtlebotmission_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="turtlebotmission_Mission14", type=turtlebotmission_Task, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_turtlebotmission_TurtleBot_NamedElement = Generalization(general=NamedElement, specific=turtlebotmission_TurtleBot)
gen_turtlebotmission_ShortestPathTask_Task = Generalization(general=Task, specific=turtlebotmission_ShortestPathTask)
gen_turtlebotmission_ReturnToStartTask_Task = Generalization(general=Task, specific=turtlebotmission_ReturnToStartTask)
gen_turtlebotmission_WaypointType_NamedElement = Generalization(general=NamedElement, specific=turtlebotmission_WaypointType)
gen_turtlebotmission_WayPoint_NamedElement = Generalization(general=NamedElement, specific=turtlebotmission_WayPoint)
gen_turtlebotmission_Mission_NamedElement = Generalization(general=NamedElement, specific=turtlebotmission_Mission)
gen_turtlebotmission_LineTask_Task = Generalization(general=Task, specific=turtlebotmission_LineTask)

# Domain Model
domain_model = DomainModel(
    name="turtlebotmission",
    types={turtlebotmission_TurtleBot, NamedElement, turtlebotmission_Area, turtlebotmission_WaypointType, turtlebotmission_WayPoint, turtlebotmission_Mission, turtlebotmission_NamedElement, turtlebotmission_ShortestPathTask, turtlebotmission_ReturnToStartTask, turtlebotmission_Task, turtlebotmission_LineTask, Task},
    associations={area0, waypointtypes1, bot_start3, waypoints5, missions8, waypoints15, waypoints17, waypointtypes10, task13},
    generalizations={gen_turtlebotmission_TurtleBot_NamedElement, gen_turtlebotmission_ShortestPathTask_Task, gen_turtlebotmission_ReturnToStartTask_Task, gen_turtlebotmission_WaypointType_NamedElement, gen_turtlebotmission_WayPoint_NamedElement, gen_turtlebotmission_Mission_NamedElement, gen_turtlebotmission_LineTask_Task},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)