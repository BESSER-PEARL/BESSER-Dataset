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
FSM_StateMachine = Class(name="FSM::StateMachine")
FSM_Transition = Class(name="FSM::Transition")
FSM_RegularState = Class(name="FSM::RegularState")
FSM_AbstractState = Class(name="FSM::AbstractState", is_abstract=True)
FSM_CompositeState = Class(name="FSM::CompositeState")
FSM_InitialState = Class(name="FSM::InitialState")
AbstractState = Class(name="AbstractState")

# FSM_StateMachine class attributes and methods
FSM_StateMachine_name: Property = Property(name="name", type=StringType)
FSM_StateMachine.attributes={FSM_StateMachine_name}

# FSM_Transition class attributes and methods
FSM_Transition_label: Property = Property(name="label", type=StringType)
FSM_Transition.attributes={FSM_Transition_label}

# FSM_RegularState class attributes and methods

# FSM_AbstractState class attributes and methods
FSM_AbstractState_name: Property = Property(name="name", type=StringType)
FSM_AbstractState.attributes={FSM_AbstractState_name}

# FSM_CompositeState class attributes and methods

# FSM_InitialState class attributes and methods

# AbstractState class attributes and methods

# Relationships
states12: BinaryAssociation = BinaryAssociation(
    name="states12",
    ends={
        Property(name="AbstractState13", type=FSM_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeState", type=FSM_AbstractState, multiplicity=Multiplicity(0, 9999))
    }
)
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="Transition", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=FSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="AbstractState", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine2", type=FSM_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine3: BinaryAssociation = BinaryAssociation(
    name="stateMachine3",
    ends={
        Property(name="StateMachine", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=FSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="FSM_AbstractState", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_Transition", type=FSM_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="FSM_AbstractState7", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_Transition6", type=FSM_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine8: BinaryAssociation = BinaryAssociation(
    name="stateMachine8",
    ends={
        Property(name="StateMachine9", type=FSM_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=FSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
compositeState10: BinaryAssociation = BinaryAssociation(
    name="compositeState10",
    ends={
        Property(name="CompositeState", type=FSM_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states11", type=FSM_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_FSM_InitialState_AbstractState = Generalization(general=AbstractState, specific=FSM_InitialState)
gen_FSM_RegularState_AbstractState = Generalization(general=AbstractState, specific=FSM_RegularState)
gen_FSM_CompositeState_AbstractState = Generalization(general=AbstractState, specific=FSM_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="FSM",
    types={FSM_StateMachine, FSM_Transition, FSM_RegularState, FSM_AbstractState, FSM_CompositeState, FSM_InitialState, AbstractState},
    associations={states12, transitions0, states1, stateMachine3, source4, target5, stateMachine8, compositeState10},
    generalizations={gen_FSM_InitialState_AbstractState, gen_FSM_RegularState_AbstractState, gen_FSM_CompositeState_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)