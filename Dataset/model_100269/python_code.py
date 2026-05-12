from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class extendedpetrinet_Animation:

    pass
class StructuredLabel:

    pass
class Label:

    pass
class Attribute:

    pass
class extendedpetrinet_GeometryLabel(Label):

    def __init__(self, text: str, extendedpetrinet_GeometryLabel: "extendedpetrinet_Place" = None):
        self.text = text
        self.extendedpetrinet_GeometryLabel = extendedpetrinet_GeometryLabel
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def extendedpetrinet_GeometryLabel(self):
        return self.__extendedpetrinet_GeometryLabel

    @extendedpetrinet_GeometryLabel.setter
    def extendedpetrinet_GeometryLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedpetrinet_GeometryLabel__extendedpetrinet_GeometryLabel", None)
        self.__extendedpetrinet_GeometryLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedpetrinet_Place9"):
                opp_val = getattr(old_value, "extendedpetrinet_Place9", None)
                if opp_val == self:
                    setattr(old_value, "extendedpetrinet_Place9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedpetrinet_Place9"):
                opp_val = getattr(value, "extendedpetrinet_Place9", None)
                setattr(value, "extendedpetrinet_Place9", self)

class extendedpetrinet_InputPlaceAppearance(Label):

    def __init__(self, text: str, extendedpetrinet_InputPlaceAppearance: "extendedpetrinet_Place" = None):
        self.text = text
        self.extendedpetrinet_InputPlaceAppearance = extendedpetrinet_InputPlaceAppearance
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def extendedpetrinet_InputPlaceAppearance(self):
        return self.__extendedpetrinet_InputPlaceAppearance

    @extendedpetrinet_InputPlaceAppearance.setter
    def extendedpetrinet_InputPlaceAppearance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedpetrinet_InputPlaceAppearance__extendedpetrinet_InputPlaceAppearance", None)
        self.__extendedpetrinet_InputPlaceAppearance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedpetrinet_Place7"):
                opp_val = getattr(old_value, "extendedpetrinet_Place7", None)
                if opp_val == self:
                    setattr(old_value, "extendedpetrinet_Place7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedpetrinet_Place7"):
                opp_val = getattr(value, "extendedpetrinet_Place7", None)
                setattr(value, "extendedpetrinet_Place7", self)

class extendedpetrinet_Token(Label):

    def __init__(self, text: str, extendedpetrinet_Token: "extendedpetrinet_Place" = None):
        self.text = text
        self.extendedpetrinet_Token = extendedpetrinet_Token
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def extendedpetrinet_Token(self):
        return self.__extendedpetrinet_Token

    @extendedpetrinet_Token.setter
    def extendedpetrinet_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedpetrinet_Token__extendedpetrinet_Token", None)
        self.__extendedpetrinet_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedpetrinet_Place5"):
                opp_val = getattr(old_value, "extendedpetrinet_Place5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedpetrinet_Place5"):
                opp_val = getattr(value, "extendedpetrinet_Place5", None)
                if opp_val is None:
                    setattr(value, "extendedpetrinet_Place5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extendedpetrinet_AnimationLabel(StructuredLabel):

    pass
class Place:

    pass
class extendedpetrinet_Place(Place):

    pass
class extendedpetrinet_Identity(Attribute):

    def __init__(self, text: int, extendedpetrinet_Identity: "extendedpetrinet_Arc" = None):
        self.text = text
        self.extendedpetrinet_Identity = extendedpetrinet_Identity
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: int):
        self.__text = text


    @property
    def extendedpetrinet_Identity(self):
        return self.__extendedpetrinet_Identity

    @extendedpetrinet_Identity.setter
    def extendedpetrinet_Identity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedpetrinet_Identity__extendedpetrinet_Identity", None)
        self.__extendedpetrinet_Identity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedpetrinet_Arc"):
                opp_val = getattr(old_value, "extendedpetrinet_Arc", None)
                if opp_val == self:
                    setattr(old_value, "extendedpetrinet_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedpetrinet_Arc"):
                opp_val = getattr(value, "extendedpetrinet_Arc", None)
                setattr(value, "extendedpetrinet_Arc", self)

class Arc:

    pass
class extendedpetrinet_Arc(Arc):

    pass
class PetriNetType:

    pass
class extendedpetrinet_ExtendedPetriNet(PetriNetType):

    pass
class extendedpetrinet_InteractiveInput(Attribute):

    def __init__(self, text: bool, extendedpetrinet_InteractiveInput: "extendedpetrinet_Place" = None):
        self.text = text
        self.extendedpetrinet_InteractiveInput = extendedpetrinet_InteractiveInput
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: bool):
        self.__text = text


    @property
    def extendedpetrinet_InteractiveInput(self):
        return self.__extendedpetrinet_InteractiveInput

    @extendedpetrinet_InteractiveInput.setter
    def extendedpetrinet_InteractiveInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extendedpetrinet_InteractiveInput__extendedpetrinet_InteractiveInput", None)
        self.__extendedpetrinet_InteractiveInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extendedpetrinet_Place"):
                opp_val = getattr(old_value, "extendedpetrinet_Place", None)
                if opp_val == self:
                    setattr(old_value, "extendedpetrinet_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extendedpetrinet_Place"):
                opp_val = getattr(value, "extendedpetrinet_Place", None)
                setattr(value, "extendedpetrinet_Place", self)
