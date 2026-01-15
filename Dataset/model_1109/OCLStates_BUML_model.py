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
oclstates_Module = Class(name="oclstates::Module")
oclstates_Event = Class(name="oclstates::Event")
oclstates_State = Class(name="oclstates::State")
oclstates_Transition = Class(name="oclstates::Transition")
oclstates_SimpleState = Class(name="oclstates::SimpleState")
State = Class(name="State")
oclstates_Statemachine = Class(name="oclstates::Statemachine")
oclstates_CompoundState = Class(name="oclstates::CompoundState")

# oclstates_Module class attributes and methods
oclstates_Module_name: Property = Property(name="name", type=StringType)
oclstates_Module.attributes={oclstates_Module_name}

# oclstates_Event class attributes and methods
oclstates_Event_name: Property = Property(name="name", type=StringType)
oclstates_Event.attributes={oclstates_Event_name}

# oclstates_State class attributes and methods
oclstates_State_initial: Property = Property(name="initial", type=BooleanType)
oclstates_State_name: Property = Property(name="name", type=StringType)
oclstates_State.attributes={oclstates_State_name, oclstates_State_initial}

# oclstates_Transition class attributes and methods

# oclstates_SimpleState class attributes and methods
oclstates_SimpleState_value: Property = Property(name="value", type=IntegerType)
oclstates_SimpleState.attributes={oclstates_SimpleState_value}

# State class attributes and methods

# oclstates_Statemachine class attributes and methods
oclstates_Statemachine_initial: Property = Property(name="initial", type=BooleanType)
oclstates_Statemachine_name: Property = Property(name="name", type=StringType)
oclstates_Statemachine_value: Property = Property(name="value", type=IntegerType)
oclstates_Statemachine.attributes={oclstates_Statemachine_name, oclstates_Statemachine_initial, oclstates_Statemachine_value}

# oclstates_CompoundState class attributes and methods

# Relationships
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="oclstates_Event", type=oclstates_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_Statemachine2", type=oclstates_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="oclstates_State", type=oclstates_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_Statemachine4", type=oclstates_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions5: BinaryAssociation = BinaryAssociation(
    name="transitions5",
    ends={
        Property(name="oclstates_Transition", type=oclstates_State, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_State6", type=oclstates_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachine7: BinaryAssociation = BinaryAssociation(
    name="statemachine7",
    ends={
        Property(name="oclstates_Statemachine9", type=oclstates_State, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_State8", type=oclstates_Statemachine, multiplicity=Multiplicity(0, 1))
    }
)
machines0: BinaryAssociation = BinaryAssociation(
    name="machines0",
    ends={
        Property(name="oclstates_Statemachine", type=oclstates_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_Module", type=oclstates_Statemachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event12: BinaryAssociation = BinaryAssociation(
    name="event12",
    ends={
        Property(name="oclstates_Event14", type=oclstates_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_Transition13", type=oclstates_Event, multiplicity=Multiplicity(0, 1))
    }
)
state15: BinaryAssociation = BinaryAssociation(
    name="state15",
    ends={
        Property(name="oclstates_State17", type=oclstates_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_Transition16", type=oclstates_State, multiplicity=Multiplicity(0, 1))
    }
)
machine10: BinaryAssociation = BinaryAssociation(
    name="machine10",
    ends={
        Property(name="oclstates_Statemachine11", type=oclstates_CompoundState, multiplicity=Multiplicity(1, 1)),
        Property(name="oclstates_CompoundState", type=oclstates_Statemachine, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_oclstates_SimpleState_State = Generalization(general=State, specific=oclstates_SimpleState)
gen_oclstates_CompoundState_State = Generalization(general=State, specific=oclstates_CompoundState)

# Domain Model
domain_model = DomainModel(
    name="oclstates",
    types={oclstates_Module, oclstates_Event, oclstates_State, oclstates_Transition, oclstates_SimpleState, State, oclstates_Statemachine, oclstates_CompoundState},
    associations={events1, states3, transitions5, statemachine7, machines0, event12, state15, machine10},
    generalizations={gen_oclstates_SimpleState_State, gen_oclstates_CompoundState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)