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
TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="external"),
			EnumerationLiteral(name="internal")
    }
)

# Classes
StateMachines_BehaviorStateMachines_Behavior = Class(name="StateMachines_BehaviorStateMachines_Behavior", is_abstract=True)
StateMachines_BehaviorStateMachines_StateMachine = Class(name="StateMachines_BehaviorStateMachines_StateMachine")
Behavior = Class(name="Behavior")
Region = Class(name="Region")
Pseudostate = Class(name="Pseudostate")
StateMachines_BehaviorStateMachines_Transition = Class(name="StateMachines_BehaviorStateMachines_Transition")
Trigger = Class(name="Trigger")
Constraint = Class(name="Constraint")
State = Class(name="State")
StateMachine = Class(name="StateMachine")
StateMachines_BehaviorStateMachines_Namespace = Class(name="StateMachines_BehaviorStateMachines_Namespace", is_abstract=True)
StateMachines_BehaviorStateMachines_Region = Class(name="StateMachines_BehaviorStateMachines_Region")
BehaviorStateMachines_Namespace = Class(name="BehaviorStateMachines_Namespace")
BehaviorStateMachines_RedefinableElement = Class(name="BehaviorStateMachines_RedefinableElement")
Vertex = Class(name="Vertex")
Transition = Class(name="Transition")
StateMachines_BehaviorStateMachines_NamedElement = Class(name="StateMachines_BehaviorStateMachines_NamedElement", is_abstract=True)
StateMachines_BehaviorStateMachines_Vertex = Class(name="StateMachines_BehaviorStateMachines_Vertex", is_abstract=True)
NamedElement = Class(name="NamedElement")
StateMachines_BehaviorStateMachines_FinalState = Class(name="StateMachines_BehaviorStateMachines_FinalState")
StateMachines_BehaviorStateMachines_RedefinableElement = Class(name="StateMachines_BehaviorStateMachines_RedefinableElement", is_abstract=True)
StateMachines_BehaviorStateMachines_Classifier = Class(name="StateMachines_BehaviorStateMachines_Classifier", is_abstract=True)
StateMachines_BehaviorStateMachines_TimeEvent = Class(name="StateMachines_BehaviorStateMachines_TimeEvent")
StateMachines_BehaviorStateMachines_Constraint = Class(name="StateMachines_BehaviorStateMachines_Constraint", is_abstract=True)
StateMachines_BehaviorStateMachines_Trigger = Class(name="StateMachines_BehaviorStateMachines_Trigger", is_abstract=True)
StateMachines_BehaviorStateMachines_Pseudostate = Class(name="StateMachines_BehaviorStateMachines_Pseudostate")
StateMachines_BehaviorStateMachines_ConnectionPointReference = Class(name="StateMachines_BehaviorStateMachines_ConnectionPointReference")
StateMachines_BehaviorStateMachines_State = Class(name="StateMachines_BehaviorStateMachines_State")
BehaviorStateMachines_Vertex = Class(name="BehaviorStateMachines_Vertex")
ConnectionPointReference = Class(name="ConnectionPointReference")
StateMachines_ProtocolStateMachines_ProtocolStateMachine = Class(name="StateMachines_ProtocolStateMachines_ProtocolStateMachine")
ProtocolConformance = Class(name="ProtocolConformance")
StateMachines_ProtocolStateMachines_ProtocolConformance = Class(name="StateMachines_ProtocolStateMachines_ProtocolConformance")
DirectedRelationship = Class(name="DirectedRelationship")
ProtocolStateMachine = Class(name="ProtocolStateMachine")
StateMachines_ProtocolStateMachines_DirectedRelationship = Class(name="StateMachines_ProtocolStateMachines_DirectedRelationship", is_abstract=True)
StateMachines_ProtocolStateMachines_Port = Class(name="StateMachines_ProtocolStateMachines_Port")
StateMachines_ProtocolStateMachines_Interface = Class(name="StateMachines_ProtocolStateMachines_Interface")
Classifier = Class(name="Classifier")
StateMachines_ProtocolStateMachines_ProtocolTransition = Class(name="StateMachines_ProtocolStateMachines_ProtocolTransition")
Operation = Class(name="Operation")
StateMachines_ProtocolStateMachines_Operation = Class(name="StateMachines_ProtocolStateMachines_Operation")

# StateMachines_BehaviorStateMachines_Behavior class attributes and methods

# StateMachines_BehaviorStateMachines_StateMachine class attributes and methods

# Behavior class attributes and methods

# Region class attributes and methods

# Pseudostate class attributes and methods

# StateMachines_BehaviorStateMachines_Transition class attributes and methods
StateMachines_BehaviorStateMachines_Transition_kind: Property = Property(name="kind", type=StringType)
StateMachines_BehaviorStateMachines_Transition.attributes={StateMachines_BehaviorStateMachines_Transition_kind}

# Trigger class attributes and methods

# Constraint class attributes and methods

# State class attributes and methods

# StateMachine class attributes and methods

# StateMachines_BehaviorStateMachines_Namespace class attributes and methods

# StateMachines_BehaviorStateMachines_Region class attributes and methods

# BehaviorStateMachines_Namespace class attributes and methods

# BehaviorStateMachines_RedefinableElement class attributes and methods

# Vertex class attributes and methods

# Transition class attributes and methods

# StateMachines_BehaviorStateMachines_NamedElement class attributes and methods

# StateMachines_BehaviorStateMachines_Vertex class attributes and methods

# NamedElement class attributes and methods

# StateMachines_BehaviorStateMachines_FinalState class attributes and methods

# StateMachines_BehaviorStateMachines_RedefinableElement class attributes and methods

# StateMachines_BehaviorStateMachines_Classifier class attributes and methods

# StateMachines_BehaviorStateMachines_TimeEvent class attributes and methods

# StateMachines_BehaviorStateMachines_Constraint class attributes and methods

# StateMachines_BehaviorStateMachines_Trigger class attributes and methods

# StateMachines_BehaviorStateMachines_Pseudostate class attributes and methods

# StateMachines_BehaviorStateMachines_ConnectionPointReference class attributes and methods

# StateMachines_BehaviorStateMachines_State class attributes and methods
StateMachines_BehaviorStateMachines_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
StateMachines_BehaviorStateMachines_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
StateMachines_BehaviorStateMachines_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
StateMachines_BehaviorStateMachines_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
StateMachines_BehaviorStateMachines_State.attributes={StateMachines_BehaviorStateMachines_State_isSimple, StateMachines_BehaviorStateMachines_State_isOrthogonal, StateMachines_BehaviorStateMachines_State_isComposite, StateMachines_BehaviorStateMachines_State_isSubmachineState}

# BehaviorStateMachines_Vertex class attributes and methods

# ConnectionPointReference class attributes and methods

# StateMachines_ProtocolStateMachines_ProtocolStateMachine class attributes and methods

# ProtocolConformance class attributes and methods

# StateMachines_ProtocolStateMachines_ProtocolConformance class attributes and methods

# DirectedRelationship class attributes and methods

# ProtocolStateMachine class attributes and methods

# StateMachines_ProtocolStateMachines_DirectedRelationship class attributes and methods

# StateMachines_ProtocolStateMachines_Port class attributes and methods

# StateMachines_ProtocolStateMachines_Interface class attributes and methods

# Classifier class attributes and methods

# StateMachines_ProtocolStateMachines_ProtocolTransition class attributes and methods

# Operation class attributes and methods

# StateMachines_ProtocolStateMachines_Operation class attributes and methods

# Relationships
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="Region", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
connectionPoint1: BinaryAssociation = BinaryAssociation(
    name="connectionPoint1",
    ends={
        Property(name="Pseudostate", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_StateMachine", type=Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="Vertex22", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="Vertex24", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
effect25: BinaryAssociation = BinaryAssociation(
    name="effect25",
    ends={
        Property(name="Behavior", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger26: BinaryAssociation = BinaryAssociation(
    name="trigger26",
    ends={
        Property(name="Trigger", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition27", type=Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard28: BinaryAssociation = BinaryAssociation(
    name="guard28",
    ends={
        Property(name="Constraint", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition29", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container30: BinaryAssociation = BinaryAssociation(
    name="container30",
    ends={
        Property(name="Region31", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
redefinedTransition32: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition32",
    ends={
        Property(name="Transition34", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition33", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
submachineState2: BinaryAssociation = BinaryAssociation(
    name="submachineState2",
    ends={
        Property(name="State", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=State, multiplicity=Multiplicity(0, 9999))
    }
)
extendedStateMachine3: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine3",
    ends={
        Property(name="StateMachine", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_StateMachine4", type=StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex5: BinaryAssociation = BinaryAssociation(
    name="subvertex5",
    ends={
        Property(name="Vertex", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine6: BinaryAssociation = BinaryAssociation(
    name="stateMachine6",
    ends={
        Property(name="StateMachine7", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="Transition", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container9", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state10: BinaryAssociation = BinaryAssociation(
    name="state10",
    ends={
        Property(name="State12", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region11", type=State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion13: BinaryAssociation = BinaryAssociation(
    name="extendedRegion13",
    ends={
        Property(name="Region14", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Region", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing15: BinaryAssociation = BinaryAssociation(
    name="outgoing15",
    ends={
        Property(name="Transition16", type=StateMachines_BehaviorStateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming17: BinaryAssociation = BinaryAssociation(
    name="incoming17",
    ends={
        Property(name="Transition18", type=StateMachines_BehaviorStateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container19: BinaryAssociation = BinaryAssociation(
    name="container19",
    ends={
        Property(name="Region20", type=StateMachines_BehaviorStateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
deferrableTrigger53: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger53",
    ends={
        Property(name="Trigger54", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State", type=Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit55: BinaryAssociation = BinaryAssociation(
    name="exit55",
    ends={
        Property(name="Behavior57", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State56", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity58: BinaryAssociation = BinaryAssociation(
    name="doActivity58",
    ends={
        Property(name="Behavior60", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State59", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry61: BinaryAssociation = BinaryAssociation(
    name="entry61",
    ends={
        Property(name="Behavior63", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State62", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateInvariant64: BinaryAssociation = BinaryAssociation(
    name="stateInvariant64",
    ends={
        Property(name="Constraint66", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State65", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedState67: BinaryAssociation = BinaryAssociation(
    name="redefinedState67",
    ends={
        Property(name="State69", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State68", type=State, multiplicity=Multiplicity(0, 1))
    }
)
state35: BinaryAssociation = BinaryAssociation(
    name="state35",
    ends={
        Property(name="State36", type=StateMachines_BehaviorStateMachines_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint", type=State, multiplicity=Multiplicity(0, 1))
    }
)
exit37: BinaryAssociation = BinaryAssociation(
    name="exit37",
    ends={
        Property(name="Pseudostate38", type=StateMachines_BehaviorStateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_ConnectionPointReference", type=Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
entry39: BinaryAssociation = BinaryAssociation(
    name="entry39",
    ends={
        Property(name="Pseudostate41", type=StateMachines_BehaviorStateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_ConnectionPointReference40", type=Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
state42: BinaryAssociation = BinaryAssociation(
    name="state42",
    ends={
        Property(name="State43", type=StateMachines_BehaviorStateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=State, multiplicity=Multiplicity(0, 1))
    }
)
connection44: BinaryAssociation = BinaryAssociation(
    name="connection44",
    ends={
        Property(name="ConnectionPointReference", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint45: BinaryAssociation = BinaryAssociation(
    name="connectionPoint45",
    ends={
        Property(name="Pseudostate47", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state46", type=Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachine48: BinaryAssociation = BinaryAssociation(
    name="submachine48",
    ends={
        Property(name="StateMachine49", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region50: BinaryAssociation = BinaryAssociation(
    name="region50",
    ends={
        Property(name="Region52", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state51", type=Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conformance70: BinaryAssociation = BinaryAssociation(
    name="conformance70",
    ends={
        Property(name="ProtocolConformance", type=StateMachines_ProtocolStateMachines_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="specificMachine", type=ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificMachine71: BinaryAssociation = BinaryAssociation(
    name="specificMachine71",
    ends={
        Property(name="ProtocolStateMachine", type=StateMachines_ProtocolStateMachines_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="conformance", type=ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine72: BinaryAssociation = BinaryAssociation(
    name="generalMachine72",
    ends={
        Property(name="ProtocolStateMachine73", type=StateMachines_ProtocolStateMachines_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolConformance", type=ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
protocol74: BinaryAssociation = BinaryAssociation(
    name="protocol74",
    ends={
        Property(name="ProtocolStateMachine75", type=StateMachines_ProtocolStateMachines_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_Port", type=ProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
protocol76: BinaryAssociation = BinaryAssociation(
    name="protocol76",
    ends={
        Property(name="ProtocolStateMachine77", type=StateMachines_ProtocolStateMachines_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_Interface", type=ProtocolStateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preCondition78: BinaryAssociation = BinaryAssociation(
    name="preCondition78",
    ends={
        Property(name="Constraint79", type=StateMachines_ProtocolStateMachines_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolTransition", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postCondition80: BinaryAssociation = BinaryAssociation(
    name="postCondition80",
    ends={
        Property(name="Constraint82", type=StateMachines_ProtocolStateMachines_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolTransition81", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referred83: BinaryAssociation = BinaryAssociation(
    name="referred83",
    ends={
        Property(name="Operation", type=StateMachines_ProtocolStateMachines_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolTransition84", type=Operation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_StateMachines_BehaviorStateMachines_StateMachine_Behavior = Generalization(general=Behavior, specific=StateMachines_BehaviorStateMachines_StateMachine)
gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_Namespace = Generalization(general=BehaviorStateMachines_Namespace, specific=StateMachines_BehaviorStateMachines_Transition)
gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_RedefinableElement = Generalization(general=BehaviorStateMachines_RedefinableElement, specific=StateMachines_BehaviorStateMachines_Transition)
gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_Namespace = Generalization(general=BehaviorStateMachines_Namespace, specific=StateMachines_BehaviorStateMachines_Region)
gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_RedefinableElement = Generalization(general=BehaviorStateMachines_RedefinableElement, specific=StateMachines_BehaviorStateMachines_Region)
gen_StateMachines_BehaviorStateMachines_Vertex_NamedElement = Generalization(general=NamedElement, specific=StateMachines_BehaviorStateMachines_Vertex)
gen_StateMachines_BehaviorStateMachines_FinalState_State = Generalization(general=State, specific=StateMachines_BehaviorStateMachines_FinalState)
gen_StateMachines_BehaviorStateMachines_Pseudostate_Vertex = Generalization(general=Vertex, specific=StateMachines_BehaviorStateMachines_Pseudostate)
gen_StateMachines_BehaviorStateMachines_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=StateMachines_BehaviorStateMachines_ConnectionPointReference)
gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Vertex = Generalization(general=BehaviorStateMachines_Vertex, specific=StateMachines_BehaviorStateMachines_State)
gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_RedefinableElement = Generalization(general=BehaviorStateMachines_RedefinableElement, specific=StateMachines_BehaviorStateMachines_State)
gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Namespace = Generalization(general=BehaviorStateMachines_Namespace, specific=StateMachines_BehaviorStateMachines_State)
gen_StateMachines_ProtocolStateMachines_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=StateMachines_ProtocolStateMachines_ProtocolStateMachine)
gen_StateMachines_ProtocolStateMachines_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=StateMachines_ProtocolStateMachines_ProtocolConformance)
gen_StateMachines_ProtocolStateMachines_Interface_Classifier = Generalization(general=Classifier, specific=StateMachines_ProtocolStateMachines_Interface)
gen_StateMachines_ProtocolStateMachines_ProtocolTransition_Transition = Generalization(general=Transition, specific=StateMachines_ProtocolStateMachines_ProtocolTransition)

# Domain Model
domain_model = DomainModel(
    name="StateMachines",
    types={StateMachines_BehaviorStateMachines_Behavior, StateMachines_BehaviorStateMachines_StateMachine, Behavior, Region, Pseudostate, StateMachines_BehaviorStateMachines_Transition, Trigger, Constraint, State, StateMachine, StateMachines_BehaviorStateMachines_Namespace, StateMachines_BehaviorStateMachines_Region, BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement, Vertex, Transition, StateMachines_BehaviorStateMachines_NamedElement, StateMachines_BehaviorStateMachines_Vertex, NamedElement, StateMachines_BehaviorStateMachines_FinalState, StateMachines_BehaviorStateMachines_RedefinableElement, StateMachines_BehaviorStateMachines_Classifier, StateMachines_BehaviorStateMachines_TimeEvent, StateMachines_BehaviorStateMachines_Constraint, StateMachines_BehaviorStateMachines_Trigger, StateMachines_BehaviorStateMachines_Pseudostate, StateMachines_BehaviorStateMachines_ConnectionPointReference, StateMachines_BehaviorStateMachines_State, BehaviorStateMachines_Vertex, ConnectionPointReference, StateMachines_ProtocolStateMachines_ProtocolStateMachine, ProtocolConformance, StateMachines_ProtocolStateMachines_ProtocolConformance, DirectedRelationship, ProtocolStateMachine, StateMachines_ProtocolStateMachines_DirectedRelationship, StateMachines_ProtocolStateMachines_Port, StateMachines_ProtocolStateMachines_Interface, Classifier, StateMachines_ProtocolStateMachines_ProtocolTransition, Operation, StateMachines_ProtocolStateMachines_Operation, TransitionKind},
    associations={region0, connectionPoint1, source21, target23, effect25, trigger26, guard28, container30, redefinedTransition32, submachineState2, extendedStateMachine3, subvertex5, stateMachine6, transition8, state10, extendedRegion13, outgoing15, incoming17, container19, deferrableTrigger53, exit55, doActivity58, entry61, stateInvariant64, redefinedState67, state35, exit37, entry39, state42, connection44, connectionPoint45, submachine48, region50, conformance70, specificMachine71, generalMachine72, protocol74, protocol76, preCondition78, postCondition80, referred83},
    generalizations={gen_StateMachines_BehaviorStateMachines_StateMachine_Behavior, gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_Namespace, gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_RedefinableElement, gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_Namespace, gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_RedefinableElement, gen_StateMachines_BehaviorStateMachines_Vertex_NamedElement, gen_StateMachines_BehaviorStateMachines_FinalState_State, gen_StateMachines_BehaviorStateMachines_Pseudostate_Vertex, gen_StateMachines_BehaviorStateMachines_ConnectionPointReference_Vertex, gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Vertex, gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_RedefinableElement, gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Namespace, gen_StateMachines_ProtocolStateMachines_ProtocolStateMachine_StateMachine, gen_StateMachines_ProtocolStateMachines_ProtocolConformance_DirectedRelationship, gen_StateMachines_ProtocolStateMachines_Interface_Classifier, gen_StateMachines_ProtocolStateMachines_ProtocolTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)