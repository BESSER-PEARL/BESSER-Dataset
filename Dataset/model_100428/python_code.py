from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class statemachine_FinalState(State):

    pass
class statemachine_InitialState(State):

    pass
class statemachine_NormalState(State):

    pass
class statemachine_Action:

    def __init__(self, actionLabel: str, statemachine_Action: "statemachine_Statement" = None, statemachine_Action20: "statemachine_NormalState" = None):
        self.actionLabel = actionLabel
        self.statemachine_Action = statemachine_Action
        self.statemachine_Action20 = statemachine_Action20
        
        pass
    @property
    def actionLabel(self):
        return self.__actionLabel

    @actionLabel.setter
    def actionLabel(self, actionLabel: str):
        self.__actionLabel = actionLabel


    @property
    def statemachine_Action(self):
        return self.__statemachine_Action

    @statemachine_Action.setter
    def statemachine_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Action__statemachine_Action", None)
        self.__statemachine_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statement18"):
                opp_val = getattr(old_value, "statemachine_Statement18", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Statement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statement18"):
                opp_val = getattr(value, "statemachine_Statement18", None)
                setattr(value, "statemachine_Statement18", self)

    @property
    def statemachine_Action20(self):
        return self.__statemachine_Action20

    @statemachine_Action20.setter
    def statemachine_Action20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Action__statemachine_Action20", None)
        self.__statemachine_Action20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_NormalState"):
                opp_val = getattr(old_value, "statemachine_NormalState", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_NormalState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_NormalState"):
                opp_val = getattr(value, "statemachine_NormalState", None)
                setattr(value, "statemachine_NormalState", self)

class statemachine_Statement:

    pass
class statemachine_Expression:

    pass
class Declaration:

    pass
class statemachine_State(Declaration):

    def __init__(self, label: str, id: int, statemachine_State: "statemachine_Transition" = None, statemachine_State6: "statemachine_Transition" = None, statemachine_State16: "statemachine_State" = None, statemachine_State14: set["statemachine_State"] = None, statemachine_State13: "statemachine_State" = None, statemachine_State11: set["statemachine_State"] = None):
        self.label = label
        self.id = id
        self.statemachine_State = statemachine_State
        self.statemachine_State6 = statemachine_State6
        self.statemachine_State16 = statemachine_State16
        self.statemachine_State14 = statemachine_State14 if statemachine_State14 is not None else set()
        self.statemachine_State13 = statemachine_State13
        self.statemachine_State11 = statemachine_State11 if statemachine_State11 is not None else set()
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def statemachine_State14(self):
        return self.__statemachine_State14

    @statemachine_State14.setter
    def statemachine_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State14", None)
        self.__statemachine_State14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State16"):
                    opp_val = getattr(item, "statemachine_State16", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State16"):
                    opp_val = getattr(item, "statemachine_State16", None)
                    
                    setattr(item, "statemachine_State16", self)
                    

    @property
    def statemachine_State11(self):
        return self.__statemachine_State11

    @statemachine_State11.setter
    def statemachine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State11", None)
        self.__statemachine_State11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_State13"):
                    opp_val = getattr(item, "statemachine_State13", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_State13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_State13"):
                    opp_val = getattr(item, "statemachine_State13", None)
                    
                    setattr(item, "statemachine_State13", self)
                    

    @property
    def statemachine_State(self):
        return self.__statemachine_State

    @statemachine_State.setter
    def statemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State", None)
        self.__statemachine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition"):
                opp_val = getattr(old_value, "statemachine_Transition", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition"):
                opp_val = getattr(value, "statemachine_Transition", None)
                setattr(value, "statemachine_Transition", self)

    @property
    def statemachine_State16(self):
        return self.__statemachine_State16

    @statemachine_State16.setter
    def statemachine_State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State16", None)
        self.__statemachine_State16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State14"):
                opp_val = getattr(old_value, "statemachine_State14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State14"):
                opp_val = getattr(value, "statemachine_State14", None)
                if opp_val is None:
                    setattr(value, "statemachine_State14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_State6(self):
        return self.__statemachine_State6

    @statemachine_State6.setter
    def statemachine_State6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State6", None)
        self.__statemachine_State6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Transition5"):
                opp_val = getattr(old_value, "statemachine_Transition5", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Transition5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Transition5"):
                opp_val = getattr(value, "statemachine_Transition5", None)
                setattr(value, "statemachine_Transition5", self)

    @property
    def statemachine_State13(self):
        return self.__statemachine_State13

    @statemachine_State13.setter
    def statemachine_State13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_State__statemachine_State13", None)
        self.__statemachine_State13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State11"):
                opp_val = getattr(old_value, "statemachine_State11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State11"):
                opp_val = getattr(value, "statemachine_State11", None)
                if opp_val is None:
                    setattr(value, "statemachine_State11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def printReachable(self):
        # TODO: Implement printReachable method
        pass

class statemachine_Transition(Declaration):

    def __init__(self, label: str, guardLabel: str, actionLabel: str, sourceLabel: str, targetLabel: str, statemachine_Transition: "statemachine_State" = None, statemachine_Transition5: "statemachine_State" = None, statemachine_Transition8: "statemachine_Expression" = None, statemachine_Transition10: "statemachine_Statement" = None):
        self.label = label
        self.guardLabel = guardLabel
        self.actionLabel = actionLabel
        self.sourceLabel = sourceLabel
        self.targetLabel = targetLabel
        self.statemachine_Transition = statemachine_Transition
        self.statemachine_Transition5 = statemachine_Transition5
        self.statemachine_Transition8 = statemachine_Transition8
        self.statemachine_Transition10 = statemachine_Transition10
        
        pass
    @property
    def actionLabel(self):
        return self.__actionLabel

    @actionLabel.setter
    def actionLabel(self, actionLabel: str):
        self.__actionLabel = actionLabel


    @property
    def sourceLabel(self):
        return self.__sourceLabel

    @sourceLabel.setter
    def sourceLabel(self, sourceLabel: str):
        self.__sourceLabel = sourceLabel


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def targetLabel(self):
        return self.__targetLabel

    @targetLabel.setter
    def targetLabel(self, targetLabel: str):
        self.__targetLabel = targetLabel


    @property
    def guardLabel(self):
        return self.__guardLabel

    @guardLabel.setter
    def guardLabel(self, guardLabel: str):
        self.__guardLabel = guardLabel


    @property
    def statemachine_Transition10(self):
        return self.__statemachine_Transition10

    @statemachine_Transition10.setter
    def statemachine_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition10", None)
        self.__statemachine_Transition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Statement"):
                opp_val = getattr(old_value, "statemachine_Statement", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Statement"):
                opp_val = getattr(value, "statemachine_Statement", None)
                setattr(value, "statemachine_Statement", self)

    @property
    def statemachine_Transition(self):
        return self.__statemachine_Transition

    @statemachine_Transition.setter
    def statemachine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition", None)
        self.__statemachine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State"):
                opp_val = getattr(old_value, "statemachine_State", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State"):
                opp_val = getattr(value, "statemachine_State", None)
                setattr(value, "statemachine_State", self)

    @property
    def statemachine_Transition5(self):
        return self.__statemachine_Transition5

    @statemachine_Transition5.setter
    def statemachine_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition5", None)
        self.__statemachine_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_State6"):
                opp_val = getattr(old_value, "statemachine_State6", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_State6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_State6"):
                opp_val = getattr(value, "statemachine_State6", None)
                setattr(value, "statemachine_State6", self)

    @property
    def statemachine_Transition8(self):
        return self.__statemachine_Transition8

    @statemachine_Transition8.setter
    def statemachine_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Transition__statemachine_Transition8", None)
        self.__statemachine_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_Expression"):
                opp_val = getattr(old_value, "statemachine_Expression", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_Expression"):
                opp_val = getattr(value, "statemachine_Expression", None)
                setattr(value, "statemachine_Expression", self)

class statemachine_StateMachineVariable:

    def __init__(self, name: str, type: str, statemachine_StateMachineVariable: "statemachine_StateMachine" = None):
        self.name = name
        self.type = type
        self.statemachine_StateMachineVariable = statemachine_StateMachineVariable
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def statemachine_StateMachineVariable(self):
        return self.__statemachine_StateMachineVariable

    @statemachine_StateMachineVariable.setter
    def statemachine_StateMachineVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachineVariable__statemachine_StateMachineVariable", None)
        self.__statemachine_StateMachineVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine2"):
                opp_val = getattr(old_value, "statemachine_StateMachine2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine2"):
                opp_val = getattr(value, "statemachine_StateMachine2", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_Declaration(ABC):

    def __init__(self, statemachine_Declaration: "statemachine_StateMachine" = None):
        self.statemachine_Declaration = statemachine_Declaration
        
        pass
    @property
    def statemachine_Declaration(self):
        return self.__statemachine_Declaration

    @statemachine_Declaration.setter
    def statemachine_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Declaration__statemachine_Declaration", None)
        self.__statemachine_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateMachine"):
                opp_val = getattr(old_value, "statemachine_StateMachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateMachine"):
                opp_val = getattr(value, "statemachine_StateMachine", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateMachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def printReachable(self):
        # TODO: Implement printReachable method
        pass

class statemachine_StateMachine:

    def __init__(self, statemachine_StateMachine: set["statemachine_Declaration"] = None, statemachine_StateMachine2: set["statemachine_StateMachineVariable"] = None):
        self.statemachine_StateMachine = statemachine_StateMachine if statemachine_StateMachine is not None else set()
        self.statemachine_StateMachine2 = statemachine_StateMachine2 if statemachine_StateMachine2 is not None else set()
        
        pass
    @property
    def statemachine_StateMachine(self):
        return self.__statemachine_StateMachine

    @statemachine_StateMachine.setter
    def statemachine_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine", None)
        self.__statemachine_StateMachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_Declaration"):
                    opp_val = getattr(item, "statemachine_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_Declaration"):
                    opp_val = getattr(item, "statemachine_Declaration", None)
                    
                    setattr(item, "statemachine_Declaration", self)
                    

    @property
    def statemachine_StateMachine2(self):
        return self.__statemachine_StateMachine2

    @statemachine_StateMachine2.setter
    def statemachine_StateMachine2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateMachine__statemachine_StateMachine2", None)
        self.__statemachine_StateMachine2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_StateMachineVariable"):
                    opp_val = getattr(item, "statemachine_StateMachineVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_StateMachineVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_StateMachineVariable"):
                    opp_val = getattr(item, "statemachine_StateMachineVariable", None)
                    
                    setattr(item, "statemachine_StateMachineVariable", self)
                    

    def printReachable(self):
        # TODO: Implement printReachable method
        pass
