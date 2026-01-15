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
idm_State = Class(name="idm::State")
idm_Transition = Class(name="idm::Transition")
idm_StateMachine = Class(name="idm::StateMachine")

# idm_State class attributes and methods
idm_State_name: Property = Property(name="name", type=StringType)
idm_State.attributes={idm_State_name}

# idm_Transition class attributes and methods
idm_Transition_name: Property = Property(name="name", type=StringType)
idm_Transition.attributes={idm_Transition_name}

# idm_StateMachine class attributes and methods
idm_StateMachine_name: Property = Property(name="name", type=StringType)
idm_StateMachine.attributes={idm_StateMachine_name}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="idm_State", type=idm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="idm_StateMachine", type=idm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="idm_Transition", type=idm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="idm_StateMachine2", type=idm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from3: BinaryAssociation = BinaryAssociation(
    name="from3",
    ends={
        Property(name="Transition", type=idm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=idm_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="Transition5", type=idm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=idm_Transition, multiplicity=Multiplicity(1, 1))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="State", type=idm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=idm_State, multiplicity=Multiplicity(0, 9999))
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="State8", type=idm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=idm_State, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="idm",
    types={idm_State, idm_Transition, idm_StateMachine},
    associations={state0, transition1, from3, to4, outgoing6, incoming7},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)