from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class State:

    pass
class DFAAutomaton_CompositeState(State):

    pass
class DFAAutomaton_AlphabetSymbol:

    def __init__(self, symbol: str, DFAAutomaton_AlphabetSymbol: "DFAAutomaton_Automaton" = None, DFAAutomaton_AlphabetSymbol12: "DFAAutomaton_Transition" = None):
        self.symbol = symbol
        self.DFAAutomaton_AlphabetSymbol = DFAAutomaton_AlphabetSymbol
        self.DFAAutomaton_AlphabetSymbol12 = DFAAutomaton_AlphabetSymbol12
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def DFAAutomaton_AlphabetSymbol12(self):
        return self.__DFAAutomaton_AlphabetSymbol12

    @DFAAutomaton_AlphabetSymbol12.setter
    def DFAAutomaton_AlphabetSymbol12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_AlphabetSymbol__DFAAutomaton_AlphabetSymbol12", None)
        self.__DFAAutomaton_AlphabetSymbol12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFAAutomaton_Transition11"):
                opp_val = getattr(old_value, "DFAAutomaton_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "DFAAutomaton_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFAAutomaton_Transition11"):
                opp_val = getattr(value, "DFAAutomaton_Transition11", None)
                setattr(value, "DFAAutomaton_Transition11", self)

    @property
    def DFAAutomaton_AlphabetSymbol(self):
        return self.__DFAAutomaton_AlphabetSymbol

    @DFAAutomaton_AlphabetSymbol.setter
    def DFAAutomaton_AlphabetSymbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_AlphabetSymbol__DFAAutomaton_AlphabetSymbol", None)
        self.__DFAAutomaton_AlphabetSymbol = value
        
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
class DFAAutomaton_State:

    def __init__(self, name: str, isInitial: bool, isFinal: bool, DFAAutomaton_State: "DFAAutomaton_Automaton" = None, to: set["DFAAutomaton_Transition"] = None, DFAAutomaton_State8: "DFAAutomaton_Transition" = None, State: "DFAAutomaton_Transition" = None):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.DFAAutomaton_State = DFAAutomaton_State
        self.to = to if to is not None else set()
        self.DFAAutomaton_State8 = DFAAutomaton_State8
        self.State = State
        
    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_State__to", None)
        self.__to = value if value is not None else set()
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_State__State", None)
        self.__State = value
        
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
    def DFAAutomaton_State8(self):
        return self.__DFAAutomaton_State8

    @DFAAutomaton_State8.setter
    def DFAAutomaton_State8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DFAAutomaton_State__DFAAutomaton_State8", None)
        self.__DFAAutomaton_State8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFAAutomaton_Transition7"):
                opp_val = getattr(old_value, "DFAAutomaton_Transition7", None)
                if opp_val == self:
                    setattr(old_value, "DFAAutomaton_Transition7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFAAutomaton_Transition7"):
                opp_val = getattr(value, "DFAAutomaton_Transition7", None)
                setattr(value, "DFAAutomaton_Transition7", self)

class DFAAutomaton_Automaton:

    def __init__(self, name: str, DFAAutomaton_Automaton: set["DFAAutomaton_State"] = None, DFAAutomaton_Automaton2: set["DFAAutomaton_Transition"] = None, DFAAutomaton_Automaton4: set["DFAAutomaton_AlphabetSymbol"] = None):
        self.name = name
        self.DFAAutomaton_Automaton = DFAAutomaton_Automaton if DFAAutomaton_Automaton is not None else set()
        self.DFAAutomaton_Automaton2 = DFAAutomaton_Automaton2 if DFAAutomaton_Automaton2 is not None else set()
        self.DFAAutomaton_Automaton4 = DFAAutomaton_Automaton4 if DFAAutomaton_Automaton4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "DFAAutomaton_AlphabetSymbol"):
                    opp_val = getattr(item, "DFAAutomaton_AlphabetSymbol", None)
                    
                    if opp_val == self:
                        setattr(item, "DFAAutomaton_AlphabetSymbol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DFAAutomaton_AlphabetSymbol"):
                    opp_val = getattr(item, "DFAAutomaton_AlphabetSymbol", None)
                    
                    setattr(item, "DFAAutomaton_AlphabetSymbol", self)
                    

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
                    
