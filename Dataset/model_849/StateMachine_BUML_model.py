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
fsm_Model = Class(name="fsm::Model")
NamedElement = Class(name="NamedElement")
fsm_FiniteStateMachine = Class(name="fsm::FiniteStateMachine")
fsm_State = Class(name="fsm::State")
fsm_NamedElement = Class(name="fsm::NamedElement", is_abstract=True)
fsm_Transition = Class(name="fsm::Transition")

# fsm_Model class attributes and methods

# NamedElement class attributes and methods

# fsm_FiniteStateMachine class attributes and methods

# fsm_State class attributes and methods

# fsm_NamedElement class attributes and methods
fsm_NamedElement_name: Property = Property(name="name", type=StringType)
fsm_NamedElement.attributes={fsm_NamedElement_name}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output}

# Relationships
machine0: BinaryAssociation = BinaryAssociation(
    name="machine0",
    ends={
        Property(name="fsm_FiniteStateMachine", type=fsm_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Model", type=fsm_FiniteStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="fsm_State7", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="State9", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="leavingTransitions", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=fsm_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine", type=fsm_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial2: BinaryAssociation = BinaryAssociation(
    name="initial2",
    ends={
        Property(name="fsm_State", type=fsm_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FiniteStateMachine3", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
leavingTransitions4: BinaryAssociation = BinaryAssociation(
    name="leavingTransitions4",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machine5: BinaryAssociation = BinaryAssociation(
    name="machine5",
    ends={
        Property(name="FiniteStateMachine", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=fsm_FiniteStateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fsm_Model_NamedElement = Generalization(general=NamedElement, specific=fsm_Model)
gen_fsm_FiniteStateMachine_NamedElement = Generalization(general=NamedElement, specific=fsm_FiniteStateMachine)
gen_fsm_State_NamedElement = Generalization(general=NamedElement, specific=fsm_State)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Model, NamedElement, fsm_FiniteStateMachine, fsm_State, fsm_NamedElement, fsm_Transition},
    associations={machine0, target6, source8, states1, initial2, leavingTransitions4, machine5},
    generalizations={gen_fsm_Model_NamedElement, gen_fsm_FiniteStateMachine_NamedElement, gen_fsm_State_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)