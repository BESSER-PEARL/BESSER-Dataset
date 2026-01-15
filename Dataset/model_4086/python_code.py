from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class classDiagram_UMLElement(ABC):

    def __init__(self, name: str, UMLElement: "classDiagram_UMLClassDiagram" = None, elements: "classDiagram_UMLClassDiagram" = None):
        self.name = name
        self.UMLElement = UMLElement
        self.elements = elements
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLClassDiagram"):
                opp_val = getattr(old_value, "UMLClassDiagram", None)
                if opp_val == self:
                    setattr(old_value, "UMLClassDiagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLClassDiagram"):
                opp_val = getattr(value, "UMLClassDiagram", None)
                setattr(value, "UMLClassDiagram", self)

    @property
    def UMLElement(self):
        return self.__UMLElement

    @UMLElement.setter
    def UMLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLElement__UMLElement", None)
        self.__UMLElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram"):
                opp_val = getattr(old_value, "diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram"):
                opp_val = getattr(value, "diagram", None)
                if opp_val is None:
                    setattr(value, "diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UMLElement:

    pass
class classDiagram_UMLIncrement(UMLElement):

    pass
class classDiagram_UMLClassDiagram(UMLElement):

    pass
class UMLIncrement:

    pass
class classDiagram_UMLStereotype(UMLIncrement):

    def __init__(self, text: str, stereotypes: "classDiagram_UMLIncrement" = None, UMLStereotype: "classDiagram_UMLIncrement" = None):
        self.text = text
        self.stereotypes = stereotypes
        self.UMLStereotype = UMLStereotype
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def stereotypes(self):
        return self.__stereotypes

    @stereotypes.setter
    def stereotypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLStereotype__stereotypes", None)
        self.__stereotypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLIncrement"):
                opp_val = getattr(old_value, "UMLIncrement", None)
                if opp_val == self:
                    setattr(old_value, "UMLIncrement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLIncrement"):
                opp_val = getattr(value, "UMLIncrement", None)
                setattr(value, "UMLIncrement", self)

    @property
    def UMLStereotype(self):
        return self.__UMLStereotype

    @UMLStereotype.setter
    def UMLStereotype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLStereotype__UMLStereotype", None)
        self.__UMLStereotype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "increment"):
                opp_val = getattr(old_value, "increment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "increment"):
                opp_val = getattr(value, "increment", None)
                if opp_val is None:
                    setattr(value, "increment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class classDiagram_UMLDiagramItem(UMLIncrement):

    pass
class classDiagram_UMLCardinality(UMLIncrement):

    def __init__(self, cardString: str, card: "classDiagram_UMLRole" = None, UMLCardinality: "classDiagram_UMLRole" = None):
        self.cardString = cardString
        self.card = card
        self.UMLCardinality = UMLCardinality
        
    @property
    def cardString(self) -> str:
        return self.__cardString

    @cardString.setter
    def cardString(self, cardString: str):
        self.__cardString = cardString

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLCardinality__card", None)
        self.__card = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLRole4"):
                opp_val = getattr(old_value, "UMLRole4", None)
                if opp_val == self:
                    setattr(old_value, "UMLRole4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLRole4"):
                opp_val = getattr(value, "UMLRole4", None)
                setattr(value, "UMLRole4", self)

    @property
    def UMLCardinality(self):
        return self.__UMLCardinality

    @UMLCardinality.setter
    def UMLCardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLCardinality__UMLCardinality", None)
        self.__UMLCardinality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revCard"):
                opp_val = getattr(old_value, "revCard", None)
                if opp_val == self:
                    setattr(old_value, "revCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revCard"):
                opp_val = getattr(value, "revCard", None)
                setattr(value, "revCard", self)

class classDiagram_UMLRole(UMLIncrement):

    def __init__(self, adornment: str, UMLRole: "classDiagram_UMLAssoc" = None, UMLRole2: "classDiagram_UMLAssoc" = None, UMLRole4: "classDiagram_UMLCardinality" = None, UMLRole7: "classDiagram_UMLClass" = None, roles: "classDiagram_UMLClass" = None, revCard: "classDiagram_UMLCardinality" = None, leftRole: "classDiagram_UMLAssoc" = None, rightRole: "classDiagram_UMLAssoc" = None):
        self.adornment = adornment
        self.UMLRole = UMLRole
        self.UMLRole2 = UMLRole2
        self.UMLRole4 = UMLRole4
        self.UMLRole7 = UMLRole7
        self.roles = roles
        self.revCard = revCard
        self.leftRole = leftRole
        self.rightRole = rightRole
        
    @property
    def adornment(self) -> str:
        return self.__adornment

    @adornment.setter
    def adornment(self, adornment: str):
        self.__adornment = adornment

    @property
    def UMLRole4(self):
        return self.__UMLRole4

    @UMLRole4.setter
    def UMLRole4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__UMLRole4", None)
        self.__UMLRole4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card"):
                opp_val = getattr(old_value, "card", None)
                if opp_val == self:
                    setattr(old_value, "card", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card"):
                opp_val = getattr(value, "card", None)
                setattr(value, "card", self)

    @property
    def rightRole(self):
        return self.__rightRole

    @rightRole.setter
    def rightRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__rightRole", None)
        self.__rightRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLAssoc13"):
                opp_val = getattr(old_value, "UMLAssoc13", None)
                if opp_val == self:
                    setattr(old_value, "UMLAssoc13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLAssoc13"):
                opp_val = getattr(value, "UMLAssoc13", None)
                setattr(value, "UMLAssoc13", self)

    @property
    def UMLRole7(self):
        return self.__UMLRole7

    @UMLRole7.setter
    def UMLRole7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__UMLRole7", None)
        self.__UMLRole7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UMLRole2(self):
        return self.__UMLRole2

    @UMLRole2.setter
    def UMLRole2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__UMLRole2", None)
        self.__UMLRole2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revRightRole"):
                opp_val = getattr(old_value, "revRightRole", None)
                if opp_val == self:
                    setattr(old_value, "revRightRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revRightRole"):
                opp_val = getattr(value, "revRightRole", None)
                setattr(value, "revRightRole", self)

    @property
    def UMLRole(self):
        return self.__UMLRole

    @UMLRole.setter
    def UMLRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__UMLRole", None)
        self.__UMLRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "revLeftRole"):
                opp_val = getattr(old_value, "revLeftRole", None)
                if opp_val == self:
                    setattr(old_value, "revLeftRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "revLeftRole"):
                opp_val = getattr(value, "revLeftRole", None)
                setattr(value, "revLeftRole", self)

    @property
    def leftRole(self):
        return self.__leftRole

    @leftRole.setter
    def leftRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__leftRole", None)
        self.__leftRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLAssoc"):
                opp_val = getattr(old_value, "UMLAssoc", None)
                if opp_val == self:
                    setattr(old_value, "UMLAssoc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLAssoc"):
                opp_val = getattr(value, "UMLAssoc", None)
                setattr(value, "UMLAssoc", self)

    @property
    def revCard(self):
        return self.__revCard

    @revCard.setter
    def revCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__revCard", None)
        self.__revCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLCardinality"):
                opp_val = getattr(old_value, "UMLCardinality", None)
                if opp_val == self:
                    setattr(old_value, "UMLCardinality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLCardinality"):
                opp_val = getattr(value, "UMLCardinality", None)
                setattr(value, "UMLCardinality", self)

    @property
    def roles(self):
        return self.__roles

    @roles.setter
    def roles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classDiagram_UMLRole__roles", None)
        self.__roles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLClass"):
                opp_val = getattr(old_value, "UMLClass", None)
                if opp_val == self:
                    setattr(old_value, "UMLClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLClass"):
                opp_val = getattr(value, "UMLClass", None)
                setattr(value, "UMLClass", self)

class UMLDiagramItem:

    pass
class classDiagram_UMLClass(UMLDiagramItem):

    pass
class classDiagram_UMLAssoc(UMLDiagramItem):

    pass