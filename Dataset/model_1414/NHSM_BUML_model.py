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
NHSM_StateMachine = Class(name="NHSM::StateMachine")
NHSM_State = Class(name="NHSM::State")
NHSM_Transition = Class(name="NHSM::Transition")

# NHSM_StateMachine class attributes and methods
NHSM_StateMachine_name: Property = Property(name="name", type=StringType)
NHSM_StateMachine.attributes={NHSM_StateMachine_name}

# NHSM_State class attributes and methods
NHSM_State_name: Property = Property(name="name", type=StringType)
NHSM_State.attributes={NHSM_State_name}

# NHSM_Transition class attributes and methods

# Relationships
machine2: BinaryAssociation = BinaryAssociation(
    name="machine2",
    ends={
        Property(name="StateMachine", type=NHSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=NHSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="NHSM_State", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_Transition4", type=NHSM_State, multiplicity=Multiplicity(1, 1))
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="NHSM_State7", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_Transition6", type=NHSM_State, multiplicity=Multiplicity(1, 1))
    }
)
machine8: BinaryAssociation = BinaryAssociation(
    name="machine8",
    ends={
        Property(name="NHSM_StateMachine10", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_Transition9", type=NHSM_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine", type=NHSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="NHSM_Transition", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_StateMachine", type=NHSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="NHSM",
    types={NHSM_StateMachine, NHSM_State, NHSM_Transition},
    associations={machine2, source3, target5, machine8, states0, transitions1},
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