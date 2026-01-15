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
states_Module = Class(name="states::Module")
states_Statemachine = Class(name="states::Statemachine")
states_Transition = Class(name="states::Transition")
states_SimpleState = Class(name="states::SimpleState")
State = Class(name="State")
states_CompoundState = Class(name="states::CompoundState")
states_Event = Class(name="states::Event")
states_State = Class(name="states::State")

# states_Module class attributes and methods
states_Module_name: Property = Property(name="name", type=StringType)
states_Module.attributes={states_Module_name}

# states_Statemachine class attributes and methods
states_Statemachine_initial: Property = Property(name="initial", type=BooleanType)
states_Statemachine_name: Property = Property(name="name", type=StringType)
states_Statemachine_value: Property = Property(name="value", type=IntegerType)
states_Statemachine.attributes={states_Statemachine_value, states_Statemachine_initial, states_Statemachine_name}

# states_Transition class attributes and methods

# states_SimpleState class attributes and methods
states_SimpleState_value: Property = Property(name="value", type=IntegerType)
states_SimpleState.attributes={states_SimpleState_value}

# State class attributes and methods

# states_CompoundState class attributes and methods

# states_Event class attributes and methods
states_Event_name: Property = Property(name="name", type=StringType)
states_Event.attributes={states_Event_name}

# states_State class attributes and methods
states_State_initial: Property = Property(name="initial", type=BooleanType)
states_State_name: Property = Property(name="name", type=StringType)
states_State.attributes={states_State_name, states_State_initial}

# Relationships
machines0: BinaryAssociation = BinaryAssociation(
    name="machines0",
    ends={
        Property(name="states_Statemachine", type=states_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="states_Module", type=states_Statemachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="states_Transition", type=states_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states_State6", type=states_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machine7: BinaryAssociation = BinaryAssociation(
    name="machine7",
    ends={
        Property(name="states_Statemachine8", type=states_CompoundState, multiplicity=Multiplicity(1, 1)),
        Property(name="states_CompoundState", type=states_Statemachine, multiplicity=Multiplicity(0, 1))
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="states_Event", type=states_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="states_Statemachine2", type=states_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="states_State", type=states_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="states_Statemachine4", type=states_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event9: BinaryAssociation = BinaryAssociation(
    name="event9",
    ends={
        Property(name="states_Event11", type=states_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="states_Transition10", type=states_Event, multiplicity=Multiplicity(0, 1))
    }
)
state12: BinaryAssociation = BinaryAssociation(
    name="state12",
    ends={
        Property(name="states_State14", type=states_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="states_Transition13", type=states_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_states_SimpleState_State = Generalization(general=State, specific=states_SimpleState)
gen_states_CompoundState_State = Generalization(general=State, specific=states_CompoundState)

# Domain Model
domain_model = DomainModel(
    name="states",
    types={states_Module, states_Statemachine, states_Transition, states_SimpleState, State, states_CompoundState, states_Event, states_State},
    associations={machines0, transitions5, machine7, events1, states3, event9, state12},
    generalizations={gen_states_SimpleState_State, gen_states_CompoundState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)