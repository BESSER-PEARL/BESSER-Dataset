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
statemachine_AbstractState = Class(name="statemachine::AbstractState", is_abstract=True)
statemachine_Transition = Class(name="statemachine::Transition")
Named = Class(name="Named")
statemachine_Initial = Class(name="statemachine::Initial")
AbstractState = Class(name="AbstractState")
statemachine_Named = Class(name="statemachine::Named", is_abstract=True)
statemachine_State = Class(name="statemachine::State")

# statemachine_StateMachine class attributes and methods

# statemachine_AbstractState class attributes and methods

# statemachine_Transition class attributes and methods

# Named class attributes and methods

# statemachine_Initial class attributes and methods

# AbstractState class attributes and methods

# statemachine_Named class attributes and methods
statemachine_Named_name: Property = Property(name="name", type=StringType)
statemachine_Named.attributes={statemachine_Named_name}

# statemachine_State class attributes and methods

# Relationships
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="statemachine_AbstractState5", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition4", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="statemachine_AbstractState8", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition7", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_AbstractState", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachine_AbstractState_Named = Generalization(general=Named, specific=statemachine_AbstractState)
gen_statemachine_Initial_AbstractState = Generalization(general=AbstractState, specific=statemachine_Initial)
gen_statemachine_Transition_Named = Generalization(general=Named, specific=statemachine_Transition)
gen_statemachine_State_AbstractState = Generalization(general=AbstractState, specific=statemachine_State)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_StateMachine, statemachine_AbstractState, statemachine_Transition, Named, statemachine_Initial, AbstractState, statemachine_Named, statemachine_State},
    associations={source3, target6, states0, transitions1},
    generalizations={gen_statemachine_AbstractState_Named, gen_statemachine_Initial_AbstractState, gen_statemachine_Transition_Named, gen_statemachine_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)