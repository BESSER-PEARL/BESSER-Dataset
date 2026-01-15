from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractLink:

    pass
class etrace_Link(AbstractLink):

    pass
class etrace_CompositeLink(AbstractLink):

    def __init__(self, etrace_CompositeLink: set["etrace_AbstractLink"] = None):
        self.etrace_CompositeLink = etrace_CompositeLink if etrace_CompositeLink is not None else set()
        
    @property
    def etrace_CompositeLink(self):
        return self.__etrace_CompositeLink

    @etrace_CompositeLink.setter
    def etrace_CompositeLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_CompositeLink__etrace_CompositeLink", None)
        self.__etrace_CompositeLink = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etrace_AbstractLink20"):
                    opp_val = getattr(item, "etrace_AbstractLink20", None)
                    
                    if opp_val == self:
                        setattr(item, "etrace_AbstractLink20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etrace_AbstractLink20"):
                    opp_val = getattr(item, "etrace_AbstractLink20", None)
                    
                    setattr(item, "etrace_AbstractLink20", self)
                    

    def createLink(self) -> str:
        # TODO: Implement createLink method
        pass

    def createCompositeLink(self, source: str, target: str, links: AbstractLink, type: str) -> CompositeLink:
        # TODO: Implement createCompositeLink method
        pass

    def createLink(self, type: str, target: str, source: str) -> str:
        # TODO: Implement createLink method
        pass

    def createCompositeLink(self) -> CompositeLink:
        # TODO: Implement createCompositeLink method
        pass

    def createCompositeLink(self, type: str, target: str, source: str) -> CompositeLink:
        # TODO: Implement createCompositeLink method
        pass

class CompositeLink:

    pass
class etrace_ETrace(CompositeLink):

    def __init__(self, name: str, etrace_ETrace: set["etrace_LinkType"] = None, etrace_ETrace14: set["etrace_EObject"] = None, etrace_ETrace17: set["etrace_EObject"] = None):
        self.name = name
        self.etrace_ETrace = etrace_ETrace if etrace_ETrace is not None else set()
        self.etrace_ETrace14 = etrace_ETrace14 if etrace_ETrace14 is not None else set()
        self.etrace_ETrace17 = etrace_ETrace17 if etrace_ETrace17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def etrace_ETrace14(self):
        return self.__etrace_ETrace14

    @etrace_ETrace14.setter
    def etrace_ETrace14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_ETrace__etrace_ETrace14", None)
        self.__etrace_ETrace14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etrace_EObject15"):
                    opp_val = getattr(item, "etrace_EObject15", None)
                    
                    if opp_val == self:
                        setattr(item, "etrace_EObject15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etrace_EObject15"):
                    opp_val = getattr(item, "etrace_EObject15", None)
                    
                    setattr(item, "etrace_EObject15", self)
                    

    @property
    def etrace_ETrace(self):
        return self.__etrace_ETrace

    @etrace_ETrace.setter
    def etrace_ETrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_ETrace__etrace_ETrace", None)
        self.__etrace_ETrace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etrace_LinkType12"):
                    opp_val = getattr(item, "etrace_LinkType12", None)
                    
                    if opp_val == self:
                        setattr(item, "etrace_LinkType12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etrace_LinkType12"):
                    opp_val = getattr(item, "etrace_LinkType12", None)
                    
                    setattr(item, "etrace_LinkType12", self)
                    

    @property
    def etrace_ETrace17(self):
        return self.__etrace_ETrace17

    @etrace_ETrace17.setter
    def etrace_ETrace17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_ETrace__etrace_ETrace17", None)
        self.__etrace_ETrace17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etrace_EObject18"):
                    opp_val = getattr(item, "etrace_EObject18", None)
                    
                    if opp_val == self:
                        setattr(item, "etrace_EObject18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etrace_EObject18"):
                    opp_val = getattr(item, "etrace_EObject18", None)
                    
                    setattr(item, "etrace_EObject18", self)
                    

class etrace_LinkType:

    def __init__(self, description: str, purpose: str, uses: str, example: str, name: str, superType: set["etrace_LinkType"] = None, LinkType10: "etrace_LinkType" = None, subType: "etrace_LinkType" = None, etrace_LinkType: "etrace_AbstractLink" = None, LinkType: "etrace_LinkType" = None, etrace_LinkType12: "etrace_ETrace" = None):
        self.description = description
        self.purpose = purpose
        self.uses = uses
        self.example = example
        self.name = name
        self.superType = superType if superType is not None else set()
        self.LinkType10 = LinkType10
        self.subType = subType
        self.etrace_LinkType = etrace_LinkType
        self.LinkType = LinkType
        self.etrace_LinkType12 = etrace_LinkType12
        
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
    def purpose(self) -> str:
        return self.__purpose

    @purpose.setter
    def purpose(self, purpose: str):
        self.__purpose = purpose

    @property
    def example(self) -> str:
        return self.__example

    @example.setter
    def example(self, example: str):
        self.__example = example

    @property
    def uses(self) -> str:
        return self.__uses

    @uses.setter
    def uses(self, uses: str):
        self.__uses = uses

    @property
    def superType(self):
        return self.__superType

    @superType.setter
    def superType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_LinkType__superType", None)
        self.__superType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LinkType"):
                    opp_val = getattr(item, "LinkType", None)
                    
                    if opp_val == self:
                        setattr(item, "LinkType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LinkType"):
                    opp_val = getattr(item, "LinkType", None)
                    
                    setattr(item, "LinkType", self)
                    

    @property
    def LinkType(self):
        return self.__LinkType

    @LinkType.setter
    def LinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_LinkType__LinkType", None)
        self.__LinkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "superType"):
                opp_val = getattr(old_value, "superType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "superType"):
                opp_val = getattr(value, "superType", None)
                if opp_val is None:
                    setattr(value, "superType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LinkType10(self):
        return self.__LinkType10

    @LinkType10.setter
    def LinkType10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_LinkType__LinkType10", None)
        self.__LinkType10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subType"):
                opp_val = getattr(old_value, "subType", None)
                if opp_val == self:
                    setattr(old_value, "subType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subType"):
                opp_val = getattr(value, "subType", None)
                setattr(value, "subType", self)

    @property
    def etrace_LinkType(self):
        return self.__etrace_LinkType

    @etrace_LinkType.setter
    def etrace_LinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_LinkType__etrace_LinkType", None)
        self.__etrace_LinkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etrace_AbstractLink5"):
                opp_val = getattr(old_value, "etrace_AbstractLink5", None)
                if opp_val == self:
                    setattr(old_value, "etrace_AbstractLink5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etrace_AbstractLink5"):
                opp_val = getattr(value, "etrace_AbstractLink5", None)
                setattr(value, "etrace_AbstractLink5", self)

    @property
    def etrace_LinkType12(self):
        return self.__etrace_LinkType12

    @etrace_LinkType12.setter
    def etrace_LinkType12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_LinkType__etrace_LinkType12", None)
        self.__etrace_LinkType12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etrace_ETrace"):
                opp_val = getattr(old_value, "etrace_ETrace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etrace_ETrace"):
                opp_val = getattr(value, "etrace_ETrace", None)
                if opp_val is None:
                    setattr(value, "etrace_ETrace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def subType(self):
        return self.__subType

    @subType.setter
    def subType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etrace_LinkType__subType", None)
        self.__subType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LinkType10"):
                opp_val = getattr(old_value, "LinkType10", None)
                if opp_val == self:
                    setattr(old_value, "LinkType10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LinkType10"):
                opp_val = getattr(value, "LinkType10", None)
                setattr(value, "LinkType10", self)

class etrace_EObject:

    pass
class etrace_AbstractLink(ABC):

    pass