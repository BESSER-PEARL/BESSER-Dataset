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
FiniteStateMachines_Transition = Class(name="FiniteStateMachines::Transition")
FiniteStateMachines_FiniteStateMachine = Class(name="FiniteStateMachines::FiniteStateMachine")
FiniteStateMachines_State = Class(name="FiniteStateMachines::State")

# FiniteStateMachines_Transition class attributes and methods
FiniteStateMachines_Transition_input: Property = Property(name="input", type=StringType)
FiniteStateMachines_Transition.attributes={FiniteStateMachines_Transition_input}

# FiniteStateMachines_FiniteStateMachine class attributes and methods
FiniteStateMachines_FiniteStateMachine_id: Property = Property(name="id", type=StringType)
FiniteStateMachines_FiniteStateMachine.attributes={FiniteStateMachines_FiniteStateMachine_id}

# FiniteStateMachines_State class attributes and methods
FiniteStateMachines_State_isEndState: Property = Property(name="isEndState", type=BooleanType)
FiniteStateMachines_State_isStartState: Property = Property(name="isStartState", type=BooleanType)
FiniteStateMachines_State_name: Property = Property(name="name", type=StringType)
FiniteStateMachines_State.attributes={FiniteStateMachines_State_name, FiniteStateMachines_State_isEndState, FiniteStateMachines_State_isStartState}

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="FiniteStateMachines_Transition", type=FiniteStateMachines_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FiniteStateMachines_FiniteStateMachine2", type=FiniteStateMachines_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="Transition", type=FiniteStateMachines_State, multiplicity=Multiplicity(1, 1)),
        Property(name="startState", type=FiniteStateMachines_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
startState4: BinaryAssociation = BinaryAssociation(
    name="startState4",
    ends={
        Property(name="State", type=FiniteStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=FiniteStateMachines_State, multiplicity=Multiplicity(1, 1))
    }
)
endState5: BinaryAssociation = BinaryAssociation(
    name="endState5",
    ends={
        Property(name="FiniteStateMachines_State7", type=FiniteStateMachines_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="FiniteStateMachines_Transition6", type=FiniteStateMachines_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="FiniteStateMachines_State", type=FiniteStateMachines_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="FiniteStateMachines_FiniteStateMachine", type=FiniteStateMachines_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="FiniteStateMachines",
    types={FiniteStateMachines_Transition, FiniteStateMachines_FiniteStateMachine, FiniteStateMachines_State},
    associations={transitions1, transitions3, startState4, endState5, states0},
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