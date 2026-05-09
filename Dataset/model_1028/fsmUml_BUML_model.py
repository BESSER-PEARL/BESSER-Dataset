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
fsm_StateMachine = Class(name="fsm_StateMachine")
NamedElement = Class(name="NamedElement")
fsm_Region = Class(name="fsm_Region")
fsm_Constraint = Class(name="fsm_Constraint")
fsm_AndTrigger = Class(name="fsm_AndTrigger")
Trigger = Class(name="Trigger")
fsm_AbstractState = Class(name="fsm_AbstractState", is_abstract=True)
fsm_Transition = Class(name="fsm_Transition")
fsm_State = Class(name="fsm_State")
AbstractState = Class(name="AbstractState")
fsm_Program = Class(name="fsm_Program")
fsm_Trigger = Class(name="fsm_Trigger")
fsm_Statement = Class(name="fsm_Statement", is_abstract=True)
fsm_Pseudostate = Class(name="fsm_Pseudostate", is_abstract=True)
fsm_InitialState = Class(name="fsm_InitialState")
Pseudostate = Class(name="Pseudostate")
fsm_Fork = Class(name="fsm_Fork")
fsm_Join = Class(name="fsm_Join")
fsm_DeepHistory = Class(name="fsm_DeepHistory")
fsm_ShallowHistory = Class(name="fsm_ShallowHistory")
fsm_Junction = Class(name="fsm_Junction")
fsm_Choice = Class(name="fsm_Choice")
fsm_FinalState = Class(name="fsm_FinalState")
State = Class(name="State")
Statement = Class(name="Statement")
fsm_NamedElement = Class(name="fsm_NamedElement")

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_Region class attributes and methods

# fsm_Constraint class attributes and methods

# fsm_AndTrigger class attributes and methods

# Trigger class attributes and methods

# fsm_AbstractState class attributes and methods

# fsm_Transition class attributes and methods

# fsm_State class attributes and methods

# AbstractState class attributes and methods

# fsm_Program class attributes and methods

# fsm_Trigger class attributes and methods
fsm_Trigger_expression: Property = Property(name="expression", type=StringType)
fsm_Trigger.attributes={fsm_Trigger_expression}

# fsm_Statement class attributes and methods

# fsm_Pseudostate class attributes and methods

# fsm_InitialState class attributes and methods

# Pseudostate class attributes and methods

# fsm_Fork class attributes and methods

# fsm_Join class attributes and methods

# fsm_DeepHistory class attributes and methods

# fsm_ShallowHistory class attributes and methods

# fsm_Junction class attributes and methods

# fsm_Choice class attributes and methods

# fsm_FinalState class attributes and methods

# State class attributes and methods

# Statement class attributes and methods

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# Relationships
regions0: BinaryAssociation = BinaryAssociation(
    name="regions0",
    ends={
        Property(name="fsm_Region", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
effect24: BinaryAssociation = BinaryAssociation(
    name="effect24",
    ends={
        Property(name="fsm_Statement", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition25", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard26: BinaryAssociation = BinaryAssociation(
    name="guard26",
    ends={
        Property(name="fsm_Constraint", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition27", type=fsm_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
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
        Property(name="fsm_Region3", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownerState4: BinaryAssociation = BinaryAssociation(
    name="ownerState4",
    ends={
        Property(name="State", type=fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRegions", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition7", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
ownerRegion8: BinaryAssociation = BinaryAssociation(
    name="ownerRegion8",
    ends={
        Property(name="Region", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=fsm_Region, multiplicity=Multiplicity(1, 1))
    }
)
doActivity9: BinaryAssociation = BinaryAssociation(
    name="doActivity9",
    ends={
        Property(name="fsm_Program", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry10: BinaryAssociation = BinaryAssociation(
    name="entry10",
    ends={
        Property(name="fsm_Program12", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State11", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit13: BinaryAssociation = BinaryAssociation(
    name="exit13",
    ends={
        Property(name="fsm_Program15", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State14", type=fsm_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRegions16: BinaryAssociation = BinaryAssociation(
    name="ownedRegions16",
    ends={
        Property(name="Region17", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownerState", type=fsm_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger18: BinaryAssociation = BinaryAssociation(
    name="trigger18",
    ends={
        Property(name="fsm_Trigger", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition19", type=fsm_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="AbstractState21", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="AbstractState23", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
left28: BinaryAssociation = BinaryAssociation(
    name="left28",
    ends={
        Property(name="fsm_Trigger29", type=fsm_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_AndTrigger", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
right30: BinaryAssociation = BinaryAssociation(
    name="right30",
    ends={
        Property(name="fsm_Trigger32", type=fsm_AndTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_AndTrigger31", type=fsm_Trigger, multiplicity=Multiplicity(1, 1))
    }
)
statements33: BinaryAssociation = BinaryAssociation(
    name="statements33",
    ends={
        Property(name="fsm_Statement35", type=fsm_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Program34", type=fsm_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_Region_NamedElement = Generalization(general=NamedElement, specific=fsm_Region)
gen_fsm_AndTrigger_Trigger = Generalization(general=Trigger, specific=fsm_AndTrigger)
gen_fsm_AbstractState_NamedElement = Generalization(general=NamedElement, specific=fsm_AbstractState)
gen_fsm_State_AbstractState = Generalization(general=AbstractState, specific=fsm_State)
gen_fsm_Transition_NamedElement = Generalization(general=NamedElement, specific=fsm_Transition)
gen_fsm_Pseudostate_AbstractState = Generalization(general=AbstractState, specific=fsm_Pseudostate)
gen_fsm_InitialState_Pseudostate = Generalization(general=Pseudostate, specific=fsm_InitialState)
gen_fsm_Fork_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Fork)
gen_fsm_Join_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Join)
gen_fsm_DeepHistory_Pseudostate = Generalization(general=Pseudostate, specific=fsm_DeepHistory)
gen_fsm_ShallowHistory_Pseudostate = Generalization(general=Pseudostate, specific=fsm_ShallowHistory)
gen_fsm_Junction_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Junction)
gen_fsm_Choice_Pseudostate = Generalization(general=Pseudostate, specific=fsm_Choice)
gen_fsm_FinalState_State = Generalization(general=State, specific=fsm_FinalState)
gen_fsm_Program_Statement = Generalization(general=Statement, specific=fsm_Program)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, NamedElement, fsm_Region, fsm_Constraint, fsm_AndTrigger, Trigger, fsm_AbstractState, fsm_Transition, fsm_State, AbstractState, fsm_Program, fsm_Trigger, fsm_Statement, fsm_Pseudostate, fsm_InitialState, Pseudostate, fsm_Fork, fsm_Join, fsm_DeepHistory, fsm_ShallowHistory, fsm_Junction, fsm_Choice, fsm_FinalState, State, Statement, fsm_NamedElement},
    associations={regions0, effect24, guard26, subvertex1, transitions2, ownerState4, incoming5, outgoing6, ownerRegion8, doActivity9, entry10, exit13, ownedRegions16, trigger18, target20, source22, left28, right30, statements33},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_Region_NamedElement, gen_fsm_AndTrigger_Trigger, gen_fsm_AbstractState_NamedElement, gen_fsm_State_AbstractState, gen_fsm_Transition_NamedElement, gen_fsm_Pseudostate_AbstractState, gen_fsm_InitialState_Pseudostate, gen_fsm_Fork_Pseudostate, gen_fsm_Join_Pseudostate, gen_fsm_DeepHistory_Pseudostate, gen_fsm_ShallowHistory_Pseudostate, gen_fsm_Junction_Pseudostate, gen_fsm_Choice_Pseudostate, gen_fsm_FinalState_State, gen_fsm_Program_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)