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
sm_sm_StateMachine = Class(name="sm::sm::StateMachine")
StateMachine = Class(name="StateMachine")
sm_sm_State = Class(name="sm::sm::State")
State = Class(name="State")
sm_sm_Transition = Class(name="sm::sm::Transition")
Transition = Class(name="Transition")
sm_Event = Class(name="sm::Event")
sm_Transition = Class(name="sm::Transition")
sm_StateMachine = Class(name="sm::StateMachine")
sm_State = Class(name="sm::State")

# sm_sm_StateMachine class attributes and methods

# StateMachine class attributes and methods

# sm_sm_State class attributes and methods

# State class attributes and methods

# sm_sm_Transition class attributes and methods

# Transition class attributes and methods

# sm_Event class attributes and methods
sm_Event_name: Property = Property(name="name", type=StringType)
sm_Event.attributes={sm_Event_name}

# sm_Transition class attributes and methods
sm_Transition_name: Property = Property(name="name", type=StringType)
sm_Transition.attributes={sm_Transition_name}

# sm_StateMachine class attributes and methods
sm_StateMachine_name: Property = Property(name="name", type=StringType)
sm_StateMachine.attributes={sm_StateMachine_name}

# sm_State class attributes and methods
sm_State_name: Property = Property(name="name", type=StringType)
sm_State.attributes={sm_State_name}

# Relationships
event0: BinaryAssociation = BinaryAssociation(
    name="event0",
    ends={
        Property(name="sm_Event", type=sm_sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_sm_Transition", type=sm_Event, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
final2: BinaryAssociation = BinaryAssociation(
    name="final2",
    ends={
        Property(name="sm_State4", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine3", type=sm_State, multiplicity=Multiplicity(0, 9999))
    }
)
nodes5: BinaryAssociation = BinaryAssociation(
    name="nodes5",
    ends={
        Property(name="sm_State7", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine6", type=sm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges8: BinaryAssociation = BinaryAssociation(
    name="edges8",
    ends={
        Property(name="sm_Transition", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine9", type=sm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subMachines10: BinaryAssociation = BinaryAssociation(
    name="subMachines10",
    ends={
        Property(name="sm_StateMachine12", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State11", type=sm_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="sm_State15", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition14", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="sm_State18", type=sm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_Transition17", type=sm_State, multiplicity=Multiplicity(1, 1))
    }
)
initial1: BinaryAssociation = BinaryAssociation(
    name="initial1",
    ends={
        Property(name="sm_State", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine", type=sm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sm_sm_StateMachine_StateMachine = Generalization(general=StateMachine, specific=sm_sm_StateMachine)
gen_sm_sm_State_State = Generalization(general=State, specific=sm_sm_State)
gen_sm_sm_Transition_Transition = Generalization(general=Transition, specific=sm_sm_Transition)

# Domain Model
domain_model = DomainModel(
    name="sm",
    types={sm_sm_StateMachine, StateMachine, sm_sm_State, State, sm_sm_Transition, Transition, sm_Event, sm_Transition, sm_StateMachine, sm_State},
    associations={event0, final2, nodes5, edges8, subMachines10, source13, target16, initial1},
    generalizations={gen_sm_sm_StateMachine_StateMachine, gen_sm_sm_State_State, gen_sm_sm_Transition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)