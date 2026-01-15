from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CollectionKindCS(Enum):
    Collection = "Collection"


############################################
# Definition of Classes
############################################

class minioclcs_CSTrace(ABC):

    pass
class minioclcs_EObject:

    pass
class BooleanLiteralExpCS:

    pass
class minioclcs_BooleanExpCS(BooleanLiteralExpCS):

    def __init__(self, boolSymbol: bool):
        self.boolSymbol = boolSymbol
        
    @property
    def boolSymbol(self) -> bool:
        return self.__boolSymbol

    @boolSymbol.setter
    def boolSymbol(self, boolSymbol: bool):
        self.__boolSymbol = boolSymbol

class minioclcs_EClass:

    pass
class LiteralExpCS:

    pass
class minioclcs_CollectionLiteralExpCS(LiteralExpCS):

    def __init__(self, kind: str, minioclcs_CollectionLiteralExpCS: set["minioclcs_CollectionLiteralPartCS"] = None):
        self.kind = kind
        self.minioclcs_CollectionLiteralExpCS = minioclcs_CollectionLiteralExpCS if minioclcs_CollectionLiteralExpCS is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def minioclcs_CollectionLiteralExpCS(self):
        return self.__minioclcs_CollectionLiteralExpCS

    @minioclcs_CollectionLiteralExpCS.setter
    def minioclcs_CollectionLiteralExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_CollectionLiteralExpCS__minioclcs_CollectionLiteralExpCS", None)
        self.__minioclcs_CollectionLiteralExpCS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minioclcs_CollectionLiteralPartCS"):
                    opp_val = getattr(item, "minioclcs_CollectionLiteralPartCS", None)
                    
                    if opp_val == self:
                        setattr(item, "minioclcs_CollectionLiteralPartCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minioclcs_CollectionLiteralPartCS"):
                    opp_val = getattr(item, "minioclcs_CollectionLiteralPartCS", None)
                    
                    setattr(item, "minioclcs_CollectionLiteralPartCS", self)
                    

class minioclcs_BooleanLiteralExpCS(LiteralExpCS):

    pass
class minioclcs_NullLiteralExpCS(LiteralExpCS):

    pass
class minioclcs_IntLiteralExpCS(LiteralExpCS):

    def __init__(self, intSymbol: int):
        self.intSymbol = intSymbol
        
    @property
    def intSymbol(self) -> int:
        return self.__intSymbol

    @intSymbol.setter
    def intSymbol(self, intSymbol: int):
        self.__intSymbol = intSymbol

class LoopExpCS:

    pass
class minioclcs_IterateExpCS(LoopExpCS):

    pass
class minioclcs_CollectExpCS(LoopExpCS):

    pass
class NavigationExpCS:

    pass
class minioclcs_LoopExpCS(NavigationExpCS):

    pass
class PrimaryExpCS:

    pass
class minioclcs_NameExpCS(PrimaryExpCS, NavigationExpCS):

    pass
class minioclcs_LiteralExpCS(PrimaryExpCS):

    pass
class minioclcs_LetExpCS(PrimaryExpCS):

    pass
class minioclcs_SelfExpCS(PrimaryExpCS):

    pass
class CallExpCS:

    pass
class minioclcs_PrimaryExpCS(CallExpCS):

    pass
class EqualityExpCS:

    pass
class minioclcs_CallExpCS(EqualityExpCS):

    pass
class ExpCS:

    pass
class minioclcs_EqualityExpCS(ExpCS):

    def __init__(self, opName: str, minioclcs_EqualityExpCS: "minioclcs_EqualityExpCS" = None, minioclcs_EqualityExpCS39: "minioclcs_EqualityExpCS" = None, minioclcs_EqualityExpCS42: "minioclcs_CallExpCS" = None):
        self.opName = opName
        self.minioclcs_EqualityExpCS = minioclcs_EqualityExpCS
        self.minioclcs_EqualityExpCS39 = minioclcs_EqualityExpCS39
        self.minioclcs_EqualityExpCS42 = minioclcs_EqualityExpCS42
        
    @property
    def opName(self) -> str:
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName

    @property
    def minioclcs_EqualityExpCS(self):
        return self.__minioclcs_EqualityExpCS

    @minioclcs_EqualityExpCS.setter
    def minioclcs_EqualityExpCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_EqualityExpCS__minioclcs_EqualityExpCS", None)
        self.__minioclcs_EqualityExpCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_EqualityExpCS39"):
                opp_val = getattr(old_value, "minioclcs_EqualityExpCS39", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_EqualityExpCS39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_EqualityExpCS39"):
                opp_val = getattr(value, "minioclcs_EqualityExpCS39", None)
                setattr(value, "minioclcs_EqualityExpCS39", self)

    @property
    def minioclcs_EqualityExpCS39(self):
        return self.__minioclcs_EqualityExpCS39

    @minioclcs_EqualityExpCS39.setter
    def minioclcs_EqualityExpCS39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_EqualityExpCS__minioclcs_EqualityExpCS39", None)
        self.__minioclcs_EqualityExpCS39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_EqualityExpCS"):
                opp_val = getattr(old_value, "minioclcs_EqualityExpCS", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_EqualityExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_EqualityExpCS"):
                opp_val = getattr(value, "minioclcs_EqualityExpCS", None)
                setattr(value, "minioclcs_EqualityExpCS", self)

    @property
    def minioclcs_EqualityExpCS42(self):
        return self.__minioclcs_EqualityExpCS42

    @minioclcs_EqualityExpCS42.setter
    def minioclcs_EqualityExpCS42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_EqualityExpCS__minioclcs_EqualityExpCS42", None)
        self.__minioclcs_EqualityExpCS42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_CallExpCS"):
                opp_val = getattr(old_value, "minioclcs_CallExpCS", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_CallExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_CallExpCS"):
                opp_val = getattr(value, "minioclcs_CallExpCS", None)
                setattr(value, "minioclcs_CallExpCS", self)

class CSTrace:

    pass
class minioclcs_PropertyCS(CSTrace):

    def __init__(self, name: str, minioclcs_PropertyCS: "minioclcs_ClassCS" = None, minioclcs_PropertyCS17: "minioclcs_PathNameCS" = None, minioclcs_PropertyCS20: "minioclcs_MultiplicityCS" = None):
        self.name = name
        self.minioclcs_PropertyCS = minioclcs_PropertyCS
        self.minioclcs_PropertyCS17 = minioclcs_PropertyCS17
        self.minioclcs_PropertyCS20 = minioclcs_PropertyCS20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minioclcs_PropertyCS17(self):
        return self.__minioclcs_PropertyCS17

    @minioclcs_PropertyCS17.setter
    def minioclcs_PropertyCS17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_PropertyCS__minioclcs_PropertyCS17", None)
        self.__minioclcs_PropertyCS17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PathNameCS18"):
                opp_val = getattr(old_value, "minioclcs_PathNameCS18", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PathNameCS18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PathNameCS18"):
                opp_val = getattr(value, "minioclcs_PathNameCS18", None)
                setattr(value, "minioclcs_PathNameCS18", self)

    @property
    def minioclcs_PropertyCS20(self):
        return self.__minioclcs_PropertyCS20

    @minioclcs_PropertyCS20.setter
    def minioclcs_PropertyCS20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_PropertyCS__minioclcs_PropertyCS20", None)
        self.__minioclcs_PropertyCS20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_MultiplicityCS"):
                opp_val = getattr(old_value, "minioclcs_MultiplicityCS", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_MultiplicityCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_MultiplicityCS"):
                opp_val = getattr(value, "minioclcs_MultiplicityCS", None)
                setattr(value, "minioclcs_MultiplicityCS", self)

    @property
    def minioclcs_PropertyCS(self):
        return self.__minioclcs_PropertyCS

    @minioclcs_PropertyCS.setter
    def minioclcs_PropertyCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_PropertyCS__minioclcs_PropertyCS", None)
        self.__minioclcs_PropertyCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_ClassCS13"):
                opp_val = getattr(old_value, "minioclcs_ClassCS13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_ClassCS13"):
                opp_val = getattr(value, "minioclcs_ClassCS13", None)
                if opp_val is None:
                    setattr(value, "minioclcs_ClassCS13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class minioclcs_ClassCS(CSTrace):

    def __init__(self, name: str, minioclcs_ClassCS: "minioclcs_PackageCS" = None, minioclcs_ClassCS13: set["minioclcs_PropertyCS"] = None, minioclcs_ClassCS15: set["minioclcs_OperationCS"] = None, minioclcs_ClassCS11: "minioclcs_PathNameCS" = None):
        self.name = name
        self.minioclcs_ClassCS = minioclcs_ClassCS
        self.minioclcs_ClassCS13 = minioclcs_ClassCS13 if minioclcs_ClassCS13 is not None else set()
        self.minioclcs_ClassCS15 = minioclcs_ClassCS15 if minioclcs_ClassCS15 is not None else set()
        self.minioclcs_ClassCS11 = minioclcs_ClassCS11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minioclcs_ClassCS13(self):
        return self.__minioclcs_ClassCS13

    @minioclcs_ClassCS13.setter
    def minioclcs_ClassCS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_ClassCS__minioclcs_ClassCS13", None)
        self.__minioclcs_ClassCS13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minioclcs_PropertyCS"):
                    opp_val = getattr(item, "minioclcs_PropertyCS", None)
                    
                    if opp_val == self:
                        setattr(item, "minioclcs_PropertyCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minioclcs_PropertyCS"):
                    opp_val = getattr(item, "minioclcs_PropertyCS", None)
                    
                    setattr(item, "minioclcs_PropertyCS", self)
                    

    @property
    def minioclcs_ClassCS15(self):
        return self.__minioclcs_ClassCS15

    @minioclcs_ClassCS15.setter
    def minioclcs_ClassCS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_ClassCS__minioclcs_ClassCS15", None)
        self.__minioclcs_ClassCS15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minioclcs_OperationCS"):
                    opp_val = getattr(item, "minioclcs_OperationCS", None)
                    
                    if opp_val == self:
                        setattr(item, "minioclcs_OperationCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minioclcs_OperationCS"):
                    opp_val = getattr(item, "minioclcs_OperationCS", None)
                    
                    setattr(item, "minioclcs_OperationCS", self)
                    

    @property
    def minioclcs_ClassCS11(self):
        return self.__minioclcs_ClassCS11

    @minioclcs_ClassCS11.setter
    def minioclcs_ClassCS11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_ClassCS__minioclcs_ClassCS11", None)
        self.__minioclcs_ClassCS11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PathNameCS"):
                opp_val = getattr(old_value, "minioclcs_PathNameCS", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PathNameCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PathNameCS"):
                opp_val = getattr(value, "minioclcs_PathNameCS", None)
                setattr(value, "minioclcs_PathNameCS", self)

    @property
    def minioclcs_ClassCS(self):
        return self.__minioclcs_ClassCS

    @minioclcs_ClassCS.setter
    def minioclcs_ClassCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_ClassCS__minioclcs_ClassCS", None)
        self.__minioclcs_ClassCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PackageCS9"):
                opp_val = getattr(old_value, "minioclcs_PackageCS9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PackageCS9"):
                opp_val = getattr(value, "minioclcs_PackageCS9", None)
                if opp_val is None:
                    setattr(value, "minioclcs_PackageCS9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class minioclcs_OperationCS(CSTrace):

    def __init__(self, name: str, minioclcs_OperationCS: "minioclcs_ClassCS" = None, minioclcs_OperationCS22: set["minioclcs_ParameterCS"] = None, minioclcs_OperationCS24: "minioclcs_PathNameCS" = None, minioclcs_OperationCS27: "minioclcs_ExpCS" = None):
        self.name = name
        self.minioclcs_OperationCS = minioclcs_OperationCS
        self.minioclcs_OperationCS22 = minioclcs_OperationCS22 if minioclcs_OperationCS22 is not None else set()
        self.minioclcs_OperationCS24 = minioclcs_OperationCS24
        self.minioclcs_OperationCS27 = minioclcs_OperationCS27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minioclcs_OperationCS22(self):
        return self.__minioclcs_OperationCS22

    @minioclcs_OperationCS22.setter
    def minioclcs_OperationCS22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_OperationCS__minioclcs_OperationCS22", None)
        self.__minioclcs_OperationCS22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minioclcs_ParameterCS"):
                    opp_val = getattr(item, "minioclcs_ParameterCS", None)
                    
                    if opp_val == self:
                        setattr(item, "minioclcs_ParameterCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minioclcs_ParameterCS"):
                    opp_val = getattr(item, "minioclcs_ParameterCS", None)
                    
                    setattr(item, "minioclcs_ParameterCS", self)
                    

    @property
    def minioclcs_OperationCS27(self):
        return self.__minioclcs_OperationCS27

    @minioclcs_OperationCS27.setter
    def minioclcs_OperationCS27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_OperationCS__minioclcs_OperationCS27", None)
        self.__minioclcs_OperationCS27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_ExpCS"):
                opp_val = getattr(old_value, "minioclcs_ExpCS", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_ExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_ExpCS"):
                opp_val = getattr(value, "minioclcs_ExpCS", None)
                setattr(value, "minioclcs_ExpCS", self)

    @property
    def minioclcs_OperationCS(self):
        return self.__minioclcs_OperationCS

    @minioclcs_OperationCS.setter
    def minioclcs_OperationCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_OperationCS__minioclcs_OperationCS", None)
        self.__minioclcs_OperationCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_ClassCS15"):
                opp_val = getattr(old_value, "minioclcs_ClassCS15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_ClassCS15"):
                opp_val = getattr(value, "minioclcs_ClassCS15", None)
                if opp_val is None:
                    setattr(value, "minioclcs_ClassCS15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minioclcs_OperationCS24(self):
        return self.__minioclcs_OperationCS24

    @minioclcs_OperationCS24.setter
    def minioclcs_OperationCS24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_OperationCS__minioclcs_OperationCS24", None)
        self.__minioclcs_OperationCS24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PathNameCS25"):
                opp_val = getattr(old_value, "minioclcs_PathNameCS25", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PathNameCS25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PathNameCS25"):
                opp_val = getattr(value, "minioclcs_PathNameCS25", None)
                setattr(value, "minioclcs_PathNameCS25", self)

class minioclcs_CollectionLiteralPartCS(CSTrace):

    pass
class minioclcs_PathNameCS(CSTrace):

    pass
class minioclcs_ImportCS(CSTrace):

    def __init__(self, alias: str, uri: str, minioclcs_ImportCS: "minioclcs_RootCS" = None):
        self.alias = alias
        self.uri = uri
        self.minioclcs_ImportCS = minioclcs_ImportCS
        
    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def minioclcs_ImportCS(self):
        return self.__minioclcs_ImportCS

    @minioclcs_ImportCS.setter
    def minioclcs_ImportCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_ImportCS__minioclcs_ImportCS", None)
        self.__minioclcs_ImportCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_RootCS"):
                opp_val = getattr(old_value, "minioclcs_RootCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_RootCS"):
                opp_val = getattr(value, "minioclcs_RootCS", None)
                if opp_val is None:
                    setattr(value, "minioclcs_RootCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class minioclcs_MultiplicityCS(CSTrace):

    def __init__(self, opt: bool, mult: bool, mandatory: int, lowerInt: int, upperInt: int, upperMult: bool, minioclcs_MultiplicityCS: "minioclcs_PropertyCS" = None):
        self.opt = opt
        self.mult = mult
        self.mandatory = mandatory
        self.lowerInt = lowerInt
        self.upperInt = upperInt
        self.upperMult = upperMult
        self.minioclcs_MultiplicityCS = minioclcs_MultiplicityCS
        
    @property
    def mandatory(self) -> int:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: int):
        self.__mandatory = mandatory

    @property
    def opt(self) -> bool:
        return self.__opt

    @opt.setter
    def opt(self, opt: bool):
        self.__opt = opt

    @property
    def upperInt(self) -> int:
        return self.__upperInt

    @upperInt.setter
    def upperInt(self, upperInt: int):
        self.__upperInt = upperInt

    @property
    def upperMult(self) -> bool:
        return self.__upperMult

    @upperMult.setter
    def upperMult(self, upperMult: bool):
        self.__upperMult = upperMult

    @property
    def mult(self) -> bool:
        return self.__mult

    @mult.setter
    def mult(self, mult: bool):
        self.__mult = mult

    @property
    def lowerInt(self) -> int:
        return self.__lowerInt

    @lowerInt.setter
    def lowerInt(self, lowerInt: int):
        self.__lowerInt = lowerInt

    @property
    def minioclcs_MultiplicityCS(self):
        return self.__minioclcs_MultiplicityCS

    @minioclcs_MultiplicityCS.setter
    def minioclcs_MultiplicityCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_MultiplicityCS__minioclcs_MultiplicityCS", None)
        self.__minioclcs_MultiplicityCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PropertyCS20"):
                opp_val = getattr(old_value, "minioclcs_PropertyCS20", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PropertyCS20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PropertyCS20"):
                opp_val = getattr(value, "minioclcs_PropertyCS20", None)
                setattr(value, "minioclcs_PropertyCS20", self)

class minioclcs_InvariantCS(CSTrace):

    pass
class minioclcs_AccVarCS(CSTrace):

    def __init__(self, accName: str, minioclcs_AccVarCS: "minioclcs_IterateExpCS" = None, minioclcs_AccVarCS57: "minioclcs_PathNameCS" = None, minioclcs_AccVarCS60: "minioclcs_ExpCS" = None):
        self.accName = accName
        self.minioclcs_AccVarCS = minioclcs_AccVarCS
        self.minioclcs_AccVarCS57 = minioclcs_AccVarCS57
        self.minioclcs_AccVarCS60 = minioclcs_AccVarCS60
        
    @property
    def accName(self) -> str:
        return self.__accName

    @accName.setter
    def accName(self, accName: str):
        self.__accName = accName

    @property
    def minioclcs_AccVarCS(self):
        return self.__minioclcs_AccVarCS

    @minioclcs_AccVarCS.setter
    def minioclcs_AccVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_AccVarCS__minioclcs_AccVarCS", None)
        self.__minioclcs_AccVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_IterateExpCS"):
                opp_val = getattr(old_value, "minioclcs_IterateExpCS", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_IterateExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_IterateExpCS"):
                opp_val = getattr(value, "minioclcs_IterateExpCS", None)
                setattr(value, "minioclcs_IterateExpCS", self)

    @property
    def minioclcs_AccVarCS57(self):
        return self.__minioclcs_AccVarCS57

    @minioclcs_AccVarCS57.setter
    def minioclcs_AccVarCS57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_AccVarCS__minioclcs_AccVarCS57", None)
        self.__minioclcs_AccVarCS57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PathNameCS58"):
                opp_val = getattr(old_value, "minioclcs_PathNameCS58", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PathNameCS58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PathNameCS58"):
                opp_val = getattr(value, "minioclcs_PathNameCS58", None)
                setattr(value, "minioclcs_PathNameCS58", self)

    @property
    def minioclcs_AccVarCS60(self):
        return self.__minioclcs_AccVarCS60

    @minioclcs_AccVarCS60.setter
    def minioclcs_AccVarCS60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_AccVarCS__minioclcs_AccVarCS60", None)
        self.__minioclcs_AccVarCS60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_ExpCS61"):
                opp_val = getattr(old_value, "minioclcs_ExpCS61", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_ExpCS61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_ExpCS61"):
                opp_val = getattr(value, "minioclcs_ExpCS61", None)
                setattr(value, "minioclcs_ExpCS61", self)

class minioclcs_PathElementCS(CSTrace):

    pass
class minioclcs_ConstraintsDefCS(CSTrace):

    pass
class minioclcs_PackageCS(CSTrace):

    def __init__(self, name: str, minioclcs_PackageCS: "minioclcs_RootCS" = None, minioclcs_PackageCS7: "minioclcs_PackageCS" = None, minioclcs_PackageCS5: set["minioclcs_PackageCS"] = None, minioclcs_PackageCS9: set["minioclcs_ClassCS"] = None):
        self.name = name
        self.minioclcs_PackageCS = minioclcs_PackageCS
        self.minioclcs_PackageCS7 = minioclcs_PackageCS7
        self.minioclcs_PackageCS5 = minioclcs_PackageCS5 if minioclcs_PackageCS5 is not None else set()
        self.minioclcs_PackageCS9 = minioclcs_PackageCS9 if minioclcs_PackageCS9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minioclcs_PackageCS5(self):
        return self.__minioclcs_PackageCS5

    @minioclcs_PackageCS5.setter
    def minioclcs_PackageCS5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_PackageCS__minioclcs_PackageCS5", None)
        self.__minioclcs_PackageCS5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minioclcs_PackageCS7"):
                    opp_val = getattr(item, "minioclcs_PackageCS7", None)
                    
                    if opp_val == self:
                        setattr(item, "minioclcs_PackageCS7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minioclcs_PackageCS7"):
                    opp_val = getattr(item, "minioclcs_PackageCS7", None)
                    
                    setattr(item, "minioclcs_PackageCS7", self)
                    

    @property
    def minioclcs_PackageCS9(self):
        return self.__minioclcs_PackageCS9

    @minioclcs_PackageCS9.setter
    def minioclcs_PackageCS9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_PackageCS__minioclcs_PackageCS9", None)
        self.__minioclcs_PackageCS9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "minioclcs_ClassCS"):
                    opp_val = getattr(item, "minioclcs_ClassCS", None)
                    
                    if opp_val == self:
                        setattr(item, "minioclcs_ClassCS", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "minioclcs_ClassCS"):
                    opp_val = getattr(item, "minioclcs_ClassCS", None)
                    
                    setattr(item, "minioclcs_ClassCS", self)
                    

    @property
    def minioclcs_PackageCS(self):
        return self.__minioclcs_PackageCS

    @minioclcs_PackageCS.setter
    def minioclcs_PackageCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_PackageCS__minioclcs_PackageCS", None)
        self.__minioclcs_PackageCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_RootCS2"):
                opp_val = getattr(old_value, "minioclcs_RootCS2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_RootCS2"):
                opp_val = getattr(value, "minioclcs_RootCS2", None)
                if opp_val is None:
                    setattr(value, "minioclcs_RootCS2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minioclcs_PackageCS7(self):
        return self.__minioclcs_PackageCS7

    @minioclcs_PackageCS7.setter
    def minioclcs_PackageCS7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_PackageCS__minioclcs_PackageCS7", None)
        self.__minioclcs_PackageCS7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PackageCS5"):
                opp_val = getattr(old_value, "minioclcs_PackageCS5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PackageCS5"):
                opp_val = getattr(value, "minioclcs_PackageCS5", None)
                if opp_val is None:
                    setattr(value, "minioclcs_PackageCS5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class minioclcs_ExpCS(CSTrace):

    pass
class minioclcs_ParameterCS(CSTrace):

    def __init__(self, name: str, minioclcs_ParameterCS: "minioclcs_OperationCS" = None, minioclcs_ParameterCS29: "minioclcs_PathNameCS" = None):
        self.name = name
        self.minioclcs_ParameterCS = minioclcs_ParameterCS
        self.minioclcs_ParameterCS29 = minioclcs_ParameterCS29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minioclcs_ParameterCS(self):
        return self.__minioclcs_ParameterCS

    @minioclcs_ParameterCS.setter
    def minioclcs_ParameterCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_ParameterCS__minioclcs_ParameterCS", None)
        self.__minioclcs_ParameterCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_OperationCS22"):
                opp_val = getattr(old_value, "minioclcs_OperationCS22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_OperationCS22"):
                opp_val = getattr(value, "minioclcs_OperationCS22", None)
                if opp_val is None:
                    setattr(value, "minioclcs_OperationCS22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minioclcs_ParameterCS29(self):
        return self.__minioclcs_ParameterCS29

    @minioclcs_ParameterCS29.setter
    def minioclcs_ParameterCS29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_ParameterCS__minioclcs_ParameterCS29", None)
        self.__minioclcs_ParameterCS29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PathNameCS30"):
                opp_val = getattr(old_value, "minioclcs_PathNameCS30", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PathNameCS30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PathNameCS30"):
                opp_val = getattr(value, "minioclcs_PathNameCS30", None)
                setattr(value, "minioclcs_PathNameCS30", self)

class minioclcs_RoundedBracketClauseCS(CSTrace):

    pass
class minioclcs_LetVarCS(CSTrace):

    def __init__(self, name: str, minioclcs_LetVarCS: "minioclcs_LetExpCS" = None, minioclcs_LetVarCS81: "minioclcs_PathNameCS" = None, minioclcs_LetVarCS84: "minioclcs_ExpCS" = None):
        self.name = name
        self.minioclcs_LetVarCS = minioclcs_LetVarCS
        self.minioclcs_LetVarCS81 = minioclcs_LetVarCS81
        self.minioclcs_LetVarCS84 = minioclcs_LetVarCS84
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def minioclcs_LetVarCS(self):
        return self.__minioclcs_LetVarCS

    @minioclcs_LetVarCS.setter
    def minioclcs_LetVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_LetVarCS__minioclcs_LetVarCS", None)
        self.__minioclcs_LetVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_LetExpCS"):
                opp_val = getattr(old_value, "minioclcs_LetExpCS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_LetExpCS"):
                opp_val = getattr(value, "minioclcs_LetExpCS", None)
                if opp_val is None:
                    setattr(value, "minioclcs_LetExpCS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def minioclcs_LetVarCS81(self):
        return self.__minioclcs_LetVarCS81

    @minioclcs_LetVarCS81.setter
    def minioclcs_LetVarCS81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_LetVarCS__minioclcs_LetVarCS81", None)
        self.__minioclcs_LetVarCS81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PathNameCS82"):
                opp_val = getattr(old_value, "minioclcs_PathNameCS82", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PathNameCS82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PathNameCS82"):
                opp_val = getattr(value, "minioclcs_PathNameCS82", None)
                setattr(value, "minioclcs_PathNameCS82", self)

    @property
    def minioclcs_LetVarCS84(self):
        return self.__minioclcs_LetVarCS84

    @minioclcs_LetVarCS84.setter
    def minioclcs_LetVarCS84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_LetVarCS__minioclcs_LetVarCS84", None)
        self.__minioclcs_LetVarCS84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_ExpCS85"):
                opp_val = getattr(old_value, "minioclcs_ExpCS85", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_ExpCS85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_ExpCS85"):
                opp_val = getattr(value, "minioclcs_ExpCS85", None)
                setattr(value, "minioclcs_ExpCS85", self)

class minioclcs_NavigationExpCS(CSTrace):

    pass
class minioclcs_IteratorVarCS(CSTrace):

    def __init__(self, itName: str, minioclcs_IteratorVarCS: "minioclcs_LoopExpCS" = None, minioclcs_IteratorVarCS53: "minioclcs_PathNameCS" = None):
        self.itName = itName
        self.minioclcs_IteratorVarCS = minioclcs_IteratorVarCS
        self.minioclcs_IteratorVarCS53 = minioclcs_IteratorVarCS53
        
    @property
    def itName(self) -> str:
        return self.__itName

    @itName.setter
    def itName(self, itName: str):
        self.__itName = itName

    @property
    def minioclcs_IteratorVarCS53(self):
        return self.__minioclcs_IteratorVarCS53

    @minioclcs_IteratorVarCS53.setter
    def minioclcs_IteratorVarCS53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_IteratorVarCS__minioclcs_IteratorVarCS53", None)
        self.__minioclcs_IteratorVarCS53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_PathNameCS54"):
                opp_val = getattr(old_value, "minioclcs_PathNameCS54", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_PathNameCS54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_PathNameCS54"):
                opp_val = getattr(value, "minioclcs_PathNameCS54", None)
                setattr(value, "minioclcs_PathNameCS54", self)

    @property
    def minioclcs_IteratorVarCS(self):
        return self.__minioclcs_IteratorVarCS

    @minioclcs_IteratorVarCS.setter
    def minioclcs_IteratorVarCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_minioclcs_IteratorVarCS__minioclcs_IteratorVarCS", None)
        self.__minioclcs_IteratorVarCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "minioclcs_LoopExpCS"):
                opp_val = getattr(old_value, "minioclcs_LoopExpCS", None)
                if opp_val == self:
                    setattr(old_value, "minioclcs_LoopExpCS", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "minioclcs_LoopExpCS"):
                opp_val = getattr(value, "minioclcs_LoopExpCS", None)
                setattr(value, "minioclcs_LoopExpCS", self)

class minioclcs_RootCS(CSTrace):

    pass