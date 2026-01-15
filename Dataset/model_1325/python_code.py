from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Transition:

    pass
class state_TimeoutTransition(Transition):

    pass
class state_StateMachine:

    def __init__(self, name: str, state_StateMachine: set["state_Node"] = None, state_StateMachine17: set["state_Transition"] = None):
        self.name = name
        self.state_StateMachine = state_StateMachine if state_StateMachine is not None else set()
        self.state_StateMachine17 = state_StateMachine17 if state_StateMachine17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def state_StateMachine17(self):
        return self.__state_StateMachine17

    @state_StateMachine17.setter
    def state_StateMachine17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_StateMachine__state_StateMachine17", None)
        self.__state_StateMachine17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "state_Transition18"):
                    opp_val = getattr(item, "state_Transition18", None)
                    
                    if opp_val == self:
                        setattr(item, "state_Transition18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "state_Transition18"):
                    opp_val = getattr(item, "state_Transition18", None)
                    
                    setattr(item, "state_Transition18", self)
                    

    @property
    def state_StateMachine(self):
        return self.__state_StateMachine

    @state_StateMachine.setter
    def state_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_StateMachine__state_StateMachine", None)
        self.__state_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "state_Node15"):
                    opp_val = getattr(item, "state_Node15", None)
                    
                    if opp_val == self:
                        setattr(item, "state_Node15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "state_Node15"):
                    opp_val = getattr(item, "state_Node15", None)
                    
                    setattr(item, "state_Node15", self)
                    

class state_Transition:

    def __init__(self, triggerEventName: str, state_Transition8: "state_Node" = None, state_Transition11: "state_Condition" = None, state_Transition: "state_Node" = None, state_Transition3: "state_Node" = None, state_Transition5: "state_Node" = None, state_Transition18: "state_StateMachine" = None):
        self.triggerEventName = triggerEventName
        self.state_Transition8 = state_Transition8
        self.state_Transition11 = state_Transition11
        self.state_Transition = state_Transition
        self.state_Transition3 = state_Transition3
        self.state_Transition5 = state_Transition5
        self.state_Transition18 = state_Transition18
        
    @property
    def triggerEventName(self) -> str:
        return self.__triggerEventName

    @triggerEventName.setter
    def triggerEventName(self, triggerEventName: str):
        self.__triggerEventName = triggerEventName

    @property
    def state_Transition(self):
        return self.__state_Transition

    @state_Transition.setter
    def state_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition", None)
        self.__state_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Node"):
                opp_val = getattr(old_value, "state_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Node"):
                opp_val = getattr(value, "state_Node", None)
                if opp_val is None:
                    setattr(value, "state_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def state_Transition5(self):
        return self.__state_Transition5

    @state_Transition5.setter
    def state_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition5", None)
        self.__state_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Node6"):
                opp_val = getattr(old_value, "state_Node6", None)
                if opp_val == self:
                    setattr(old_value, "state_Node6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Node6"):
                opp_val = getattr(value, "state_Node6", None)
                setattr(value, "state_Node6", self)

    @property
    def state_Transition11(self):
        return self.__state_Transition11

    @state_Transition11.setter
    def state_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition11", None)
        self.__state_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Condition"):
                opp_val = getattr(old_value, "state_Condition", None)
                if opp_val == self:
                    setattr(old_value, "state_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Condition"):
                opp_val = getattr(value, "state_Condition", None)
                setattr(value, "state_Condition", self)

    @property
    def state_Transition8(self):
        return self.__state_Transition8

    @state_Transition8.setter
    def state_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition8", None)
        self.__state_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Node9"):
                opp_val = getattr(old_value, "state_Node9", None)
                if opp_val == self:
                    setattr(old_value, "state_Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Node9"):
                opp_val = getattr(value, "state_Node9", None)
                setattr(value, "state_Node9", self)

    @property
    def state_Transition3(self):
        return self.__state_Transition3

    @state_Transition3.setter
    def state_Transition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition3", None)
        self.__state_Transition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Node2"):
                opp_val = getattr(old_value, "state_Node2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Node2"):
                opp_val = getattr(value, "state_Node2", None)
                if opp_val is None:
                    setattr(value, "state_Node2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def state_Transition18(self):
        return self.__state_Transition18

    @state_Transition18.setter
    def state_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Transition__state_Transition18", None)
        self.__state_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_StateMachine17"):
                opp_val = getattr(old_value, "state_StateMachine17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_StateMachine17"):
                opp_val = getattr(value, "state_StateMachine17", None)
                if opp_val is None:
                    setattr(value, "state_StateMachine17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class state_Node(ABC):

    pass
class Node:

    pass
class state_FinalNode(Node):

    pass
class state_State(Node):

    def __init__(self, name: str, duration: str):
        self.name = name
        self.duration = duration
        
    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class state_ConditionalNode(Node):

    pass
class state_InitialNode(Node):

    pass
class state_Condition:

    def __init__(self, expression: str, state_Condition: "state_Transition" = None, state_Condition13: "state_ConditionalNode" = None):
        self.expression = expression
        self.state_Condition = state_Condition
        self.state_Condition13 = state_Condition13
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def state_Condition13(self):
        return self.__state_Condition13

    @state_Condition13.setter
    def state_Condition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Condition__state_Condition13", None)
        self.__state_Condition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_ConditionalNode"):
                opp_val = getattr(old_value, "state_ConditionalNode", None)
                if opp_val == self:
                    setattr(old_value, "state_ConditionalNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_ConditionalNode"):
                opp_val = getattr(value, "state_ConditionalNode", None)
                setattr(value, "state_ConditionalNode", self)

    @property
    def state_Condition(self):
        return self.__state_Condition

    @state_Condition.setter
    def state_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_state_Condition__state_Condition", None)
        self.__state_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "state_Transition11"):
                opp_val = getattr(old_value, "state_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "state_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "state_Transition11"):
                opp_val = getattr(value, "state_Transition11", None)
                setattr(value, "state_Transition11", self)
