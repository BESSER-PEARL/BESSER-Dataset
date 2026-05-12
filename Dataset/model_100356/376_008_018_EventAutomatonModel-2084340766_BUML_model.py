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
EventAutomatonModel_Automaton = Class(name="EventAutomatonModel_Automaton")
EventAutomatonModel_State = Class(name="EventAutomatonModel_State")
EventAutomatonModel_Token = Class(name="EventAutomatonModel_Token")
EventAutomatonModel_SymbolicParameter = Class(name="EventAutomatonModel_SymbolicParameter", is_abstract=True)
EventAutomatonModel_SymbolicTimer = Class(name="EventAutomatonModel_SymbolicTimer")
EventAutomatonModel_TokenParameterBinding = Class(name="EventAutomatonModel_TokenParameterBinding")
Binding = Class(name="Binding")
EventAutomatonModel_SymbolicTokenParameter = Class(name="EventAutomatonModel_SymbolicTokenParameter")
EventAutomatonModel_ResetTimerAction = Class(name="EventAutomatonModel_ResetTimerAction")
TimerAction = Class(name="TimerAction")
EventAutomatonModel_SymbolicInputEvent = Class(name="EventAutomatonModel_SymbolicInputEvent")
SymbolicEvent = Class(name="SymbolicEvent")
EventAutomatonModel_SymbolicTimeoutEvent = Class(name="EventAutomatonModel_SymbolicTimeoutEvent")
SymbolicParameter = Class(name="SymbolicParameter")
EventAutomatonModel_ComplexEventProcessor = Class(name="EventAutomatonModel_ComplexEventProcessor")
EventAutomatonModel_SymbolicEvent = Class(name="EventAutomatonModel_SymbolicEvent", is_abstract=True)
EventAutomatonModel_Parameter = Class(name="EventAutomatonModel_Parameter", is_abstract=True)
EventAutomatonModel_AbstractTransition = Class(name="EventAutomatonModel_AbstractTransition")
EventAutomatonModel_ConstantBinding = Class(name="EventAutomatonModel_ConstantBinding")
EventAutomatonModel_FixParameter = Class(name="EventAutomatonModel_FixParameter")
EventAutomatonModel_SymbolicEventParameter = Class(name="EventAutomatonModel_SymbolicEventParameter")
EventAutomatonModel_FreeParameter = Class(name="EventAutomatonModel_FreeParameter")
Parameter_ = Class(name="Parameter")
EventAutomatonModel_SetTimerAction = Class(name="EventAutomatonModel_SetTimerAction")
EventAutomatonModel_Binding = Class(name="EventAutomatonModel_Binding", is_abstract=True)
EventAutomatonModel_TimerAction = Class(name="EventAutomatonModel_TimerAction", is_abstract=True)
Action = Class(name="Action")
EventAutomatonModel_EpsilonTransition = Class(name="EventAutomatonModel_EpsilonTransition")
AbstractTransition = Class(name="AbstractTransition")
EventAutomatonModel_Action = Class(name="EventAutomatonModel_Action", is_abstract=True)
EventAutomatonModel_Transition = Class(name="EventAutomatonModel_Transition")
EventAutomatonModel_EventGuard = Class(name="EventAutomatonModel_EventGuard")
EventAutomatonModel_Event = Class(name="EventAutomatonModel_Event")

# EventAutomatonModel_Automaton class attributes and methods
EventAutomatonModel_Automaton_name: Property = Property(name="name", type=StringType)
EventAutomatonModel_Automaton.attributes={EventAutomatonModel_Automaton_name}

# EventAutomatonModel_State class attributes and methods
EventAutomatonModel_State_id: Property = Property(name="id", type=IntegerType)
EventAutomatonModel_State_acceptor: Property = Property(name="acceptor", type=StringType)
EventAutomatonModel_State.attributes={EventAutomatonModel_State_acceptor, EventAutomatonModel_State_id}

# EventAutomatonModel_Token class attributes and methods

# EventAutomatonModel_SymbolicParameter class attributes and methods
EventAutomatonModel_SymbolicParameter_name: Property = Property(name="name", type=StringType)
EventAutomatonModel_SymbolicParameter.attributes={EventAutomatonModel_SymbolicParameter_name}

# EventAutomatonModel_SymbolicTimer class attributes and methods
EventAutomatonModel_SymbolicTimer_name: Property = Property(name="name", type=StringType)
EventAutomatonModel_SymbolicTimer.attributes={EventAutomatonModel_SymbolicTimer_name}

# EventAutomatonModel_TokenParameterBinding class attributes and methods

# Binding class attributes and methods

# EventAutomatonModel_SymbolicTokenParameter class attributes and methods

# EventAutomatonModel_ResetTimerAction class attributes and methods

# TimerAction class attributes and methods

# EventAutomatonModel_SymbolicInputEvent class attributes and methods
EventAutomatonModel_SymbolicInputEvent_name: Property = Property(name="name", type=StringType)
EventAutomatonModel_SymbolicInputEvent.attributes={EventAutomatonModel_SymbolicInputEvent_name}

# SymbolicEvent class attributes and methods

# EventAutomatonModel_SymbolicTimeoutEvent class attributes and methods

# SymbolicParameter class attributes and methods

# EventAutomatonModel_ComplexEventProcessor class attributes and methods

# EventAutomatonModel_SymbolicEvent class attributes and methods

# EventAutomatonModel_Parameter class attributes and methods

# EventAutomatonModel_AbstractTransition class attributes and methods

# EventAutomatonModel_ConstantBinding class attributes and methods

# EventAutomatonModel_FixParameter class attributes and methods
EventAutomatonModel_FixParameter_value: Property = Property(name="value", type=StringType)
EventAutomatonModel_FixParameter.attributes={EventAutomatonModel_FixParameter_value}

# EventAutomatonModel_SymbolicEventParameter class attributes and methods

# EventAutomatonModel_FreeParameter class attributes and methods
EventAutomatonModel_FreeParameter_excludedValues: Property = Property(name="excludedValues", type=StringType)
EventAutomatonModel_FreeParameter.attributes={EventAutomatonModel_FreeParameter_excludedValues}

# Parameter class attributes and methods

# EventAutomatonModel_SetTimerAction class attributes and methods
EventAutomatonModel_SetTimerAction_toValue: Property = Property(name="toValue", type=IntegerType)
EventAutomatonModel_SetTimerAction.attributes={EventAutomatonModel_SetTimerAction_toValue}

# EventAutomatonModel_Binding class attributes and methods

# EventAutomatonModel_TimerAction class attributes and methods

# Action class attributes and methods

# EventAutomatonModel_EpsilonTransition class attributes and methods

# AbstractTransition class attributes and methods

# EventAutomatonModel_Action class attributes and methods

# EventAutomatonModel_Transition class attributes and methods

# EventAutomatonModel_EventGuard class attributes and methods

# EventAutomatonModel_Event class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="EventAutomatonModel_State", type=EventAutomatonModel_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Automaton", type=EventAutomatonModel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens1: BinaryAssociation = BinaryAssociation(
    name="tokens1",
    ends={
        Property(name="EventAutomatonModel_Token", type=EventAutomatonModel_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Automaton2", type=EventAutomatonModel_Token, multiplicity=Multiplicity(0, 9999))
    }
)
initialState3: BinaryAssociation = BinaryAssociation(
    name="initialState3",
    ends={
        Property(name="EventAutomatonModel_State5", type=EventAutomatonModel_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Automaton4", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1))
    }
)
symbolicTokenParameters6: BinaryAssociation = BinaryAssociation(
    name="symbolicTokenParameters6",
    ends={
        Property(name="EventAutomatonModel_SymbolicParameter", type=EventAutomatonModel_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Automaton7", type=EventAutomatonModel_SymbolicParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timers8: BinaryAssociation = BinaryAssociation(
    name="timers8",
    ends={
        Property(name="EventAutomatonModel_SymbolicTimer", type=EventAutomatonModel_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Automaton9", type=EventAutomatonModel_SymbolicTimer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trapState10: BinaryAssociation = BinaryAssociation(
    name="trapState10",
    ends={
        Property(name="EventAutomatonModel_State12", type=EventAutomatonModel_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Automaton11", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1))
    }
)
boundTo13: BinaryAssociation = BinaryAssociation(
    name="boundTo13",
    ends={
        Property(name="EventAutomatonModel_SymbolicTokenParameter", type=EventAutomatonModel_TokenParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_TokenParameterBinding", type=EventAutomatonModel_SymbolicTokenParameter, multiplicity=Multiplicity(1, 1))
    }
)
timeoutEvent14: BinaryAssociation = BinaryAssociation(
    name="timeoutEvent14",
    ends={
        Property(name="SymbolicTimeoutEvent", type=EventAutomatonModel_SymbolicTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="timer", type=EventAutomatonModel_SymbolicTimeoutEvent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
automata15: BinaryAssociation = BinaryAssociation(
    name="automata15",
    ends={
        Property(name="EventAutomatonModel_Automaton16", type=EventAutomatonModel_ComplexEventProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_ComplexEventProcessor", type=EventAutomatonModel_Automaton, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
symbolicEvents17: BinaryAssociation = BinaryAssociation(
    name="symbolicEvents17",
    ends={
        Property(name="EventAutomatonModel_SymbolicInputEvent", type=EventAutomatonModel_ComplexEventProcessor, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_ComplexEventProcessor18", type=EventAutomatonModel_SymbolicInputEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
symbolicParameters19: BinaryAssociation = BinaryAssociation(
    name="symbolicParameters19",
    ends={
        Property(name="EventAutomatonModel_SymbolicParameter20", type=EventAutomatonModel_SymbolicEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_SymbolicEvent", type=EventAutomatonModel_SymbolicParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="EventAutomatonModel_SymbolicParameter22", type=EventAutomatonModel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Parameter", type=EventAutomatonModel_SymbolicParameter, multiplicity=Multiplicity(1, 1))
    }
)
tokens23: BinaryAssociation = BinaryAssociation(
    name="tokens23",
    ends={
        Property(name="Token", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="on", type=EventAutomatonModel_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions24: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions24",
    ends={
        Property(name="AbstractTransition", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=EventAutomatonModel_AbstractTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions25: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions25",
    ends={
        Property(name="AbstractTransition26", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=EventAutomatonModel_AbstractTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundTo27: BinaryAssociation = BinaryAssociation(
    name="boundTo27",
    ends={
        Property(name="EventAutomatonModel_FixParameter", type=EventAutomatonModel_ConstantBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_ConstantBinding", type=EventAutomatonModel_FixParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timer28: BinaryAssociation = BinaryAssociation(
    name="timer28",
    ends={
        Property(name="timeoutEvent", type=EventAutomatonModel_SymbolicTimer, multiplicity=Multiplicity(1, 1)),
        Property(name="SymbolicTimer", type=EventAutomatonModel_SymbolicTimeoutEvent, multiplicity=Multiplicity(1, 1))
    }
)
binds29: BinaryAssociation = BinaryAssociation(
    name="binds29",
    ends={
        Property(name="EventAutomatonModel_SymbolicEventParameter", type=EventAutomatonModel_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Binding", type=EventAutomatonModel_SymbolicEventParameter, multiplicity=Multiplicity(1, 1))
    }
)
timer30: BinaryAssociation = BinaryAssociation(
    name="timer30",
    ends={
        Property(name="EventAutomatonModel_SymbolicTimer31", type=EventAutomatonModel_TimerAction, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_TimerAction", type=EventAutomatonModel_SymbolicTimer, multiplicity=Multiplicity(1, 1))
    }
)
type32: BinaryAssociation = BinaryAssociation(
    name="type32",
    ends={
        Property(name="EventAutomatonModel_SymbolicEvent33", type=EventAutomatonModel_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Event", type=EventAutomatonModel_SymbolicEvent, multiplicity=Multiplicity(1, 1))
    }
)
parameters34: BinaryAssociation = BinaryAssociation(
    name="parameters34",
    ends={
        Property(name="EventAutomatonModel_FixParameter36", type=EventAutomatonModel_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Event35", type=EventAutomatonModel_FixParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
on37: BinaryAssociation = BinaryAssociation(
    name="on37",
    ends={
        Property(name="State", type=EventAutomatonModel_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1))
    }
)
parameters38: BinaryAssociation = BinaryAssociation(
    name="parameters38",
    ends={
        Property(name="EventAutomatonModel_Parameter40", type=EventAutomatonModel_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Token39", type=EventAutomatonModel_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventguard41: BinaryAssociation = BinaryAssociation(
    name="eventguard41",
    ends={
        Property(name="EventAutomatonModel_EventGuard", type=EventAutomatonModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_Transition", type=EventAutomatonModel_EventGuard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindings42: BinaryAssociation = BinaryAssociation(
    name="bindings42",
    ends={
        Property(name="EventAutomatonModel_Binding44", type=EventAutomatonModel_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_EventGuard43", type=EventAutomatonModel_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="EventAutomatonModel_SymbolicEvent47", type=EventAutomatonModel_EventGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_EventGuard46", type=EventAutomatonModel_SymbolicEvent, multiplicity=Multiplicity(0, 1))
    }
)
to48: BinaryAssociation = BinaryAssociation(
    name="to48",
    ends={
        Property(name="State49", type=EventAutomatonModel_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1))
    }
)
from_50: BinaryAssociation = BinaryAssociation(
    name="from_50",
    ends={
        Property(name="State51", type=EventAutomatonModel_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=EventAutomatonModel_State, multiplicity=Multiplicity(1, 1))
    }
)
actions52: BinaryAssociation = BinaryAssociation(
    name="actions52",
    ends={
        Property(name="EventAutomatonModel_Action", type=EventAutomatonModel_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="EventAutomatonModel_AbstractTransition", type=EventAutomatonModel_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_EventAutomatonModel_TokenParameterBinding_Binding = Generalization(general=Binding, specific=EventAutomatonModel_TokenParameterBinding)
gen_EventAutomatonModel_ResetTimerAction_TimerAction = Generalization(general=TimerAction, specific=EventAutomatonModel_ResetTimerAction)
gen_EventAutomatonModel_SymbolicInputEvent_SymbolicEvent = Generalization(general=SymbolicEvent, specific=EventAutomatonModel_SymbolicInputEvent)
gen_EventAutomatonModel_SymbolicTokenParameter_SymbolicParameter = Generalization(general=SymbolicParameter, specific=EventAutomatonModel_SymbolicTokenParameter)
gen_EventAutomatonModel_ConstantBinding_Binding = Generalization(general=Binding, specific=EventAutomatonModel_ConstantBinding)
gen_EventAutomatonModel_SymbolicEventParameter_SymbolicParameter = Generalization(general=SymbolicParameter, specific=EventAutomatonModel_SymbolicEventParameter)
gen_EventAutomatonModel_FreeParameter_Parameter = Generalization(general=Parameter_, specific=EventAutomatonModel_FreeParameter)
gen_EventAutomatonModel_SetTimerAction_TimerAction = Generalization(general=TimerAction, specific=EventAutomatonModel_SetTimerAction)
gen_EventAutomatonModel_SymbolicTimeoutEvent_SymbolicEvent = Generalization(general=SymbolicEvent, specific=EventAutomatonModel_SymbolicTimeoutEvent)
gen_EventAutomatonModel_FixParameter_Parameter = Generalization(general=Parameter_, specific=EventAutomatonModel_FixParameter)
gen_EventAutomatonModel_TimerAction_Action = Generalization(general=Action, specific=EventAutomatonModel_TimerAction)
gen_EventAutomatonModel_EpsilonTransition_AbstractTransition = Generalization(general=AbstractTransition, specific=EventAutomatonModel_EpsilonTransition)
gen_EventAutomatonModel_Transition_AbstractTransition = Generalization(general=AbstractTransition, specific=EventAutomatonModel_Transition)

# Domain Model
domain_model = DomainModel(
    name="EventAutomatonModel",
    types={EventAutomatonModel_Automaton, EventAutomatonModel_State, EventAutomatonModel_Token, EventAutomatonModel_SymbolicParameter, EventAutomatonModel_SymbolicTimer, EventAutomatonModel_TokenParameterBinding, Binding, EventAutomatonModel_SymbolicTokenParameter, EventAutomatonModel_ResetTimerAction, TimerAction, EventAutomatonModel_SymbolicInputEvent, SymbolicEvent, EventAutomatonModel_SymbolicTimeoutEvent, SymbolicParameter, EventAutomatonModel_ComplexEventProcessor, EventAutomatonModel_SymbolicEvent, EventAutomatonModel_Parameter, EventAutomatonModel_AbstractTransition, EventAutomatonModel_ConstantBinding, EventAutomatonModel_FixParameter, EventAutomatonModel_SymbolicEventParameter, EventAutomatonModel_FreeParameter, Parameter_, EventAutomatonModel_SetTimerAction, EventAutomatonModel_Binding, EventAutomatonModel_TimerAction, Action, EventAutomatonModel_EpsilonTransition, AbstractTransition, EventAutomatonModel_Action, EventAutomatonModel_Transition, EventAutomatonModel_EventGuard, EventAutomatonModel_Event},
    associations={states0, tokens1, initialState3, symbolicTokenParameters6, timers8, trapState10, boundTo13, timeoutEvent14, automata15, symbolicEvents17, symbolicParameters19, type21, tokens23, incomingTransitions24, outgoingTransitions25, boundTo27, timer28, binds29, timer30, type32, parameters34, on37, parameters38, eventguard41, bindings42, type45, to48, from_50, actions52},
    generalizations={gen_EventAutomatonModel_TokenParameterBinding_Binding, gen_EventAutomatonModel_ResetTimerAction_TimerAction, gen_EventAutomatonModel_SymbolicInputEvent_SymbolicEvent, gen_EventAutomatonModel_SymbolicTokenParameter_SymbolicParameter, gen_EventAutomatonModel_ConstantBinding_Binding, gen_EventAutomatonModel_SymbolicEventParameter_SymbolicParameter, gen_EventAutomatonModel_FreeParameter_Parameter, gen_EventAutomatonModel_SetTimerAction_TimerAction, gen_EventAutomatonModel_SymbolicTimeoutEvent_SymbolicEvent, gen_EventAutomatonModel_FixParameter_Parameter, gen_EventAutomatonModel_TimerAction_Action, gen_EventAutomatonModel_EpsilonTransition_AbstractTransition, gen_EventAutomatonModel_Transition_AbstractTransition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)