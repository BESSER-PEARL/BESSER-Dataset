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
machine_State = Class(name="machine_State")
machine_Transition = Class(name="machine_Transition")
machine_Machine = Class(name="machine_Machine")
machine_Initial = Class(name="machine_Initial")
machine_Final = Class(name="machine_Final")
machine_Current = Class(name="machine_Current")
machine_Head = Class(name="machine_Head")
machine_Tape = Class(name="machine_Tape")
machine_Symbol = Class(name="machine_Symbol")
machine_TuringMachine = Class(name="machine_TuringMachine")

# machine_State class attributes and methods
machine_State_name: Property = Property(name="name", type=StringType)
machine_State.attributes={machine_State_name}

# machine_Transition class attributes and methods
machine_Transition_name: Property = Property(name="name", type=StringType)
machine_Transition_read: Property = Property(name="read", type=StringType)
machine_Transition_write: Property = Property(name="write", type=StringType)
machine_Transition_moveTo: Property = Property(name="moveTo", type=StringType)
machine_Transition.attributes={machine_Transition_read, machine_Transition_moveTo, machine_Transition_write, machine_Transition_name}

# machine_Machine class attributes and methods

# machine_Initial class attributes and methods
machine_Initial_name: Property = Property(name="name", type=StringType)
machine_Initial.attributes={machine_Initial_name}

# machine_Final class attributes and methods
machine_Final_name: Property = Property(name="name", type=StringType)
machine_Final.attributes={machine_Final_name}

# machine_Current class attributes and methods
machine_Current_name: Property = Property(name="name", type=StringType)
machine_Current.attributes={machine_Current_name}

# machine_Head class attributes and methods
machine_Head_name: Property = Property(name="name", type=StringType)
machine_Head.attributes={machine_Head_name}

# machine_Tape class attributes and methods

# machine_Symbol class attributes and methods
machine_Symbol_value: Property = Property(name="value", type=StringType)
machine_Symbol_name: Property = Property(name="name", type=StringType)
machine_Symbol_position: Property = Property(name="position", type=StringType)
machine_Symbol.attributes={machine_Symbol_name, machine_Symbol_value, machine_Symbol_position}

# machine_TuringMachine class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="machine_State", type=machine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Transition", type=machine_State, multiplicity=Multiplicity(0, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="machine_State3", type=machine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Transition2", type=machine_State, multiplicity=Multiplicity(0, 1))
    }
)
initial4: BinaryAssociation = BinaryAssociation(
    name="initial4",
    ends={
        Property(name="machine_Initial", type=machine_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Machine", type=machine_Initial, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finals5: BinaryAssociation = BinaryAssociation(
    name="finals5",
    ends={
        Property(name="machine_Final", type=machine_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Machine6", type=machine_Final, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
current7: BinaryAssociation = BinaryAssociation(
    name="current7",
    ends={
        Property(name="machine_Current", type=machine_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Machine8", type=machine_Current, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states9: BinaryAssociation = BinaryAssociation(
    name="states9",
    ends={
        Property(name="machine_State11", type=machine_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Machine10", type=machine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions12: BinaryAssociation = BinaryAssociation(
    name="transitions12",
    ends={
        Property(name="machine_Transition14", type=machine_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Machine13", type=machine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
head15: BinaryAssociation = BinaryAssociation(
    name="head15",
    ends={
        Property(name="machine_Head", type=machine_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Machine16", type=machine_Head, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
machine24: BinaryAssociation = BinaryAssociation(
    name="machine24",
    ends={
        Property(name="machine_Machine25", type=machine_TuringMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_TuringMachine", type=machine_Machine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tape26: BinaryAssociation = BinaryAssociation(
    name="tape26",
    ends={
        Property(name="machine_Tape28", type=machine_TuringMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_TuringMachine27", type=machine_Tape, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
state29: BinaryAssociation = BinaryAssociation(
    name="state29",
    ends={
        Property(name="machine_State31", type=machine_Final, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Final30", type=machine_State, multiplicity=Multiplicity(0, 1))
    }
)
next33: BinaryAssociation = BinaryAssociation(
    name="next33",
    ends={
        Property(name="machine_Symbol34", type=machine_Symbol, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Symbol32", type=machine_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
symbol35: BinaryAssociation = BinaryAssociation(
    name="symbol35",
    ends={
        Property(name="machine_Symbol37", type=machine_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Head36", type=machine_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
state17: BinaryAssociation = BinaryAssociation(
    name="state17",
    ends={
        Property(name="machine_State19", type=machine_Current, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Current18", type=machine_State, multiplicity=Multiplicity(0, 1))
    }
)
state20: BinaryAssociation = BinaryAssociation(
    name="state20",
    ends={
        Property(name="machine_State22", type=machine_Initial, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Initial21", type=machine_State, multiplicity=Multiplicity(0, 1))
    }
)
symbols23: BinaryAssociation = BinaryAssociation(
    name="symbols23",
    ends={
        Property(name="machine_Symbol", type=machine_Tape, multiplicity=Multiplicity(1, 1)),
        Property(name="machine_Tape", type=machine_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="machine",
    types={machine_State, machine_Transition, machine_Machine, machine_Initial, machine_Final, machine_Current, machine_Head, machine_Tape, machine_Symbol, machine_TuringMachine},
    associations={source0, target1, initial4, finals5, current7, states9, transitions12, head15, machine24, tape26, state29, next33, symbol35, state17, state20, symbols23},
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