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
ioAutomaton_AutomatonCollection = Class(name="ioAutomaton::AutomatonCollection")
ioAutomaton_Automaton = Class(name="ioAutomaton::Automaton")
State = Class(name="State")
ioAutomaton_SystemActor = Class(name="ioAutomaton::SystemActor")
ioAutomaton_State = Class(name="ioAutomaton::State")
ioAutomaton_Transition = Class(name="ioAutomaton::Transition")
ioAutomaton_Operation = Class(name="ioAutomaton::Operation")
ioAutomaton_OutMessage = Class(name="ioAutomaton::OutMessage")
ioAutomaton_Return = Class(name="ioAutomaton::Return")
ioAutomaton_Actor = Class(name="ioAutomaton::Actor")

# ioAutomaton_AutomatonCollection class attributes and methods

# ioAutomaton_Automaton class attributes and methods

# State class attributes and methods

# ioAutomaton_SystemActor class attributes and methods

# ioAutomaton_State class attributes and methods

# ioAutomaton_Transition class attributes and methods

# ioAutomaton_Operation class attributes and methods

# ioAutomaton_OutMessage class attributes and methods

# ioAutomaton_Return class attributes and methods

# ioAutomaton_Actor class attributes and methods

# Relationships
collection5: BinaryAssociation = BinaryAssociation(
    name="collection5",
    ends={
        Property(name="AutomatonCollection", type=ioAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton6", type=ioAutomaton_AutomatonCollection, multiplicity=Multiplicity(1, 1))
    }
)
startState7: BinaryAssociation = BinaryAssociation(
    name="startState7",
    ends={
        Property(name="ioAutomaton_State", type=ioAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_Automaton8", type=ioAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
automaton9: BinaryAssociation = BinaryAssociation(
    name="automaton9",
    ends={
        Property(name="Automaton10", type=ioAutomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=ioAutomaton_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
automaton0: BinaryAssociation = BinaryAssociation(
    name="automaton0",
    ends={
        Property(name="Automaton", type=ioAutomaton_AutomatonCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=ioAutomaton_Automaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainActor1: BinaryAssociation = BinaryAssociation(
    name="mainActor1",
    ends={
        Property(name="ioAutomaton_SystemActor", type=ioAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_Automaton", type=ioAutomaton_SystemActor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state2: BinaryAssociation = BinaryAssociation(
    name="state2",
    ends={
        Property(name="State", type=ioAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton", type=ioAutomaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition3: BinaryAssociation = BinaryAssociation(
    name="transition3",
    ends={
        Property(name="Transition", type=ioAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="automaton4", type=ioAutomaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preState17: BinaryAssociation = BinaryAssociation(
    name="preState17",
    ends={
        Property(name="outgoingTransition", type=ioAutomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="State18", type=ioAutomaton_Transition, multiplicity=Multiplicity(1, 1))
    }
)
operation19: BinaryAssociation = BinaryAssociation(
    name="operation19",
    ends={
        Property(name="ioAutomaton_Operation", type=ioAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_Transition", type=ioAutomaton_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outMessage20: BinaryAssociation = BinaryAssociation(
    name="outMessage20",
    ends={
        Property(name="ioAutomaton_OutMessage", type=ioAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_Transition21", type=ioAutomaton_OutMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue22: BinaryAssociation = BinaryAssociation(
    name="returnValue22",
    ends={
        Property(name="ioAutomaton_Return", type=ioAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_Transition23", type=ioAutomaton_Return, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outgoingTransition11: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition11",
    ends={
        Property(name="Transition12", type=ioAutomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="preState", type=ioAutomaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransition13: BinaryAssociation = BinaryAssociation(
    name="incomingTransition13",
    ends={
        Property(name="Transition14", type=ioAutomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="postState", type=ioAutomaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
automaton15: BinaryAssociation = BinaryAssociation(
    name="automaton15",
    ends={
        Property(name="Automaton16", type=ioAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=ioAutomaton_Automaton, multiplicity=Multiplicity(1, 1))
    }
)
postState24: BinaryAssociation = BinaryAssociation(
    name="postState24",
    ends={
        Property(name="State25", type=ioAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=ioAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
operation26: BinaryAssociation = BinaryAssociation(
    name="operation26",
    ends={
        Property(name="ioAutomaton_Operation28", type=ioAutomaton_OutMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_OutMessage27", type=ioAutomaton_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receiver29: BinaryAssociation = BinaryAssociation(
    name="receiver29",
    ends={
        Property(name="ioAutomaton_Actor", type=ioAutomaton_OutMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_OutMessage30", type=ioAutomaton_Actor, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnValue31: BinaryAssociation = BinaryAssociation(
    name="returnValue31",
    ends={
        Property(name="ioAutomaton_Return33", type=ioAutomaton_OutMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ioAutomaton_OutMessage32", type=ioAutomaton_Return, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ioAutomaton_State_State = Generalization(general=State, specific=ioAutomaton_State)

# Domain Model
domain_model = DomainModel(
    name="ioAutomaton",
    types={ioAutomaton_AutomatonCollection, ioAutomaton_Automaton, State, ioAutomaton_SystemActor, ioAutomaton_State, ioAutomaton_Transition, ioAutomaton_Operation, ioAutomaton_OutMessage, ioAutomaton_Return, ioAutomaton_Actor},
    associations={collection5, startState7, automaton9, automaton0, mainActor1, state2, transition3, preState17, operation19, outMessage20, returnValue22, outgoingTransition11, incomingTransition13, automaton15, postState24, operation26, receiver29, returnValue31},
    generalizations={gen_ioAutomaton_State_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)