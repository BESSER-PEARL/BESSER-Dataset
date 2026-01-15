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
wheel_WheelSM = Class(name="wheel::WheelSM")
wheel_State = Class(name="wheel::State")
wheel_Transition = Class(name="wheel::Transition")

# wheel_WheelSM class attributes and methods

# wheel_State class attributes and methods
wheel_State_name: Property = Property(name="name", type=StringType)
wheel_State.attributes={wheel_State_name}

# wheel_Transition class attributes and methods
wheel_Transition_speed: Property = Property(name="speed", type=StringType)
wheel_Transition_time: Property = Property(name="time", type=StringType)
wheel_Transition.attributes={wheel_Transition_speed, wheel_Transition_time}

# Relationships
owningFSM8: BinaryAssociation = BinaryAssociation(
    name="owningFSM8",
    ends={
        Property(name="WheelSM", type=wheel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=wheel_WheelSM, multiplicity=Multiplicity(1, 1))
    }
)
initialState0: BinaryAssociation = BinaryAssociation(
    name="initialState0",
    ends={
        Property(name="wheel_State", type=wheel_WheelSM, multiplicity=Multiplicity(1, 1)),
        Property(name="wheel_WheelSM", type=wheel_State, multiplicity=Multiplicity(0, 1))
    }
)
finalState1: BinaryAssociation = BinaryAssociation(
    name="finalState1",
    ends={
        Property(name="wheel_State3", type=wheel_WheelSM, multiplicity=Multiplicity(1, 1)),
        Property(name="wheel_WheelSM2", type=wheel_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedState4: BinaryAssociation = BinaryAssociation(
    name="ownedState4",
    ends={
        Property(name="State", type=wheel_WheelSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=wheel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition5: BinaryAssociation = BinaryAssociation(
    name="incomingTransition5",
    ends={
        Property(name="wheel_Transition", type=wheel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="wheel_State6", type=wheel_Transition, multiplicity=Multiplicity(0, 1))
    }
)
outgoingTransition7: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition7",
    ends={
        Property(name="Transition", type=wheel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="Source", type=wheel_Transition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="wheel_State11", type=wheel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="wheel_Transition10", type=wheel_State, multiplicity=Multiplicity(0, 1))
    }
)
Source12: BinaryAssociation = BinaryAssociation(
    name="Source12",
    ends={
        Property(name="State13", type=wheel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=wheel_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="wheel",
    types={wheel_WheelSM, wheel_State, wheel_Transition},
    associations={owningFSM8, initialState0, finalState1, ownedState4, incomingTransition5, outgoingTransition7, target9, Source12},
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