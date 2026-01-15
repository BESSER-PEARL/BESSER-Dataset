from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Region:

    pass
class trialStatemachine_Statemachine(Region):

    def __init__(self, name: str, trialStatemachine_Statemachine: set["trialStatemachine_Action"] = None):
        self.name = name
        self.trialStatemachine_Statemachine = trialStatemachine_Statemachine if trialStatemachine_Statemachine is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trialStatemachine_Statemachine(self):
        return self.__trialStatemachine_Statemachine

    @trialStatemachine_Statemachine.setter
    def trialStatemachine_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Statemachine__trialStatemachine_Statemachine", None)
        self.__trialStatemachine_Statemachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trialStatemachine_Action"):
                    opp_val = getattr(item, "trialStatemachine_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "trialStatemachine_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trialStatemachine_Action"):
                    opp_val = getattr(item, "trialStatemachine_Action", None)
                    
                    setattr(item, "trialStatemachine_Action", self)
                    

class State:

    pass
class trialStatemachine_ComplexState(State):

    pass
class trialStatemachine_Region:

    def __init__(self, history: str, trialStatemachine_Region7: "trialStatemachine_State" = None, trialStatemachine_Region10: set["trialStatemachine_State"] = None, trialStatemachine_Region: "trialStatemachine_State" = None, trialStatemachine_Region4: "trialStatemachine_ComplexState" = None, trialStatemachine_Region13: "trialStatemachine_State" = None, trialStatemachine_Region16: "trialStatemachine_ComplexState" = None):
        self.history = history
        self.trialStatemachine_Region7 = trialStatemachine_Region7
        self.trialStatemachine_Region10 = trialStatemachine_Region10 if trialStatemachine_Region10 is not None else set()
        self.trialStatemachine_Region = trialStatemachine_Region
        self.trialStatemachine_Region4 = trialStatemachine_Region4
        self.trialStatemachine_Region13 = trialStatemachine_Region13
        self.trialStatemachine_Region16 = trialStatemachine_Region16
        
    @property
    def history(self) -> str:
        return self.__history

    @history.setter
    def history(self, history: str):
        self.__history = history

    @property
    def trialStatemachine_Region(self):
        return self.__trialStatemachine_Region

    @trialStatemachine_Region.setter
    def trialStatemachine_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Region__trialStatemachine_Region", None)
        self.__trialStatemachine_Region = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_State2"):
                opp_val = getattr(old_value, "trialStatemachine_State2", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_State2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_State2"):
                opp_val = getattr(value, "trialStatemachine_State2", None)
                setattr(value, "trialStatemachine_State2", self)

    @property
    def trialStatemachine_Region4(self):
        return self.__trialStatemachine_Region4

    @trialStatemachine_Region4.setter
    def trialStatemachine_Region4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Region__trialStatemachine_Region4", None)
        self.__trialStatemachine_Region4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_ComplexState"):
                opp_val = getattr(old_value, "trialStatemachine_ComplexState", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_ComplexState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_ComplexState"):
                opp_val = getattr(value, "trialStatemachine_ComplexState", None)
                setattr(value, "trialStatemachine_ComplexState", self)

    @property
    def trialStatemachine_Region13(self):
        return self.__trialStatemachine_Region13

    @trialStatemachine_Region13.setter
    def trialStatemachine_Region13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Region__trialStatemachine_Region13", None)
        self.__trialStatemachine_Region13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_State14"):
                opp_val = getattr(old_value, "trialStatemachine_State14", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_State14"):
                opp_val = getattr(value, "trialStatemachine_State14", None)
                setattr(value, "trialStatemachine_State14", self)

    @property
    def trialStatemachine_Region10(self):
        return self.__trialStatemachine_Region10

    @trialStatemachine_Region10.setter
    def trialStatemachine_Region10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Region__trialStatemachine_Region10", None)
        self.__trialStatemachine_Region10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trialStatemachine_State11"):
                    opp_val = getattr(item, "trialStatemachine_State11", None)
                    
                    if opp_val == self:
                        setattr(item, "trialStatemachine_State11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trialStatemachine_State11"):
                    opp_val = getattr(item, "trialStatemachine_State11", None)
                    
                    setattr(item, "trialStatemachine_State11", self)
                    

    @property
    def trialStatemachine_Region16(self):
        return self.__trialStatemachine_Region16

    @trialStatemachine_Region16.setter
    def trialStatemachine_Region16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Region__trialStatemachine_Region16", None)
        self.__trialStatemachine_Region16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_ComplexState17"):
                opp_val = getattr(old_value, "trialStatemachine_ComplexState17", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_ComplexState17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_ComplexState17"):
                opp_val = getattr(value, "trialStatemachine_ComplexState17", None)
                setattr(value, "trialStatemachine_ComplexState17", self)

    @property
    def trialStatemachine_Region7(self):
        return self.__trialStatemachine_Region7

    @trialStatemachine_Region7.setter
    def trialStatemachine_Region7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Region__trialStatemachine_Region7", None)
        self.__trialStatemachine_Region7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_State8"):
                opp_val = getattr(old_value, "trialStatemachine_State8", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_State8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_State8"):
                opp_val = getattr(value, "trialStatemachine_State8", None)
                setattr(value, "trialStatemachine_State8", self)

class trialStatemachine_Action:

    def __init__(self, name: str, trialStatemachine_Action: "trialStatemachine_Statemachine" = None, trialStatemachine_Action23: "trialStatemachine_LabeledTransition" = None):
        self.name = name
        self.trialStatemachine_Action = trialStatemachine_Action
        self.trialStatemachine_Action23 = trialStatemachine_Action23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def trialStatemachine_Action(self):
        return self.__trialStatemachine_Action

    @trialStatemachine_Action.setter
    def trialStatemachine_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Action__trialStatemachine_Action", None)
        self.__trialStatemachine_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_Statemachine"):
                opp_val = getattr(old_value, "trialStatemachine_Statemachine", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_Statemachine"):
                opp_val = getattr(value, "trialStatemachine_Statemachine", None)
                if opp_val is None:
                    setattr(value, "trialStatemachine_Statemachine", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trialStatemachine_Action23(self):
        return self.__trialStatemachine_Action23

    @trialStatemachine_Action23.setter
    def trialStatemachine_Action23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_Action__trialStatemachine_Action23", None)
        self.__trialStatemachine_Action23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_LabeledTransition22"):
                opp_val = getattr(old_value, "trialStatemachine_LabeledTransition22", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_LabeledTransition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_LabeledTransition22"):
                opp_val = getattr(value, "trialStatemachine_LabeledTransition22", None)
                setattr(value, "trialStatemachine_LabeledTransition22", self)

class trialStatemachine_LabeledTransition:

    def __init__(self, id: str, trialStatemachine_LabeledTransition: "trialStatemachine_State" = None, trialStatemachine_LabeledTransition19: "trialStatemachine_State" = None, trialStatemachine_LabeledTransition22: "trialStatemachine_Action" = None):
        self.id = id
        self.trialStatemachine_LabeledTransition = trialStatemachine_LabeledTransition
        self.trialStatemachine_LabeledTransition19 = trialStatemachine_LabeledTransition19
        self.trialStatemachine_LabeledTransition22 = trialStatemachine_LabeledTransition22
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def trialStatemachine_LabeledTransition19(self):
        return self.__trialStatemachine_LabeledTransition19

    @trialStatemachine_LabeledTransition19.setter
    def trialStatemachine_LabeledTransition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_LabeledTransition__trialStatemachine_LabeledTransition19", None)
        self.__trialStatemachine_LabeledTransition19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_State20"):
                opp_val = getattr(old_value, "trialStatemachine_State20", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_State20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_State20"):
                opp_val = getattr(value, "trialStatemachine_State20", None)
                setattr(value, "trialStatemachine_State20", self)

    @property
    def trialStatemachine_LabeledTransition22(self):
        return self.__trialStatemachine_LabeledTransition22

    @trialStatemachine_LabeledTransition22.setter
    def trialStatemachine_LabeledTransition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_LabeledTransition__trialStatemachine_LabeledTransition22", None)
        self.__trialStatemachine_LabeledTransition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_Action23"):
                opp_val = getattr(old_value, "trialStatemachine_Action23", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_Action23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_Action23"):
                opp_val = getattr(value, "trialStatemachine_Action23", None)
                setattr(value, "trialStatemachine_Action23", self)

    @property
    def trialStatemachine_LabeledTransition(self):
        return self.__trialStatemachine_LabeledTransition

    @trialStatemachine_LabeledTransition.setter
    def trialStatemachine_LabeledTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_LabeledTransition__trialStatemachine_LabeledTransition", None)
        self.__trialStatemachine_LabeledTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_State"):
                opp_val = getattr(old_value, "trialStatemachine_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_State"):
                opp_val = getattr(value, "trialStatemachine_State", None)
                if opp_val is None:
                    setattr(value, "trialStatemachine_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trialStatemachine_State:

    def __init__(self, name: str, initialState: str, trialStatemachine_State8: "trialStatemachine_Region" = None, trialStatemachine_State11: "trialStatemachine_Region" = None, trialStatemachine_State: set["trialStatemachine_LabeledTransition"] = None, trialStatemachine_State2: "trialStatemachine_Region" = None, trialStatemachine_State14: "trialStatemachine_Region" = None, trialStatemachine_State20: "trialStatemachine_LabeledTransition" = None):
        self.name = name
        self.initialState = initialState
        self.trialStatemachine_State8 = trialStatemachine_State8
        self.trialStatemachine_State11 = trialStatemachine_State11
        self.trialStatemachine_State = trialStatemachine_State if trialStatemachine_State is not None else set()
        self.trialStatemachine_State2 = trialStatemachine_State2
        self.trialStatemachine_State14 = trialStatemachine_State14
        self.trialStatemachine_State20 = trialStatemachine_State20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initialState(self) -> str:
        return self.__initialState

    @initialState.setter
    def initialState(self, initialState: str):
        self.__initialState = initialState

    @property
    def trialStatemachine_State(self):
        return self.__trialStatemachine_State

    @trialStatemachine_State.setter
    def trialStatemachine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_State__trialStatemachine_State", None)
        self.__trialStatemachine_State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trialStatemachine_LabeledTransition"):
                    opp_val = getattr(item, "trialStatemachine_LabeledTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "trialStatemachine_LabeledTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trialStatemachine_LabeledTransition"):
                    opp_val = getattr(item, "trialStatemachine_LabeledTransition", None)
                    
                    setattr(item, "trialStatemachine_LabeledTransition", self)
                    

    @property
    def trialStatemachine_State2(self):
        return self.__trialStatemachine_State2

    @trialStatemachine_State2.setter
    def trialStatemachine_State2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_State__trialStatemachine_State2", None)
        self.__trialStatemachine_State2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_Region"):
                opp_val = getattr(old_value, "trialStatemachine_Region", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_Region", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_Region"):
                opp_val = getattr(value, "trialStatemachine_Region", None)
                setattr(value, "trialStatemachine_Region", self)

    @property
    def trialStatemachine_State8(self):
        return self.__trialStatemachine_State8

    @trialStatemachine_State8.setter
    def trialStatemachine_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_State__trialStatemachine_State8", None)
        self.__trialStatemachine_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_Region7"):
                opp_val = getattr(old_value, "trialStatemachine_Region7", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_Region7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_Region7"):
                opp_val = getattr(value, "trialStatemachine_Region7", None)
                setattr(value, "trialStatemachine_Region7", self)

    @property
    def trialStatemachine_State14(self):
        return self.__trialStatemachine_State14

    @trialStatemachine_State14.setter
    def trialStatemachine_State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_State__trialStatemachine_State14", None)
        self.__trialStatemachine_State14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_Region13"):
                opp_val = getattr(old_value, "trialStatemachine_Region13", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_Region13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_Region13"):
                opp_val = getattr(value, "trialStatemachine_Region13", None)
                setattr(value, "trialStatemachine_Region13", self)

    @property
    def trialStatemachine_State20(self):
        return self.__trialStatemachine_State20

    @trialStatemachine_State20.setter
    def trialStatemachine_State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_State__trialStatemachine_State20", None)
        self.__trialStatemachine_State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_LabeledTransition19"):
                opp_val = getattr(old_value, "trialStatemachine_LabeledTransition19", None)
                if opp_val == self:
                    setattr(old_value, "trialStatemachine_LabeledTransition19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_LabeledTransition19"):
                opp_val = getattr(value, "trialStatemachine_LabeledTransition19", None)
                setattr(value, "trialStatemachine_LabeledTransition19", self)

    @property
    def trialStatemachine_State11(self):
        return self.__trialStatemachine_State11

    @trialStatemachine_State11.setter
    def trialStatemachine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trialStatemachine_State__trialStatemachine_State11", None)
        self.__trialStatemachine_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trialStatemachine_Region10"):
                opp_val = getattr(old_value, "trialStatemachine_Region10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trialStatemachine_Region10"):
                opp_val = getattr(value, "trialStatemachine_Region10", None)
                if opp_val is None:
                    setattr(value, "trialStatemachine_Region10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
