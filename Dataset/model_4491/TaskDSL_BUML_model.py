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

# Enumerations
Object: Enumeration = Enumeration(
    name="Object",
    literals={
            EnumerationLiteral(name="ROCK"),
			EnumerationLiteral(name="LAKE")
    }
)

Speed: Enumeration = Enumeration(
    name="Speed",
    literals={
            EnumerationLiteral(name="FAST"),
			EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="SLOW")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE")
    }
)

# Classes
taskDSL_Task = Class(name="taskDSL::Task")
taskDSL_Action = Class(name="taskDSL::Action")
taskDSL_Detector = Class(name="taskDSL::Detector")
taskDSL_Avoid = Class(name="taskDSL::Avoid")
taskDSL_DriveUntil = Class(name="taskDSL::DriveUntil")
Action = Class(name="Action")
taskDSL_Investigate = Class(name="taskDSL::Investigate")
taskDSL_Speak = Class(name="taskDSL::Speak")
taskDSL_FollowLine = Class(name="taskDSL::FollowLine")
taskDSL_DSL = Class(name="taskDSL::DSL")
taskDSL_Mission = Class(name="taskDSL::Mission")
taskDSL_DriveAction = Class(name="taskDSL::DriveAction")
taskDSL_MoveBack = Class(name="taskDSL::MoveBack")
DriveAction = Class(name="DriveAction")
taskDSL_TurnLeft = Class(name="taskDSL::TurnLeft")
taskDSL_TurnRight = Class(name="taskDSL::TurnRight")

# taskDSL_Task class attributes and methods
taskDSL_Task_name: Property = Property(name="name", type=StringType)
taskDSL_Task.attributes={taskDSL_Task_name}

# taskDSL_Action class attributes and methods

# taskDSL_Detector class attributes and methods

# taskDSL_Avoid class attributes and methods
taskDSL_Avoid_color: Property = Property(name="color", type=StringType)
taskDSL_Avoid_object: Property = Property(name="object", type=StringType)
taskDSL_Avoid.attributes={taskDSL_Avoid_color, taskDSL_Avoid_object}

# taskDSL_DriveUntil class attributes and methods
taskDSL_DriveUntil_speed: Property = Property(name="speed", type=StringType)
taskDSL_DriveUntil_color: Property = Property(name="color", type=StringType)
taskDSL_DriveUntil_object: Property = Property(name="object", type=StringType)
taskDSL_DriveUntil.attributes={taskDSL_DriveUntil_object, taskDSL_DriveUntil_color, taskDSL_DriveUntil_speed}

# Action class attributes and methods

# taskDSL_Investigate class attributes and methods
taskDSL_Investigate_speed: Property = Property(name="speed", type=StringType)
taskDSL_Investigate.attributes={taskDSL_Investigate_speed}

# taskDSL_Speak class attributes and methods
taskDSL_Speak_text: Property = Property(name="text", type=StringType)
taskDSL_Speak.attributes={taskDSL_Speak_text}

# taskDSL_FollowLine class attributes and methods
taskDSL_FollowLine_distance: Property = Property(name="distance", type=IntegerType)
taskDSL_FollowLine.attributes={taskDSL_FollowLine_distance}

# taskDSL_DSL class attributes and methods

# taskDSL_Mission class attributes and methods
taskDSL_Mission_name: Property = Property(name="name", type=StringType)
taskDSL_Mission.attributes={taskDSL_Mission_name}

# taskDSL_DriveAction class attributes and methods

# taskDSL_MoveBack class attributes and methods
taskDSL_MoveBack_meters: Property = Property(name="meters", type=IntegerType)
taskDSL_MoveBack.attributes={taskDSL_MoveBack_meters}

# DriveAction class attributes and methods

# taskDSL_TurnLeft class attributes and methods
taskDSL_TurnLeft_degrees: Property = Property(name="degrees", type=IntegerType)
taskDSL_TurnLeft.attributes={taskDSL_TurnLeft_degrees}

# taskDSL_TurnRight class attributes and methods
taskDSL_TurnRight_degrees: Property = Property(name="degrees", type=IntegerType)
taskDSL_TurnRight.attributes={taskDSL_TurnRight_degrees}

# Relationships
missions0: BinaryAssociation = BinaryAssociation(
    name="missions0",
    ends={
        Property(name="taskDSL_DSL", type=taskDSL_Mission, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="taskDSL_Mission", type=taskDSL_DSL, multiplicity=Multiplicity(1, 1))
    }
)
tasks1: BinaryAssociation = BinaryAssociation(
    name="tasks1",
    ends={
        Property(name="taskDSL_Task", type=taskDSL_DSL, multiplicity=Multiplicity(1, 1)),
        Property(name="taskDSL_DSL2", type=taskDSL_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks3: BinaryAssociation = BinaryAssociation(
    name="tasks3",
    ends={
        Property(name="taskDSL_Task5", type=taskDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="taskDSL_Mission4", type=taskDSL_Task, multiplicity=Multiplicity(0, 9999))
    }
)
action6: BinaryAssociation = BinaryAssociation(
    name="action6",
    ends={
        Property(name="taskDSL_Action", type=taskDSL_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="taskDSL_Task7", type=taskDSL_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
detector8: BinaryAssociation = BinaryAssociation(
    name="detector8",
    ends={
        Property(name="taskDSL_Detector", type=taskDSL_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="taskDSL_Task9", type=taskDSL_Detector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
avoiders10: BinaryAssociation = BinaryAssociation(
    name="avoiders10",
    ends={
        Property(name="taskDSL_Avoid", type=taskDSL_Detector, multiplicity=Multiplicity(1, 1)),
        Property(name="taskDSL_Detector11", type=taskDSL_Avoid, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
driveActions12: BinaryAssociation = BinaryAssociation(
    name="driveActions12",
    ends={
        Property(name="taskDSL_DriveAction", type=taskDSL_Avoid, multiplicity=Multiplicity(1, 1)),
        Property(name="taskDSL_Avoid13", type=taskDSL_DriveAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_taskDSL_DriveUntil_Action = Generalization(general=Action, specific=taskDSL_DriveUntil)
gen_taskDSL_Investigate_Action = Generalization(general=Action, specific=taskDSL_Investigate)
gen_taskDSL_Speak_Action = Generalization(general=Action, specific=taskDSL_Speak)
gen_taskDSL_FollowLine_Action = Generalization(general=Action, specific=taskDSL_FollowLine)
gen_taskDSL_MoveBack_DriveAction = Generalization(general=DriveAction, specific=taskDSL_MoveBack)
gen_taskDSL_TurnLeft_DriveAction = Generalization(general=DriveAction, specific=taskDSL_TurnLeft)
gen_taskDSL_TurnRight_DriveAction = Generalization(general=DriveAction, specific=taskDSL_TurnRight)

# Domain Model
domain_model = DomainModel(
    name="taskDSL",
    types={taskDSL_Task, taskDSL_Action, taskDSL_Detector, taskDSL_Avoid, taskDSL_DriveUntil, Action, taskDSL_Investigate, taskDSL_Speak, taskDSL_FollowLine, taskDSL_DSL, taskDSL_Mission, taskDSL_DriveAction, taskDSL_MoveBack, DriveAction, taskDSL_TurnLeft, taskDSL_TurnRight, Object, Speed, Color},
    associations={missions0, tasks1, tasks3, action6, detector8, avoiders10, driveActions12},
    generalizations={gen_taskDSL_DriveUntil_Action, gen_taskDSL_Investigate_Action, gen_taskDSL_Speak_Action, gen_taskDSL_FollowLine_Action, gen_taskDSL_MoveBack_DriveAction, gen_taskDSL_TurnLeft_DriveAction, gen_taskDSL_TurnRight_DriveAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)