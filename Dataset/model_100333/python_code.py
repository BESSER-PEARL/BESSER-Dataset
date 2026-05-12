from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Label:

    pass
class OurPNVis_Sequence:

    pass
class StructuredLabel:

    pass
class Attribute:

    pass
class OurPNVis_ident(Label):

    def __init__(self, text: str, OurPNVis_ident: "OurPNVis_Arc" = None):
        self.text = text
        self.OurPNVis_ident = OurPNVis_ident
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def OurPNVis_ident(self):
        return self.__OurPNVis_ident

    @OurPNVis_ident.setter
    def OurPNVis_ident(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OurPNVis_ident__OurPNVis_ident", None)
        self.__OurPNVis_ident = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OurPNVis_Arc4"):
                opp_val = getattr(old_value, "OurPNVis_Arc4", None)
                if opp_val == self:
                    setattr(old_value, "OurPNVis_Arc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OurPNVis_Arc4"):
                opp_val = getattr(value, "OurPNVis_Arc4", None)
                setattr(value, "OurPNVis_Arc4", self)

class OurPNVis_KeepAnim(Attribute):

    def __init__(self, text: bool, OurPNVis_KeepAnim: "OurPNVis_Arc" = None):
        self.text = text
        self.OurPNVis_KeepAnim = OurPNVis_KeepAnim
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: bool):
        self.__text = text


    @property
    def OurPNVis_KeepAnim(self):
        return self.__OurPNVis_KeepAnim

    @OurPNVis_KeepAnim.setter
    def OurPNVis_KeepAnim(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OurPNVis_KeepAnim__OurPNVis_KeepAnim", None)
        self.__OurPNVis_KeepAnim = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OurPNVis_Arc2"):
                opp_val = getattr(old_value, "OurPNVis_Arc2", None)
                if opp_val == self:
                    setattr(old_value, "OurPNVis_Arc2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OurPNVis_Arc2"):
                opp_val = getattr(value, "OurPNVis_Arc2", None)
                setattr(value, "OurPNVis_Arc2", self)

class OurPNVis_Finished(Attribute):

    def __init__(self, text: bool, OurPNVis_Finished: "OurPNVis_Arc" = None):
        self.text = text
        self.OurPNVis_Finished = OurPNVis_Finished
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: bool):
        self.__text = text


    @property
    def OurPNVis_Finished(self):
        return self.__OurPNVis_Finished

    @OurPNVis_Finished.setter
    def OurPNVis_Finished(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OurPNVis_Finished__OurPNVis_Finished", None)
        self.__OurPNVis_Finished = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OurPNVis_Arc"):
                opp_val = getattr(old_value, "OurPNVis_Arc", None)
                if opp_val == self:
                    setattr(old_value, "OurPNVis_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OurPNVis_Arc"):
                opp_val = getattr(value, "OurPNVis_Arc", None)
                setattr(value, "OurPNVis_Arc", self)

class Arc:

    pass
class OurPNVis_Arc(Arc):

    pass
class PetriNetType:

    pass
class OurPNVis_PNVis(PetriNetType):

    pass
class Transition:

    pass
class OurPNVis_Transition(Transition):

    pass
class OurPNVis_Geometry(Label):

    def __init__(self, text: str, OurPNVis_Geometry: "OurPNVis_Place" = None):
        self.text = text
        self.OurPNVis_Geometry = OurPNVis_Geometry
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def OurPNVis_Geometry(self):
        return self.__OurPNVis_Geometry

    @OurPNVis_Geometry.setter
    def OurPNVis_Geometry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OurPNVis_Geometry__OurPNVis_Geometry", None)
        self.__OurPNVis_Geometry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OurPNVis_Place13"):
                opp_val = getattr(old_value, "OurPNVis_Place13", None)
                if opp_val == self:
                    setattr(old_value, "OurPNVis_Place13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OurPNVis_Place13"):
                opp_val = getattr(value, "OurPNVis_Place13", None)
                setattr(value, "OurPNVis_Place13", self)

class OurPNVis_Activities(StructuredLabel):

    pass
class OurPNVis_Shape(Attribute):

    def __init__(self, text: str, OurPNVis_Shape: "OurPNVis_Place" = None):
        self.text = text
        self.OurPNVis_Shape = OurPNVis_Shape
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def OurPNVis_Shape(self):
        return self.__OurPNVis_Shape

    @OurPNVis_Shape.setter
    def OurPNVis_Shape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OurPNVis_Shape__OurPNVis_Shape", None)
        self.__OurPNVis_Shape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OurPNVis_Place9"):
                opp_val = getattr(old_value, "OurPNVis_Place9", None)
                if opp_val == self:
                    setattr(old_value, "OurPNVis_Place9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OurPNVis_Place9"):
                opp_val = getattr(value, "OurPNVis_Place9", None)
                setattr(value, "OurPNVis_Place9", self)

class OurPNVis_CanChange(Attribute):

    def __init__(self, text: bool, OurPNVis_CanChange: "OurPNVis_Place" = None):
        self.text = text
        self.OurPNVis_CanChange = OurPNVis_CanChange
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: bool):
        self.__text = text


    @property
    def OurPNVis_CanChange(self):
        return self.__OurPNVis_CanChange

    @OurPNVis_CanChange.setter
    def OurPNVis_CanChange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OurPNVis_CanChange__OurPNVis_CanChange", None)
        self.__OurPNVis_CanChange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OurPNVis_Place7"):
                opp_val = getattr(old_value, "OurPNVis_Place7", None)
                if opp_val == self:
                    setattr(old_value, "OurPNVis_Place7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OurPNVis_Place7"):
                opp_val = getattr(value, "OurPNVis_Place7", None)
                setattr(value, "OurPNVis_Place7", self)

class OurPNVis_Tokens(Attribute):

    def __init__(self, text: str, OurPNVis_Tokens: "OurPNVis_Place" = None):
        self.text = text
        self.OurPNVis_Tokens = OurPNVis_Tokens
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def OurPNVis_Tokens(self):
        return self.__OurPNVis_Tokens

    @OurPNVis_Tokens.setter
    def OurPNVis_Tokens(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OurPNVis_Tokens__OurPNVis_Tokens", None)
        self.__OurPNVis_Tokens = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OurPNVis_Place"):
                opp_val = getattr(old_value, "OurPNVis_Place", None)
                if opp_val == self:
                    setattr(old_value, "OurPNVis_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OurPNVis_Place"):
                opp_val = getattr(value, "OurPNVis_Place", None)
                setattr(value, "OurPNVis_Place", self)

class Place:

    pass
class OurPNVis_Place(Place):

    pass