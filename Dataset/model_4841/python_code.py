from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class refinement(Enum):
    AND = "AND"
    OR = "OR"
class relationType(Enum):
    association = "association"
    realization = "realization"
    trigger = "trigger"
    composition = "composition"
    influences = "influences"


############################################
# Definition of Classes
############################################

class BusinessElement:

    pass
class archimate_BusinessProcess(BusinessElement):

    pass
class StrategyElement:

    pass
class archimate_Resource(StrategyElement):

    pass
class Requirement:

    pass
class archimate_Constraint(Requirement):

    pass
class ActiveStructureElement:

    pass
class archimate_Stakeholder(ActiveStructureElement):

    pass
class archimate_StrategyElement(ABC):

    def __init__(self, name: str, refinementType: str, relationType: str, archimate_StrategyElement: "archimate_ArchimateDiagram" = None, archimate_StrategyElement54: "archimate_StrategyElement" = None, archimate_StrategyElement52: set["archimate_StrategyElement"] = None, archimate_StrategyElement56: set["archimate_MotivationElement"] = None):
        self.name = name
        self.refinementType = refinementType
        self.relationType = relationType
        self.archimate_StrategyElement = archimate_StrategyElement
        self.archimate_StrategyElement54 = archimate_StrategyElement54
        self.archimate_StrategyElement52 = archimate_StrategyElement52 if archimate_StrategyElement52 is not None else set()
        self.archimate_StrategyElement56 = archimate_StrategyElement56 if archimate_StrategyElement56 is not None else set()
        
    @property
    def relationType(self) -> str:
        return self.__relationType

    @relationType.setter
    def relationType(self, relationType: str):
        self.__relationType = relationType

    @property
    def refinementType(self) -> str:
        return self.__refinementType

    @refinementType.setter
    def refinementType(self, refinementType: str):
        self.__refinementType = refinementType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archimate_StrategyElement52(self):
        return self.__archimate_StrategyElement52

    @archimate_StrategyElement52.setter
    def archimate_StrategyElement52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_StrategyElement__archimate_StrategyElement52", None)
        self.__archimate_StrategyElement52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_StrategyElement54"):
                    opp_val = getattr(item, "archimate_StrategyElement54", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_StrategyElement54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_StrategyElement54"):
                    opp_val = getattr(item, "archimate_StrategyElement54", None)
                    
                    setattr(item, "archimate_StrategyElement54", self)
                    

    @property
    def archimate_StrategyElement54(self):
        return self.__archimate_StrategyElement54

    @archimate_StrategyElement54.setter
    def archimate_StrategyElement54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_StrategyElement__archimate_StrategyElement54", None)
        self.__archimate_StrategyElement54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_StrategyElement52"):
                opp_val = getattr(old_value, "archimate_StrategyElement52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_StrategyElement52"):
                opp_val = getattr(value, "archimate_StrategyElement52", None)
                if opp_val is None:
                    setattr(value, "archimate_StrategyElement52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_StrategyElement56(self):
        return self.__archimate_StrategyElement56

    @archimate_StrategyElement56.setter
    def archimate_StrategyElement56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_StrategyElement__archimate_StrategyElement56", None)
        self.__archimate_StrategyElement56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement57"):
                    opp_val = getattr(item, "archimate_MotivationElement57", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement57"):
                    opp_val = getattr(item, "archimate_MotivationElement57", None)
                    
                    setattr(item, "archimate_MotivationElement57", self)
                    

    @property
    def archimate_StrategyElement(self):
        return self.__archimate_StrategyElement

    @archimate_StrategyElement.setter
    def archimate_StrategyElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_StrategyElement__archimate_StrategyElement", None)
        self.__archimate_StrategyElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_ArchimateDiagram6"):
                opp_val = getattr(old_value, "archimate_ArchimateDiagram6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_ArchimateDiagram6"):
                opp_val = getattr(value, "archimate_ArchimateDiagram6", None)
                if opp_val is None:
                    setattr(value, "archimate_ArchimateDiagram6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archimate_BusinessElement(ABC):

    def __init__(self, name: str, refinementType: str, relationType: str, archimate_BusinessElement: "archimate_ArchimateDiagram" = None, archimate_BusinessElement60: "archimate_BusinessElement" = None, archimate_BusinessElement58: set["archimate_BusinessElement"] = None, archimate_BusinessElement62: set["archimate_MotivationElement"] = None, archimate_BusinessElement65: set["archimate_MotivationElement"] = None, archimate_BusinessElement69: "archimate_BusinessElement" = None, archimate_BusinessElement67: "archimate_BusinessElement" = None, archimate_BusinessElement71: set["archimate_MotivationElement"] = None):
        self.name = name
        self.refinementType = refinementType
        self.relationType = relationType
        self.archimate_BusinessElement = archimate_BusinessElement
        self.archimate_BusinessElement60 = archimate_BusinessElement60
        self.archimate_BusinessElement58 = archimate_BusinessElement58 if archimate_BusinessElement58 is not None else set()
        self.archimate_BusinessElement62 = archimate_BusinessElement62 if archimate_BusinessElement62 is not None else set()
        self.archimate_BusinessElement65 = archimate_BusinessElement65 if archimate_BusinessElement65 is not None else set()
        self.archimate_BusinessElement69 = archimate_BusinessElement69
        self.archimate_BusinessElement67 = archimate_BusinessElement67
        self.archimate_BusinessElement71 = archimate_BusinessElement71 if archimate_BusinessElement71 is not None else set()
        
    @property
    def refinementType(self) -> str:
        return self.__refinementType

    @refinementType.setter
    def refinementType(self, refinementType: str):
        self.__refinementType = refinementType

    @property
    def relationType(self) -> str:
        return self.__relationType

    @relationType.setter
    def relationType(self, relationType: str):
        self.__relationType = relationType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archimate_BusinessElement71(self):
        return self.__archimate_BusinessElement71

    @archimate_BusinessElement71.setter
    def archimate_BusinessElement71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement71", None)
        self.__archimate_BusinessElement71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement72"):
                    opp_val = getattr(item, "archimate_MotivationElement72", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement72"):
                    opp_val = getattr(item, "archimate_MotivationElement72", None)
                    
                    setattr(item, "archimate_MotivationElement72", self)
                    

    @property
    def archimate_BusinessElement69(self):
        return self.__archimate_BusinessElement69

    @archimate_BusinessElement69.setter
    def archimate_BusinessElement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement69", None)
        self.__archimate_BusinessElement69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_BusinessElement67"):
                opp_val = getattr(old_value, "archimate_BusinessElement67", None)
                if opp_val == self:
                    setattr(old_value, "archimate_BusinessElement67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_BusinessElement67"):
                opp_val = getattr(value, "archimate_BusinessElement67", None)
                setattr(value, "archimate_BusinessElement67", self)

    @property
    def archimate_BusinessElement60(self):
        return self.__archimate_BusinessElement60

    @archimate_BusinessElement60.setter
    def archimate_BusinessElement60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement60", None)
        self.__archimate_BusinessElement60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_BusinessElement58"):
                opp_val = getattr(old_value, "archimate_BusinessElement58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_BusinessElement58"):
                opp_val = getattr(value, "archimate_BusinessElement58", None)
                if opp_val is None:
                    setattr(value, "archimate_BusinessElement58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_BusinessElement67(self):
        return self.__archimate_BusinessElement67

    @archimate_BusinessElement67.setter
    def archimate_BusinessElement67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement67", None)
        self.__archimate_BusinessElement67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_BusinessElement69"):
                opp_val = getattr(old_value, "archimate_BusinessElement69", None)
                if opp_val == self:
                    setattr(old_value, "archimate_BusinessElement69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_BusinessElement69"):
                opp_val = getattr(value, "archimate_BusinessElement69", None)
                setattr(value, "archimate_BusinessElement69", self)

    @property
    def archimate_BusinessElement58(self):
        return self.__archimate_BusinessElement58

    @archimate_BusinessElement58.setter
    def archimate_BusinessElement58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement58", None)
        self.__archimate_BusinessElement58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_BusinessElement60"):
                    opp_val = getattr(item, "archimate_BusinessElement60", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_BusinessElement60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_BusinessElement60"):
                    opp_val = getattr(item, "archimate_BusinessElement60", None)
                    
                    setattr(item, "archimate_BusinessElement60", self)
                    

    @property
    def archimate_BusinessElement65(self):
        return self.__archimate_BusinessElement65

    @archimate_BusinessElement65.setter
    def archimate_BusinessElement65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement65", None)
        self.__archimate_BusinessElement65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement66"):
                    opp_val = getattr(item, "archimate_MotivationElement66", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement66"):
                    opp_val = getattr(item, "archimate_MotivationElement66", None)
                    
                    setattr(item, "archimate_MotivationElement66", self)
                    

    @property
    def archimate_BusinessElement(self):
        return self.__archimate_BusinessElement

    @archimate_BusinessElement.setter
    def archimate_BusinessElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement", None)
        self.__archimate_BusinessElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_ArchimateDiagram4"):
                opp_val = getattr(old_value, "archimate_ArchimateDiagram4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_ArchimateDiagram4"):
                opp_val = getattr(value, "archimate_ArchimateDiagram4", None)
                if opp_val is None:
                    setattr(value, "archimate_ArchimateDiagram4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_BusinessElement62(self):
        return self.__archimate_BusinessElement62

    @archimate_BusinessElement62.setter
    def archimate_BusinessElement62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_BusinessElement__archimate_BusinessElement62", None)
        self.__archimate_BusinessElement62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement63"):
                    opp_val = getattr(item, "archimate_MotivationElement63", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement63"):
                    opp_val = getattr(item, "archimate_MotivationElement63", None)
                    
                    setattr(item, "archimate_MotivationElement63", self)
                    

class archimate_MotivationElement(ABC):

    def __init__(self, name: str, refinementType: str, relationType: str, archimate_MotivationElement21: "archimate_MotivationElement" = None, archimate_MotivationElement19: set["archimate_MotivationElement"] = None, archimate_MotivationElement24: "archimate_MotivationElement" = None, archimate_MotivationElement22: set["archimate_MotivationElement"] = None, archimate_MotivationElement: "archimate_ArchimateDiagram" = None, archimate_MotivationElement12: "archimate_ActiveStructureElement" = None, archimate_MotivationElement18: "archimate_MotivationElement" = None, archimate_MotivationElement16: set["archimate_MotivationElement"] = None, archimate_MotivationElement57: "archimate_StrategyElement" = None, archimate_MotivationElement63: "archimate_BusinessElement" = None, archimate_MotivationElement66: "archimate_BusinessElement" = None, archimate_MotivationElement72: "archimate_BusinessElement" = None):
        self.name = name
        self.refinementType = refinementType
        self.relationType = relationType
        self.archimate_MotivationElement21 = archimate_MotivationElement21
        self.archimate_MotivationElement19 = archimate_MotivationElement19 if archimate_MotivationElement19 is not None else set()
        self.archimate_MotivationElement24 = archimate_MotivationElement24
        self.archimate_MotivationElement22 = archimate_MotivationElement22 if archimate_MotivationElement22 is not None else set()
        self.archimate_MotivationElement = archimate_MotivationElement
        self.archimate_MotivationElement12 = archimate_MotivationElement12
        self.archimate_MotivationElement18 = archimate_MotivationElement18
        self.archimate_MotivationElement16 = archimate_MotivationElement16 if archimate_MotivationElement16 is not None else set()
        self.archimate_MotivationElement57 = archimate_MotivationElement57
        self.archimate_MotivationElement63 = archimate_MotivationElement63
        self.archimate_MotivationElement66 = archimate_MotivationElement66
        self.archimate_MotivationElement72 = archimate_MotivationElement72
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def refinementType(self) -> str:
        return self.__refinementType

    @refinementType.setter
    def refinementType(self, refinementType: str):
        self.__refinementType = refinementType

    @property
    def relationType(self) -> str:
        return self.__relationType

    @relationType.setter
    def relationType(self, relationType: str):
        self.__relationType = relationType

    @property
    def archimate_MotivationElement19(self):
        return self.__archimate_MotivationElement19

    @archimate_MotivationElement19.setter
    def archimate_MotivationElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement19", None)
        self.__archimate_MotivationElement19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement21"):
                    opp_val = getattr(item, "archimate_MotivationElement21", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement21"):
                    opp_val = getattr(item, "archimate_MotivationElement21", None)
                    
                    setattr(item, "archimate_MotivationElement21", self)
                    

    @property
    def archimate_MotivationElement(self):
        return self.__archimate_MotivationElement

    @archimate_MotivationElement.setter
    def archimate_MotivationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement", None)
        self.__archimate_MotivationElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_ArchimateDiagram2"):
                opp_val = getattr(old_value, "archimate_ArchimateDiagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_ArchimateDiagram2"):
                opp_val = getattr(value, "archimate_ArchimateDiagram2", None)
                if opp_val is None:
                    setattr(value, "archimate_ArchimateDiagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement16(self):
        return self.__archimate_MotivationElement16

    @archimate_MotivationElement16.setter
    def archimate_MotivationElement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement16", None)
        self.__archimate_MotivationElement16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement18"):
                    opp_val = getattr(item, "archimate_MotivationElement18", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement18"):
                    opp_val = getattr(item, "archimate_MotivationElement18", None)
                    
                    setattr(item, "archimate_MotivationElement18", self)
                    

    @property
    def archimate_MotivationElement63(self):
        return self.__archimate_MotivationElement63

    @archimate_MotivationElement63.setter
    def archimate_MotivationElement63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement63", None)
        self.__archimate_MotivationElement63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_BusinessElement62"):
                opp_val = getattr(old_value, "archimate_BusinessElement62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_BusinessElement62"):
                opp_val = getattr(value, "archimate_BusinessElement62", None)
                if opp_val is None:
                    setattr(value, "archimate_BusinessElement62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement72(self):
        return self.__archimate_MotivationElement72

    @archimate_MotivationElement72.setter
    def archimate_MotivationElement72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement72", None)
        self.__archimate_MotivationElement72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_BusinessElement71"):
                opp_val = getattr(old_value, "archimate_BusinessElement71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_BusinessElement71"):
                opp_val = getattr(value, "archimate_BusinessElement71", None)
                if opp_val is None:
                    setattr(value, "archimate_BusinessElement71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement18(self):
        return self.__archimate_MotivationElement18

    @archimate_MotivationElement18.setter
    def archimate_MotivationElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement18", None)
        self.__archimate_MotivationElement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_MotivationElement16"):
                opp_val = getattr(old_value, "archimate_MotivationElement16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_MotivationElement16"):
                opp_val = getattr(value, "archimate_MotivationElement16", None)
                if opp_val is None:
                    setattr(value, "archimate_MotivationElement16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement57(self):
        return self.__archimate_MotivationElement57

    @archimate_MotivationElement57.setter
    def archimate_MotivationElement57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement57", None)
        self.__archimate_MotivationElement57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_StrategyElement56"):
                opp_val = getattr(old_value, "archimate_StrategyElement56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_StrategyElement56"):
                opp_val = getattr(value, "archimate_StrategyElement56", None)
                if opp_val is None:
                    setattr(value, "archimate_StrategyElement56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement66(self):
        return self.__archimate_MotivationElement66

    @archimate_MotivationElement66.setter
    def archimate_MotivationElement66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement66", None)
        self.__archimate_MotivationElement66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_BusinessElement65"):
                opp_val = getattr(old_value, "archimate_BusinessElement65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_BusinessElement65"):
                opp_val = getattr(value, "archimate_BusinessElement65", None)
                if opp_val is None:
                    setattr(value, "archimate_BusinessElement65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement12(self):
        return self.__archimate_MotivationElement12

    @archimate_MotivationElement12.setter
    def archimate_MotivationElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement12", None)
        self.__archimate_MotivationElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_ActiveStructureElement11"):
                opp_val = getattr(old_value, "archimate_ActiveStructureElement11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_ActiveStructureElement11"):
                opp_val = getattr(value, "archimate_ActiveStructureElement11", None)
                if opp_val is None:
                    setattr(value, "archimate_ActiveStructureElement11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement22(self):
        return self.__archimate_MotivationElement22

    @archimate_MotivationElement22.setter
    def archimate_MotivationElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement22", None)
        self.__archimate_MotivationElement22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement24"):
                    opp_val = getattr(item, "archimate_MotivationElement24", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement24"):
                    opp_val = getattr(item, "archimate_MotivationElement24", None)
                    
                    setattr(item, "archimate_MotivationElement24", self)
                    

    @property
    def archimate_MotivationElement24(self):
        return self.__archimate_MotivationElement24

    @archimate_MotivationElement24.setter
    def archimate_MotivationElement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement24", None)
        self.__archimate_MotivationElement24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_MotivationElement22"):
                opp_val = getattr(old_value, "archimate_MotivationElement22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_MotivationElement22"):
                opp_val = getattr(value, "archimate_MotivationElement22", None)
                if opp_val is None:
                    setattr(value, "archimate_MotivationElement22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_MotivationElement21(self):
        return self.__archimate_MotivationElement21

    @archimate_MotivationElement21.setter
    def archimate_MotivationElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_MotivationElement__archimate_MotivationElement21", None)
        self.__archimate_MotivationElement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_MotivationElement19"):
                opp_val = getattr(old_value, "archimate_MotivationElement19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_MotivationElement19"):
                opp_val = getattr(value, "archimate_MotivationElement19", None)
                if opp_val is None:
                    setattr(value, "archimate_MotivationElement19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archimate_ActiveStructureElement(ABC):

    def __init__(self, name: str, archimate_ActiveStructureElement: "archimate_ArchimateDiagram" = None, archimate_ActiveStructureElement9: "archimate_ActiveStructureElement" = None, archimate_ActiveStructureElement7: set["archimate_ActiveStructureElement"] = None, archimate_ActiveStructureElement11: set["archimate_MotivationElement"] = None):
        self.name = name
        self.archimate_ActiveStructureElement = archimate_ActiveStructureElement
        self.archimate_ActiveStructureElement9 = archimate_ActiveStructureElement9
        self.archimate_ActiveStructureElement7 = archimate_ActiveStructureElement7 if archimate_ActiveStructureElement7 is not None else set()
        self.archimate_ActiveStructureElement11 = archimate_ActiveStructureElement11 if archimate_ActiveStructureElement11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def archimate_ActiveStructureElement9(self):
        return self.__archimate_ActiveStructureElement9

    @archimate_ActiveStructureElement9.setter
    def archimate_ActiveStructureElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_ActiveStructureElement__archimate_ActiveStructureElement9", None)
        self.__archimate_ActiveStructureElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_ActiveStructureElement7"):
                opp_val = getattr(old_value, "archimate_ActiveStructureElement7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_ActiveStructureElement7"):
                opp_val = getattr(value, "archimate_ActiveStructureElement7", None)
                if opp_val is None:
                    setattr(value, "archimate_ActiveStructureElement7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def archimate_ActiveStructureElement11(self):
        return self.__archimate_ActiveStructureElement11

    @archimate_ActiveStructureElement11.setter
    def archimate_ActiveStructureElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_ActiveStructureElement__archimate_ActiveStructureElement11", None)
        self.__archimate_ActiveStructureElement11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_MotivationElement12"):
                    opp_val = getattr(item, "archimate_MotivationElement12", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_MotivationElement12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_MotivationElement12"):
                    opp_val = getattr(item, "archimate_MotivationElement12", None)
                    
                    setattr(item, "archimate_MotivationElement12", self)
                    

    @property
    def archimate_ActiveStructureElement7(self):
        return self.__archimate_ActiveStructureElement7

    @archimate_ActiveStructureElement7.setter
    def archimate_ActiveStructureElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_ActiveStructureElement__archimate_ActiveStructureElement7", None)
        self.__archimate_ActiveStructureElement7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "archimate_ActiveStructureElement9"):
                    opp_val = getattr(item, "archimate_ActiveStructureElement9", None)
                    
                    if opp_val == self:
                        setattr(item, "archimate_ActiveStructureElement9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "archimate_ActiveStructureElement9"):
                    opp_val = getattr(item, "archimate_ActiveStructureElement9", None)
                    
                    setattr(item, "archimate_ActiveStructureElement9", self)
                    

    @property
    def archimate_ActiveStructureElement(self):
        return self.__archimate_ActiveStructureElement

    @archimate_ActiveStructureElement.setter
    def archimate_ActiveStructureElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_archimate_ActiveStructureElement__archimate_ActiveStructureElement", None)
        self.__archimate_ActiveStructureElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "archimate_ArchimateDiagram"):
                opp_val = getattr(old_value, "archimate_ArchimateDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "archimate_ArchimateDiagram"):
                opp_val = getattr(value, "archimate_ArchimateDiagram", None)
                if opp_val is None:
                    setattr(value, "archimate_ArchimateDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class archimate_ArchimateDiagram:

    pass
class MotivationElement:

    pass
class archimate_Driver(MotivationElement):

    pass
class archimate_Meaning(MotivationElement):

    pass
class archimate_Requirement(MotivationElement):

    pass
class archimate_Outcome(MotivationElement):

    pass
class archimate_Goal(MotivationElement):

    pass
class archimate_Value(MotivationElement):

    pass
class archimate_Assessment(MotivationElement):

    pass
class archimate_Principle(MotivationElement):

    pass