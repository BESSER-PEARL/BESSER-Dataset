from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Tree:

    pass
class kwas_Leaf(Tree):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class kwas_Bin(Tree):

    pass
class kwas_Tree(ABC):

    def __init__(self, labelS: str, labelI: str, valsI: int, valsS: int, kwas_Tree: "kwas_Top" = None, kwas_Tree2: "kwas_Bin" = None, kwas_Tree5: "kwas_Bin" = None):
        self.labelS = labelS
        self.labelI = labelI
        self.valsI = valsI
        self.valsS = valsS
        self.kwas_Tree = kwas_Tree
        self.kwas_Tree2 = kwas_Tree2
        self.kwas_Tree5 = kwas_Tree5
        
    @property
    def valsI(self) -> int:
        return self.__valsI

    @valsI.setter
    def valsI(self, valsI: int):
        self.__valsI = valsI

    @property
    def labelS(self) -> str:
        return self.__labelS

    @labelS.setter
    def labelS(self, labelS: str):
        self.__labelS = labelS

    @property
    def valsS(self) -> int:
        return self.__valsS

    @valsS.setter
    def valsS(self, valsS: int):
        self.__valsS = valsS

    @property
    def labelI(self) -> str:
        return self.__labelI

    @labelI.setter
    def labelI(self, labelI: str):
        self.__labelI = labelI

    @property
    def kwas_Tree5(self):
        return self.__kwas_Tree5

    @kwas_Tree5.setter
    def kwas_Tree5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kwas_Tree__kwas_Tree5", None)
        self.__kwas_Tree5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kwas_Bin4"):
                opp_val = getattr(old_value, "kwas_Bin4", None)
                if opp_val == self:
                    setattr(old_value, "kwas_Bin4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kwas_Bin4"):
                opp_val = getattr(value, "kwas_Bin4", None)
                setattr(value, "kwas_Bin4", self)

    @property
    def kwas_Tree(self):
        return self.__kwas_Tree

    @kwas_Tree.setter
    def kwas_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kwas_Tree__kwas_Tree", None)
        self.__kwas_Tree = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kwas_Top"):
                opp_val = getattr(old_value, "kwas_Top", None)
                if opp_val == self:
                    setattr(old_value, "kwas_Top", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kwas_Top"):
                opp_val = getattr(value, "kwas_Top", None)
                setattr(value, "kwas_Top", self)

    @property
    def kwas_Tree2(self):
        return self.__kwas_Tree2

    @kwas_Tree2.setter
    def kwas_Tree2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kwas_Tree__kwas_Tree2", None)
        self.__kwas_Tree2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kwas_Bin"):
                opp_val = getattr(old_value, "kwas_Bin", None)
                if opp_val == self:
                    setattr(old_value, "kwas_Bin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kwas_Bin"):
                opp_val = getattr(value, "kwas_Bin", None)
                setattr(value, "kwas_Bin", self)

class kwas_Top:

    pass