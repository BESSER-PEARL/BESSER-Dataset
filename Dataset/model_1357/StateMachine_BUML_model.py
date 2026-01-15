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
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_State = Class(name="statemachine::State", is_abstract=True)
statemachine_Initial = Class(name="statemachine::Initial")
State = Class(name="State")
statemachine_Final = Class(name="statemachine::Final")
statemachine_Simple = Class(name="statemachine::Simple")
statemachine_StateMachine = Class(name="statemachine::StateMachine")

# statemachine_Transition class attributes and methods
statemachine_Transition_Id: Property = Property(name="Id", type=IntegerType)
statemachine_Transition.attributes={statemachine_Transition_Id}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Initial class attributes and methods

# State class attributes and methods

# statemachine_Final class attributes and methods

# statemachine_Simple class attributes and methods

# statemachine_StateMachine class attributes and methods
statemachine_StateMachine_name: Property = Property(name="name", type=StringType)
statemachine_StateMachine.attributes={statemachine_StateMachine_name}

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="statemachine_State", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition2", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="statemachine_State5", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition4", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statemachine_Initial_State = Generalization(general=State, specific=statemachine_Initial)
gen_statemachine_Final_State = Generalization(general=State, specific=statemachine_Final)
gen_statemachine_Simple_State = Generalization(general=State, specific=statemachine_Simple)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Transition, statemachine_State, statemachine_Initial, State, statemachine_Final, statemachine_Simple, statemachine_StateMachine},
    associations={transitions0, source1, target3},
    generalizations={gen_statemachine_Initial_State, gen_statemachine_Final_State, gen_statemachine_Simple_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)