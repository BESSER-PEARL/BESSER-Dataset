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
NamedElement = Class(name="NamedElement")
statemachine_StateMachineDescription = Class(name="statemachine::StateMachineDescription", is_abstract=True)
statemachine_AbstractState = Class(name="statemachine::AbstractState", is_abstract=True)
statemachine_NamedElement = Class(name="statemachine::NamedElement", is_abstract=True)
ObeoDSMObject = Class(name="ObeoDSMObject")
statemachine_StateMachine = Class(name="statemachine::StateMachine")
StateMachineDescription = Class(name="StateMachineDescription")
Behaviour = Class(name="Behaviour")
statemachine_Region = Class(name="statemachine::Region")
statemachine_State = Class(name="statemachine::State")
AbstractState = Class(name="AbstractState")
statemachine_InitialState = Class(name="statemachine::InitialState")
statemachine_FinalState = Class(name="statemachine::FinalState")
statemachine_Transition = Class(name="statemachine::Transition")

# NamedElement class attributes and methods

# statemachine_StateMachineDescription class attributes and methods

# statemachine_AbstractState class attributes and methods

# statemachine_NamedElement class attributes and methods
statemachine_NamedElement_name: Property = Property(name="name", type=StringType)
statemachine_NamedElement.attributes={statemachine_NamedElement_name}

# ObeoDSMObject class attributes and methods

# statemachine_StateMachine class attributes and methods

# StateMachineDescription class attributes and methods

# Behaviour class attributes and methods

# statemachine_Region class attributes and methods

# statemachine_State class attributes and methods

# AbstractState class attributes and methods

# statemachine_InitialState class attributes and methods

# statemachine_FinalState class attributes and methods

# statemachine_Transition class attributes and methods
statemachine_Transition_guard: Property = Property(name="guard", type=StringType)
statemachine_Transition.attributes={statemachine_Transition_guard}

# Relationships
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="statemachine_AbstractState", type=statemachine_StateMachineDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachineDescription", type=statemachine_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regions0: BinaryAssociation = BinaryAssociation(
    name="regions0",
    ends={
        Property(name="statemachine_Region", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="AbstractState9", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachineDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachineDescription3", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions4: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions4",
    ends={
        Property(name="Transition", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outcomingTransitions5: BinaryAssociation = BinaryAssociation(
    name="outcomingTransitions5",
    ends={
        Property(name="Transition6", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
from7: BinaryAssociation = BinaryAssociation(
    name="from7",
    ends={
        Property(name="AbstractState", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outcomingTransitions", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_statemachine_State_AbstractState = Generalization(general=AbstractState, specific=statemachine_State)
gen_statemachine_State_NamedElement = Generalization(general=NamedElement, specific=statemachine_State)
gen_statemachine_StateMachineDescription_NamedElement = Generalization(general=NamedElement, specific=statemachine_StateMachineDescription)
gen_statemachine_NamedElement_ObeoDSMObject = Generalization(general=ObeoDSMObject, specific=statemachine_NamedElement)
gen_statemachine_StateMachine_StateMachineDescription = Generalization(general=StateMachineDescription, specific=statemachine_StateMachine)
gen_statemachine_StateMachine_Behaviour = Generalization(general=Behaviour, specific=statemachine_StateMachine)
gen_statemachine_InitialState_AbstractState = Generalization(general=AbstractState, specific=statemachine_InitialState)
gen_statemachine_Region_StateMachineDescription = Generalization(general=StateMachineDescription, specific=statemachine_Region)
gen_statemachine_AbstractState_ObeoDSMObject = Generalization(general=ObeoDSMObject, specific=statemachine_AbstractState)
gen_statemachine_Transition_ObeoDSMObject = Generalization(general=ObeoDSMObject, specific=statemachine_Transition)
gen_statemachine_FinalState_AbstractState = Generalization(general=AbstractState, specific=statemachine_FinalState)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={NamedElement, statemachine_StateMachineDescription, statemachine_AbstractState, statemachine_NamedElement, ObeoDSMObject, statemachine_StateMachine, StateMachineDescription, Behaviour, statemachine_Region, statemachine_State, AbstractState, statemachine_InitialState, statemachine_FinalState, statemachine_Transition},
    associations={states1, regions0, to8, transitions2, incomingTransitions4, outcomingTransitions5, from7},
    generalizations={gen_statemachine_State_AbstractState, gen_statemachine_State_NamedElement, gen_statemachine_StateMachineDescription_NamedElement, gen_statemachine_NamedElement_ObeoDSMObject, gen_statemachine_StateMachine_StateMachineDescription, gen_statemachine_StateMachine_Behaviour, gen_statemachine_InitialState_AbstractState, gen_statemachine_Region_StateMachineDescription, gen_statemachine_AbstractState_ObeoDSMObject, gen_statemachine_Transition_ObeoDSMObject, gen_statemachine_FinalState_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)