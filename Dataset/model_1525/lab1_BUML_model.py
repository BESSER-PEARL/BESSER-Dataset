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
lab1_StateMachine = Class(name="lab1::StateMachine")
lab1_State = Class(name="lab1::State")
lab1_Transition = Class(name="lab1::Transition")

# lab1_StateMachine class attributes and methods
lab1_StateMachine_name: Property = Property(name="name", type=StringType)
lab1_StateMachine.attributes={lab1_StateMachine_name}

# lab1_State class attributes and methods
lab1_State_name: Property = Property(name="name", type=StringType)
lab1_State_init: Property = Property(name="init", type=BooleanType)
lab1_State.attributes={lab1_State_init, lab1_State_name}

# lab1_Transition class attributes and methods
lab1_Transition_name: Property = Property(name="name", type=StringType)
lab1_Transition.attributes={lab1_Transition_name}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="State", type=lab1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm", type=lab1_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="lab1_Transition", type=lab1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="lab1_StateMachine", type=lab1_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing2: BinaryAssociation = BinaryAssociation(
    name="outgoing2",
    ends={
        Property(name="Transition", type=lab1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=lab1_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition4", type=lab1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=lab1_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fsm5: BinaryAssociation = BinaryAssociation(
    name="fsm5",
    ends={
        Property(name="StateMachine", type=lab1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=lab1_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="State7", type=lab1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=lab1_State, multiplicity=Multiplicity(1, 1))
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="State9", type=lab1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=lab1_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="lab1",
    types={lab1_StateMachine, lab1_State, lab1_Transition},
    associations={states0, transitions1, outgoing2, incoming3, fsm5, from6, to8},
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