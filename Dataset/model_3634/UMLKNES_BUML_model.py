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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

# Classes
umlknes_Activity = Class(name="umlknes::Activity")
umlknes_ActivityNode = Class(name="umlknes::ActivityNode", is_abstract=True)
umlknes_ActivityEdge = Class(name="umlknes::ActivityEdge", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
umlknes_ControlNode = Class(name="umlknes::ControlNode", is_abstract=True)
ActivityNode = Class(name="ActivityNode")
umlknes_ActivityFinalNode = Class(name="umlknes::ActivityFinalNode")
ControlNode = Class(name="ControlNode")
umlknes_InitialNode = Class(name="umlknes::InitialNode")
umlknes_ValueSpecification = Class(name="umlknes::ValueSpecification", is_abstract=True)
umlknes_ControlFlow = Class(name="umlknes::ControlFlow")
ActivityEdge = Class(name="ActivityEdge")
umlknes_DecisionNode = Class(name="umlknes::DecisionNode")
umlknes_Action = Class(name="umlknes::Action", is_abstract=True)
umlknes_AcceptEventAction = Class(name="umlknes::AcceptEventAction")
Action = Class(name="Action")
umlknes_Trigger = Class(name="umlknes::Trigger")
NamedElement = Class(name="NamedElement")
umlknes_RedefinableElement = Class(name="umlknes::RedefinableElement", is_abstract=True)
umlknes_NamedElement = Class(name="umlknes::NamedElement", is_abstract=True)
umlknes_Event = Class(name="umlknes::Event", is_abstract=True)
umlknes_ExecutionEvent = Class(name="umlknes::ExecutionEvent")
Event = Class(name="Event")
umlknes_CreationEvent = Class(name="umlknes::CreationEvent")
umlknes_DestructionEvent = Class(name="umlknes::DestructionEvent")
umlknes_OpaqueExpression = Class(name="umlknes::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")

# umlknes_Activity class attributes and methods
umlknes_Activity_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
umlknes_Activity_isSingleExecution: Property = Property(name="isSingleExecution", type=BooleanType)
umlknes_Activity.attributes={umlknes_Activity_isReadOnly, umlknes_Activity_isSingleExecution}

# umlknes_ActivityNode class attributes and methods

# umlknes_ActivityEdge class attributes and methods

# RedefinableElement class attributes and methods

# umlknes_ControlNode class attributes and methods

# ActivityNode class attributes and methods

# umlknes_ActivityFinalNode class attributes and methods

# ControlNode class attributes and methods

# umlknes_InitialNode class attributes and methods

# umlknes_ValueSpecification class attributes and methods

# umlknes_ControlFlow class attributes and methods

# ActivityEdge class attributes and methods

# umlknes_DecisionNode class attributes and methods

# umlknes_Action class attributes and methods

# umlknes_AcceptEventAction class attributes and methods
umlknes_AcceptEventAction_isUnMarshall: Property = Property(name="isUnMarshall", type=BooleanType)
umlknes_AcceptEventAction.attributes={umlknes_AcceptEventAction_isUnMarshall}

# Action class attributes and methods

# umlknes_Trigger class attributes and methods

# NamedElement class attributes and methods

# umlknes_RedefinableElement class attributes and methods
umlknes_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
umlknes_RedefinableElement.attributes={umlknes_RedefinableElement_isLeaf}

# umlknes_NamedElement class attributes and methods
umlknes_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
umlknes_NamedElement.attributes={umlknes_NamedElement_visibility}

# umlknes_Event class attributes and methods

# umlknes_ExecutionEvent class attributes and methods

# Event class attributes and methods

# umlknes_CreationEvent class attributes and methods

# umlknes_DestructionEvent class attributes and methods

# umlknes_OpaqueExpression class attributes and methods

# ValueSpecification class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="ActivityNode", type=umlknes_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity", type=umlknes_ActivityNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edge1: BinaryAssociation = BinaryAssociation(
    name="edge1",
    ends={
        Property(name="ActivityEdge", type=umlknes_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="activity2", type=umlknes_ActivityEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activity3: BinaryAssociation = BinaryAssociation(
    name="activity3",
    ends={
        Property(name="Activity", type=umlknes_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=umlknes_Activity, multiplicity=Multiplicity(0, 1))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="ActivityEdge5", type=umlknes_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=umlknes_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="ActivityEdge7", type=umlknes_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=umlknes_ActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedElement9: BinaryAssociation = BinaryAssociation(
    name="redefinedElement9",
    ends={
        Property(name="umlknes_ActivityNode", type=umlknes_ActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="umlknes_ActivityNode8", type=umlknes_ActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="ActivityNode11", type=umlknes_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=umlknes_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="ActivityNode13", type=umlknes_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=umlknes_ActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
activity14: BinaryAssociation = BinaryAssociation(
    name="activity14",
    ends={
        Property(name="Activity15", type=umlknes_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edge", type=umlknes_Activity, multiplicity=Multiplicity(0, 1))
    }
)
weight16: BinaryAssociation = BinaryAssociation(
    name="weight16",
    ends={
        Property(name="umlknes_ValueSpecification", type=umlknes_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlknes_ActivityEdge", type=umlknes_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guard17: BinaryAssociation = BinaryAssociation(
    name="guard17",
    ends={
        Property(name="umlknes_ValueSpecification19", type=umlknes_ActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="umlknes_ActivityEdge18", type=umlknes_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trigger20: BinaryAssociation = BinaryAssociation(
    name="trigger20",
    ends={
        Property(name="umlknes_Trigger", type=umlknes_AcceptEventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="umlknes_AcceptEventAction", type=umlknes_Trigger, multiplicity=Multiplicity(1, 9999))
    }
)
event21: BinaryAssociation = BinaryAssociation(
    name="event21",
    ends={
        Property(name="umlknes_Event", type=umlknes_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="umlknes_Trigger22", type=umlknes_Event, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_umlknes_ActivityNode_RedefinableElement = Generalization(general=RedefinableElement, specific=umlknes_ActivityNode)
gen_umlknes_ControlNode_ActivityNode = Generalization(general=ActivityNode, specific=umlknes_ControlNode)
gen_umlknes_ActivityFinalNode_ControlNode = Generalization(general=ControlNode, specific=umlknes_ActivityFinalNode)
gen_umlknes_InitialNode_ControlNode = Generalization(general=ControlNode, specific=umlknes_InitialNode)
gen_umlknes_ActivityEdge_RedefinableElement = Generalization(general=RedefinableElement, specific=umlknes_ActivityEdge)
gen_umlknes_ControlFlow_ActivityEdge = Generalization(general=ActivityEdge, specific=umlknes_ControlFlow)
gen_umlknes_DecisionNode_ControlNode = Generalization(general=ControlNode, specific=umlknes_DecisionNode)
gen_umlknes_Action_ActivityNode = Generalization(general=ActivityNode, specific=umlknes_Action)
gen_umlknes_AcceptEventAction_Action = Generalization(general=Action, specific=umlknes_AcceptEventAction)
gen_umlknes_ValueSpecification_NamedElement = Generalization(general=NamedElement, specific=umlknes_ValueSpecification)
gen_umlknes_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=umlknes_RedefinableElement)
gen_umlknes_Trigger_NamedElement = Generalization(general=NamedElement, specific=umlknes_Trigger)
gen_umlknes_ExecutionEvent_Event = Generalization(general=Event, specific=umlknes_ExecutionEvent)
gen_umlknes_CreationEvent_Event = Generalization(general=Event, specific=umlknes_CreationEvent)
gen_umlknes_DestructionEvent_Event = Generalization(general=Event, specific=umlknes_DestructionEvent)
gen_umlknes_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=umlknes_OpaqueExpression)

# Domain Model
domain_model = DomainModel(
    name="umlknes",
    types={umlknes_Activity, umlknes_ActivityNode, umlknes_ActivityEdge, RedefinableElement, umlknes_ControlNode, ActivityNode, umlknes_ActivityFinalNode, ControlNode, umlknes_InitialNode, umlknes_ValueSpecification, umlknes_ControlFlow, ActivityEdge, umlknes_DecisionNode, umlknes_Action, umlknes_AcceptEventAction, Action, umlknes_Trigger, NamedElement, umlknes_RedefinableElement, umlknes_NamedElement, umlknes_Event, umlknes_ExecutionEvent, Event, umlknes_CreationEvent, umlknes_DestructionEvent, umlknes_OpaqueExpression, ValueSpecification, VisibilityKind},
    associations={node0, edge1, activity3, incoming4, outgoing6, redefinedElement9, target10, source12, activity14, weight16, guard17, trigger20, event21},
    generalizations={gen_umlknes_ActivityNode_RedefinableElement, gen_umlknes_ControlNode_ActivityNode, gen_umlknes_ActivityFinalNode_ControlNode, gen_umlknes_InitialNode_ControlNode, gen_umlknes_ActivityEdge_RedefinableElement, gen_umlknes_ControlFlow_ActivityEdge, gen_umlknes_DecisionNode_ControlNode, gen_umlknes_Action_ActivityNode, gen_umlknes_AcceptEventAction_Action, gen_umlknes_ValueSpecification_NamedElement, gen_umlknes_RedefinableElement_NamedElement, gen_umlknes_Trigger_NamedElement, gen_umlknes_ExecutionEvent_Event, gen_umlknes_CreationEvent_Event, gen_umlknes_DestructionEvent_Event, gen_umlknes_OpaqueExpression_ValueSpecification},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)