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
Statecharts_BooleanExpression = Class(name="Statecharts_BooleanExpression")
Statecharts_StateMachine = Class(name="Statecharts_StateMachine")
Transition = Class(name="Transition")
State = Class(name="State")
Statecharts_State = Class(name="Statecharts_State")
StateVertex = Class(name="StateVertex")
StateMachine = Class(name="StateMachine")
Event = Class(name="Event")
Statecharts_CompositeState = Class(name="Statecharts_CompositeState")
Statecharts_Transition = Class(name="Statecharts_Transition")
Guard = Class(name="Guard")
Statecharts_StateVertex = Class(name="Statecharts_StateVertex")
CompositeState = Class(name="CompositeState")
Statecharts_Guard = Class(name="Statecharts_Guard")
BooleanExpression = Class(name="BooleanExpression")
Statecharts_Event = Class(name="Statecharts_Event")

# Statecharts_BooleanExpression class attributes and methods
Statecharts_BooleanExpression_value: Property = Property(name="value", type=StringType)
Statecharts_BooleanExpression.attributes={Statecharts_BooleanExpression_value}

# Statecharts_StateMachine class attributes and methods

# Transition class attributes and methods

# State class attributes and methods

# Statecharts_State class attributes and methods

# StateVertex class attributes and methods

# StateMachine class attributes and methods

# Event class attributes and methods

# Statecharts_CompositeState class attributes and methods
Statecharts_CompositeState_isConcurrent: Property = Property(name="isConcurrent", type=StringType)
Statecharts_CompositeState.attributes={Statecharts_CompositeState_isConcurrent}

# Statecharts_Transition class attributes and methods

# Guard class attributes and methods

# Statecharts_StateVertex class attributes and methods

# CompositeState class attributes and methods

# Statecharts_Guard class attributes and methods

# BooleanExpression class attributes and methods

# Statecharts_Event class attributes and methods

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="Transition", type=Statecharts_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="transSM_container", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
top1: BinaryAssociation = BinaryAssociation(
    name="top1",
    ends={
        Property(name="State", type=Statecharts_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="state_container", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state_container2: BinaryAssociation = BinaryAssociation(
    name="state_container2",
    ends={
        Property(name="StateMachine", type=Statecharts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="top", type=StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
internalTransitions3: BinaryAssociation = BinaryAssociation(
    name="internalTransitions3",
    ends={
        Property(name="Transition4", type=Statecharts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="transS_container", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableEvents5: BinaryAssociation = BinaryAssociation(
    name="deferrableEvents5",
    ends={
        Property(name="Event", type=Statecharts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="targets", type=Event, multiplicity=Multiplicity(0, 9999))
    }
)
subVertexes6: BinaryAssociation = BinaryAssociation(
    name="subVertexes6",
    ends={
        Property(name="StateVertex", type=Statecharts_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="sv_container", type=StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transSM_container7: BinaryAssociation = BinaryAssociation(
    name="transSM_container7",
    ends={
        Property(name="StateMachine8", type=Statecharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
transS_container9: BinaryAssociation = BinaryAssociation(
    name="transS_container9",
    ends={
        Property(name="State10", type=Statecharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="internalTransitions", type=State, multiplicity=Multiplicity(0, 1))
    }
)
trigger11: BinaryAssociation = BinaryAssociation(
    name="trigger11",
    ends={
        Property(name="Event12", type=Statecharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="evt_container", type=Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard13: BinaryAssociation = BinaryAssociation(
    name="guard13",
    ends={
        Property(name="Guard", type=Statecharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="gua_container", type=Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="StateVertex15", type=Statecharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="StateVertex17", type=Statecharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
sv_container18: BinaryAssociation = BinaryAssociation(
    name="sv_container18",
    ends={
        Property(name="CompositeState", type=Statecharts_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subVertexes", type=CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
outgoing19: BinaryAssociation = BinaryAssociation(
    name="outgoing19",
    ends={
        Property(name="Transition20", type=Statecharts_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming21: BinaryAssociation = BinaryAssociation(
    name="incoming21",
    ends={
        Property(name="Transition22", type=Statecharts_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
gua_container23: BinaryAssociation = BinaryAssociation(
    name="gua_container23",
    ends={
        Property(name="Transition24", type=Statecharts_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="guard", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
expression25: BinaryAssociation = BinaryAssociation(
    name="expression25",
    ends={
        Property(name="BooleanExpression", type=Statecharts_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="Statecharts_Guard", type=BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
evt_container26: BinaryAssociation = BinaryAssociation(
    name="evt_container26",
    ends={
        Property(name="Transition27", type=Statecharts_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=Transition, multiplicity=Multiplicity(0, 9999))
    }
)
targets28: BinaryAssociation = BinaryAssociation(
    name="targets28",
    ends={
        Property(name="State29", type=Statecharts_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="deferrableEvents", type=State, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Statecharts_State_StateVertex = Generalization(general=StateVertex, specific=Statecharts_State)
gen_Statecharts_CompositeState_State = Generalization(general=State, specific=Statecharts_CompositeState)

# Domain Model
domain_model = DomainModel(
    name="Statecharts",
    types={Statecharts_BooleanExpression, Statecharts_StateMachine, Transition, State, Statecharts_State, StateVertex, StateMachine, Event, Statecharts_CompositeState, Statecharts_Transition, Guard, Statecharts_StateVertex, CompositeState, Statecharts_Guard, BooleanExpression, Statecharts_Event},
    associations={transitions0, top1, state_container2, internalTransitions3, deferrableEvents5, subVertexes6, transSM_container7, transS_container9, trigger11, guard13, source14, target16, sv_container18, outgoing19, incoming21, gua_container23, expression25, evt_container26, targets28},
    generalizations={gen_Statecharts_State_StateVertex, gen_Statecharts_CompositeState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)