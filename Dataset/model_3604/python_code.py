from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StorageType(Enum):
    INESPRG = "INESPRG"
    INESCHR = "INESCHR"
    INESMAPPER = "INESMAPPER"
    PRGROM = "PRGROM"
    CHRROM = "CHRROM"
    INESMIR = "INESMIR"
    ZP = "ZP"
    INLINE = "INLINE"
    RESET = "RESET"
    NMI = "NMI"
    IRQ = "IRQ"
    MMC3CFG = "MMC3CFG"
class AssignmentType(Enum):
    ASSIGN = "ASSIGN"
    ADD_ASSIGN = "ADD_ASSIGN"
    SUB_ASSIGN = "SUB_ASSIGN"
    MUL_ASSIGN = "MUL_ASSIGN"
    DIV_ASSIGN = "DIV_ASSIGN"
    MOD_ASSIGN = "MOD_ASSIGN"
    BOR_ASSIGN = "BOR_ASSIGN"
    BAN_ASSIGN = "BAN_ASSIGN"
    XOR_ASSIGN = "XOR_ASSIGN"
    BLS_ASSIGN = "BLS_ASSIGN"
    BRS_ASSIGN = "BRS_ASSIGN"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class noop_AndExpression(Expression):

    pass
class noop_MulExpression(Expression):

    pass
class noop_DifferExpression(Expression):

    pass
class noop_IncExpression(Expression):

    pass
class noop_AddExpression(Expression):

    pass
class noop_EqualsExpression(Expression):

    pass
class noop_BXorExpression(Expression):

    pass
class noop_ModExpression(Expression):

    pass
class noop_DecExpression(Expression):

    pass
class noop_GeExpression(Expression):

    pass
class noop_RShiftExpression(Expression):

    pass
class noop_GtExpression(Expression):

    pass
class noop_LShiftExpression(Expression):

    pass
class noop_This(Expression):

    pass
class noop_LeExpression(Expression):

    pass
class noop_OrExpression(Expression):

    pass
class noop_SubExpression(Expression):

    pass
class noop_BAndExpression(Expression):

    pass
class noop_LtExpression(Expression):

    pass
class noop_NewInstance(Expression):

    pass
class noop_MemberSelect(Expression):

    def __init__(self, hasArgs: bool, noop_MemberSelect: "noop_Expression" = None, noop_MemberSelect195: set["noop_Index"] = None, noop_MemberSelect189: "noop_Member" = None, noop_MemberSelect192: set["noop_Expression"] = None):
        self.hasArgs = hasArgs
        self.noop_MemberSelect = noop_MemberSelect
        self.noop_MemberSelect195 = noop_MemberSelect195 if noop_MemberSelect195 is not None else set()
        self.noop_MemberSelect189 = noop_MemberSelect189
        self.noop_MemberSelect192 = noop_MemberSelect192 if noop_MemberSelect192 is not None else set()
        
    @property
    def hasArgs(self) -> bool:
        return self.__hasArgs

    @hasArgs.setter
    def hasArgs(self, hasArgs: bool):
        self.__hasArgs = hasArgs

    @property
    def noop_MemberSelect195(self):
        return self.__noop_MemberSelect195

    @noop_MemberSelect195.setter
    def noop_MemberSelect195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_MemberSelect__noop_MemberSelect195", None)
        self.__noop_MemberSelect195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Index196"):
                    opp_val = getattr(item, "noop_Index196", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Index196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Index196"):
                    opp_val = getattr(item, "noop_Index196", None)
                    
                    setattr(item, "noop_Index196", self)
                    

    @property
    def noop_MemberSelect(self):
        return self.__noop_MemberSelect

    @noop_MemberSelect.setter
    def noop_MemberSelect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_MemberSelect__noop_MemberSelect", None)
        self.__noop_MemberSelect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Expression187"):
                opp_val = getattr(old_value, "noop_Expression187", None)
                if opp_val == self:
                    setattr(old_value, "noop_Expression187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Expression187"):
                opp_val = getattr(value, "noop_Expression187", None)
                setattr(value, "noop_Expression187", self)

    @property
    def noop_MemberSelect189(self):
        return self.__noop_MemberSelect189

    @noop_MemberSelect189.setter
    def noop_MemberSelect189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_MemberSelect__noop_MemberSelect189", None)
        self.__noop_MemberSelect189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Member190"):
                opp_val = getattr(old_value, "noop_Member190", None)
                if opp_val == self:
                    setattr(old_value, "noop_Member190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Member190"):
                opp_val = getattr(value, "noop_Member190", None)
                setattr(value, "noop_Member190", self)

    @property
    def noop_MemberSelect192(self):
        return self.__noop_MemberSelect192

    @noop_MemberSelect192.setter
    def noop_MemberSelect192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_MemberSelect__noop_MemberSelect192", None)
        self.__noop_MemberSelect192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Expression193"):
                    opp_val = getattr(item, "noop_Expression193", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Expression193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Expression193"):
                    opp_val = getattr(item, "noop_Expression193", None)
                    
                    setattr(item, "noop_Expression193", self)
                    

class noop_ArrayLiteral(Expression):

    pass
class noop_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class noop_Super(Expression):

    pass
class noop_ByteLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class noop_NotExpression(Expression):

    pass
class noop_InstanceOfExpression(Expression):

    pass
class noop_BoolLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class noop_DivExpression(Expression):

    pass
class noop_MemberRef(Expression):

    def __init__(self, hasArgs: bool, noop_MemberRef: "noop_Member" = None, noop_MemberRef210: set["noop_Expression"] = None, noop_MemberRef213: set["noop_Index"] = None):
        self.hasArgs = hasArgs
        self.noop_MemberRef = noop_MemberRef
        self.noop_MemberRef210 = noop_MemberRef210 if noop_MemberRef210 is not None else set()
        self.noop_MemberRef213 = noop_MemberRef213 if noop_MemberRef213 is not None else set()
        
    @property
    def hasArgs(self) -> bool:
        return self.__hasArgs

    @hasArgs.setter
    def hasArgs(self, hasArgs: bool):
        self.__hasArgs = hasArgs

    @property
    def noop_MemberRef213(self):
        return self.__noop_MemberRef213

    @noop_MemberRef213.setter
    def noop_MemberRef213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_MemberRef__noop_MemberRef213", None)
        self.__noop_MemberRef213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Index214"):
                    opp_val = getattr(item, "noop_Index214", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Index214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Index214"):
                    opp_val = getattr(item, "noop_Index214", None)
                    
                    setattr(item, "noop_Index214", self)
                    

    @property
    def noop_MemberRef(self):
        return self.__noop_MemberRef

    @noop_MemberRef.setter
    def noop_MemberRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_MemberRef__noop_MemberRef", None)
        self.__noop_MemberRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Member208"):
                opp_val = getattr(old_value, "noop_Member208", None)
                if opp_val == self:
                    setattr(old_value, "noop_Member208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Member208"):
                opp_val = getattr(value, "noop_Member208", None)
                setattr(value, "noop_Member208", self)

    @property
    def noop_MemberRef210(self):
        return self.__noop_MemberRef210

    @noop_MemberRef210.setter
    def noop_MemberRef210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_MemberRef__noop_MemberRef210", None)
        self.__noop_MemberRef210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Expression211"):
                    opp_val = getattr(item, "noop_Expression211", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Expression211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Expression211"):
                    opp_val = getattr(item, "noop_Expression211", None)
                    
                    setattr(item, "noop_Expression211", self)
                    

class noop_CastExpression(Expression):

    pass
class noop_ComplementExpression(Expression):

    pass
class noop_SigPosExpression(Expression):

    pass
class noop_SigNegExpression(Expression):

    pass
class noop_AssignmentExpression(Expression):

    def __init__(self, assignment: str, noop_AssignmentExpression: "noop_Expression" = None, noop_AssignmentExpression69: "noop_Expression" = None):
        self.assignment = assignment
        self.noop_AssignmentExpression = noop_AssignmentExpression
        self.noop_AssignmentExpression69 = noop_AssignmentExpression69
        
    @property
    def assignment(self) -> str:
        return self.__assignment

    @assignment.setter
    def assignment(self, assignment: str):
        self.__assignment = assignment

    @property
    def noop_AssignmentExpression69(self):
        return self.__noop_AssignmentExpression69

    @noop_AssignmentExpression69.setter
    def noop_AssignmentExpression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_AssignmentExpression__noop_AssignmentExpression69", None)
        self.__noop_AssignmentExpression69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Expression70"):
                opp_val = getattr(old_value, "noop_Expression70", None)
                if opp_val == self:
                    setattr(old_value, "noop_Expression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Expression70"):
                opp_val = getattr(value, "noop_Expression70", None)
                setattr(value, "noop_Expression70", self)

    @property
    def noop_AssignmentExpression(self):
        return self.__noop_AssignmentExpression

    @noop_AssignmentExpression.setter
    def noop_AssignmentExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_AssignmentExpression__noop_AssignmentExpression", None)
        self.__noop_AssignmentExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Expression67"):
                opp_val = getattr(old_value, "noop_Expression67", None)
                if opp_val == self:
                    setattr(old_value, "noop_Expression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Expression67"):
                opp_val = getattr(value, "noop_Expression67", None)
                setattr(value, "noop_Expression67", self)

class noop_BOrExpression(Expression):

    pass
class noop_Index:

    pass
class noop_ConstructorField:

    pass
class noop_Constructor:

    pass
class noop_ElseStatement:

    def __init__(self, name: str, noop_ElseStatement: "noop_IfStatement" = None, noop_ElseStatement31: "noop_Block" = None, noop_ElseStatement34: "noop_IfStatement" = None):
        self.name = name
        self.noop_ElseStatement = noop_ElseStatement
        self.noop_ElseStatement31 = noop_ElseStatement31
        self.noop_ElseStatement34 = noop_ElseStatement34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noop_ElseStatement34(self):
        return self.__noop_ElseStatement34

    @noop_ElseStatement34.setter
    def noop_ElseStatement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ElseStatement__noop_ElseStatement34", None)
        self.__noop_ElseStatement34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_IfStatement35"):
                opp_val = getattr(old_value, "noop_IfStatement35", None)
                if opp_val == self:
                    setattr(old_value, "noop_IfStatement35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_IfStatement35"):
                opp_val = getattr(value, "noop_IfStatement35", None)
                setattr(value, "noop_IfStatement35", self)

    @property
    def noop_ElseStatement31(self):
        return self.__noop_ElseStatement31

    @noop_ElseStatement31.setter
    def noop_ElseStatement31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ElseStatement__noop_ElseStatement31", None)
        self.__noop_ElseStatement31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Block32"):
                opp_val = getattr(old_value, "noop_Block32", None)
                if opp_val == self:
                    setattr(old_value, "noop_Block32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Block32"):
                opp_val = getattr(value, "noop_Block32", None)
                setattr(value, "noop_Block32", self)

    @property
    def noop_ElseStatement(self):
        return self.__noop_ElseStatement

    @noop_ElseStatement.setter
    def noop_ElseStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ElseStatement__noop_ElseStatement", None)
        self.__noop_ElseStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_IfStatement29"):
                opp_val = getattr(old_value, "noop_IfStatement29", None)
                if opp_val == self:
                    setattr(old_value, "noop_IfStatement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_IfStatement29"):
                opp_val = getattr(value, "noop_IfStatement29", None)
                setattr(value, "noop_IfStatement29", self)

class noop_Statement:

    pass
class noop_Block:

    pass
class noop_Length:

    pass
class Statement:

    pass
class noop_ForeverStatement(Statement):

    def __init__(self, name: str, noop_ForeverStatement: "noop_Block" = None):
        self.name = name
        self.noop_ForeverStatement = noop_ForeverStatement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noop_ForeverStatement(self):
        return self.__noop_ForeverStatement

    @noop_ForeverStatement.setter
    def noop_ForeverStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ForeverStatement__noop_ForeverStatement", None)
        self.__noop_ForeverStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Block51"):
                opp_val = getattr(old_value, "noop_Block51", None)
                if opp_val == self:
                    setattr(old_value, "noop_Block51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Block51"):
                opp_val = getattr(value, "noop_Block51", None)
                setattr(value, "noop_Block51", self)

class noop_BreakStatement(Statement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class noop_ContinueStatement(Statement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class noop_ForStatement(Statement):

    def __init__(self, name: str, noop_ForStatement42: "noop_Expression" = None, noop_ForStatement: set["noop_Variable"] = None, noop_ForStatement39: set["noop_Expression"] = None, noop_ForStatement45: set["noop_Expression"] = None, noop_ForStatement48: "noop_Block" = None):
        self.name = name
        self.noop_ForStatement42 = noop_ForStatement42
        self.noop_ForStatement = noop_ForStatement if noop_ForStatement is not None else set()
        self.noop_ForStatement39 = noop_ForStatement39 if noop_ForStatement39 is not None else set()
        self.noop_ForStatement45 = noop_ForStatement45 if noop_ForStatement45 is not None else set()
        self.noop_ForStatement48 = noop_ForStatement48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noop_ForStatement(self):
        return self.__noop_ForStatement

    @noop_ForStatement.setter
    def noop_ForStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ForStatement__noop_ForStatement", None)
        self.__noop_ForStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Variable37"):
                    opp_val = getattr(item, "noop_Variable37", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Variable37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Variable37"):
                    opp_val = getattr(item, "noop_Variable37", None)
                    
                    setattr(item, "noop_Variable37", self)
                    

    @property
    def noop_ForStatement39(self):
        return self.__noop_ForStatement39

    @noop_ForStatement39.setter
    def noop_ForStatement39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ForStatement__noop_ForStatement39", None)
        self.__noop_ForStatement39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Expression40"):
                    opp_val = getattr(item, "noop_Expression40", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Expression40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Expression40"):
                    opp_val = getattr(item, "noop_Expression40", None)
                    
                    setattr(item, "noop_Expression40", self)
                    

    @property
    def noop_ForStatement45(self):
        return self.__noop_ForStatement45

    @noop_ForStatement45.setter
    def noop_ForStatement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ForStatement__noop_ForStatement45", None)
        self.__noop_ForStatement45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Expression46"):
                    opp_val = getattr(item, "noop_Expression46", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Expression46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Expression46"):
                    opp_val = getattr(item, "noop_Expression46", None)
                    
                    setattr(item, "noop_Expression46", self)
                    

    @property
    def noop_ForStatement48(self):
        return self.__noop_ForStatement48

    @noop_ForStatement48.setter
    def noop_ForStatement48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ForStatement__noop_ForStatement48", None)
        self.__noop_ForStatement48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Block49"):
                opp_val = getattr(old_value, "noop_Block49", None)
                if opp_val == self:
                    setattr(old_value, "noop_Block49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Block49"):
                opp_val = getattr(value, "noop_Block49", None)
                setattr(value, "noop_Block49", self)

    @property
    def noop_ForStatement42(self):
        return self.__noop_ForStatement42

    @noop_ForStatement42.setter
    def noop_ForStatement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ForStatement__noop_ForStatement42", None)
        self.__noop_ForStatement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Expression43"):
                opp_val = getattr(old_value, "noop_Expression43", None)
                if opp_val == self:
                    setattr(old_value, "noop_Expression43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Expression43"):
                opp_val = getattr(value, "noop_Expression43", None)
                setattr(value, "noop_Expression43", self)

class noop_AsmStatement(Statement):

    def __init__(self, codes: str, noop_AsmStatement: set["noop_Expression"] = None):
        self.codes = codes
        self.noop_AsmStatement = noop_AsmStatement if noop_AsmStatement is not None else set()
        
    @property
    def codes(self) -> str:
        return self.__codes

    @codes.setter
    def codes(self, codes: str):
        self.__codes = codes

    @property
    def noop_AsmStatement(self):
        return self.__noop_AsmStatement

    @noop_AsmStatement.setter
    def noop_AsmStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_AsmStatement__noop_AsmStatement", None)
        self.__noop_AsmStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Expression53"):
                    opp_val = getattr(item, "noop_Expression53", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Expression53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Expression53"):
                    opp_val = getattr(item, "noop_Expression53", None)
                    
                    setattr(item, "noop_Expression53", self)
                    

class noop_ReturnStatement(Statement):

    def __init__(self, name: str, noop_ReturnStatement: "noop_Expression" = None):
        self.name = name
        self.noop_ReturnStatement = noop_ReturnStatement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noop_ReturnStatement(self):
        return self.__noop_ReturnStatement

    @noop_ReturnStatement.setter
    def noop_ReturnStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_ReturnStatement__noop_ReturnStatement", None)
        self.__noop_ReturnStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Expression22"):
                opp_val = getattr(old_value, "noop_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "noop_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Expression22"):
                opp_val = getattr(value, "noop_Expression22", None)
                setattr(value, "noop_Expression22", self)

class noop_IfStatement(Statement):

    def __init__(self, name: str, noop_IfStatement: "noop_Expression" = None, noop_IfStatement26: "noop_Block" = None, noop_IfStatement29: "noop_ElseStatement" = None, noop_IfStatement35: "noop_ElseStatement" = None):
        self.name = name
        self.noop_IfStatement = noop_IfStatement
        self.noop_IfStatement26 = noop_IfStatement26
        self.noop_IfStatement29 = noop_IfStatement29
        self.noop_IfStatement35 = noop_IfStatement35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noop_IfStatement(self):
        return self.__noop_IfStatement

    @noop_IfStatement.setter
    def noop_IfStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_IfStatement__noop_IfStatement", None)
        self.__noop_IfStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Expression24"):
                opp_val = getattr(old_value, "noop_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "noop_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Expression24"):
                opp_val = getattr(value, "noop_Expression24", None)
                setattr(value, "noop_Expression24", self)

    @property
    def noop_IfStatement35(self):
        return self.__noop_IfStatement35

    @noop_IfStatement35.setter
    def noop_IfStatement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_IfStatement__noop_IfStatement35", None)
        self.__noop_IfStatement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_ElseStatement34"):
                opp_val = getattr(old_value, "noop_ElseStatement34", None)
                if opp_val == self:
                    setattr(old_value, "noop_ElseStatement34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_ElseStatement34"):
                opp_val = getattr(value, "noop_ElseStatement34", None)
                setattr(value, "noop_ElseStatement34", self)

    @property
    def noop_IfStatement29(self):
        return self.__noop_IfStatement29

    @noop_IfStatement29.setter
    def noop_IfStatement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_IfStatement__noop_IfStatement29", None)
        self.__noop_IfStatement29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_ElseStatement"):
                opp_val = getattr(old_value, "noop_ElseStatement", None)
                if opp_val == self:
                    setattr(old_value, "noop_ElseStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_ElseStatement"):
                opp_val = getattr(value, "noop_ElseStatement", None)
                setattr(value, "noop_ElseStatement", self)

    @property
    def noop_IfStatement26(self):
        return self.__noop_IfStatement26

    @noop_IfStatement26.setter
    def noop_IfStatement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_IfStatement__noop_IfStatement26", None)
        self.__noop_IfStatement26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Block27"):
                opp_val = getattr(old_value, "noop_Block27", None)
                if opp_val == self:
                    setattr(old_value, "noop_Block27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Block27"):
                opp_val = getattr(value, "noop_Block27", None)
                setattr(value, "noop_Block27", self)

class Member:

    pass
class noop_Method(Member):

    pass
class noop_Variable(Statement, Member):

    pass
class noop_Expression(Statement):

    pass
class noop_Storage:

    def __init__(self, type: str, noop_Storage: "noop_Member" = None, noop_Storage7: "noop_Expression" = None):
        self.type = type
        self.noop_Storage = noop_Storage
        self.noop_Storage7 = noop_Storage7
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def noop_Storage(self):
        return self.__noop_Storage

    @noop_Storage.setter
    def noop_Storage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_Storage__noop_Storage", None)
        self.__noop_Storage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Member5"):
                opp_val = getattr(old_value, "noop_Member5", None)
                if opp_val == self:
                    setattr(old_value, "noop_Member5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Member5"):
                opp_val = getattr(value, "noop_Member5", None)
                setattr(value, "noop_Member5", self)

    @property
    def noop_Storage7(self):
        return self.__noop_Storage7

    @noop_Storage7.setter
    def noop_Storage7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_Storage__noop_Storage7", None)
        self.__noop_Storage7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Expression"):
                opp_val = getattr(old_value, "noop_Expression", None)
                if opp_val == self:
                    setattr(old_value, "noop_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Expression"):
                opp_val = getattr(value, "noop_Expression", None)
                setattr(value, "noop_Expression", self)

class noop_Member:

    def __init__(self, name: str, noop_Member: "noop_NoopClass" = None, noop_Member5: "noop_Storage" = None, noop_Member190: "noop_MemberSelect" = None, noop_Member208: "noop_MemberRef" = None):
        self.name = name
        self.noop_Member = noop_Member
        self.noop_Member5 = noop_Member5
        self.noop_Member190 = noop_Member190
        self.noop_Member208 = noop_Member208
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noop_Member208(self):
        return self.__noop_Member208

    @noop_Member208.setter
    def noop_Member208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_Member__noop_Member208", None)
        self.__noop_Member208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_MemberRef"):
                opp_val = getattr(old_value, "noop_MemberRef", None)
                if opp_val == self:
                    setattr(old_value, "noop_MemberRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_MemberRef"):
                opp_val = getattr(value, "noop_MemberRef", None)
                setattr(value, "noop_MemberRef", self)

    @property
    def noop_Member190(self):
        return self.__noop_Member190

    @noop_Member190.setter
    def noop_Member190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_Member__noop_Member190", None)
        self.__noop_Member190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_MemberSelect189"):
                opp_val = getattr(old_value, "noop_MemberSelect189", None)
                if opp_val == self:
                    setattr(old_value, "noop_MemberSelect189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_MemberSelect189"):
                opp_val = getattr(value, "noop_MemberSelect189", None)
                setattr(value, "noop_MemberSelect189", self)

    @property
    def noop_Member5(self):
        return self.__noop_Member5

    @noop_Member5.setter
    def noop_Member5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_Member__noop_Member5", None)
        self.__noop_Member5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Storage"):
                opp_val = getattr(old_value, "noop_Storage", None)
                if opp_val == self:
                    setattr(old_value, "noop_Storage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Storage"):
                opp_val = getattr(value, "noop_Storage", None)
                setattr(value, "noop_Storage", self)

    @property
    def noop_Member(self):
        return self.__noop_Member

    @noop_Member.setter
    def noop_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_Member__noop_Member", None)
        self.__noop_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_NoopClass3"):
                opp_val = getattr(old_value, "noop_NoopClass3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_NoopClass3"):
                opp_val = getattr(value, "noop_NoopClass3", None)
                if opp_val is None:
                    setattr(value, "noop_NoopClass3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class noop_NoopClass:

    def __init__(self, name: str, noop_NoopClass: "noop_NoopClass" = None, noop_NoopClass0: "noop_NoopClass" = None, noop_NoopClass3: set["noop_Member"] = None, noop_NoopClass12: "noop_Variable" = None, noop_NoopClass130: "noop_InstanceOfExpression" = None, noop_NoopClass170: "noop_CastExpression" = None, noop_NoopClass200: "noop_NewInstance" = None):
        self.name = name
        self.noop_NoopClass = noop_NoopClass
        self.noop_NoopClass0 = noop_NoopClass0
        self.noop_NoopClass3 = noop_NoopClass3 if noop_NoopClass3 is not None else set()
        self.noop_NoopClass12 = noop_NoopClass12
        self.noop_NoopClass130 = noop_NoopClass130
        self.noop_NoopClass170 = noop_NoopClass170
        self.noop_NoopClass200 = noop_NoopClass200
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def noop_NoopClass170(self):
        return self.__noop_NoopClass170

    @noop_NoopClass170.setter
    def noop_NoopClass170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_NoopClass__noop_NoopClass170", None)
        self.__noop_NoopClass170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_CastExpression169"):
                opp_val = getattr(old_value, "noop_CastExpression169", None)
                if opp_val == self:
                    setattr(old_value, "noop_CastExpression169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_CastExpression169"):
                opp_val = getattr(value, "noop_CastExpression169", None)
                setattr(value, "noop_CastExpression169", self)

    @property
    def noop_NoopClass12(self):
        return self.__noop_NoopClass12

    @noop_NoopClass12.setter
    def noop_NoopClass12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_NoopClass__noop_NoopClass12", None)
        self.__noop_NoopClass12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_Variable11"):
                opp_val = getattr(old_value, "noop_Variable11", None)
                if opp_val == self:
                    setattr(old_value, "noop_Variable11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_Variable11"):
                opp_val = getattr(value, "noop_Variable11", None)
                setattr(value, "noop_Variable11", self)

    @property
    def noop_NoopClass130(self):
        return self.__noop_NoopClass130

    @noop_NoopClass130.setter
    def noop_NoopClass130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_NoopClass__noop_NoopClass130", None)
        self.__noop_NoopClass130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_InstanceOfExpression129"):
                opp_val = getattr(old_value, "noop_InstanceOfExpression129", None)
                if opp_val == self:
                    setattr(old_value, "noop_InstanceOfExpression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_InstanceOfExpression129"):
                opp_val = getattr(value, "noop_InstanceOfExpression129", None)
                setattr(value, "noop_InstanceOfExpression129", self)

    @property
    def noop_NoopClass200(self):
        return self.__noop_NoopClass200

    @noop_NoopClass200.setter
    def noop_NoopClass200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_NoopClass__noop_NoopClass200", None)
        self.__noop_NoopClass200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_NewInstance"):
                opp_val = getattr(old_value, "noop_NewInstance", None)
                if opp_val == self:
                    setattr(old_value, "noop_NewInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_NewInstance"):
                opp_val = getattr(value, "noop_NewInstance", None)
                setattr(value, "noop_NewInstance", self)

    @property
    def noop_NoopClass(self):
        return self.__noop_NoopClass

    @noop_NoopClass.setter
    def noop_NoopClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_NoopClass__noop_NoopClass", None)
        self.__noop_NoopClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_NoopClass0"):
                opp_val = getattr(old_value, "noop_NoopClass0", None)
                if opp_val == self:
                    setattr(old_value, "noop_NoopClass0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_NoopClass0"):
                opp_val = getattr(value, "noop_NoopClass0", None)
                setattr(value, "noop_NoopClass0", self)

    @property
    def noop_NoopClass0(self):
        return self.__noop_NoopClass0

    @noop_NoopClass0.setter
    def noop_NoopClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_NoopClass__noop_NoopClass0", None)
        self.__noop_NoopClass0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "noop_NoopClass"):
                opp_val = getattr(old_value, "noop_NoopClass", None)
                if opp_val == self:
                    setattr(old_value, "noop_NoopClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "noop_NoopClass"):
                opp_val = getattr(value, "noop_NoopClass", None)
                setattr(value, "noop_NoopClass", self)

    @property
    def noop_NoopClass3(self):
        return self.__noop_NoopClass3

    @noop_NoopClass3.setter
    def noop_NoopClass3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_noop_NoopClass__noop_NoopClass3", None)
        self.__noop_NoopClass3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "noop_Member"):
                    opp_val = getattr(item, "noop_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "noop_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "noop_Member"):
                    opp_val = getattr(item, "noop_Member", None)
                    
                    setattr(item, "noop_Member", self)
                    
