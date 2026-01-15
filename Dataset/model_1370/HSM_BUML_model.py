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
HSM_HSM_StateMachine = Class(name="HSM::HSM::StateMachine")
HSM_HSM_Transition = Class(name="HSM::HSM::Transition")
HSM_HSM_AbstractState = Class(name="HSM::HSM::AbstractState", is_abstract=True)
HSM_HSM_CompositeState = Class(name="HSM::HSM::CompositeState")
HSM_HSM_RegularState = Class(name="HSM::HSM::RegularState")
HSM_HSM_InitialState = Class(name="HSM::HSM::InitialState")
HSM_AbstractState = Class(name="HSM::AbstractState")

# HSM_HSM_StateMachine class attributes and methods
HSM_HSM_StateMachine_name: Property = Property(name="name", type=StringType)
HSM_HSM_StateMachine.attributes={HSM_HSM_StateMachine_name}

# HSM_HSM_Transition class attributes and methods
HSM_HSM_Transition_label: Property = Property(name="label", type=StringType)
HSM_HSM_Transition.attributes={HSM_HSM_Transition_label}

# HSM_HSM_AbstractState class attributes and methods
HSM_HSM_AbstractState_name: Property = Property(name="name", type=StringType)
HSM_HSM_AbstractState.attributes={HSM_HSM_AbstractState_name}

# HSM_HSM_CompositeState class attributes and methods

# HSM_HSM_RegularState class attributes and methods

# HSM_HSM_InitialState class attributes and methods

# HSM_AbstractState class attributes and methods

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="HSM_Transition", type=HSM_HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=HSM_HSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="HSM_AbstractState", type=HSM_HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine2", type=HSM_HSM_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="HSM_HSM_AbstractState7", type=HSM_HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_HSM_Transition6", type=HSM_HSM_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine8: BinaryAssociation = BinaryAssociation(
    name="stateMachine8",
    ends={
        Property(name="HSM_StateMachine9", type=HSM_HSM_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=HSM_HSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
compositeState10: BinaryAssociation = BinaryAssociation(
    name="compositeState10",
    ends={
        Property(name="HSM_CompositeState", type=HSM_HSM_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states11", type=HSM_HSM_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine3: BinaryAssociation = BinaryAssociation(
    name="stateMachine3",
    ends={
        Property(name="HSM_StateMachine", type=HSM_HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=HSM_HSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="HSM_HSM_AbstractState", type=HSM_HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_HSM_Transition", type=HSM_HSM_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
states12: BinaryAssociation = BinaryAssociation(
    name="states12",
    ends={
        Property(name="HSM_AbstractState13", type=HSM_HSM_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeState", type=HSM_HSM_AbstractState, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_HSM_HSM_RegularState_HSM_AbstractState = Generalization(general=HSM_AbstractState, specific=HSM_HSM_RegularState)
gen_HSM_HSM_CompositeState_HSM_AbstractState = Generalization(general=HSM_AbstractState, specific=HSM_HSM_CompositeState)
gen_HSM_HSM_InitialState_HSM_AbstractState = Generalization(general=HSM_AbstractState, specific=HSM_HSM_InitialState)

# Domain Model
domain_model = DomainModel(
    name="HSM",
    types={HSM_HSM_StateMachine, HSM_HSM_Transition, HSM_HSM_AbstractState, HSM_HSM_CompositeState, HSM_HSM_RegularState, HSM_HSM_InitialState, HSM_AbstractState},
    associations={transitions0, states1, target5, stateMachine8, compositeState10, stateMachine3, source4, states12},
    generalizations={gen_HSM_HSM_RegularState_HSM_AbstractState, gen_HSM_HSM_CompositeState_HSM_AbstractState, gen_HSM_HSM_InitialState_HSM_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)