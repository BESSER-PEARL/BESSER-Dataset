from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOperator(Enum):
    rsh = "rsh"
    ursh = "ursh"
    less = "less"
    greater = "greater"
    leq = "leq"
    geq = "geq"
    mul = "mul"
    div = "div"
    mod = "mod"
    add = "add"
    sub = "sub"
    lsh = "lsh"
    xorAssign = "xorAssign"
    orAssign = "orAssign"
    comma = "comma"
    instanceof = "instanceof"
    in = "in"
    eq = "eq"
    neq = "neq"
    same = "same"
    nsame = "nsame"
    bwAnd = "bwAnd"
    bwXor = "bwXor"
    bwOr = "bwOr"
    logAnd = "logAnd"
    logOr = "logOr"
    assign = "assign"
    mulAssign = "mulAssign"
    divAssign = "divAssign"
    modAssign = "modAssign"
    addAssign = "addAssign"
    subAssign = "subAssign"
    lshAssign = "lshAssign"
    rshAssign = "rshAssign"
    urshAssign = "urshAssign"
    andAssign = "andAssign"
class UnaryOperator(Enum):
    not = "not"
    postfixInc = "postfixInc"
    postfixDec = "postfixDec"
    delete = "delete"
    void = "void"
    typeof = "typeof"
    prefixInc = "prefixInc"
    prefixDec = "prefixDec"
    unaryPlus = "unaryPlus"
    numNeg = "numNeg"
    bwNot = "bwNot"
    yield = "yield"


############################################
# Definition of Classes
############################################

class XmlFragment:

    pass
class dom_XmlTextFragment(XmlFragment):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class IUnqualifiedSelector:

    pass
class dom_ExpressionSelector(IUnqualifiedSelector):

    pass
class dom_IPropertySelector(IUnqualifiedSelector):

    pass
class ISelector:

    pass
class dom_IUnqualifiedSelector(ISelector):

    pass
class dom_XmlExpressionFragment(XmlFragment):

    pass
class PropertyIdentifier:

    pass
class dom_QualifiedIdentifier(ISelector, PropertyIdentifier):

    pass
class dom_AttributeIdentifier(PropertyIdentifier):

    pass
class SwitchElement:

    pass
class dom_DefaultClause(SwitchElement):

    pass
class dom_CaseClause(SwitchElement):

    pass
class IterationStatement:

    pass
class dom_ForInStatement(IterationStatement):

    pass
class dom_WhileStatement(IterationStatement):

    pass
class dom_ForEachInStatement(IterationStatement):

    pass
class dom_DoStatement(IterationStatement):

    pass
class dom_ForStatement(IterationStatement):

    pass
class Statement:

    pass
class dom_ContinueStatement(Statement):

    pass
class dom_DefaultXmlNamespaceStatement(Statement):

    pass
class dom_LabeledStatement(Statement):

    pass
class dom_WithStatement(Statement):

    pass
class dom_ReturnStatement(Statement):

    pass
class dom_BreakStatement(Statement):

    pass
class dom_SwitchStatement(Statement):

    pass
class dom_TryStatement(Statement):

    pass
class dom_ThrowStatement(Statement):

    pass
class dom_IfStatement(Statement):

    pass
class dom_ConstStatement(Statement):

    pass
class dom_IterationStatement(Statement):

    pass
class dom_ExpressionStatement(Statement):

    pass
class dom_EmptyStatement(Statement):

    pass
class AccessorAssignment:

    pass
class dom_SetterAssignment(AccessorAssignment):

    pass
class dom_GetterAssignment(AccessorAssignment):

    pass
class dom_BlockStatement(Statement):

    pass
class PropertyAssignment:

    pass
class dom_AccessorAssignment(PropertyAssignment):

    pass
class dom_SimplePropertyAssignment(PropertyAssignment):

    pass
class IForInitializer:

    pass
class dom_VariableStatement(Statement, IForInitializer):

    pass
class IArrayElement:

    pass
class dom_Elision(IArrayElement):

    pass
class IPropertySelector:

    pass
class dom_WildcardIdentifier(IPropertySelector, PropertyIdentifier):

    pass
class IPropertyName:

    pass
class Node:

    pass
class dom_IPropertyName(Node):

    pass
class dom_PropertyAssignment(Node):

    pass
class dom_SwitchElement(Node):

    pass
class dom_FinallyClause(Node):

    pass
class dom_CatchClause(Node):

    pass
class dom_Parameter(Node):

    pass
class dom_IArrayElement(Node):

    pass
class dom_Label(Node):

    def __init__(self, name: str, dom_Label: "dom_ContinueStatement" = None, dom_Label84: "dom_BreakStatement" = None, dom_Label102: "dom_LabeledStatement" = None):
        self.name = name
        self.dom_Label = dom_Label
        self.dom_Label84 = dom_Label84
        self.dom_Label102 = dom_Label102
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_Label(self):
        return self.__dom_Label

    @dom_Label.setter
    def dom_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Label__dom_Label", None)
        self.__dom_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_ContinueStatement"):
                opp_val = getattr(old_value, "dom_ContinueStatement", None)
                if opp_val == self:
                    setattr(old_value, "dom_ContinueStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_ContinueStatement"):
                opp_val = getattr(value, "dom_ContinueStatement", None)
                setattr(value, "dom_ContinueStatement", self)

    @property
    def dom_Label84(self):
        return self.__dom_Label84

    @dom_Label84.setter
    def dom_Label84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Label__dom_Label84", None)
        self.__dom_Label84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_BreakStatement"):
                opp_val = getattr(old_value, "dom_BreakStatement", None)
                if opp_val == self:
                    setattr(old_value, "dom_BreakStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_BreakStatement"):
                opp_val = getattr(value, "dom_BreakStatement", None)
                setattr(value, "dom_BreakStatement", self)

    @property
    def dom_Label102(self):
        return self.__dom_Label102

    @dom_Label102.setter
    def dom_Label102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Label__dom_Label102", None)
        self.__dom_Label102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_LabeledStatement"):
                opp_val = getattr(old_value, "dom_LabeledStatement", None)
                if opp_val == self:
                    setattr(old_value, "dom_LabeledStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_LabeledStatement"):
                opp_val = getattr(value, "dom_LabeledStatement", None)
                setattr(value, "dom_LabeledStatement", self)

class dom_Statement(Node):

    pass
class dom_IProperty(Node):

    pass
class dom_XmlFragment(Node):

    pass
class dom_IForInitializer(Node):

    pass
class dom_VariableDeclaration(Node):

    pass
class dom_ISelector(Node):

    pass
class dom_Source(Node):

    pass
class dom_Expression(Node, IForInitializer, IArrayElement):

    pass
class dom_Comment(Node):

    def __init__(self, text: str, dom_Comment: "dom_FunctionExpression" = None):
        self.text = text
        self.dom_Comment = dom_Comment
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def dom_Comment(self):
        return self.__dom_Comment

    @dom_Comment.setter
    def dom_Comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Comment__dom_Comment", None)
        self.__dom_Comment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_FunctionExpression"):
                opp_val = getattr(old_value, "dom_FunctionExpression", None)
                if opp_val == self:
                    setattr(old_value, "dom_FunctionExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_FunctionExpression"):
                opp_val = getattr(value, "dom_FunctionExpression", None)
                setattr(value, "dom_FunctionExpression", self)

class dom_Node(ABC):

    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end
        
    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end

    @property
    def begin(self) -> int:
        return self.__begin

    @begin.setter
    def begin(self, begin: int):
        self.__begin = begin

class Expression:

    pass
class dom_FunctionExpression(Expression):

    def __init__(self, parametersPosition: int, dom_FunctionExpression: "dom_Comment" = None, dom_FunctionExpression128: "dom_Identifier" = None, dom_FunctionExpression131: set["dom_Parameter"] = None, dom_FunctionExpression133: "dom_BlockStatement" = None):
        self.parametersPosition = parametersPosition
        self.dom_FunctionExpression = dom_FunctionExpression
        self.dom_FunctionExpression128 = dom_FunctionExpression128
        self.dom_FunctionExpression131 = dom_FunctionExpression131 if dom_FunctionExpression131 is not None else set()
        self.dom_FunctionExpression133 = dom_FunctionExpression133
        
    @property
    def parametersPosition(self) -> int:
        return self.__parametersPosition

    @parametersPosition.setter
    def parametersPosition(self, parametersPosition: int):
        self.__parametersPosition = parametersPosition

    @property
    def dom_FunctionExpression(self):
        return self.__dom_FunctionExpression

    @dom_FunctionExpression.setter
    def dom_FunctionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FunctionExpression__dom_FunctionExpression", None)
        self.__dom_FunctionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Comment"):
                opp_val = getattr(old_value, "dom_Comment", None)
                if opp_val == self:
                    setattr(old_value, "dom_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Comment"):
                opp_val = getattr(value, "dom_Comment", None)
                setattr(value, "dom_Comment", self)

    @property
    def dom_FunctionExpression133(self):
        return self.__dom_FunctionExpression133

    @dom_FunctionExpression133.setter
    def dom_FunctionExpression133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FunctionExpression__dom_FunctionExpression133", None)
        self.__dom_FunctionExpression133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_BlockStatement134"):
                opp_val = getattr(old_value, "dom_BlockStatement134", None)
                if opp_val == self:
                    setattr(old_value, "dom_BlockStatement134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_BlockStatement134"):
                opp_val = getattr(value, "dom_BlockStatement134", None)
                setattr(value, "dom_BlockStatement134", self)

    @property
    def dom_FunctionExpression128(self):
        return self.__dom_FunctionExpression128

    @dom_FunctionExpression128.setter
    def dom_FunctionExpression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FunctionExpression__dom_FunctionExpression128", None)
        self.__dom_FunctionExpression128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Identifier129"):
                opp_val = getattr(old_value, "dom_Identifier129", None)
                if opp_val == self:
                    setattr(old_value, "dom_Identifier129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Identifier129"):
                opp_val = getattr(value, "dom_Identifier129", None)
                setattr(value, "dom_Identifier129", self)

    @property
    def dom_FunctionExpression131(self):
        return self.__dom_FunctionExpression131

    @dom_FunctionExpression131.setter
    def dom_FunctionExpression131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_FunctionExpression__dom_FunctionExpression131", None)
        self.__dom_FunctionExpression131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dom_Parameter"):
                    opp_val = getattr(item, "dom_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "dom_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dom_Parameter"):
                    opp_val = getattr(item, "dom_Parameter", None)
                    
                    setattr(item, "dom_Parameter", self)
                    

class dom_NumericLiteral(Expression, IPropertyName):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class dom_FilterExpression(Expression):

    pass
class dom_PropertyAccessExpression(Expression):

    pass
class dom_ArrayLiteral(Expression):

    pass
class dom_ConditionalExpression(Expression):

    pass
class dom_XmlInitializer(Expression):

    pass
class dom_DescendantAccessExpression(Expression):

    pass
class dom_ThisExpression(Expression):

    pass
class dom_RegularExpressionLiteral(Expression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class dom_CallExpression(Expression):

    pass
class dom_UnaryExpression(Expression):

    def __init__(self, operation: str, dom_UnaryExpression: "dom_Expression" = None):
        self.operation = operation
        self.dom_UnaryExpression = dom_UnaryExpression
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def dom_UnaryExpression(self):
        return self.__dom_UnaryExpression

    @dom_UnaryExpression.setter
    def dom_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_UnaryExpression__dom_UnaryExpression", None)
        self.__dom_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression31"):
                opp_val = getattr(old_value, "dom_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression31"):
                opp_val = getattr(value, "dom_Expression31", None)
                setattr(value, "dom_Expression31", self)

class dom_ParenthesizedExpression(Expression):

    pass
class dom_ArrayAccessExpression(Expression):

    pass
class dom_NullLiteral(Expression):

    pass
class dom_BinaryExpression(Expression):

    def __init__(self, operation: str, operatorPosition: int, dom_BinaryExpression: "dom_Expression" = None, dom_BinaryExpression35: "dom_Expression" = None):
        self.operation = operation
        self.operatorPosition = operatorPosition
        self.dom_BinaryExpression = dom_BinaryExpression
        self.dom_BinaryExpression35 = dom_BinaryExpression35
        
    @property
    def operatorPosition(self) -> int:
        return self.__operatorPosition

    @operatorPosition.setter
    def operatorPosition(self, operatorPosition: int):
        self.__operatorPosition = operatorPosition

    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def dom_BinaryExpression35(self):
        return self.__dom_BinaryExpression35

    @dom_BinaryExpression35.setter
    def dom_BinaryExpression35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BinaryExpression__dom_BinaryExpression35", None)
        self.__dom_BinaryExpression35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression36"):
                opp_val = getattr(old_value, "dom_Expression36", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression36"):
                opp_val = getattr(value, "dom_Expression36", None)
                setattr(value, "dom_Expression36", self)

    @property
    def dom_BinaryExpression(self):
        return self.__dom_BinaryExpression

    @dom_BinaryExpression.setter
    def dom_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_BinaryExpression__dom_BinaryExpression", None)
        self.__dom_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Expression33"):
                opp_val = getattr(old_value, "dom_Expression33", None)
                if opp_val == self:
                    setattr(old_value, "dom_Expression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Expression33"):
                opp_val = getattr(value, "dom_Expression33", None)
                setattr(value, "dom_Expression33", self)

class dom_StringLiteral(Expression, IPropertyName):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class dom_ObjectLiteral(Expression):

    pass
class dom_NewExpression(Expression):

    pass
class dom_BooleanLiteral(Expression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class dom_VariableReference(Expression):

    pass
class IProperty:

    pass
class dom_Identifier(Node, IPropertySelector, IProperty, IPropertyName):

    def __init__(self, name: str, dom_Identifier: "dom_VariableReference" = None, dom_Identifier8: "dom_SetterAssignment" = None, dom_Identifier50: "dom_VariableDeclaration" = None, dom_Identifier116: "dom_CatchClause" = None, dom_Identifier137: "dom_Parameter" = None, dom_Identifier129: "dom_FunctionExpression" = None):
        self.name = name
        self.dom_Identifier = dom_Identifier
        self.dom_Identifier8 = dom_Identifier8
        self.dom_Identifier50 = dom_Identifier50
        self.dom_Identifier116 = dom_Identifier116
        self.dom_Identifier137 = dom_Identifier137
        self.dom_Identifier129 = dom_Identifier129
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dom_Identifier(self):
        return self.__dom_Identifier

    @dom_Identifier.setter
    def dom_Identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Identifier__dom_Identifier", None)
        self.__dom_Identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_VariableReference"):
                opp_val = getattr(old_value, "dom_VariableReference", None)
                if opp_val == self:
                    setattr(old_value, "dom_VariableReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_VariableReference"):
                opp_val = getattr(value, "dom_VariableReference", None)
                setattr(value, "dom_VariableReference", self)

    @property
    def dom_Identifier116(self):
        return self.__dom_Identifier116

    @dom_Identifier116.setter
    def dom_Identifier116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Identifier__dom_Identifier116", None)
        self.__dom_Identifier116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_CatchClause115"):
                opp_val = getattr(old_value, "dom_CatchClause115", None)
                if opp_val == self:
                    setattr(old_value, "dom_CatchClause115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_CatchClause115"):
                opp_val = getattr(value, "dom_CatchClause115", None)
                setattr(value, "dom_CatchClause115", self)

    @property
    def dom_Identifier129(self):
        return self.__dom_Identifier129

    @dom_Identifier129.setter
    def dom_Identifier129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Identifier__dom_Identifier129", None)
        self.__dom_Identifier129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_FunctionExpression128"):
                opp_val = getattr(old_value, "dom_FunctionExpression128", None)
                if opp_val == self:
                    setattr(old_value, "dom_FunctionExpression128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_FunctionExpression128"):
                opp_val = getattr(value, "dom_FunctionExpression128", None)
                setattr(value, "dom_FunctionExpression128", self)

    @property
    def dom_Identifier8(self):
        return self.__dom_Identifier8

    @dom_Identifier8.setter
    def dom_Identifier8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Identifier__dom_Identifier8", None)
        self.__dom_Identifier8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_SetterAssignment"):
                opp_val = getattr(old_value, "dom_SetterAssignment", None)
                if opp_val == self:
                    setattr(old_value, "dom_SetterAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_SetterAssignment"):
                opp_val = getattr(value, "dom_SetterAssignment", None)
                setattr(value, "dom_SetterAssignment", self)

    @property
    def dom_Identifier137(self):
        return self.__dom_Identifier137

    @dom_Identifier137.setter
    def dom_Identifier137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Identifier__dom_Identifier137", None)
        self.__dom_Identifier137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_Parameter136"):
                opp_val = getattr(old_value, "dom_Parameter136", None)
                if opp_val == self:
                    setattr(old_value, "dom_Parameter136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_Parameter136"):
                opp_val = getattr(value, "dom_Parameter136", None)
                setattr(value, "dom_Parameter136", self)

    @property
    def dom_Identifier50(self):
        return self.__dom_Identifier50

    @dom_Identifier50.setter
    def dom_Identifier50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dom_Identifier__dom_Identifier50", None)
        self.__dom_Identifier50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dom_VariableDeclaration49"):
                opp_val = getattr(old_value, "dom_VariableDeclaration49", None)
                if opp_val == self:
                    setattr(old_value, "dom_VariableDeclaration49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dom_VariableDeclaration49"):
                opp_val = getattr(value, "dom_VariableDeclaration49", None)
                setattr(value, "dom_VariableDeclaration49", self)

class dom_PropertyIdentifier(Expression, IProperty):

    pass