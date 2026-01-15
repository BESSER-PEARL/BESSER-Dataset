from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class kreq205_SObject(ABC):

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class kreq205_Llll:

    def __init__(self, d6: str, kreq205_Llll: "kreq205_Cccc" = None, kreq205_Llll46: "kreq205_Cccc" = None, kreq205_Llll49: "kreq205_Rqs" = None):
        self.d6 = d6
        self.kreq205_Llll = kreq205_Llll
        self.kreq205_Llll46 = kreq205_Llll46
        self.kreq205_Llll49 = kreq205_Llll49
        
    @property
    def d6(self) -> str:
        return self.__d6

    @d6.setter
    def d6(self, d6: str):
        self.__d6 = d6

    @property
    def kreq205_Llll46(self):
        return self.__kreq205_Llll46

    @kreq205_Llll46.setter
    def kreq205_Llll46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Llll__kreq205_Llll46", None)
        self.__kreq205_Llll46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Cccc47"):
                opp_val = getattr(old_value, "kreq205_Cccc47", None)
                if opp_val == self:
                    setattr(old_value, "kreq205_Cccc47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Cccc47"):
                opp_val = getattr(value, "kreq205_Cccc47", None)
                setattr(value, "kreq205_Cccc47", self)

    @property
    def kreq205_Llll49(self):
        return self.__kreq205_Llll49

    @kreq205_Llll49.setter
    def kreq205_Llll49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Llll__kreq205_Llll49", None)
        self.__kreq205_Llll49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Rqs50"):
                opp_val = getattr(old_value, "kreq205_Rqs50", None)
                if opp_val == self:
                    setattr(old_value, "kreq205_Rqs50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Rqs50"):
                opp_val = getattr(value, "kreq205_Rqs50", None)
                setattr(value, "kreq205_Rqs50", self)

    @property
    def kreq205_Llll(self):
        return self.__kreq205_Llll

    @kreq205_Llll.setter
    def kreq205_Llll(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Llll__kreq205_Llll", None)
        self.__kreq205_Llll = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Cccc44"):
                opp_val = getattr(old_value, "kreq205_Cccc44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Cccc44"):
                opp_val = getattr(value, "kreq205_Cccc44", None)
                if opp_val is None:
                    setattr(value, "kreq205_Cccc44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq205_Cccc:

    def __init__(self, de1: str, kreq205_Cccc: "kreq205_Bbbb" = None, Cccc: "kreq205_Rqs" = None, Cccc25: "kreq205_Ffff" = None, Cccc30: "kreq205_Ffff" = None, kreq205_Cccc32: set["kreq205_Rqs"] = None, spc: set["kreq205_Rqs"] = None, dmof: set["kreq205_Ffff"] = None, kreq205_Cccc40: "kreq205_Cccc" = None, kreq205_Cccc38: set["kreq205_Cccc"] = None, alto: set["kreq205_Ffff"] = None, kreq205_Cccc44: set["kreq205_Llll"] = None, kreq205_Cccc47: "kreq205_Llll" = None):
        self.de1 = de1
        self.kreq205_Cccc = kreq205_Cccc
        self.Cccc = Cccc
        self.Cccc25 = Cccc25
        self.Cccc30 = Cccc30
        self.kreq205_Cccc32 = kreq205_Cccc32 if kreq205_Cccc32 is not None else set()
        self.spc = spc if spc is not None else set()
        self.dmof = dmof if dmof is not None else set()
        self.kreq205_Cccc40 = kreq205_Cccc40
        self.kreq205_Cccc38 = kreq205_Cccc38 if kreq205_Cccc38 is not None else set()
        self.alto = alto if alto is not None else set()
        self.kreq205_Cccc44 = kreq205_Cccc44 if kreq205_Cccc44 is not None else set()
        self.kreq205_Cccc47 = kreq205_Cccc47
        
    @property
    def de1(self) -> str:
        return self.__de1

    @de1.setter
    def de1(self, de1: str):
        self.__de1 = de1

    @property
    def kreq205_Cccc(self):
        return self.__kreq205_Cccc

    @kreq205_Cccc.setter
    def kreq205_Cccc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__kreq205_Cccc", None)
        self.__kreq205_Cccc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Bbbb4"):
                opp_val = getattr(old_value, "kreq205_Bbbb4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Bbbb4"):
                opp_val = getattr(value, "kreq205_Bbbb4", None)
                if opp_val is None:
                    setattr(value, "kreq205_Bbbb4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Cccc38(self):
        return self.__kreq205_Cccc38

    @kreq205_Cccc38.setter
    def kreq205_Cccc38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__kreq205_Cccc38", None)
        self.__kreq205_Cccc38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Cccc40"):
                    opp_val = getattr(item, "kreq205_Cccc40", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Cccc40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Cccc40"):
                    opp_val = getattr(item, "kreq205_Cccc40", None)
                    
                    setattr(item, "kreq205_Cccc40", self)
                    

    @property
    def kreq205_Cccc32(self):
        return self.__kreq205_Cccc32

    @kreq205_Cccc32.setter
    def kreq205_Cccc32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__kreq205_Cccc32", None)
        self.__kreq205_Cccc32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Rqs33"):
                    opp_val = getattr(item, "kreq205_Rqs33", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Rqs33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Rqs33"):
                    opp_val = getattr(item, "kreq205_Rqs33", None)
                    
                    setattr(item, "kreq205_Rqs33", self)
                    

    @property
    def dmof(self):
        return self.__dmof

    @dmof.setter
    def dmof(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__dmof", None)
        self.__dmof = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ffff37"):
                    opp_val = getattr(item, "Ffff37", None)
                    
                    if opp_val == self:
                        setattr(item, "Ffff37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ffff37"):
                    opp_val = getattr(item, "Ffff37", None)
                    
                    setattr(item, "Ffff37", self)
                    

    @property
    def Cccc30(self):
        return self.__Cccc30

    @Cccc30.setter
    def Cccc30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__Cccc30", None)
        self.__Cccc30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "impf"):
                opp_val = getattr(old_value, "impf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "impf"):
                opp_val = getattr(value, "impf", None)
                if opp_val is None:
                    setattr(value, "impf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__alto", None)
        self.__alto = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ffff42"):
                    opp_val = getattr(item, "Ffff42", None)
                    
                    if opp_val == self:
                        setattr(item, "Ffff42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ffff42"):
                    opp_val = getattr(item, "Ffff42", None)
                    
                    setattr(item, "Ffff42", self)
                    

    @property
    def kreq205_Cccc47(self):
        return self.__kreq205_Cccc47

    @kreq205_Cccc47.setter
    def kreq205_Cccc47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__kreq205_Cccc47", None)
        self.__kreq205_Cccc47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Llll46"):
                opp_val = getattr(old_value, "kreq205_Llll46", None)
                if opp_val == self:
                    setattr(old_value, "kreq205_Llll46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Llll46"):
                opp_val = getattr(value, "kreq205_Llll46", None)
                setattr(value, "kreq205_Llll46", self)

    @property
    def kreq205_Cccc44(self):
        return self.__kreq205_Cccc44

    @kreq205_Cccc44.setter
    def kreq205_Cccc44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__kreq205_Cccc44", None)
        self.__kreq205_Cccc44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Llll"):
                    opp_val = getattr(item, "kreq205_Llll", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Llll", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Llll"):
                    opp_val = getattr(item, "kreq205_Llll", None)
                    
                    setattr(item, "kreq205_Llll", self)
                    

    @property
    def spc(self):
        return self.__spc

    @spc.setter
    def spc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__spc", None)
        self.__spc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rqs35"):
                    opp_val = getattr(item, "Rqs35", None)
                    
                    if opp_val == self:
                        setattr(item, "Rqs35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rqs35"):
                    opp_val = getattr(item, "Rqs35", None)
                    
                    setattr(item, "Rqs35", self)
                    

    @property
    def Cccc25(self):
        return self.__Cccc25

    @Cccc25.setter
    def Cccc25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__Cccc25", None)
        self.__Cccc25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pfrmis"):
                opp_val = getattr(old_value, "pfrmis", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pfrmis"):
                opp_val = getattr(value, "pfrmis", None)
                if opp_val is None:
                    setattr(value, "pfrmis", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Cccc40(self):
        return self.__kreq205_Cccc40

    @kreq205_Cccc40.setter
    def kreq205_Cccc40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__kreq205_Cccc40", None)
        self.__kreq205_Cccc40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Cccc38"):
                opp_val = getattr(old_value, "kreq205_Cccc38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Cccc38"):
                opp_val = getattr(value, "kreq205_Cccc38", None)
                if opp_val is None:
                    setattr(value, "kreq205_Cccc38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Cccc(self):
        return self.__Cccc

    @Cccc.setter
    def Cccc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Cccc__Cccc", None)
        self.__Cccc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specifiedBy"):
                opp_val = getattr(old_value, "specifiedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specifiedBy"):
                opp_val = getattr(value, "specifiedBy", None)
                if opp_val is None:
                    setattr(value, "specifiedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SObject:

    pass
class kreq205_Rqs(SObject):

    def __init__(self, d2: str, a: bool, kreq205_Rqs: "kreq205_Rrrr" = None, Rqs: "kreq205_Tttt" = None, rqs: set["kreq205_Tttt"] = None, kreq205_Rqs13: "kreq205_Rqs" = None, kreq205_Rqs11: set["kreq205_Rqs"] = None, kreq205_Rqs16: "kreq205_Rqs" = None, kreq205_Rqs14: set["kreq205_Rqs"] = None, kreq205_Rqs20: "kreq205_Rqs" = None, kreq205_Rqs18: set["kreq205_Rqs"] = None, specifiedBy: set["kreq205_Cccc"] = None, Rqs23: "kreq205_Ffff" = None, isBy: set["kreq205_Ffff"] = None, kreq205_Rqs33: "kreq205_Cccc" = None, Rqs35: "kreq205_Cccc" = None, kreq205_Rqs50: "kreq205_Llll" = None):
        self.d2 = d2
        self.a = a
        self.kreq205_Rqs = kreq205_Rqs
        self.Rqs = Rqs
        self.rqs = rqs if rqs is not None else set()
        self.kreq205_Rqs13 = kreq205_Rqs13
        self.kreq205_Rqs11 = kreq205_Rqs11 if kreq205_Rqs11 is not None else set()
        self.kreq205_Rqs16 = kreq205_Rqs16
        self.kreq205_Rqs14 = kreq205_Rqs14 if kreq205_Rqs14 is not None else set()
        self.kreq205_Rqs20 = kreq205_Rqs20
        self.kreq205_Rqs18 = kreq205_Rqs18 if kreq205_Rqs18 is not None else set()
        self.specifiedBy = specifiedBy if specifiedBy is not None else set()
        self.Rqs23 = Rqs23
        self.isBy = isBy if isBy is not None else set()
        self.kreq205_Rqs33 = kreq205_Rqs33
        self.Rqs35 = Rqs35
        self.kreq205_Rqs50 = kreq205_Rqs50
        
    @property
    def d2(self) -> str:
        return self.__d2

    @d2.setter
    def d2(self, d2: str):
        self.__d2 = d2

    @property
    def a(self) -> bool:
        return self.__a

    @a.setter
    def a(self, a: bool):
        self.__a = a

    @property
    def isBy(self):
        return self.__isBy

    @isBy.setter
    def isBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__isBy", None)
        self.__isBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ffff"):
                    opp_val = getattr(item, "Ffff", None)
                    
                    if opp_val == self:
                        setattr(item, "Ffff", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ffff"):
                    opp_val = getattr(item, "Ffff", None)
                    
                    setattr(item, "Ffff", self)
                    

    @property
    def kreq205_Rqs16(self):
        return self.__kreq205_Rqs16

    @kreq205_Rqs16.setter
    def kreq205_Rqs16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs16", None)
        self.__kreq205_Rqs16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Rqs14"):
                opp_val = getattr(old_value, "kreq205_Rqs14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Rqs14"):
                opp_val = getattr(value, "kreq205_Rqs14", None)
                if opp_val is None:
                    setattr(value, "kreq205_Rqs14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Rqs50(self):
        return self.__kreq205_Rqs50

    @kreq205_Rqs50.setter
    def kreq205_Rqs50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs50", None)
        self.__kreq205_Rqs50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Llll49"):
                opp_val = getattr(old_value, "kreq205_Llll49", None)
                if opp_val == self:
                    setattr(old_value, "kreq205_Llll49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Llll49"):
                opp_val = getattr(value, "kreq205_Llll49", None)
                setattr(value, "kreq205_Llll49", self)

    @property
    def kreq205_Rqs18(self):
        return self.__kreq205_Rqs18

    @kreq205_Rqs18.setter
    def kreq205_Rqs18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs18", None)
        self.__kreq205_Rqs18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Rqs20"):
                    opp_val = getattr(item, "kreq205_Rqs20", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Rqs20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Rqs20"):
                    opp_val = getattr(item, "kreq205_Rqs20", None)
                    
                    setattr(item, "kreq205_Rqs20", self)
                    

    @property
    def kreq205_Rqs14(self):
        return self.__kreq205_Rqs14

    @kreq205_Rqs14.setter
    def kreq205_Rqs14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs14", None)
        self.__kreq205_Rqs14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Rqs16"):
                    opp_val = getattr(item, "kreq205_Rqs16", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Rqs16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Rqs16"):
                    opp_val = getattr(item, "kreq205_Rqs16", None)
                    
                    setattr(item, "kreq205_Rqs16", self)
                    

    @property
    def kreq205_Rqs13(self):
        return self.__kreq205_Rqs13

    @kreq205_Rqs13.setter
    def kreq205_Rqs13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs13", None)
        self.__kreq205_Rqs13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Rqs11"):
                opp_val = getattr(old_value, "kreq205_Rqs11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Rqs11"):
                opp_val = getattr(value, "kreq205_Rqs11", None)
                if opp_val is None:
                    setattr(value, "kreq205_Rqs11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rqs35(self):
        return self.__Rqs35

    @Rqs35.setter
    def Rqs35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__Rqs35", None)
        self.__Rqs35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spc"):
                opp_val = getattr(old_value, "spc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spc"):
                opp_val = getattr(value, "spc", None)
                if opp_val is None:
                    setattr(value, "spc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Rqs(self):
        return self.__kreq205_Rqs

    @kreq205_Rqs.setter
    def kreq205_Rqs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs", None)
        self.__kreq205_Rqs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Rrrr8"):
                opp_val = getattr(old_value, "kreq205_Rrrr8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Rrrr8"):
                opp_val = getattr(value, "kreq205_Rrrr8", None)
                if opp_val is None:
                    setattr(value, "kreq205_Rrrr8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rqs23(self):
        return self.__Rqs23

    @Rqs23.setter
    def Rqs23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__Rqs23", None)
        self.__Rqs23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specs"):
                opp_val = getattr(old_value, "specs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specs"):
                opp_val = getattr(value, "specs", None)
                if opp_val is None:
                    setattr(value, "specs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Rqs(self):
        return self.__Rqs

    @Rqs.setter
    def Rqs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__Rqs", None)
        self.__Rqs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rts"):
                opp_val = getattr(old_value, "rts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rts"):
                opp_val = getattr(value, "rts", None)
                if opp_val is None:
                    setattr(value, "rts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Rqs20(self):
        return self.__kreq205_Rqs20

    @kreq205_Rqs20.setter
    def kreq205_Rqs20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs20", None)
        self.__kreq205_Rqs20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Rqs18"):
                opp_val = getattr(old_value, "kreq205_Rqs18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Rqs18"):
                opp_val = getattr(value, "kreq205_Rqs18", None)
                if opp_val is None:
                    setattr(value, "kreq205_Rqs18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Rqs33(self):
        return self.__kreq205_Rqs33

    @kreq205_Rqs33.setter
    def kreq205_Rqs33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs33", None)
        self.__kreq205_Rqs33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Cccc32"):
                opp_val = getattr(old_value, "kreq205_Cccc32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Cccc32"):
                opp_val = getattr(value, "kreq205_Cccc32", None)
                if opp_val is None:
                    setattr(value, "kreq205_Cccc32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specifiedBy(self):
        return self.__specifiedBy

    @specifiedBy.setter
    def specifiedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__specifiedBy", None)
        self.__specifiedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cccc"):
                    opp_val = getattr(item, "Cccc", None)
                    
                    if opp_val == self:
                        setattr(item, "Cccc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cccc"):
                    opp_val = getattr(item, "Cccc", None)
                    
                    setattr(item, "Cccc", self)
                    

    @property
    def kreq205_Rqs11(self):
        return self.__kreq205_Rqs11

    @kreq205_Rqs11.setter
    def kreq205_Rqs11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__kreq205_Rqs11", None)
        self.__kreq205_Rqs11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Rqs13"):
                    opp_val = getattr(item, "kreq205_Rqs13", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Rqs13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Rqs13"):
                    opp_val = getattr(item, "kreq205_Rqs13", None)
                    
                    setattr(item, "kreq205_Rqs13", self)
                    

    @property
    def rqs(self):
        return self.__rqs

    @rqs.setter
    def rqs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rqs__rqs", None)
        self.__rqs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tttt"):
                    opp_val = getattr(item, "Tttt", None)
                    
                    if opp_val == self:
                        setattr(item, "Tttt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tttt"):
                    opp_val = getattr(item, "Tttt", None)
                    
                    setattr(item, "Tttt", self)
                    

class kreq205_Ffff:

    def __init__(self, d4: str, kreq205_Ffff: "kreq205_Bbbb" = None, specs: set["kreq205_Rqs"] = None, pfrmis: set["kreq205_Cccc"] = None, kreq205_Ffff28: "kreq205_Ffff" = None, kreq205_Ffff26: set["kreq205_Ffff"] = None, impf: set["kreq205_Cccc"] = None, Ffff: "kreq205_Rqs" = None, Ffff37: "kreq205_Cccc" = None, Ffff42: "kreq205_Cccc" = None):
        self.d4 = d4
        self.kreq205_Ffff = kreq205_Ffff
        self.specs = specs if specs is not None else set()
        self.pfrmis = pfrmis if pfrmis is not None else set()
        self.kreq205_Ffff28 = kreq205_Ffff28
        self.kreq205_Ffff26 = kreq205_Ffff26 if kreq205_Ffff26 is not None else set()
        self.impf = impf if impf is not None else set()
        self.Ffff = Ffff
        self.Ffff37 = Ffff37
        self.Ffff42 = Ffff42
        
    @property
    def d4(self) -> str:
        return self.__d4

    @d4.setter
    def d4(self, d4: str):
        self.__d4 = d4

    @property
    def specs(self):
        return self.__specs

    @specs.setter
    def specs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__specs", None)
        self.__specs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rqs23"):
                    opp_val = getattr(item, "Rqs23", None)
                    
                    if opp_val == self:
                        setattr(item, "Rqs23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rqs23"):
                    opp_val = getattr(item, "Rqs23", None)
                    
                    setattr(item, "Rqs23", self)
                    

    @property
    def kreq205_Ffff26(self):
        return self.__kreq205_Ffff26

    @kreq205_Ffff26.setter
    def kreq205_Ffff26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__kreq205_Ffff26", None)
        self.__kreq205_Ffff26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Ffff28"):
                    opp_val = getattr(item, "kreq205_Ffff28", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Ffff28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Ffff28"):
                    opp_val = getattr(item, "kreq205_Ffff28", None)
                    
                    setattr(item, "kreq205_Ffff28", self)
                    

    @property
    def kreq205_Ffff(self):
        return self.__kreq205_Ffff

    @kreq205_Ffff.setter
    def kreq205_Ffff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__kreq205_Ffff", None)
        self.__kreq205_Ffff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Bbbb6"):
                opp_val = getattr(old_value, "kreq205_Bbbb6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Bbbb6"):
                opp_val = getattr(value, "kreq205_Bbbb6", None)
                if opp_val is None:
                    setattr(value, "kreq205_Bbbb6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Ffff28(self):
        return self.__kreq205_Ffff28

    @kreq205_Ffff28.setter
    def kreq205_Ffff28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__kreq205_Ffff28", None)
        self.__kreq205_Ffff28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Ffff26"):
                opp_val = getattr(old_value, "kreq205_Ffff26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Ffff26"):
                opp_val = getattr(value, "kreq205_Ffff26", None)
                if opp_val is None:
                    setattr(value, "kreq205_Ffff26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def impf(self):
        return self.__impf

    @impf.setter
    def impf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__impf", None)
        self.__impf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cccc30"):
                    opp_val = getattr(item, "Cccc30", None)
                    
                    if opp_val == self:
                        setattr(item, "Cccc30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cccc30"):
                    opp_val = getattr(item, "Cccc30", None)
                    
                    setattr(item, "Cccc30", self)
                    

    @property
    def Ffff37(self):
        return self.__Ffff37

    @Ffff37.setter
    def Ffff37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__Ffff37", None)
        self.__Ffff37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmof"):
                opp_val = getattr(old_value, "dmof", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmof"):
                opp_val = getattr(value, "dmof", None)
                if opp_val is None:
                    setattr(value, "dmof", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pfrmis(self):
        return self.__pfrmis

    @pfrmis.setter
    def pfrmis(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__pfrmis", None)
        self.__pfrmis = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Cccc25"):
                    opp_val = getattr(item, "Cccc25", None)
                    
                    if opp_val == self:
                        setattr(item, "Cccc25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Cccc25"):
                    opp_val = getattr(item, "Cccc25", None)
                    
                    setattr(item, "Cccc25", self)
                    

    @property
    def Ffff(self):
        return self.__Ffff

    @Ffff.setter
    def Ffff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__Ffff", None)
        self.__Ffff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isBy"):
                opp_val = getattr(old_value, "isBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isBy"):
                opp_val = getattr(value, "isBy", None)
                if opp_val is None:
                    setattr(value, "isBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ffff42(self):
        return self.__Ffff42

    @Ffff42.setter
    def Ffff42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Ffff__Ffff42", None)
        self.__Ffff42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alto"):
                opp_val = getattr(old_value, "alto", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alto"):
                opp_val = getattr(value, "alto", None)
                if opp_val is None:
                    setattr(value, "alto", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq205_Tttt(SObject):

    pass
class kreq205_Rrrr:

    def __init__(self, d3: str, kreq205_Rrrr: "kreq205_Bbbb" = None, kreq205_Rrrr8: set["kreq205_Rqs"] = None):
        self.d3 = d3
        self.kreq205_Rrrr = kreq205_Rrrr
        self.kreq205_Rrrr8 = kreq205_Rrrr8 if kreq205_Rrrr8 is not None else set()
        
    @property
    def d3(self) -> str:
        return self.__d3

    @d3.setter
    def d3(self, d3: str):
        self.__d3 = d3

    @property
    def kreq205_Rrrr(self):
        return self.__kreq205_Rrrr

    @kreq205_Rrrr.setter
    def kreq205_Rrrr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rrrr__kreq205_Rrrr", None)
        self.__kreq205_Rrrr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq205_Bbbb"):
                opp_val = getattr(old_value, "kreq205_Bbbb", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq205_Bbbb"):
                opp_val = getattr(value, "kreq205_Bbbb", None)
                if opp_val is None:
                    setattr(value, "kreq205_Bbbb", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq205_Rrrr8(self):
        return self.__kreq205_Rrrr8

    @kreq205_Rrrr8.setter
    def kreq205_Rrrr8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq205_Rrrr__kreq205_Rrrr8", None)
        self.__kreq205_Rrrr8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq205_Rqs"):
                    opp_val = getattr(item, "kreq205_Rqs", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq205_Rqs", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq205_Rqs"):
                    opp_val = getattr(item, "kreq205_Rqs", None)
                    
                    setattr(item, "kreq205_Rqs", self)
                    

class kreq205_Bbbb:

    pass