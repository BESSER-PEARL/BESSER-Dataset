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
HSM_State = Class(name="HSM::State")
HSM_Transition = Class(name="HSM::Transition")
HSM_StateMachine = Class(name="HSM::StateMachine")
HSM_CompositeState = Class(name="HSM::CompositeState")
State = Class(name="State")

# HSM_State class attributes and methods
HSM_State_name: Property = Property(name="name", type=StringType)
HSM_State.attributes={HSM_State_name}

# HSM_Transition class attributes and methods

# HSM_StateMachine class attributes and methods
HSM_StateMachine_m_addTransition: Method = Method(name="addTransition", parameters={Parameter(name='trg'), Parameter(name='src')})
HSM_StateMachine.methods={HSM_StateMachine_m_addTransition}

# HSM_CompositeState class attributes and methods

# State class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="HSM_State", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_StateMachine", type=HSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="HSM_Transition", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_StateMachine2", type=HSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="HSM_CompositeState", type=HSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_State4", type=HSM_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="HSM_State7", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition6", type=HSM_State, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="HSM_State10", type=HSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_Transition9", type=HSM_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_HSM_CompositeState_State = Generalization(general=State, specific=HSM_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="HSM",
    types={HSM_State, HSM_Transition, HSM_StateMachine, HSM_CompositeState, State},
    associations={states0, transitions1, owner3, source5, target8},
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