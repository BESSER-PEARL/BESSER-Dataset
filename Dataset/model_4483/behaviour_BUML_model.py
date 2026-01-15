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
ConditionKind: Enumeration = Enumeration(
    name="ConditionKind",
    literals={
            EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="LESSER_THAN")
    }
)

# Classes
behaviour_NamedElement = Class(name="behaviour::NamedElement", is_abstract=True)
behaviour_DroneBehaviour = Class(name="behaviour::DroneBehaviour")
NamedElement = Class(name="NamedElement")
behaviour_Instruction = Class(name="behaviour::Instruction", is_abstract=True)
behaviour_Drone = Class(name="behaviour::Drone")
behaviour_While = Class(name="behaviour::While")
behaviour_Instruct = Class(name="behaviour::Instruct")
behaviour_Lift = Class(name="behaviour::Lift")
behaviour_MovableObject = Class(name="behaviour::MovableObject")
behaviour_MoveTo = Class(name="behaviour::MoveTo")
Instruction = Class(name="Instruction")
behaviour_FieldObject = Class(name="behaviour::FieldObject")
behaviour_Pause = Class(name="behaviour::Pause")
behaviour_PerformAction = Class(name="behaviour::PerformAction")
behaviour_Action = Class(name="behaviour::Action")
behaviour_Choice = Class(name="behaviour::Choice")
behaviour_Condition = Class(name="behaviour::Condition")
behaviour_WaitForMessage = Class(name="behaviour::WaitForMessage")
behaviour_PlaceObject = Class(name="behaviour::PlaceObject")
behaviour_SendMessage = Class(name="behaviour::SendMessage")

# behaviour_NamedElement class attributes and methods
behaviour_NamedElement_name: Property = Property(name="name", type=StringType)
behaviour_NamedElement.attributes={behaviour_NamedElement_name}

# behaviour_DroneBehaviour class attributes and methods
behaviour_DroneBehaviour_canBeInterrupted: Property = Property(name="canBeInterrupted", type=BooleanType)
behaviour_DroneBehaviour.attributes={behaviour_DroneBehaviour_canBeInterrupted}

# NamedElement class attributes and methods

# behaviour_Instruction class attributes and methods

# behaviour_Drone class attributes and methods

# behaviour_While class attributes and methods

# behaviour_Instruct class attributes and methods

# behaviour_Lift class attributes and methods

# behaviour_MovableObject class attributes and methods

# behaviour_MoveTo class attributes and methods

# Instruction class attributes and methods

# behaviour_FieldObject class attributes and methods

# behaviour_Pause class attributes and methods
behaviour_Pause_duration: Property = Property(name="duration", type=FloatType)
behaviour_Pause.attributes={behaviour_Pause_duration}

# behaviour_PerformAction class attributes and methods

# behaviour_Action class attributes and methods

# behaviour_Choice class attributes and methods

# behaviour_Condition class attributes and methods
behaviour_Condition_operation: Property = Property(name="operation", type=StringType)
behaviour_Condition_key: Property = Property(name="key", type=StringType)
behaviour_Condition_value: Property = Property(name="value", type=StringType)
behaviour_Condition.attributes={behaviour_Condition_value, behaviour_Condition_key, behaviour_Condition_operation}

# behaviour_WaitForMessage class attributes and methods
behaviour_WaitForMessage_type: Property = Property(name="type", type=StringType)
behaviour_WaitForMessage_timeout: Property = Property(name="timeout", type=FloatType)
behaviour_WaitForMessage.attributes={behaviour_WaitForMessage_type, behaviour_WaitForMessage_timeout}

# behaviour_PlaceObject class attributes and methods

# behaviour_SendMessage class attributes and methods
behaviour_SendMessage_messageType: Property = Property(name="messageType", type=StringType)
behaviour_SendMessage.attributes={behaviour_SendMessage_messageType}

# Relationships
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="behaviour_Instruction", type=behaviour_DroneBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DroneBehaviour", type=behaviour_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
drones1: BinaryAssociation = BinaryAssociation(
    name="drones1",
    ends={
        Property(name="behaviour_Drone", type=behaviour_DroneBehaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DroneBehaviour2", type=behaviour_Drone, multiplicity=Multiplicity(1, 9999))
    }
)
whenLost20: BinaryAssociation = BinaryAssociation(
    name="whenLost20",
    ends={
        Property(name="behaviour_Instruction22", type=behaviour_WaitForMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_WaitForMessage21", type=behaviour_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
instructions23: BinaryAssociation = BinaryAssociation(
    name="instructions23",
    ends={
        Property(name="behaviour_Instruction24", type=behaviour_While, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_While", type=behaviour_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition25: BinaryAssociation = BinaryAssociation(
    name="condition25",
    ends={
        Property(name="behaviour_Condition27", type=behaviour_While, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_While26", type=behaviour_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions28: BinaryAssociation = BinaryAssociation(
    name="instructions28",
    ends={
        Property(name="behaviour_Instruction29", type=behaviour_Instruct, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Instruct", type=behaviour_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="behaviour_MovableObject", type=behaviour_Lift, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Lift", type=behaviour_MovableObject, multiplicity=Multiplicity(1, 1))
    }
)
fieldObject3: BinaryAssociation = BinaryAssociation(
    name="fieldObject3",
    ends={
        Property(name="behaviour_FieldObject", type=behaviour_MoveTo, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_MoveTo", type=behaviour_FieldObject, multiplicity=Multiplicity(1, 1))
    }
)
action4: BinaryAssociation = BinaryAssociation(
    name="action4",
    ends={
        Property(name="behaviour_Action", type=behaviour_PerformAction, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_PerformAction", type=behaviour_Action, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="behaviour_FieldObject7", type=behaviour_PerformAction, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_PerformAction6", type=behaviour_FieldObject, multiplicity=Multiplicity(1, 1))
    }
)
condition8: BinaryAssociation = BinaryAssociation(
    name="condition8",
    ends={
        Property(name="behaviour_Condition", type=behaviour_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Choice", type=behaviour_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueBranch9: BinaryAssociation = BinaryAssociation(
    name="trueBranch9",
    ends={
        Property(name="behaviour_Instruction11", type=behaviour_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Choice10", type=behaviour_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
falseBranch12: BinaryAssociation = BinaryAssociation(
    name="falseBranch12",
    ends={
        Property(name="behaviour_Instruction14", type=behaviour_Choice, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Choice13", type=behaviour_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldObject15: BinaryAssociation = BinaryAssociation(
    name="fieldObject15",
    ends={
        Property(name="behaviour_FieldObject17", type=behaviour_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Condition16", type=behaviour_FieldObject, multiplicity=Multiplicity(1, 1))
    }
)
whenArrived18: BinaryAssociation = BinaryAssociation(
    name="whenArrived18",
    ends={
        Property(name="behaviour_Instruction19", type=behaviour_WaitForMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_WaitForMessage", type=behaviour_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_behaviour_DroneBehaviour_NamedElement = Generalization(general=NamedElement, specific=behaviour_DroneBehaviour)
gen_behaviour_While_Instruction = Generalization(general=Instruction, specific=behaviour_While)
gen_behaviour_Instruct_Instruction = Generalization(general=Instruction, specific=behaviour_Instruct)
gen_behaviour_Lift_Instruction = Generalization(general=Instruction, specific=behaviour_Lift)
gen_behaviour_MoveTo_Instruction = Generalization(general=Instruction, specific=behaviour_MoveTo)
gen_behaviour_Pause_Instruction = Generalization(general=Instruction, specific=behaviour_Pause)
gen_behaviour_PerformAction_Instruction = Generalization(general=Instruction, specific=behaviour_PerformAction)
gen_behaviour_Choice_Instruction = Generalization(general=Instruction, specific=behaviour_Choice)
gen_behaviour_WaitForMessage_Instruction = Generalization(general=Instruction, specific=behaviour_WaitForMessage)
gen_behaviour_PlaceObject_Instruction = Generalization(general=Instruction, specific=behaviour_PlaceObject)
gen_behaviour_SendMessage_Instruction = Generalization(general=Instruction, specific=behaviour_SendMessage)

# Domain Model
domain_model = DomainModel(
    name="behaviour",
    types={behaviour_NamedElement, behaviour_DroneBehaviour, NamedElement, behaviour_Instruction, behaviour_Drone, behaviour_While, behaviour_Instruct, behaviour_Lift, behaviour_MovableObject, behaviour_MoveTo, Instruction, behaviour_FieldObject, behaviour_Pause, behaviour_PerformAction, behaviour_Action, behaviour_Choice, behaviour_Condition, behaviour_WaitForMessage, behaviour_PlaceObject, behaviour_SendMessage, ConditionKind},
    associations={instructions0, drones1, whenLost20, instructions23, condition25, instructions28, target30, fieldObject3, action4, target5, condition8, trueBranch9, falseBranch12, fieldObject15, whenArrived18},
    generalizations={gen_behaviour_DroneBehaviour_NamedElement, gen_behaviour_While_Instruction, gen_behaviour_Instruct_Instruction, gen_behaviour_Lift_Instruction, gen_behaviour_MoveTo_Instruction, gen_behaviour_Pause_Instruction, gen_behaviour_PerformAction_Instruction, gen_behaviour_Choice_Instruction, gen_behaviour_WaitForMessage_Instruction, gen_behaviour_PlaceObject_Instruction, gen_behaviour_SendMessage_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)