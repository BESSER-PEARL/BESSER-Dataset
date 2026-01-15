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
HSM_Transition = Class(name="HSM::Transition")
HSM_CompositeState = Class(name="HSM::CompositeState")
HSM_StateMachine = Class(name="HSM::StateMachine")
HSM_State = Class(name="HSM::State")
State = Class(name="State")

# HSM_Transition class attributes and methods

# HSM_CompositeState class attributes and methods

# HSM_StateMachine class attributes and methods
HSM_StateMachine_name: Property = Property(name="name", type=StringType)
HSM_StateMachine_m_addTransition: Method = Method(name="addTransition", parameters={Parameter(name='trg'), Parameter(name='src')})
HSM_StateMachine.attributes={HSM_StateMachine_name}
HSM_StateMachine.methods={HSM_StateMachine_m_addTransition}

# HSM_State class attributes and methods
HSM_State_name: Property = Property(name="name", type=StringType)
HSM_State.attributes={HSM_State_name}

# State class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="HSM_Transition", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_StateMachine", type=HSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container2: BinaryAssociation = BinaryAssociation(
    name="container2",
    ends={
        Property(name="HSM_CompositeState", type=HSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_State", type=HSM_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
machine3: BinaryAssociation = BinaryAssociation(
    name="machine3",
    ends={
        Property(name="StateMachine", type=HSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine", type=HSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="HSM_State6", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition5", type=HSM_State, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="HSM_State9", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition8", type=HSM_State, multiplicity=Multiplicity(1, 1))
    }
)
machine10: BinaryAssociation = BinaryAssociation(
    name="machine10",
    ends={
        Property(name="HSM_StateMachine12", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition11", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HSM_CompositeState_State = Generalization(general=State, specific=HSM_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="HSM",
    types={HSM_Transition, HSM_CompositeState, HSM_StateMachine, HSM_State, State},
    associations={transitions1, container2, machine3, states0, source4, target7, machine10},
    generalizations={gen_HSM_CompositeState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)