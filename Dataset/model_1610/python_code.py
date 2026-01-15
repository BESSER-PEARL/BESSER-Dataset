from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class pnml_Element(ABC):

    def __init__(self, id: str, location: str, pnml_Element: "pnml_NetElement" = None):
        self.id = id
        self.location = location
        self.pnml_Element = pnml_Element
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pnml_Element(self):
        return self.__pnml_Element

    @pnml_Element.setter
    def pnml_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_Element__pnml_Element", None)
        self.__pnml_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnml_NetElement10"):
                opp_val = getattr(old_value, "pnml_NetElement10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnml_NetElement10"):
                opp_val = getattr(value, "pnml_NetElement10", None)
                if opp_val is None:
                    setattr(value, "pnml_NetElement10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class pnml_ArcTransition2Place(Element):

    pass
class pnml_TransitionElement(Element):

    def __init__(self, name: str, pnml_TransitionElement: "pnml_ArcPlace2Transition" = None, pnml_TransitionElement8: "pnml_ArcTransition2Place" = None):
        self.name = name
        self.pnml_TransitionElement = pnml_TransitionElement
        self.pnml_TransitionElement8 = pnml_TransitionElement8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pnml_TransitionElement(self):
        return self.__pnml_TransitionElement

    @pnml_TransitionElement.setter
    def pnml_TransitionElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_TransitionElement__pnml_TransitionElement", None)
        self.__pnml_TransitionElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnml_ArcPlace2Transition3"):
                opp_val = getattr(old_value, "pnml_ArcPlace2Transition3", None)
                if opp_val == self:
                    setattr(old_value, "pnml_ArcPlace2Transition3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnml_ArcPlace2Transition3"):
                opp_val = getattr(value, "pnml_ArcPlace2Transition3", None)
                setattr(value, "pnml_ArcPlace2Transition3", self)

    @property
    def pnml_TransitionElement8(self):
        return self.__pnml_TransitionElement8

    @pnml_TransitionElement8.setter
    def pnml_TransitionElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_TransitionElement__pnml_TransitionElement8", None)
        self.__pnml_TransitionElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnml_ArcTransition2Place7"):
                opp_val = getattr(old_value, "pnml_ArcTransition2Place7", None)
                if opp_val == self:
                    setattr(old_value, "pnml_ArcTransition2Place7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnml_ArcTransition2Place7"):
                opp_val = getattr(value, "pnml_ArcTransition2Place7", None)
                setattr(value, "pnml_ArcTransition2Place7", self)

class pnml_ArcPlace2Transition(Element):

    pass
class pnml_PlaceElement(Element):

    def __init__(self, name: str, tokens: int, pnml_PlaceElement5: "pnml_ArcTransition2Place" = None, pnml_PlaceElement: "pnml_ArcPlace2Transition" = None):
        self.name = name
        self.tokens = tokens
        self.pnml_PlaceElement5 = pnml_PlaceElement5
        self.pnml_PlaceElement = pnml_PlaceElement
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pnml_PlaceElement(self):
        return self.__pnml_PlaceElement

    @pnml_PlaceElement.setter
    def pnml_PlaceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_PlaceElement__pnml_PlaceElement", None)
        self.__pnml_PlaceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnml_ArcPlace2Transition"):
                opp_val = getattr(old_value, "pnml_ArcPlace2Transition", None)
                if opp_val == self:
                    setattr(old_value, "pnml_ArcPlace2Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnml_ArcPlace2Transition"):
                opp_val = getattr(value, "pnml_ArcPlace2Transition", None)
                setattr(value, "pnml_ArcPlace2Transition", self)

    @property
    def pnml_PlaceElement5(self):
        return self.__pnml_PlaceElement5

    @pnml_PlaceElement5.setter
    def pnml_PlaceElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_PlaceElement__pnml_PlaceElement5", None)
        self.__pnml_PlaceElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnml_ArcTransition2Place"):
                opp_val = getattr(old_value, "pnml_ArcTransition2Place", None)
                if opp_val == self:
                    setattr(old_value, "pnml_ArcTransition2Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnml_ArcTransition2Place"):
                opp_val = getattr(value, "pnml_ArcTransition2Place", None)
                setattr(value, "pnml_ArcTransition2Place", self)

class pnml_NetElement(Element):

    def __init__(self, name: str, pnml_NetElement: "pnml_PNMLDocument" = None, pnml_NetElement10: set["pnml_Element"] = None):
        self.name = name
        self.pnml_NetElement = pnml_NetElement
        self.pnml_NetElement10 = pnml_NetElement10 if pnml_NetElement10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pnml_NetElement(self):
        return self.__pnml_NetElement

    @pnml_NetElement.setter
    def pnml_NetElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_NetElement__pnml_NetElement", None)
        self.__pnml_NetElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnml_PNMLDocument"):
                opp_val = getattr(old_value, "pnml_PNMLDocument", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnml_PNMLDocument"):
                opp_val = getattr(value, "pnml_PNMLDocument", None)
                if opp_val is None:
                    setattr(value, "pnml_PNMLDocument", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pnml_NetElement10(self):
        return self.__pnml_NetElement10

    @pnml_NetElement10.setter
    def pnml_NetElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_NetElement__pnml_NetElement10", None)
        self.__pnml_NetElement10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pnml_Element"):
                    opp_val = getattr(item, "pnml_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "pnml_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pnml_Element"):
                    opp_val = getattr(item, "pnml_Element", None)
                    
                    setattr(item, "pnml_Element", self)
                    

class pnml_PNMLDocument:

    def __init__(self, location: str, pnml_PNMLDocument: set["pnml_NetElement"] = None):
        self.location = location
        self.pnml_PNMLDocument = pnml_PNMLDocument if pnml_PNMLDocument is not None else set()
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def pnml_PNMLDocument(self):
        return self.__pnml_PNMLDocument

    @pnml_PNMLDocument.setter
    def pnml_PNMLDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnml_PNMLDocument__pnml_PNMLDocument", None)
        self.__pnml_PNMLDocument = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pnml_NetElement"):
                    opp_val = getattr(item, "pnml_NetElement", None)
                    
                    if opp_val == self:
                        setattr(item, "pnml_NetElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pnml_NetElement"):
                    opp_val = getattr(item, "pnml_NetElement", None)
                    
                    setattr(item, "pnml_NetElement", self)
                    
