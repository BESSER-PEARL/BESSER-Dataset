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
metaModelStateMachine_StateMachine = Class(name="metaModelStateMachine::StateMachine")
metaModelStateMachine_state = Class(name="metaModelStateMachine::state")
metaModelStateMachine_Transition = Class(name="metaModelStateMachine::Transition")
metaModelStateMachine_Guard = Class(name="metaModelStateMachine::Guard")
metaModelStateMachine_Trigger = Class(name="metaModelStateMachine::Trigger")

# metaModelStateMachine_StateMachine class attributes and methods

# metaModelStateMachine_state class attributes and methods

# metaModelStateMachine_Transition class attributes and methods

# metaModelStateMachine_Guard class attributes and methods

# metaModelStateMachine_Trigger class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="metaModelStateMachine_state", type=metaModelStateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_StateMachine", type=metaModelStateMachine_state, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="metaModelStateMachine_Transition", type=metaModelStateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_StateMachine2", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachine3: BinaryAssociation = BinaryAssociation(
    name="statemachine3",
    ends={
        Property(name="metaModelStateMachine_StateMachine5", type=metaModelStateMachine_state, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_state4", type=metaModelStateMachine_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition6: BinaryAssociation = BinaryAssociation(
    name="transition6",
    ends={
        Property(name="metaModelStateMachine_Transition8", type=metaModelStateMachine_state, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_state7", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition9: BinaryAssociation = BinaryAssociation(
    name="transition9",
    ends={
        Property(name="metaModelStateMachine_Transition10", type=metaModelStateMachine_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_Guard", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="metaModelStateMachine_state16", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_Transition15", type=metaModelStateMachine_state, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statemachine17: BinaryAssociation = BinaryAssociation(
    name="statemachine17",
    ends={
        Property(name="metaModelStateMachine_StateMachine19", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_Transition18", type=metaModelStateMachine_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger20: BinaryAssociation = BinaryAssociation(
    name="trigger20",
    ends={
        Property(name="metaModelStateMachine_Trigger", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_Transition21", type=metaModelStateMachine_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard22: BinaryAssociation = BinaryAssociation(
    name="guard22",
    ends={
        Property(name="metaModelStateMachine_Guard24", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_Transition23", type=metaModelStateMachine_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition25: BinaryAssociation = BinaryAssociation(
    name="transition25",
    ends={
        Property(name="metaModelStateMachine_Transition27", type=metaModelStateMachine_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_Trigger26", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="metaModelStateMachine_state13", type=metaModelStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="metaModelStateMachine_Transition12", type=metaModelStateMachine_state, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="metaModelStateMachine",
    types={metaModelStateMachine_StateMachine, metaModelStateMachine_state, metaModelStateMachine_Transition, metaModelStateMachine_Guard, metaModelStateMachine_Trigger},
    associations={state0, transition1, statemachine3, transition6, transition9, source14, statemachine17, trigger20, guard22, transition25, target11},
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