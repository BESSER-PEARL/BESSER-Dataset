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
lts_LTS = Class(name="lts::LTS")
lts_State = Class(name="lts::State")
lts_Transition = Class(name="lts::Transition")

# lts_LTS class attributes and methods
lts_LTS_name: Property = Property(name="name", type=StringType)
lts_LTS.attributes={lts_LTS_name}

# lts_State class attributes and methods
lts_State_name: Property = Property(name="name", type=StringType)
lts_State.attributes={lts_State_name}

# lts_Transition class attributes and methods
lts_Transition_input: Property = Property(name="input", type=StringType)
lts_Transition_output: Property = Property(name="output", type=StringType)
lts_Transition.attributes={lts_Transition_output, lts_Transition_input}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningLTS", type=lts_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="lts_State", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_LTS", type=lts_State, multiplicity=Multiplicity(1, 1))
    }
)
currentState2: BinaryAssociation = BinaryAssociation(
    name="currentState2",
    ends={
        Property(name="lts_State4", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_LTS3", type=lts_State, multiplicity=Multiplicity(0, 1))
    }
)
finalState5: BinaryAssociation = BinaryAssociation(
    name="finalState5",
    ends={
        Property(name="lts_State7", type=lts_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_LTS6", type=lts_State, multiplicity=Multiplicity(0, 9999))
    }
)
owningLTS8: BinaryAssociation = BinaryAssociation(
    name="owningLTS8",
    ends={
        Property(name="LTS", type=lts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=lts_LTS, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition9",
    ends={
        Property(name="Transition", type=lts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=lts_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition10: BinaryAssociation = BinaryAssociation(
    name="incomingTransition10",
    ends={
        Property(name="Transition11", type=lts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=lts_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=lts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=lts_State, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="State15", type=lts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=lts_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="lts",
    types={lts_LTS, lts_State, lts_Transition},
    associations={ownedState0, initialState1, currentState2, finalState5, owningLTS8, outgoingTransition9, incomingTransition10, source12, target14},
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