from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class InfixOperatorType(Enum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONDITIONAL_AND = "CONDITIONAL_AND"
    CONDITIONAL_OR = "CONDITIONAL_OR"
class VisibilityType(Enum):
    PUBLIC = "PUBLIC"
    PROTECTED = "PROTECTED"
    PACKAGE = "PACKAGE"
    PRIVATE = "PRIVATE"
class LiteralType(Enum):
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    NULL = "NULL"
    STRING = "STRING"
class AssignmentOperatorType(Enum):
    ASSIGN = "ASSIGN"
    PLUS_ASSIGN = "PLUS_ASSIGN"


############################################
# Definition of Classes
############################################

class JavaSimplified_MethodCall:

    pass
class Expression:

    pass
class JavaSimplified_Literal(Expression):

    def __init__(self, value: str, type: str):
        self.value = value
        self.type = type
        
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

class JavaSimplified_InfixExpression(Expression):

    def __init__(self, operator: str, JavaSimplified_InfixExpression: "JavaSimplified_Expression" = None, JavaSimplified_InfixExpression52: "JavaSimplified_Expression" = None):
        self.operator = operator
        self.JavaSimplified_InfixExpression = JavaSimplified_InfixExpression
        self.JavaSimplified_InfixExpression52 = JavaSimplified_InfixExpression52
        
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
            if hasattr(old_value, "JavaSimplified_Expression50"):
                opp_val = getattr(old_value, "JavaSimplified_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression50"):
                opp_val = getattr(value, "JavaSimplified_Expression50", None)
                setattr(value, "JavaSimplified_Expression50", self)

    @property
    def JavaSimplified_InfixExpression52(self):
        return self.__JavaSimplified_InfixExpression52

    @JavaSimplified_InfixExpression52.setter
    def JavaSimplified_InfixExpression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_InfixExpression__JavaSimplified_InfixExpression52", None)
        self.__JavaSimplified_InfixExpression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Expression53"):
                opp_val = getattr(old_value, "JavaSimplified_Expression53", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression53"):
                opp_val = getattr(value, "JavaSimplified_Expression53", None)
                setattr(value, "JavaSimplified_Expression53", self)

class JavaSimplified_MethodInvocation(Expression):

    pass
class JavaSimplified_Assignment(Expression):

    def __init__(self, operator: str, JavaSimplified_Assignment: "JavaSimplified_Expression" = None, JavaSimplified_Assignment57: "JavaSimplified_Expression" = None):
        self.operator = operator
        self.JavaSimplified_Assignment = JavaSimplified_Assignment
        self.JavaSimplified_Assignment57 = JavaSimplified_Assignment57
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

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
            if hasattr(old_value, "JavaSimplified_Expression55"):
                opp_val = getattr(old_value, "JavaSimplified_Expression55", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression55"):
                opp_val = getattr(value, "JavaSimplified_Expression55", None)
                setattr(value, "JavaSimplified_Expression55", self)

    @property
    def JavaSimplified_Assignment57(self):
        return self.__JavaSimplified_Assignment57

    @JavaSimplified_Assignment57.setter
    def JavaSimplified_Assignment57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Assignment__JavaSimplified_Assignment57", None)
        self.__JavaSimplified_Assignment57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Expression58"):
                opp_val = getattr(old_value, "JavaSimplified_Expression58", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Expression58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Expression58"):
                opp_val = getattr(value, "JavaSimplified_Expression58", None)
                setattr(value, "JavaSimplified_Expression58", self)

class JavaSimplified_CastExpression(Expression):

    pass
class JavaSimplified_ClassInstanceCreation(Expression):

    pass
class Statement:

    pass
class JavaSimplified_ExpressionStatement(Statement):

    pass
class JavaSimplified_ReturnStatement(Statement):

    pass
class JavaSimplified_IfStatement(Statement):

    pass
class JavaSimplified_CommentStatement(Statement):

    pass
class TypedElement:

    pass
class NamedElement:

    pass
class JavaSimplified_VariableDeclarationStatement(Statement, NamedElement, TypedElement):

    pass
class JavaSimplified_Parameter(NamedElement, TypedElement):

    pass
class CommentedElement:

    pass
class JavaSimplified_JavaClass(CommentedElement, NamedElement):

    def __init__(self, imports: str, JavaSimplified_JavaClass: set["JavaSimplified_Field"] = None, JavaSimplified_JavaClass5: set["JavaSimplified_Method"] = None):
        self.imports = imports
        self.JavaSimplified_JavaClass = JavaSimplified_JavaClass if JavaSimplified_JavaClass is not None else set()
        self.JavaSimplified_JavaClass5 = JavaSimplified_JavaClass5 if JavaSimplified_JavaClass5 is not None else set()
        
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
                if hasattr(item, "JavaSimplified_Field"):
                    opp_val = getattr(item, "JavaSimplified_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaSimplified_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaSimplified_Field"):
                    opp_val = getattr(item, "JavaSimplified_Field", None)
                    
                    setattr(item, "JavaSimplified_Field", self)
                    

    @property
    def JavaSimplified_JavaClass5(self):
        return self.__JavaSimplified_JavaClass5

    @JavaSimplified_JavaClass5.setter
    def JavaSimplified_JavaClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_JavaClass__JavaSimplified_JavaClass5", None)
        self.__JavaSimplified_JavaClass5 = value if value is not None else set()
        
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
                    

class JavaSimplified_CommentedElement(ABC):

    pass
class StringElement:

    pass
class JavaSimplified_Statement(StringElement):

    pass
class JavaSimplified_Field(StringElement, CommentedElement, NamedElement, TypedElement):

    def __init__(self, visibility: str, JavaSimplified_Field: "JavaSimplified_JavaClass" = None, JavaSimplified_Field7: "JavaSimplified_Expression" = None):
        self.visibility = visibility
        self.JavaSimplified_Field = JavaSimplified_Field
        self.JavaSimplified_Field7 = JavaSimplified_Field7
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def JavaSimplified_Field(self):
        return self.__JavaSimplified_Field

    @JavaSimplified_Field.setter
    def JavaSimplified_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Field__JavaSimplified_Field", None)
        self.__JavaSimplified_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_JavaClass"):
                opp_val = getattr(old_value, "JavaSimplified_JavaClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_JavaClass"):
                opp_val = getattr(value, "JavaSimplified_JavaClass", None)
                if opp_val is None:
                    setattr(value, "JavaSimplified_JavaClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JavaSimplified_Field7(self):
        return self.__JavaSimplified_Field7

    @JavaSimplified_Field7.setter
    def JavaSimplified_Field7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Field__JavaSimplified_Field7", None)
        self.__JavaSimplified_Field7 = value
        
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

class JavaSimplified_Expression(StringElement):

    pass
class JavaSimplified_Method(StringElement, CommentedElement, NamedElement):

    def __init__(self, exceptions: str, JavaSimplified_Method: "JavaSimplified_JavaClass" = None, JavaSimplified_Method9: set["JavaSimplified_Parameter"] = None, JavaSimplified_Method11: set["JavaSimplified_Statement"] = None, JavaSimplified_Method13: "JavaSimplified_Type" = None):
        self.exceptions = exceptions
        self.JavaSimplified_Method = JavaSimplified_Method
        self.JavaSimplified_Method9 = JavaSimplified_Method9 if JavaSimplified_Method9 is not None else set()
        self.JavaSimplified_Method11 = JavaSimplified_Method11 if JavaSimplified_Method11 is not None else set()
        self.JavaSimplified_Method13 = JavaSimplified_Method13
        
    @property
    def exceptions(self) -> str:
        return self.__exceptions

    @exceptions.setter
    def exceptions(self, exceptions: str):
        self.__exceptions = exceptions

    @property
    def JavaSimplified_Method13(self):
        return self.__JavaSimplified_Method13

    @JavaSimplified_Method13.setter
    def JavaSimplified_Method13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Method__JavaSimplified_Method13", None)
        self.__JavaSimplified_Method13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Type14"):
                opp_val = getattr(old_value, "JavaSimplified_Type14", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Type14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Type14"):
                opp_val = getattr(value, "JavaSimplified_Type14", None)
                setattr(value, "JavaSimplified_Type14", self)

    @property
    def JavaSimplified_Method11(self):
        return self.__JavaSimplified_Method11

    @JavaSimplified_Method11.setter
    def JavaSimplified_Method11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Method__JavaSimplified_Method11", None)
        self.__JavaSimplified_Method11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaSimplified_Statement"):
                    opp_val = getattr(item, "JavaSimplified_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaSimplified_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaSimplified_Statement"):
                    opp_val = getattr(item, "JavaSimplified_Statement", None)
                    
                    setattr(item, "JavaSimplified_Statement", self)
                    

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
            if hasattr(old_value, "JavaSimplified_JavaClass5"):
                opp_val = getattr(old_value, "JavaSimplified_JavaClass5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_JavaClass5"):
                opp_val = getattr(value, "JavaSimplified_JavaClass5", None)
                if opp_val is None:
                    setattr(value, "JavaSimplified_JavaClass5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def JavaSimplified_Method9(self):
        return self.__JavaSimplified_Method9

    @JavaSimplified_Method9.setter
    def JavaSimplified_Method9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Method__JavaSimplified_Method9", None)
        self.__JavaSimplified_Method9 = value if value is not None else set()
        
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
                    

class JavaSimplified_Comment(StringElement):

    def __init__(self, isJavadoc: bool, JavaSimplified_Comment: "JavaSimplified_CommentedElement" = None, JavaSimplified_Comment16: "JavaSimplified_CommentStatement" = None):
        self.isJavadoc = isJavadoc
        self.JavaSimplified_Comment = JavaSimplified_Comment
        self.JavaSimplified_Comment16 = JavaSimplified_Comment16
        
    @property
    def isJavadoc(self) -> bool:
        return self.__isJavadoc

    @isJavadoc.setter
    def isJavadoc(self, isJavadoc: bool):
        self.__isJavadoc = isJavadoc

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

    @property
    def JavaSimplified_Comment16(self):
        return self.__JavaSimplified_Comment16

    @JavaSimplified_Comment16.setter
    def JavaSimplified_Comment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Comment__JavaSimplified_Comment16", None)
        self.__JavaSimplified_Comment16 = value
        
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

class JavaSimplified_Type:

    def __init__(self, type: str, JavaSimplified_Type: "JavaSimplified_TypedElement" = None, JavaSimplified_Type14: "JavaSimplified_Method" = None, JavaSimplified_Type35: "JavaSimplified_CastExpression" = None, JavaSimplified_Type63: "JavaSimplified_ClassInstanceCreation" = None):
        self.type = type
        self.JavaSimplified_Type = JavaSimplified_Type
        self.JavaSimplified_Type14 = JavaSimplified_Type14
        self.JavaSimplified_Type35 = JavaSimplified_Type35
        self.JavaSimplified_Type63 = JavaSimplified_Type63
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def JavaSimplified_Type14(self):
        return self.__JavaSimplified_Type14

    @JavaSimplified_Type14.setter
    def JavaSimplified_Type14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type14", None)
        self.__JavaSimplified_Type14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_Method13"):
                opp_val = getattr(old_value, "JavaSimplified_Method13", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_Method13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_Method13"):
                opp_val = getattr(value, "JavaSimplified_Method13", None)
                setattr(value, "JavaSimplified_Method13", self)

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
    def JavaSimplified_Type35(self):
        return self.__JavaSimplified_Type35

    @JavaSimplified_Type35.setter
    def JavaSimplified_Type35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type35", None)
        self.__JavaSimplified_Type35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_CastExpression34"):
                opp_val = getattr(old_value, "JavaSimplified_CastExpression34", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_CastExpression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_CastExpression34"):
                opp_val = getattr(value, "JavaSimplified_CastExpression34", None)
                setattr(value, "JavaSimplified_CastExpression34", self)

    @property
    def JavaSimplified_Type63(self):
        return self.__JavaSimplified_Type63

    @JavaSimplified_Type63.setter
    def JavaSimplified_Type63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Type__JavaSimplified_Type63", None)
        self.__JavaSimplified_Type63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_ClassInstanceCreation62"):
                opp_val = getattr(old_value, "JavaSimplified_ClassInstanceCreation62", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_ClassInstanceCreation62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_ClassInstanceCreation62"):
                opp_val = getattr(value, "JavaSimplified_ClassInstanceCreation62", None)
                setattr(value, "JavaSimplified_ClassInstanceCreation62", self)

class JavaSimplified_TypedElement(ABC):

    pass
class JavaSimplified_Name(Expression):

    def __init__(self, identifier: str, JavaSimplified_Name: "JavaSimplified_NamedElement" = None, JavaSimplified_Name32: "JavaSimplified_CastExpression" = None, JavaSimplified_Name37: "JavaSimplified_MethodInvocation" = None, JavaSimplified_Name48: "JavaSimplified_MethodCall" = None):
        self.identifier = identifier
        self.JavaSimplified_Name = JavaSimplified_Name
        self.JavaSimplified_Name32 = JavaSimplified_Name32
        self.JavaSimplified_Name37 = JavaSimplified_Name37
        self.JavaSimplified_Name48 = JavaSimplified_Name48
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def JavaSimplified_Name32(self):
        return self.__JavaSimplified_Name32

    @JavaSimplified_Name32.setter
    def JavaSimplified_Name32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Name__JavaSimplified_Name32", None)
        self.__JavaSimplified_Name32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_CastExpression"):
                opp_val = getattr(old_value, "JavaSimplified_CastExpression", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_CastExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_CastExpression"):
                opp_val = getattr(value, "JavaSimplified_CastExpression", None)
                setattr(value, "JavaSimplified_CastExpression", self)

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
    def JavaSimplified_Name48(self):
        return self.__JavaSimplified_Name48

    @JavaSimplified_Name48.setter
    def JavaSimplified_Name48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Name__JavaSimplified_Name48", None)
        self.__JavaSimplified_Name48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "JavaSimplified_MethodCall47"):
                opp_val = getattr(old_value, "JavaSimplified_MethodCall47", None)
                if opp_val == self:
                    setattr(old_value, "JavaSimplified_MethodCall47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "JavaSimplified_MethodCall47"):
                opp_val = getattr(value, "JavaSimplified_MethodCall47", None)
                setattr(value, "JavaSimplified_MethodCall47", self)

    @property
    def JavaSimplified_Name37(self):
        return self.__JavaSimplified_Name37

    @JavaSimplified_Name37.setter
    def JavaSimplified_Name37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JavaSimplified_Name__JavaSimplified_Name37", None)
        self.__JavaSimplified_Name37 = value
        
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

class JavaSimplified_StringElement(ABC):

    def __init__(self, strValue: str):
        self.strValue = strValue
        
    @property
    def strValue(self) -> str:
        return self.__strValue

    @strValue.setter
    def strValue(self, strValue: str):
        self.__strValue = strValue

class JavaSimplified_NamedElement(ABC):

    pass