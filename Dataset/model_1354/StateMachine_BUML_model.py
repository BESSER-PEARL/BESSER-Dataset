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
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Resource = Class(name="statemachine::Resource")
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

# statemachine_Transition class attributes and methods
statemachine_Transition_Id: Property = Property(name="Id", type=IntegerType)
statemachine_Transition.attributes={statemachine_Transition_Id}

# statemachine_Resource class attributes and methods
statemachine_Resource_name: Property = Property(name="name", type=StringType)
statemachine_Resource.attributes={statemachine_Resource_name}

# statemachine_Need class attributes and methods

# statemachine_Simple class attributes and methods

# State class attributes and methods

# statemachine_Initial class attributes and methods

# statemachine_Final class attributes and methods

# statemachine_Composite class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
needs5: BinaryAssociation = BinaryAssociation(
    name="needs5",
    ends={
        Property(name="statemachine_Need", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine6", type=statemachine_Need, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="statemachine_State9", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition8", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="statemachine_State12", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition11", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
target_need13: BinaryAssociation = BinaryAssociation(
    name="target_need13",
    ends={
        Property(name="statemachine_Resource15", type=statemachine_Need, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Need14", type=statemachine_Resource, multiplicity=Multiplicity(1, 1))
    }
)
source_need16: BinaryAssociation = BinaryAssociation(
    name="source_need16",
    ends={
        Property(name="statemachine_State18", type=statemachine_Need, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Need17", type=statemachine_State, multiplicity=Multiplicity(1, 1))
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
    types={statemachine_StateMachine, statemachine_State, statemachine_Transition, statemachine_Resource, statemachine_Need, statemachine_Simple, State, statemachine_Initial, statemachine_Final, statemachine_Composite},
    associations={states0, transitions1, resources3, needs5, source7, target10, target_need13, source_need16},
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