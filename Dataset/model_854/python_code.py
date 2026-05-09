from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fsm_Region:

    pass
class Pseudostate:

    pass
class fsm_Choice(Pseudostate):

    pass
class fsm_Join(Pseudostate):

    pass
class fsm_Fork(Pseudostate):

    pass
class fsm_Trigger:

    def __init__(self, expression: str, fsm_Trigger: "fsm_Transition" = None):
        self.expression = expression
        self.fsm_Trigger = fsm_Trigger
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def fsm_Trigger(self):
        return self.__fsm_Trigger

    @fsm_Trigger.setter
    def fsm_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Trigger__fsm_Trigger", None)
        self.__fsm_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition"):
                opp_val = getattr(old_value, "fsm_Transition", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition"):
                opp_val = getattr(value, "fsm_Transition", None)
                setattr(value, "fsm_Transition", self)

class State:

    pass
class fsm_Pseudostate(State):

    pass
class fsm_InitialState(State):

    pass
class fsm_FinalState(State):

    pass
class fsm_CompositeState(State):

    pass
class fsm_Variable:

    def __init__(self, name: str, value: bool, fsm_Variable: "fsm_StateMachine" = None):
        self.name = name
        self.value = value
        self.fsm_Variable = fsm_Variable
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


    @property
    def fsm_Variable(self):
        return self.__fsm_Variable

    @fsm_Variable.setter
    def fsm_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Variable__fsm_Variable", None)
        self.__fsm_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_StateMachine"):
                opp_val = getattr(old_value, "fsm_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_StateMachine"):
                opp_val = getattr(value, "fsm_StateMachine", None)
                if opp_val is None:
                    setattr(value, "fsm_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transition:

    pass
class fsm_TimedTransition(Transition):

    def __init__(self, duration: int):
        self.duration = duration
        
        pass
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration


class fsm_Action:

    def __init__(self, variable: str, value: bool, fsm_Action: "fsm_Transition" = None):
        self.variable = variable
        self.value = value
        self.fsm_Action = fsm_Action
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable


    @property
    def fsm_Action(self):
        return self.__fsm_Action

    @fsm_Action.setter
    def fsm_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Action__fsm_Action", None)
        self.__fsm_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition20"):
                opp_val = getattr(old_value, "fsm_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition20"):
                opp_val = getattr(value, "fsm_Transition20", None)
                setattr(value, "fsm_Transition20", self)

class fsm_Guard:

    def __init__(self, expression: str, fsm_Guard: "fsm_Transition" = None):
        self.expression = expression
        self.fsm_Guard = fsm_Guard
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def fsm_Guard(self):
        return self.__fsm_Guard

    @fsm_Guard.setter
    def fsm_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Guard__fsm_Guard", None)
        self.__fsm_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Transition18"):
                opp_val = getattr(old_value, "fsm_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Transition18"):
                opp_val = getattr(value, "fsm_Transition18", None)
                setattr(value, "fsm_Transition18", self)

class NamedElement:

    pass
class fsm_State(NamedElement):

    def __init__(self, initialTime: int, finalTime: int, State: "fsm_StateMachine" = None, source: set["fsm_Transition"] = None, target: set["fsm_Transition"] = None, states: "fsm_StateMachine" = None, fsm_State: "fsm_CompositeState" = None, State11: "fsm_Transition" = None, State13: "fsm_Transition" = None, fsm_State25: "fsm_Region" = None):
        self.initialTime = initialTime
        self.finalTime = finalTime
        self.State = State
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.states = states
        self.fsm_State = fsm_State
        self.State11 = State11
        self.State13 = State13
        self.fsm_State25 = fsm_State25
        
        pass
    @property
    def finalTime(self):
        return self.__finalTime

    @finalTime.setter
    def finalTime(self, finalTime: int):
        self.__finalTime = finalTime


    @property
    def initialTime(self):
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime


    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine"):
                opp_val = getattr(old_value, "StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine"):
                opp_val = getattr(value, "StateMachine", None)
                setattr(value, "StateMachine", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition7"):
                    opp_val = getattr(item, "Transition7", None)
                    
                    setattr(item, "Transition7", self)
                    

    @property
    def State11(self):
        return self.__State11

    @State11.setter
    def State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State11", None)
        self.__State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine"):
                opp_val = getattr(old_value, "stateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine"):
                opp_val = getattr(value, "stateMachine", None)
                if opp_val is None:
                    setattr(value, "stateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_State(self):
        return self.__fsm_State

    @fsm_State.setter
    def fsm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State", None)
        self.__fsm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_CompositeState"):
                opp_val = getattr(old_value, "fsm_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "fsm_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_CompositeState"):
                opp_val = getattr(value, "fsm_CompositeState", None)
                setattr(value, "fsm_CompositeState", self)

    @property
    def State13(self):
        return self.__State13

    @State13.setter
    def State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__State13", None)
        self.__State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def fsm_State25(self):
        return self.__fsm_State25

    @fsm_State25.setter
    def fsm_State25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__fsm_State25", None)
        self.__fsm_State25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Region24"):
                opp_val = getattr(old_value, "fsm_Region24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Region24"):
                opp_val = getattr(value, "fsm_Region24", None)
                if opp_val is None:
                    setattr(value, "fsm_Region24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition5"):
                    opp_val = getattr(item, "Transition5", None)
                    
                    setattr(item, "Transition5", self)
                    

class fsm_Transition(NamedElement):

    def __init__(self, initialTime: int, finalTime: int, Transition: "fsm_StateMachine" = None, transitions: "fsm_StateMachine" = None, fsm_Transition18: "fsm_Guard" = None, fsm_Transition20: "fsm_Action" = None, Transition5: "fsm_State" = None, Transition7: "fsm_State" = None, incoming: "fsm_State" = None, outgoing: "fsm_State" = None, fsm_Transition: "fsm_Trigger" = None):
        self.initialTime = initialTime
        self.finalTime = finalTime
        self.Transition = Transition
        self.transitions = transitions
        self.fsm_Transition18 = fsm_Transition18
        self.fsm_Transition20 = fsm_Transition20
        self.Transition5 = Transition5
        self.Transition7 = Transition7
        self.incoming = incoming
        self.outgoing = outgoing
        self.fsm_Transition = fsm_Transition
        
        pass
    @property
    def initialTime(self):
        return self.__initialTime

    @initialTime.setter
    def initialTime(self, initialTime: int):
        self.__initialTime = initialTime


    @property
    def finalTime(self):
        return self.__finalTime

    @finalTime.setter
    def finalTime(self, finalTime: int):
        self.__finalTime = finalTime


    @property
    def fsm_Transition20(self):
        return self.__fsm_Transition20

    @fsm_Transition20.setter
    def fsm_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition20", None)
        self.__fsm_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Action"):
                opp_val = getattr(old_value, "fsm_Action", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Action"):
                opp_val = getattr(value, "fsm_Action", None)
                setattr(value, "fsm_Action", self)

    @property
    def Transition7(self):
        return self.__Transition7

    @Transition7.setter
    def Transition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition7", None)
        self.__Transition7 = value
        
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
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State13"):
                opp_val = getattr(old_value, "State13", None)
                if opp_val == self:
                    setattr(old_value, "State13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State13"):
                opp_val = getattr(value, "State13", None)
                setattr(value, "State13", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stateMachine2"):
                opp_val = getattr(old_value, "stateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stateMachine2"):
                opp_val = getattr(value, "stateMachine2", None)
                if opp_val is None:
                    setattr(value, "stateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fsm_Transition18(self):
        return self.__fsm_Transition18

    @fsm_Transition18.setter
    def fsm_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition18", None)
        self.__fsm_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Guard"):
                opp_val = getattr(old_value, "fsm_Guard", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Guard"):
                opp_val = getattr(value, "fsm_Guard", None)
                setattr(value, "fsm_Guard", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State11"):
                opp_val = getattr(old_value, "State11", None)
                if opp_val == self:
                    setattr(old_value, "State11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State11"):
                opp_val = getattr(value, "State11", None)
                setattr(value, "State11", self)

    @property
    def fsm_Transition(self):
        return self.__fsm_Transition

    @fsm_Transition.setter
    def fsm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__fsm_Transition", None)
        self.__fsm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fsm_Trigger"):
                opp_val = getattr(old_value, "fsm_Trigger", None)
                if opp_val == self:
                    setattr(old_value, "fsm_Trigger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fsm_Trigger"):
                opp_val = getattr(value, "fsm_Trigger", None)
                setattr(value, "fsm_Trigger", self)

    @property
    def Transition5(self):
        return self.__Transition5

    @Transition5.setter
    def Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__Transition5", None)
        self.__Transition5 = value
        
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
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fsm_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StateMachine16"):
                opp_val = getattr(old_value, "StateMachine16", None)
                if opp_val == self:
                    setattr(old_value, "StateMachine16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StateMachine16"):
                opp_val = getattr(value, "StateMachine16", None)
                setattr(value, "StateMachine16", self)

class fsm_StateMachine(NamedElement):

    pass
class fsm_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

