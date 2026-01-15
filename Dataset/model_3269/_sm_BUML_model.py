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
SM_StateMachine = Class(name="SM::StateMachine")
SM_State = Class(name="SM::State")
SM_InitialState = Class(name="SM::InitialState")
State = Class(name="State")
SM_FinalState = Class(name="SM::FinalState")

# SM_StateMachine class attributes and methods

# SM_State class attributes and methods
SM_State_name: Property = Property(name="name", type=StringType)
SM_State.attributes={SM_State_name}

# SM_InitialState class attributes and methods

# State class attributes and methods

# SM_FinalState class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="SM_State", type=SM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SM_StateMachine", type=SM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SM_InitialState_State = Generalization(general=State, specific=SM_InitialState)
gen_SM_FinalState_State = Generalization(general=State, specific=SM_FinalState)

# Domain Model
domain_model = DomainModel(
    name="SM",
    types={SM_StateMachine, SM_State, SM_InitialState, State, SM_FinalState},
    associations={ownedState0},
    generalizations={gen_SM_InitialState_State, gen_SM_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)