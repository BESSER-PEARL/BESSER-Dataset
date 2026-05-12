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
ControllerUML_Controller = Class(name="ControllerUML_Controller")
ControllerAttribute = Class(name="ControllerAttribute")
ControllerUML_ControllerAttribute = Class(name="ControllerUML_ControllerAttribute")
Controller = Class(name="Controller")
StateTransition = Class(name="StateTransition")
StateMachine = Class(name="StateMachine")
ControllerUML_StateMachine = Class(name="ControllerUML_StateMachine")
State = Class(name="State")
ControllerUML_State = Class(name="ControllerUML_State")
StateMachineAction = Class(name="StateMachineAction")
ControllerUML_SubControllerState = Class(name="ControllerUML_SubControllerState")
ControllerUML_ViewState = Class(name="ControllerUML_ViewState")
ControllerUML_StateTransition = Class(name="ControllerUML_StateTransition")
Event = Class(name="Event")
ControllerUML_StateMachineAction = Class(name="ControllerUML_StateMachineAction")
ControllerUML_Event = Class(name="ControllerUML_Event")

# ControllerUML_Controller class attributes and methods

# ControllerAttribute class attributes and methods

# ControllerUML_ControllerAttribute class attributes and methods

# Controller class attributes and methods

# StateTransition class attributes and methods

# StateMachine class attributes and methods

# ControllerUML_StateMachine class attributes and methods

# State class attributes and methods

# ControllerUML_State class attributes and methods

# StateMachineAction class attributes and methods

# ControllerUML_SubControllerState class attributes and methods

# ControllerUML_ViewState class attributes and methods

# ControllerUML_StateTransition class attributes and methods

# Event class attributes and methods

# ControllerUML_StateMachineAction class attributes and methods

# ControllerUML_Event class attributes and methods

# Relationships
controllerAttribute1: BinaryAssociation = BinaryAssociation(
    name="controllerAttribute1",
    ends={
        Property(name="ControllerAttribute", type=ControllerUML_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="controller", type=ControllerAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
controller0: BinaryAssociation = BinaryAssociation(
    name="controller0",
    ends={
        Property(name="Controller", type=ControllerUML_ControllerAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="controllerAttribute", type=Controller, multiplicity=Multiplicity(1, 1))
    }
)
outGoing8: BinaryAssociation = BinaryAssociation(
    name="outGoing8",
    ends={
        Property(name="StateTransition", type=ControllerUML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=StateTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behavior2: BinaryAssociation = BinaryAssociation(
    name="behavior2",
    ends={
        Property(name="StateMachine", type=ControllerUML_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="ControllerUML_Controller", type=StateMachine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="State", type=ControllerUML_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="ControllerUML_StateMachine", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substates4: BinaryAssociation = BinaryAssociation(
    name="substates4",
    ends={
        Property(name="State5", type=ControllerUML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="theContainer", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theContainer6: BinaryAssociation = BinaryAssociation(
    name="theContainer6",
    ends={
        Property(name="State7", type=ControllerUML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="substates", type=State, multiplicity=Multiplicity(0, 1))
    }
)
effect18: BinaryAssociation = BinaryAssociation(
    name="effect18",
    ends={
        Property(name="StateMachineAction", type=ControllerUML_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ControllerUML_StateTransition19", type=StateMachineAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incoming9: BinaryAssociation = BinaryAssociation(
    name="incoming9",
    ends={
        Property(name="StateTransition10", type=ControllerUML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=StateTransition, multiplicity=Multiplicity(0, 9999))
    }
)
controller11: BinaryAssociation = BinaryAssociation(
    name="controller11",
    ends={
        Property(name="Controller12", type=ControllerUML_SubControllerState, multiplicity=Multiplicity(1, 1)),
        Property(name="ControllerUML_SubControllerState", type=Controller, multiplicity=Multiplicity(1, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="State14", type=ControllerUML_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outGoing", type=State, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="State16", type=ControllerUML_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=State, multiplicity=Multiplicity(1, 1))
    }
)
trigger17: BinaryAssociation = BinaryAssociation(
    name="trigger17",
    ends={
        Property(name="Event", type=ControllerUML_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ControllerUML_StateTransition", type=Event, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ControllerUML_SubControllerState_State = Generalization(general=State, specific=ControllerUML_SubControllerState)
gen_ControllerUML_ViewState_State = Generalization(general=State, specific=ControllerUML_ViewState)

# Domain Model
domain_model = DomainModel(
    name="ControllerUML",
    types={ControllerUML_Controller, ControllerAttribute, ControllerUML_ControllerAttribute, Controller, StateTransition, StateMachine, ControllerUML_StateMachine, State, ControllerUML_State, StateMachineAction, ControllerUML_SubControllerState, ControllerUML_ViewState, ControllerUML_StateTransition, Event, ControllerUML_StateMachineAction, ControllerUML_Event},
    associations={controllerAttribute1, controller0, outGoing8, behavior2, states3, substates4, theContainer6, effect18, incoming9, controller11, source13, target15, trigger17},
    generalizations={gen_ControllerUML_SubControllerState_State, gen_ControllerUML_ViewState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)