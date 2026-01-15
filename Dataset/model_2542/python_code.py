from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class content_W:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class W:

    pass
class content_M(W):

    pass
class content_J(W):

    def __init__(self, linkName: str, cardinality: int, content_J: "content_F" = None, content_J36: "content_H" = None):
        self.linkName = linkName
        self.cardinality = cardinality
        self.content_J = content_J
        self.content_J36 = content_J36
        
    @property
    def cardinality(self) -> int:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: int):
        self.__cardinality = cardinality

    @property
    def linkName(self) -> str:
        return self.__linkName

    @linkName.setter
    def linkName(self, linkName: str):
        self.__linkName = linkName

    @property
    def content_J36(self):
        return self.__content_J36

    @content_J36.setter
    def content_J36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_content_J__content_J36", None)
        self.__content_J36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "content_H37"):
                opp_val = getattr(old_value, "content_H37", None)
                if opp_val == self:
                    setattr(old_value, "content_H37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "content_H37"):
                opp_val = getattr(value, "content_H37", None)
                setattr(value, "content_H37", self)

    @property
    def content_J(self):
        return self.__content_J

    @content_J.setter
    def content_J(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_content_J__content_J", None)
        self.__content_J = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "content_F18"):
                opp_val = getattr(old_value, "content_F18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "content_F18"):
                opp_val = getattr(value, "content_F18", None)
                if opp_val is None:
                    setattr(value, "content_F18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class content_N(W):

    pass
class content_C(W):

    pass
class content_Q(W):

    pass
class content_B(W):

    pass
class content_P(W):

    pass
class content_R(W):

    pass
class content_I(W):

    pass
class content_H(W):

    pass
class content_G(W):

    pass
class content_A(W):

    pass
class content_E(W):

    pass
class content_F(W):

    pass
class content_D(W):

    pass