from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ArithmeticExpression:

    pass
class siple_Subtraction(ArithmeticExpression):

    pass
class siple_Division(ArithmeticExpression):

    pass
class siple_Multiplication(ArithmeticExpression):

    pass
class siple_Addition(ArithmeticExpression):

    pass
class UnaryExpression:

    pass
class siple_Dereference(UnaryExpression):

    pass
class siple_UMinus(UnaryExpression):

    pass
class siple_RealCoercion(UnaryExpression):

    pass
class siple_Not(UnaryExpression):

    pass
class EqualityExpression:

    pass
class siple_GreaterThanEqual(EqualityExpression):

    pass
class siple_LesserThanEqual(EqualityExpression):

    pass
class siple_GreaterThan(EqualityExpression):

    pass
class siple_LesserThan(EqualityExpression):

    pass
class siple_Equal(EqualityExpression):

    pass
class LogicExpression:

    pass
class siple_Or(LogicExpression):

    pass
class siple_And(LogicExpression):

    pass
class BinaryExpression:

    pass
class siple_ArithmeticExpression(BinaryExpression):

    pass
class siple_EqualityExpression(BinaryExpression):

    pass
class siple_LogicExpression(BinaryExpression):

    pass
class Declaration:

    pass
class siple_VariableDeclaration(Declaration):

    def __init__(self, DeclaredType: str, siple_VariableDeclaration: "siple_ProcedureDeclaration" = None):
        self.DeclaredType = DeclaredType
        self.siple_VariableDeclaration = siple_VariableDeclaration
        
    @property
    def DeclaredType(self) -> str:
        return self.__DeclaredType

    @DeclaredType.setter
    def DeclaredType(self, DeclaredType: str):
        self.__DeclaredType = DeclaredType

    @property
    def siple_VariableDeclaration(self):
        return self.__siple_VariableDeclaration

    @siple_VariableDeclaration.setter
    def siple_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_VariableDeclaration__siple_VariableDeclaration", None)
        self.__siple_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_ProcedureDeclaration34"):
                opp_val = getattr(old_value, "siple_ProcedureDeclaration34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_ProcedureDeclaration34"):
                opp_val = getattr(value, "siple_ProcedureDeclaration34", None)
                if opp_val is None:
                    setattr(value, "siple_ProcedureDeclaration34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expression:

    pass
class siple_Reference(Expression):

    def __init__(self, Name: str, siple_Reference: "siple_Declaration" = None):
        self.Name = Name
        self.siple_Reference = siple_Reference
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def siple_Reference(self):
        return self.__siple_Reference

    @siple_Reference.setter
    def siple_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Reference__siple_Reference", None)
        self.__siple_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Declaration39"):
                opp_val = getattr(old_value, "siple_Declaration39", None)
                if opp_val == self:
                    setattr(old_value, "siple_Declaration39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Declaration39"):
                opp_val = getattr(value, "siple_Declaration39", None)
                setattr(value, "siple_Declaration39", self)

class siple_NestedExpression(Expression):

    pass
class siple_BinaryExpression(Expression):

    pass
class siple_ProcedureCall(Expression):

    pass
class siple_UnaryExpression(Expression):

    pass
class siple_Constant(Expression):

    def __init__(self, Lexem: str, AsBoolean: str, AsInteger: str, AsReal: str):
        self.Lexem = Lexem
        self.AsBoolean = AsBoolean
        self.AsInteger = AsInteger
        self.AsReal = AsReal
        
    @property
    def AsInteger(self) -> str:
        return self.__AsInteger

    @AsInteger.setter
    def AsInteger(self, AsInteger: str):
        self.__AsInteger = AsInteger

    @property
    def AsReal(self) -> str:
        return self.__AsReal

    @AsReal.setter
    def AsReal(self, AsReal: str):
        self.__AsReal = AsReal

    @property
    def AsBoolean(self) -> str:
        return self.__AsBoolean

    @AsBoolean.setter
    def AsBoolean(self, AsBoolean: str):
        self.__AsBoolean = AsBoolean

    @property
    def Lexem(self) -> str:
        return self.__Lexem

    @Lexem.setter
    def Lexem(self, Lexem: str):
        self.__Lexem = Lexem

class Statement:

    pass
class siple_ProcedureReturn(Statement):

    def __init__(self, Type: str, siple_ProcedureReturn: "siple_Expression" = None):
        self.Type = Type
        self.siple_ProcedureReturn = siple_ProcedureReturn
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def siple_ProcedureReturn(self):
        return self.__siple_ProcedureReturn

    @siple_ProcedureReturn.setter
    def siple_ProcedureReturn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_ProcedureReturn__siple_ProcedureReturn", None)
        self.__siple_ProcedureReturn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Expression28"):
                opp_val = getattr(old_value, "siple_Expression28", None)
                if opp_val == self:
                    setattr(old_value, "siple_Expression28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Expression28"):
                opp_val = getattr(value, "siple_Expression28", None)
                setattr(value, "siple_Expression28", self)

class siple_Write(Statement):

    def __init__(self, Type: str, siple_Write: "siple_Expression" = None):
        self.Type = Type
        self.siple_Write = siple_Write
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def siple_Write(self):
        return self.__siple_Write

    @siple_Write.setter
    def siple_Write(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Write__siple_Write", None)
        self.__siple_Write = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Expression30"):
                opp_val = getattr(old_value, "siple_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "siple_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Expression30"):
                opp_val = getattr(value, "siple_Expression30", None)
                setattr(value, "siple_Expression30", self)

class siple_If(Statement):

    pass
class siple_Read(Statement):

    def __init__(self, Type: str, siple_Read: "siple_Expression" = None):
        self.Type = Type
        self.siple_Read = siple_Read
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def siple_Read(self):
        return self.__siple_Read

    @siple_Read.setter
    def siple_Read(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Read__siple_Read", None)
        self.__siple_Read = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Expression32"):
                opp_val = getattr(old_value, "siple_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "siple_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Expression32"):
                opp_val = getattr(value, "siple_Expression32", None)
                setattr(value, "siple_Expression32", self)

class siple_Block(Statement):

    pass
class siple_Statement(ABC):

    def __init__(self, siple_Statement: "siple_ProcedureDeclaration" = None, siple_Statement6: "siple_Block" = None):
        self.siple_Statement = siple_Statement
        self.siple_Statement6 = siple_Statement6
        
    @property
    def siple_Statement6(self):
        return self.__siple_Statement6

    @siple_Statement6.setter
    def siple_Statement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Statement__siple_Statement6", None)
        self.__siple_Statement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Block"):
                opp_val = getattr(old_value, "siple_Block", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Block"):
                opp_val = getattr(value, "siple_Block", None)
                if opp_val is None:
                    setattr(value, "siple_Block", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def siple_Statement(self):
        return self.__siple_Statement

    @siple_Statement.setter
    def siple_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Statement__siple_Statement", None)
        self.__siple_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_ProcedureDeclaration4"):
                opp_val = getattr(old_value, "siple_ProcedureDeclaration4", None)
                if opp_val == self:
                    setattr(old_value, "siple_ProcedureDeclaration4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_ProcedureDeclaration4"):
                opp_val = getattr(value, "siple_ProcedureDeclaration4", None)
                setattr(value, "siple_ProcedureDeclaration4", self)

    def Interpret(self, vm: str):
        # TODO: Implement Interpret method
        pass

class siple_ProcedureDeclaration(Declaration):

    def __init__(self, ReturnType: str, siple_ProcedureDeclaration: "siple_CompilationUnit" = None, siple_ProcedureDeclaration4: "siple_Statement" = None, siple_ProcedureDeclaration9: "siple_Block" = None, siple_ProcedureDeclaration36: "siple_Block" = None, siple_ProcedureDeclaration47: "siple_ProcedureCall" = None, siple_ProcedureDeclaration34: set["siple_VariableDeclaration"] = None):
        self.ReturnType = ReturnType
        self.siple_ProcedureDeclaration = siple_ProcedureDeclaration
        self.siple_ProcedureDeclaration4 = siple_ProcedureDeclaration4
        self.siple_ProcedureDeclaration9 = siple_ProcedureDeclaration9
        self.siple_ProcedureDeclaration36 = siple_ProcedureDeclaration36
        self.siple_ProcedureDeclaration47 = siple_ProcedureDeclaration47
        self.siple_ProcedureDeclaration34 = siple_ProcedureDeclaration34 if siple_ProcedureDeclaration34 is not None else set()
        
    @property
    def ReturnType(self) -> str:
        return self.__ReturnType

    @ReturnType.setter
    def ReturnType(self, ReturnType: str):
        self.__ReturnType = ReturnType

    @property
    def siple_ProcedureDeclaration9(self):
        return self.__siple_ProcedureDeclaration9

    @siple_ProcedureDeclaration9.setter
    def siple_ProcedureDeclaration9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_ProcedureDeclaration__siple_ProcedureDeclaration9", None)
        self.__siple_ProcedureDeclaration9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Block8"):
                opp_val = getattr(old_value, "siple_Block8", None)
                if opp_val == self:
                    setattr(old_value, "siple_Block8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Block8"):
                opp_val = getattr(value, "siple_Block8", None)
                setattr(value, "siple_Block8", self)

    @property
    def siple_ProcedureDeclaration36(self):
        return self.__siple_ProcedureDeclaration36

    @siple_ProcedureDeclaration36.setter
    def siple_ProcedureDeclaration36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_ProcedureDeclaration__siple_ProcedureDeclaration36", None)
        self.__siple_ProcedureDeclaration36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Block37"):
                opp_val = getattr(old_value, "siple_Block37", None)
                if opp_val == self:
                    setattr(old_value, "siple_Block37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Block37"):
                opp_val = getattr(value, "siple_Block37", None)
                setattr(value, "siple_Block37", self)

    @property
    def siple_ProcedureDeclaration34(self):
        return self.__siple_ProcedureDeclaration34

    @siple_ProcedureDeclaration34.setter
    def siple_ProcedureDeclaration34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_ProcedureDeclaration__siple_ProcedureDeclaration34", None)
        self.__siple_ProcedureDeclaration34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "siple_VariableDeclaration"):
                    opp_val = getattr(item, "siple_VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "siple_VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "siple_VariableDeclaration"):
                    opp_val = getattr(item, "siple_VariableDeclaration", None)
                    
                    setattr(item, "siple_VariableDeclaration", self)
                    

    @property
    def siple_ProcedureDeclaration47(self):
        return self.__siple_ProcedureDeclaration47

    @siple_ProcedureDeclaration47.setter
    def siple_ProcedureDeclaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_ProcedureDeclaration__siple_ProcedureDeclaration47", None)
        self.__siple_ProcedureDeclaration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_ProcedureCall46"):
                opp_val = getattr(old_value, "siple_ProcedureCall46", None)
                if opp_val == self:
                    setattr(old_value, "siple_ProcedureCall46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_ProcedureCall46"):
                opp_val = getattr(value, "siple_ProcedureCall46", None)
                setattr(value, "siple_ProcedureCall46", self)

    @property
    def siple_ProcedureDeclaration(self):
        return self.__siple_ProcedureDeclaration

    @siple_ProcedureDeclaration.setter
    def siple_ProcedureDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_ProcedureDeclaration__siple_ProcedureDeclaration", None)
        self.__siple_ProcedureDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_CompilationUnit2"):
                opp_val = getattr(old_value, "siple_CompilationUnit2", None)
                if opp_val == self:
                    setattr(old_value, "siple_CompilationUnit2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_CompilationUnit2"):
                opp_val = getattr(value, "siple_CompilationUnit2", None)
                setattr(value, "siple_CompilationUnit2", self)

    @property
    def siple_ProcedureDeclaration4(self):
        return self.__siple_ProcedureDeclaration4

    @siple_ProcedureDeclaration4.setter
    def siple_ProcedureDeclaration4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_ProcedureDeclaration__siple_ProcedureDeclaration4", None)
        self.__siple_ProcedureDeclaration4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Statement"):
                opp_val = getattr(old_value, "siple_Statement", None)
                if opp_val == self:
                    setattr(old_value, "siple_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Statement"):
                opp_val = getattr(value, "siple_Statement", None)
                setattr(value, "siple_Statement", self)

class siple_VariableAssignment(Statement):

    def __init__(self, Type: str, siple_VariableAssignment: "siple_Expression" = None, siple_VariableAssignment25: "siple_Expression" = None):
        self.Type = Type
        self.siple_VariableAssignment = siple_VariableAssignment
        self.siple_VariableAssignment25 = siple_VariableAssignment25
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def siple_VariableAssignment(self):
        return self.__siple_VariableAssignment

    @siple_VariableAssignment.setter
    def siple_VariableAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_VariableAssignment__siple_VariableAssignment", None)
        self.__siple_VariableAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Expression23"):
                opp_val = getattr(old_value, "siple_Expression23", None)
                if opp_val == self:
                    setattr(old_value, "siple_Expression23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Expression23"):
                opp_val = getattr(value, "siple_Expression23", None)
                setattr(value, "siple_Expression23", self)

    @property
    def siple_VariableAssignment25(self):
        return self.__siple_VariableAssignment25

    @siple_VariableAssignment25.setter
    def siple_VariableAssignment25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_VariableAssignment__siple_VariableAssignment25", None)
        self.__siple_VariableAssignment25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Expression26"):
                opp_val = getattr(old_value, "siple_Expression26", None)
                if opp_val == self:
                    setattr(old_value, "siple_Expression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Expression26"):
                opp_val = getattr(value, "siple_Expression26", None)
                setattr(value, "siple_Expression26", self)

class siple_Declaration(Statement):

    def __init__(self, Name: str, IsParameterDeclaration: bool, Type: str, siple_Declaration: "siple_CompilationUnit" = None, siple_Declaration39: "siple_Reference" = None):
        self.Name = Name
        self.IsParameterDeclaration = IsParameterDeclaration
        self.Type = Type
        self.siple_Declaration = siple_Declaration
        self.siple_Declaration39 = siple_Declaration39
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def IsParameterDeclaration(self) -> bool:
        return self.__IsParameterDeclaration

    @IsParameterDeclaration.setter
    def IsParameterDeclaration(self, IsParameterDeclaration: bool):
        self.__IsParameterDeclaration = IsParameterDeclaration

    @property
    def siple_Declaration39(self):
        return self.__siple_Declaration39

    @siple_Declaration39.setter
    def siple_Declaration39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Declaration__siple_Declaration39", None)
        self.__siple_Declaration39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Reference"):
                opp_val = getattr(old_value, "siple_Reference", None)
                if opp_val == self:
                    setattr(old_value, "siple_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Reference"):
                opp_val = getattr(value, "siple_Reference", None)
                setattr(value, "siple_Reference", self)

    @property
    def siple_Declaration(self):
        return self.__siple_Declaration

    @siple_Declaration.setter
    def siple_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Declaration__siple_Declaration", None)
        self.__siple_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_CompilationUnit"):
                opp_val = getattr(old_value, "siple_CompilationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_CompilationUnit"):
                opp_val = getattr(value, "siple_CompilationUnit", None)
                if opp_val is None:
                    setattr(value, "siple_CompilationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class siple_While(Statement):

    pass
class siple_Expression(Statement):

    def __init__(self, Type: str, siple_Expression: "siple_If" = None, siple_Expression18: "siple_While" = None, siple_Expression30: "siple_Write" = None, siple_Expression32: "siple_Read" = None, siple_Expression23: "siple_VariableAssignment" = None, siple_Expression26: "siple_VariableAssignment" = None, siple_Expression28: "siple_ProcedureReturn" = None, siple_Expression41: "siple_ProcedureCall" = None, siple_Expression44: "siple_ProcedureCall" = None, siple_Expression53: "siple_BinaryExpression" = None, siple_Expression56: "siple_BinaryExpression" = None, siple_Expression49: "siple_NestedExpression" = None, siple_Expression51: "siple_UnaryExpression" = None):
        self.Type = Type
        self.siple_Expression = siple_Expression
        self.siple_Expression18 = siple_Expression18
        self.siple_Expression30 = siple_Expression30
        self.siple_Expression32 = siple_Expression32
        self.siple_Expression23 = siple_Expression23
        self.siple_Expression26 = siple_Expression26
        self.siple_Expression28 = siple_Expression28
        self.siple_Expression41 = siple_Expression41
        self.siple_Expression44 = siple_Expression44
        self.siple_Expression53 = siple_Expression53
        self.siple_Expression56 = siple_Expression56
        self.siple_Expression49 = siple_Expression49
        self.siple_Expression51 = siple_Expression51
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def siple_Expression53(self):
        return self.__siple_Expression53

    @siple_Expression53.setter
    def siple_Expression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression53", None)
        self.__siple_Expression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_BinaryExpression"):
                opp_val = getattr(old_value, "siple_BinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "siple_BinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_BinaryExpression"):
                opp_val = getattr(value, "siple_BinaryExpression", None)
                setattr(value, "siple_BinaryExpression", self)

    @property
    def siple_Expression28(self):
        return self.__siple_Expression28

    @siple_Expression28.setter
    def siple_Expression28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression28", None)
        self.__siple_Expression28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_ProcedureReturn"):
                opp_val = getattr(old_value, "siple_ProcedureReturn", None)
                if opp_val == self:
                    setattr(old_value, "siple_ProcedureReturn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_ProcedureReturn"):
                opp_val = getattr(value, "siple_ProcedureReturn", None)
                setattr(value, "siple_ProcedureReturn", self)

    @property
    def siple_Expression56(self):
        return self.__siple_Expression56

    @siple_Expression56.setter
    def siple_Expression56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression56", None)
        self.__siple_Expression56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_BinaryExpression55"):
                opp_val = getattr(old_value, "siple_BinaryExpression55", None)
                if opp_val == self:
                    setattr(old_value, "siple_BinaryExpression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_BinaryExpression55"):
                opp_val = getattr(value, "siple_BinaryExpression55", None)
                setattr(value, "siple_BinaryExpression55", self)

    @property
    def siple_Expression(self):
        return self.__siple_Expression

    @siple_Expression.setter
    def siple_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression", None)
        self.__siple_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_If"):
                opp_val = getattr(old_value, "siple_If", None)
                if opp_val == self:
                    setattr(old_value, "siple_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_If"):
                opp_val = getattr(value, "siple_If", None)
                setattr(value, "siple_If", self)

    @property
    def siple_Expression26(self):
        return self.__siple_Expression26

    @siple_Expression26.setter
    def siple_Expression26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression26", None)
        self.__siple_Expression26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_VariableAssignment25"):
                opp_val = getattr(old_value, "siple_VariableAssignment25", None)
                if opp_val == self:
                    setattr(old_value, "siple_VariableAssignment25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_VariableAssignment25"):
                opp_val = getattr(value, "siple_VariableAssignment25", None)
                setattr(value, "siple_VariableAssignment25", self)

    @property
    def siple_Expression51(self):
        return self.__siple_Expression51

    @siple_Expression51.setter
    def siple_Expression51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression51", None)
        self.__siple_Expression51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_UnaryExpression"):
                opp_val = getattr(old_value, "siple_UnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "siple_UnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_UnaryExpression"):
                opp_val = getattr(value, "siple_UnaryExpression", None)
                setattr(value, "siple_UnaryExpression", self)

    @property
    def siple_Expression44(self):
        return self.__siple_Expression44

    @siple_Expression44.setter
    def siple_Expression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression44", None)
        self.__siple_Expression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_ProcedureCall43"):
                opp_val = getattr(old_value, "siple_ProcedureCall43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_ProcedureCall43"):
                opp_val = getattr(value, "siple_ProcedureCall43", None)
                if opp_val is None:
                    setattr(value, "siple_ProcedureCall43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def siple_Expression41(self):
        return self.__siple_Expression41

    @siple_Expression41.setter
    def siple_Expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression41", None)
        self.__siple_Expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_ProcedureCall"):
                opp_val = getattr(old_value, "siple_ProcedureCall", None)
                if opp_val == self:
                    setattr(old_value, "siple_ProcedureCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_ProcedureCall"):
                opp_val = getattr(value, "siple_ProcedureCall", None)
                setattr(value, "siple_ProcedureCall", self)

    @property
    def siple_Expression23(self):
        return self.__siple_Expression23

    @siple_Expression23.setter
    def siple_Expression23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression23", None)
        self.__siple_Expression23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_VariableAssignment"):
                opp_val = getattr(old_value, "siple_VariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "siple_VariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_VariableAssignment"):
                opp_val = getattr(value, "siple_VariableAssignment", None)
                setattr(value, "siple_VariableAssignment", self)

    @property
    def siple_Expression18(self):
        return self.__siple_Expression18

    @siple_Expression18.setter
    def siple_Expression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression18", None)
        self.__siple_Expression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_While"):
                opp_val = getattr(old_value, "siple_While", None)
                if opp_val == self:
                    setattr(old_value, "siple_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_While"):
                opp_val = getattr(value, "siple_While", None)
                setattr(value, "siple_While", self)

    @property
    def siple_Expression30(self):
        return self.__siple_Expression30

    @siple_Expression30.setter
    def siple_Expression30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression30", None)
        self.__siple_Expression30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Write"):
                opp_val = getattr(old_value, "siple_Write", None)
                if opp_val == self:
                    setattr(old_value, "siple_Write", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Write"):
                opp_val = getattr(value, "siple_Write", None)
                setattr(value, "siple_Write", self)

    @property
    def siple_Expression32(self):
        return self.__siple_Expression32

    @siple_Expression32.setter
    def siple_Expression32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression32", None)
        self.__siple_Expression32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_Read"):
                opp_val = getattr(old_value, "siple_Read", None)
                if opp_val == self:
                    setattr(old_value, "siple_Read", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_Read"):
                opp_val = getattr(value, "siple_Read", None)
                setattr(value, "siple_Read", self)

    @property
    def siple_Expression49(self):
        return self.__siple_Expression49

    @siple_Expression49.setter
    def siple_Expression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_Expression__siple_Expression49", None)
        self.__siple_Expression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_NestedExpression"):
                opp_val = getattr(old_value, "siple_NestedExpression", None)
                if opp_val == self:
                    setattr(old_value, "siple_NestedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_NestedExpression"):
                opp_val = getattr(value, "siple_NestedExpression", None)
                setattr(value, "siple_NestedExpression", self)

    def Value(self, vm: str) -> str:
        # TODO: Implement Value method
        pass

class siple_CompilationUnit:

    def __init__(self, siple_CompilationUnit: set["siple_Declaration"] = None, siple_CompilationUnit2: "siple_ProcedureDeclaration" = None):
        self.siple_CompilationUnit = siple_CompilationUnit if siple_CompilationUnit is not None else set()
        self.siple_CompilationUnit2 = siple_CompilationUnit2
        
    @property
    def siple_CompilationUnit(self):
        return self.__siple_CompilationUnit

    @siple_CompilationUnit.setter
    def siple_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_CompilationUnit__siple_CompilationUnit", None)
        self.__siple_CompilationUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "siple_Declaration"):
                    opp_val = getattr(item, "siple_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "siple_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "siple_Declaration"):
                    opp_val = getattr(item, "siple_Declaration", None)
                    
                    setattr(item, "siple_Declaration", self)
                    

    @property
    def siple_CompilationUnit2(self):
        return self.__siple_CompilationUnit2

    @siple_CompilationUnit2.setter
    def siple_CompilationUnit2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_siple_CompilationUnit__siple_CompilationUnit2", None)
        self.__siple_CompilationUnit2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "siple_ProcedureDeclaration"):
                opp_val = getattr(old_value, "siple_ProcedureDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "siple_ProcedureDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "siple_ProcedureDeclaration"):
                opp_val = getattr(value, "siple_ProcedureDeclaration", None)
                setattr(value, "siple_ProcedureDeclaration", self)

    def Interpret(self) -> str:
        # TODO: Implement Interpret method
        pass
