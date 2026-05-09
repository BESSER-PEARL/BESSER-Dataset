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
NHSM_Transition = Class(name="NHSM_Transition")
NHSM_StateMachine = Class(name="NHSM_StateMachine")
NHSM_State = Class(name="NHSM_State")

# NHSM_Transition class attributes and methods

# NHSM_StateMachine class attributes and methods

# NHSM_State class attributes and methods
NHSM_State_name: Property = Property(name="name", type=StringType)
NHSM_State.attributes={NHSM_State_name}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="NHSM_StateMachine", type=NHSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="NHSM_State", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="NHSM_Transition", type=NHSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_StateMachine2", type=NHSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="NHSM_State5", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_Transition4", type=NHSM_State, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="NHSM_State8", type=NHSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="NHSM_Transition7", type=NHSM_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="NHSM",
    types={NHSM_Transition, NHSM_StateMachine, NHSM_State},
    associations={states0, transitions1, source3, target6},
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