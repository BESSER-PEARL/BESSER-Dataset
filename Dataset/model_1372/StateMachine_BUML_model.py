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
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_StateMachine = Class(name="statemachine::StateMachine")
statemachine_State = Class(name="statemachine::State")

# statemachine_Transition class attributes and methods
statemachine_Transition_action: Property = Property(name="action", type=StringType)
statemachine_Transition_trigger: Property = Property(name="trigger", type=StringType)
statemachine_Transition.attributes={statemachine_Transition_action, statemachine_Transition_trigger}

# statemachine_StateMachine class attributes and methods

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="Transition", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
in4: BinaryAssociation = BinaryAssociation(
    name="in4",
    ends={
        Property(name="Transition5", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="State", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dst7: BinaryAssociation = BinaryAssociation(
    name="dst7",
    ends={
        Property(name="State8", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Transition, statemachine_StateMachine, statemachine_State},
    associations={transitions1, out3, in4, src6, states0, dst7},
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