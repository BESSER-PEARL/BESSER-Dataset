from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DFAAutomaton_State:

    def __init__(self, name: str, isInitial: bool, isFinal: bool, DFAAutomaton_State: "DFAAutomaton_Automaton" = None, DFAAutomaton_State7: "DFAAutomaton_Transition" = None, DFAAutomaton_State10: "DFAAutomaton_Transition" = None):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.DFAAutomaton_State = DFAAutomaton_State
        self.DFAAutomaton_State7 = DFAAutomaton_State7
        self.DFAAutomaton_State10 = DFAAutomaton_State10
        
    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DFAAutomaton_State10(self):
        return self.__DFAAutomaton_State10

    @DFAAutomaton_State10.setter
    def DFAAutomaton_State10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_State__DFAAutomaton_State10", None)
        self.__DFAAutomaton_State10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFAAutomaton_Transition9"):
                opp_val = getattr(old_value, "DFAAutomaton_Transition9", None)
                if opp_val == self:
                    setattr(old_value, "DFAAutomaton_Transition9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFAAutomaton_Transition9"):
                opp_val = getattr(value, "DFAAutomaton_Transition9", None)
                setattr(value, "DFAAutomaton_Transition9", self)

    @property
    def DFAAutomaton_State7(self):
        return self.__DFAAutomaton_State7

    @DFAAutomaton_State7.setter
    def DFAAutomaton_State7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_State__DFAAutomaton_State7", None)
        self.__DFAAutomaton_State7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFAAutomaton_Transition6"):
                opp_val = getattr(old_value, "DFAAutomaton_Transition6", None)
                if opp_val == self:
                    setattr(old_value, "DFAAutomaton_Transition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFAAutomaton_Transition6"):
                opp_val = getattr(value, "DFAAutomaton_Transition6", None)
                setattr(value, "DFAAutomaton_Transition6", self)

    @property
    def DFAAutomaton_State(self):
        return self.__DFAAutomaton_State

    @DFAAutomaton_State.setter
    def DFAAutomaton_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_State__DFAAutomaton_State", None)
        self.__DFAAutomaton_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFAAutomaton_Automaton"):
                opp_val = getattr(old_value, "DFAAutomaton_Automaton", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFAAutomaton_Automaton"):
                opp_val = getattr(value, "DFAAutomaton_Automaton", None)
                if opp_val is None:
                    setattr(value, "DFAAutomaton_Automaton", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DFAAutomaton_Automaton:

    def __init__(self, name: str, DFAAutomaton_Automaton2: set["DFAAutomaton_Transition"] = None, DFAAutomaton_Automaton4: set["DFAAutomaton_Symbol"] = None, DFAAutomaton_Automaton: set["DFAAutomaton_State"] = None):
        self.name = name
        self.DFAAutomaton_Automaton2 = DFAAutomaton_Automaton2 if DFAAutomaton_Automaton2 is not None else set()
        self.DFAAutomaton_Automaton4 = DFAAutomaton_Automaton4 if DFAAutomaton_Automaton4 is not None else set()
        self.DFAAutomaton_Automaton = DFAAutomaton_Automaton if DFAAutomaton_Automaton is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def DFAAutomaton_Automaton(self):
        return self.__DFAAutomaton_Automaton

    @DFAAutomaton_Automaton.setter
    def DFAAutomaton_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_Automaton__DFAAutomaton_Automaton", None)
        self.__DFAAutomaton_Automaton = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DFAAutomaton_State"):
                    opp_val = getattr(item, "DFAAutomaton_State", None)
                    
                    if opp_val == self:
                        setattr(item, "DFAAutomaton_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DFAAutomaton_State"):
                    opp_val = getattr(item, "DFAAutomaton_State", None)
                    
                    setattr(item, "DFAAutomaton_State", self)
                    

    @property
    def DFAAutomaton_Automaton4(self):
        return self.__DFAAutomaton_Automaton4

    @DFAAutomaton_Automaton4.setter
    def DFAAutomaton_Automaton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_Automaton__DFAAutomaton_Automaton4", None)
        self.__DFAAutomaton_Automaton4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DFAAutomaton_Symbol"):
                    opp_val = getattr(item, "DFAAutomaton_Symbol", None)
                    
                    if opp_val == self:
                        setattr(item, "DFAAutomaton_Symbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DFAAutomaton_Symbol"):
                    opp_val = getattr(item, "DFAAutomaton_Symbol", None)
                    
                    setattr(item, "DFAAutomaton_Symbol", self)
                    

    @property
    def DFAAutomaton_Automaton2(self):
        return self.__DFAAutomaton_Automaton2

    @DFAAutomaton_Automaton2.setter
    def DFAAutomaton_Automaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_Automaton__DFAAutomaton_Automaton2", None)
        self.__DFAAutomaton_Automaton2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DFAAutomaton_Transition"):
                    opp_val = getattr(item, "DFAAutomaton_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "DFAAutomaton_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DFAAutomaton_Transition"):
                    opp_val = getattr(item, "DFAAutomaton_Transition", None)
                    
                    setattr(item, "DFAAutomaton_Transition", self)
                    

class DFAAutomaton_Symbol:

    def __init__(self, symbol: str, DFAAutomaton_Symbol: "DFAAutomaton_Automaton" = None, DFAAutomaton_Symbol13: "DFAAutomaton_Transition" = None):
        self.symbol = symbol
        self.DFAAutomaton_Symbol = DFAAutomaton_Symbol
        self.DFAAutomaton_Symbol13 = DFAAutomaton_Symbol13
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def DFAAutomaton_Symbol13(self):
        return self.__DFAAutomaton_Symbol13

    @DFAAutomaton_Symbol13.setter
    def DFAAutomaton_Symbol13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_Symbol__DFAAutomaton_Symbol13", None)
        self.__DFAAutomaton_Symbol13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFAAutomaton_Transition12"):
                opp_val = getattr(old_value, "DFAAutomaton_Transition12", None)
                if opp_val == self:
                    setattr(old_value, "DFAAutomaton_Transition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFAAutomaton_Transition12"):
                opp_val = getattr(value, "DFAAutomaton_Transition12", None)
                setattr(value, "DFAAutomaton_Transition12", self)

    @property
    def DFAAutomaton_Symbol(self):
        return self.__DFAAutomaton_Symbol

    @DFAAutomaton_Symbol.setter
    def DFAAutomaton_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_Symbol__DFAAutomaton_Symbol", None)
        self.__DFAAutomaton_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFAAutomaton_Automaton4"):
                opp_val = getattr(old_value, "DFAAutomaton_Automaton4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFAAutomaton_Automaton4"):
                opp_val = getattr(value, "DFAAutomaton_Automaton4", None)
                if opp_val is None:
                    setattr(value, "DFAAutomaton_Automaton4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DFAAutomaton_Transition:

    pass