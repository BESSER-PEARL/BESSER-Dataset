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
sAAP_State = Class(name="sAAP::State")
sAAP_Transition = Class(name="sAAP::Transition")
sAAP_StateMachine = Class(name="sAAP::StateMachine")

# sAAP_State class attributes and methods
sAAP_State_name: Property = Property(name="name", type=StringType)
sAAP_State_default: Property = Property(name="default", type=BooleanType)
sAAP_State.attributes={sAAP_State_name, sAAP_State_default}

# sAAP_Transition class attributes and methods
sAAP_Transition_name: Property = Property(name="name", type=StringType)
sAAP_Transition.attributes={sAAP_Transition_name}

# sAAP_StateMachine class attributes and methods
sAAP_StateMachine_name: Property = Property(name="name", type=StringType)
sAAP_StateMachine_m_execute: Method = Method(name="execute", parameters={})
sAAP_StateMachine.attributes={sAAP_StateMachine_name}
sAAP_StateMachine.methods={sAAP_StateMachine_m_execute}

# Relationships
transition4: BinaryAssociation = BinaryAssociation(
    name="transition4",
    ends={
        Property(name="sAAP_Transition", type=sAAP_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sAAP_StateMachine5", type=sAAP_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing0: BinaryAssociation = BinaryAssociation(
    name="outgoing0",
    ends={
        Property(name="Transition", type=sAAP_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=sAAP_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming1: BinaryAssociation = BinaryAssociation(
    name="incoming1",
    ends={
        Property(name="Transition2", type=sAAP_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=sAAP_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
state3: BinaryAssociation = BinaryAssociation(
    name="state3",
    ends={
        Property(name="sAAP_State", type=sAAP_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sAAP_StateMachine", type=sAAP_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="State", type=sAAP_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=sAAP_State, multiplicity=Multiplicity(1, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="State8", type=sAAP_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=sAAP_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sAAP",
    types={sAAP_State, sAAP_Transition, sAAP_StateMachine},
    associations={transition4, outgoing0, incoming1, state3, from6, to7},
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