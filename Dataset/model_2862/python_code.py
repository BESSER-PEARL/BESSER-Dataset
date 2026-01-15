from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class gDSL_Field:

    def __init__(self, name: str, gDSL_Field: "gDSL_AtomicExp" = None, gDSL_Field107: "gDSL_Exp" = None):
        self.name = name
        self.gDSL_Field = gDSL_Field
        self.gDSL_Field107 = gDSL_Field107
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gDSL_Field(self):
        return self.__gDSL_Field

    @gDSL_Field.setter
    def gDSL_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Field__gDSL_Field", None)
        self.__gDSL_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_AtomicExp97"):
                opp_val = getattr(old_value, "gDSL_AtomicExp97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_AtomicExp97"):
                opp_val = getattr(value, "gDSL_AtomicExp97", None)
                if opp_val is None:
                    setattr(value, "gDSL_AtomicExp97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_Field107(self):
        return self.__gDSL_Field107

    @gDSL_Field107.setter
    def gDSL_Field107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Field__gDSL_Field107", None)
        self.__gDSL_Field107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Exp108"):
                opp_val = getattr(old_value, "gDSL_Exp108", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Exp108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Exp108"):
                opp_val = getattr(value, "gDSL_Exp108", None)
                setattr(value, "gDSL_Exp108", self)

class ApplyExp:

    pass
class gDSL_Args:

    pass
class gDSL_AtomicExp(ApplyExp):

    def __init__(self, id: str, gDSL_AtomicExp99: "gDSL_Exp" = None, gDSL_AtomicExp102: set["gDSL_Exp"] = None, gDSL_AtomicExp105: set["gDSL_ValueDecl"] = None, gDSL_AtomicExp: "gDSL_ApplyExp" = None, gDSL_AtomicExp95: "gDSL_Args" = None, gDSL_AtomicExp97: set["gDSL_Field"] = None):
        self.id = id
        self.gDSL_AtomicExp99 = gDSL_AtomicExp99
        self.gDSL_AtomicExp102 = gDSL_AtomicExp102 if gDSL_AtomicExp102 is not None else set()
        self.gDSL_AtomicExp105 = gDSL_AtomicExp105 if gDSL_AtomicExp105 is not None else set()
        self.gDSL_AtomicExp = gDSL_AtomicExp
        self.gDSL_AtomicExp95 = gDSL_AtomicExp95
        self.gDSL_AtomicExp97 = gDSL_AtomicExp97 if gDSL_AtomicExp97 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def gDSL_AtomicExp99(self):
        return self.__gDSL_AtomicExp99

    @gDSL_AtomicExp99.setter
    def gDSL_AtomicExp99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AtomicExp__gDSL_AtomicExp99", None)
        self.__gDSL_AtomicExp99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Exp100"):
                opp_val = getattr(old_value, "gDSL_Exp100", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Exp100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Exp100"):
                opp_val = getattr(value, "gDSL_Exp100", None)
                setattr(value, "gDSL_Exp100", self)

    @property
    def gDSL_AtomicExp105(self):
        return self.__gDSL_AtomicExp105

    @gDSL_AtomicExp105.setter
    def gDSL_AtomicExp105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AtomicExp__gDSL_AtomicExp105", None)
        self.__gDSL_AtomicExp105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_ValueDecl"):
                    opp_val = getattr(item, "gDSL_ValueDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_ValueDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_ValueDecl"):
                    opp_val = getattr(item, "gDSL_ValueDecl", None)
                    
                    setattr(item, "gDSL_ValueDecl", self)
                    

    @property
    def gDSL_AtomicExp95(self):
        return self.__gDSL_AtomicExp95

    @gDSL_AtomicExp95.setter
    def gDSL_AtomicExp95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AtomicExp__gDSL_AtomicExp95", None)
        self.__gDSL_AtomicExp95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Args94"):
                opp_val = getattr(old_value, "gDSL_Args94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Args94"):
                opp_val = getattr(value, "gDSL_Args94", None)
                if opp_val is None:
                    setattr(value, "gDSL_Args94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_AtomicExp(self):
        return self.__gDSL_AtomicExp

    @gDSL_AtomicExp.setter
    def gDSL_AtomicExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AtomicExp__gDSL_AtomicExp", None)
        self.__gDSL_AtomicExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ApplyExp90"):
                opp_val = getattr(old_value, "gDSL_ApplyExp90", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ApplyExp90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ApplyExp90"):
                opp_val = getattr(value, "gDSL_ApplyExp90", None)
                setattr(value, "gDSL_ApplyExp90", self)

    @property
    def gDSL_AtomicExp102(self):
        return self.__gDSL_AtomicExp102

    @gDSL_AtomicExp102.setter
    def gDSL_AtomicExp102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AtomicExp__gDSL_AtomicExp102", None)
        self.__gDSL_AtomicExp102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_Exp103"):
                    opp_val = getattr(item, "gDSL_Exp103", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_Exp103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_Exp103"):
                    opp_val = getattr(item, "gDSL_Exp103", None)
                    
                    setattr(item, "gDSL_Exp103", self)
                    

    @property
    def gDSL_AtomicExp97(self):
        return self.__gDSL_AtomicExp97

    @gDSL_AtomicExp97.setter
    def gDSL_AtomicExp97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AtomicExp__gDSL_AtomicExp97", None)
        self.__gDSL_AtomicExp97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_Field"):
                    opp_val = getattr(item, "gDSL_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_Field"):
                    opp_val = getattr(item, "gDSL_Field", None)
                    
                    setattr(item, "gDSL_Field", self)
                    

class gDSL_ValueDecl:

    def __init__(self, name: str, ids: str, gDSL_ValueDecl: "gDSL_AtomicExp" = None, gDSL_ValueDecl110: "gDSL_Exp" = None):
        self.name = name
        self.ids = ids
        self.gDSL_ValueDecl = gDSL_ValueDecl
        self.gDSL_ValueDecl110 = gDSL_ValueDecl110
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gDSL_ValueDecl(self):
        return self.__gDSL_ValueDecl

    @gDSL_ValueDecl.setter
    def gDSL_ValueDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_ValueDecl__gDSL_ValueDecl", None)
        self.__gDSL_ValueDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_AtomicExp105"):
                opp_val = getattr(old_value, "gDSL_AtomicExp105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_AtomicExp105"):
                opp_val = getattr(value, "gDSL_AtomicExp105", None)
                if opp_val is None:
                    setattr(value, "gDSL_AtomicExp105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_ValueDecl110(self):
        return self.__gDSL_ValueDecl110

    @gDSL_ValueDecl110.setter
    def gDSL_ValueDecl110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_ValueDecl__gDSL_ValueDecl110", None)
        self.__gDSL_ValueDecl110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Exp111"):
                opp_val = getattr(old_value, "gDSL_Exp111", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Exp111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Exp111"):
                opp_val = getattr(value, "gDSL_Exp111", None)
                setattr(value, "gDSL_Exp111", self)

class AExp:

    pass
class gDSL_MExp(AExp):

    def __init__(self, sign: str, gDSL_MExp: "gDSL_MExp" = None, gDSL_MExp86: set["gDSL_MExp"] = None):
        self.sign = sign
        self.gDSL_MExp = gDSL_MExp
        self.gDSL_MExp86 = gDSL_MExp86 if gDSL_MExp86 is not None else set()
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def gDSL_MExp(self):
        return self.__gDSL_MExp

    @gDSL_MExp.setter
    def gDSL_MExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_MExp__gDSL_MExp", None)
        self.__gDSL_MExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_MExp86"):
                opp_val = getattr(old_value, "gDSL_MExp86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_MExp86"):
                opp_val = getattr(value, "gDSL_MExp86", None)
                if opp_val is None:
                    setattr(value, "gDSL_MExp86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_MExp86(self):
        return self.__gDSL_MExp86

    @gDSL_MExp86.setter
    def gDSL_MExp86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_MExp__gDSL_MExp86", None)
        self.__gDSL_MExp86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_MExp"):
                    opp_val = getattr(item, "gDSL_MExp", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_MExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_MExp"):
                    opp_val = getattr(item, "gDSL_MExp", None)
                    
                    setattr(item, "gDSL_MExp", self)
                    

class RExp:

    pass
class gDSL_AExp(RExp):

    def __init__(self, sym: str, gDSL_AExp: "gDSL_AExp" = None, gDSL_AExp84: set["gDSL_AExp"] = None):
        self.sym = sym
        self.gDSL_AExp = gDSL_AExp
        self.gDSL_AExp84 = gDSL_AExp84 if gDSL_AExp84 is not None else set()
        
    @property
    def sym(self) -> str:
        return self.__sym

    @sym.setter
    def sym(self, sym: str):
        self.__sym = sym

    @property
    def gDSL_AExp(self):
        return self.__gDSL_AExp

    @gDSL_AExp.setter
    def gDSL_AExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AExp__gDSL_AExp", None)
        self.__gDSL_AExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_AExp84"):
                opp_val = getattr(old_value, "gDSL_AExp84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_AExp84"):
                opp_val = getattr(value, "gDSL_AExp84", None)
                if opp_val is None:
                    setattr(value, "gDSL_AExp84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_AExp84(self):
        return self.__gDSL_AExp84

    @gDSL_AExp84.setter
    def gDSL_AExp84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_AExp__gDSL_AExp84", None)
        self.__gDSL_AExp84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_AExp"):
                    opp_val = getattr(item, "gDSL_AExp", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_AExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_AExp"):
                    opp_val = getattr(item, "gDSL_AExp", None)
                    
                    setattr(item, "gDSL_AExp", self)
                    

class AndAlsoExp:

    pass
class gDSL_RExp(AndAlsoExp):

    pass
class OrElseExp:

    pass
class SelectExp:

    pass
class gDSL_AndAlsoExp(OrElseExp):

    pass
class gDSL_ApplyExp(SelectExp):

    pass
class MExp:

    pass
class gDSL_SelectExp(MExp):

    def __init__(self, symbol: str, gDSL_SelectExp: set["gDSL_ApplyExp"] = None):
        self.symbol = symbol
        self.gDSL_SelectExp = gDSL_SelectExp if gDSL_SelectExp is not None else set()
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def gDSL_SelectExp(self):
        return self.__gDSL_SelectExp

    @gDSL_SelectExp.setter
    def gDSL_SelectExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_SelectExp__gDSL_SelectExp", None)
        self.__gDSL_SelectExp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_ApplyExp"):
                    opp_val = getattr(item, "gDSL_ApplyExp", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_ApplyExp", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_ApplyExp"):
                    opp_val = getattr(item, "gDSL_ApplyExp", None)
                    
                    setattr(item, "gDSL_ApplyExp", self)
                    

class CaseExp:

    pass
class gDSL_PAT:

    def __init__(self, uscore: str, int: str, id: str, bitpat: str, gDSL_PAT: "gDSL_CaseExp" = None, gDSL_PAT114: "gDSL_PAT" = None, gDSL_PAT112: "gDSL_PAT" = None):
        self.uscore = uscore
        self.int = int
        self.id = id
        self.bitpat = bitpat
        self.gDSL_PAT = gDSL_PAT
        self.gDSL_PAT114 = gDSL_PAT114
        self.gDSL_PAT112 = gDSL_PAT112
        
    @property
    def uscore(self) -> str:
        return self.__uscore

    @uscore.setter
    def uscore(self, uscore: str):
        self.__uscore = uscore

    @property
    def bitpat(self) -> str:
        return self.__bitpat

    @bitpat.setter
    def bitpat(self, bitpat: str):
        self.__bitpat = bitpat

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def int(self) -> str:
        return self.__int

    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def gDSL_PAT(self):
        return self.__gDSL_PAT

    @gDSL_PAT.setter
    def gDSL_PAT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_PAT__gDSL_PAT", None)
        self.__gDSL_PAT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_CaseExp62"):
                opp_val = getattr(old_value, "gDSL_CaseExp62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_CaseExp62"):
                opp_val = getattr(value, "gDSL_CaseExp62", None)
                if opp_val is None:
                    setattr(value, "gDSL_CaseExp62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_PAT112(self):
        return self.__gDSL_PAT112

    @gDSL_PAT112.setter
    def gDSL_PAT112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_PAT__gDSL_PAT112", None)
        self.__gDSL_PAT112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_PAT114"):
                opp_val = getattr(old_value, "gDSL_PAT114", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_PAT114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_PAT114"):
                opp_val = getattr(value, "gDSL_PAT114", None)
                setattr(value, "gDSL_PAT114", self)

    @property
    def gDSL_PAT114(self):
        return self.__gDSL_PAT114

    @gDSL_PAT114.setter
    def gDSL_PAT114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_PAT__gDSL_PAT114", None)
        self.__gDSL_PAT114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_PAT112"):
                opp_val = getattr(old_value, "gDSL_PAT112", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_PAT112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_PAT112"):
                opp_val = getattr(value, "gDSL_PAT112", None)
                setattr(value, "gDSL_PAT112", self)

class gDSL_ClosedExp(CaseExp):

    pass
class ClosedExp:

    pass
class gDSL_OrElseExp(ClosedExp):

    pass
class gDSL_MonadicExp:

    def __init__(self, name: str, gDSL_MonadicExp: "gDSL_ClosedExp" = None, gDSL_MonadicExp78: "gDSL_Exp" = None):
        self.name = name
        self.gDSL_MonadicExp = gDSL_MonadicExp
        self.gDSL_MonadicExp78 = gDSL_MonadicExp78
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gDSL_MonadicExp(self):
        return self.__gDSL_MonadicExp

    @gDSL_MonadicExp.setter
    def gDSL_MonadicExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_MonadicExp__gDSL_MonadicExp", None)
        self.__gDSL_MonadicExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ClosedExp76"):
                opp_val = getattr(old_value, "gDSL_ClosedExp76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ClosedExp76"):
                opp_val = getattr(value, "gDSL_ClosedExp76", None)
                if opp_val is None:
                    setattr(value, "gDSL_ClosedExp76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_MonadicExp78(self):
        return self.__gDSL_MonadicExp78

    @gDSL_MonadicExp78.setter
    def gDSL_MonadicExp78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_MonadicExp__gDSL_MonadicExp78", None)
        self.__gDSL_MonadicExp78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Exp79"):
                opp_val = getattr(old_value, "gDSL_Exp79", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Exp79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Exp79"):
                opp_val = getattr(value, "gDSL_Exp79", None)
                setattr(value, "gDSL_Exp79", self)

class gDSL_CaseExp:

    def __init__(self, name: str, gDSL_CaseExp: "gDSL_Exp" = None, gDSL_CaseExp58: "gDSL_Exp" = None, gDSL_CaseExp60: "gDSL_ClosedExp" = None, gDSL_CaseExp62: set["gDSL_PAT"] = None, gDSL_CaseExp64: set["gDSL_Exp"] = None, gDSL_CaseExp68: "gDSL_ClosedExp" = None, gDSL_CaseExp71: "gDSL_ClosedExp" = None, gDSL_CaseExp74: "gDSL_ClosedExp" = None):
        self.name = name
        self.gDSL_CaseExp = gDSL_CaseExp
        self.gDSL_CaseExp58 = gDSL_CaseExp58
        self.gDSL_CaseExp60 = gDSL_CaseExp60
        self.gDSL_CaseExp62 = gDSL_CaseExp62 if gDSL_CaseExp62 is not None else set()
        self.gDSL_CaseExp64 = gDSL_CaseExp64 if gDSL_CaseExp64 is not None else set()
        self.gDSL_CaseExp68 = gDSL_CaseExp68
        self.gDSL_CaseExp71 = gDSL_CaseExp71
        self.gDSL_CaseExp74 = gDSL_CaseExp74
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gDSL_CaseExp64(self):
        return self.__gDSL_CaseExp64

    @gDSL_CaseExp64.setter
    def gDSL_CaseExp64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp64", None)
        self.__gDSL_CaseExp64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_Exp65"):
                    opp_val = getattr(item, "gDSL_Exp65", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_Exp65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_Exp65"):
                    opp_val = getattr(item, "gDSL_Exp65", None)
                    
                    setattr(item, "gDSL_Exp65", self)
                    

    @property
    def gDSL_CaseExp71(self):
        return self.__gDSL_CaseExp71

    @gDSL_CaseExp71.setter
    def gDSL_CaseExp71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp71", None)
        self.__gDSL_CaseExp71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ClosedExp70"):
                opp_val = getattr(old_value, "gDSL_ClosedExp70", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ClosedExp70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ClosedExp70"):
                opp_val = getattr(value, "gDSL_ClosedExp70", None)
                setattr(value, "gDSL_ClosedExp70", self)

    @property
    def gDSL_CaseExp74(self):
        return self.__gDSL_CaseExp74

    @gDSL_CaseExp74.setter
    def gDSL_CaseExp74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp74", None)
        self.__gDSL_CaseExp74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ClosedExp73"):
                opp_val = getattr(old_value, "gDSL_ClosedExp73", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ClosedExp73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ClosedExp73"):
                opp_val = getattr(value, "gDSL_ClosedExp73", None)
                setattr(value, "gDSL_ClosedExp73", self)

    @property
    def gDSL_CaseExp60(self):
        return self.__gDSL_CaseExp60

    @gDSL_CaseExp60.setter
    def gDSL_CaseExp60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp60", None)
        self.__gDSL_CaseExp60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ClosedExp"):
                opp_val = getattr(old_value, "gDSL_ClosedExp", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ClosedExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ClosedExp"):
                opp_val = getattr(value, "gDSL_ClosedExp", None)
                setattr(value, "gDSL_ClosedExp", self)

    @property
    def gDSL_CaseExp62(self):
        return self.__gDSL_CaseExp62

    @gDSL_CaseExp62.setter
    def gDSL_CaseExp62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp62", None)
        self.__gDSL_CaseExp62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_PAT"):
                    opp_val = getattr(item, "gDSL_PAT", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_PAT", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_PAT"):
                    opp_val = getattr(item, "gDSL_PAT", None)
                    
                    setattr(item, "gDSL_PAT", self)
                    

    @property
    def gDSL_CaseExp58(self):
        return self.__gDSL_CaseExp58

    @gDSL_CaseExp58.setter
    def gDSL_CaseExp58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp58", None)
        self.__gDSL_CaseExp58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Exp57"):
                opp_val = getattr(old_value, "gDSL_Exp57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Exp57"):
                opp_val = getattr(value, "gDSL_Exp57", None)
                if opp_val is None:
                    setattr(value, "gDSL_Exp57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_CaseExp(self):
        return self.__gDSL_CaseExp

    @gDSL_CaseExp.setter
    def gDSL_CaseExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp", None)
        self.__gDSL_CaseExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Exp55"):
                opp_val = getattr(old_value, "gDSL_Exp55", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Exp55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Exp55"):
                opp_val = getattr(value, "gDSL_Exp55", None)
                setattr(value, "gDSL_Exp55", self)

    @property
    def gDSL_CaseExp68(self):
        return self.__gDSL_CaseExp68

    @gDSL_CaseExp68.setter
    def gDSL_CaseExp68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CaseExp__gDSL_CaseExp68", None)
        self.__gDSL_CaseExp68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ClosedExp67"):
                opp_val = getattr(old_value, "gDSL_ClosedExp67", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ClosedExp67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ClosedExp67"):
                opp_val = getattr(value, "gDSL_ClosedExp67", None)
                setattr(value, "gDSL_ClosedExp67", self)

class gDSL_TyBind:

    def __init__(self, name: str, gDSL_TyBind: "gDSL_Ty" = None, gDSL_TyBind49: "gDSL_Ty" = None):
        self.name = name
        self.gDSL_TyBind = gDSL_TyBind
        self.gDSL_TyBind49 = gDSL_TyBind49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gDSL_TyBind49(self):
        return self.__gDSL_TyBind49

    @gDSL_TyBind49.setter
    def gDSL_TyBind49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_TyBind__gDSL_TyBind49", None)
        self.__gDSL_TyBind49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty50"):
                opp_val = getattr(old_value, "gDSL_Ty50", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty50"):
                opp_val = getattr(value, "gDSL_Ty50", None)
                setattr(value, "gDSL_Ty50", self)

    @property
    def gDSL_TyBind(self):
        return self.__gDSL_TyBind

    @gDSL_TyBind.setter
    def gDSL_TyBind(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_TyBind__gDSL_TyBind", None)
        self.__gDSL_TyBind = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty30"):
                opp_val = getattr(old_value, "gDSL_Ty30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty30"):
                opp_val = getattr(value, "gDSL_Ty30", None)
                if opp_val is None:
                    setattr(value, "gDSL_Ty30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gDSL_CONS:

    def __init__(self, conName: str, gDSL_CONS: "gDSL_ConDecl" = None):
        self.conName = conName
        self.gDSL_CONS = gDSL_CONS
        
    @property
    def conName(self) -> str:
        return self.__conName

    @conName.setter
    def conName(self, conName: str):
        self.__conName = conName

    @property
    def gDSL_CONS(self):
        return self.__gDSL_CONS

    @gDSL_CONS.setter
    def gDSL_CONS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_CONS__gDSL_CONS", None)
        self.__gDSL_CONS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ConDecl22"):
                opp_val = getattr(old_value, "gDSL_ConDecl22", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ConDecl22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ConDecl22"):
                opp_val = getattr(value, "gDSL_ConDecl22", None)
                setattr(value, "gDSL_ConDecl22", self)

class gDSL_TyElement:

    def __init__(self, name: str, gDSL_TyElement: "gDSL_Ty" = None, gDSL_TyElement52: "gDSL_Ty" = None):
        self.name = name
        self.gDSL_TyElement = gDSL_TyElement
        self.gDSL_TyElement52 = gDSL_TyElement52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gDSL_TyElement(self):
        return self.__gDSL_TyElement

    @gDSL_TyElement.setter
    def gDSL_TyElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_TyElement__gDSL_TyElement", None)
        self.__gDSL_TyElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty32"):
                opp_val = getattr(old_value, "gDSL_Ty32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty32"):
                opp_val = getattr(value, "gDSL_Ty32", None)
                if opp_val is None:
                    setattr(value, "gDSL_Ty32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_TyElement52(self):
        return self.__gDSL_TyElement52

    @gDSL_TyElement52.setter
    def gDSL_TyElement52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_TyElement__gDSL_TyElement52", None)
        self.__gDSL_TyElement52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty53"):
                opp_val = getattr(old_value, "gDSL_Ty53", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty53"):
                opp_val = getattr(value, "gDSL_Ty53", None)
                setattr(value, "gDSL_Ty53", self)

class gDSL_ConDecl:

    pass
class gDSL_Ty:

    def __init__(self, value: str, type: str, gDSL_Ty: "gDSL_DeclExport" = None, gDSL_Ty12: "gDSL_Type" = None, gDSL_Ty30: set["gDSL_TyBind"] = None, gDSL_Ty32: set["gDSL_TyElement"] = None, gDSL_Ty35: "gDSL_Ty" = None, gDSL_Ty33: set["gDSL_Ty"] = None, gDSL_Ty38: "gDSL_Ty" = None, gDSL_Ty36: "gDSL_Ty" = None, gDSL_Ty41: "gDSL_Ty" = None, gDSL_Ty25: "gDSL_ConDecl" = None, gDSL_Ty27: "gDSL_Type" = None, gDSL_Ty39: "gDSL_Ty" = None, gDSL_Ty44: "gDSL_Ty" = None, gDSL_Ty42: "gDSL_Ty" = None, gDSL_Ty47: "gDSL_Ty" = None, gDSL_Ty45: "gDSL_Ty" = None, gDSL_Ty50: "gDSL_TyBind" = None, gDSL_Ty53: "gDSL_TyElement" = None):
        self.value = value
        self.type = type
        self.gDSL_Ty = gDSL_Ty
        self.gDSL_Ty12 = gDSL_Ty12
        self.gDSL_Ty30 = gDSL_Ty30 if gDSL_Ty30 is not None else set()
        self.gDSL_Ty32 = gDSL_Ty32 if gDSL_Ty32 is not None else set()
        self.gDSL_Ty35 = gDSL_Ty35
        self.gDSL_Ty33 = gDSL_Ty33 if gDSL_Ty33 is not None else set()
        self.gDSL_Ty38 = gDSL_Ty38
        self.gDSL_Ty36 = gDSL_Ty36
        self.gDSL_Ty41 = gDSL_Ty41
        self.gDSL_Ty25 = gDSL_Ty25
        self.gDSL_Ty27 = gDSL_Ty27
        self.gDSL_Ty39 = gDSL_Ty39
        self.gDSL_Ty44 = gDSL_Ty44
        self.gDSL_Ty42 = gDSL_Ty42
        self.gDSL_Ty47 = gDSL_Ty47
        self.gDSL_Ty45 = gDSL_Ty45
        self.gDSL_Ty50 = gDSL_Ty50
        self.gDSL_Ty53 = gDSL_Ty53
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def gDSL_Ty41(self):
        return self.__gDSL_Ty41

    @gDSL_Ty41.setter
    def gDSL_Ty41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty41", None)
        self.__gDSL_Ty41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty39"):
                opp_val = getattr(old_value, "gDSL_Ty39", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty39"):
                opp_val = getattr(value, "gDSL_Ty39", None)
                setattr(value, "gDSL_Ty39", self)

    @property
    def gDSL_Ty36(self):
        return self.__gDSL_Ty36

    @gDSL_Ty36.setter
    def gDSL_Ty36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty36", None)
        self.__gDSL_Ty36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty38"):
                opp_val = getattr(old_value, "gDSL_Ty38", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty38"):
                opp_val = getattr(value, "gDSL_Ty38", None)
                setattr(value, "gDSL_Ty38", self)

    @property
    def gDSL_Ty35(self):
        return self.__gDSL_Ty35

    @gDSL_Ty35.setter
    def gDSL_Ty35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty35", None)
        self.__gDSL_Ty35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty33"):
                opp_val = getattr(old_value, "gDSL_Ty33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty33"):
                opp_val = getattr(value, "gDSL_Ty33", None)
                if opp_val is None:
                    setattr(value, "gDSL_Ty33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_Ty44(self):
        return self.__gDSL_Ty44

    @gDSL_Ty44.setter
    def gDSL_Ty44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty44", None)
        self.__gDSL_Ty44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty42"):
                opp_val = getattr(old_value, "gDSL_Ty42", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty42"):
                opp_val = getattr(value, "gDSL_Ty42", None)
                setattr(value, "gDSL_Ty42", self)

    @property
    def gDSL_Ty30(self):
        return self.__gDSL_Ty30

    @gDSL_Ty30.setter
    def gDSL_Ty30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty30", None)
        self.__gDSL_Ty30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_TyBind"):
                    opp_val = getattr(item, "gDSL_TyBind", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_TyBind", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_TyBind"):
                    opp_val = getattr(item, "gDSL_TyBind", None)
                    
                    setattr(item, "gDSL_TyBind", self)
                    

    @property
    def gDSL_Ty(self):
        return self.__gDSL_Ty

    @gDSL_Ty.setter
    def gDSL_Ty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty", None)
        self.__gDSL_Ty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_DeclExport5"):
                opp_val = getattr(old_value, "gDSL_DeclExport5", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_DeclExport5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_DeclExport5"):
                opp_val = getattr(value, "gDSL_DeclExport5", None)
                setattr(value, "gDSL_DeclExport5", self)

    @property
    def gDSL_Ty39(self):
        return self.__gDSL_Ty39

    @gDSL_Ty39.setter
    def gDSL_Ty39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty39", None)
        self.__gDSL_Ty39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty41"):
                opp_val = getattr(old_value, "gDSL_Ty41", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty41"):
                opp_val = getattr(value, "gDSL_Ty41", None)
                setattr(value, "gDSL_Ty41", self)

    @property
    def gDSL_Ty50(self):
        return self.__gDSL_Ty50

    @gDSL_Ty50.setter
    def gDSL_Ty50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty50", None)
        self.__gDSL_Ty50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_TyBind49"):
                opp_val = getattr(old_value, "gDSL_TyBind49", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_TyBind49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_TyBind49"):
                opp_val = getattr(value, "gDSL_TyBind49", None)
                setattr(value, "gDSL_TyBind49", self)

    @property
    def gDSL_Ty38(self):
        return self.__gDSL_Ty38

    @gDSL_Ty38.setter
    def gDSL_Ty38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty38", None)
        self.__gDSL_Ty38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty36"):
                opp_val = getattr(old_value, "gDSL_Ty36", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty36"):
                opp_val = getattr(value, "gDSL_Ty36", None)
                setattr(value, "gDSL_Ty36", self)

    @property
    def gDSL_Ty27(self):
        return self.__gDSL_Ty27

    @gDSL_Ty27.setter
    def gDSL_Ty27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty27", None)
        self.__gDSL_Ty27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Type28"):
                opp_val = getattr(old_value, "gDSL_Type28", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Type28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Type28"):
                opp_val = getattr(value, "gDSL_Type28", None)
                setattr(value, "gDSL_Type28", self)

    @property
    def gDSL_Ty12(self):
        return self.__gDSL_Ty12

    @gDSL_Ty12.setter
    def gDSL_Ty12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty12", None)
        self.__gDSL_Ty12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Type11"):
                opp_val = getattr(old_value, "gDSL_Type11", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Type11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Type11"):
                opp_val = getattr(value, "gDSL_Type11", None)
                setattr(value, "gDSL_Type11", self)

    @property
    def gDSL_Ty32(self):
        return self.__gDSL_Ty32

    @gDSL_Ty32.setter
    def gDSL_Ty32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty32", None)
        self.__gDSL_Ty32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_TyElement"):
                    opp_val = getattr(item, "gDSL_TyElement", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_TyElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_TyElement"):
                    opp_val = getattr(item, "gDSL_TyElement", None)
                    
                    setattr(item, "gDSL_TyElement", self)
                    

    @property
    def gDSL_Ty42(self):
        return self.__gDSL_Ty42

    @gDSL_Ty42.setter
    def gDSL_Ty42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty42", None)
        self.__gDSL_Ty42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty44"):
                opp_val = getattr(old_value, "gDSL_Ty44", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty44"):
                opp_val = getattr(value, "gDSL_Ty44", None)
                setattr(value, "gDSL_Ty44", self)

    @property
    def gDSL_Ty25(self):
        return self.__gDSL_Ty25

    @gDSL_Ty25.setter
    def gDSL_Ty25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty25", None)
        self.__gDSL_Ty25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ConDecl24"):
                opp_val = getattr(old_value, "gDSL_ConDecl24", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ConDecl24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ConDecl24"):
                opp_val = getattr(value, "gDSL_ConDecl24", None)
                setattr(value, "gDSL_ConDecl24", self)

    @property
    def gDSL_Ty45(self):
        return self.__gDSL_Ty45

    @gDSL_Ty45.setter
    def gDSL_Ty45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty45", None)
        self.__gDSL_Ty45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty47"):
                opp_val = getattr(old_value, "gDSL_Ty47", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty47"):
                opp_val = getattr(value, "gDSL_Ty47", None)
                setattr(value, "gDSL_Ty47", self)

    @property
    def gDSL_Ty47(self):
        return self.__gDSL_Ty47

    @gDSL_Ty47.setter
    def gDSL_Ty47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty47", None)
        self.__gDSL_Ty47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty45"):
                opp_val = getattr(old_value, "gDSL_Ty45", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty45"):
                opp_val = getattr(value, "gDSL_Ty45", None)
                setattr(value, "gDSL_Ty45", self)

    @property
    def gDSL_Ty53(self):
        return self.__gDSL_Ty53

    @gDSL_Ty53.setter
    def gDSL_Ty53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty53", None)
        self.__gDSL_Ty53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_TyElement52"):
                opp_val = getattr(old_value, "gDSL_TyElement52", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_TyElement52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_TyElement52"):
                opp_val = getattr(value, "gDSL_TyElement52", None)
                setattr(value, "gDSL_TyElement52", self)

    @property
    def gDSL_Ty33(self):
        return self.__gDSL_Ty33

    @gDSL_Ty33.setter
    def gDSL_Ty33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Ty__gDSL_Ty33", None)
        self.__gDSL_Ty33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_Ty35"):
                    opp_val = getattr(item, "gDSL_Ty35", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_Ty35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_Ty35"):
                    opp_val = getattr(item, "gDSL_Ty35", None)
                    
                    setattr(item, "gDSL_Ty35", self)
                    

class gDSL_TyVars:

    pass
class gDSL_Exp:

    def __init__(self, mid: str, gDSL_Exp: "gDSL_Val" = None, gDSL_Exp17: "gDSL_Val" = None, gDSL_Exp55: "gDSL_CaseExp" = None, gDSL_Exp57: set["gDSL_CaseExp"] = None, gDSL_Exp79: "gDSL_MonadicExp" = None, gDSL_Exp65: "gDSL_CaseExp" = None, gDSL_Exp103: "gDSL_AtomicExp" = None, gDSL_Exp100: "gDSL_AtomicExp" = None, gDSL_Exp108: "gDSL_Field" = None, gDSL_Exp111: "gDSL_ValueDecl" = None):
        self.mid = mid
        self.gDSL_Exp = gDSL_Exp
        self.gDSL_Exp17 = gDSL_Exp17
        self.gDSL_Exp55 = gDSL_Exp55
        self.gDSL_Exp57 = gDSL_Exp57 if gDSL_Exp57 is not None else set()
        self.gDSL_Exp79 = gDSL_Exp79
        self.gDSL_Exp65 = gDSL_Exp65
        self.gDSL_Exp103 = gDSL_Exp103
        self.gDSL_Exp100 = gDSL_Exp100
        self.gDSL_Exp108 = gDSL_Exp108
        self.gDSL_Exp111 = gDSL_Exp111
        
    @property
    def mid(self) -> str:
        return self.__mid

    @mid.setter
    def mid(self, mid: str):
        self.__mid = mid

    @property
    def gDSL_Exp111(self):
        return self.__gDSL_Exp111

    @gDSL_Exp111.setter
    def gDSL_Exp111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp111", None)
        self.__gDSL_Exp111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_ValueDecl110"):
                opp_val = getattr(old_value, "gDSL_ValueDecl110", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_ValueDecl110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_ValueDecl110"):
                opp_val = getattr(value, "gDSL_ValueDecl110", None)
                setattr(value, "gDSL_ValueDecl110", self)

    @property
    def gDSL_Exp108(self):
        return self.__gDSL_Exp108

    @gDSL_Exp108.setter
    def gDSL_Exp108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp108", None)
        self.__gDSL_Exp108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Field107"):
                opp_val = getattr(old_value, "gDSL_Field107", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Field107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Field107"):
                opp_val = getattr(value, "gDSL_Field107", None)
                setattr(value, "gDSL_Field107", self)

    @property
    def gDSL_Exp103(self):
        return self.__gDSL_Exp103

    @gDSL_Exp103.setter
    def gDSL_Exp103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp103", None)
        self.__gDSL_Exp103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_AtomicExp102"):
                opp_val = getattr(old_value, "gDSL_AtomicExp102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_AtomicExp102"):
                opp_val = getattr(value, "gDSL_AtomicExp102", None)
                if opp_val is None:
                    setattr(value, "gDSL_AtomicExp102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_Exp57(self):
        return self.__gDSL_Exp57

    @gDSL_Exp57.setter
    def gDSL_Exp57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp57", None)
        self.__gDSL_Exp57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_CaseExp58"):
                    opp_val = getattr(item, "gDSL_CaseExp58", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_CaseExp58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_CaseExp58"):
                    opp_val = getattr(item, "gDSL_CaseExp58", None)
                    
                    setattr(item, "gDSL_CaseExp58", self)
                    

    @property
    def gDSL_Exp79(self):
        return self.__gDSL_Exp79

    @gDSL_Exp79.setter
    def gDSL_Exp79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp79", None)
        self.__gDSL_Exp79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_MonadicExp78"):
                opp_val = getattr(old_value, "gDSL_MonadicExp78", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_MonadicExp78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_MonadicExp78"):
                opp_val = getattr(value, "gDSL_MonadicExp78", None)
                setattr(value, "gDSL_MonadicExp78", self)

    @property
    def gDSL_Exp(self):
        return self.__gDSL_Exp

    @gDSL_Exp.setter
    def gDSL_Exp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp", None)
        self.__gDSL_Exp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Val14"):
                opp_val = getattr(old_value, "gDSL_Val14", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Val14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Val14"):
                opp_val = getattr(value, "gDSL_Val14", None)
                setattr(value, "gDSL_Val14", self)

    @property
    def gDSL_Exp65(self):
        return self.__gDSL_Exp65

    @gDSL_Exp65.setter
    def gDSL_Exp65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp65", None)
        self.__gDSL_Exp65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_CaseExp64"):
                opp_val = getattr(old_value, "gDSL_CaseExp64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_CaseExp64"):
                opp_val = getattr(value, "gDSL_CaseExp64", None)
                if opp_val is None:
                    setattr(value, "gDSL_CaseExp64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_Exp17(self):
        return self.__gDSL_Exp17

    @gDSL_Exp17.setter
    def gDSL_Exp17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp17", None)
        self.__gDSL_Exp17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Val16"):
                opp_val = getattr(old_value, "gDSL_Val16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Val16"):
                opp_val = getattr(value, "gDSL_Val16", None)
                if opp_val is None:
                    setattr(value, "gDSL_Val16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gDSL_Exp100(self):
        return self.__gDSL_Exp100

    @gDSL_Exp100.setter
    def gDSL_Exp100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp100", None)
        self.__gDSL_Exp100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_AtomicExp99"):
                opp_val = getattr(old_value, "gDSL_AtomicExp99", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_AtomicExp99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_AtomicExp99"):
                opp_val = getattr(value, "gDSL_AtomicExp99", None)
                setattr(value, "gDSL_AtomicExp99", self)

    @property
    def gDSL_Exp55(self):
        return self.__gDSL_Exp55

    @gDSL_Exp55.setter
    def gDSL_Exp55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Exp__gDSL_Exp55", None)
        self.__gDSL_Exp55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_CaseExp"):
                opp_val = getattr(old_value, "gDSL_CaseExp", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_CaseExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_CaseExp"):
                opp_val = getattr(value, "gDSL_CaseExp", None)
                setattr(value, "gDSL_CaseExp", self)

class Decl:

    pass
class gDSL_Type(Decl):

    def __init__(self, name: str, gDSL_Type: "gDSL_TyVars" = None, gDSL_Type9: set["gDSL_ConDecl"] = None, gDSL_Type11: "gDSL_Ty" = None, gDSL_Type20: "gDSL_TyVars" = None, gDSL_Type28: "gDSL_Ty" = None):
        self.name = name
        self.gDSL_Type = gDSL_Type
        self.gDSL_Type9 = gDSL_Type9 if gDSL_Type9 is not None else set()
        self.gDSL_Type11 = gDSL_Type11
        self.gDSL_Type20 = gDSL_Type20
        self.gDSL_Type28 = gDSL_Type28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gDSL_Type9(self):
        return self.__gDSL_Type9

    @gDSL_Type9.setter
    def gDSL_Type9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Type__gDSL_Type9", None)
        self.__gDSL_Type9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_ConDecl"):
                    opp_val = getattr(item, "gDSL_ConDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_ConDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_ConDecl"):
                    opp_val = getattr(item, "gDSL_ConDecl", None)
                    
                    setattr(item, "gDSL_ConDecl", self)
                    

    @property
    def gDSL_Type(self):
        return self.__gDSL_Type

    @gDSL_Type.setter
    def gDSL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Type__gDSL_Type", None)
        self.__gDSL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_TyVars7"):
                opp_val = getattr(old_value, "gDSL_TyVars7", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_TyVars7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_TyVars7"):
                opp_val = getattr(value, "gDSL_TyVars7", None)
                setattr(value, "gDSL_TyVars7", self)

    @property
    def gDSL_Type11(self):
        return self.__gDSL_Type11

    @gDSL_Type11.setter
    def gDSL_Type11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Type__gDSL_Type11", None)
        self.__gDSL_Type11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty12"):
                opp_val = getattr(old_value, "gDSL_Ty12", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty12"):
                opp_val = getattr(value, "gDSL_Ty12", None)
                setattr(value, "gDSL_Ty12", self)

    @property
    def gDSL_Type28(self):
        return self.__gDSL_Type28

    @gDSL_Type28.setter
    def gDSL_Type28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Type__gDSL_Type28", None)
        self.__gDSL_Type28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Ty27"):
                opp_val = getattr(old_value, "gDSL_Ty27", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Ty27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Ty27"):
                opp_val = getattr(value, "gDSL_Ty27", None)
                setattr(value, "gDSL_Ty27", self)

    @property
    def gDSL_Type20(self):
        return self.__gDSL_Type20

    @gDSL_Type20.setter
    def gDSL_Type20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Type__gDSL_Type20", None)
        self.__gDSL_Type20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_TyVars19"):
                opp_val = getattr(old_value, "gDSL_TyVars19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_TyVars19"):
                opp_val = getattr(value, "gDSL_TyVars19", None)
                if opp_val is None:
                    setattr(value, "gDSL_TyVars19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gDSL_Val(Decl):

    def __init__(self, name: str, attr: str, mid: str, decPat: str, gDSL_Val: "gDSL_DeclExport" = None, gDSL_Val14: "gDSL_Exp" = None, gDSL_Val16: set["gDSL_Exp"] = None):
        self.name = name
        self.attr = attr
        self.mid = mid
        self.decPat = decPat
        self.gDSL_Val = gDSL_Val
        self.gDSL_Val14 = gDSL_Val14
        self.gDSL_Val16 = gDSL_Val16 if gDSL_Val16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mid(self) -> str:
        return self.__mid

    @mid.setter
    def mid(self, mid: str):
        self.__mid = mid

    @property
    def decPat(self) -> str:
        return self.__decPat

    @decPat.setter
    def decPat(self, decPat: str):
        self.__decPat = decPat

    @property
    def attr(self) -> str:
        return self.__attr

    @attr.setter
    def attr(self, attr: str):
        self.__attr = attr

    @property
    def gDSL_Val14(self):
        return self.__gDSL_Val14

    @gDSL_Val14.setter
    def gDSL_Val14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Val__gDSL_Val14", None)
        self.__gDSL_Val14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_Exp"):
                opp_val = getattr(old_value, "gDSL_Exp", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_Exp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_Exp"):
                opp_val = getattr(value, "gDSL_Exp", None)
                setattr(value, "gDSL_Exp", self)

    @property
    def gDSL_Val(self):
        return self.__gDSL_Val

    @gDSL_Val.setter
    def gDSL_Val(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Val__gDSL_Val", None)
        self.__gDSL_Val = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gDSL_DeclExport"):
                opp_val = getattr(old_value, "gDSL_DeclExport", None)
                if opp_val == self:
                    setattr(old_value, "gDSL_DeclExport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gDSL_DeclExport"):
                opp_val = getattr(value, "gDSL_DeclExport", None)
                setattr(value, "gDSL_DeclExport", self)

    @property
    def gDSL_Val16(self):
        return self.__gDSL_Val16

    @gDSL_Val16.setter
    def gDSL_Val16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gDSL_Val__gDSL_Val16", None)
        self.__gDSL_Val16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gDSL_Exp17"):
                    opp_val = getattr(item, "gDSL_Exp17", None)
                    
                    if opp_val == self:
                        setattr(item, "gDSL_Exp17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gDSL_Exp17"):
                    opp_val = getattr(item, "gDSL_Exp17", None)
                    
                    setattr(item, "gDSL_Exp17", self)
                    

class gDSL_DeclExport(Decl):

    pass
class gDSL_Decl:

    pass
class gDSL_Model:

    pass