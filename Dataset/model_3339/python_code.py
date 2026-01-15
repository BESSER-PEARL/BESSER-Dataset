from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LiteralType(Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    NULL = "NULL"
class AssignmentOperatorType(Enum):
    ASSIGN = "ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"
class VisibilityType(Enum):
    PUBLIC = "PUBLIC"
    PROTECTED = "PROTECTED"
    PACKAGE = "PACKAGE"
    PRIVATE = "PRIVATE"
class InfixOperatorType(Enum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONDITIONAL_AND = "CONDITIONAL_AND"
    CONDITIONAL_OR = "CONDITIONAL_OR"


############################################
# Definition of Classes
############################################

class JavaSimplified_StringElement(ABC):

    def __init__(self, strValue: str):
        self.strValue = strValue
        
    @property
    def strValue(self) -> str:
        return self.__strValue

    @strValue.setter
    def strValue(self, strValue: str):
        self.__strValue = strValue

class JavaSimplified_TypedElement(ABC):

    pass
class JavaSimplified_NamedElement(ABC):

    pass
class JavaSimplified_MethodCall:

    pass
class JavaSimplified_JavaModel:

    pass
class Feature:

    pass
class JavaSimplified_Method(Feature):

    def __init__(self, exceptions: str, JavaSimplified_Method: "JavaSimplified_JavaClass" = None, JavaSimplified_Method46: set["JavaSimplified_Parameter"] = None, JavaSimplified_Method48: set["JavaSimplified_Statement"] = None, JavaSimplified_Method51: "JavaSimplified_Type" = None):
        self.exceptions = exceptions
        self.JavaSimplified_Method = JavaSimplified_Method
        self.JavaSimplified_Method46 = JavaSimplified_Method46 if JavaSimplified_Method46 is not None else set()
        self.JavaSimplified_Method48 = JavaSimplified_Method48 if JavaSimplified_Method48 is not None else set()
        self.JavaSimplified_Method51 = JavaSimplified_Method51
        
    @property
    def exceptions(self) -> str:
        return self.__exceptions

    @exceptions.setter
    def exceptions(self, exceptions: str):
        self.__exceptions = exceptions

    @property
    def JavaSimplified_Method51(self):
        return self.__JavaSimplified_Method51

    @JavaSimplified_Method51.setter
    def JavaSimplified_Method51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Method__JavaSimplified_Method51", None)
        self.__JavaSimplified_Method51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Type52"):
                opp_val = getattr(old_value, "JavaSimplified_Type52", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Type52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Type52"):
                opp_val = getattr(value, "JavaSimplified_Type52", None)
                setattr(value, "JavaSimplified_Type52", self)

    @property
    def JavaSimplified_Method46(self):
        return self.__JavaSimplified_Method46

    @JavaSimplified_Method46.setter
    def JavaSimplified_Method46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Method__JavaSimplified_Method46", None)
        self.__JavaSimplified_Method46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaSimplified_Parameter"):
                    opp_val = getattr(item, "JavaSimplified_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaSimplified_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaSimplified_Parameter"):
                    opp_val = getattr(item, "JavaSimplified_Parameter", None)
                    
                    setattr(item, "JavaSimplified_Parameter", self)
                    

    @property
    def JavaSimplified_Method(self):
        return self.__JavaSimplified_Method

    @JavaSimplified_Method.setter
    def JavaSimplified_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Method__JavaSimplified_Method", None)
        self.__JavaSimplified_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_JavaClass39"):
                opp_val = getattr(old_value, "JavaSimplified_JavaClass39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_JavaClass39"):
                opp_val = getattr(value, "JavaSimplified_JavaClass39", None)
                if opp_val is None:
                    setattr(value, "JavaSimplified_JavaClass39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JavaSimplified_Method48(self):
        return self.__JavaSimplified_Method48

    @JavaSimplified_Method48.setter
    def JavaSimplified_Method48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Method__JavaSimplified_Method48", None)
        self.__JavaSimplified_Method48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaSimplified_Statement49"):
                    opp_val = getattr(item, "JavaSimplified_Statement49", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaSimplified_Statement49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaSimplified_Statement49"):
                    opp_val = getattr(item, "JavaSimplified_Statement49", None)
                    
                    setattr(item, "JavaSimplified_Statement49", self)
                    

class TypedElement:

    pass
class JavaSimplified_Field(Feature, TypedElement):

    pass
class JavaSimplified_CommentedElement(ABC):

    pass
class StringElement:

    pass
class JavaSimplified_Statement(StringElement):

    pass
class NamedElement:

    pass
class JavaSimplified_Parameter(TypedElement, NamedElement):

    pass
class CommentedElement:

    pass
class JavaSimplified_JavaClass(NamedElement, CommentedElement):

    def __init__(self, imports: str, JavaSimplified_JavaClass: set["JavaSimplified_Field"] = None, JavaSimplified_JavaClass39: set["JavaSimplified_Method"] = None, JavaSimplified_JavaClass41: "JavaSimplified_JavaModel" = None):
        self.imports = imports
        self.JavaSimplified_JavaClass = JavaSimplified_JavaClass if JavaSimplified_JavaClass is not None else set()
        self.JavaSimplified_JavaClass39 = JavaSimplified_JavaClass39 if JavaSimplified_JavaClass39 is not None else set()
        self.JavaSimplified_JavaClass41 = JavaSimplified_JavaClass41
        
    @property
    def imports(self) -> str:
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports

    @property
    def JavaSimplified_JavaClass(self):
        return self.__JavaSimplified_JavaClass

    @JavaSimplified_JavaClass.setter
    def JavaSimplified_JavaClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_JavaClass__JavaSimplified_JavaClass", None)
        self.__JavaSimplified_JavaClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaSimplified_Field37"):
                    opp_val = getattr(item, "JavaSimplified_Field37", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaSimplified_Field37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaSimplified_Field37"):
                    opp_val = getattr(item, "JavaSimplified_Field37", None)
                    
                    setattr(item, "JavaSimplified_Field37", self)
                    

    @property
    def JavaSimplified_JavaClass39(self):
        return self.__JavaSimplified_JavaClass39

    @JavaSimplified_JavaClass39.setter
    def JavaSimplified_JavaClass39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_JavaClass__JavaSimplified_JavaClass39", None)
        self.__JavaSimplified_JavaClass39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaSimplified_Method"):
                    opp_val = getattr(item, "JavaSimplified_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaSimplified_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaSimplified_Method"):
                    opp_val = getattr(item, "JavaSimplified_Method", None)
                    
                    setattr(item, "JavaSimplified_Method", self)
                    

    @property
    def JavaSimplified_JavaClass41(self):
        return self.__JavaSimplified_JavaClass41

    @JavaSimplified_JavaClass41.setter
    def JavaSimplified_JavaClass41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_JavaClass__JavaSimplified_JavaClass41", None)
        self.__JavaSimplified_JavaClass41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_JavaModel"):
                opp_val = getattr(old_value, "JavaSimplified_JavaModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_JavaModel"):
                opp_val = getattr(value, "JavaSimplified_JavaModel", None)
                if opp_val is None:
                    setattr(value, "JavaSimplified_JavaModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JavaSimplified_Feature(NamedElement, CommentedElement, StringElement):

    def __init__(self, visibility: str):
        self.visibility = visibility
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class Statement:

    pass
class JavaSimplified_IfStatement(Statement):

    pass
class JavaSimplified_ReturnStatement(Statement):

    pass
class JavaSimplified_VariableDeclarationStatement(TypedElement, NamedElement, Statement):

    pass
class JavaSimplified_ExpressionStatement(Statement):

    pass
class JavaSimplified_CommentStatement(Statement):

    pass
class JavaSimplified_Comment(StringElement):

    def __init__(self, isJavadoc: bool, JavaSimplified_Comment: "JavaSimplified_CommentedElement" = None, JavaSimplified_Comment15: "JavaSimplified_CommentStatement" = None):
        self.isJavadoc = isJavadoc
        self.JavaSimplified_Comment = JavaSimplified_Comment
        self.JavaSimplified_Comment15 = JavaSimplified_Comment15
        
    @property
    def isJavadoc(self) -> bool:
        return self.__isJavadoc

    @isJavadoc.setter
    def isJavadoc(self, isJavadoc: bool):
        self.__isJavadoc = isJavadoc

    @property
    def JavaSimplified_Comment15(self):
        return self.__JavaSimplified_Comment15

    @JavaSimplified_Comment15.setter
    def JavaSimplified_Comment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Comment__JavaSimplified_Comment15", None)
        self.__JavaSimplified_Comment15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_CommentStatement"):
                opp_val = getattr(old_value, "JavaSimplified_CommentStatement", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_CommentStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_CommentStatement"):
                opp_val = getattr(value, "JavaSimplified_CommentStatement", None)
                setattr(value, "JavaSimplified_CommentStatement", self)

    @property
    def JavaSimplified_Comment(self):
        return self.__JavaSimplified_Comment

    @JavaSimplified_Comment.setter
    def JavaSimplified_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Comment__JavaSimplified_Comment", None)
        self.__JavaSimplified_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_CommentedElement"):
                opp_val = getattr(old_value, "JavaSimplified_CommentedElement", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_CommentedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_CommentedElement"):
                opp_val = getattr(value, "JavaSimplified_CommentedElement", None)
                setattr(value, "JavaSimplified_CommentedElement", self)

class JavaSimplified_Type:

    def __init__(self, type: str, JavaSimplified_Type: "JavaSimplified_CastExpression" = None, JavaSimplified_Type12: "JavaSimplified_ClassInstanceCreation" = None, JavaSimplified_Type52: "JavaSimplified_Method" = None, JavaSimplified_Type44: "JavaSimplified_JavaModel" = None, JavaSimplified_Type71: "JavaSimplified_TypedElement" = None):
        self.type = type
        self.JavaSimplified_Type = JavaSimplified_Type
        self.JavaSimplified_Type12 = JavaSimplified_Type12
        self.JavaSimplified_Type52 = JavaSimplified_Type52
        self.JavaSimplified_Type44 = JavaSimplified_Type44
        self.JavaSimplified_Type71 = JavaSimplified_Type71
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def JavaSimplified_Type12(self):
        return self.__JavaSimplified_Type12

    @JavaSimplified_Type12.setter
    def JavaSimplified_Type12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type12", None)
        self.__JavaSimplified_Type12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_ClassInstanceCreation11"):
                opp_val = getattr(old_value, "JavaSimplified_ClassInstanceCreation11", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_ClassInstanceCreation11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_ClassInstanceCreation11"):
                opp_val = getattr(value, "JavaSimplified_ClassInstanceCreation11", None)
                setattr(value, "JavaSimplified_ClassInstanceCreation11", self)

    @property
    def JavaSimplified_Type71(self):
        return self.__JavaSimplified_Type71

    @JavaSimplified_Type71.setter
    def JavaSimplified_Type71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type71", None)
        self.__JavaSimplified_Type71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_TypedElement"):
                opp_val = getattr(old_value, "JavaSimplified_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_TypedElement"):
                opp_val = getattr(value, "JavaSimplified_TypedElement", None)
                setattr(value, "JavaSimplified_TypedElement", self)

    @property
    def JavaSimplified_Type(self):
        return self.__JavaSimplified_Type

    @JavaSimplified_Type.setter
    def JavaSimplified_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type", None)
        self.__JavaSimplified_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_CastExpression7"):
                opp_val = getattr(old_value, "JavaSimplified_CastExpression7", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_CastExpression7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_CastExpression7"):
                opp_val = getattr(value, "JavaSimplified_CastExpression7", None)
                setattr(value, "JavaSimplified_CastExpression7", self)

    @property
    def JavaSimplified_Type52(self):
        return self.__JavaSimplified_Type52

    @JavaSimplified_Type52.setter
    def JavaSimplified_Type52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type52", None)
        self.__JavaSimplified_Type52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Method51"):
                opp_val = getattr(old_value, "JavaSimplified_Method51", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Method51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Method51"):
                opp_val = getattr(value, "JavaSimplified_Method51", None)
                setattr(value, "JavaSimplified_Method51", self)

    @property
    def JavaSimplified_Type44(self):
        return self.__JavaSimplified_Type44

    @JavaSimplified_Type44.setter
    def JavaSimplified_Type44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type44", None)
        self.__JavaSimplified_Type44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_JavaModel43"):
                opp_val = getattr(old_value, "JavaSimplified_JavaModel43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_JavaModel43"):
                opp_val = getattr(value, "JavaSimplified_JavaModel43", None)
                if opp_val is None:
                    setattr(value, "JavaSimplified_JavaModel43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class JavaSimplified_Expression(StringElement):

    pass
class Expression:

    pass
class JavaSimplified_Name(Expression):

    def __init__(self, identifier: str, JavaSimplified_Name: "JavaSimplified_FieldAccess" = None, JavaSimplified_Name62: "JavaSimplified_MethodInvocation" = None, JavaSimplified_Name67: "JavaSimplified_NamedElement" = None, JavaSimplified_Name60: "JavaSimplified_MethodCall" = None):
        self.identifier = identifier
        self.JavaSimplified_Name = JavaSimplified_Name
        self.JavaSimplified_Name62 = JavaSimplified_Name62
        self.JavaSimplified_Name67 = JavaSimplified_Name67
        self.JavaSimplified_Name60 = JavaSimplified_Name60
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def JavaSimplified_Name60(self):
        return self.__JavaSimplified_Name60

    @JavaSimplified_Name60.setter
    def JavaSimplified_Name60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Name__JavaSimplified_Name60", None)
        self.__JavaSimplified_Name60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_MethodCall59"):
                opp_val = getattr(old_value, "JavaSimplified_MethodCall59", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_MethodCall59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_MethodCall59"):
                opp_val = getattr(value, "JavaSimplified_MethodCall59", None)
                setattr(value, "JavaSimplified_MethodCall59", self)

    @property
    def JavaSimplified_Name67(self):
        return self.__JavaSimplified_Name67

    @JavaSimplified_Name67.setter
    def JavaSimplified_Name67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Name__JavaSimplified_Name67", None)
        self.__JavaSimplified_Name67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_NamedElement"):
                opp_val = getattr(old_value, "JavaSimplified_NamedElement", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_NamedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_NamedElement"):
                opp_val = getattr(value, "JavaSimplified_NamedElement", None)
                setattr(value, "JavaSimplified_NamedElement", self)

    @property
    def JavaSimplified_Name62(self):
        return self.__JavaSimplified_Name62

    @JavaSimplified_Name62.setter
    def JavaSimplified_Name62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Name__JavaSimplified_Name62", None)
        self.__JavaSimplified_Name62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_MethodInvocation"):
                opp_val = getattr(old_value, "JavaSimplified_MethodInvocation", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_MethodInvocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_MethodInvocation"):
                opp_val = getattr(value, "JavaSimplified_MethodInvocation", None)
                setattr(value, "JavaSimplified_MethodInvocation", self)

    @property
    def JavaSimplified_Name(self):
        return self.__JavaSimplified_Name

    @JavaSimplified_Name.setter
    def JavaSimplified_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Name__JavaSimplified_Name", None)
        self.__JavaSimplified_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_FieldAccess23"):
                opp_val = getattr(old_value, "JavaSimplified_FieldAccess23", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_FieldAccess23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_FieldAccess23"):
                opp_val = getattr(value, "JavaSimplified_FieldAccess23", None)
                setattr(value, "JavaSimplified_FieldAccess23", self)

class JavaSimplified_MethodInvocation(Expression):

    pass
class JavaSimplified_Literal(Expression):

    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value
        
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

class JavaSimplified_ThisExpression(Expression):

    pass
class JavaSimplified_FieldAccess(Expression):

    pass
class JavaSimplified_InfixExpression(Expression):

    def __init__(self, operator: str, JavaSimplified_InfixExpression34: "JavaSimplified_Expression" = None, JavaSimplified_InfixExpression: "JavaSimplified_Expression" = None):
        self.operator = operator
        self.JavaSimplified_InfixExpression34 = JavaSimplified_InfixExpression34
        self.JavaSimplified_InfixExpression = JavaSimplified_InfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def JavaSimplified_InfixExpression(self):
        return self.__JavaSimplified_InfixExpression

    @JavaSimplified_InfixExpression.setter
    def JavaSimplified_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_InfixExpression__JavaSimplified_InfixExpression", None)
        self.__JavaSimplified_InfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Expression32"):
                opp_val = getattr(old_value, "JavaSimplified_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression32"):
                opp_val = getattr(value, "JavaSimplified_Expression32", None)
                setattr(value, "JavaSimplified_Expression32", self)

    @property
    def JavaSimplified_InfixExpression34(self):
        return self.__JavaSimplified_InfixExpression34

    @JavaSimplified_InfixExpression34.setter
    def JavaSimplified_InfixExpression34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_InfixExpression__JavaSimplified_InfixExpression34", None)
        self.__JavaSimplified_InfixExpression34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Expression35"):
                opp_val = getattr(old_value, "JavaSimplified_Expression35", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression35"):
                opp_val = getattr(value, "JavaSimplified_Expression35", None)
                setattr(value, "JavaSimplified_Expression35", self)

class JavaSimplified_CastExpression(Expression):

    pass
class JavaSimplified_ClassInstanceCreation(Expression):

    pass
class JavaSimplified_Assignment(Expression):

    def __init__(self, operator: str, JavaSimplified_Assignment: "JavaSimplified_Expression" = None, JavaSimplified_Assignment2: "JavaSimplified_Expression" = None):
        self.operator = operator
        self.JavaSimplified_Assignment = JavaSimplified_Assignment
        self.JavaSimplified_Assignment2 = JavaSimplified_Assignment2
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def JavaSimplified_Assignment2(self):
        return self.__JavaSimplified_Assignment2

    @JavaSimplified_Assignment2.setter
    def JavaSimplified_Assignment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Assignment__JavaSimplified_Assignment2", None)
        self.__JavaSimplified_Assignment2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Expression3"):
                opp_val = getattr(old_value, "JavaSimplified_Expression3", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression3"):
                opp_val = getattr(value, "JavaSimplified_Expression3", None)
                setattr(value, "JavaSimplified_Expression3", self)

    @property
    def JavaSimplified_Assignment(self):
        return self.__JavaSimplified_Assignment

    @JavaSimplified_Assignment.setter
    def JavaSimplified_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Assignment__JavaSimplified_Assignment", None)
        self.__JavaSimplified_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Expression"):
                opp_val = getattr(old_value, "JavaSimplified_Expression", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression"):
                opp_val = getattr(value, "JavaSimplified_Expression", None)
                setattr(value, "JavaSimplified_Expression", self)
