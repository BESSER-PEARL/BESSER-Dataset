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
Pseudostate = Class(name="Pseudostate")
State = Class(name="State")
StateMachine = Class(name="StateMachine")
StateMachines_BehaviorStateMachines_Namespace = Class(name="StateMachines::BehaviorStateMachines::Namespace", is_abstract=True)
StateMachines_BehaviorStateMachines_Region = Class(name="StateMachines::BehaviorStateMachines::Region")
BehaviorStateMachines_Namespace = Class(name="BehaviorStateMachines::Namespace")
BehaviorStateMachines_RedefinableElement = Class(name="BehaviorStateMachines::RedefinableElement")
Vertex = Class(name="Vertex")
StateMachines_BehaviorStateMachines_Behavior = Class(name="StateMachines::BehaviorStateMachines::Behavior", is_abstract=True)
StateMachines_BehaviorStateMachines_StateMachine = Class(name="StateMachines::BehaviorStateMachines::StateMachine")
Behavior = Class(name="Behavior")
Region = Class(name="Region")
Transition = Class(name="Transition")
StateMachines_BehaviorStateMachines_NamedElement = Class(name="StateMachines::BehaviorStateMachines::NamedElement", is_abstract=True)
StateMachines_BehaviorStateMachines_Vertex = Class(name="StateMachines::BehaviorStateMachines::Vertex", is_abstract=True)
NamedElement = Class(name="NamedElement")
Trigger = Class(name="Trigger")
Constraint = Class(name="Constraint")
StateMachines_BehaviorStateMachines_Transition = Class(name="StateMachines::BehaviorStateMachines::Transition")
StateMachines_BehaviorStateMachines_ConnectionPointReference = Class(name="StateMachines::BehaviorStateMachines::ConnectionPointReference")
StateMachines_BehaviorStateMachines_State = Class(name="StateMachines::BehaviorStateMachines::State")
BehaviorStateMachines_Vertex = Class(name="BehaviorStateMachines::Vertex")
StateMachines_BehaviorStateMachines_Constraint = Class(name="StateMachines::BehaviorStateMachines::Constraint", is_abstract=True)
StateMachines_BehaviorStateMachines_Trigger = Class(name="StateMachines::BehaviorStateMachines::Trigger", is_abstract=True)
StateMachines_BehaviorStateMachines_Pseudostate = Class(name="StateMachines::BehaviorStateMachines::Pseudostate")
StateMachines_BehaviorStateMachines_FinalState = Class(name="StateMachines::BehaviorStateMachines::FinalState")
ConnectionPointReference = Class(name="ConnectionPointReference")
StateMachines_ProtocolStateMachines_ProtocolConformance = Class(name="StateMachines::ProtocolStateMachines::ProtocolConformance")
DirectedRelationship = Class(name="DirectedRelationship")
ProtocolStateMachine = Class(name="ProtocolStateMachine")
StateMachines_ProtocolStateMachines_DirectedRelationship = Class(name="StateMachines::ProtocolStateMachines::DirectedRelationship", is_abstract=True)
StateMachines_ProtocolStateMachines_Port = Class(name="StateMachines::ProtocolStateMachines::Port")
StateMachines_ProtocolStateMachines_Interface = Class(name="StateMachines::ProtocolStateMachines::Interface")
Classifier = Class(name="Classifier")
StateMachines_BehaviorStateMachines_RedefinableElement = Class(name="StateMachines::BehaviorStateMachines::RedefinableElement", is_abstract=True)
StateMachines_BehaviorStateMachines_Classifier = Class(name="StateMachines::BehaviorStateMachines::Classifier", is_abstract=True)
StateMachines_BehaviorStateMachines_TimeEvent = Class(name="StateMachines::BehaviorStateMachines::TimeEvent")
StateMachines_ProtocolStateMachines_ProtocolStateMachine = Class(name="StateMachines::ProtocolStateMachines::ProtocolStateMachine")
ProtocolConformance = Class(name="ProtocolConformance")
StateMachines_ProtocolStateMachines_ProtocolTransition = Class(name="StateMachines::ProtocolStateMachines::ProtocolTransition")
Operation = Class(name="Operation")
StateMachines_ProtocolStateMachines_Operation = Class(name="StateMachines::ProtocolStateMachines::Operation")

# Pseudostate class attributes and methods

# State class attributes and methods

# StateMachine class attributes and methods

# StateMachines_BehaviorStateMachines_Namespace class attributes and methods

# StateMachines_BehaviorStateMachines_Region class attributes and methods

# BehaviorStateMachines_Namespace class attributes and methods

# BehaviorStateMachines_RedefinableElement class attributes and methods

# Vertex class attributes and methods

# StateMachines_BehaviorStateMachines_Behavior class attributes and methods

# StateMachines_BehaviorStateMachines_StateMachine class attributes and methods

# Behavior class attributes and methods

# Region class attributes and methods

# Transition class attributes and methods

# StateMachines_BehaviorStateMachines_NamedElement class attributes and methods

# StateMachines_BehaviorStateMachines_Vertex class attributes and methods

# NamedElement class attributes and methods

# Trigger class attributes and methods

# Constraint class attributes and methods

# StateMachines_BehaviorStateMachines_Transition class attributes and methods
StateMachines_BehaviorStateMachines_Transition_kind: Property = Property(name="kind", type=StringType)
StateMachines_BehaviorStateMachines_Transition.attributes={StateMachines_BehaviorStateMachines_Transition_kind}

# StateMachines_BehaviorStateMachines_ConnectionPointReference class attributes and methods

# StateMachines_BehaviorStateMachines_State class attributes and methods
StateMachines_BehaviorStateMachines_State_isComposite: Property = Property(name="isComposite", type=BooleanType)
StateMachines_BehaviorStateMachines_State_isOrthogonal: Property = Property(name="isOrthogonal", type=BooleanType)
StateMachines_BehaviorStateMachines_State_isSimple: Property = Property(name="isSimple", type=BooleanType)
StateMachines_BehaviorStateMachines_State_isSubmachineState: Property = Property(name="isSubmachineState", type=BooleanType)
StateMachines_BehaviorStateMachines_State.attributes={StateMachines_BehaviorStateMachines_State_isOrthogonal, StateMachines_BehaviorStateMachines_State_isComposite, StateMachines_BehaviorStateMachines_State_isSimple, StateMachines_BehaviorStateMachines_State_isSubmachineState}

# BehaviorStateMachines_Vertex class attributes and methods

# StateMachines_BehaviorStateMachines_Constraint class attributes and methods

# StateMachines_BehaviorStateMachines_Trigger class attributes and methods

# StateMachines_BehaviorStateMachines_Pseudostate class attributes and methods

# StateMachines_BehaviorStateMachines_FinalState class attributes and methods

# ConnectionPointReference class attributes and methods

# StateMachines_ProtocolStateMachines_ProtocolConformance class attributes and methods

# DirectedRelationship class attributes and methods

# ProtocolStateMachine class attributes and methods

# StateMachines_ProtocolStateMachines_DirectedRelationship class attributes and methods

# StateMachines_ProtocolStateMachines_Port class attributes and methods

# StateMachines_ProtocolStateMachines_Interface class attributes and methods

# Classifier class attributes and methods

# StateMachines_BehaviorStateMachines_RedefinableElement class attributes and methods

# StateMachines_BehaviorStateMachines_Classifier class attributes and methods

# StateMachines_BehaviorStateMachines_TimeEvent class attributes and methods

# StateMachines_ProtocolStateMachines_ProtocolStateMachine class attributes and methods

# ProtocolConformance class attributes and methods

# StateMachines_ProtocolStateMachines_ProtocolTransition class attributes and methods

# Operation class attributes and methods

# StateMachines_ProtocolStateMachines_Operation class attributes and methods

# Relationships
connectionPoint2: BinaryAssociation = BinaryAssociation(
    name="connectionPoint2",
    ends={
        Property(name="Pseudostate", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_StateMachine", type=Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachineState3: BinaryAssociation = BinaryAssociation(
    name="submachineState3",
    ends={
        Property(name="5", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=State, multiplicity=Multiplicity(0, 9999))
    }
)
extendedStateMachine6: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine6",
    ends={
        Property(name="StateMachine", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_StateMachine7", type=StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex8: BinaryAssociation = BinaryAssociation(
    name="subvertex8",
    ends={
        Property(name="10", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="1", type=StateMachines_BehaviorStateMachines_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
outgoing21: BinaryAssociation = BinaryAssociation(
    name="outgoing21",
    ends={
        Property(name="23", type=StateMachines_BehaviorStateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming24: BinaryAssociation = BinaryAssociation(
    name="incoming24",
    ends={
        Property(name="26", type=StateMachines_BehaviorStateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
container27: BinaryAssociation = BinaryAssociation(
    name="container27",
    ends={
        Property(name="29", type=StateMachines_BehaviorStateMachines_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="28", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine11: BinaryAssociation = BinaryAssociation(
    name="stateMachine11",
    ends={
        Property(name="13", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transition14: BinaryAssociation = BinaryAssociation(
    name="transition14",
    ends={
        Property(name="16", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state17: BinaryAssociation = BinaryAssociation(
    name="state17",
    ends={
        Property(name="19", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion20: BinaryAssociation = BinaryAssociation(
    name="extendedRegion20",
    ends={
        Property(name="Region", type=StateMachines_BehaviorStateMachines_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Region", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
effect36: BinaryAssociation = BinaryAssociation(
    name="effect36",
    ends={
        Property(name="Behavior", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger37: BinaryAssociation = BinaryAssociation(
    name="trigger37",
    ends={
        Property(name="Trigger", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition38", type=Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard39: BinaryAssociation = BinaryAssociation(
    name="guard39",
    ends={
        Property(name="Constraint", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition40", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container41: BinaryAssociation = BinaryAssociation(
    name="container41",
    ends={
        Property(name="43", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="42", type=Region, multiplicity=Multiplicity(0, 1))
    }
)
source30: BinaryAssociation = BinaryAssociation(
    name="source30",
    ends={
        Property(name="32", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="31", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target33: BinaryAssociation = BinaryAssociation(
    name="target33",
    ends={
        Property(name="35", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="34", type=Vertex, multiplicity=Multiplicity(1, 1))
    }
)
exit49: BinaryAssociation = BinaryAssociation(
    name="exit49",
    ends={
        Property(name="Pseudostate50", type=StateMachines_BehaviorStateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_ConnectionPointReference", type=Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
entry51: BinaryAssociation = BinaryAssociation(
    name="entry51",
    ends={
        Property(name="Pseudostate53", type=StateMachines_BehaviorStateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_ConnectionPointReference52", type=Pseudostate, multiplicity=Multiplicity(0, 1))
    }
)
state54: BinaryAssociation = BinaryAssociation(
    name="state54",
    ends={
        Property(name="56", type=StateMachines_BehaviorStateMachines_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="55", type=State, multiplicity=Multiplicity(0, 1))
    }
)
redefinedTransition44: BinaryAssociation = BinaryAssociation(
    name="redefinedTransition44",
    ends={
        Property(name="Transition", type=StateMachines_BehaviorStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_Transition45", type=Transition, multiplicity=Multiplicity(0, 1))
    }
)
state46: BinaryAssociation = BinaryAssociation(
    name="state46",
    ends={
        Property(name="48", type=StateMachines_BehaviorStateMachines_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="47", type=State, multiplicity=Multiplicity(0, 1))
    }
)
doActivity74: BinaryAssociation = BinaryAssociation(
    name="doActivity74",
    ends={
        Property(name="Behavior76", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State75", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry77: BinaryAssociation = BinaryAssociation(
    name="entry77",
    ends={
        Property(name="Behavior79", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State78", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateInvariant80: BinaryAssociation = BinaryAssociation(
    name="stateInvariant80",
    ends={
        Property(name="Constraint82", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State81", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedState83: BinaryAssociation = BinaryAssociation(
    name="redefinedState83",
    ends={
        Property(name="State", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State84", type=State, multiplicity=Multiplicity(0, 1))
    }
)
connection57: BinaryAssociation = BinaryAssociation(
    name="connection57",
    ends={
        Property(name="59", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="58", type=ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint60: BinaryAssociation = BinaryAssociation(
    name="connectionPoint60",
    ends={
        Property(name="62", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="61", type=Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachine63: BinaryAssociation = BinaryAssociation(
    name="submachine63",
    ends={
        Property(name="65", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="64", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region66: BinaryAssociation = BinaryAssociation(
    name="region66",
    ends={
        Property(name="68", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="67", type=Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableTrigger69: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger69",
    ends={
        Property(name="Trigger70", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State", type=Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exit71: BinaryAssociation = BinaryAssociation(
    name="exit71",
    ends={
        Property(name="Behavior73", type=StateMachines_BehaviorStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_BehaviorStateMachines_State72", type=Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conformance85: BinaryAssociation = BinaryAssociation(
    name="conformance85",
    ends={
        Property(name="87", type=StateMachines_ProtocolStateMachines_ProtocolStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="86", type=ProtocolConformance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specificMachine88: BinaryAssociation = BinaryAssociation(
    name="specificMachine88",
    ends={
        Property(name="90", type=StateMachines_ProtocolStateMachines_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="89", type=ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
generalMachine91: BinaryAssociation = BinaryAssociation(
    name="generalMachine91",
    ends={
        Property(name="ProtocolStateMachine", type=StateMachines_ProtocolStateMachines_ProtocolConformance, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolConformance", type=ProtocolStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
protocol92: BinaryAssociation = BinaryAssociation(
    name="protocol92",
    ends={
        Property(name="ProtocolStateMachine93", type=StateMachines_ProtocolStateMachines_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_Port", type=ProtocolStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
protocol94: BinaryAssociation = BinaryAssociation(
    name="protocol94",
    ends={
        Property(name="ProtocolStateMachine95", type=StateMachines_ProtocolStateMachines_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_Interface", type=ProtocolStateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preCondition96: BinaryAssociation = BinaryAssociation(
    name="preCondition96",
    ends={
        Property(name="Constraint97", type=StateMachines_ProtocolStateMachines_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolTransition", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postCondition98: BinaryAssociation = BinaryAssociation(
    name="postCondition98",
    ends={
        Property(name="Constraint100", type=StateMachines_ProtocolStateMachines_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolTransition99", type=Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referred101: BinaryAssociation = BinaryAssociation(
    name="referred101",
    ends={
        Property(name="Operation", type=StateMachines_ProtocolStateMachines_ProtocolTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachines_ProtocolStateMachines_ProtocolTransition102", type=Operation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_Namespace = Generalization(general=BehaviorStateMachines_Namespace, specific=StateMachines_BehaviorStateMachines_Region)
gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_RedefinableElement = Generalization(general=BehaviorStateMachines_RedefinableElement, specific=StateMachines_BehaviorStateMachines_Region)
gen_StateMachines_BehaviorStateMachines_StateMachine_Behavior = Generalization(general=Behavior, specific=StateMachines_BehaviorStateMachines_StateMachine)
gen_StateMachines_BehaviorStateMachines_Vertex_NamedElement = Generalization(general=NamedElement, specific=StateMachines_BehaviorStateMachines_Vertex)
gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_Namespace = Generalization(general=BehaviorStateMachines_Namespace, specific=StateMachines_BehaviorStateMachines_Transition)
gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_RedefinableElement = Generalization(general=BehaviorStateMachines_RedefinableElement, specific=StateMachines_BehaviorStateMachines_Transition)
gen_StateMachines_BehaviorStateMachines_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=StateMachines_BehaviorStateMachines_ConnectionPointReference)
gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Vertex = Generalization(general=BehaviorStateMachines_Vertex, specific=StateMachines_BehaviorStateMachines_State)
gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_RedefinableElement = Generalization(general=BehaviorStateMachines_RedefinableElement, specific=StateMachines_BehaviorStateMachines_State)
gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Namespace = Generalization(general=BehaviorStateMachines_Namespace, specific=StateMachines_BehaviorStateMachines_State)
gen_StateMachines_BehaviorStateMachines_Pseudostate_Vertex = Generalization(general=Vertex, specific=StateMachines_BehaviorStateMachines_Pseudostate)
gen_StateMachines_ProtocolStateMachines_ProtocolConformance_DirectedRelationship = Generalization(general=DirectedRelationship, specific=StateMachines_ProtocolStateMachines_ProtocolConformance)
gen_StateMachines_ProtocolStateMachines_Interface_Classifier = Generalization(general=Classifier, specific=StateMachines_ProtocolStateMachines_Interface)
gen_StateMachines_BehaviorStateMachines_FinalState_State = Generalization(general=State, specific=StateMachines_BehaviorStateMachines_FinalState)
gen_StateMachines_ProtocolStateMachines_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=StateMachines_ProtocolStateMachines_ProtocolStateMachine)
gen_StateMachines_ProtocolStateMachines_ProtocolTransition_Transition = Generalization(general=Transition, specific=StateMachines_ProtocolStateMachines_ProtocolTransition)

# Domain Model
domain_model = DomainModel(
    name="StateMachines",
    types={Pseudostate, State, StateMachine, StateMachines_BehaviorStateMachines_Namespace, StateMachines_BehaviorStateMachines_Region, BehaviorStateMachines_Namespace, BehaviorStateMachines_RedefinableElement, Vertex, StateMachines_BehaviorStateMachines_Behavior, StateMachines_BehaviorStateMachines_StateMachine, Behavior, Region, Transition, StateMachines_BehaviorStateMachines_NamedElement, StateMachines_BehaviorStateMachines_Vertex, NamedElement, Trigger, Constraint, StateMachines_BehaviorStateMachines_Transition, StateMachines_BehaviorStateMachines_ConnectionPointReference, StateMachines_BehaviorStateMachines_State, BehaviorStateMachines_Vertex, StateMachines_BehaviorStateMachines_Constraint, StateMachines_BehaviorStateMachines_Trigger, StateMachines_BehaviorStateMachines_Pseudostate, StateMachines_BehaviorStateMachines_FinalState, ConnectionPointReference, StateMachines_ProtocolStateMachines_ProtocolConformance, DirectedRelationship, ProtocolStateMachine, StateMachines_ProtocolStateMachines_DirectedRelationship, StateMachines_ProtocolStateMachines_Port, StateMachines_ProtocolStateMachines_Interface, Classifier, StateMachines_BehaviorStateMachines_RedefinableElement, StateMachines_BehaviorStateMachines_Classifier, StateMachines_BehaviorStateMachines_TimeEvent, StateMachines_ProtocolStateMachines_ProtocolStateMachine, ProtocolConformance, StateMachines_ProtocolStateMachines_ProtocolTransition, Operation, StateMachines_ProtocolStateMachines_Operation, TransitionKind},
    associations={connectionPoint2, submachineState3, extendedStateMachine6, subvertex8, region0, outgoing21, incoming24, container27, stateMachine11, transition14, state17, extendedRegion20, effect36, trigger37, guard39, container41, source30, target33, exit49, entry51, state54, redefinedTransition44, state46, doActivity74, entry77, stateInvariant80, redefinedState83, connection57, connectionPoint60, submachine63, region66, deferrableTrigger69, exit71, conformance85, specificMachine88, generalMachine91, protocol92, protocol94, preCondition96, postCondition98, referred101},
    generalizations={gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_Namespace, gen_StateMachines_BehaviorStateMachines_Region_BehaviorStateMachines_RedefinableElement, gen_StateMachines_BehaviorStateMachines_StateMachine_Behavior, gen_StateMachines_BehaviorStateMachines_Vertex_NamedElement, gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_Namespace, gen_StateMachines_BehaviorStateMachines_Transition_BehaviorStateMachines_RedefinableElement, gen_StateMachines_BehaviorStateMachines_ConnectionPointReference_Vertex, gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Vertex, gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_RedefinableElement, gen_StateMachines_BehaviorStateMachines_State_BehaviorStateMachines_Namespace, gen_StateMachines_BehaviorStateMachines_Pseudostate_Vertex, gen_StateMachines_ProtocolStateMachines_ProtocolConformance_DirectedRelationship, gen_StateMachines_ProtocolStateMachines_Interface_Classifier, gen_StateMachines_BehaviorStateMachines_FinalState_State, gen_StateMachines_ProtocolStateMachines_ProtocolStateMachine_StateMachine, gen_StateMachines_ProtocolStateMachines_ProtocolTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)