from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class K:

    pass
class F:

    pass
class refinher_I(F, K):

    pass
class D:

    pass
class refinher_F(D):

    pass
class B:

    pass
class refinher_D(B):

    pass
class Named:

    pass
class refinher_E(Named):

    pass
class refinher_C(Named):

    pass
class refinher_G(Named):

    pass
class refinher_L(Named):

    pass
class refinher_H(Named):

    pass
class refinher_K(Named):

    pass
class refinher_B(Named):

    pass
class refinher_A:

    pass
class refinher_Named:

    def __init__(self, name: str, refinher_Named: "refinher_A" = None):
        self.name = name
        self.refinher_Named = refinher_Named
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def refinher_Named(self):
        return self.__refinher_Named

    @refinher_Named.setter
    def refinher_Named(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refinher_Named__refinher_Named", None)
        self.__refinher_Named = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinher_A4"):
                opp_val = getattr(old_value, "refinher_A4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinher_A4"):
                opp_val = getattr(value, "refinher_A4", None)
                if opp_val is None:
                    setattr(value, "refinher_A4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
