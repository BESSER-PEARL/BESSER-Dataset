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
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

TimeEventKind: Enumeration = Enumeration(
    name="TimeEventKind",
    literals={
            EnumerationLiteral(name="AT"),
			EnumerationLiteral(name="AFTER")
    }
)

ChangeEventKind: Enumeration = Enumeration(
    name="ChangeEventKind",
    literals={
            EnumerationLiteral(name="WHEN")
    }
)

# Classes
capellacommon_AbstractCapabilityPkg = Class(name="capellacommon::AbstractCapabilityPkg", is_abstract=True)
Structure = Class(name="Structure")
capellacommon_GenericTrace = Class(name="capellacommon::GenericTrace")
CapellaElement = Class(name="CapellaElement")
TraceableElement = Class(name="TraceableElement")
ModelElement = Class(name="ModelElement")
capellacommon_TraceableElement = Class(name="capellacommon::TraceableElement")
NamedElement = Class(name="NamedElement")
capellacommon_AbstractState = Class(name="capellacommon::AbstractState", is_abstract=True)
capellacommon_StateTransition = Class(name="capellacommon::StateTransition")
capellacommon_State = Class(name="capellacommon::State")
AbstractState = Class(name="AbstractState")
capellacommon_AbstractFunction = Class(name="capellacommon::AbstractFunction")
capellacommon_FunctionalChain = Class(name="capellacommon::FunctionalChain")
capellacommon_StateMachine = Class(name="capellacommon::StateMachine")
AbstractBehavior = Class(name="AbstractBehavior")
capellacommon_Region = Class(name="capellacommon::Region")
capellacommon_AbstractEvent = Class(name="capellacommon::AbstractEvent")
capellacommon_Mode = Class(name="capellacommon::Mode")
State = Class(name="State")
capellacommon_FinalState = Class(name="capellacommon::FinalState")
IState = Class(name="IState")
capellacommon_Constraint = Class(name="capellacommon::Constraint")
capellacommon_AbstractCapability = Class(name="capellacommon::AbstractCapability")
capellacommon_Pseudostate = Class(name="capellacommon::Pseudostate", is_abstract=True)
capellacommon_InitialPseudoState = Class(name="capellacommon::InitialPseudoState")
Pseudostate = Class(name="Pseudostate")
capellacommon_JoinPseudoState = Class(name="capellacommon::JoinPseudoState")
capellacommon_ForkPseudoState = Class(name="capellacommon::ForkPseudoState")
capellacommon_ChoicePseudoState = Class(name="capellacommon::ChoicePseudoState")
capellacommon_TerminatePseudoState = Class(name="capellacommon::TerminatePseudoState")
capellacommon_ShallowHistoryPseudoState = Class(name="capellacommon::ShallowHistoryPseudoState")
capellacommon_EntryPointPseudoState = Class(name="capellacommon::EntryPointPseudoState")
capellacommon_ExitPointPseudoState = Class(name="capellacommon::ExitPointPseudoState")
capellacommon_StateEvent = Class(name="capellacommon::StateEvent", is_abstract=True)
AbstractEvent = Class(name="AbstractEvent")
capellacommon_ChangeEvent = Class(name="capellacommon::ChangeEvent")
StateEvent = Class(name="StateEvent")
capellacommon_TimeEvent = Class(name="capellacommon::TimeEvent")
capellacommon_DeepHistoryPseudoState = Class(name="capellacommon::DeepHistoryPseudoState")

# capellacommon_AbstractCapabilityPkg class attributes and methods

# Structure class attributes and methods

# capellacommon_GenericTrace class attributes and methods

# CapellaElement class attributes and methods

# TraceableElement class attributes and methods

# ModelElement class attributes and methods

# capellacommon_TraceableElement class attributes and methods

# NamedElement class attributes and methods

# capellacommon_AbstractState class attributes and methods

# capellacommon_StateTransition class attributes and methods
capellacommon_StateTransition_kind: Property = Property(name="kind", type=StringType)
capellacommon_StateTransition_triggerDescription: Property = Property(name="triggerDescription", type=StringType)
capellacommon_StateTransition.attributes={capellacommon_StateTransition_kind, capellacommon_StateTransition_triggerDescription}

# capellacommon_State class attributes and methods

# AbstractState class attributes and methods

# capellacommon_AbstractFunction class attributes and methods

# capellacommon_FunctionalChain class attributes and methods

# capellacommon_StateMachine class attributes and methods

# AbstractBehavior class attributes and methods

# capellacommon_Region class attributes and methods

# capellacommon_AbstractEvent class attributes and methods

# capellacommon_Mode class attributes and methods

# State class attributes and methods

# capellacommon_FinalState class attributes and methods

# IState class attributes and methods

# capellacommon_Constraint class attributes and methods

# capellacommon_AbstractCapability class attributes and methods

# capellacommon_Pseudostate class attributes and methods

# capellacommon_InitialPseudoState class attributes and methods

# Pseudostate class attributes and methods

# capellacommon_JoinPseudoState class attributes and methods

# capellacommon_ForkPseudoState class attributes and methods

# capellacommon_ChoicePseudoState class attributes and methods

# capellacommon_TerminatePseudoState class attributes and methods

# capellacommon_ShallowHistoryPseudoState class attributes and methods

# capellacommon_EntryPointPseudoState class attributes and methods

# capellacommon_ExitPointPseudoState class attributes and methods

# capellacommon_StateEvent class attributes and methods

# AbstractEvent class attributes and methods

# capellacommon_ChangeEvent class attributes and methods
capellacommon_ChangeEvent_kind: Property = Property(name="kind", type=StringType)
capellacommon_ChangeEvent.attributes={capellacommon_ChangeEvent_kind}

# StateEvent class attributes and methods

# capellacommon_TimeEvent class attributes and methods
capellacommon_TimeEvent_kind: Property = Property(name="kind", type=StringType)
capellacommon_TimeEvent_time: Property = Property(name="time", type=StringType)
capellacommon_TimeEvent.attributes={capellacommon_TimeEvent_kind, capellacommon_TimeEvent_time}

# capellacommon_DeepHistoryPseudoState class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="capellacommon_TraceableElement", type=capellacommon_GenericTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_GenericTrace", type=capellacommon_TraceableElement, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="capellacommon_TraceableElement3", type=capellacommon_GenericTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_GenericTrace2", type=capellacommon_TraceableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedStates5: BinaryAssociation = BinaryAssociation(
    name="ownedStates5",
    ends={
        Property(name="capellacommon_AbstractState", type=capellacommon_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_Region6", type=capellacommon_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransitions7: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions7",
    ends={
        Property(name="capellacommon_StateTransition", type=capellacommon_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_Region8", type=capellacommon_StateTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
involvedStates9: BinaryAssociation = BinaryAssociation(
    name="involvedStates9",
    ends={
        Property(name="capellacommon_AbstractState11", type=capellacommon_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_Region10", type=capellacommon_AbstractState, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRegions12: BinaryAssociation = BinaryAssociation(
    name="ownedRegions12",
    ends={
        Property(name="capellacommon_Region13", type=capellacommon_State, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_State", type=capellacommon_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
availableAbstractFunctions14: BinaryAssociation = BinaryAssociation(
    name="availableAbstractFunctions14",
    ends={
        Property(name="capellacommon_AbstractFunction", type=capellacommon_State, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_State15", type=capellacommon_AbstractFunction, multiplicity=Multiplicity(0, 9999))
    }
)
ownedRegions4: BinaryAssociation = BinaryAssociation(
    name="ownedRegions4",
    ends={
        Property(name="capellacommon_Region", type=capellacommon_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateMachine", type=capellacommon_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doActivity20: BinaryAssociation = BinaryAssociation(
    name="doActivity20",
    ends={
        Property(name="capellacommon_AbstractEvent", type=capellacommon_State, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_State21", type=capellacommon_AbstractEvent, multiplicity=Multiplicity(0, 1))
    }
)
realizedAbstractStates23: BinaryAssociation = BinaryAssociation(
    name="realizedAbstractStates23",
    ends={
        Property(name="capellacommon_AbstractState24", type=capellacommon_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_AbstractState22", type=capellacommon_AbstractState, multiplicity=Multiplicity(0, 9999))
    }
)
guard25: BinaryAssociation = BinaryAssociation(
    name="guard25",
    ends={
        Property(name="capellacommon_Constraint", type=capellacommon_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateTransition26", type=capellacommon_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
availableFunctionalChains16: BinaryAssociation = BinaryAssociation(
    name="availableFunctionalChains16",
    ends={
        Property(name="capellacommon_FunctionalChain", type=capellacommon_State, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_State17", type=capellacommon_FunctionalChain, multiplicity=Multiplicity(0, 9999))
    }
)
availableAbstractCapabilities18: BinaryAssociation = BinaryAssociation(
    name="availableAbstractCapabilities18",
    ends={
        Property(name="capellacommon_AbstractCapability", type=capellacommon_State, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_State19", type=capellacommon_AbstractCapability, multiplicity=Multiplicity(0, 9999))
    }
)
effect33: BinaryAssociation = BinaryAssociation(
    name="effect33",
    ends={
        Property(name="capellacommon_AbstractEvent35", type=capellacommon_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateTransition34", type=capellacommon_AbstractEvent, multiplicity=Multiplicity(0, 1))
    }
)
triggers36: BinaryAssociation = BinaryAssociation(
    name="triggers36",
    ends={
        Property(name="capellacommon_AbstractEvent38", type=capellacommon_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateTransition37", type=capellacommon_AbstractEvent, multiplicity=Multiplicity(0, 9999))
    }
)
realizedStateTransitions40: BinaryAssociation = BinaryAssociation(
    name="realizedStateTransitions40",
    ends={
        Property(name="capellacommon_StateTransition41", type=capellacommon_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateTransition39", type=capellacommon_StateTransition, multiplicity=Multiplicity(0, 9999))
    }
)
source27: BinaryAssociation = BinaryAssociation(
    name="source27",
    ends={
        Property(name="capellacommon_AbstractState29", type=capellacommon_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateTransition28", type=capellacommon_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="capellacommon_AbstractState32", type=capellacommon_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateTransition31", type=capellacommon_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
condition42: BinaryAssociation = BinaryAssociation(
    name="condition42",
    ends={
        Property(name="capellacommon_Constraint43", type=capellacommon_StateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="capellacommon_StateEvent", type=capellacommon_Constraint, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_capellacommon_AbstractCapabilityPkg_Structure = Generalization(general=Structure, specific=capellacommon_AbstractCapabilityPkg)
gen_capellacommon_GenericTrace_CapellaElement = Generalization(general=CapellaElement, specific=capellacommon_GenericTrace)
gen_capellacommon_GenericTrace_TraceableElement = Generalization(general=TraceableElement, specific=capellacommon_GenericTrace)
gen_capellacommon_GenericTrace_ModelElement = Generalization(general=ModelElement, specific=capellacommon_GenericTrace)
gen_capellacommon_Region_NamedElement = Generalization(general=NamedElement, specific=capellacommon_Region)
gen_capellacommon_State_AbstractState = Generalization(general=AbstractState, specific=capellacommon_State)
gen_capellacommon_StateMachine_CapellaElement = Generalization(general=CapellaElement, specific=capellacommon_StateMachine)
gen_capellacommon_StateMachine_AbstractBehavior = Generalization(general=AbstractBehavior, specific=capellacommon_StateMachine)
gen_capellacommon_Mode_State = Generalization(general=State, specific=capellacommon_Mode)
gen_capellacommon_FinalState_State = Generalization(general=State, specific=capellacommon_FinalState)
gen_capellacommon_AbstractState_NamedElement = Generalization(general=NamedElement, specific=capellacommon_AbstractState)
gen_capellacommon_AbstractState_IState = Generalization(general=IState, specific=capellacommon_AbstractState)
gen_capellacommon_StateTransition_NamedElement = Generalization(general=NamedElement, specific=capellacommon_StateTransition)
gen_capellacommon_StateTransition_CapellaElement = Generalization(general=CapellaElement, specific=capellacommon_StateTransition)
gen_capellacommon_StateTransition_ModelElement = Generalization(general=ModelElement, specific=capellacommon_StateTransition)
gen_capellacommon_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=capellacommon_Pseudostate)
gen_capellacommon_InitialPseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_InitialPseudoState)
gen_capellacommon_JoinPseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_JoinPseudoState)
gen_capellacommon_ForkPseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_ForkPseudoState)
gen_capellacommon_ChoicePseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_ChoicePseudoState)
gen_capellacommon_TerminatePseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_TerminatePseudoState)
gen_capellacommon_ShallowHistoryPseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_ShallowHistoryPseudoState)
gen_capellacommon_EntryPointPseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_EntryPointPseudoState)
gen_capellacommon_ExitPointPseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_ExitPointPseudoState)
gen_capellacommon_StateEvent_NamedElement = Generalization(general=NamedElement, specific=capellacommon_StateEvent)
gen_capellacommon_StateEvent_AbstractEvent = Generalization(general=AbstractEvent, specific=capellacommon_StateEvent)
gen_capellacommon_ChangeEvent_StateEvent = Generalization(general=StateEvent, specific=capellacommon_ChangeEvent)
gen_capellacommon_TimeEvent_StateEvent = Generalization(general=StateEvent, specific=capellacommon_TimeEvent)
gen_capellacommon_DeepHistoryPseudoState_Pseudostate = Generalization(general=Pseudostate, specific=capellacommon_DeepHistoryPseudoState)

# Domain Model
domain_model = DomainModel(
    name="capellacommon",
    types={capellacommon_AbstractCapabilityPkg, Structure, capellacommon_GenericTrace, CapellaElement, TraceableElement, ModelElement, capellacommon_TraceableElement, NamedElement, capellacommon_AbstractState, capellacommon_StateTransition, capellacommon_State, AbstractState, capellacommon_AbstractFunction, capellacommon_FunctionalChain, capellacommon_StateMachine, AbstractBehavior, capellacommon_Region, capellacommon_AbstractEvent, capellacommon_Mode, State, capellacommon_FinalState, IState, capellacommon_Constraint, capellacommon_AbstractCapability, capellacommon_Pseudostate, capellacommon_InitialPseudoState, Pseudostate, capellacommon_JoinPseudoState, capellacommon_ForkPseudoState, capellacommon_ChoicePseudoState, capellacommon_TerminatePseudoState, capellacommon_ShallowHistoryPseudoState, capellacommon_EntryPointPseudoState, capellacommon_ExitPointPseudoState, capellacommon_StateEvent, AbstractEvent, capellacommon_ChangeEvent, StateEvent, capellacommon_TimeEvent, capellacommon_DeepHistoryPseudoState, TransitionKind, TimeEventKind, ChangeEventKind},
    associations={source0, target1, ownedStates5, ownedTransitions7, involvedStates9, ownedRegions12, availableAbstractFunctions14, ownedRegions4, doActivity20, realizedAbstractStates23, guard25, availableFunctionalChains16, availableAbstractCapabilities18, effect33, triggers36, realizedStateTransitions40, source27, target30, condition42},
    generalizations={gen_capellacommon_AbstractCapabilityPkg_Structure, gen_capellacommon_GenericTrace_CapellaElement, gen_capellacommon_GenericTrace_TraceableElement, gen_capellacommon_GenericTrace_ModelElement, gen_capellacommon_Region_NamedElement, gen_capellacommon_State_AbstractState, gen_capellacommon_StateMachine_CapellaElement, gen_capellacommon_StateMachine_AbstractBehavior, gen_capellacommon_Mode_State, gen_capellacommon_FinalState_State, gen_capellacommon_AbstractState_NamedElement, gen_capellacommon_AbstractState_IState, gen_capellacommon_StateTransition_NamedElement, gen_capellacommon_StateTransition_CapellaElement, gen_capellacommon_StateTransition_ModelElement, gen_capellacommon_Pseudostate_AbstractState, gen_capellacommon_InitialPseudoState_Pseudostate, gen_capellacommon_JoinPseudoState_Pseudostate, gen_capellacommon_ForkPseudoState_Pseudostate, gen_capellacommon_ChoicePseudoState_Pseudostate, gen_capellacommon_TerminatePseudoState_Pseudostate, gen_capellacommon_ShallowHistoryPseudoState_Pseudostate, gen_capellacommon_EntryPointPseudoState_Pseudostate, gen_capellacommon_ExitPointPseudoState_Pseudostate, gen_capellacommon_StateEvent_NamedElement, gen_capellacommon_StateEvent_AbstractEvent, gen_capellacommon_ChangeEvent_StateEvent, gen_capellacommon_TimeEvent_StateEvent, gen_capellacommon_DeepHistoryPseudoState_Pseudostate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)