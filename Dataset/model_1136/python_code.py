from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ExtensionElement:

    pass
class ea_extensions_StringExtension(ExtensionElement):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ea_extensions_IntegerExtension(ExtensionElement):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class IExtendible:

    pass
class ea_extensions_ExtendibleElement(IExtendible):

    pass
class ea_extensions_IExtension(ABC):

    def __init__(self, id: str, IExtendible: "IExtendible" = None):
        self.id = id
        self.IExtendible = IExtendible
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def IExtendible(self):
        return self.__IExtendible

    @IExtendible.setter
    def IExtendible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_extensions_IExtension__IExtendible", None)
        self.__IExtendible = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensions27"):
                opp_val = getattr(old_value, "extensions27", None)
                if opp_val == self:
                    setattr(old_value, "extensions27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensions27"):
                opp_val = getattr(value, "extensions27", None)
                setattr(value, "extensions27", self)

class ea_extensions_BooleanExtension(ExtensionElement):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class ea_extensions_StringListExtension(ExtensionElement):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class IExtension:

    pass
class ea_extensions_ExtensionElement(IExtension):

    pass
class ea_extensions_IExtendible(ABC):

    def __init__(self, IExtension: set["IExtension"] = None):
        self.IExtension = IExtension if IExtension is not None else set()
        
    @property
    def IExtension(self):
        return self.__IExtension

    @IExtension.setter
    def IExtension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_extensions_IExtendible__IExtension", None)
        self.__IExtension = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extensions"):
                    opp_val = getattr(item, "extensions", None)
                    
                    if opp_val == self:
                        setattr(item, "extensions", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extensions"):
                    opp_val = getattr(item, "extensions", None)
                    
                    setattr(item, "extensions", self)
                    

    def findExtension(self, id: str) -> str:
        # TODO: Implement findExtension method
        pass

    def updateExtension(self, extension: str):
        # TODO: Implement updateExtension method
        pass

class ea_automata_Module:

    pass
class Transition:

    pass
class State:

    pass
class ExtendibleElement:

    pass
class ea_automata_Transition(ExtendibleElement):

    def __init__(self, id: str, Automaton14: "Automaton" = None, State17: "State" = None, State20: "State" = None):
        self.id = id
        self.Automaton14 = Automaton14
        self.State17 = State17
        self.State20 = State20
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def State20(self):
        return self.__State20

    @State20.setter
    def State20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Transition__State20", None)
        self.__State20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata21"):
                opp_val = getattr(old_value, "automata21", None)
                if opp_val == self:
                    setattr(old_value, "automata21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata21"):
                opp_val = getattr(value, "automata21", None)
                setattr(value, "automata21", self)

    @property
    def State17(self):
        return self.__State17

    @State17.setter
    def State17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Transition__State17", None)
        self.__State17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata18"):
                opp_val = getattr(old_value, "automata18", None)
                if opp_val == self:
                    setattr(old_value, "automata18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata18"):
                opp_val = getattr(value, "automata18", None)
                setattr(value, "automata18", self)

    @property
    def Automaton14(self):
        return self.__Automaton14

    @Automaton14.setter
    def Automaton14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Transition__Automaton14", None)
        self.__Automaton14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata15"):
                opp_val = getattr(old_value, "automata15", None)
                if opp_val == self:
                    setattr(old_value, "automata15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata15"):
                opp_val = getattr(value, "automata15", None)
                setattr(value, "automata15", self)

class ea_automata_Automaton(ExtendibleElement):

    def __init__(self, id: str, name: str, usedExtensionIds: str, Module: "Module" = None, State: set["State"] = None, Transition: set["Transition"] = None):
        self.id = id
        self.name = name
        self.usedExtensionIds = usedExtensionIds
        self.Module = Module
        self.State = State if State is not None else set()
        self.Transition = Transition if Transition is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def usedExtensionIds(self) -> str:
        return self.__usedExtensionIds

    @usedExtensionIds.setter
    def usedExtensionIds(self, usedExtensionIds: str):
        self.__usedExtensionIds = usedExtensionIds

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Automaton__State", None)
        self.__State = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automata"):
                    opp_val = getattr(item, "automata", None)
                    
                    if opp_val == self:
                        setattr(item, "automata", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automata"):
                    opp_val = getattr(item, "automata", None)
                    
                    setattr(item, "automata", self)
                    

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Automaton__Transition", None)
        self.__Transition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automata2"):
                    opp_val = getattr(item, "automata2", None)
                    
                    if opp_val == self:
                        setattr(item, "automata2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automata2"):
                    opp_val = getattr(item, "automata2", None)
                    
                    setattr(item, "automata2", self)
                    

    @property
    def Module(self):
        return self.__Module

    @Module.setter
    def Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Automaton__Module", None)
        self.__Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata4"):
                opp_val = getattr(old_value, "automata4", None)
                if opp_val == self:
                    setattr(old_value, "automata4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata4"):
                opp_val = getattr(value, "automata4", None)
                setattr(value, "automata4", self)

class Automaton:

    pass
class ea_automata_State(ExtendibleElement):

    def __init__(self, id: str, name: str, Automaton: "Automaton" = None, Transition8: set["Transition"] = None, Transition11: set["Transition"] = None):
        self.id = id
        self.name = name
        self.Automaton = Automaton
        self.Transition8 = Transition8 if Transition8 is not None else set()
        self.Transition11 = Transition11 if Transition11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Transition8(self):
        return self.__Transition8

    @Transition8.setter
    def Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_State__Transition8", None)
        self.__Transition8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automata9"):
                    opp_val = getattr(item, "automata9", None)
                    
                    if opp_val == self:
                        setattr(item, "automata9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automata9"):
                    opp_val = getattr(item, "automata9", None)
                    
                    setattr(item, "automata9", self)
                    

    @property
    def Transition11(self):
        return self.__Transition11

    @Transition11.setter
    def Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_State__Transition11", None)
        self.__Transition11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automata12"):
                    opp_val = getattr(item, "automata12", None)
                    
                    if opp_val == self:
                        setattr(item, "automata12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automata12"):
                    opp_val = getattr(item, "automata12", None)
                    
                    setattr(item, "automata12", self)
                    

    @property
    def Automaton(self):
        return self.__Automaton

    @Automaton.setter
    def Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_State__Automaton", None)
        self.__Automaton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automata6"):
                opp_val = getattr(old_value, "automata6", None)
                if opp_val == self:
                    setattr(old_value, "automata6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automata6"):
                opp_val = getattr(value, "automata6", None)
                setattr(value, "automata6", self)

class Module:

    pass