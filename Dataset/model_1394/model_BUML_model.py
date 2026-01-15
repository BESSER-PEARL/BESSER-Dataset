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
model_AbstractState = Class(name="model::AbstractState", is_abstract=True)
model_FiniteStateMachine = Class(name="model::FiniteStateMachine")
model_Transition = Class(name="model::Transition")
model_State = Class(name="model::State")
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
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="8", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=model_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="11", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="model_AbstractState13", type=model_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Transition", type=model_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="1", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=model_FiniteStateMachine, multiplicity=Multiplicity(0, 1))
    }
)
outgoings2: BinaryAssociation = BinaryAssociation(
    name="outgoings2",
    ends={
        Property(name="4", type=model_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=model_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial5: BinaryAssociation = BinaryAssociation(
    name="initial5",
    ends={
        Property(name="model_AbstractState", type=model_FiniteStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="model_FiniteStateMachine", type=model_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_State_AbstractState = Generalization(general=AbstractState, specific=model_State)
gen_model_FiniteStateMachine_AbstractState = Generalization(general=AbstractState, specific=model_FiniteStateMachine)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_AbstractState, model_FiniteStateMachine, model_Transition, model_State, AbstractState},
    associations={states6, source9, target12, parent0, outgoings2, initial5},
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