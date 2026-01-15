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
states_StateSystem = Class(name="states::StateSystem")
states_State = Class(name="states::State")
states_Transition = Class(name="states::Transition")
states_Trace = Class(name="states::Trace")
states_EObject = Class(name="states::EObject")
states_Event = Class(name="states::Event")
states_ActionExecution = Class(name="states::ActionExecution")

# states_StateSystem class attributes and methods

# states_State class attributes and methods

# states_Transition class attributes and methods

# states_Trace class attributes and methods

# states_EObject class attributes and methods

# states_Event class attributes and methods
states_Event_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
states_Event.attributes={states_Event_qualifiedName}

# states_ActionExecution class attributes and methods

# Relationships
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=states_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=states_Transition, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="states_State", type=states_StateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="states_StateSystem", type=states_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="states_Transition", type=states_StateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="states_StateSystem2", type=states_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trace3: BinaryAssociation = BinaryAssociation(
    name="trace3",
    ends={
        Property(name="states_Trace", type=states_StateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="states_StateSystem4", type=states_Trace, multiplicity=Multiplicity(0, 1))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=states_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=states_Transition, multiplicity=Multiplicity(0, 1))
    }
)
objects8: BinaryAssociation = BinaryAssociation(
    name="objects8",
    ends={
        Property(name="states_EObject", type=states_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states_State9", type=states_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="State", type=states_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=states_State, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="State12", type=states_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=states_State, multiplicity=Multiplicity(1, 1))
    }
)
event13: BinaryAssociation = BinaryAssociation(
    name="event13",
    ends={
        Property(name="states_Event", type=states_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="states_Transition14", type=states_Event, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actionExecution15: BinaryAssociation = BinaryAssociation(
    name="actionExecution15",
    ends={
        Property(name="states_ActionExecution", type=states_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="states_Event16", type=states_ActionExecution, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="states",
    types={states_StateSystem, states_State, states_Transition, states_Trace, states_EObject, states_Event, states_ActionExecution},
    associations={outgoing5, states0, transitions1, trace3, incoming6, objects8, source10, target11, event13, actionExecution15},
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