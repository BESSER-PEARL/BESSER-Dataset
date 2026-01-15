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
State = Class(name="State")
ex_stateMachine_StateMachine = Class(name="ex::stateMachine::StateMachine")
InitState = Class(name="InitState")
Transition = Class(name="Transition")
ex_stateMachine_Transition = Class(name="ex::stateMachine::Transition")
OutputState = Class(name="OutputState")
InputState = Class(name="InputState")
ex_stateMachine_State = Class(name="ex::stateMachine::State", is_abstract=True)
ex_stateMachine_InputState = Class(name="ex::stateMachine::InputState", is_abstract=True)
ex_stateMachine_OutputState = Class(name="ex::stateMachine::OutputState", is_abstract=True)
ex_stateMachine_InitState = Class(name="ex::stateMachine::InitState")
ex_stateMachine_StandardState = Class(name="ex::stateMachine::StandardState")
stateMachine_InputState = Class(name="stateMachine::InputState")
stateMachine_OutputState = Class(name="stateMachine::OutputState")
ex_stateMachine_TerminalState = Class(name="ex::stateMachine::TerminalState")

# State class attributes and methods

# ex_stateMachine_StateMachine class attributes and methods

# InitState class attributes and methods

# Transition class attributes and methods

# ex_stateMachine_Transition class attributes and methods

# OutputState class attributes and methods

# InputState class attributes and methods

# ex_stateMachine_State class attributes and methods
ex_stateMachine_State_name: Property = Property(name="name", type=StringType)
ex_stateMachine_State.attributes={ex_stateMachine_State_name}

# ex_stateMachine_InputState class attributes and methods

# ex_stateMachine_OutputState class attributes and methods

# ex_stateMachine_InitState class attributes and methods

# ex_stateMachine_StandardState class attributes and methods

# stateMachine_InputState class attributes and methods

# stateMachine_OutputState class attributes and methods

# ex_stateMachine_TerminalState class attributes and methods

# Relationships
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="State", type=ex_stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ex_stateMachine_StateMachine2", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initState0: BinaryAssociation = BinaryAssociation(
    name="initState0",
    ends={
        Property(name="InitState", type=ex_stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ex_stateMachine_StateMachine", type=InitState, multiplicity=Multiplicity(1, 1))
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="Transition", type=ex_stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ex_stateMachine_StateMachine4", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="OutputState", type=ex_stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ex_stateMachine_Transition", type=OutputState, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="InputState", type=ex_stateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ex_stateMachine_Transition7", type=InputState, multiplicity=Multiplicity(1, 1))
    }
)
ingoingTransitions8: BinaryAssociation = BinaryAssociation(
    name="ingoingTransitions8",
    ends={
        Property(name="Transition9", type=ex_stateMachine_InputState, multiplicity=Multiplicity(1, 1)),
        Property(name="ex_stateMachine_InputState", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions10: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions10",
    ends={
        Property(name="Transition11", type=ex_stateMachine_OutputState, multiplicity=Multiplicity(1, 1)),
        Property(name="ex_stateMachine_OutputState", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ex_stateMachine_InputState_State = Generalization(general=State, specific=ex_stateMachine_InputState)
gen_ex_stateMachine_OutputState_State = Generalization(general=State, specific=ex_stateMachine_OutputState)
gen_ex_stateMachine_InitState_OutputState = Generalization(general=OutputState, specific=ex_stateMachine_InitState)
gen_ex_stateMachine_StandardState_stateMachine_InputState = Generalization(general=stateMachine_InputState, specific=ex_stateMachine_StandardState)
gen_ex_stateMachine_StandardState_stateMachine_OutputState = Generalization(general=stateMachine_OutputState, specific=ex_stateMachine_StandardState)
gen_ex_stateMachine_TerminalState_InputState = Generalization(general=InputState, specific=ex_stateMachine_TerminalState)

# Domain Model
domain_model = DomainModel(
    name="ex",
    types={State, ex_stateMachine_StateMachine, InitState, Transition, ex_stateMachine_Transition, OutputState, InputState, ex_stateMachine_State, ex_stateMachine_InputState, ex_stateMachine_OutputState, ex_stateMachine_InitState, ex_stateMachine_StandardState, stateMachine_InputState, stateMachine_OutputState, ex_stateMachine_TerminalState},
    associations={states1, initState0, transitions3, source5, target6, ingoingTransitions8, outgoingTransitions10},
    generalizations={gen_ex_stateMachine_InputState_State, gen_ex_stateMachine_OutputState_State, gen_ex_stateMachine_InitState_OutputState, gen_ex_stateMachine_StandardState_stateMachine_InputState, gen_ex_stateMachine_StandardState_stateMachine_OutputState, gen_ex_stateMachine_TerminalState_InputState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)