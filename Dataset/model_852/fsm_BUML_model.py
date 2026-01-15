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
FSM_StateMachine = Class(name="FSM::StateMachine")
FSM_State = Class(name="FSM::State")
FSM_Transition = Class(name="FSM::Transition")

# FSM_StateMachine class attributes and methods
FSM_StateMachine_name: Property = Property(name="name", type=StringType)
FSM_StateMachine.attributes={FSM_StateMachine_name}

# FSM_State class attributes and methods
FSM_State_name: Property = Property(name="name", type=StringType)
FSM_State_isAccepting: Property = Property(name="isAccepting", type=BooleanType)
FSM_State.attributes={FSM_State_name, FSM_State_isAccepting}

# FSM_Transition class attributes and methods
FSM_Transition_input: Property = Property(name="input", type=StringType)
FSM_Transition.attributes={FSM_Transition_input}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="FSM_State", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_StateMachine", type=FSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startState1: BinaryAssociation = BinaryAssociation(
    name="startState1",
    ends={
        Property(name="FSM_State3", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_StateMachine2", type=FSM_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=FSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition6", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=FSM_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="State", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=FSM_State, multiplicity=Multiplicity(1, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="State9", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=FSM_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="FSM",
    types={FSM_StateMachine, FSM_State, FSM_Transition},
    associations={states0, startState1, outgoing4, incoming5, source7, target8},
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