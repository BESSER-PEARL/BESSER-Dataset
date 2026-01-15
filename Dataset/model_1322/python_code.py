from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class NameBase:

    pass
class StateAction:

    pass
class statechart_ENTRY(StateAction):

    pass
class statechart_EXIT(StateAction):

    pass
class statechart_DO(StateAction):

    pass
class Action:

    pass
class statechart_TransitionAction(Action):

    pass
class State:

    pass
class statechart_CompositeState(State):

    def __init__(self, isConcurrent: bool, sv_container: set["statechart_StateVertex"] = None, CompositeState: "statechart_StateVertex" = None):
        self.isConcurrent = isConcurrent
        self.sv_container = sv_container if sv_container is not None else set()
        self.CompositeState = CompositeState
        
    @property
    def isConcurrent(self) -> bool:
        return self.__isConcurrent

    @isConcurrent.setter
    def isConcurrent(self, isConcurrent: bool):
        self.__isConcurrent = isConcurrent

    @property
    def sv_container(self):
        return self.__sv_container

    @sv_container.setter
    def sv_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_CompositeState__sv_container", None)
        self.__sv_container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateVertex"):
                    opp_val = getattr(item, "StateVertex", None)
                    
                    if opp_val == self:
                        setattr(item, "StateVertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateVertex"):
                    opp_val = getattr(item, "StateVertex", None)
                    
                    setattr(item, "StateVertex", self)
                    

    @property
    def CompositeState(self):
        return self.__CompositeState

    @CompositeState.setter
    def CompositeState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_CompositeState__CompositeState", None)
        self.__CompositeState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subVertexes"):
                opp_val = getattr(old_value, "subVertexes", None)
                if opp_val == self:
                    setattr(old_value, "subVertexes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subVertexes"):
                opp_val = getattr(value, "subVertexes", None)
                setattr(value, "subVertexes", self)

class statechart_StateAction(Action):

    pass
class StateVertex:

    pass
class statechart_State(StateVertex):

    pass
class IDBase:

    pass
class statechart_Transition(IDBase):

    def __init__(self, description: str, Transition: "statechart_StateMachine" = None, Transition11: "statechart_State" = None, internalTransitions: "statechart_State" = None, evt_container: "statechart_Event" = None, gua_container: "statechart_Guard" = None, act_container: "statechart_TransitionAction" = None, outgoing: "statechart_StateVertex" = None, incoming: "statechart_StateVertex" = None, Transition30: "statechart_Event" = None, Transition32: "statechart_Guard" = None, transitions: "statechart_StateMachine" = None, Transition37: "statechart_StateVertex" = None, Transition39: "statechart_StateVertex" = None, Transition34: "statechart_TransitionAction" = None):
        self.description = description
        self.Transition = Transition
        self.Transition11 = Transition11
        self.internalTransitions = internalTransitions
        self.evt_container = evt_container
        self.gua_container = gua_container
        self.act_container = act_container
        self.outgoing = outgoing
        self.incoming = incoming
        self.Transition30 = Transition30
        self.Transition32 = Transition32
        self.transitions = transitions
        self.Transition37 = Transition37
        self.Transition39 = Transition39
        self.Transition34 = Transition34
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transSM_container"):
                opp_val = getattr(old_value, "transSM_container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transSM_container"):
                opp_val = getattr(value, "transSM_container", None)
                if opp_val is None:
                    setattr(value, "transSM_container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateVertex28"):
                opp_val = getattr(old_value, "StateVertex28", None)
                if opp_val == self:
                    setattr(old_value, "StateVertex28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateVertex28"):
                opp_val = getattr(value, "StateVertex28", None)
                setattr(value, "StateVertex28", self)

    @property
    def evt_container(self):
        return self.__evt_container

    @evt_container.setter
    def evt_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__evt_container", None)
        self.__evt_container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Event"):
                opp_val = getattr(old_value, "Event", None)
                if opp_val == self:
                    setattr(old_value, "Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Event"):
                opp_val = getattr(value, "Event", None)
                setattr(value, "Event", self)

    @property
    def Transition11(self):
        return self.__Transition11

    @Transition11.setter
    def Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition11", None)
        self.__Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transS_container"):
                opp_val = getattr(old_value, "transS_container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transS_container"):
                opp_val = getattr(value, "transS_container", None)
                if opp_val is None:
                    setattr(value, "transS_container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition37(self):
        return self.__Transition37

    @Transition37.setter
    def Transition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition37", None)
        self.__Transition37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def internalTransitions(self):
        return self.__internalTransitions

    @internalTransitions.setter
    def internalTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__internalTransitions", None)
        self.__internalTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State21"):
                opp_val = getattr(old_value, "State21", None)
                if opp_val == self:
                    setattr(old_value, "State21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State21"):
                opp_val = getattr(value, "State21", None)
                setattr(value, "State21", self)

    @property
    def Transition32(self):
        return self.__Transition32

    @Transition32.setter
    def Transition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition32", None)
        self.__Transition32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guard"):
                opp_val = getattr(old_value, "guard", None)
                if opp_val == self:
                    setattr(old_value, "guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guard"):
                opp_val = getattr(value, "guard", None)
                setattr(value, "guard", self)

    @property
    def gua_container(self):
        return self.__gua_container

    @gua_container.setter
    def gua_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__gua_container", None)
        self.__gua_container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Guard"):
                opp_val = getattr(old_value, "Guard", None)
                if opp_val == self:
                    setattr(old_value, "Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Guard"):
                opp_val = getattr(value, "Guard", None)
                setattr(value, "Guard", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateVertex26"):
                opp_val = getattr(old_value, "StateVertex26", None)
                if opp_val == self:
                    setattr(old_value, "StateVertex26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateVertex26"):
                opp_val = getattr(value, "StateVertex26", None)
                setattr(value, "StateVertex26", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine19"):
                opp_val = getattr(old_value, "StateMachine19", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine19"):
                opp_val = getattr(value, "StateMachine19", None)
                setattr(value, "StateMachine19", self)

    @property
    def Transition30(self):
        return self.__Transition30

    @Transition30.setter
    def Transition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition30", None)
        self.__Transition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trigger"):
                opp_val = getattr(old_value, "trigger", None)
                if opp_val == self:
                    setattr(old_value, "trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trigger"):
                opp_val = getattr(value, "trigger", None)
                setattr(value, "trigger", self)

    @property
    def Transition39(self):
        return self.__Transition39

    @Transition39.setter
    def Transition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition39", None)
        self.__Transition39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition34(self):
        return self.__Transition34

    @Transition34.setter
    def Transition34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__Transition34", None)
        self.__Transition34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "action"):
                opp_val = getattr(old_value, "action", None)
                if opp_val == self:
                    setattr(old_value, "action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "action"):
                opp_val = getattr(value, "action", None)
                setattr(value, "action", self)

    @property
    def act_container(self):
        return self.__act_container

    @act_container.setter
    def act_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Transition__act_container", None)
        self.__act_container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransitionAction"):
                opp_val = getattr(old_value, "TransitionAction", None)
                if opp_val == self:
                    setattr(old_value, "TransitionAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransitionAction"):
                opp_val = getattr(value, "TransitionAction", None)
                setattr(value, "TransitionAction", self)

class statechart_Label(IDBase):

    def __init__(self, name: str, statechart_Label: "statechart_StateVertex" = None):
        self.name = name
        self.statechart_Label = statechart_Label
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statechart_Label(self):
        return self.__statechart_Label

    @statechart_Label.setter
    def statechart_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Label__statechart_Label", None)
        self.__statechart_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_StateVertex"):
                opp_val = getattr(old_value, "statechart_StateVertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_StateVertex"):
                opp_val = getattr(value, "statechart_StateVertex", None)
                if opp_val is None:
                    setattr(value, "statechart_StateVertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statechart_Action(IDBase):

    def __init__(self, value: str, Action: "statechart_StateMachine" = None, calledByAction: "statechart_StateMachine" = None):
        self.value = value
        self.Action = Action
        self.calledByAction = calledByAction
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachineCall"):
                opp_val = getattr(old_value, "stateMachineCall", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachineCall"):
                opp_val = getattr(value, "stateMachineCall", None)
                if opp_val is None:
                    setattr(value, "stateMachineCall", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def calledByAction(self):
        return self.__calledByAction

    @calledByAction.setter
    def calledByAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Action__calledByAction", None)
        self.__calledByAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine17"):
                opp_val = getattr(old_value, "StateMachine17", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine17"):
                opp_val = getattr(value, "StateMachine17", None)
                setattr(value, "StateMachine17", self)

class statechart_Guard(IDBase):

    def __init__(self, expression: str, Guard: "statechart_Transition" = None, guard: "statechart_Transition" = None):
        self.expression = expression
        self.Guard = Guard
        self.guard = guard
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def guard(self):
        return self.__guard

    @guard.setter
    def guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Guard__guard", None)
        self.__guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition32"):
                opp_val = getattr(old_value, "Transition32", None)
                if opp_val == self:
                    setattr(old_value, "Transition32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition32"):
                opp_val = getattr(value, "Transition32", None)
                setattr(value, "Transition32", self)

    @property
    def Guard(self):
        return self.__Guard

    @Guard.setter
    def Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Guard__Guard", None)
        self.__Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gua_container"):
                opp_val = getattr(old_value, "gua_container", None)
                if opp_val == self:
                    setattr(old_value, "gua_container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gua_container"):
                opp_val = getattr(value, "gua_container", None)
                setattr(value, "gua_container", self)

class statechart_Event(IDBase):

    def __init__(self, name: str, statechart_Event: "statechart_State" = None, Event: "statechart_Transition" = None, trigger: "statechart_Transition" = None):
        self.name = name
        self.statechart_Event = statechart_Event
        self.Event = Event
        self.trigger = trigger
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def statechart_Event(self):
        return self.__statechart_Event

    @statechart_Event.setter
    def statechart_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Event__statechart_Event", None)
        self.__statechart_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_State13"):
                opp_val = getattr(old_value, "statechart_State13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_State13"):
                opp_val = getattr(value, "statechart_State13", None)
                if opp_val is None:
                    setattr(value, "statechart_State13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trigger(self):
        return self.__trigger

    @trigger.setter
    def trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Event__trigger", None)
        self.__trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition30"):
                opp_val = getattr(old_value, "Transition30", None)
                if opp_val == self:
                    setattr(old_value, "Transition30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition30"):
                opp_val = getattr(value, "Transition30", None)
                setattr(value, "Transition30", self)

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_Event__Event", None)
        self.__Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evt_container"):
                opp_val = getattr(old_value, "evt_container", None)
                if opp_val == self:
                    setattr(old_value, "evt_container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evt_container"):
                opp_val = getattr(value, "evt_container", None)
                setattr(value, "evt_container", self)

class statechart_StateVertex(NameBase, IDBase):

    pass
class statechart_StateMachine(IDBase):

    def __init__(self, name: str, StateMachine: "statechart_StateMachineRoot" = None, statechart_StateMachine: "statechart_StateMachineRoot" = None, transSM_container: set["statechart_Transition"] = None, stateMachineCall: set["statechart_Action"] = None, statechart_StateMachine7: "statechart_State" = None, StateMachine9: "statechart_State" = None, state_container: set["statechart_State"] = None, subStateMachines: "statechart_StateMachineRoot" = None, StateMachine17: "statechart_Action" = None, StateMachine19: "statechart_Transition" = None):
        self.name = name
        self.StateMachine = StateMachine
        self.statechart_StateMachine = statechart_StateMachine
        self.transSM_container = transSM_container if transSM_container is not None else set()
        self.stateMachineCall = stateMachineCall if stateMachineCall is not None else set()
        self.statechart_StateMachine7 = statechart_StateMachine7
        self.StateMachine9 = StateMachine9
        self.state_container = state_container if state_container is not None else set()
        self.subStateMachines = subStateMachines
        self.StateMachine17 = StateMachine17
        self.StateMachine19 = StateMachine19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StateMachine(self):
        return self.__StateMachine

    @StateMachine.setter
    def StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__StateMachine", None)
        self.__StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_container"):
                opp_val = getattr(old_value, "statemachine_container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_container"):
                opp_val = getattr(value, "statemachine_container", None)
                if opp_val is None:
                    setattr(value, "statemachine_container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transSM_container(self):
        return self.__transSM_container

    @transSM_container.setter
    def transSM_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__transSM_container", None)
        self.__transSM_container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def subStateMachines(self):
        return self.__subStateMachines

    @subStateMachines.setter
    def subStateMachines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__subStateMachines", None)
        self.__subStateMachines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachineRoot"):
                opp_val = getattr(old_value, "StateMachineRoot", None)
                if opp_val == self:
                    setattr(old_value, "StateMachineRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachineRoot"):
                opp_val = getattr(value, "StateMachineRoot", None)
                setattr(value, "StateMachineRoot", self)

    @property
    def StateMachine9(self):
        return self.__StateMachine9

    @StateMachine9.setter
    def StateMachine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__StateMachine9", None)
        self.__StateMachine9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "top"):
                opp_val = getattr(old_value, "top", None)
                if opp_val == self:
                    setattr(old_value, "top", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "top"):
                opp_val = getattr(value, "top", None)
                setattr(value, "top", self)

    @property
    def statechart_StateMachine7(self):
        return self.__statechart_StateMachine7

    @statechart_StateMachine7.setter
    def statechart_StateMachine7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__statechart_StateMachine7", None)
        self.__statechart_StateMachine7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_State"):
                opp_val = getattr(old_value, "statechart_State", None)
                if opp_val == self:
                    setattr(old_value, "statechart_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_State"):
                opp_val = getattr(value, "statechart_State", None)
                setattr(value, "statechart_State", self)

    @property
    def StateMachine19(self):
        return self.__StateMachine19

    @StateMachine19.setter
    def StateMachine19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__StateMachine19", None)
        self.__StateMachine19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def statechart_StateMachine(self):
        return self.__statechart_StateMachine

    @statechart_StateMachine.setter
    def statechart_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__statechart_StateMachine", None)
        self.__statechart_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statechart_StateMachineRoot"):
                opp_val = getattr(old_value, "statechart_StateMachineRoot", None)
                if opp_val == self:
                    setattr(old_value, "statechart_StateMachineRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statechart_StateMachineRoot"):
                opp_val = getattr(value, "statechart_StateMachineRoot", None)
                setattr(value, "statechart_StateMachineRoot", self)

    @property
    def stateMachineCall(self):
        return self.__stateMachineCall

    @stateMachineCall.setter
    def stateMachineCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__stateMachineCall", None)
        self.__stateMachineCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

    @property
    def state_container(self):
        return self.__state_container

    @state_container.setter
    def state_container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__state_container", None)
        self.__state_container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    if opp_val == self:
                        setattr(item, "State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "State"):
                    opp_val = getattr(item, "State", None)
                    
                    setattr(item, "State", self)
                    

    @property
    def StateMachine17(self):
        return self.__StateMachine17

    @StateMachine17.setter
    def StateMachine17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statechart_StateMachine__StateMachine17", None)
        self.__StateMachine17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calledByAction"):
                opp_val = getattr(old_value, "calledByAction", None)
                if opp_val == self:
                    setattr(old_value, "calledByAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calledByAction"):
                opp_val = getattr(value, "calledByAction", None)
                setattr(value, "calledByAction", self)

class statechart_StateMachineRoot(IDBase):

    pass