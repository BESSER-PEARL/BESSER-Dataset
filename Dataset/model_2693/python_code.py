from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ConceptA:

    pass
class test1_ConceptB(ConceptA):

    pass
class test1_ConceptC:

    def __init__(self, nbr: int, cool: bool, test1_ConceptC: "test1_ConceptA" = None):
        self.nbr = nbr
        self.cool = cool
        self.test1_ConceptC = test1_ConceptC
        
    @property
    def nbr(self) -> int:
        return self.__nbr

    @nbr.setter
    def nbr(self, nbr: int):
        self.__nbr = nbr

    @property
    def cool(self) -> bool:
        return self.__cool

    @cool.setter
    def cool(self, cool: bool):
        self.__cool = cool

    @property
    def test1_ConceptC(self):
        return self.__test1_ConceptC

    @test1_ConceptC.setter
    def test1_ConceptC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test1_ConceptC__test1_ConceptC", None)
        self.__test1_ConceptC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test1_ConceptA"):
                opp_val = getattr(old_value, "test1_ConceptA", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test1_ConceptA"):
                opp_val = getattr(value, "test1_ConceptA", None)
                if opp_val is None:
                    setattr(value, "test1_ConceptA", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test1_ConceptA:

    pass