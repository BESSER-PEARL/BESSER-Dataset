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
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_State = Class(name="statemachine::State", is_abstract=True)
statemachine_Resource = Class(name="statemachine::Resource")
statemachine_Initial = Class(name="statemachine::Initial")
State = Class(name="State")
statemachine_Simple = Class(name="statemachine::Simple")
statemachine_Composite = Class(name="statemachine::Composite")

# statemachine_StateMachine class attributes and methods
statemachine_StateMachine_name: Property = Property(name="name", type=StringType)
statemachine_StateMachine.attributes={statemachine_StateMachine_name}

# statemachine_Transition class attributes and methods
statemachine_Transition_duration: Property = Property(name="duration", type=IntegerType)
statemachine_Transition_Id: Property = Property(name="Id", type=IntegerType)
statemachine_Transition.attributes={statemachine_Transition_Id, statemachine_Transition_duration}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# statemachine_Resource class attributes and methods
statemachine_Resource_name: Property = Property(name="name", type=StringType)
statemachine_Resource.attributes={statemachine_Resource_name}

# statemachine_Initial class attributes and methods

# State class attributes and methods

# statemachine_Simple class attributes and methods

# statemachine_Composite class attributes and methods

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="statemachine_Transition", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="statemachine_State7", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition6", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="statemachine_State10", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition9", type=statemachine_State, multiplicity=Multiplicity(0, 1))
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="statemachine_State", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine2", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es_parte_de3: BinaryAssociation = BinaryAssociation(
    name="es_parte_de3",
    ends={
        Property(name="statemachine_Resource", type=statemachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateMachine4", type=statemachine_Resource, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tiene11: BinaryAssociation = BinaryAssociation(
    name="tiene11",
    ends={
        Property(name="statemachine_Resource13", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State12", type=statemachine_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
es_parte_de14: BinaryAssociation = BinaryAssociation(
    name="es_parte_de14",
    ends={
        Property(name="statemachine_State15", type=statemachine_Composite, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Composite", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachine_Initial_State = Generalization(general=State, specific=statemachine_Initial)
gen_statemachine_Composite_State = Generalization(general=State, specific=statemachine_Composite)
gen_statemachine_Simple_State = Generalization(general=State, specific=statemachine_Simple)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_StateMachine, statemachine_Transition, statemachine_State, statemachine_Resource, statemachine_Initial, State, statemachine_Simple, statemachine_Composite},
    associations={transitions0, source5, target8, states1, es_parte_de3, tiene11, es_parte_de14},
    generalizations={gen_statemachine_Initial_State, gen_statemachine_Composite_State, gen_statemachine_Simple_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)