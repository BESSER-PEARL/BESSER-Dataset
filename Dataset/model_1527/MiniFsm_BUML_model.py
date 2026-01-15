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
minifsm_Machine = Class(name="minifsm::Machine")
minifsm_State = Class(name="minifsm::State")
minifsm_Transition = Class(name="minifsm::Transition")
minifsm_FinalState = Class(name="minifsm::FinalState")
State = Class(name="State")

# minifsm_Machine class attributes and methods

# minifsm_State class attributes and methods
minifsm_State_name: Property = Property(name="name", type=StringType)
minifsm_State.attributes={minifsm_State_name}

# minifsm_Transition class attributes and methods
minifsm_Transition_event: Property = Property(name="event", type=StringType)
minifsm_Transition.attributes={minifsm_Transition_event}

# minifsm_FinalState class attributes and methods

# State class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="minifsm_State", type=minifsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_Machine", type=minifsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="minifsm_Transition", type=minifsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="minifsm_Machine2", type=minifsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="4", type=minifsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=minifsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
src8: BinaryAssociation = BinaryAssociation(
    name="src8",
    ends={
        Property(name="10", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=minifsm_State, multiplicity=Multiplicity(0, 1))
    }
)
tgt11: BinaryAssociation = BinaryAssociation(
    name="tgt11",
    ends={
        Property(name="13", type=minifsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=minifsm_State, multiplicity=Multiplicity(0, 1))
    }
)
in5: BinaryAssociation = BinaryAssociation(
    name="in5",
    ends={
        Property(name="7", type=minifsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=minifsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_minifsm_FinalState_State = Generalization(general=State, specific=minifsm_FinalState)

# Domain Model
domain_model = DomainModel(
    name="minifsm",
    types={minifsm_Machine, minifsm_State, minifsm_Transition, minifsm_FinalState, State},
    associations={states0, transitions1, out3, src8, tgt11, in5},
    generalizations={gen_minifsm_FinalState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)