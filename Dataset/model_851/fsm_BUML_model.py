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
fsm_NamedElement = Class(name="fsm::NamedElement", is_abstract=True)
fsm_StateMachine = Class(name="fsm::StateMachine")
NamedElement = Class(name="NamedElement")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")
fsm_FSMModel = Class(name="fsm::FSMModel")

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsm_State class attributes and methods
fsm_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
fsm_State.attributes={fsm_State_isFinal}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output}

# fsm_FSMModel class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fsm_State", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial1: BinaryAssociation = BinaryAssociation(
    name="initial1",
    ends={
        Property(name="fsm_State3", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_StateMachine2", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="State", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="fsm_State6", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions7: BinaryAssociation = BinaryAssociation(
    name="transitions7",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachines8: BinaryAssociation = BinaryAssociation(
    name="stateMachines8",
    ends={
        Property(name="fsm_StateMachine9", type=fsm_FSMModel, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSMModel", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_StateMachine)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)
gen_fsm_FSMModel_NamedElement = Generalization(general=NamedElement, specific=fsm_FSMModel)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_NamedElement, fsm_StateMachine, NamedElement, fsm_State, fsm_Transition, fsm_FSMModel},
    associations={states0, initial1, source4, target5, transitions7, stateMachines8},
    generalizations={gen_fsm_StateMachine_NamedElement, gen_fsm_State_NamedElement, gen_fsm_FSMModel_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)