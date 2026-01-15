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
tsm_StateMachine = Class(name="tsm::StateMachine")
NamedElement = Class(name="NamedElement")
tsm_State = Class(name="tsm::State")
tsm_Transition = Class(name="tsm::Transition")
tsm_TimeEvent = Class(name="tsm::TimeEvent")
tsm_NamedElement = Class(name="tsm::NamedElement", is_abstract=True)

# tsm_StateMachine class attributes and methods

# NamedElement class attributes and methods

# tsm_State class attributes and methods

# tsm_Transition class attributes and methods

# tsm_TimeEvent class attributes and methods
tsm_TimeEvent_time: Property = Property(name="time", type=IntegerType)
tsm_TimeEvent.attributes={tsm_TimeEvent_time}

# tsm_NamedElement class attributes and methods
tsm_NamedElement_name: Property = Property(name="name", type=StringType)
tsm_NamedElement.attributes={tsm_NamedElement_name}

# Relationships
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition", type=tsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=tsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="Transition8", type=tsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=tsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="tsm_State", type=tsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tsm_StateMachine", type=tsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="tsm_Transition", type=tsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tsm_StateMachine2", type=tsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start3: BinaryAssociation = BinaryAssociation(
    name="start3",
    ends={
        Property(name="tsm_State5", type=tsm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tsm_StateMachine4", type=tsm_State, multiplicity=Multiplicity(1, 1))
    }
)
timer9: BinaryAssociation = BinaryAssociation(
    name="timer9",
    ends={
        Property(name="tsm_TimeEvent", type=tsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="tsm_Transition10", type=tsm_TimeEvent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="State", type=tsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=tsm_State, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="State13", type=tsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=tsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_tsm_State_NamedElement = Generalization(general=NamedElement, specific=tsm_State)
gen_tsm_Transition_NamedElement = Generalization(general=NamedElement, specific=tsm_Transition)
gen_tsm_StateMachine_NamedElement = Generalization(general=NamedElement, specific=tsm_StateMachine)

# Domain Model
domain_model = DomainModel(
    name="tsm",
    types={tsm_StateMachine, NamedElement, tsm_State, tsm_Transition, tsm_TimeEvent, tsm_NamedElement},
    associations={incoming6, outgoing7, states0, transitions1, start3, timer9, target11, source12},
    generalizations={gen_tsm_State_NamedElement, gen_tsm_Transition_NamedElement, gen_tsm_StateMachine_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)