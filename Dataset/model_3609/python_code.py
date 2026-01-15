from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Lambda:

    pass
class pp_RubyLambda(Lambda):

    pass
class pp_JavaLambda(Lambda):

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
class pp_ExpressionTE(TextExpression):

    pass
class pp_VariableTE(TextExpression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp_VerbatimTE(TextExpression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class pp_TextExpression(ABC):

    pass
class IfExpression:

    pass
class pp_ElseIfExpression(IfExpression):

    pass
class IQuotedString:

    pass
class StringExpression:

    pass
class pp_UnquotedString(StringExpression):

    pass
class pp_SingleQuotedString(StringExpression, IQuotedString):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class pp_DoubleQuotedString(StringExpression, IQuotedString):

    pass
class WithLambdaExpression:

    pass
class pp_MethodCall(WithLambdaExpression):

    def __init__(self, parenthesized: bool, pp_MethodCall: "pp_Expression" = None):
        self.parenthesized = parenthesized
        self.pp_MethodCall = pp_MethodCall
        
    @property
    def parenthesized(self) -> bool:
        return self.__parenthesized

    @parenthesized.setter
    def parenthesized(self, parenthesized: bool):
        self.__parenthesized = parenthesized

    @property
    def pp_MethodCall(self):
        return self.__pp_MethodCall

    @pp_MethodCall.setter
    def pp_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp_MethodCall__pp_MethodCall", None)
        self.__pp_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp_Expression88"):
                opp_val = getattr(old_value, "pp_Expression88", None)
                if opp_val == self:
                    setattr(old_value, "pp_Expression88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp_Expression88"):
                opp_val = getattr(value, "pp_Expression88", None)
                setattr(value, "pp_Expression88", self)

class pp_FunctionCall(WithLambdaExpression):

    pass
class ParameterizedExpression:

    pass
class pp_SelectorExpression(ParameterizedExpression):

    pass
class pp_WithLambdaExpression(ParameterizedExpression):

    pass
class pp_AtExpression(ParameterizedExpression):

    pass
class BinaryExpression:

    pass
class pp_NamedAccessExpression(BinaryExpression):

    pass
class pp_AppendExpression(BinaryExpression):

    pass
class pp_SelectorEntry(BinaryExpression):

    pass
class pp_BinaryOpExpression(BinaryExpression):

    def __init__(self, opName: str):
        self.opName = opName
        
    @property
    def opName(self) -> str:
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName

class pp_AndExpression(BinaryExpression):

    pass
class pp_OrExpression(BinaryExpression):

    pass
class pp_AssignmentExpression(BinaryExpression):

    pass
class BinaryOpExpression:

    pass
class pp_EqualityExpression(BinaryOpExpression):

    pass
class pp_ShiftExpression(BinaryOpExpression):

    pass
class pp_InExpression(BinaryOpExpression):

    pass
class pp_MatchingExpression(BinaryOpExpression):

    pass
class pp_AdditiveExpression(BinaryOpExpression):

    pass
class pp_MultiplicativeExpression(BinaryOpExpression):

    pass
class pp_RelationshipExpression(BinaryOpExpression):

    pass
class pp_RelationalExpression(BinaryOpExpression):

    pass
class pp_HashEntry:

    pass
class pp_IQuotedString(ABC):

    pass
class LiteralExpression:

    pass
class pp_LiteralList(LiteralExpression):

    pass
class pp_LiteralRegex(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp_LiteralDefault(LiteralExpression):

    pass
class pp_LiteralUndef(LiteralExpression):

    pass
class pp_LiteralName(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp_LiteralHash(LiteralExpression):

    pass
class pp_LiteralClass(LiteralExpression):

    pass
class pp_LiteralBoolean(LiteralExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class pp_VirtualNameOrReference(LiteralExpression):

    def __init__(self, value: str, exported: bool):
        self.value = value
        self.exported = exported
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def exported(self) -> bool:
        return self.__exported

    @exported.setter
    def exported(self, exported: bool):
        self.__exported = exported

class pp_LiteralNameOrReference(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Expression:

    pass
class pp_ParenthesisedExpression(Expression):

    pass
class pp_ParameterizedExpression(Expression):

    pass
class pp_BinaryExpression(Expression):

    pass
class pp_ImportExpression(Expression):

    pass
class pp_VariableExpression(Expression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp_StringExpression(Expression):

    pass
class pp_SeparatorExpression(Expression):

    pass
class pp_ExpressionBlock(Expression):

    pass
class pp_UnaryExpression(Expression):

    pass
class pp_InterpolatedVariable(Expression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp_ExprList(Expression):

    pass
class pp_ResourceExpression(Expression):

    pass
class pp_CollectExpression(Expression):

    pass
class pp_CaseExpression(Expression):

    pass
class pp_LiteralExpression(Expression):

    pass
class Definition:

    pass
class pp_HostClassDefinition(Definition):

    pass
class pp_DefinitionArgument:

    def __init__(self, argName: str, op: str, pp_DefinitionArgument: "pp_DefinitionArgumentList" = None, pp_DefinitionArgument13: "pp_Expression" = None, pp_DefinitionArgument16: "pp_Expression" = None):
        self.argName = argName
        self.op = op
        self.pp_DefinitionArgument = pp_DefinitionArgument
        self.pp_DefinitionArgument13 = pp_DefinitionArgument13
        self.pp_DefinitionArgument16 = pp_DefinitionArgument16
        
    @property
    def argName(self) -> str:
        return self.__argName

    @argName.setter
    def argName(self, argName: str):
        self.__argName = argName

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def pp_DefinitionArgument16(self):
        return self.__pp_DefinitionArgument16

    @pp_DefinitionArgument16.setter
    def pp_DefinitionArgument16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp_DefinitionArgument__pp_DefinitionArgument16", None)
        self.__pp_DefinitionArgument16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp_Expression17"):
                opp_val = getattr(old_value, "pp_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "pp_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp_Expression17"):
                opp_val = getattr(value, "pp_Expression17", None)
                setattr(value, "pp_Expression17", self)

    @property
    def pp_DefinitionArgument13(self):
        return self.__pp_DefinitionArgument13

    @pp_DefinitionArgument13.setter
    def pp_DefinitionArgument13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp_DefinitionArgument__pp_DefinitionArgument13", None)
        self.__pp_DefinitionArgument13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp_Expression14"):
                opp_val = getattr(old_value, "pp_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "pp_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp_Expression14"):
                opp_val = getattr(value, "pp_Expression14", None)
                setattr(value, "pp_Expression14", self)

    @property
    def pp_DefinitionArgument(self):
        return self.__pp_DefinitionArgument

    @pp_DefinitionArgument.setter
    def pp_DefinitionArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp_DefinitionArgument__pp_DefinitionArgument", None)
        self.__pp_DefinitionArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp_DefinitionArgumentList11"):
                opp_val = getattr(old_value, "pp_DefinitionArgumentList11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp_DefinitionArgumentList11"):
                opp_val = getattr(value, "pp_DefinitionArgumentList11", None)
                if opp_val is None:
                    setattr(value, "pp_DefinitionArgumentList11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ICollectQuery:

    pass
class UnaryExpression:

    pass
class pp_UnaryMinusExpression(UnaryExpression):

    pass
class pp_UnaryNotExpression(UnaryExpression):

    pass
class pp_ExportedCollectQuery(ICollectQuery, UnaryExpression):

    pass
class pp_VirtualCollectQuery(ICollectQuery, UnaryExpression):

    pass
class pp_ICollectQuery(ABC):

    pass
class pp_DefinitionArgumentList:

    pass
class pp_Expression:

    pass
class ExpressionBlock:

    pass
class pp_Lambda(ExpressionBlock):

    pass
class pp_ElseExpression(ExpressionBlock):

    pass
class pp_Definition(ExpressionBlock):

    def __init__(self, className: str, pp_Definition: "pp_DefinitionArgumentList" = None):
        self.className = className
        self.pp_Definition = pp_Definition
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def pp_Definition(self):
        return self.__pp_Definition

    @pp_Definition.setter
    def pp_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp_Definition__pp_Definition", None)
        self.__pp_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp_DefinitionArgumentList"):
                opp_val = getattr(old_value, "pp_DefinitionArgumentList", None)
                if opp_val == self:
                    setattr(old_value, "pp_DefinitionArgumentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp_DefinitionArgumentList"):
                opp_val = getattr(value, "pp_DefinitionArgumentList", None)
                setattr(value, "pp_DefinitionArgumentList", self)

class pp_UnlessExpression(ExpressionBlock):

    pass
class pp_NodeDefinition(ExpressionBlock):

    pass
class pp_IfExpression(ExpressionBlock):

    pass
class pp_Case(ExpressionBlock):

    pass
class pp_PuppetManifest(ExpressionBlock):

    pass
class pp_AttributeOperation:

    def __init__(self, key: str, op: str, pp_AttributeOperation: "pp_Expression" = None, pp_AttributeOperation7: "pp_AttributeOperations" = None):
        self.key = key
        self.op = op
        self.pp_AttributeOperation = pp_AttributeOperation
        self.pp_AttributeOperation7 = pp_AttributeOperation7
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def pp_AttributeOperation(self):
        return self.__pp_AttributeOperation

    @pp_AttributeOperation.setter
    def pp_AttributeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp_AttributeOperation__pp_AttributeOperation", None)
        self.__pp_AttributeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp_Expression4"):
                opp_val = getattr(old_value, "pp_Expression4", None)
                if opp_val == self:
                    setattr(old_value, "pp_Expression4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp_Expression4"):
                opp_val = getattr(value, "pp_Expression4", None)
                setattr(value, "pp_Expression4", self)

    @property
    def pp_AttributeOperation7(self):
        return self.__pp_AttributeOperation7

    @pp_AttributeOperation7.setter
    def pp_AttributeOperation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp_AttributeOperation__pp_AttributeOperation7", None)
        self.__pp_AttributeOperation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp_AttributeOperations6"):
                opp_val = getattr(old_value, "pp_AttributeOperations6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp_AttributeOperations6"):
                opp_val = getattr(value, "pp_AttributeOperations6", None)
                if opp_val is None:
                    setattr(value, "pp_AttributeOperations6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pp_AttributeOperations:

    pass
class pp_ResourceBody:

    pass