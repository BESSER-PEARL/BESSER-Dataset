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
dsl_StateMachine = Class(name="dsl_StateMachine")
dsl_Event = Class(name="dsl_Event")
dsl_State = Class(name="dsl_State")
dsl_Transition = Class(name="dsl_Transition")

# dsl_StateMachine class attributes and methods

# dsl_Event class attributes and methods
dsl_Event_name: Property = Property(name="name", type=StringType)
dsl_Event.attributes={dsl_Event_name}

# dsl_State class attributes and methods
dsl_State_name: Property = Property(name="name", type=StringType)
dsl_State.attributes={dsl_State_name}

# dsl_Transition class attributes and methods

# Relationships
events0: BinaryAssociation = BinaryAssociation(
    name="events0",
    ends={
        Property(name="dsl_Event", type=dsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StateMachine", type=dsl_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="dsl_State", type=dsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StateMachine2", type=dsl_State, multiplicity=Multiplicity(0, 1))
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="dsl_State5", type=dsl_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StateMachine4", type=dsl_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="dsl_Transition", type=dsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State7", type=dsl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event8: BinaryAssociation = BinaryAssociation(
    name="event8",
    ends={
        Property(name="dsl_Event10", type=dsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Transition9", type=dsl_Event, multiplicity=Multiplicity(0, 1))
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="dsl_State13", type=dsl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Transition12", type=dsl_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_StateMachine, dsl_Event, dsl_State, dsl_Transition},
    associations={events0, initialState1, states3, transitions6, event8, state11},
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