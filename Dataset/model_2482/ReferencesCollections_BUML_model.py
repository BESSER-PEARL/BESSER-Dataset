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
fsm_State = Class(name="fsm::State")
fsm_FSM = Class(name="fsm::FSM")
fsm_Transition = Class(name="fsm::Transition")

# fsm_State class attributes and methods

# fsm_FSM class attributes and methods

# fsm_Transition class attributes and methods

# Relationships
ls1: BinaryAssociation = BinaryAssociation(
    name="ls1",
    ends={
        Property(name="fsm_State", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State0", type=fsm_State, multiplicity=Multiplicity(0, 9999))
    }
)
lf2: BinaryAssociation = BinaryAssociation(
    name="lf2",
    ends={
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State3", type=fsm_FSM, multiplicity=Multiplicity(0, 9999))
    }
)
lt4: BinaryAssociation = BinaryAssociation(
    name="lt4",
    ends={
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State5", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_State, fsm_FSM, fsm_Transition},
    associations={ls1, lf2, lt4},
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