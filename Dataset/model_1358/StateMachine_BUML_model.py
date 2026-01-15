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
statemachine_StateMachine = Class(name="statemachine::StateMachine")
statemachine_State = Class(name="statemachine::State")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Resource = Class(name="statemachine::Resource")

# statemachine_StateMachine class attributes and methods
statemachine_StateMachine_name: Property = Property(name="name", type=StringType)
statemachine_StateMachine.attributes={statemachine_StateMachine_name}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Transition class attributes and methods
statemachine_Transition_Id: Property = Property(name="Id", type=IntegerType)
statemachine_Transition.attributes={statemachine_Transition_Id}

# statemachine_Resource class attributes and methods
statemachine_Resource_name: Property = Property(name="name", type=StringType)
statemachine_Resource.attributes={statemachine_Resource_name}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="statemachine_Transition9", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State10", type=statemachine_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="statemachine_State13", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition12", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources3: BinaryAssociation = BinaryAssociation(
    name="resources3",
    ends={
        Property(name="statemachine_Resource", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine4", type=statemachine_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
need5: BinaryAssociation = BinaryAssociation(
    name="need5",
    ends={
        Property(name="statemachine_Resource7", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State6", type=statemachine_Resource, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_StateMachine, statemachine_State, statemachine_Transition, statemachine_Resource},
    associations={states0, source8, target11, transitions1, resources3, need5},
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