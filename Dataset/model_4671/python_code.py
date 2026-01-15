from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class IdUse:

    pass
class picojava_VariableUse(IdUse):

    pass
class picojava_TypeUse(IdUse):

    pass
class picojava_Use(IdUse):

    pass
class Exp:

    pass
class picojava_BooleanLiteral(Exp):

    def __init__(self, Value: str, picojava_BooleanLiteral: "picojava_PrimitiveDecl" = None):
        self.Value = Value
        self.picojava_BooleanLiteral = picojava_BooleanLiteral
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def picojava_BooleanLiteral(self):
        return self.__picojava_BooleanLiteral

    @picojava_BooleanLiteral.setter
    def picojava_BooleanLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_BooleanLiteral__picojava_BooleanLiteral", None)
        self.__picojava_BooleanLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_PrimitiveDecl57"):
                opp_val = getattr(old_value, "picojava_PrimitiveDecl57", None)
                if opp_val == self:
                    setattr(old_value, "picojava_PrimitiveDecl57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_PrimitiveDecl57"):
                opp_val = getattr(value, "picojava_PrimitiveDecl57", None)
                setattr(value, "picojava_PrimitiveDecl57", self)

class picojava_Exp(ABC):

    def __init__(self, isValue: bool, picojava_Exp: "picojava_AssignStmt" = None, picojava_Exp36: "picojava_WhileStmt" = None, picojava_Exp43: "picojava_TypeDecl" = None):
        self.isValue = isValue
        self.picojava_Exp = picojava_Exp
        self.picojava_Exp36 = picojava_Exp36
        self.picojava_Exp43 = picojava_Exp43
        
    @property
    def isValue(self) -> bool:
        return self.__isValue

    @isValue.setter
    def isValue(self, isValue: bool):
        self.__isValue = isValue

    @property
    def picojava_Exp36(self):
        return self.__picojava_Exp36

    @picojava_Exp36.setter
    def picojava_Exp36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Exp__picojava_Exp36", None)
        self.__picojava_Exp36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_WhileStmt"):
                opp_val = getattr(old_value, "picojava_WhileStmt", None)
                if opp_val == self:
                    setattr(old_value, "picojava_WhileStmt", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_WhileStmt"):
                opp_val = getattr(value, "picojava_WhileStmt", None)
                setattr(value, "picojava_WhileStmt", self)

    @property
    def picojava_Exp43(self):
        return self.__picojava_Exp43

    @picojava_Exp43.setter
    def picojava_Exp43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Exp__picojava_Exp43", None)
        self.__picojava_Exp43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_TypeDecl44"):
                opp_val = getattr(old_value, "picojava_TypeDecl44", None)
                if opp_val == self:
                    setattr(old_value, "picojava_TypeDecl44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_TypeDecl44"):
                opp_val = getattr(value, "picojava_TypeDecl44", None)
                setattr(value, "picojava_TypeDecl44", self)

    @property
    def picojava_Exp(self):
        return self.__picojava_Exp

    @picojava_Exp.setter
    def picojava_Exp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Exp__picojava_Exp", None)
        self.__picojava_Exp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_AssignStmt34"):
                opp_val = getattr(old_value, "picojava_AssignStmt34", None)
                if opp_val == self:
                    setattr(old_value, "picojava_AssignStmt34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_AssignStmt34"):
                opp_val = getattr(value, "picojava_AssignStmt34", None)
                setattr(value, "picojava_AssignStmt34", self)

class Access:

    pass
class picojava_Dot(Access):

    pass
class picojava_IdUse(Access):

    def __init__(self, Name: str, isQualified: bool, picojava_IdUse: "picojava_ClassDecl" = None, picojava_IdUse49: "picojava_Access" = None, picojava_IdUse55: "picojava_Dot" = None):
        self.Name = Name
        self.isQualified = isQualified
        self.picojava_IdUse = picojava_IdUse
        self.picojava_IdUse49 = picojava_IdUse49
        self.picojava_IdUse55 = picojava_IdUse55
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def isQualified(self) -> bool:
        return self.__isQualified

    @isQualified.setter
    def isQualified(self, isQualified: bool):
        self.__isQualified = isQualified

    @property
    def picojava_IdUse55(self):
        return self.__picojava_IdUse55

    @picojava_IdUse55.setter
    def picojava_IdUse55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_IdUse__picojava_IdUse55", None)
        self.__picojava_IdUse55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Dot54"):
                opp_val = getattr(old_value, "picojava_Dot54", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Dot54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Dot54"):
                opp_val = getattr(value, "picojava_Dot54", None)
                setattr(value, "picojava_Dot54", self)

    @property
    def picojava_IdUse(self):
        return self.__picojava_IdUse

    @picojava_IdUse.setter
    def picojava_IdUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_IdUse__picojava_IdUse", None)
        self.__picojava_IdUse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_ClassDecl"):
                opp_val = getattr(old_value, "picojava_ClassDecl", None)
                if opp_val == self:
                    setattr(old_value, "picojava_ClassDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_ClassDecl"):
                opp_val = getattr(value, "picojava_ClassDecl", None)
                setattr(value, "picojava_ClassDecl", self)

    @property
    def picojava_IdUse49(self):
        return self.__picojava_IdUse49

    @picojava_IdUse49.setter
    def picojava_IdUse49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_IdUse__picojava_IdUse49", None)
        self.__picojava_IdUse49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Access50"):
                opp_val = getattr(old_value, "picojava_Access50", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Access50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Access50"):
                opp_val = getattr(value, "picojava_Access50", None)
                setattr(value, "picojava_Access50", self)

    def lookup(self, name: str) -> Decl:
        # TODO: Implement lookup method
        pass

class TypeDecl:

    pass
class picojava_ClassDecl(TypeDecl):

    def __init__(self, hasCycleOnSuperclassChain: bool, picojava_ClassDecl: "picojava_IdUse" = None, picojava_ClassDecl24: "picojava_Block" = None, picojava_ClassDecl28: "picojava_ClassDecl" = None, picojava_ClassDecl26: "picojava_ClassDecl" = None):
        self.hasCycleOnSuperclassChain = hasCycleOnSuperclassChain
        self.picojava_ClassDecl = picojava_ClassDecl
        self.picojava_ClassDecl24 = picojava_ClassDecl24
        self.picojava_ClassDecl28 = picojava_ClassDecl28
        self.picojava_ClassDecl26 = picojava_ClassDecl26
        
    @property
    def hasCycleOnSuperclassChain(self) -> bool:
        return self.__hasCycleOnSuperclassChain

    @hasCycleOnSuperclassChain.setter
    def hasCycleOnSuperclassChain(self, hasCycleOnSuperclassChain: bool):
        self.__hasCycleOnSuperclassChain = hasCycleOnSuperclassChain

    @property
    def picojava_ClassDecl28(self):
        return self.__picojava_ClassDecl28

    @picojava_ClassDecl28.setter
    def picojava_ClassDecl28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_ClassDecl__picojava_ClassDecl28", None)
        self.__picojava_ClassDecl28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_ClassDecl26"):
                opp_val = getattr(old_value, "picojava_ClassDecl26", None)
                if opp_val == self:
                    setattr(old_value, "picojava_ClassDecl26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_ClassDecl26"):
                opp_val = getattr(value, "picojava_ClassDecl26", None)
                setattr(value, "picojava_ClassDecl26", self)

    @property
    def picojava_ClassDecl24(self):
        return self.__picojava_ClassDecl24

    @picojava_ClassDecl24.setter
    def picojava_ClassDecl24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_ClassDecl__picojava_ClassDecl24", None)
        self.__picojava_ClassDecl24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Block25"):
                opp_val = getattr(old_value, "picojava_Block25", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Block25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Block25"):
                opp_val = getattr(value, "picojava_Block25", None)
                setattr(value, "picojava_Block25", self)

    @property
    def picojava_ClassDecl26(self):
        return self.__picojava_ClassDecl26

    @picojava_ClassDecl26.setter
    def picojava_ClassDecl26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_ClassDecl__picojava_ClassDecl26", None)
        self.__picojava_ClassDecl26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_ClassDecl28"):
                opp_val = getattr(old_value, "picojava_ClassDecl28", None)
                if opp_val == self:
                    setattr(old_value, "picojava_ClassDecl28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_ClassDecl28"):
                opp_val = getattr(value, "picojava_ClassDecl28", None)
                setattr(value, "picojava_ClassDecl28", self)

    @property
    def picojava_ClassDecl(self):
        return self.__picojava_ClassDecl

    @picojava_ClassDecl.setter
    def picojava_ClassDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_ClassDecl__picojava_ClassDecl", None)
        self.__picojava_ClassDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_IdUse"):
                opp_val = getattr(old_value, "picojava_IdUse", None)
                if opp_val == self:
                    setattr(old_value, "picojava_IdUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_IdUse"):
                opp_val = getattr(value, "picojava_IdUse", None)
                setattr(value, "picojava_IdUse", self)

class picojava_Access(Exp):

    pass
class Stmt:

    pass
class picojava_WhileStmt(Stmt):

    pass
class picojava_AssignStmt(Stmt):

    pass
class Decl:

    pass
class picojava_VarDecl(Decl):

    pass
class BlockStmt:

    pass
class picojava_Stmt(BlockStmt):

    pass
class picojava_Decl(BlockStmt):

    def __init__(self, Name: str, isUnknown: bool, picojava_Decl: "picojava_Block" = None, picojava_Decl12: "picojava_TypeDecl" = None, picojava_Decl15: "picojava_PrimitiveDecl" = None, picojava_Decl21: "picojava_TypeDecl" = None, picojava_Decl47: "picojava_Access" = None):
        self.Name = Name
        self.isUnknown = isUnknown
        self.picojava_Decl = picojava_Decl
        self.picojava_Decl12 = picojava_Decl12
        self.picojava_Decl15 = picojava_Decl15
        self.picojava_Decl21 = picojava_Decl21
        self.picojava_Decl47 = picojava_Decl47
        
    @property
    def isUnknown(self) -> bool:
        return self.__isUnknown

    @isUnknown.setter
    def isUnknown(self, isUnknown: bool):
        self.__isUnknown = isUnknown

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def picojava_Decl15(self):
        return self.__picojava_Decl15

    @picojava_Decl15.setter
    def picojava_Decl15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Decl__picojava_Decl15", None)
        self.__picojava_Decl15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_PrimitiveDecl16"):
                opp_val = getattr(old_value, "picojava_PrimitiveDecl16", None)
                if opp_val == self:
                    setattr(old_value, "picojava_PrimitiveDecl16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_PrimitiveDecl16"):
                opp_val = getattr(value, "picojava_PrimitiveDecl16", None)
                setattr(value, "picojava_PrimitiveDecl16", self)

    @property
    def picojava_Decl21(self):
        return self.__picojava_Decl21

    @picojava_Decl21.setter
    def picojava_Decl21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Decl__picojava_Decl21", None)
        self.__picojava_Decl21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_TypeDecl20"):
                opp_val = getattr(old_value, "picojava_TypeDecl20", None)
                if opp_val == self:
                    setattr(old_value, "picojava_TypeDecl20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_TypeDecl20"):
                opp_val = getattr(value, "picojava_TypeDecl20", None)
                setattr(value, "picojava_TypeDecl20", self)

    @property
    def picojava_Decl47(self):
        return self.__picojava_Decl47

    @picojava_Decl47.setter
    def picojava_Decl47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Decl__picojava_Decl47", None)
        self.__picojava_Decl47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Access46"):
                opp_val = getattr(old_value, "picojava_Access46", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Access46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Access46"):
                opp_val = getattr(value, "picojava_Access46", None)
                setattr(value, "picojava_Access46", self)

    @property
    def picojava_Decl12(self):
        return self.__picojava_Decl12

    @picojava_Decl12.setter
    def picojava_Decl12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Decl__picojava_Decl12", None)
        self.__picojava_Decl12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_TypeDecl13"):
                opp_val = getattr(old_value, "picojava_TypeDecl13", None)
                if opp_val == self:
                    setattr(old_value, "picojava_TypeDecl13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_TypeDecl13"):
                opp_val = getattr(value, "picojava_TypeDecl13", None)
                setattr(value, "picojava_TypeDecl13", self)

    @property
    def picojava_Decl(self):
        return self.__picojava_Decl

    @picojava_Decl.setter
    def picojava_Decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Decl__picojava_Decl", None)
        self.__picojava_Decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Block10"):
                opp_val = getattr(old_value, "picojava_Block10", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Block10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Block10"):
                opp_val = getattr(value, "picojava_Block10", None)
                setattr(value, "picojava_Block10", self)

class picojava_BlockStmt(ABC):

    def __init__(self, picojava_BlockStmt: "picojava_Block" = None):
        self.picojava_BlockStmt = picojava_BlockStmt
        
    @property
    def picojava_BlockStmt(self):
        return self.__picojava_BlockStmt

    @picojava_BlockStmt.setter
    def picojava_BlockStmt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_BlockStmt__picojava_BlockStmt", None)
        self.__picojava_BlockStmt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Block8"):
                opp_val = getattr(old_value, "picojava_Block8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Block8"):
                opp_val = getattr(value, "picojava_Block8", None)
                if opp_val is None:
                    setattr(value, "picojava_Block8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def declarationOf(self, name: str) -> str:
        # TODO: Implement declarationOf method
        pass

class picojava_PrimitiveDecl(TypeDecl):

    pass
class picojava_Block:

    def __init__(self, picojava_Block: "picojava_Program" = None, picojava_Block8: set["picojava_BlockStmt"] = None, picojava_Block10: "picojava_Decl" = None, picojava_Block25: "picojava_ClassDecl" = None):
        self.picojava_Block = picojava_Block
        self.picojava_Block8 = picojava_Block8 if picojava_Block8 is not None else set()
        self.picojava_Block10 = picojava_Block10
        self.picojava_Block25 = picojava_Block25
        
    @property
    def picojava_Block8(self):
        return self.__picojava_Block8

    @picojava_Block8.setter
    def picojava_Block8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Block__picojava_Block8", None)
        self.__picojava_Block8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "picojava_BlockStmt"):
                    opp_val = getattr(item, "picojava_BlockStmt", None)
                    
                    if opp_val == self:
                        setattr(item, "picojava_BlockStmt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "picojava_BlockStmt"):
                    opp_val = getattr(item, "picojava_BlockStmt", None)
                    
                    setattr(item, "picojava_BlockStmt", self)
                    

    @property
    def picojava_Block25(self):
        return self.__picojava_Block25

    @picojava_Block25.setter
    def picojava_Block25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Block__picojava_Block25", None)
        self.__picojava_Block25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_ClassDecl24"):
                opp_val = getattr(old_value, "picojava_ClassDecl24", None)
                if opp_val == self:
                    setattr(old_value, "picojava_ClassDecl24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_ClassDecl24"):
                opp_val = getattr(value, "picojava_ClassDecl24", None)
                setattr(value, "picojava_ClassDecl24", self)

    @property
    def picojava_Block(self):
        return self.__picojava_Block

    @picojava_Block.setter
    def picojava_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Block__picojava_Block", None)
        self.__picojava_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Program"):
                opp_val = getattr(old_value, "picojava_Program", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Program"):
                opp_val = getattr(value, "picojava_Program", None)
                setattr(value, "picojava_Program", self)

    @property
    def picojava_Block10(self):
        return self.__picojava_Block10

    @picojava_Block10.setter
    def picojava_Block10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Block__picojava_Block10", None)
        self.__picojava_Block10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Decl"):
                opp_val = getattr(old_value, "picojava_Decl", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Decl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Decl"):
                opp_val = getattr(value, "picojava_Decl", None)
                setattr(value, "picojava_Decl", self)

    def localLookup(self, name: str) -> str:
        # TODO: Implement localLookup method
        pass

    def lookup(self, name: str) -> str:
        # TODO: Implement lookup method
        pass

class picojava_Program:

    def __init__(self, picojava_Program2: set["picojava_TypeDecl"] = None, picojava_Program4: "picojava_UnknownDecl" = None, picojava_Program: "picojava_Block" = None, picojava_Program6: "picojava_PrimitiveDecl" = None):
        self.picojava_Program2 = picojava_Program2 if picojava_Program2 is not None else set()
        self.picojava_Program4 = picojava_Program4
        self.picojava_Program = picojava_Program
        self.picojava_Program6 = picojava_Program6
        
    @property
    def picojava_Program6(self):
        return self.__picojava_Program6

    @picojava_Program6.setter
    def picojava_Program6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Program__picojava_Program6", None)
        self.__picojava_Program6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_PrimitiveDecl"):
                opp_val = getattr(old_value, "picojava_PrimitiveDecl", None)
                if opp_val == self:
                    setattr(old_value, "picojava_PrimitiveDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_PrimitiveDecl"):
                opp_val = getattr(value, "picojava_PrimitiveDecl", None)
                setattr(value, "picojava_PrimitiveDecl", self)

    @property
    def picojava_Program2(self):
        return self.__picojava_Program2

    @picojava_Program2.setter
    def picojava_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Program__picojava_Program2", None)
        self.__picojava_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "picojava_TypeDecl"):
                    opp_val = getattr(item, "picojava_TypeDecl", None)
                    
                    if opp_val == self:
                        setattr(item, "picojava_TypeDecl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "picojava_TypeDecl"):
                    opp_val = getattr(item, "picojava_TypeDecl", None)
                    
                    setattr(item, "picojava_TypeDecl", self)
                    

    @property
    def picojava_Program(self):
        return self.__picojava_Program

    @picojava_Program.setter
    def picojava_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Program__picojava_Program", None)
        self.__picojava_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Block"):
                opp_val = getattr(old_value, "picojava_Block", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Block"):
                opp_val = getattr(value, "picojava_Block", None)
                setattr(value, "picojava_Block", self)

    @property
    def picojava_Program4(self):
        return self.__picojava_Program4

    @picojava_Program4.setter
    def picojava_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_Program__picojava_Program4", None)
        self.__picojava_Program4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_UnknownDecl"):
                opp_val = getattr(old_value, "picojava_UnknownDecl", None)
                if opp_val == self:
                    setattr(old_value, "picojava_UnknownDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_UnknownDecl"):
                opp_val = getattr(value, "picojava_UnknownDecl", None)
                setattr(value, "picojava_UnknownDecl", self)

    def localLookup(self, name: str) -> str:
        # TODO: Implement localLookup method
        pass

class picojava_UnknownDecl(TypeDecl):

    pass
class picojava_TypeDecl(Decl):

    def __init__(self, isQualified: bool, picojava_TypeDecl: "picojava_Program" = None, picojava_TypeDecl13: "picojava_Decl" = None, picojava_TypeDecl18: "picojava_Access" = None, picojava_TypeDecl20: "picojava_Decl" = None, picojava_TypeDecl44: "picojava_Exp" = None):
        self.isQualified = isQualified
        self.picojava_TypeDecl = picojava_TypeDecl
        self.picojava_TypeDecl13 = picojava_TypeDecl13
        self.picojava_TypeDecl18 = picojava_TypeDecl18
        self.picojava_TypeDecl20 = picojava_TypeDecl20
        self.picojava_TypeDecl44 = picojava_TypeDecl44
        
    @property
    def isQualified(self) -> bool:
        return self.__isQualified

    @isQualified.setter
    def isQualified(self, isQualified: bool):
        self.__isQualified = isQualified

    @property
    def picojava_TypeDecl(self):
        return self.__picojava_TypeDecl

    @picojava_TypeDecl.setter
    def picojava_TypeDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_TypeDecl__picojava_TypeDecl", None)
        self.__picojava_TypeDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Program2"):
                opp_val = getattr(old_value, "picojava_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Program2"):
                opp_val = getattr(value, "picojava_Program2", None)
                if opp_val is None:
                    setattr(value, "picojava_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def picojava_TypeDecl18(self):
        return self.__picojava_TypeDecl18

    @picojava_TypeDecl18.setter
    def picojava_TypeDecl18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_TypeDecl__picojava_TypeDecl18", None)
        self.__picojava_TypeDecl18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Access"):
                opp_val = getattr(old_value, "picojava_Access", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Access", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Access"):
                opp_val = getattr(value, "picojava_Access", None)
                setattr(value, "picojava_Access", self)

    @property
    def picojava_TypeDecl13(self):
        return self.__picojava_TypeDecl13

    @picojava_TypeDecl13.setter
    def picojava_TypeDecl13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_TypeDecl__picojava_TypeDecl13", None)
        self.__picojava_TypeDecl13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Decl12"):
                opp_val = getattr(old_value, "picojava_Decl12", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Decl12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Decl12"):
                opp_val = getattr(value, "picojava_Decl12", None)
                setattr(value, "picojava_Decl12", self)

    @property
    def picojava_TypeDecl44(self):
        return self.__picojava_TypeDecl44

    @picojava_TypeDecl44.setter
    def picojava_TypeDecl44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_TypeDecl__picojava_TypeDecl44", None)
        self.__picojava_TypeDecl44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Exp43"):
                opp_val = getattr(old_value, "picojava_Exp43", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Exp43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Exp43"):
                opp_val = getattr(value, "picojava_Exp43", None)
                setattr(value, "picojava_Exp43", self)

    @property
    def picojava_TypeDecl20(self):
        return self.__picojava_TypeDecl20

    @picojava_TypeDecl20.setter
    def picojava_TypeDecl20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_picojava_TypeDecl__picojava_TypeDecl20", None)
        self.__picojava_TypeDecl20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "picojava_Decl21"):
                opp_val = getattr(old_value, "picojava_Decl21", None)
                if opp_val == self:
                    setattr(old_value, "picojava_Decl21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "picojava_Decl21"):
                opp_val = getattr(value, "picojava_Decl21", None)
                setattr(value, "picojava_Decl21", self)

    def remoteLookup(self, name: str) -> Decl:
        # TODO: Implement remoteLookup method
        pass

    def isSuperTypeOfClassDecl(self, typeDecl: str) -> bool:
        # TODO: Implement isSuperTypeOfClassDecl method
        pass

    def isSuperTypeOf(self, typeDecl: str) -> bool:
        # TODO: Implement isSuperTypeOf method
        pass

    def isSubtypeOf(self, typeDecl: str) -> bool:
        # TODO: Implement isSubtypeOf method
        pass

    def lookup(self, name: str) -> Decl:
        # TODO: Implement lookup method
        pass
