from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class adt_Operation:

    def __init__(self, name: str, adt_Operation21: "adt_ASort" = None, adt_Operation24: set["adt_ASort"] = None, adt_Operation32: "adt_Term" = None, adt_Operation: "adt_Signature" = None, adt_Operation13: "adt_Signature" = None, adt_Operation16: "adt_Signature" = None):
        self.name = name
        self.adt_Operation21 = adt_Operation21
        self.adt_Operation24 = adt_Operation24 if adt_Operation24 is not None else set()
        self.adt_Operation32 = adt_Operation32
        self.adt_Operation = adt_Operation
        self.adt_Operation13 = adt_Operation13
        self.adt_Operation16 = adt_Operation16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adt_Operation(self):
        return self.__adt_Operation

    @adt_Operation.setter
    def adt_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Operation__adt_Operation", None)
        self.__adt_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Signature7"):
                opp_val = getattr(old_value, "adt_Signature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Signature7"):
                opp_val = getattr(value, "adt_Signature7", None)
                if opp_val is None:
                    setattr(value, "adt_Signature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adt_Operation16(self):
        return self.__adt_Operation16

    @adt_Operation16.setter
    def adt_Operation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Operation__adt_Operation16", None)
        self.__adt_Operation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Signature15"):
                opp_val = getattr(old_value, "adt_Signature15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Signature15"):
                opp_val = getattr(value, "adt_Signature15", None)
                if opp_val is None:
                    setattr(value, "adt_Signature15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adt_Operation21(self):
        return self.__adt_Operation21

    @adt_Operation21.setter
    def adt_Operation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Operation__adt_Operation21", None)
        self.__adt_Operation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ASort22"):
                opp_val = getattr(old_value, "adt_ASort22", None)
                if opp_val == self:
                    setattr(old_value, "adt_ASort22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ASort22"):
                opp_val = getattr(value, "adt_ASort22", None)
                setattr(value, "adt_ASort22", self)

    @property
    def adt_Operation24(self):
        return self.__adt_Operation24

    @adt_Operation24.setter
    def adt_Operation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Operation__adt_Operation24", None)
        self.__adt_Operation24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adt_ASort25"):
                    opp_val = getattr(item, "adt_ASort25", None)
                    
                    if opp_val == self:
                        setattr(item, "adt_ASort25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adt_ASort25"):
                    opp_val = getattr(item, "adt_ASort25", None)
                    
                    setattr(item, "adt_ASort25", self)
                    

    @property
    def adt_Operation32(self):
        return self.__adt_Operation32

    @adt_Operation32.setter
    def adt_Operation32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Operation__adt_Operation32", None)
        self.__adt_Operation32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Term"):
                opp_val = getattr(old_value, "adt_Term", None)
                if opp_val == self:
                    setattr(old_value, "adt_Term", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Term"):
                opp_val = getattr(value, "adt_Term", None)
                setattr(value, "adt_Term", self)

    @property
    def adt_Operation13(self):
        return self.__adt_Operation13

    @adt_Operation13.setter
    def adt_Operation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Operation__adt_Operation13", None)
        self.__adt_Operation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Signature12"):
                opp_val = getattr(old_value, "adt_Signature12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Signature12"):
                opp_val = getattr(value, "adt_Signature12", None)
                if opp_val is None:
                    setattr(value, "adt_Signature12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ATerm:

    pass
class adt_Variable(ATerm):

    pass
class adt_Term(ATerm):

    pass
class adt_ATerm(ABC):

    def __init__(self, symbol: str, adt_ATerm: "adt_ADT" = None, adt_ATerm29: "adt_ASort" = None, adt_ATerm35: "adt_Term" = None, adt_ATerm40: "adt_Equation" = None, adt_ATerm43: "adt_Equation" = None):
        self.symbol = symbol
        self.adt_ATerm = adt_ATerm
        self.adt_ATerm29 = adt_ATerm29
        self.adt_ATerm35 = adt_ATerm35
        self.adt_ATerm40 = adt_ATerm40
        self.adt_ATerm43 = adt_ATerm43
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def adt_ATerm40(self):
        return self.__adt_ATerm40

    @adt_ATerm40.setter
    def adt_ATerm40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ATerm__adt_ATerm40", None)
        self.__adt_ATerm40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Equation39"):
                opp_val = getattr(old_value, "adt_Equation39", None)
                if opp_val == self:
                    setattr(old_value, "adt_Equation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Equation39"):
                opp_val = getattr(value, "adt_Equation39", None)
                setattr(value, "adt_Equation39", self)

    @property
    def adt_ATerm43(self):
        return self.__adt_ATerm43

    @adt_ATerm43.setter
    def adt_ATerm43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ATerm__adt_ATerm43", None)
        self.__adt_ATerm43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Equation42"):
                opp_val = getattr(old_value, "adt_Equation42", None)
                if opp_val == self:
                    setattr(old_value, "adt_Equation42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Equation42"):
                opp_val = getattr(value, "adt_Equation42", None)
                setattr(value, "adt_Equation42", self)

    @property
    def adt_ATerm29(self):
        return self.__adt_ATerm29

    @adt_ATerm29.setter
    def adt_ATerm29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ATerm__adt_ATerm29", None)
        self.__adt_ATerm29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ASort30"):
                opp_val = getattr(old_value, "adt_ASort30", None)
                if opp_val == self:
                    setattr(old_value, "adt_ASort30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ASort30"):
                opp_val = getattr(value, "adt_ASort30", None)
                setattr(value, "adt_ASort30", self)

    @property
    def adt_ATerm(self):
        return self.__adt_ATerm

    @adt_ATerm.setter
    def adt_ATerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ATerm__adt_ATerm", None)
        self.__adt_ATerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ADT27"):
                opp_val = getattr(old_value, "adt_ADT27", None)
                if opp_val == self:
                    setattr(old_value, "adt_ADT27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ADT27"):
                opp_val = getattr(value, "adt_ADT27", None)
                setattr(value, "adt_ADT27", self)

    @property
    def adt_ATerm35(self):
        return self.__adt_ATerm35

    @adt_ATerm35.setter
    def adt_ATerm35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ATerm__adt_ATerm35", None)
        self.__adt_ATerm35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Term34"):
                opp_val = getattr(old_value, "adt_Term34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Term34"):
                opp_val = getattr(value, "adt_Term34", None)
                if opp_val is None:
                    setattr(value, "adt_Term34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ASort:

    pass
class adt_Sort(ASort):

    pass
class adt_SubSort(ASort):

    pass
class adt_ASort(ABC):

    def __init__(self, name: str, adt_ASort: "adt_SubSort" = None, adt_ASort19: "adt_VariableDeclaration" = None, adt_ASort22: "adt_Operation" = None, adt_ASort25: "adt_Operation" = None, adt_ASort30: "adt_ATerm" = None, adt_ASort10: "adt_Signature" = None):
        self.name = name
        self.adt_ASort = adt_ASort
        self.adt_ASort19 = adt_ASort19
        self.adt_ASort22 = adt_ASort22
        self.adt_ASort25 = adt_ASort25
        self.adt_ASort30 = adt_ASort30
        self.adt_ASort10 = adt_ASort10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adt_ASort19(self):
        return self.__adt_ASort19

    @adt_ASort19.setter
    def adt_ASort19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ASort__adt_ASort19", None)
        self.__adt_ASort19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_VariableDeclaration18"):
                opp_val = getattr(old_value, "adt_VariableDeclaration18", None)
                if opp_val == self:
                    setattr(old_value, "adt_VariableDeclaration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_VariableDeclaration18"):
                opp_val = getattr(value, "adt_VariableDeclaration18", None)
                setattr(value, "adt_VariableDeclaration18", self)

    @property
    def adt_ASort30(self):
        return self.__adt_ASort30

    @adt_ASort30.setter
    def adt_ASort30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ASort__adt_ASort30", None)
        self.__adt_ASort30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ATerm29"):
                opp_val = getattr(old_value, "adt_ATerm29", None)
                if opp_val == self:
                    setattr(old_value, "adt_ATerm29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ATerm29"):
                opp_val = getattr(value, "adt_ATerm29", None)
                setattr(value, "adt_ATerm29", self)

    @property
    def adt_ASort22(self):
        return self.__adt_ASort22

    @adt_ASort22.setter
    def adt_ASort22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ASort__adt_ASort22", None)
        self.__adt_ASort22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Operation21"):
                opp_val = getattr(old_value, "adt_Operation21", None)
                if opp_val == self:
                    setattr(old_value, "adt_Operation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Operation21"):
                opp_val = getattr(value, "adt_Operation21", None)
                setattr(value, "adt_Operation21", self)

    @property
    def adt_ASort10(self):
        return self.__adt_ASort10

    @adt_ASort10.setter
    def adt_ASort10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ASort__adt_ASort10", None)
        self.__adt_ASort10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Signature9"):
                opp_val = getattr(old_value, "adt_Signature9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Signature9"):
                opp_val = getattr(value, "adt_Signature9", None)
                if opp_val is None:
                    setattr(value, "adt_Signature9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def adt_ASort(self):
        return self.__adt_ASort

    @adt_ASort.setter
    def adt_ASort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ASort__adt_ASort", None)
        self.__adt_ASort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_SubSort"):
                opp_val = getattr(old_value, "adt_SubSort", None)
                if opp_val == self:
                    setattr(old_value, "adt_SubSort", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_SubSort"):
                opp_val = getattr(value, "adt_SubSort", None)
                setattr(value, "adt_SubSort", self)

    @property
    def adt_ASort25(self):
        return self.__adt_ASort25

    @adt_ASort25.setter
    def adt_ASort25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ASort__adt_ASort25", None)
        self.__adt_ASort25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Operation24"):
                opp_val = getattr(old_value, "adt_Operation24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Operation24"):
                opp_val = getattr(value, "adt_Operation24", None)
                if opp_val is None:
                    setattr(value, "adt_Operation24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isSubSortOf(self, sort: str) -> bool:
        # TODO: Implement isSubSortOf method
        pass

class adt_Equation:

    pass
class adt_VariableDeclaration:

    def __init__(self, name: str, adt_VariableDeclaration: "adt_ADT" = None, adt_VariableDeclaration18: "adt_ASort" = None, adt_VariableDeclaration37: "adt_Variable" = None):
        self.name = name
        self.adt_VariableDeclaration = adt_VariableDeclaration
        self.adt_VariableDeclaration18 = adt_VariableDeclaration18
        self.adt_VariableDeclaration37 = adt_VariableDeclaration37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adt_VariableDeclaration18(self):
        return self.__adt_VariableDeclaration18

    @adt_VariableDeclaration18.setter
    def adt_VariableDeclaration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_VariableDeclaration__adt_VariableDeclaration18", None)
        self.__adt_VariableDeclaration18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ASort19"):
                opp_val = getattr(old_value, "adt_ASort19", None)
                if opp_val == self:
                    setattr(old_value, "adt_ASort19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ASort19"):
                opp_val = getattr(value, "adt_ASort19", None)
                setattr(value, "adt_ASort19", self)

    @property
    def adt_VariableDeclaration37(self):
        return self.__adt_VariableDeclaration37

    @adt_VariableDeclaration37.setter
    def adt_VariableDeclaration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_VariableDeclaration__adt_VariableDeclaration37", None)
        self.__adt_VariableDeclaration37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Variable"):
                opp_val = getattr(old_value, "adt_Variable", None)
                if opp_val == self:
                    setattr(old_value, "adt_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Variable"):
                opp_val = getattr(value, "adt_Variable", None)
                setattr(value, "adt_Variable", self)

    @property
    def adt_VariableDeclaration(self):
        return self.__adt_VariableDeclaration

    @adt_VariableDeclaration.setter
    def adt_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_VariableDeclaration__adt_VariableDeclaration", None)
        self.__adt_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ADT2"):
                opp_val = getattr(old_value, "adt_ADT2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ADT2"):
                opp_val = getattr(value, "adt_ADT2", None)
                if opp_val is None:
                    setattr(value, "adt_ADT2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class adt_Signature:

    def __init__(self, ops: str, adt_Signature: "adt_ADT" = None, adt_Signature7: set["adt_Operation"] = None, adt_Signature9: set["adt_ASort"] = None, adt_Signature12: set["adt_Operation"] = None, adt_Signature15: set["adt_Operation"] = None):
        self.ops = ops
        self.adt_Signature = adt_Signature
        self.adt_Signature7 = adt_Signature7 if adt_Signature7 is not None else set()
        self.adt_Signature9 = adt_Signature9 if adt_Signature9 is not None else set()
        self.adt_Signature12 = adt_Signature12 if adt_Signature12 is not None else set()
        self.adt_Signature15 = adt_Signature15 if adt_Signature15 is not None else set()
        
    @property
    def ops(self) -> str:
        return self.__ops

    @ops.setter
    def ops(self, ops: str):
        self.__ops = ops

    @property
    def adt_Signature15(self):
        return self.__adt_Signature15

    @adt_Signature15.setter
    def adt_Signature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Signature__adt_Signature15", None)
        self.__adt_Signature15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adt_Operation16"):
                    opp_val = getattr(item, "adt_Operation16", None)
                    
                    if opp_val == self:
                        setattr(item, "adt_Operation16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adt_Operation16"):
                    opp_val = getattr(item, "adt_Operation16", None)
                    
                    setattr(item, "adt_Operation16", self)
                    

    @property
    def adt_Signature(self):
        return self.__adt_Signature

    @adt_Signature.setter
    def adt_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Signature__adt_Signature", None)
        self.__adt_Signature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ADT"):
                opp_val = getattr(old_value, "adt_ADT", None)
                if opp_val == self:
                    setattr(old_value, "adt_ADT", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ADT"):
                opp_val = getattr(value, "adt_ADT", None)
                setattr(value, "adt_ADT", self)

    @property
    def adt_Signature7(self):
        return self.__adt_Signature7

    @adt_Signature7.setter
    def adt_Signature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Signature__adt_Signature7", None)
        self.__adt_Signature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adt_Operation"):
                    opp_val = getattr(item, "adt_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "adt_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adt_Operation"):
                    opp_val = getattr(item, "adt_Operation", None)
                    
                    setattr(item, "adt_Operation", self)
                    

    @property
    def adt_Signature9(self):
        return self.__adt_Signature9

    @adt_Signature9.setter
    def adt_Signature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Signature__adt_Signature9", None)
        self.__adt_Signature9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adt_ASort10"):
                    opp_val = getattr(item, "adt_ASort10", None)
                    
                    if opp_val == self:
                        setattr(item, "adt_ASort10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adt_ASort10"):
                    opp_val = getattr(item, "adt_ASort10", None)
                    
                    setattr(item, "adt_ASort10", self)
                    

    @property
    def adt_Signature12(self):
        return self.__adt_Signature12

    @adt_Signature12.setter
    def adt_Signature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_Signature__adt_Signature12", None)
        self.__adt_Signature12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adt_Operation13"):
                    opp_val = getattr(item, "adt_Operation13", None)
                    
                    if opp_val == self:
                        setattr(item, "adt_Operation13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adt_Operation13"):
                    opp_val = getattr(item, "adt_Operation13", None)
                    
                    setattr(item, "adt_Operation13", self)
                    

class adt_ADT:

    def __init__(self, name: str, adt_ADT: "adt_Signature" = None, adt_ADT2: set["adt_VariableDeclaration"] = None, adt_ADT4: set["adt_Equation"] = None, adt_ADT27: "adt_ATerm" = None):
        self.name = name
        self.adt_ADT = adt_ADT
        self.adt_ADT2 = adt_ADT2 if adt_ADT2 is not None else set()
        self.adt_ADT4 = adt_ADT4 if adt_ADT4 is not None else set()
        self.adt_ADT27 = adt_ADT27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def adt_ADT27(self):
        return self.__adt_ADT27

    @adt_ADT27.setter
    def adt_ADT27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ADT__adt_ADT27", None)
        self.__adt_ADT27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_ATerm"):
                opp_val = getattr(old_value, "adt_ATerm", None)
                if opp_val == self:
                    setattr(old_value, "adt_ATerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_ATerm"):
                opp_val = getattr(value, "adt_ATerm", None)
                setattr(value, "adt_ATerm", self)

    @property
    def adt_ADT2(self):
        return self.__adt_ADT2

    @adt_ADT2.setter
    def adt_ADT2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ADT__adt_ADT2", None)
        self.__adt_ADT2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adt_VariableDeclaration"):
                    opp_val = getattr(item, "adt_VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "adt_VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adt_VariableDeclaration"):
                    opp_val = getattr(item, "adt_VariableDeclaration", None)
                    
                    setattr(item, "adt_VariableDeclaration", self)
                    

    @property
    def adt_ADT(self):
        return self.__adt_ADT

    @adt_ADT.setter
    def adt_ADT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ADT__adt_ADT", None)
        self.__adt_ADT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adt_Signature"):
                opp_val = getattr(old_value, "adt_Signature", None)
                if opp_val == self:
                    setattr(old_value, "adt_Signature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adt_Signature"):
                opp_val = getattr(value, "adt_Signature", None)
                setattr(value, "adt_Signature", self)

    @property
    def adt_ADT4(self):
        return self.__adt_ADT4

    @adt_ADT4.setter
    def adt_ADT4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_adt_ADT__adt_ADT4", None)
        self.__adt_ADT4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "adt_Equation"):
                    opp_val = getattr(item, "adt_Equation", None)
                    
                    if opp_val == self:
                        setattr(item, "adt_Equation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "adt_Equation"):
                    opp_val = getattr(item, "adt_Equation", None)
                    
                    setattr(item, "adt_Equation", self)
                    
