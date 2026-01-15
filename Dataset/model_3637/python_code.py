from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AcceptanceKind(Enum):
    Finite = "Finite"
    Infinite = "Infinite"
    Probabilistic = "Probabilistic"


############################################
# Definition of Classes
############################################

class State:

    pass
class autopl_HierarchicalState(State):

    pass
class autopl_Transition:

    def __init__(self, probability: str, autopl_Transition17: "autopl_Symbol" = None, autopl_Transition: "autopl_Automaton" = None, autopl_Transition29: "autopl_State" = None, autopl_Transition32: "autopl_State" = None, autopl_Transition20: "autopl_Symbol" = None, autopl_Transition23: "autopl_Symbol" = None, autopl_Transition26: set["autopl_Symbol"] = None, autopl_Transition38: "autopl_HierarchicalState" = None):
        self.probability = probability
        self.autopl_Transition17 = autopl_Transition17
        self.autopl_Transition = autopl_Transition
        self.autopl_Transition29 = autopl_Transition29
        self.autopl_Transition32 = autopl_Transition32
        self.autopl_Transition20 = autopl_Transition20
        self.autopl_Transition23 = autopl_Transition23
        self.autopl_Transition26 = autopl_Transition26 if autopl_Transition26 is not None else set()
        self.autopl_Transition38 = autopl_Transition38
        
    @property
    def probability(self) -> str:
        return self.__probability

    @probability.setter
    def probability(self, probability: str):
        self.__probability = probability

    @property
    def autopl_Transition38(self):
        return self.__autopl_Transition38

    @autopl_Transition38.setter
    def autopl_Transition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition38", None)
        self.__autopl_Transition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_HierarchicalState37"):
                opp_val = getattr(old_value, "autopl_HierarchicalState37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_HierarchicalState37"):
                opp_val = getattr(value, "autopl_HierarchicalState37", None)
                if opp_val is None:
                    setattr(value, "autopl_HierarchicalState37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def autopl_Transition26(self):
        return self.__autopl_Transition26

    @autopl_Transition26.setter
    def autopl_Transition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition26", None)
        self.__autopl_Transition26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "autopl_Symbol27"):
                    opp_val = getattr(item, "autopl_Symbol27", None)
                    
                    if opp_val == self:
                        setattr(item, "autopl_Symbol27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "autopl_Symbol27"):
                    opp_val = getattr(item, "autopl_Symbol27", None)
                    
                    setattr(item, "autopl_Symbol27", self)
                    

    @property
    def autopl_Transition32(self):
        return self.__autopl_Transition32

    @autopl_Transition32.setter
    def autopl_Transition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition32", None)
        self.__autopl_Transition32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_State33"):
                opp_val = getattr(old_value, "autopl_State33", None)
                if opp_val == self:
                    setattr(old_value, "autopl_State33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_State33"):
                opp_val = getattr(value, "autopl_State33", None)
                setattr(value, "autopl_State33", self)

    @property
    def autopl_Transition29(self):
        return self.__autopl_Transition29

    @autopl_Transition29.setter
    def autopl_Transition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition29", None)
        self.__autopl_Transition29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_State30"):
                opp_val = getattr(old_value, "autopl_State30", None)
                if opp_val == self:
                    setattr(old_value, "autopl_State30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_State30"):
                opp_val = getattr(value, "autopl_State30", None)
                setattr(value, "autopl_State30", self)

    @property
    def autopl_Transition17(self):
        return self.__autopl_Transition17

    @autopl_Transition17.setter
    def autopl_Transition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition17", None)
        self.__autopl_Transition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Symbol18"):
                opp_val = getattr(old_value, "autopl_Symbol18", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Symbol18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Symbol18"):
                opp_val = getattr(value, "autopl_Symbol18", None)
                setattr(value, "autopl_Symbol18", self)

    @property
    def autopl_Transition23(self):
        return self.__autopl_Transition23

    @autopl_Transition23.setter
    def autopl_Transition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition23", None)
        self.__autopl_Transition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Symbol24"):
                opp_val = getattr(old_value, "autopl_Symbol24", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Symbol24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Symbol24"):
                opp_val = getattr(value, "autopl_Symbol24", None)
                setattr(value, "autopl_Symbol24", self)

    @property
    def autopl_Transition20(self):
        return self.__autopl_Transition20

    @autopl_Transition20.setter
    def autopl_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition20", None)
        self.__autopl_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Symbol21"):
                opp_val = getattr(old_value, "autopl_Symbol21", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Symbol21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Symbol21"):
                opp_val = getattr(value, "autopl_Symbol21", None)
                setattr(value, "autopl_Symbol21", self)

    @property
    def autopl_Transition(self):
        return self.__autopl_Transition

    @autopl_Transition.setter
    def autopl_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Transition__autopl_Transition", None)
        self.__autopl_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Automaton12"):
                opp_val = getattr(old_value, "autopl_Automaton12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Automaton12"):
                opp_val = getattr(value, "autopl_Automaton12", None)
                if opp_val is None:
                    setattr(value, "autopl_Automaton12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class autopl_State:

    def __init__(self, name: str, isInitial: str, isFinal: str, autopl_State: "autopl_Automaton" = None, autopl_State30: "autopl_Transition" = None, autopl_State33: "autopl_Transition" = None, autopl_State35: "autopl_HierarchicalState" = None):
        self.name = name
        self.isInitial = isInitial
        self.isFinal = isFinal
        self.autopl_State = autopl_State
        self.autopl_State30 = autopl_State30
        self.autopl_State33 = autopl_State33
        self.autopl_State35 = autopl_State35
        
    @property
    def isFinal(self) -> str:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: str):
        self.__isFinal = isFinal

    @property
    def isInitial(self) -> str:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: str):
        self.__isInitial = isInitial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def autopl_State33(self):
        return self.__autopl_State33

    @autopl_State33.setter
    def autopl_State33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_State__autopl_State33", None)
        self.__autopl_State33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Transition32"):
                opp_val = getattr(old_value, "autopl_Transition32", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Transition32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Transition32"):
                opp_val = getattr(value, "autopl_Transition32", None)
                setattr(value, "autopl_Transition32", self)

    @property
    def autopl_State30(self):
        return self.__autopl_State30

    @autopl_State30.setter
    def autopl_State30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_State__autopl_State30", None)
        self.__autopl_State30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Transition29"):
                opp_val = getattr(old_value, "autopl_Transition29", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Transition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Transition29"):
                opp_val = getattr(value, "autopl_Transition29", None)
                setattr(value, "autopl_Transition29", self)

    @property
    def autopl_State35(self):
        return self.__autopl_State35

    @autopl_State35.setter
    def autopl_State35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_State__autopl_State35", None)
        self.__autopl_State35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_HierarchicalState"):
                opp_val = getattr(old_value, "autopl_HierarchicalState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_HierarchicalState"):
                opp_val = getattr(value, "autopl_HierarchicalState", None)
                if opp_val is None:
                    setattr(value, "autopl_HierarchicalState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def autopl_State(self):
        return self.__autopl_State

    @autopl_State.setter
    def autopl_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_State__autopl_State", None)
        self.__autopl_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Automaton10"):
                opp_val = getattr(old_value, "autopl_Automaton10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Automaton10"):
                opp_val = getattr(value, "autopl_Automaton10", None)
                if opp_val is None:
                    setattr(value, "autopl_Automaton10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def outTrans(self) -> str:
        # TODO: Implement outTrans method
        pass

    def inTrans(self) -> str:
        # TODO: Implement inTrans method
        pass

    def adjacent(self) -> str:
        # TODO: Implement adjacent method
        pass

class autopl_Alphabet:

    pass
class autopl_Automaton:

    def __init__(self, autopl_Automaton8: "autopl_Symbol" = None, autopl_Automaton: "autopl_Alphabet" = None, autopl_Automaton2: "autopl_Alphabet" = None, autopl_Automaton5: "autopl_Alphabet" = None, autopl_Automaton10: set["autopl_State"] = None, autopl_Automaton12: set["autopl_Transition"] = None):
        self.autopl_Automaton8 = autopl_Automaton8
        self.autopl_Automaton = autopl_Automaton
        self.autopl_Automaton2 = autopl_Automaton2
        self.autopl_Automaton5 = autopl_Automaton5
        self.autopl_Automaton10 = autopl_Automaton10 if autopl_Automaton10 is not None else set()
        self.autopl_Automaton12 = autopl_Automaton12 if autopl_Automaton12 is not None else set()
        
    @property
    def autopl_Automaton10(self):
        return self.__autopl_Automaton10

    @autopl_Automaton10.setter
    def autopl_Automaton10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Automaton__autopl_Automaton10", None)
        self.__autopl_Automaton10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "autopl_State"):
                    opp_val = getattr(item, "autopl_State", None)
                    
                    if opp_val == self:
                        setattr(item, "autopl_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "autopl_State"):
                    opp_val = getattr(item, "autopl_State", None)
                    
                    setattr(item, "autopl_State", self)
                    

    @property
    def autopl_Automaton12(self):
        return self.__autopl_Automaton12

    @autopl_Automaton12.setter
    def autopl_Automaton12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Automaton__autopl_Automaton12", None)
        self.__autopl_Automaton12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "autopl_Transition"):
                    opp_val = getattr(item, "autopl_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "autopl_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "autopl_Transition"):
                    opp_val = getattr(item, "autopl_Transition", None)
                    
                    setattr(item, "autopl_Transition", self)
                    

    @property
    def autopl_Automaton(self):
        return self.__autopl_Automaton

    @autopl_Automaton.setter
    def autopl_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Automaton__autopl_Automaton", None)
        self.__autopl_Automaton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Alphabet"):
                opp_val = getattr(old_value, "autopl_Alphabet", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Alphabet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Alphabet"):
                opp_val = getattr(value, "autopl_Alphabet", None)
                setattr(value, "autopl_Alphabet", self)

    @property
    def autopl_Automaton2(self):
        return self.__autopl_Automaton2

    @autopl_Automaton2.setter
    def autopl_Automaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Automaton__autopl_Automaton2", None)
        self.__autopl_Automaton2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Alphabet3"):
                opp_val = getattr(old_value, "autopl_Alphabet3", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Alphabet3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Alphabet3"):
                opp_val = getattr(value, "autopl_Alphabet3", None)
                setattr(value, "autopl_Alphabet3", self)

    @property
    def autopl_Automaton5(self):
        return self.__autopl_Automaton5

    @autopl_Automaton5.setter
    def autopl_Automaton5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Automaton__autopl_Automaton5", None)
        self.__autopl_Automaton5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Alphabet6"):
                opp_val = getattr(old_value, "autopl_Alphabet6", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Alphabet6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Alphabet6"):
                opp_val = getattr(value, "autopl_Alphabet6", None)
                setattr(value, "autopl_Alphabet6", self)

    @property
    def autopl_Automaton8(self):
        return self.__autopl_Automaton8

    @autopl_Automaton8.setter
    def autopl_Automaton8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Automaton__autopl_Automaton8", None)
        self.__autopl_Automaton8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Symbol"):
                opp_val = getattr(old_value, "autopl_Symbol", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Symbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Symbol"):
                opp_val = getattr(value, "autopl_Symbol", None)
                setattr(value, "autopl_Symbol", self)

    def acceptanceCondition(self) -> str:
        # TODO: Implement acceptanceCondition method
        pass

class autopl_Symbol:

    def __init__(self, name: str, autopl_Symbol: "autopl_Automaton" = None, autopl_Symbol18: "autopl_Transition" = None, autopl_Symbol15: "autopl_Alphabet" = None, autopl_Symbol21: "autopl_Transition" = None, autopl_Symbol24: "autopl_Transition" = None, autopl_Symbol27: "autopl_Transition" = None):
        self.name = name
        self.autopl_Symbol = autopl_Symbol
        self.autopl_Symbol18 = autopl_Symbol18
        self.autopl_Symbol15 = autopl_Symbol15
        self.autopl_Symbol21 = autopl_Symbol21
        self.autopl_Symbol24 = autopl_Symbol24
        self.autopl_Symbol27 = autopl_Symbol27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def autopl_Symbol21(self):
        return self.__autopl_Symbol21

    @autopl_Symbol21.setter
    def autopl_Symbol21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Symbol__autopl_Symbol21", None)
        self.__autopl_Symbol21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Transition20"):
                opp_val = getattr(old_value, "autopl_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Transition20"):
                opp_val = getattr(value, "autopl_Transition20", None)
                setattr(value, "autopl_Transition20", self)

    @property
    def autopl_Symbol15(self):
        return self.__autopl_Symbol15

    @autopl_Symbol15.setter
    def autopl_Symbol15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Symbol__autopl_Symbol15", None)
        self.__autopl_Symbol15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Alphabet14"):
                opp_val = getattr(old_value, "autopl_Alphabet14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Alphabet14"):
                opp_val = getattr(value, "autopl_Alphabet14", None)
                if opp_val is None:
                    setattr(value, "autopl_Alphabet14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def autopl_Symbol18(self):
        return self.__autopl_Symbol18

    @autopl_Symbol18.setter
    def autopl_Symbol18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Symbol__autopl_Symbol18", None)
        self.__autopl_Symbol18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Transition17"):
                opp_val = getattr(old_value, "autopl_Transition17", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Transition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Transition17"):
                opp_val = getattr(value, "autopl_Transition17", None)
                setattr(value, "autopl_Transition17", self)

    @property
    def autopl_Symbol24(self):
        return self.__autopl_Symbol24

    @autopl_Symbol24.setter
    def autopl_Symbol24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Symbol__autopl_Symbol24", None)
        self.__autopl_Symbol24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Transition23"):
                opp_val = getattr(old_value, "autopl_Transition23", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Transition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Transition23"):
                opp_val = getattr(value, "autopl_Transition23", None)
                setattr(value, "autopl_Transition23", self)

    @property
    def autopl_Symbol(self):
        return self.__autopl_Symbol

    @autopl_Symbol.setter
    def autopl_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Symbol__autopl_Symbol", None)
        self.__autopl_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Automaton8"):
                opp_val = getattr(old_value, "autopl_Automaton8", None)
                if opp_val == self:
                    setattr(old_value, "autopl_Automaton8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Automaton8"):
                opp_val = getattr(value, "autopl_Automaton8", None)
                setattr(value, "autopl_Automaton8", self)

    @property
    def autopl_Symbol27(self):
        return self.__autopl_Symbol27

    @autopl_Symbol27.setter
    def autopl_Symbol27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_autopl_Symbol__autopl_Symbol27", None)
        self.__autopl_Symbol27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autopl_Transition26"):
                opp_val = getattr(old_value, "autopl_Transition26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autopl_Transition26"):
                opp_val = getattr(value, "autopl_Transition26", None)
                if opp_val is None:
                    setattr(value, "autopl_Transition26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
