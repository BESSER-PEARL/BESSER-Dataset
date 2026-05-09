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
statemachine_StateMachine = Class(name="statemachine_StateMachine")
statemachine_State = Class(name="statemachine_State")
statemachine_Transition = Class(name="statemachine_Transition")

# statemachine_StateMachine class attributes and methods

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Transition class attributes and methods
statemachine_Transition_trigger: Property = Property(name="trigger", type=StringType)
statemachine_Transition_action: Property = Property(name="action", type=StringType)
statemachine_Transition.attributes={statemachine_Transition_action, statemachine_Transition_trigger}

# Relationships
src6: BinaryAssociation = BinaryAssociation(
    name="src6",
    ends={
        Property(name="State", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
dst7: BinaryAssociation = BinaryAssociation(
    name="dst7",
    ends={
        Property(name="State8", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
in_4: BinaryAssociation = BinaryAssociation(
    name="in_4",
    ends={
        Property(name="Transition5", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_StateMachine, statemachine_State, statemachine_Transition},
    associations={src6, dst7, states0, transitions1, out3, in_4},
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