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
fsm_Transition = Class(name="fsm::Transition")
fsm_CompositeState = Class(name="fsm::CompositeState")
fsm_InitialState = Class(name="fsm::InitialState")
AbstractState = Class(name="AbstractState")
fsm_RegularState = Class(name="fsm::RegularState")
fsm_Root = Class(name="fsm::Root")
fsm_AbstractState = Class(name="fsm::AbstractState", is_abstract=True)

# fsm_StateMachine class attributes and methods
fsm_StateMachine_name: Property = Property(name="name", type=StringType)
fsm_StateMachine.attributes={fsm_StateMachine_name}

# fsm_Transition class attributes and methods
fsm_Transition_label: Property = Property(name="label", type=StringType)
fsm_Transition.attributes={fsm_Transition_label}

# fsm_CompositeState class attributes and methods

# fsm_InitialState class attributes and methods

# AbstractState class attributes and methods

# fsm_RegularState class attributes and methods

# fsm_Root class attributes and methods

# fsm_AbstractState class attributes and methods
fsm_AbstractState_name: Property = Property(name="name", type=StringType)
fsm_AbstractState.attributes={fsm_AbstractState_name}

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="Transition", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine3: BinaryAssociation = BinaryAssociation(
    name="stateMachine3",
    ends={
        Property(name="StateMachine", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="fsm_AbstractState", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="fsm_AbstractState7", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition6", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine8: BinaryAssociation = BinaryAssociation(
    name="stateMachine8",
    ends={
        Property(name="StateMachine9", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
compositeStates10: BinaryAssociation = BinaryAssociation(
    name="compositeStates10",
    ends={
        Property(name="CompositeState", type=fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states11", type=fsm_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
states12: BinaryAssociation = BinaryAssociation(
    name="states12",
    ends={
        Property(name="AbstractState13", type=fsm_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeStates", type=fsm_AbstractState, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachines14: BinaryAssociation = BinaryAssociation(
    name="stateMachines14",
    ends={
        Property(name="fsm_StateMachine", type=fsm_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Root", type=fsm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="AbstractState", type=fsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine2", type=fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fsm_InitialState_AbstractState = Generalization(general=AbstractState, specific=fsm_InitialState)
gen_fsm_RegularState_AbstractState = Generalization(general=AbstractState, specific=fsm_RegularState)
gen_fsm_CompositeState_AbstractState = Generalization(general=AbstractState, specific=fsm_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_StateMachine, fsm_Transition, fsm_CompositeState, fsm_InitialState, AbstractState, fsm_RegularState, fsm_Root, fsm_AbstractState},
    associations={transitions0, stateMachine3, source4, target5, stateMachine8, compositeStates10, states12, stateMachines14, states1},
    generalizations={gen_fsm_InitialState_AbstractState, gen_fsm_RegularState_AbstractState, gen_fsm_CompositeState_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)