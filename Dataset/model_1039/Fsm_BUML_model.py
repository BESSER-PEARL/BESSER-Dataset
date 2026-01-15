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
fsm_Fsm = Class(name="fsm::Fsm")
fsm_State = Class(name="fsm::State")
fsm_Transition = Class(name="fsm::Transition")

# fsm_Fsm class attributes and methods
fsm_Fsm_name: Property = Property(name="name", type=StringType)
fsm_Fsm.attributes={fsm_Fsm_name}

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_Transition class attributes and methods
fsm_Transition_name: Property = Property(name="name", type=StringType)
fsm_Transition.attributes={fsm_Transition_name}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="fsm_State", type=fsm_Fsm, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Fsm", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="fsm_State3", type=fsm_Fsm, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Fsm2", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="fsm_Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_State5", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state6: BinaryAssociation = BinaryAssociation(
    name="state6",
    ends={
        Property(name="fsm_State8", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_Transition7", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_Fsm, fsm_State, fsm_Transition},
    associations={state0, states1, transitions4, state6},
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