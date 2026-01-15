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
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
stateMachine_State = Class(name="stateMachine::State")
stateMachine_Transition = Class(name="stateMachine::Transition")

# stateMachine_StateMachine class attributes and methods
stateMachine_StateMachine_name: Property = Property(name="name", type=StringType)
stateMachine_StateMachine.attributes={stateMachine_StateMachine_name}

# stateMachine_State class attributes and methods
stateMachine_State_name: Property = Property(name="name", type=StringType)
stateMachine_State_status: Property = Property(name="status", type=BooleanType)
stateMachine_State.attributes={stateMachine_State_status, stateMachine_State_name}

# stateMachine_Transition class attributes and methods
stateMachine_Transition_name: Property = Property(name="name", type=StringType)
stateMachine_Transition_action: Property = Property(name="action", type=StringType)
stateMachine_Transition_trigger: Property = Property(name="trigger", type=StringType)
stateMachine_Transition.attributes={stateMachine_Transition_trigger, stateMachine_Transition_name, stateMachine_Transition_action}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="stateMachine_State", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine", type=stateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="stateMachine_Transition", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine2", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="stateMachine_State5", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine4", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
Outgoing6: BinaryAssociation = BinaryAssociation(
    name="Outgoing6",
    ends={
        Property(name="Transition", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="Transition8", type=stateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=stateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
from9: BinaryAssociation = BinaryAssociation(
    name="from9",
    ends={
        Property(name="State", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Outgoing", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="State11", type=stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=stateMachine_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_StateMachine, stateMachine_State, stateMachine_Transition},
    associations={state0, transition1, initialState3, Outgoing6, incoming7, from9, target10},
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