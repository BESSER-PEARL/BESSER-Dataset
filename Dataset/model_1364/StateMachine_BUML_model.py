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
PseudoStateKind: Enumeration = Enumeration(
    name="PseudoStateKind",
    literals={
            EnumerationLiteral(name="initial")
    }
)

# Classes
statemachine_Class = Class(name="statemachine::Class")
statemachine_Transition = Class(name="statemachine::Transition")
BehavioredClassifier = Class(name="BehavioredClassifier")
statemachine_StateMachine = Class(name="statemachine::StateMachine")
Behavior = Class(name="Behavior")
statemachine_Region = Class(name="statemachine::Region")
statemachine_NamedElement = Class(name="statemachine::NamedElement")
statemachine_BehavioredClassifier = Class(name="statemachine::BehavioredClassifier")
statemachine_Behavior = Class(name="statemachine::Behavior")
statemachine_Vertex = Class(name="statemachine::Vertex", is_abstract=True)
statemachine_BehavioralFeature = Class(name="statemachine::BehavioralFeature")
statemachine_OpaqueBehavior = Class(name="statemachine::OpaqueBehavior")
NamedElement = Class(name="NamedElement")
statemachine_Constraint = Class(name="statemachine::Constraint")
statemachine_State = Class(name="statemachine::State")
statemachine_FinalState = Class(name="statemachine::FinalState")
State = Class(name="State")
statemachine_Event = Class(name="statemachine::Event")
statemachine_Trigger = Class(name="statemachine::Trigger")
statemachine_PseudoState = Class(name="statemachine::PseudoState")
Vertex = Class(name="Vertex")
statemachine_MessageEvent = Class(name="statemachine::MessageEvent")
Event = Class(name="Event")
statemachine_CallEvent = Class(name="statemachine::CallEvent")
MessageEvent = Class(name="MessageEvent")
statemachine_Operation = Class(name="statemachine::Operation")
BehavioralFeature = Class(name="BehavioralFeature")

# statemachine_Class class attributes and methods

# statemachine_Transition class attributes and methods

# BehavioredClassifier class attributes and methods

# statemachine_StateMachine class attributes and methods

# Behavior class attributes and methods

# statemachine_Region class attributes and methods

# statemachine_NamedElement class attributes and methods

# statemachine_BehavioredClassifier class attributes and methods

# statemachine_Behavior class attributes and methods

# statemachine_Vertex class attributes and methods

# statemachine_BehavioralFeature class attributes and methods

# statemachine_OpaqueBehavior class attributes and methods
statemachine_OpaqueBehavior_body: Property = Property(name="body", type=StringType)
statemachine_OpaqueBehavior_language: Property = Property(name="language", type=StringType)
statemachine_OpaqueBehavior.attributes={statemachine_OpaqueBehavior_language, statemachine_OpaqueBehavior_body}

# NamedElement class attributes and methods

# statemachine_Constraint class attributes and methods

# statemachine_State class attributes and methods

# statemachine_FinalState class attributes and methods

# State class attributes and methods

# statemachine_Event class attributes and methods

# statemachine_Trigger class attributes and methods

# statemachine_PseudoState class attributes and methods
statemachine_PseudoState_kind: Property = Property(name="kind", type=StringType)
statemachine_PseudoState.attributes={statemachine_PseudoState_kind}

# Vertex class attributes and methods

# statemachine_MessageEvent class attributes and methods

# Event class attributes and methods

# statemachine_CallEvent class attributes and methods

# MessageEvent class attributes and methods

# statemachine_Operation class attributes and methods

# BehavioralFeature class attributes and methods

# Relationships
subvertex3: BinaryAssociation = BinaryAssociation(
    name="subvertex3",
    ends={
        Property(name="Vertex", type=statemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="regionvertex", type=statemachine_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition4: BinaryAssociation = BinaryAssociation(
    name="transition4",
    ends={
        Property(name="Transition", type=statemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="transitionregion", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="Region", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine", type=statemachine_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedBehavior1: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior1",
    ends={
        Property(name="Behavior", type=statemachine_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=statemachine_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machine2: BinaryAssociation = BinaryAssociation(
    name="machine2",
    ends={
        Property(name="StateMachine", type=statemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=statemachine_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="Vertex13", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
transitionregion14: BinaryAssociation = BinaryAssociation(
    name="transitionregion14",
    ends={
        Property(name="Region15", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=statemachine_Region, multiplicity=Multiplicity(1, 1))
    }
)
specification5: BinaryAssociation = BinaryAssociation(
    name="specification5",
    ends={
        Property(name="BehavioralFeature", type=statemachine_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="behavior", type=statemachine_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
context6: BinaryAssociation = BinaryAssociation(
    name="context6",
    ends={
        Property(name="BehavioredClassifier", type=statemachine_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBehavior", type=statemachine_BehavioredClassifier, multiplicity=Multiplicity(0, 1))
    }
)
behaviortransition7: BinaryAssociation = BinaryAssociation(
    name="behaviortransition7",
    ends={
        Property(name="Transition8", type=statemachine_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="effect", type=statemachine_Transition, multiplicity=Multiplicity(0, 1))
    }
)
guard9: BinaryAssociation = BinaryAssociation(
    name="guard9",
    ends={
        Property(name="Constraint", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainttransition", type=statemachine_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="Vertex11", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
eventtrigger25: BinaryAssociation = BinaryAssociation(
    name="eventtrigger25",
    ends={
        Property(name="Trigger", type=statemachine_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="event", type=statemachine_Trigger, multiplicity=Multiplicity(0, 1))
    }
)
trigger16: BinaryAssociation = BinaryAssociation(
    name="trigger16",
    ends={
        Property(name="statemachine_Trigger", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition", type=statemachine_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
effect17: BinaryAssociation = BinaryAssociation(
    name="effect17",
    ends={
        Property(name="Behavior18", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviortransition", type=statemachine_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing19: BinaryAssociation = BinaryAssociation(
    name="outgoing19",
    ends={
        Property(name="Transition20", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming21: BinaryAssociation = BinaryAssociation(
    name="incoming21",
    ends={
        Property(name="Transition22", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
regionvertex23: BinaryAssociation = BinaryAssociation(
    name="regionvertex23",
    ends={
        Property(name="Region24", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=statemachine_Region, multiplicity=Multiplicity(0, 1))
    }
)
constrainttransition33: BinaryAssociation = BinaryAssociation(
    name="constrainttransition33",
    ends={
        Property(name="guard", type=statemachine_Transition, multiplicity=Multiplicity(0, 1)),
        Property(name="Transition34", type=statemachine_Constraint, multiplicity=Multiplicity(1, 1))
    }
)
operation26: BinaryAssociation = BinaryAssociation(
    name="operation26",
    ends={
        Property(name="statemachine_Operation", type=statemachine_CallEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_CallEvent", type=statemachine_Operation, multiplicity=Multiplicity(1, 1))
    }
)
behavior27: BinaryAssociation = BinaryAssociation(
    name="behavior27",
    ends={
        Property(name="Behavior28", type=statemachine_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=statemachine_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
triggertransition29: BinaryAssociation = BinaryAssociation(
    name="triggertransition29",
    ends={
        Property(name="statemachine_Transition31", type=statemachine_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Trigger30", type=statemachine_Transition, multiplicity=Multiplicity(0, 1))
    }
)
event32: BinaryAssociation = BinaryAssociation(
    name="event32",
    ends={
        Property(name="Event", type=statemachine_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="eventtrigger", type=statemachine_Event, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_statemachine_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=statemachine_Class)
gen_statemachine_StateMachine_Behavior = Generalization(general=Behavior, specific=statemachine_StateMachine)
gen_statemachine_OpaqueBehavior_Behavior = Generalization(general=Behavior, specific=statemachine_OpaqueBehavior)
gen_statemachine_Transition_NamedElement = Generalization(general=NamedElement, specific=statemachine_Transition)
gen_statemachine_State_Vertex = Generalization(general=Vertex, specific=statemachine_State)
gen_statemachine_FinalState_State = Generalization(general=State, specific=statemachine_FinalState)
gen_statemachine_Vertex_NamedElement = Generalization(general=NamedElement, specific=statemachine_Vertex)
gen_statemachine_PseudoState_Vertex = Generalization(general=Vertex, specific=statemachine_PseudoState)
gen_statemachine_MessageEvent_Event = Generalization(general=Event, specific=statemachine_MessageEvent)
gen_statemachine_CallEvent_MessageEvent = Generalization(general=MessageEvent, specific=statemachine_CallEvent)
gen_statemachine_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=statemachine_Operation)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Class, statemachine_Transition, BehavioredClassifier, statemachine_StateMachine, Behavior, statemachine_Region, statemachine_NamedElement, statemachine_BehavioredClassifier, statemachine_Behavior, statemachine_Vertex, statemachine_BehavioralFeature, statemachine_OpaqueBehavior, NamedElement, statemachine_Constraint, statemachine_State, statemachine_FinalState, State, statemachine_Event, statemachine_Trigger, statemachine_PseudoState, Vertex, statemachine_MessageEvent, Event, statemachine_CallEvent, MessageEvent, statemachine_Operation, BehavioralFeature, PseudoStateKind},
    associations={subvertex3, transition4, region0, ownedBehavior1, machine2, target12, transitionregion14, specification5, context6, behaviortransition7, guard9, source10, eventtrigger25, trigger16, effect17, outgoing19, incoming21, regionvertex23, constrainttransition33, operation26, behavior27, triggertransition29, event32},
    generalizations={gen_statemachine_Class_BehavioredClassifier, gen_statemachine_StateMachine_Behavior, gen_statemachine_OpaqueBehavior_Behavior, gen_statemachine_Transition_NamedElement, gen_statemachine_State_Vertex, gen_statemachine_FinalState_State, gen_statemachine_Vertex_NamedElement, gen_statemachine_PseudoState_Vertex, gen_statemachine_MessageEvent_Event, gen_statemachine_CallEvent_MessageEvent, gen_statemachine_Operation_BehavioralFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)