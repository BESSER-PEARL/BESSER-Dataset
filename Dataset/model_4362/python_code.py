from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessModifiers(Enum):
    default = "default"
    public = "public"
    protected = "protected"
    private = "private"
class Languages(Enum):
    Java = "Java"
    CS = "CS"
    Python = "Python"
    CPP = "CPP"
class Type(Enum):
    int = "int"
    long = "long"
    double = "double"
    float = "float"
    string = "string"
    boolean = "boolean"
    void = "void"


############################################
# Definition of Classes
############################################

class ArithmeticExpression:

    pass
class workflow_Multiplication(ArithmeticExpression):

    pass
class workflow_Subtraction(ArithmeticExpression):

    pass
class workflow_Addition(ArithmeticExpression):

    pass
class EqualityExpression:

    pass
class workflow_LessThan(EqualityExpression):

    pass
class workflow_LessThanOrEqual(EqualityExpression):

    pass
class workflow_GreaterThanOrEqual(EqualityExpression):

    pass
class workflow_GreaterThan(EqualityExpression):

    pass
class workflow_Equal(EqualityExpression):

    pass
class LogicExpression:

    pass
class workflow_Or(LogicExpression):

    pass
class workflow_And(LogicExpression):

    pass
class BinaryExpression:

    pass
class workflow_EqualityExpression(BinaryExpression):

    pass
class workflow_ArithmeticExpression(BinaryExpression):

    pass
class workflow_LogicExpression(BinaryExpression):

    pass
class workflow_NotEqual(EqualityExpression):

    pass
class workflow_Division(ArithmeticExpression):

    pass
class Expression:

    pass
class workflow_Constant(Expression):

    def __init__(self, asBoolean: str, asInteger: str, asReal: str, asString: str):
        self.asBoolean = asBoolean
        self.asInteger = asInteger
        self.asReal = asReal
        self.asString = asString
        
    @property
    def asString(self) -> str:
        return self.__asString

    @asString.setter
    def asString(self, asString: str):
        self.__asString = asString

    @property
    def asReal(self) -> str:
        return self.__asReal

    @asReal.setter
    def asReal(self, asReal: str):
        self.__asReal = asReal

    @property
    def asBoolean(self) -> str:
        return self.__asBoolean

    @asBoolean.setter
    def asBoolean(self, asBoolean: str):
        self.__asBoolean = asBoolean

    @property
    def asInteger(self) -> str:
        return self.__asInteger

    @asInteger.setter
    def asInteger(self, asInteger: str):
        self.__asInteger = asInteger

class Declaration:

    pass
class workflow_ParameterDeclaration(Declaration):

    def __init__(self, type: str, workflow_ParameterDeclaration: "workflow_ProcedureDeclaration" = None):
        self.type = type
        self.workflow_ParameterDeclaration = workflow_ParameterDeclaration
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def workflow_ParameterDeclaration(self):
        return self.__workflow_ParameterDeclaration

    @workflow_ParameterDeclaration.setter
    def workflow_ParameterDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ParameterDeclaration__workflow_ParameterDeclaration", None)
        self.__workflow_ParameterDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ProcedureDeclaration30"):
                opp_val = getattr(old_value, "workflow_ProcedureDeclaration30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ProcedureDeclaration30"):
                opp_val = getattr(value, "workflow_ProcedureDeclaration30", None)
                if opp_val is None:
                    setattr(value, "workflow_ProcedureDeclaration30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_VariableDeclaration(Declaration):

    def __init__(self, type: str, isConstant: str, workflow_VariableDeclaration: "workflow_ProcedureDeclaration" = None):
        self.type = type
        self.isConstant = isConstant
        self.workflow_VariableDeclaration = workflow_VariableDeclaration
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def isConstant(self) -> str:
        return self.__isConstant

    @isConstant.setter
    def isConstant(self, isConstant: str):
        self.__isConstant = isConstant

    @property
    def workflow_VariableDeclaration(self):
        return self.__workflow_VariableDeclaration

    @workflow_VariableDeclaration.setter
    def workflow_VariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_VariableDeclaration__workflow_VariableDeclaration", None)
        self.__workflow_VariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_ProcedureDeclaration25"):
                opp_val = getattr(old_value, "workflow_ProcedureDeclaration25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_ProcedureDeclaration25"):
                opp_val = getattr(value, "workflow_ProcedureDeclaration25", None)
                if opp_val is None:
                    setattr(value, "workflow_ProcedureDeclaration25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class workflow_BinaryExpression(Expression):

    pass
class UnaryExpression:

    pass
class workflow_UMinus(UnaryExpression):

    pass
class workflow_Not(UnaryExpression):

    pass
class workflow_UnaryExpression(Expression):

    pass
class workflow_ProcedureCall(Expression):

    def __init__(self, name: str, workflow_ProcedureCall: set["workflow_Expression"] = None):
        self.name = name
        self.workflow_ProcedureCall = workflow_ProcedureCall if workflow_ProcedureCall is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_ProcedureCall(self):
        return self.__workflow_ProcedureCall

    @workflow_ProcedureCall.setter
    def workflow_ProcedureCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcedureCall__workflow_ProcedureCall", None)
        self.__workflow_ProcedureCall = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_Expression32"):
                    opp_val = getattr(item, "workflow_Expression32", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_Expression32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_Expression32"):
                    opp_val = getattr(item, "workflow_Expression32", None)
                    
                    setattr(item, "workflow_Expression32", self)
                    

class workflow_Variable(Expression):

    def __init__(self, name: str, workflow_Variable: "workflow_VariableAssignment" = None, workflow_Variable21: "workflow_Write" = None, workflow_Variable23: "workflow_Read" = None):
        self.name = name
        self.workflow_Variable = workflow_Variable
        self.workflow_Variable21 = workflow_Variable21
        self.workflow_Variable23 = workflow_Variable23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def workflow_Variable21(self):
        return self.__workflow_Variable21

    @workflow_Variable21.setter
    def workflow_Variable21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Variable__workflow_Variable21", None)
        self.__workflow_Variable21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Write"):
                opp_val = getattr(old_value, "workflow_Write", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Write", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Write"):
                opp_val = getattr(value, "workflow_Write", None)
                setattr(value, "workflow_Write", self)

    @property
    def workflow_Variable(self):
        return self.__workflow_Variable

    @workflow_Variable.setter
    def workflow_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Variable__workflow_Variable", None)
        self.__workflow_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_VariableAssignment"):
                opp_val = getattr(old_value, "workflow_VariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "workflow_VariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_VariableAssignment"):
                opp_val = getattr(value, "workflow_VariableAssignment", None)
                setattr(value, "workflow_VariableAssignment", self)

    @property
    def workflow_Variable23(self):
        return self.__workflow_Variable23

    @workflow_Variable23.setter
    def workflow_Variable23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Variable__workflow_Variable23", None)
        self.__workflow_Variable23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Read"):
                opp_val = getattr(old_value, "workflow_Read", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Read", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Read"):
                opp_val = getattr(value, "workflow_Read", None)
                setattr(value, "workflow_Read", self)

class Statement:

    pass
class workflow_Declaration(Statement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class workflow_Write(Statement):

    pass
class workflow_ProcedureReturn(Statement):

    pass
class workflow_While(Statement):

    pass
class workflow_Expression(Statement):

    pass
class workflow_If(Statement):

    pass
class workflow_VariableAssignment(Statement):

    pass
class workflow_Read(Statement):

    def __init__(self, type: str, workflow_Read: "workflow_Variable" = None):
        self.type = type
        self.workflow_Read = workflow_Read
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def workflow_Read(self):
        return self.__workflow_Read

    @workflow_Read.setter
    def workflow_Read(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_Read__workflow_Read", None)
        self.__workflow_Read = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Variable23"):
                opp_val = getattr(old_value, "workflow_Variable23", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Variable23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Variable23"):
                opp_val = getattr(value, "workflow_Variable23", None)
                setattr(value, "workflow_Variable23", self)

class workflow_Block(Statement):

    pass
class workflow_Statement(ABC):

    pass
class workflow_ProcedureDeclaration(Declaration):

    def __init__(self, returnType: str, accessModifier: str, workflow_ProcedureDeclaration: "workflow_CompilationUnit" = None, workflow_ProcedureDeclaration25: set["workflow_VariableDeclaration"] = None, workflow_ProcedureDeclaration27: "workflow_Block" = None, workflow_ProcedureDeclaration30: set["workflow_ParameterDeclaration"] = None):
        self.returnType = returnType
        self.accessModifier = accessModifier
        self.workflow_ProcedureDeclaration = workflow_ProcedureDeclaration
        self.workflow_ProcedureDeclaration25 = workflow_ProcedureDeclaration25 if workflow_ProcedureDeclaration25 is not None else set()
        self.workflow_ProcedureDeclaration27 = workflow_ProcedureDeclaration27
        self.workflow_ProcedureDeclaration30 = workflow_ProcedureDeclaration30 if workflow_ProcedureDeclaration30 is not None else set()
        
    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def accessModifier(self) -> str:
        return self.__accessModifier

    @accessModifier.setter
    def accessModifier(self, accessModifier: str):
        self.__accessModifier = accessModifier

    @property
    def workflow_ProcedureDeclaration25(self):
        return self.__workflow_ProcedureDeclaration25

    @workflow_ProcedureDeclaration25.setter
    def workflow_ProcedureDeclaration25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcedureDeclaration__workflow_ProcedureDeclaration25", None)
        self.__workflow_ProcedureDeclaration25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_VariableDeclaration"):
                    opp_val = getattr(item, "workflow_VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_VariableDeclaration"):
                    opp_val = getattr(item, "workflow_VariableDeclaration", None)
                    
                    setattr(item, "workflow_VariableDeclaration", self)
                    

    @property
    def workflow_ProcedureDeclaration27(self):
        return self.__workflow_ProcedureDeclaration27

    @workflow_ProcedureDeclaration27.setter
    def workflow_ProcedureDeclaration27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcedureDeclaration__workflow_ProcedureDeclaration27", None)
        self.__workflow_ProcedureDeclaration27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_Block28"):
                opp_val = getattr(old_value, "workflow_Block28", None)
                if opp_val == self:
                    setattr(old_value, "workflow_Block28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_Block28"):
                opp_val = getattr(value, "workflow_Block28", None)
                setattr(value, "workflow_Block28", self)

    @property
    def workflow_ProcedureDeclaration(self):
        return self.__workflow_ProcedureDeclaration

    @workflow_ProcedureDeclaration.setter
    def workflow_ProcedureDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcedureDeclaration__workflow_ProcedureDeclaration", None)
        self.__workflow_ProcedureDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workflow_CompilationUnit"):
                opp_val = getattr(old_value, "workflow_CompilationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workflow_CompilationUnit"):
                opp_val = getattr(value, "workflow_CompilationUnit", None)
                if opp_val is None:
                    setattr(value, "workflow_CompilationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workflow_ProcedureDeclaration30(self):
        return self.__workflow_ProcedureDeclaration30

    @workflow_ProcedureDeclaration30.setter
    def workflow_ProcedureDeclaration30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_ProcedureDeclaration__workflow_ProcedureDeclaration30", None)
        self.__workflow_ProcedureDeclaration30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_ParameterDeclaration"):
                    opp_val = getattr(item, "workflow_ParameterDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_ParameterDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_ParameterDeclaration"):
                    opp_val = getattr(item, "workflow_ParameterDeclaration", None)
                    
                    setattr(item, "workflow_ParameterDeclaration", self)
                    

class workflow_CompilationUnit:

    def __init__(self, name: str, language: str, workflow_CompilationUnit: set["workflow_ProcedureDeclaration"] = None):
        self.name = name
        self.language = language
        self.workflow_CompilationUnit = workflow_CompilationUnit if workflow_CompilationUnit is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def workflow_CompilationUnit(self):
        return self.__workflow_CompilationUnit

    @workflow_CompilationUnit.setter
    def workflow_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_workflow_CompilationUnit__workflow_CompilationUnit", None)
        self.__workflow_CompilationUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "workflow_ProcedureDeclaration"):
                    opp_val = getattr(item, "workflow_ProcedureDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "workflow_ProcedureDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "workflow_ProcedureDeclaration"):
                    opp_val = getattr(item, "workflow_ProcedureDeclaration", None)
                    
                    setattr(item, "workflow_ProcedureDeclaration", self)
                    
