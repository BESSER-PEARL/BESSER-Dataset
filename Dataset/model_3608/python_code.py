from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Lambda:

    pass
class pp2_RubyLambda(Lambda):

    pass
class pp2_JavaLambda(Lambda):

    def __init__(self, farrow: bool):
        self.farrow = farrow
        
    @property
    def farrow(self) -> bool:
        return self.__farrow

    @farrow.setter
    def farrow(self, farrow: bool):
        self.__farrow = farrow

class TextExpression:

    pass
class pp2_ExpressionTE(TextExpression):

    pass
class pp2_VerbatimTE(TextExpression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class pp2_VariableTE(TextExpression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class IQuotedString:

    pass
class StringExpression:

    pass
class pp2_DoubleQuotedString(IQuotedString, StringExpression):

    pass
class pp2_UnquotedString(StringExpression):

    pass
class pp2_SingleQuotedString(IQuotedString, StringExpression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class pp2_TextExpression(ABC):

    pass
class IfExpression:

    pass
class pp2_ElseIfExpression(IfExpression):

    pass
class ParameterizedExpression:

    pass
class pp2_WithLambdaExpression(ParameterizedExpression):

    pass
class pp2_AtExpression(ParameterizedExpression):

    pass
class WithLambdaExpression:

    pass
class pp2_MethodCall(WithLambdaExpression):

    def __init__(self, parenthesized: bool, pp2_MethodCall: "pp2_Expression" = None):
        self.parenthesized = parenthesized
        self.pp2_MethodCall = pp2_MethodCall
        
    @property
    def parenthesized(self) -> bool:
        return self.__parenthesized

    @parenthesized.setter
    def parenthesized(self, parenthesized: bool):
        self.__parenthesized = parenthesized

    @property
    def pp2_MethodCall(self):
        return self.__pp2_MethodCall

    @pp2_MethodCall.setter
    def pp2_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp2_MethodCall__pp2_MethodCall", None)
        self.__pp2_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp2_Expression88"):
                opp_val = getattr(old_value, "pp2_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "pp2_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp2_Expression88"):
                opp_val = getattr(value, "pp2_Expression88", None)
                setattr(value, "pp2_Expression88", self)

class pp2_FunctionCall(WithLambdaExpression):

    pass
class pp2_SelectorExpression(ParameterizedExpression):

    pass
class BinaryExpression:

    pass
class pp2_NamedAccessExpression(BinaryExpression):

    pass
class pp2_BinaryOpExpression(BinaryExpression):

    def __init__(self, opName: str):
        self.opName = opName
        
    @property
    def opName(self) -> str:
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName

class pp2_SelectorEntry(BinaryExpression):

    pass
class pp2_AppendExpression(BinaryExpression):

    pass
class pp2_AndExpression(BinaryExpression):

    pass
class pp2_OrExpression(BinaryExpression):

    pass
class pp2_AssignmentExpression(BinaryExpression):

    pass
class BinaryOpExpression:

    pass
class pp2_InExpression(BinaryOpExpression):

    pass
class pp2_MatchingExpression(BinaryOpExpression):

    pass
class pp2_MultiplicativeExpression(BinaryOpExpression):

    pass
class pp2_AdditiveExpression(BinaryOpExpression):

    pass
class pp2_ShiftExpression(BinaryOpExpression):

    pass
class pp2_EqualityExpression(BinaryOpExpression):

    pass
class pp2_RelationalExpression(BinaryOpExpression):

    pass
class pp2_RelationshipExpression(BinaryOpExpression):

    pass
class pp2_IQuotedString(ABC):

    pass
class pp2_HashEntry:

    pass
class LiteralExpression:

    pass
class pp2_LiteralRegex(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp2_VirtualNameOrReference(LiteralExpression):

    def __init__(self, value: str, exported: bool):
        self.value = value
        self.exported = exported
        
    @property
    def exported(self) -> bool:
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp2_LiteralList(LiteralExpression):

    pass
class pp2_LiteralClass(LiteralExpression):

    pass
class pp2_LiteralName(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp2_LiteralBoolean(LiteralExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class pp2_LiteralDefault(LiteralExpression):

    pass
class pp2_LiteralUndef(LiteralExpression):

    pass
class pp2_LiteralHash(LiteralExpression):

    pass
class pp2_LiteralNameOrReference(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp2_DefinitionArgument:

    def __init__(self, argName: str, op: str, pp2_DefinitionArgument16: "pp2_Expression" = None, pp2_DefinitionArgument: "pp2_DefinitionArgumentList" = None, pp2_DefinitionArgument13: "pp2_Expression" = None):
        self.argName = argName
        self.op = op
        self.pp2_DefinitionArgument16 = pp2_DefinitionArgument16
        self.pp2_DefinitionArgument = pp2_DefinitionArgument
        self.pp2_DefinitionArgument13 = pp2_DefinitionArgument13
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def argName(self) -> str:
        return self.__argName

    @argName.setter
    def argName(self, argName: str):
        self.__argName = argName

    @property
    def pp2_DefinitionArgument16(self):
        return self.__pp2_DefinitionArgument16

    @pp2_DefinitionArgument16.setter
    def pp2_DefinitionArgument16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp2_DefinitionArgument__pp2_DefinitionArgument16", None)
        self.__pp2_DefinitionArgument16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp2_Expression17"):
                opp_val = getattr(old_value, "pp2_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "pp2_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp2_Expression17"):
                opp_val = getattr(value, "pp2_Expression17", None)
                setattr(value, "pp2_Expression17", self)

    @property
    def pp2_DefinitionArgument(self):
        return self.__pp2_DefinitionArgument

    @pp2_DefinitionArgument.setter
    def pp2_DefinitionArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp2_DefinitionArgument__pp2_DefinitionArgument", None)
        self.__pp2_DefinitionArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp2_DefinitionArgumentList11"):
                opp_val = getattr(old_value, "pp2_DefinitionArgumentList11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp2_DefinitionArgumentList11"):
                opp_val = getattr(value, "pp2_DefinitionArgumentList11", None)
                if opp_val is None:
                    setattr(value, "pp2_DefinitionArgumentList11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pp2_DefinitionArgument13(self):
        return self.__pp2_DefinitionArgument13

    @pp2_DefinitionArgument13.setter
    def pp2_DefinitionArgument13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp2_DefinitionArgument__pp2_DefinitionArgument13", None)
        self.__pp2_DefinitionArgument13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp2_Expression14"):
                opp_val = getattr(old_value, "pp2_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "pp2_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp2_Expression14"):
                opp_val = getattr(value, "pp2_Expression14", None)
                setattr(value, "pp2_Expression14", self)

class pp2_DefinitionArgumentList:

    pass
class Expression:

    pass
class pp2_StringExpression(Expression):

    pass
class pp2_ParenthesisedExpression(Expression):

    pass
class pp2_InterpolatedVariable(Expression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp2_ParameterizedExpression(Expression):

    pass
class pp2_BinaryExpression(Expression):

    pass
class pp2_VariableExpression(Expression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp2_ResourceExpression(Expression):

    pass
class pp2_ImportExpression(Expression):

    pass
class pp2_ExpressionBlock(Expression):

    pass
class pp2_UnaryExpression(Expression):

    pass
class pp2_CollectExpression(Expression):

    pass
class pp2_ExprList(Expression):

    pass
class pp2_SeparatorExpression(Expression):

    pass
class pp2_CaseExpression(Expression):

    pass
class UnaryExpression:

    pass
class pp2_UnaryMinusExpression(UnaryExpression):

    pass
class pp2_UnaryNotExpression(UnaryExpression):

    pass
class pp2_ICollectQuery(ABC):

    pass
class pp2_LiteralExpression(Expression):

    pass
class Definition:

    pass
class pp2_HostClassDefinition(Definition):

    pass
class ICollectQuery:

    pass
class pp2_ExportedCollectQuery(ICollectQuery, UnaryExpression):

    pass
class pp2_VirtualCollectQuery(ICollectQuery, UnaryExpression):

    pass
class pp2_AttributeOperation:

    def __init__(self, key: str, op: str, pp2_AttributeOperation: "pp2_Expression" = None, pp2_AttributeOperation7: "pp2_AttributeOperations" = None):
        self.key = key
        self.op = op
        self.pp2_AttributeOperation = pp2_AttributeOperation
        self.pp2_AttributeOperation7 = pp2_AttributeOperation7
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def pp2_AttributeOperation(self):
        return self.__pp2_AttributeOperation

    @pp2_AttributeOperation.setter
    def pp2_AttributeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp2_AttributeOperation__pp2_AttributeOperation", None)
        self.__pp2_AttributeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp2_Expression4"):
                opp_val = getattr(old_value, "pp2_Expression4", None)
                if opp_val == self:
                    setattr(old_value, "pp2_Expression4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp2_Expression4"):
                opp_val = getattr(value, "pp2_Expression4", None)
                setattr(value, "pp2_Expression4", self)

    @property
    def pp2_AttributeOperation7(self):
        return self.__pp2_AttributeOperation7

    @pp2_AttributeOperation7.setter
    def pp2_AttributeOperation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp2_AttributeOperation__pp2_AttributeOperation7", None)
        self.__pp2_AttributeOperation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp2_AttributeOperations6"):
                opp_val = getattr(old_value, "pp2_AttributeOperations6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp2_AttributeOperations6"):
                opp_val = getattr(value, "pp2_AttributeOperations6", None)
                if opp_val is None:
                    setattr(value, "pp2_AttributeOperations6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pp2_AttributeOperations:

    pass
class pp2_ResourceBody:

    pass
class pp2_Expression:

    pass
class ExpressionBlock:

    pass
class pp2_IfExpression(ExpressionBlock):

    pass
class pp2_Case(ExpressionBlock):

    pass
class pp2_UnlessExpression(ExpressionBlock):

    pass
class pp2_NodeDefinition(ExpressionBlock):

    pass
class pp2_Lambda(ExpressionBlock):

    pass
class pp2_ElseExpression(ExpressionBlock):

    pass
class pp2_Definition(ExpressionBlock):

    def __init__(self, className: str, pp2_Definition: "pp2_DefinitionArgumentList" = None):
        self.className = className
        self.pp2_Definition = pp2_Definition
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def pp2_Definition(self):
        return self.__pp2_Definition

    @pp2_Definition.setter
    def pp2_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp2_Definition__pp2_Definition", None)
        self.__pp2_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp2_DefinitionArgumentList"):
                opp_val = getattr(old_value, "pp2_DefinitionArgumentList", None)
                if opp_val == self:
                    setattr(old_value, "pp2_DefinitionArgumentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp2_DefinitionArgumentList"):
                opp_val = getattr(value, "pp2_DefinitionArgumentList", None)
                setattr(value, "pp2_DefinitionArgumentList", self)

class pp2_PuppetManifest(ExpressionBlock):

    pass