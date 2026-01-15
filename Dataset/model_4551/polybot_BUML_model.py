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
polybot_GoTo = Class(name="polybot::GoTo")
Move = Class(name="Move")
polybot_Move = Class(name="polybot::Move", is_abstract=True)
Instruction = Class(name="Instruction")
polybot_Right = Class(name="polybot::Right")
polybot_Left = Class(name="polybot::Left")
polybot_Reverse = Class(name="polybot::Reverse")
polybot_Forward = Class(name="polybot::Forward")
polybot_IfObjectDetected = Class(name="polybot::IfObjectDetected")
polybot_IfObstacleDetected = Class(name="polybot::IfObstacleDetected")
polybot_TakeDropObject = Class(name="polybot::TakeDropObject")
polybot_While = Class(name="polybot::While")
polybot_Bot = Class(name="polybot::Bot")
polybot_Point = Class(name="polybot::Point")
polybot_Instruction = Class(name="polybot::Instruction", is_abstract=True)

# polybot_GoTo class attributes and methods

# Move class attributes and methods

# polybot_Move class attributes and methods
polybot_Move_speed: Property = Property(name="speed", type=IntegerType)
polybot_Move_duration: Property = Property(name="duration", type=IntegerType)
polybot_Move.attributes={polybot_Move_speed, polybot_Move_duration}

# Instruction class attributes and methods

# polybot_Right class attributes and methods

# polybot_Left class attributes and methods

# polybot_Reverse class attributes and methods

# polybot_Forward class attributes and methods

# polybot_IfObjectDetected class attributes and methods

# polybot_IfObstacleDetected class attributes and methods

# polybot_TakeDropObject class attributes and methods

# polybot_While class attributes and methods
polybot_While_nb: Property = Property(name="nb", type=IntegerType)
polybot_While.attributes={polybot_While_nb}

# polybot_Bot class attributes and methods

# polybot_Point class attributes and methods
polybot_Point_x: Property = Property(name="x", type=IntegerType)
polybot_Point_y: Property = Property(name="y", type=IntegerType)
polybot_Point.attributes={polybot_Point_x, polybot_Point_y}

# polybot_Instruction class attributes and methods

# Relationships
listOfInstructions3: BinaryAssociation = BinaryAssociation(
    name="listOfInstructions3",
    ends={
        Property(name="polybot_Instruction4", type=polybot_IfObjectDetected, multiplicity=Multiplicity(1, 1)),
        Property(name="polybot_IfObjectDetected", type=polybot_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listOfInstructions5: BinaryAssociation = BinaryAssociation(
    name="listOfInstructions5",
    ends={
        Property(name="polybot_Instruction6", type=polybot_IfObstacleDetected, multiplicity=Multiplicity(1, 1)),
        Property(name="polybot_IfObstacleDetected", type=polybot_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
listOfInstructions7: BinaryAssociation = BinaryAssociation(
    name="listOfInstructions7",
    ends={
        Property(name="polybot_Instruction8", type=polybot_While, multiplicity=Multiplicity(1, 1)),
        Property(name="polybot_While", type=polybot_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialPosition0: BinaryAssociation = BinaryAssociation(
    name="initialPosition0",
    ends={
        Property(name="polybot_Point", type=polybot_Bot, multiplicity=Multiplicity(1, 1)),
        Property(name="polybot_Bot", type=polybot_Point, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instructionList1: BinaryAssociation = BinaryAssociation(
    name="instructionList1",
    ends={
        Property(name="polybot_Instruction", type=polybot_Bot, multiplicity=Multiplicity(1, 1)),
        Property(name="polybot_Bot2", type=polybot_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_polybot_GoTo_Move = Generalization(general=Move, specific=polybot_GoTo)
gen_polybot_Move_Instruction = Generalization(general=Instruction, specific=polybot_Move)
gen_polybot_Right_Move = Generalization(general=Move, specific=polybot_Right)
gen_polybot_Left_Move = Generalization(general=Move, specific=polybot_Left)
gen_polybot_Reverse_Move = Generalization(general=Move, specific=polybot_Reverse)
gen_polybot_Forward_Move = Generalization(general=Move, specific=polybot_Forward)
gen_polybot_IfObjectDetected_Instruction = Generalization(general=Instruction, specific=polybot_IfObjectDetected)
gen_polybot_IfObstacleDetected_Instruction = Generalization(general=Instruction, specific=polybot_IfObstacleDetected)
gen_polybot_TakeDropObject_Instruction = Generalization(general=Instruction, specific=polybot_TakeDropObject)
gen_polybot_While_Instruction = Generalization(general=Instruction, specific=polybot_While)

# Domain Model
domain_model = DomainModel(
    name="polybot",
    types={polybot_GoTo, Move, polybot_Move, Instruction, polybot_Right, polybot_Left, polybot_Reverse, polybot_Forward, polybot_IfObjectDetected, polybot_IfObstacleDetected, polybot_TakeDropObject, polybot_While, polybot_Bot, polybot_Point, polybot_Instruction},
    associations={listOfInstructions3, listOfInstructions5, listOfInstructions7, initialPosition0, instructionList1},
    generalizations={gen_polybot_GoTo_Move, gen_polybot_Move_Instruction, gen_polybot_Right_Move, gen_polybot_Left_Move, gen_polybot_Reverse_Move, gen_polybot_Forward_Move, gen_polybot_IfObjectDetected_Instruction, gen_polybot_IfObstacleDetected_Instruction, gen_polybot_TakeDropObject_Instruction, gen_polybot_While_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)