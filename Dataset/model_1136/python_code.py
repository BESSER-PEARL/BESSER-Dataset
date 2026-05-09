from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IExtendible:

    pass
class ea_extensions_ExtendibleElement(IExtendible):

    pass
class ea_extensions_IExtension(ABC):

    def __init__(self, id: str, extensions: "IExtendible" = None):
        self.id = id
        self.extensions = extensions
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def extensions(self):
        return self.__extensions

    @extensions.setter
    def extensions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_extensions_IExtension__extensions", None)
        self.__extensions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IExtendible"):
                opp_val = getattr(old_value, "IExtendible", None)
                if opp_val == self:
                    setattr(old_value, "IExtendible", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IExtendible"):
                opp_val = getattr(value, "IExtendible", None)
                setattr(value, "IExtendible", self)

class IExtension:

    pass
class ExtensionElement:

    pass
class ea_extensions_StringExtension(ExtensionElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class ea_extensions_BooleanExtension(ExtensionElement):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class ea_extensions_StringListExtension(ExtensionElement):

    def __init__(self, values: str):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class ea_extensions_IntegerExtension(ExtensionElement):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class ea_extensions_ExtensionElement(IExtension):

    pass
class State:

    pass
class ExtendibleElement:

    pass
class ea_automata_Automaton(ExtendibleElement):

    def __init__(self, name: str, usedExtensionIds: str, id: str, automaton: set["State"] = None, automaton2: set["Transition"] = None, automata: "Module" = None):
        self.name = name
        self.usedExtensionIds = usedExtensionIds
        self.id = id
        self.automaton = automaton if automaton is not None else set()
        self.automaton2 = automaton2 if automaton2 is not None else set()
        self.automata = automata
        
        pass
    @property
    def usedExtensionIds(self):
        return self.__usedExtensionIds

    @usedExtensionIds.setter
    def usedExtensionIds(self, usedExtensionIds: str):
        self.__usedExtensionIds = usedExtensionIds


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def automaton(self):
        return self.__automaton

    @automaton.setter
    def automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Automaton__automaton", None)
        self.__automaton = value if value is not None else set()
        
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
    def automata(self):
        return self.__automata

    @automata.setter
    def automata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Automaton__automata", None)
        self.__automata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module"):
                opp_val = getattr(old_value, "Module", None)
                if opp_val == self:
                    setattr(old_value, "Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module"):
                opp_val = getattr(value, "Module", None)
                setattr(value, "Module", self)

    @property
    def automaton2(self):
        return self.__automaton2

    @automaton2.setter
    def automaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Automaton__automaton2", None)
        self.__automaton2 = value if value is not None else set()
        
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
                    

class ea_extensions_IExtendible(ABC):

    def __init__(self, owner: set["IExtension"] = None):
        self.owner = owner if owner is not None else set()
        
        pass
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_extensions_IExtendible__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IExtension"):
                    opp_val = getattr(item, "IExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "IExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IExtension"):
                    opp_val = getattr(item, "IExtension", None)
                    
                    setattr(item, "IExtension", self)
                    

    def updateExtension(self, ea_extension):
        # TODO: Implement updateExtension method
        pass

    def findExtension(self, ea_id) :
        # TODO: Implement findExtension method
        pass

class ea_automata_Module:

    pass
class ea_automata_Transition(ExtendibleElement):

    def __init__(self, id: str, transitions: "Automaton" = None, outgoing: "State" = None, incoming: "State" = None):
        self.id = id
        self.transitions = transitions
        self.outgoing = outgoing
        self.incoming = incoming
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Transition__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State12"):
                opp_val = getattr(old_value, "State12", None)
                if opp_val == self:
                    setattr(old_value, "State12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State12"):
                opp_val = getattr(value, "State12", None)
                setattr(value, "State12", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Automaton10"):
                opp_val = getattr(old_value, "Automaton10", None)
                if opp_val == self:
                    setattr(old_value, "Automaton10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Automaton10"):
                opp_val = getattr(value, "Automaton10", None)
                setattr(value, "Automaton10", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_Transition__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State14"):
                opp_val = getattr(old_value, "State14", None)
                if opp_val == self:
                    setattr(old_value, "State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State14"):
                opp_val = getattr(value, "State14", None)
                setattr(value, "State14", self)

class Automaton:

    pass
class ea_automata_State(ExtendibleElement):

    def __init__(self, id: str, name: str, states: "Automaton" = None, target: set["Transition"] = None, source: set["Transition"] = None):
        self.id = id
        self.name = name
        self.states = states
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_State__states", None)
        self.__states = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Automaton"):
                opp_val = getattr(old_value, "Automaton", None)
                if opp_val == self:
                    setattr(old_value, "Automaton", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Automaton"):
                opp_val = getattr(value, "Automaton", None)
                setattr(value, "Automaton", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition6"):
                    opp_val = getattr(item, "Transition6", None)
                    
                    setattr(item, "Transition6", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ea_automata_State__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition8"):
                    opp_val = getattr(item, "Transition8", None)
                    
                    setattr(item, "Transition8", self)
                    

class Module:

    pass
class Transition:

    pass