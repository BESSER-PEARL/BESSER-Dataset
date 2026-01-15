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
ioautomaton_AutomatonContainer = Class(name="ioautomaton::AutomatonContainer")
ioautomaton_Automaton = Class(name="ioautomaton::Automaton")
ioautomaton_State = Class(name="ioautomaton::State")
ioautomaton_Transition = Class(name="ioautomaton::Transition")
ioautomaton_Operation = Class(name="ioautomaton::Operation")
ioautomaton_Return = Class(name="ioautomaton::Return")
ioautomaton_OutMessage = Class(name="ioautomaton::OutMessage")
ioautomaton_Object = Class(name="ioautomaton::Object")

# ioautomaton_AutomatonContainer class attributes and methods

# ioautomaton_Automaton class attributes and methods
ioautomaton_Automaton_sender: Property = Property(name="sender", type=StringType)
ioautomaton_Automaton.attributes={ioautomaton_Automaton_sender}

# ioautomaton_State class attributes and methods
ioautomaton_State_name: Property = Property(name="name", type=StringType)
ioautomaton_State.attributes={ioautomaton_State_name}

# ioautomaton_Transition class attributes and methods

# ioautomaton_Operation class attributes and methods
ioautomaton_Operation_name: Property = Property(name="name", type=StringType)
ioautomaton_Operation.attributes={ioautomaton_Operation_name}

# ioautomaton_Return class attributes and methods
ioautomaton_Return_value: Property = Property(name="value", type=StringType)
ioautomaton_Return.attributes={ioautomaton_Return_value}

# ioautomaton_OutMessage class attributes and methods

# ioautomaton_Object class attributes and methods
ioautomaton_Object_name: Property = Property(name="name", type=StringType)
ioautomaton_Object.attributes={ioautomaton_Object_name}

# Relationships
automaton0: BinaryAssociation = BinaryAssociation(
    name="automaton0",
    ends={
        Property(name="ioautomaton_Automaton", type=ioautomaton_AutomatonContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_AutomatonContainer", type=ioautomaton_Automaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="ioautomaton_State", type=ioautomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_Automaton2", type=ioautomaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition3: BinaryAssociation = BinaryAssociation(
    name="transition3",
    ends={
        Property(name="ioautomaton_Transition", type=ioautomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_Automaton4", type=ioautomaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialstate5: BinaryAssociation = BinaryAssociation(
    name="initialstate5",
    ends={
        Property(name="ioautomaton_State7", type=ioautomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_Automaton6", type=ioautomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoingtransition8: BinaryAssociation = BinaryAssociation(
    name="outgoingtransition8",
    ends={
        Property(name="Transition", type=ioautomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="prestate", type=ioautomaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingtransition9: BinaryAssociation = BinaryAssociation(
    name="incomingtransition9",
    ends={
        Property(name="Transition10", type=ioautomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="poststate", type=ioautomaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
operation11: BinaryAssociation = BinaryAssociation(
    name="operation11",
    ends={
        Property(name="ioautomaton_Operation", type=ioautomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_Transition12", type=ioautomaton_Operation, multiplicity=Multiplicity(1, 1))
    }
)
_return13: BinaryAssociation = BinaryAssociation(
    name="_return13",
    ends={
        Property(name="ioautomaton_Return", type=ioautomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_Transition14", type=ioautomaton_Return, multiplicity=Multiplicity(1, 1))
    }
)
outmessage15: BinaryAssociation = BinaryAssociation(
    name="outmessage15",
    ends={
        Property(name="ioautomaton_OutMessage", type=ioautomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_Transition16", type=ioautomaton_OutMessage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
prestate17: BinaryAssociation = BinaryAssociation(
    name="prestate17",
    ends={
        Property(name="State", type=ioautomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingtransition", type=ioautomaton_State, multiplicity=Multiplicity(0, 1))
    }
)
poststate18: BinaryAssociation = BinaryAssociation(
    name="poststate18",
    ends={
        Property(name="State19", type=ioautomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingtransition", type=ioautomaton_State, multiplicity=Multiplicity(0, 1))
    }
)
_return20: BinaryAssociation = BinaryAssociation(
    name="_return20",
    ends={
        Property(name="ioautomaton_Return22", type=ioautomaton_OutMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_OutMessage21", type=ioautomaton_Return, multiplicity=Multiplicity(0, 1))
    }
)
_object23: BinaryAssociation = BinaryAssociation(
    name="_object23",
    ends={
        Property(name="ioautomaton_Object", type=ioautomaton_OutMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_OutMessage24", type=ioautomaton_Object, multiplicity=Multiplicity(0, 1))
    }
)
operation25: BinaryAssociation = BinaryAssociation(
    name="operation25",
    ends={
        Property(name="ioautomaton_Operation27", type=ioautomaton_OutMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="ioautomaton_OutMessage26", type=ioautomaton_Operation, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ioautomaton",
    types={ioautomaton_AutomatonContainer, ioautomaton_Automaton, ioautomaton_State, ioautomaton_Transition, ioautomaton_Operation, ioautomaton_Return, ioautomaton_OutMessage, ioautomaton_Object},
    associations={automaton0, state1, transition3, initialstate5, outgoingtransition8, incomingtransition9, operation11, _return13, outmessage15, prestate17, poststate18, _return20, _object23, operation25},
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