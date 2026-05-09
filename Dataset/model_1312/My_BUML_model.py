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
StateMachine_WashingMachine = Class(name="StateMachine_WashingMachine")
StateMachine_State = Class(name="StateMachine_State", is_abstract=True)
StateMachine_Transition = Class(name="StateMachine_Transition")
StateMachine_NamedState = Class(name="StateMachine_NamedState")
State = Class(name="State")
StateMachine_UnNamedState = Class(name="StateMachine_UnNamedState")

# StateMachine_WashingMachine class attributes and methods

# StateMachine_State class attributes and methods

# StateMachine_Transition class attributes and methods
StateMachine_Transition_action: Property = Property(name="action", type=StringType)
StateMachine_Transition_trigger: Property = Property(name="trigger", type=StringType)
StateMachine_Transition_id: Property = Property(name="id", type=IntegerType)
StateMachine_Transition_name: Property = Property(name="name", type=StringType)
StateMachine_Transition.attributes={StateMachine_Transition_name, StateMachine_Transition_id, StateMachine_Transition_trigger, StateMachine_Transition_action}

# StateMachine_NamedState class attributes and methods
StateMachine_NamedState_name: Property = Property(name="name", type=StringType)
StateMachine_NamedState.attributes={StateMachine_NamedState_name}

# State class attributes and methods

# StateMachine_UnNamedState class attributes and methods
StateMachine_UnNamedState_name: Property = Property(name="name", type=StringType)
StateMachine_UnNamedState.attributes={StateMachine_UnNamedState_name}

# Relationships
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="StateMachine_State3", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition2", type=StateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="StateMachine_State6", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition5", type=StateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
states7: BinaryAssociation = BinaryAssociation(
    name="states7",
    ends={
        Property(name="StateMachine_State8", type=StateMachine_WashingMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_WashingMachine", type=StateMachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoings0: BinaryAssociation = BinaryAssociation(
    name="outgoings0",
    ends={
        Property(name="StateMachine_Transition", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="StateMachine_Transition11", type=StateMachine_WashingMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_WashingMachine10", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_StateMachine_UnNamedState_State = Generalization(general=State, specific=StateMachine_UnNamedState)
gen_StateMachine_NamedState_State = Generalization(general=State, specific=StateMachine_NamedState)

# Domain Model
domain_model = DomainModel(
    name="StateMachine",
    types={StateMachine_WashingMachine, StateMachine_State, StateMachine_Transition, StateMachine_NamedState, State, StateMachine_UnNamedState},
    associations={source1, target4, states7, outgoings0, transitions9},
    generalizations={gen_StateMachine_UnNamedState_State, gen_StateMachine_NamedState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)