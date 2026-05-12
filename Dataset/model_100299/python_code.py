from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Arc:

    pass
class petrinet_Arc(Arc):

    pass
class Attribute:

    pass
class petrinet_Identity(Attribute):

    def __init__(self, text: str, petrinet_Identity: "petrinet_Arc" = None):
        self.text = text
        self.petrinet_Identity = petrinet_Identity
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def petrinet_Identity(self):
        return self.__petrinet_Identity

    @petrinet_Identity.setter
    def petrinet_Identity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Identity__petrinet_Identity", None)
        self.__petrinet_Identity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc"):
                opp_val = getattr(old_value, "petrinet_Arc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc"):
                opp_val = getattr(value, "petrinet_Arc", None)
                setattr(value, "petrinet_Arc", self)

class petrinet_Animation:

    pass
class StructuredLabel:

    pass
class petrinet_AnimationLabel(StructuredLabel):

    pass
class Label:

    pass
class petrinet_InputPlace(Attribute):

    def __init__(self, text: bool, petrinet_InputPlace: "petrinet_Place" = None):
        self.text = text
        self.petrinet_InputPlace = petrinet_InputPlace
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: bool):
        self.__text = text


    @property
    def petrinet_InputPlace(self):
        return self.__petrinet_InputPlace

    @petrinet_InputPlace.setter
    def petrinet_InputPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_InputPlace__petrinet_InputPlace", None)
        self.__petrinet_InputPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Place6"):
                opp_val = getattr(old_value, "petrinet_Place6", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Place6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Place6"):
                opp_val = getattr(value, "petrinet_Place6", None)
                setattr(value, "petrinet_Place6", self)

class petrinet_Token(Attribute):

    def __init__(self, text: str, petrinet_Token: "petrinet_Place" = None):
        self.text = text
        self.petrinet_Token = petrinet_Token
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def petrinet_Token(self):
        return self.__petrinet_Token

    @petrinet_Token.setter
    def petrinet_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Token__petrinet_Token", None)
        self.__petrinet_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Place4"):
                opp_val = getattr(old_value, "petrinet_Place4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Place4"):
                opp_val = getattr(value, "petrinet_Place4", None)
                if opp_val is None:
                    setattr(value, "petrinet_Place4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_GeometryLabel(Label):

    def __init__(self, text: str, petrinet_GeometryLabel: "petrinet_Place" = None):
        self.text = text
        self.petrinet_GeometryLabel = petrinet_GeometryLabel
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def petrinet_GeometryLabel(self):
        return self.__petrinet_GeometryLabel

    @petrinet_GeometryLabel.setter
    def petrinet_GeometryLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_GeometryLabel__petrinet_GeometryLabel", None)
        self.__petrinet_GeometryLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Place"):
                opp_val = getattr(old_value, "petrinet_Place", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Place"):
                opp_val = getattr(value, "petrinet_Place", None)
                setattr(value, "petrinet_Place", self)

class Place:

    pass
class petrinet_Place(Place):

    pass
class PetriNetType:

    pass
class petrinet_ExtendedPetriNet(PetriNetType):

    pass