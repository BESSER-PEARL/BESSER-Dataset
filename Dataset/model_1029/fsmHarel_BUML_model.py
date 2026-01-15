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
fsm_AbstractState = Class(name="fsm::AbstractState", is_abstract=True)
fsm_Transition = Class(name="fsm::Transition")
fsm_State = Class(name="fsm::State")
fsm_Trigger = Class(name="fsm::Trigger")
fsm_Statement = Class(name="fsm::Statement", is_abstract=True)
fsm_Constraint = Class(name="fsm::Constraint")
fsm_NotTrigger = Class(name="fsm::NotTrigger")
Trigger = Class(name="Trigger")
fsm_AndTrigger = Class(name="fsm::AndTrigger")
fsm_OrTrigger = Class(name="fsm::OrTrigger")
AbstractState = Class(name="AbstractState")
fsm_Program = Class(name="fsm::Program")
fsm_Junction = Class(name="fsm::Junction")
fsm_Conditional = Class(name="fsm::Conditional")
fsm_FinalState = Class(name="fsm::FinalState")
State = Class(name="State")
Statement = Class(name="Statement")
fsm_NamedElement = Class(name="fsm::NamedElement")
fsm_Pseudostate = Class(name="fsm::Pseudostate", is_abstract=True)
fsm_InitialState = Class(name="fsm::InitialState")
Pseudostate = Class(name="Pseudostate")
fsm_Fork = Class(name="fsm::Fork")
fsm_Join = Class(name="fsm::Join")
fsm_DeepHistory = Class(name="fsm::DeepHistory")
fsm_ShallowHistory = Class(name="fsm::ShallowHistory")

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_Region class attributes and methods

# fsm_AbstractState class attributes and methods

# fsm_Transition class attributes and methods

# fsm_State class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_Statement class attributes and methods

# fsm_Constraint class attributes and methods

# fsm_NotTrigger class attributes and methods

# Trigger class attributes and methods

# fsm_AndTrigger class attributes and methods

# fsm_OrTrigger class attributes and methods

# AbstractState class attributes and methods

# fsm_Program class attributes and methods

# fsm_Junction class attributes and methods

# fsm_Conditional class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# Statement class attributes and methods

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_Pseudostate class attributes and methods

# fsm_InitialState class attributes and methods

# Pseudostate class attributes and methods

# fsm_Fork class attributes and methods

# fsm_Join class attributes and methods

# fsm_DeepHistory class attributes and methods

# fsm_ShallowHistory class attributes and methods

# Relationships
regions0: BinaryAssociation = BinaryAssociation(
    name="regions0",
    ends={
        Property(name="fsm_Region", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subvertex1: BinaryAssociation = BinaryAssociation(
    name="subvertex1",
    ends={
        Property(name="2", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="fsm_Transition", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Region4", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerState5: BinaryAssociation = BinaryAssociation(
    name="ownerState5",
    ends={
        Property(name="7", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="10", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
exit21: BinaryAssociation = BinaryAssociation(
    name="exit21",
    ends={
        Property(name="fsm_Program23", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State22", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRegions24: BinaryAssociation = BinaryAssociation(
    name="ownedRegions24",
    ends={
        Property(name="26", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=fsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger27: BinaryAssociation = BinaryAssociation(
    name="trigger27",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition28", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target29: BinaryAssociation = BinaryAssociation(
    name="target29",
    ends={
        Property(name="31", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="30", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source32: BinaryAssociation = BinaryAssociation(
    name="source32",
    ends={
        Property(name="34", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="33", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
effect35: BinaryAssociation = BinaryAssociation(
    name="effect35",
    ends={
        Property(name="fsm_Statement", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition36", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard37: BinaryAssociation = BinaryAssociation(
    name="guard37",
    ends={
        Property(name="fsm_Constraint", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition38", type=fsm_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trigger39: BinaryAssociation = BinaryAssociation(
    name="trigger39",
    ends={
        Property(name="fsm_Trigger40", type=fsm_NotTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_NotTrigger", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
left41: BinaryAssociation = BinaryAssociation(
    name="left41",
    ends={
        Property(name="fsm_Trigger42", type=fsm_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_AndTrigger", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
right43: BinaryAssociation = BinaryAssociation(
    name="right43",
    ends={
        Property(name="fsm_Trigger45", type=fsm_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_AndTrigger44", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
left46: BinaryAssociation = BinaryAssociation(
    name="left46",
    ends={
        Property(name="fsm_Trigger47", type=fsm_OrTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_OrTrigger", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="13", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion14: BinaryAssociation = BinaryAssociation(
    name="ownerRegion14",
    ends={
        Property(name="16", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=fsm_Region, multiplicity=Multiplicity(1, 1))
    }
)
doActivity17: BinaryAssociation = BinaryAssociation(
    name="doActivity17",
    ends={
        Property(name="fsm_Program", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry18: BinaryAssociation = BinaryAssociation(
    name="entry18",
    ends={
        Property(name="fsm_Program20", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State19", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements51: BinaryAssociation = BinaryAssociation(
    name="statements51",
    ends={
        Property(name="fsm_Statement53", type=fsm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Program52", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right48: BinaryAssociation = BinaryAssociation(
    name="right48",
    ends={
        Property(name="fsm_Trigger50", type=fsm_OrTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_OrTrigger49", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_Region_NamedElement = Generalization(general=NamedElement, specific=fsm_Region)
gen_fsm_AbstractState_NamedElement = Generalization(general=NamedElement, specific=fsm_AbstractState)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_NotTrigger_Trigger = Generalization(general=Trigger, specific=fsm_NotTrigger)
gen_fsm_AndTrigger_Trigger = Generalization(general=Trigger, specific=fsm_AndTrigger)
gen_fsm_OrTrigger_Trigger = Generalization(general=Trigger, specific=fsm_OrTrigger)
gen_fsm_State_AbstractState = Generalization(general=AbstractState, specific=fsm_State)
gen_fsm_Junction_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Junction)
gen_fsm_Conditional_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Conditional)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_Program_Statement = Generalization(general=Statement, specific=fsm_Program)
gen_fsm_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsm_Pseudostate)
gen_fsm_InitialState_Pseudostate = Generalization(general=Pseudostate, specific=fsm_InitialState)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)
gen_fsm_DeepHistory_Pseudostate = Generalization(general=Pseudostate, specific=fsm_DeepHistory)
gen_fsm_ShallowHistory_Pseudostate = Generalization(general=Pseudostate, specific=fsm_ShallowHistory)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, NamedElement, fsm_Region, fsm_AbstractState, fsm_Transition, fsm_State, fsm_Trigger, fsm_Statement, fsm_Constraint, fsm_NotTrigger, Trigger, fsm_AndTrigger, fsm_OrTrigger, AbstractState, fsm_Program, fsm_Junction, fsm_Conditional, fsm_FinalState, State, Statement, fsm_NamedElement, fsm_Pseudostate, fsm_InitialState, Pseudostate, fsm_Fork, fsm_Join, fsm_DeepHistory, fsm_ShallowHistory},
    associations={regions0, subvertex1, transitions3, ownerState5, incoming8, exit21, ownedRegions24, trigger27, target29, source32, effect35, guard37, trigger39, left41, right43, left46, outgoing11, ownerRegion14, doActivity17, entry18, statements51, right48},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_Region_NamedElement, gen_fsm_AbstractState_NamedElement, gen_fsm_Transition_NamedElement, gen_fsm_NotTrigger_Trigger, gen_fsm_AndTrigger_Trigger, gen_fsm_OrTrigger_Trigger, gen_fsm_State_AbstractState, gen_fsm_Junction_Pseudostate, gen_fsm_Conditional_Pseudostate, gen_fsm_FinalState_State, gen_fsm_Program_Statement, gen_fsm_Pseudostate_AbstractState, gen_fsm_InitialState_Pseudostate, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate, gen_fsm_DeepHistory_Pseudostate, gen_fsm_ShallowHistory_Pseudostate},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)