from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EventType(Enum):
    Basic = "Basic"
    External = "External"
    Undevelopped = "Undevelopped"
    Conditioning = "Conditioning"
    Intermediate = "Intermediate"
class GateType(Enum):
    OR = "OR"
    AND = "AND"
    XOR = "XOR"
    PRIORITY_AND = "PRIORITY_AND"
    INHIBIT = "INHIBIT"
    PRIORITY_OR = "PRIORITY_OR"
    INTERMEDIATE = "INTERMEDIATE"
    ORMORE = "ORMORE"
    ORLESS = "ORLESS"


############################################
# Definition of Classes
############################################

class emfta_FTAModel:

    def __init__(self, name: str, description: str, comments: str, emfta_FTAModel: "emfta_Event" = None, emfta_FTAModel7: set["emfta_Event"] = None):
        self.name = name
        self.description = description
        self.comments = comments
        self.emfta_FTAModel = emfta_FTAModel
        self.emfta_FTAModel7 = emfta_FTAModel7 if emfta_FTAModel7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def emfta_FTAModel7(self):
        return self.__emfta_FTAModel7

    @emfta_FTAModel7.setter
    def emfta_FTAModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_FTAModel__emfta_FTAModel7", None)
        self.__emfta_FTAModel7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emfta_Event8"):
                    opp_val = getattr(item, "emfta_Event8", None)
                    
                    if opp_val == self:
                        setattr(item, "emfta_Event8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emfta_Event8"):
                    opp_val = getattr(item, "emfta_Event8", None)
                    
                    setattr(item, "emfta_Event8", self)
                    

    @property
    def emfta_FTAModel(self):
        return self.__emfta_FTAModel

    @emfta_FTAModel.setter
    def emfta_FTAModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_FTAModel__emfta_FTAModel", None)
        self.__emfta_FTAModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfta_Event5"):
                opp_val = getattr(old_value, "emfta_Event5", None)
                if opp_val == self:
                    setattr(old_value, "emfta_Event5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfta_Event5"):
                opp_val = getattr(value, "emfta_Event5", None)
                setattr(value, "emfta_Event5", self)

class emfta_Gate:

    def __init__(self, type: str, description: str, nbOccurrences: int, emfta_Gate: "emfta_Event" = None, emfta_Gate2: set["emfta_Event"] = None):
        self.type = type
        self.description = description
        self.nbOccurrences = nbOccurrences
        self.emfta_Gate = emfta_Gate
        self.emfta_Gate2 = emfta_Gate2 if emfta_Gate2 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def nbOccurrences(self) -> int:
        return self.__nbOccurrences

    @nbOccurrences.setter
    def nbOccurrences(self, nbOccurrences: int):
        self.__nbOccurrences = nbOccurrences

    @property
    def emfta_Gate2(self):
        return self.__emfta_Gate2

    @emfta_Gate2.setter
    def emfta_Gate2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_Gate__emfta_Gate2", None)
        self.__emfta_Gate2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emfta_Event3"):
                    opp_val = getattr(item, "emfta_Event3", None)
                    
                    if opp_val == self:
                        setattr(item, "emfta_Event3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emfta_Event3"):
                    opp_val = getattr(item, "emfta_Event3", None)
                    
                    setattr(item, "emfta_Event3", self)
                    

    @property
    def emfta_Gate(self):
        return self.__emfta_Gate

    @emfta_Gate.setter
    def emfta_Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_Gate__emfta_Gate", None)
        self.__emfta_Gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfta_Event"):
                opp_val = getattr(old_value, "emfta_Event", None)
                if opp_val == self:
                    setattr(old_value, "emfta_Event", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfta_Event"):
                opp_val = getattr(value, "emfta_Event", None)
                setattr(value, "emfta_Event", self)

class emfta_Event:

    def __init__(self, probability: float, type: str, name: str, description: str, relatedObject: str, referenceCount: int, emfta_Event: "emfta_Gate" = None, emfta_Event3: "emfta_Gate" = None, emfta_Event5: "emfta_FTAModel" = None, emfta_Event8: "emfta_FTAModel" = None):
        self.probability = probability
        self.type = type
        self.name = name
        self.description = description
        self.relatedObject = relatedObject
        self.referenceCount = referenceCount
        self.emfta_Event = emfta_Event
        self.emfta_Event3 = emfta_Event3
        self.emfta_Event5 = emfta_Event5
        self.emfta_Event8 = emfta_Event8
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def referenceCount(self) -> int:
        return self.__referenceCount

    @referenceCount.setter
    def referenceCount(self, referenceCount: int):
        self.__referenceCount = referenceCount

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def relatedObject(self) -> str:
        return self.__relatedObject

    @relatedObject.setter
    def relatedObject(self, relatedObject: str):
        self.__relatedObject = relatedObject

    @property
    def probability(self) -> float:
        return self.__probability

    @probability.setter
    def probability(self, probability: float):
        self.__probability = probability

    @property
    def emfta_Event3(self):
        return self.__emfta_Event3

    @emfta_Event3.setter
    def emfta_Event3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_Event__emfta_Event3", None)
        self.__emfta_Event3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfta_Gate2"):
                opp_val = getattr(old_value, "emfta_Gate2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfta_Gate2"):
                opp_val = getattr(value, "emfta_Gate2", None)
                if opp_val is None:
                    setattr(value, "emfta_Gate2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emfta_Event5(self):
        return self.__emfta_Event5

    @emfta_Event5.setter
    def emfta_Event5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_Event__emfta_Event5", None)
        self.__emfta_Event5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfta_FTAModel"):
                opp_val = getattr(old_value, "emfta_FTAModel", None)
                if opp_val == self:
                    setattr(old_value, "emfta_FTAModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfta_FTAModel"):
                opp_val = getattr(value, "emfta_FTAModel", None)
                setattr(value, "emfta_FTAModel", self)

    @property
    def emfta_Event(self):
        return self.__emfta_Event

    @emfta_Event.setter
    def emfta_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_Event__emfta_Event", None)
        self.__emfta_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfta_Gate"):
                opp_val = getattr(old_value, "emfta_Gate", None)
                if opp_val == self:
                    setattr(old_value, "emfta_Gate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfta_Gate"):
                opp_val = getattr(value, "emfta_Gate", None)
                setattr(value, "emfta_Gate", self)

    @property
    def emfta_Event8(self):
        return self.__emfta_Event8

    @emfta_Event8.setter
    def emfta_Event8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emfta_Event__emfta_Event8", None)
        self.__emfta_Event8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emfta_FTAModel7"):
                opp_val = getattr(old_value, "emfta_FTAModel7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emfta_FTAModel7"):
                opp_val = getattr(value, "emfta_FTAModel7", None)
                if opp_val is None:
                    setattr(value, "emfta_FTAModel7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
