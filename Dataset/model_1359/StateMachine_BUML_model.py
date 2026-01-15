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
statemachine_State = Class(name="statemachine::State", is_abstract=True)
statemachine_Resource = Class(name="statemachine::Resource")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Need = Class(name="statemachine::Need")
statemachine_Simple = Class(name="statemachine::Simple")
State = Class(name="State")
statemachine_Initial = Class(name="statemachine::Initial")
statemachine_Final = Class(name="statemachine::Final")
statemachine_Composite = Class(name="statemachine::Composite")

# statemachine_StateMachine class attributes and methods
statemachine_StateMachine_name: Property = Property(name="name", type=StringType)
statemachine_StateMachine.attributes={statemachine_StateMachine_name}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Resource class attributes and methods
statemachine_Resource_name: Property = Property(name="name", type=StringType)
statemachine_Resource.attributes={statemachine_Resource_name}

# statemachine_Transition class attributes and methods
statemachine_Transition_Id: Property = Property(name="Id", type=IntegerType)
statemachine_Transition.attributes={statemachine_Transition_Id}

# statemachine_Need class attributes and methods

# statemachine_Simple class attributes and methods

# State class attributes and methods

# statemachine_Initial class attributes and methods

# statemachine_Final class attributes and methods

# statemachine_Composite class attributes and methods

# Relationships
source_need5: BinaryAssociation = BinaryAssociation(
    name="source_need5",
    ends={
        Property(name="statemachine_Need", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State6", type=statemachine_Need, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resources1: BinaryAssociation = BinaryAssociation(
    name="resources1",
    ends={
        Property(name="statemachine_Resource", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="statemachine_Transition", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State4", type=statemachine_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="statemachine_State9", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition8", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
target_need10: BinaryAssociation = BinaryAssociation(
    name="target_need10",
    ends={
        Property(name="statemachine_Resource12", type=statemachine_Need, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Need11", type=statemachine_Resource, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_statemachine_Simple_State = Generalization(general=State, specific=statemachine_Simple)
gen_statemachine_Initial_State = Generalization(general=State, specific=statemachine_Initial)
gen_statemachine_Final_State = Generalization(general=State, specific=statemachine_Final)
gen_statemachine_Composite_State = Generalization(general=State, specific=statemachine_Composite)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_StateMachine, statemachine_State, statemachine_Resource, statemachine_Transition, statemachine_Need, statemachine_Simple, State, statemachine_Initial, statemachine_Final, statemachine_Composite},
    associations={source_need5, states0, resources1, source3, target7, target_need10},
    generalizations={gen_statemachine_Simple_State, gen_statemachine_Initial_State, gen_statemachine_Final_State, gen_statemachine_Composite_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)