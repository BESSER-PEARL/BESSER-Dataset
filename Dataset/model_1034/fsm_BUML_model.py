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
fsm_StateMachine = Class(name="fsm::StateMachine")
NamedElement = Class(name="NamedElement")
fsm_Region = Class(name="fsm::Region")
fsm_Constraint = Class(name="fsm::Constraint")
fsm_Pseudostate = Class(name="fsm::Pseudostate", is_abstract=True)
fsm_InitialState = Class(name="fsm::InitialState")
Pseudostate = Class(name="Pseudostate")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")
fsm_NamedElement = Class(name="fsm::NamedElement")
fsm_AbstractState = Class(name="fsm::AbstractState", is_abstract=True)
fsm_Transition = Class(name="fsm::Transition")
fsm_State = Class(name="fsm::State")
AbstractState = Class(name="AbstractState")
fsm_Trigger = Class(name="fsm::Trigger")

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_Region class attributes and methods

# fsm_Constraint class attributes and methods
fsm_Constraint_m_eval: Method = Method(name="eval", parameters={Parameter(name='context')}, type=BooleanType)
fsm_Constraint.methods={fsm_Constraint_m_eval}

# fsm_Pseudostate class attributes and methods

# fsm_InitialState class attributes and methods

# Pseudostate class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_AbstractState class attributes and methods

# fsm_Transition class attributes and methods

# fsm_State class attributes and methods

# AbstractState class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# Relationships
regions0: BinaryAssociation = BinaryAssociation(
    name="regions0",
    ends={
        Property(name="Region", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerStateMachine", type=fsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger9: BinaryAssociation = BinaryAssociation(
    name="trigger9",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition10", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="AbstractState12", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="AbstractState14", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
guard15: BinaryAssociation = BinaryAssociation(
    name="guard15",
    ends={
        Property(name="fsm_Constraint", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition16", type=fsm_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subvertex1: BinaryAssociation = BinaryAssociation(
    name="subvertex1",
    ends={
        Property(name="AbstractState", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerRegion", type=fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="fsm_Transition", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerStateMachine3: BinaryAssociation = BinaryAssociation(
    name="ownerStateMachine3",
    ends={
        Property(name="StateMachine", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="regions", type=fsm_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition6", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion7: BinaryAssociation = BinaryAssociation(
    name="ownerRegion7",
    ends={
        Property(name="Region8", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=fsm_Region, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsm_Pseudostate)
gen_fsm_InitialState_Pseudostate = Generalization(general=Pseudostate, specific=fsm_InitialState)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_Region_NamedElement = Generalization(general=NamedElement, specific=fsm_Region)
gen_fsm_AbstractState_NamedElement = Generalization(general=NamedElement, specific=fsm_AbstractState)
gen_fsm_State_AbstractState = Generalization(general=AbstractState, specific=fsm_State)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, NamedElement, fsm_Region, fsm_Constraint, fsm_Pseudostate, fsm_InitialState, Pseudostate, fsm_FinalState, State, fsm_NamedElement, fsm_AbstractState, fsm_Transition, fsm_State, AbstractState, fsm_Trigger},
    associations={regions0, trigger9, target11, source13, guard15, subvertex1, transitions2, ownerStateMachine3, incoming4, outgoing5, ownerRegion7},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_Pseudostate_AbstractState, gen_fsm_InitialState_Pseudostate, gen_fsm_FinalState_State, gen_fsm_Region_NamedElement, gen_fsm_AbstractState_NamedElement, gen_fsm_State_AbstractState, gen_fsm_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)