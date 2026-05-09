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
model_AbstractState = Class(name="model_AbstractState", is_abstract=True)
model_FiniteStateMachine = Class(name="model_FiniteStateMachine")
model_Transition = Class(name="model_Transition")
model_State = Class(name="model_State")
AbstractState = Class(name="AbstractState")

# model_AbstractState class attributes and methods
model_AbstractState_name: Property = Property(name="name", type=StringType)
model_AbstractState.attributes={model_AbstractState_name}

# model_FiniteStateMachine class attributes and methods

# model_Transition class attributes and methods
model_Transition_name: Property = Property(name="name", type=StringType)
model_Transition_trigger: Property = Property(name="trigger", type=StringType)
model_Transition.attributes={model_Transition_trigger, model_Transition_name}

# model_State class attributes and methods

# AbstractState class attributes and methods

# Relationships
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="FiniteStateMachine", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=model_FiniteStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoings1: BinaryAssociation = BinaryAssociation(
    name="outgoings1",
    ends={
        Property(name="Transition", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial2: BinaryAssociation = BinaryAssociation(
    name="initial2",
    ends={
        Property(name="model_AbstractState", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FiniteStateMachine", type=model_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="AbstractState", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="AbstractState5", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="model_AbstractState7", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Transition", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_model_State_AbstractState = Generalization(general=AbstractState, specific=model_State)
gen_model_FiniteStateMachine_AbstractState = Generalization(general=AbstractState, specific=model_FiniteStateMachine)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_AbstractState, model_FiniteStateMachine, model_Transition, model_State, AbstractState},
    associations={parent0, outgoings1, initial2, states3, source4, target6},
    generalizations={gen_model_State_AbstractState, gen_model_FiniteStateMachine_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)