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
etatma_StateMachine = Class(name="etatma::StateMachine")
etatma_Transition = Class(name="etatma::Transition")
etatma_State = Class(name="etatma::State")

# etatma_StateMachine class attributes and methods
etatma_StateMachine_name: Property = Property(name="name", type=StringType)
etatma_StateMachine.attributes={etatma_StateMachine_name}

# etatma_Transition class attributes and methods
etatma_Transition_name: Property = Property(name="name", type=StringType)
etatma_Transition.attributes={etatma_Transition_name}

# etatma_State class attributes and methods
etatma_State_name: Property = Property(name="name", type=StringType)
etatma_State.attributes={etatma_State_name}

# Relationships
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="etatma_Transition", type=etatma_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="etatma_StateMachine", type=etatma_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="etatma_State", type=etatma_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="etatma_StateMachine2", type=etatma_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from3: BinaryAssociation = BinaryAssociation(
    name="from3",
    ends={
        Property(name="State", type=etatma_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=etatma_State, multiplicity=Multiplicity(0, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="State5", type=etatma_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=etatma_State, multiplicity=Multiplicity(0, 1))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition", type=etatma_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=etatma_Transition, multiplicity=Multiplicity(0, 1))
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="Transition8", type=etatma_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=etatma_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="etatma",
    types={etatma_StateMachine, etatma_Transition, etatma_State},
    associations={transition0, state1, from3, to4, outgoing6, incoming7},
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