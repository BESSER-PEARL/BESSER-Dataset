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
HSM_CompositeState = Class(name="HSM::CompositeState")
State = Class(name="State")
HSM_InitialState = Class(name="HSM::InitialState")
HSM_FinalState = Class(name="HSM::FinalState")
HSM_StateMachine = Class(name="HSM::StateMachine")

# HSM_State class attributes and methods
HSM_State_name: Property = Property(name="name", type=StringType)
HSM_State.attributes={HSM_State_name}

# HSM_CompositeState class attributes and methods

# State class attributes and methods

# HSM_InitialState class attributes and methods

# HSM_FinalState class attributes and methods

# HSM_StateMachine class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="HSM_State", type=HSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="HSM_StateMachine", type=HSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_HSM_CompositeState_State = Generalization(general=State, specific=HSM_CompositeState)
gen_HSM_InitialState_State = Generalization(general=State, specific=HSM_InitialState)
gen_HSM_FinalState_State = Generalization(general=State, specific=HSM_FinalState)

# Domain Model
domain_model = DomainModel(
    name="HSM",
    types={HSM_State, HSM_CompositeState, State, HSM_InitialState, HSM_FinalState, HSM_StateMachine},
    associations={ownedState0},
    generalizations={gen_HSM_CompositeState_State, gen_HSM_InitialState_State, gen_HSM_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)