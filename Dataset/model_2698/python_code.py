from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ConceptA:

    pass
class democea_ConceptB(ConceptA):

    pass
class democea_ConceptA:

    pass
class democea_ConceptC:

    def __init__(self, value: int, democea_ConceptC: "democea_ConceptB" = None, democea_ConceptC2: "democea_ConceptB" = None):
        self.value = value
        self.democea_ConceptC = democea_ConceptC
        self.democea_ConceptC2 = democea_ConceptC2
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def democea_ConceptC2(self):
        return self.__democea_ConceptC2

    @democea_ConceptC2.setter
    def democea_ConceptC2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_democea_ConceptC__democea_ConceptC2", None)
        self.__democea_ConceptC2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "democea_ConceptB3"):
                opp_val = getattr(old_value, "democea_ConceptB3", None)
                if opp_val == self:
                    setattr(old_value, "democea_ConceptB3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "democea_ConceptB3"):
                opp_val = getattr(value, "democea_ConceptB3", None)
                setattr(value, "democea_ConceptB3", self)

    @property
    def democea_ConceptC(self):
        return self.__democea_ConceptC

    @democea_ConceptC.setter
    def democea_ConceptC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_democea_ConceptC__democea_ConceptC", None)
        self.__democea_ConceptC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "democea_ConceptB"):
                opp_val = getattr(old_value, "democea_ConceptB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "democea_ConceptB"):
                opp_val = getattr(value, "democea_ConceptB", None)
                if opp_val is None:
                    setattr(value, "democea_ConceptB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
