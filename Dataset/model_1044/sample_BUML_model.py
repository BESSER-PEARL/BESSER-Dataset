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
sample_Transition = Class(name="sample::Transition")
sample_State = Class(name="sample::State")
sample_Initstate = Class(name="sample::Initstate")
State = Class(name="State")
sample_Finalstate = Class(name="sample::Finalstate")
sample_FSM = Class(name="sample::FSM")

# sample_Transition class attributes and methods
sample_Transition_name: Property = Property(name="name", type=StringType)
sample_Transition_trigger: Property = Property(name="trigger", type=StringType)
sample_Transition.attributes={sample_Transition_trigger, sample_Transition_name}

# sample_State class attributes and methods
sample_State_name: Property = Property(name="name", type=StringType)
sample_State.attributes={sample_State_name}

# sample_Initstate class attributes and methods

# State class attributes and methods

# sample_Finalstate class attributes and methods

# sample_FSM class attributes and methods
sample_FSM_name: Property = Property(name="name", type=StringType)
sample_FSM.attributes={sample_FSM_name}

# Relationships
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="sample_Transition", type=sample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_FSM", type=sample_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="sample_State", type=sample_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_FSM2", type=sample_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StateTo3: BinaryAssociation = BinaryAssociation(
    name="StateTo3",
    ends={
        Property(name="sample_State5", type=sample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Transition4", type=sample_State, multiplicity=Multiplicity(1, 1))
    }
)
stateFrom6: BinaryAssociation = BinaryAssociation(
    name="stateFrom6",
    ends={
        Property(name="sample_State8", type=sample_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sample_Transition7", type=sample_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_sample_Initstate_State = Generalization(general=State, specific=sample_Initstate)
gen_sample_Finalstate_State = Generalization(general=State, specific=sample_Finalstate)

# Domain Model
domain_model = DomainModel(
    name="sample",
    types={sample_Transition, sample_State, sample_Initstate, State, sample_Finalstate, sample_FSM},
    associations={transition0, state1, StateTo3, stateFrom6},
    generalizations={gen_sample_Initstate_State, gen_sample_Finalstate_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)