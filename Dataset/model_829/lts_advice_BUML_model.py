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
lts_av_LTS = Class(name="lts::av::LTS")
lts_av_State = Class(name="lts::av::State")
lts_av_Transition = Class(name="lts::av::Transition")
lts_av_Advice = Class(name="lts::av::Advice")
lts_av_EObject = Class(name="lts::av::EObject")
lts_av_GlobalScope = Class(name="lts::av::GlobalScope")
lts_av_PerJoinPointScope = Class(name="lts::av::PerJoinPointScope")

# lts_av_LTS class attributes and methods
lts_av_LTS_name: Property = Property(name="name", type=StringType)
lts_av_LTS.attributes={lts_av_LTS_name}

# lts_av_State class attributes and methods
lts_av_State_name: Property = Property(name="name", type=StringType)
lts_av_State.attributes={lts_av_State_name}

# lts_av_Transition class attributes and methods
lts_av_Transition_input: Property = Property(name="input", type=StringType)
lts_av_Transition_output: Property = Property(name="output", type=StringType)
lts_av_Transition.attributes={lts_av_Transition_input, lts_av_Transition_output}

# lts_av_Advice class attributes and methods

# lts_av_EObject class attributes and methods

# lts_av_GlobalScope class attributes and methods

# lts_av_PerJoinPointScope class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=lts_av_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="owningLTS", type=lts_av_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="lts_av_State", type=lts_av_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_av_LTS", type=lts_av_State, multiplicity=Multiplicity(0, 1))
    }
)
currentState2: BinaryAssociation = BinaryAssociation(
    name="currentState2",
    ends={
        Property(name="lts_av_State4", type=lts_av_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_av_LTS3", type=lts_av_State, multiplicity=Multiplicity(0, 1))
    }
)
finalState5: BinaryAssociation = BinaryAssociation(
    name="finalState5",
    ends={
        Property(name="lts_av_State7", type=lts_av_LTS, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_av_LTS6", type=lts_av_State, multiplicity=Multiplicity(0, 9999))
    }
)
owningLTS8: BinaryAssociation = BinaryAssociation(
    name="owningLTS8",
    ends={
        Property(name="LTS", type=lts_av_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=lts_av_LTS, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransition9: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition9",
    ends={
        Property(name="Transition", type=lts_av_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=lts_av_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition10: BinaryAssociation = BinaryAssociation(
    name="incomingTransition10",
    ends={
        Property(name="Transition11", type=lts_av_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=lts_av_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=lts_av_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=lts_av_State, multiplicity=Multiplicity(0, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="State15", type=lts_av_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=lts_av_State, multiplicity=Multiplicity(0, 1))
    }
)
children16: BinaryAssociation = BinaryAssociation(
    name="children16",
    ends={
        Property(name="lts_av_EObject", type=lts_av_Advice, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_av_Advice", type=lts_av_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scopedObject17: BinaryAssociation = BinaryAssociation(
    name="scopedObject17",
    ends={
        Property(name="lts_av_EObject18", type=lts_av_GlobalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_av_GlobalScope", type=lts_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)
scopedObject19: BinaryAssociation = BinaryAssociation(
    name="scopedObject19",
    ends={
        Property(name="lts_av_EObject20", type=lts_av_PerJoinPointScope, multiplicity=Multiplicity(1, 1)),
        Property(name="lts_av_PerJoinPointScope", type=lts_av_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="lts_av",
    types={lts_av_LTS, lts_av_State, lts_av_Transition, lts_av_Advice, lts_av_EObject, lts_av_GlobalScope, lts_av_PerJoinPointScope},
    associations={ownedState0, initialState1, currentState2, finalState5, owningLTS8, outgoingTransition9, incomingTransition10, source12, target14, children16, scopedObject17, scopedObject19},
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