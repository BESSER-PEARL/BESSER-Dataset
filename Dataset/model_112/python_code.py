from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    none = "none"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class javasimplified_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class javasimplified_ArrayCreation(Expression):

    pass
class javasimplified_CastExpression(Expression):

    pass
class javasimplified_NullLiteral(Expression):

    pass
class javasimplified_InstanceOfExpression(Expression):

    pass
class javasimplified_ArrayAccess(Expression):

    pass
class javasimplified_ThisExpression(Expression):

    pass
class javasimplified_ClassInstanceCreation(Expression):

    pass
class javasimplified_VariableAccess(Expression):

    pass
class javasimplified_NumberLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class javasimplified_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class javasimplified_Assignment(Expression):

    pass
class javasimplified_Expression(ABC):

    pass
class Type:

    pass
class javasimplified_PrimitiveType(Type):

    pass
class javasimplified_Comment:

    pass
class javasimplified_Interface(Type):

    pass
class javasimplified_ImportDeclaration:

    pass
class javasimplified_Statement(ABC):

    pass
class javasimplified_Modifier:

    def __init__(self, visibility: str, isStatic: bool, isVolatile: bool, isSynchronized: bool, isFinal: bool, javasimplified_Modifier14: "javasimplified_Variable" = None, javasimplified_Modifier: "javasimplified_Method" = None, javasimplified_Modifier33: "javasimplified_Class" = None):
        self.visibility = visibility
        self.isStatic = isStatic
        self.isVolatile = isVolatile
        self.isSynchronized = isSynchronized
        self.isFinal = isFinal
        self.javasimplified_Modifier14 = javasimplified_Modifier14
        self.javasimplified_Modifier = javasimplified_Modifier
        self.javasimplified_Modifier33 = javasimplified_Modifier33
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def isSynchronized(self) -> bool:
        return self.__isSynchronized

    @isSynchronized.setter
    def isSynchronized(self, isSynchronized: bool):
        self.__isSynchronized = isSynchronized

    @property
    def isFinal(self) -> bool:
        return self.__isFinal

    @isFinal.setter
    def isFinal(self, isFinal: bool):
        self.__isFinal = isFinal

    @property
    def isVolatile(self) -> bool:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: bool):
        self.__isVolatile = isVolatile

    @property
    def javasimplified_Modifier(self):
        return self.__javasimplified_Modifier

    @javasimplified_Modifier.setter
    def javasimplified_Modifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Modifier__javasimplified_Modifier", None)
        self.__javasimplified_Modifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Method6"):
                opp_val = getattr(old_value, "javasimplified_Method6", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Method6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Method6"):
                opp_val = getattr(value, "javasimplified_Method6", None)
                setattr(value, "javasimplified_Method6", self)

    @property
    def javasimplified_Modifier14(self):
        return self.__javasimplified_Modifier14

    @javasimplified_Modifier14.setter
    def javasimplified_Modifier14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Modifier__javasimplified_Modifier14", None)
        self.__javasimplified_Modifier14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Variable13"):
                opp_val = getattr(old_value, "javasimplified_Variable13", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Variable13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Variable13"):
                opp_val = getattr(value, "javasimplified_Variable13", None)
                setattr(value, "javasimplified_Variable13", self)

    @property
    def javasimplified_Modifier33(self):
        return self.__javasimplified_Modifier33

    @javasimplified_Modifier33.setter
    def javasimplified_Modifier33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Modifier__javasimplified_Modifier33", None)
        self.__javasimplified_Modifier33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Class32"):
                opp_val = getattr(old_value, "javasimplified_Class32", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Class32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Class32"):
                opp_val = getattr(value, "javasimplified_Class32", None)
                setattr(value, "javasimplified_Class32", self)

class Statement:

    pass
class javasimplified_ExpressionStatement(Statement):

    pass
class javasimplified_WhileStatement(Statement):

    pass
class javasimplified_Block(Statement):

    pass
class javasimplified_ForStatement(Statement):

    pass
class javasimplified_IfStatement(Statement):

    pass
class javasimplified_TryStatement(Statement):

    pass
class javasimplified_ThrowStatement(Statement):

    pass
class javasimplified_CatchStatment(Statement):

    pass
class javasimplified_ReturnStatement(Statement):

    pass
class javasimplified_Variable(Statement):

    def __init__(self, name: str, javasimplified_Variable: "javasimplified_Type" = None, variables: "javasimplified_Class" = None, javasimplified_Variable13: "javasimplified_Modifier" = None, Variable: "javasimplified_Class" = None, javasimplified_Variable99: "javasimplified_VariableAccess" = None):
        self.name = name
        self.javasimplified_Variable = javasimplified_Variable
        self.variables = variables
        self.javasimplified_Variable13 = javasimplified_Variable13
        self.Variable = Variable
        self.javasimplified_Variable99 = javasimplified_Variable99
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javasimplified_Variable(self):
        return self.__javasimplified_Variable

    @javasimplified_Variable.setter
    def javasimplified_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Variable__javasimplified_Variable", None)
        self.__javasimplified_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Type10"):
                opp_val = getattr(old_value, "javasimplified_Type10", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Type10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Type10"):
                opp_val = getattr(value, "javasimplified_Type10", None)
                setattr(value, "javasimplified_Type10", self)

    @property
    def javasimplified_Variable13(self):
        return self.__javasimplified_Variable13

    @javasimplified_Variable13.setter
    def javasimplified_Variable13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Variable__javasimplified_Variable13", None)
        self.__javasimplified_Variable13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Modifier14"):
                opp_val = getattr(old_value, "javasimplified_Modifier14", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Modifier14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Modifier14"):
                opp_val = getattr(value, "javasimplified_Modifier14", None)
                setattr(value, "javasimplified_Modifier14", self)

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Variable__variables", None)
        self.__variables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class"):
                opp_val = getattr(old_value, "Class", None)
                if opp_val == self:
                    setattr(old_value, "Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class"):
                opp_val = getattr(value, "Class", None)
                setattr(value, "Class", self)

    @property
    def javasimplified_Variable99(self):
        return self.__javasimplified_Variable99

    @javasimplified_Variable99.setter
    def javasimplified_Variable99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Variable__javasimplified_Variable99", None)
        self.__javasimplified_Variable99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_VariableAccess"):
                opp_val = getattr(old_value, "javasimplified_VariableAccess", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_VariableAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_VariableAccess"):
                opp_val = getattr(value, "javasimplified_VariableAccess", None)
                setattr(value, "javasimplified_VariableAccess", self)

    @property
    def Variable(self):
        return self.__Variable

    @Variable.setter
    def Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Variable__Variable", None)
        self.__Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javasimplified_Class(Type):

    def __init__(self, isAbstract: bool, javasimplified_Class: "javasimplified_Method" = None, Class: "javasimplified_Variable" = None, javasimplified_Class25: "javasimplified_Class" = None, javasimplified_Class23: "javasimplified_Class" = None, javasimplified_Class27: set["javasimplified_Method"] = None, javasimplified_Class30: set["javasimplified_ImportDeclaration"] = None, javasimplified_Class32: "javasimplified_Modifier" = None, Class19: "javasimplified_Comment" = None, class: set["javasimplified_Variable"] = None, class22: set["javasimplified_Comment"] = None, javasimplified_Class35: set["javasimplified_Interface"] = None, javasimplified_Class37: "javasimplified_Package" = None):
        self.isAbstract = isAbstract
        self.javasimplified_Class = javasimplified_Class
        self.Class = Class
        self.javasimplified_Class25 = javasimplified_Class25
        self.javasimplified_Class23 = javasimplified_Class23
        self.javasimplified_Class27 = javasimplified_Class27 if javasimplified_Class27 is not None else set()
        self.javasimplified_Class30 = javasimplified_Class30 if javasimplified_Class30 is not None else set()
        self.javasimplified_Class32 = javasimplified_Class32
        self.Class19 = Class19
        self.class = class if class is not None else set()
        self.class22 = class22 if class22 is not None else set()
        self.javasimplified_Class35 = javasimplified_Class35 if javasimplified_Class35 is not None else set()
        self.javasimplified_Class37 = javasimplified_Class37
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def javasimplified_Class27(self):
        return self.__javasimplified_Class27

    @javasimplified_Class27.setter
    def javasimplified_Class27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class27", None)
        self.__javasimplified_Class27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javasimplified_Method28"):
                    opp_val = getattr(item, "javasimplified_Method28", None)
                    
                    if opp_val == self:
                        setattr(item, "javasimplified_Method28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javasimplified_Method28"):
                    opp_val = getattr(item, "javasimplified_Method28", None)
                    
                    setattr(item, "javasimplified_Method28", self)
                    

    @property
    def Class(self):
        return self.__Class

    @Class.setter
    def Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__Class", None)
        self.__Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variables"):
                opp_val = getattr(old_value, "variables", None)
                if opp_val == self:
                    setattr(old_value, "variables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variables"):
                opp_val = getattr(value, "variables", None)
                setattr(value, "variables", self)

    @property
    def javasimplified_Class30(self):
        return self.__javasimplified_Class30

    @javasimplified_Class30.setter
    def javasimplified_Class30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class30", None)
        self.__javasimplified_Class30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javasimplified_ImportDeclaration"):
                    opp_val = getattr(item, "javasimplified_ImportDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "javasimplified_ImportDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javasimplified_ImportDeclaration"):
                    opp_val = getattr(item, "javasimplified_ImportDeclaration", None)
                    
                    setattr(item, "javasimplified_ImportDeclaration", self)
                    

    @property
    def javasimplified_Class25(self):
        return self.__javasimplified_Class25

    @javasimplified_Class25.setter
    def javasimplified_Class25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class25", None)
        self.__javasimplified_Class25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Class23"):
                opp_val = getattr(old_value, "javasimplified_Class23", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Class23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Class23"):
                opp_val = getattr(value, "javasimplified_Class23", None)
                setattr(value, "javasimplified_Class23", self)

    @property
    def javasimplified_Class23(self):
        return self.__javasimplified_Class23

    @javasimplified_Class23.setter
    def javasimplified_Class23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class23", None)
        self.__javasimplified_Class23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Class25"):
                opp_val = getattr(old_value, "javasimplified_Class25", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Class25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Class25"):
                opp_val = getattr(value, "javasimplified_Class25", None)
                setattr(value, "javasimplified_Class25", self)

    @property
    def javasimplified_Class35(self):
        return self.__javasimplified_Class35

    @javasimplified_Class35.setter
    def javasimplified_Class35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class35", None)
        self.__javasimplified_Class35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javasimplified_Interface"):
                    opp_val = getattr(item, "javasimplified_Interface", None)
                    
                    if opp_val == self:
                        setattr(item, "javasimplified_Interface", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javasimplified_Interface"):
                    opp_val = getattr(item, "javasimplified_Interface", None)
                    
                    setattr(item, "javasimplified_Interface", self)
                    

    @property
    def class22(self):
        return self.__class22

    @class22.setter
    def class22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__class22", None)
        self.__class22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

    @property
    def javasimplified_Class(self):
        return self.__javasimplified_Class

    @javasimplified_Class.setter
    def javasimplified_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class", None)
        self.__javasimplified_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Method"):
                opp_val = getattr(old_value, "javasimplified_Method", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Method", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Method"):
                opp_val = getattr(value, "javasimplified_Method", None)
                setattr(value, "javasimplified_Method", self)

    @property
    def class(self):
        return self.__class

    @class.setter
    def class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__class", None)
        self.__class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def javasimplified_Class37(self):
        return self.__javasimplified_Class37

    @javasimplified_Class37.setter
    def javasimplified_Class37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class37", None)
        self.__javasimplified_Class37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Package"):
                opp_val = getattr(old_value, "javasimplified_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Package"):
                opp_val = getattr(value, "javasimplified_Package", None)
                if opp_val is None:
                    setattr(value, "javasimplified_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javasimplified_Class32(self):
        return self.__javasimplified_Class32

    @javasimplified_Class32.setter
    def javasimplified_Class32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__javasimplified_Class32", None)
        self.__javasimplified_Class32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Modifier33"):
                opp_val = getattr(old_value, "javasimplified_Modifier33", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Modifier33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Modifier33"):
                opp_val = getattr(value, "javasimplified_Modifier33", None)
                setattr(value, "javasimplified_Modifier33", self)

    @property
    def Class19(self):
        return self.__Class19

    @Class19.setter
    def Class19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Class__Class19", None)
        self.__Class19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "comments"):
                opp_val = getattr(old_value, "comments", None)
                if opp_val == self:
                    setattr(old_value, "comments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "comments"):
                opp_val = getattr(value, "comments", None)
                setattr(value, "comments", self)

class NamedElement:

    pass
class javasimplified_Model(NamedElement):

    pass
class javasimplified_Parameter(NamedElement):

    pass
class javasimplified_Type(NamedElement):

    pass
class javasimplified_Package(NamedElement):

    pass
class javasimplified_Method(NamedElement):

    def __init__(self, visibility: str, javasimplified_Method: "javasimplified_Class" = None, javasimplified_Method2: set["javasimplified_Parameter"] = None, javasimplified_Method4: "javasimplified_Type" = None, javasimplified_Method6: "javasimplified_Modifier" = None, javasimplified_Method8: set["javasimplified_Statement"] = None, javasimplified_Method28: "javasimplified_Class" = None):
        self.visibility = visibility
        self.javasimplified_Method = javasimplified_Method
        self.javasimplified_Method2 = javasimplified_Method2 if javasimplified_Method2 is not None else set()
        self.javasimplified_Method4 = javasimplified_Method4
        self.javasimplified_Method6 = javasimplified_Method6
        self.javasimplified_Method8 = javasimplified_Method8 if javasimplified_Method8 is not None else set()
        self.javasimplified_Method28 = javasimplified_Method28
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def javasimplified_Method8(self):
        return self.__javasimplified_Method8

    @javasimplified_Method8.setter
    def javasimplified_Method8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Method__javasimplified_Method8", None)
        self.__javasimplified_Method8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javasimplified_Statement"):
                    opp_val = getattr(item, "javasimplified_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "javasimplified_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javasimplified_Statement"):
                    opp_val = getattr(item, "javasimplified_Statement", None)
                    
                    setattr(item, "javasimplified_Statement", self)
                    

    @property
    def javasimplified_Method2(self):
        return self.__javasimplified_Method2

    @javasimplified_Method2.setter
    def javasimplified_Method2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Method__javasimplified_Method2", None)
        self.__javasimplified_Method2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javasimplified_Parameter"):
                    opp_val = getattr(item, "javasimplified_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "javasimplified_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javasimplified_Parameter"):
                    opp_val = getattr(item, "javasimplified_Parameter", None)
                    
                    setattr(item, "javasimplified_Parameter", self)
                    

    @property
    def javasimplified_Method6(self):
        return self.__javasimplified_Method6

    @javasimplified_Method6.setter
    def javasimplified_Method6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Method__javasimplified_Method6", None)
        self.__javasimplified_Method6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Modifier"):
                opp_val = getattr(old_value, "javasimplified_Modifier", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Modifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Modifier"):
                opp_val = getattr(value, "javasimplified_Modifier", None)
                setattr(value, "javasimplified_Modifier", self)

    @property
    def javasimplified_Method28(self):
        return self.__javasimplified_Method28

    @javasimplified_Method28.setter
    def javasimplified_Method28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Method__javasimplified_Method28", None)
        self.__javasimplified_Method28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Class27"):
                opp_val = getattr(old_value, "javasimplified_Class27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Class27"):
                opp_val = getattr(value, "javasimplified_Class27", None)
                if opp_val is None:
                    setattr(value, "javasimplified_Class27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javasimplified_Method(self):
        return self.__javasimplified_Method

    @javasimplified_Method.setter
    def javasimplified_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Method__javasimplified_Method", None)
        self.__javasimplified_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Class"):
                opp_val = getattr(old_value, "javasimplified_Class", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Class"):
                opp_val = getattr(value, "javasimplified_Class", None)
                setattr(value, "javasimplified_Class", self)

    @property
    def javasimplified_Method4(self):
        return self.__javasimplified_Method4

    @javasimplified_Method4.setter
    def javasimplified_Method4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_Method__javasimplified_Method4", None)
        self.__javasimplified_Method4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_Type"):
                opp_val = getattr(old_value, "javasimplified_Type", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_Type"):
                opp_val = getattr(value, "javasimplified_Type", None)
                setattr(value, "javasimplified_Type", self)

class javasimplified_NamedElement(ABC):

    def __init__(self, name: str, javasimplified_NamedElement: "javasimplified_ImportDeclaration" = None):
        self.name = name
        self.javasimplified_NamedElement = javasimplified_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javasimplified_NamedElement(self):
        return self.__javasimplified_NamedElement

    @javasimplified_NamedElement.setter
    def javasimplified_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javasimplified_NamedElement__javasimplified_NamedElement", None)
        self.__javasimplified_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javasimplified_ImportDeclaration44"):
                opp_val = getattr(old_value, "javasimplified_ImportDeclaration44", None)
                if opp_val == self:
                    setattr(old_value, "javasimplified_ImportDeclaration44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javasimplified_ImportDeclaration44"):
                opp_val = getattr(value, "javasimplified_ImportDeclaration44", None)
                setattr(value, "javasimplified_ImportDeclaration44", self)
