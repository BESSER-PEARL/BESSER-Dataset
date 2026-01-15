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
statemachine_SM = Class(name="statemachine::SM")
statemachine_State = Class(name="statemachine::State")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Event = Class(name="statemachine::Event")

# statemachine_SM class attributes and methods

# statemachine_State class attributes and methods
statemachine_State_id: Property = Property(name="id", type=StringType)
statemachine_State.attributes={statemachine_State_id}

# statemachine_Transition class attributes and methods

# statemachine_Event class attributes and methods
statemachine_Event_id: Property = Property(name="id", type=StringType)
statemachine_Event.attributes={statemachine_Event_id}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_SM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_SM", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to14: BinaryAssociation = BinaryAssociation(
    name="to14",
    ends={
        Property(name="statemachine_State16", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition15", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
event17: BinaryAssociation = BinaryAssociation(
    name="event17",
    ends={
        Property(name="statemachine_Event19", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition18", type=statemachine_Event, multiplicity=Multiplicity(0, 1))
    }
)
initial1: BinaryAssociation = BinaryAssociation(
    name="initial1",
    ends={
        Property(name="statemachine_State3", type=statemachine_SM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_SM2", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
final4: BinaryAssociation = BinaryAssociation(
    name="final4",
    ends={
        Property(name="statemachine_State6", type=statemachine_SM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_SM5", type=statemachine_State, multiplicity=Multiplicity(0, 9999))
    }
)
transitions7: BinaryAssociation = BinaryAssociation(
    name="transitions7",
    ends={
        Property(name="statemachine_Transition", type=statemachine_SM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_SM8", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events9: BinaryAssociation = BinaryAssociation(
    name="events9",
    ends={
        Property(name="statemachine_Event", type=statemachine_SM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_SM10", type=statemachine_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from11: BinaryAssociation = BinaryAssociation(
    name="from11",
    ends={
        Property(name="statemachine_State13", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition12", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_SM, statemachine_State, statemachine_Transition, statemachine_Event},
    associations={states0, to14, event17, initial1, final4, transitions7, events9, from11},
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