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
tp1_Transition = Class(name="tp1::Transition")
tp1_State = Class(name="tp1::State")
tp1_StateMachine = Class(name="tp1::StateMachine")

# tp1_Transition class attributes and methods
tp1_Transition_name: Property = Property(name="name", type=StringType)
tp1_Transition.attributes={tp1_Transition_name}

# tp1_State class attributes and methods
tp1_State_name: Property = Property(name="name", type=StringType)
tp1_State.attributes={tp1_State_name}

# tp1_StateMachine class attributes and methods
tp1_StateMachine_name: Property = Property(name="name", type=StringType)
tp1_StateMachine_m_execute: Method = Method(name="execute", parameters={})
tp1_StateMachine.attributes={tp1_StateMachine_name}
tp1_StateMachine.methods={tp1_StateMachine_m_execute}

# Relationships
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="tp1_Transition", type=tp1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tp1_StateMachine", type=tp1_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state1: BinaryAssociation = BinaryAssociation(
    name="state1",
    ends={
        Property(name="tp1_State", type=tp1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tp1_StateMachine2", type=tp1_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outcoming3: BinaryAssociation = BinaryAssociation(
    name="outcoming3",
    ends={
        Property(name="Transition", type=tp1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=tp1_Transition, multiplicity=Multiplicity(0, 1))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=tp1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=tp1_Transition, multiplicity=Multiplicity(0, 1))
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="State", type=tp1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outcoming", type=tp1_State, multiplicity=Multiplicity(0, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="State8", type=tp1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=tp1_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tp1",
    types={tp1_Transition, tp1_State, tp1_StateMachine},
    associations={transition0, state1, outcoming3, incoming4, from6, to7},
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