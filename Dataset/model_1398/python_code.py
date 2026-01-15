from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractState:

    pass
class model_FiniteStateMachine(AbstractState):

    def __init__(self, 1: "model_AbstractState" = None, 7: set["model_AbstractState"] = None, model_FiniteStateMachine10: "model_AbstractState" = None, model_FiniteStateMachine: "model_AbstractState" = None):
        self.1 = 1
        self.7 = 7 if 7 is not None else set()
        self.model_FiniteStateMachine10 = model_FiniteStateMachine10
        self.model_FiniteStateMachine = model_FiniteStateMachine
        
    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def model_FiniteStateMachine(self):
        return self.__model_FiniteStateMachine

    @model_FiniteStateMachine.setter
    def model_FiniteStateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__model_FiniteStateMachine", None)
        self.__model_FiniteStateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractState"):
                opp_val = getattr(old_value, "model_AbstractState", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState"):
                opp_val = getattr(value, "model_AbstractState", None)
                setattr(value, "model_AbstractState", self)

    @property
    def model_FiniteStateMachine10(self):
        return self.__model_FiniteStateMachine10

    @model_FiniteStateMachine10.setter
    def model_FiniteStateMachine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__model_FiniteStateMachine10", None)
        self.__model_FiniteStateMachine10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractState11"):
                opp_val = getattr(old_value, "model_AbstractState11", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState11"):
                opp_val = getattr(value, "model_AbstractState11", None)
                setattr(value, "model_AbstractState11", self)

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FiniteStateMachine__7", None)
        self.__7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    if opp_val == self:
                        setattr(item, "8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "8"):
                    opp_val = getattr(item, "8", None)
                    
                    setattr(item, "8", self)
                    

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

    def enterInitialState(self, args: str):
        # TODO: Implement enterInitialState method
        pass

    def on(self, event: str) -> AbstractState:
        # TODO: Implement on method
        pass

    def main(self):
        # TODO: Implement main method
        pass

class model_State(AbstractState):

    def __init__(self):
        
    def onExit(self):
        # TODO: Implement onExit method
        pass

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

class model_Transition:

    def __init__(self, trigger: str, name: str, 4: "model_AbstractState" = None, 13: "model_AbstractState" = None, model_Transition: "model_AbstractState" = None):
        self.trigger = trigger
        self.name = name
        self.4 = 4
        self.13 = 13
        self.model_Transition = model_Transition
        
    @property
    def trigger(self) -> str:
        return self.__trigger

    @trigger.setter
    def trigger(self, trigger: str):
        self.__trigger = trigger

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__13", None)
        self.__13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "14"):
                opp_val = getattr(old_value, "14", None)
                if opp_val == self:
                    setattr(old_value, "14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "14"):
                opp_val = getattr(value, "14", None)
                setattr(value, "14", self)

    @property
    def model_Transition(self):
        return self.__model_Transition

    @model_Transition.setter
    def model_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__model_Transition", None)
        self.__model_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_AbstractState16"):
                opp_val = getattr(old_value, "model_AbstractState16", None)
                if opp_val == self:
                    setattr(old_value, "model_AbstractState16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_AbstractState16"):
                opp_val = getattr(value, "model_AbstractState16", None)
                setattr(value, "model_AbstractState16", self)

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Transition__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                if opp_val is None:
                    setattr(value, "3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def on(self, event: str) -> AbstractState:
        # TODO: Implement on method
        pass

    def accepts(self, event: str):
        # TODO: Implement accepts method
        pass

class model_AbstractState:

    def __init__(self, name: bool, : "model_FiniteStateMachine" = None, 3: set["model_Transition"] = None, 8: "model_FiniteStateMachine" = None, model_AbstractState11: "model_FiniteStateMachine" = None, 14: "model_Transition" = None, model_AbstractState: "model_FiniteStateMachine" = None, model_AbstractState16: "model_Transition" = None):
        self.name = name
        self. = 
        self.3 = 3 if 3 is not None else set()
        self.8 = 8
        self.model_AbstractState11 = model_AbstractState11
        self.14 = 14
        self.model_AbstractState = model_AbstractState
        self.model_AbstractState16 = model_AbstractState16
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__3", None)
        self.__3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    

    @property
    def model_AbstractState11(self):
        return self.__model_AbstractState11

    @model_AbstractState11.setter
    def model_AbstractState11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState11", None)
        self.__model_AbstractState11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FiniteStateMachine10"):
                opp_val = getattr(old_value, "model_FiniteStateMachine10", None)
                if opp_val == self:
                    setattr(old_value, "model_FiniteStateMachine10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FiniteStateMachine10"):
                opp_val = getattr(value, "model_FiniteStateMachine10", None)
                setattr(value, "model_FiniteStateMachine10", self)

    @property
    def 8(self):
        return self.__8

    @8.setter
    def 8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__8", None)
        self.__8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "7"):
                opp_val = getattr(old_value, "7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "7"):
                opp_val = getattr(value, "7", None)
                if opp_val is None:
                    setattr(value, "7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "1"):
                opp_val = getattr(old_value, "1", None)
                if opp_val == self:
                    setattr(old_value, "1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "1"):
                opp_val = getattr(value, "1", None)
                setattr(value, "1", self)

    @property
    def model_AbstractState(self):
        return self.__model_AbstractState

    @model_AbstractState.setter
    def model_AbstractState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState", None)
        self.__model_AbstractState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FiniteStateMachine"):
                opp_val = getattr(old_value, "model_FiniteStateMachine", None)
                if opp_val == self:
                    setattr(old_value, "model_FiniteStateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FiniteStateMachine"):
                opp_val = getattr(value, "model_FiniteStateMachine", None)
                setattr(value, "model_FiniteStateMachine", self)

    @property
    def model_AbstractState16(self):
        return self.__model_AbstractState16

    @model_AbstractState16.setter
    def model_AbstractState16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_AbstractState__model_AbstractState16", None)
        self.__model_AbstractState16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Transition"):
                opp_val = getattr(old_value, "model_Transition", None)
                if opp_val == self:
                    setattr(old_value, "model_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Transition"):
                opp_val = getattr(value, "model_Transition", None)
                setattr(value, "model_Transition", self)

    def onEnter(self):
        # TODO: Implement onEnter method
        pass

    def onExit(self):
        # TODO: Implement onExit method
        pass

    def on(self, event: str) -> str:
        # TODO: Implement on method
        pass
