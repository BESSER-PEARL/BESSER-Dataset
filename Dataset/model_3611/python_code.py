from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Lambda:

    pass
class pp1_RubyLambda(Lambda):

    pass
class pp1_JavaLambda(Lambda):

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
class pp1_VariableTE(TextExpression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp1_ExpressionTE(TextExpression):

    pass
class pp1_VerbatimTE(TextExpression):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class IQuotedString:

    pass
class StringExpression:

    pass
class pp1_UnquotedString(StringExpression):

    pass
class pp1_SingleQuotedString(StringExpression, IQuotedString):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class pp1_DoubleQuotedString(StringExpression, IQuotedString):

    pass
class IfExpression:

    pass
class pp1_ElseIfExpression(IfExpression):

    pass
class pp1_TextExpression(ABC):

    pass
class ParameterizedExpression:

    pass
class pp1_SelectorExpression(ParameterizedExpression):

    pass
class pp1_WithLambdaExpression(ParameterizedExpression):

    pass
class pp1_AtExpression(ParameterizedExpression):

    pass
class BinaryExpression:

    pass
class pp1_AndExpression(BinaryExpression):

    pass
class pp1_BinaryOpExpression(BinaryExpression):

    def __init__(self, opName: str):
        self.opName = opName
        
    @property
    def opName(self) -> str:
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName

class pp1_OrExpression(BinaryExpression):

    pass
class pp1_AppendExpression(BinaryExpression):

    pass
class pp1_NamedAccessExpression(BinaryExpression):

    pass
class pp1_AssignmentExpression(BinaryExpression):

    pass
class BinaryOpExpression:

    pass
class pp1_MultiplicativeExpression(BinaryOpExpression):

    pass
class pp1_InExpression(BinaryOpExpression):

    pass
class pp1_AdditiveExpression(BinaryOpExpression):

    pass
class pp1_MatchingExpression(BinaryOpExpression):

    pass
class pp1_ShiftExpression(BinaryOpExpression):

    pass
class pp1_EqualityExpression(BinaryOpExpression):

    pass
class pp1_RelationalExpression(BinaryOpExpression):

    pass
class pp1_RelationshipExpression(BinaryOpExpression):

    pass
class WithLambdaExpression:

    pass
class pp1_MethodCall(WithLambdaExpression):

    def __init__(self, parenthesized: bool, pp1_MethodCall: "pp1_Expression" = None):
        self.parenthesized = parenthesized
        self.pp1_MethodCall = pp1_MethodCall
        
    @property
    def parenthesized(self) -> bool:
        return self.__parenthesized

    @parenthesized.setter
    def parenthesized(self, parenthesized: bool):
        self.__parenthesized = parenthesized

    @property
    def pp1_MethodCall(self):
        return self.__pp1_MethodCall

    @pp1_MethodCall.setter
    def pp1_MethodCall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp1_MethodCall__pp1_MethodCall", None)
        self.__pp1_MethodCall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp1_Expression100"):
                opp_val = getattr(old_value, "pp1_Expression100", None)
                if opp_val == self:
                    setattr(old_value, "pp1_Expression100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp1_Expression100"):
                opp_val = getattr(value, "pp1_Expression100", None)
                setattr(value, "pp1_Expression100", self)

class pp1_FunctionCall(WithLambdaExpression):

    pass
class pp1_SelectorEntry(BinaryExpression):

    pass
class pp1_HashEntry:

    pass
class pp1_IQuotedString(ABC):

    pass
class LiteralExpression:

    pass
class pp1_VirtualNameOrReference(LiteralExpression):

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

class pp1_LiteralList(LiteralExpression):

    pass
class pp1_LiteralName(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp1_LiteralBoolean(LiteralExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class pp1_LiteralClass(LiteralExpression):

    pass
class pp1_LiteralDefault(LiteralExpression):

    pass
class pp1_LiteralRegex(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp1_LiteralUndef(LiteralExpression):

    pass
class pp1_LiteralHash(LiteralExpression):

    pass
class pp1_LiteralNameOrReference(LiteralExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class pp1_DefinitionArgument:

    def __init__(self, argName: str, op: str, pp1_DefinitionArgument: "pp1_DefinitionArgumentList" = None, pp1_DefinitionArgument16: "pp1_Expression" = None):
        self.argName = argName
        self.op = op
        self.pp1_DefinitionArgument = pp1_DefinitionArgument
        self.pp1_DefinitionArgument16 = pp1_DefinitionArgument16
        
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
    def pp1_DefinitionArgument(self):
        return self.__pp1_DefinitionArgument

    @pp1_DefinitionArgument.setter
    def pp1_DefinitionArgument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp1_DefinitionArgument__pp1_DefinitionArgument", None)
        self.__pp1_DefinitionArgument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp1_DefinitionArgumentList14"):
                opp_val = getattr(old_value, "pp1_DefinitionArgumentList14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp1_DefinitionArgumentList14"):
                opp_val = getattr(value, "pp1_DefinitionArgumentList14", None)
                if opp_val is None:
                    setattr(value, "pp1_DefinitionArgumentList14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pp1_DefinitionArgument16(self):
        return self.__pp1_DefinitionArgument16

    @pp1_DefinitionArgument16.setter
    def pp1_DefinitionArgument16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp1_DefinitionArgument__pp1_DefinitionArgument16", None)
        self.__pp1_DefinitionArgument16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp1_Expression17"):
                opp_val = getattr(old_value, "pp1_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "pp1_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp1_Expression17"):
                opp_val = getattr(value, "pp1_Expression17", None)
                setattr(value, "pp1_Expression17", self)

class pp1_DefinitionArgumentList:

    pass
class Expression:

    pass
class pp1_ParenthesisedExpression(Expression):

    pass
class pp1_UnaryExpression(Expression):

    pass
class pp1_ResourceExpression(Expression):

    pass
class pp1_StringExpression(Expression):

    pass
class pp1_InterpolatedVariable(Expression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp1_ExprList(Expression):

    pass
class pp1_CollectExpression(Expression):

    pass
class pp1_ParameterizedExpression(Expression):

    pass
class pp1_SeparatorExpression(Expression):

    pass
class pp1_IfExpression(Expression):

    pass
class pp1_NodeDefinition(Expression):

    pass
class pp1_ExpressionBlock(Expression):

    pass
class pp1_BinaryExpression(Expression):

    pass
class pp1_VariableExpression(Expression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class pp1_CaseExpression(Expression):

    pass
class pp1_ImportExpression(Expression):

    pass
class pp1_UnlessExpression(Expression):

    pass
class pp1_Definition(Expression):

    def __init__(self, className: str, pp1_Definition: "pp1_DefinitionArgumentList" = None, pp1_Definition11: set["pp1_Expression"] = None):
        self.className = className
        self.pp1_Definition = pp1_Definition
        self.pp1_Definition11 = pp1_Definition11 if pp1_Definition11 is not None else set()
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def pp1_Definition11(self):
        return self.__pp1_Definition11

    @pp1_Definition11.setter
    def pp1_Definition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp1_Definition__pp1_Definition11", None)
        self.__pp1_Definition11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pp1_Expression12"):
                    opp_val = getattr(item, "pp1_Expression12", None)
                    
                    if opp_val == self:
                        setattr(item, "pp1_Expression12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pp1_Expression12"):
                    opp_val = getattr(item, "pp1_Expression12", None)
                    
                    setattr(item, "pp1_Expression12", self)
                    

    @property
    def pp1_Definition(self):
        return self.__pp1_Definition

    @pp1_Definition.setter
    def pp1_Definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp1_Definition__pp1_Definition", None)
        self.__pp1_Definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp1_DefinitionArgumentList"):
                opp_val = getattr(old_value, "pp1_DefinitionArgumentList", None)
                if opp_val == self:
                    setattr(old_value, "pp1_DefinitionArgumentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp1_DefinitionArgumentList"):
                opp_val = getattr(value, "pp1_DefinitionArgumentList", None)
                setattr(value, "pp1_DefinitionArgumentList", self)

class pp1_LiteralExpression(Expression):

    pass
class Definition:

    pass
class pp1_HostClassDefinition(Definition):

    pass
class ICollectQuery:

    pass
class UnaryExpression:

    pass
class pp1_ExportedCollectQuery(ICollectQuery, UnaryExpression):

    pass
class pp1_UnaryMinusExpression(UnaryExpression):

    pass
class pp1_UnaryNotExpression(UnaryExpression):

    pass
class pp1_VirtualCollectQuery(ICollectQuery, UnaryExpression):

    pass
class pp1_ICollectQuery(ABC):

    pass
class pp1_AttributeOperation:

    def __init__(self, key: str, op: str, pp1_AttributeOperation: "pp1_Expression" = None, pp1_AttributeOperation7: "pp1_AttributeOperations" = None):
        self.key = key
        self.op = op
        self.pp1_AttributeOperation = pp1_AttributeOperation
        self.pp1_AttributeOperation7 = pp1_AttributeOperation7
        
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
    def pp1_AttributeOperation7(self):
        return self.__pp1_AttributeOperation7

    @pp1_AttributeOperation7.setter
    def pp1_AttributeOperation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp1_AttributeOperation__pp1_AttributeOperation7", None)
        self.__pp1_AttributeOperation7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp1_AttributeOperations6"):
                opp_val = getattr(old_value, "pp1_AttributeOperations6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp1_AttributeOperations6"):
                opp_val = getattr(value, "pp1_AttributeOperations6", None)
                if opp_val is None:
                    setattr(value, "pp1_AttributeOperations6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pp1_AttributeOperation(self):
        return self.__pp1_AttributeOperation

    @pp1_AttributeOperation.setter
    def pp1_AttributeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pp1_AttributeOperation__pp1_AttributeOperation", None)
        self.__pp1_AttributeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pp1_Expression4"):
                opp_val = getattr(old_value, "pp1_Expression4", None)
                if opp_val == self:
                    setattr(old_value, "pp1_Expression4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pp1_Expression4"):
                opp_val = getattr(value, "pp1_Expression4", None)
                setattr(value, "pp1_Expression4", self)

class pp1_Case:

    pass
class pp1_AttributeOperations:

    pass
class pp1_ResourceBody:

    pass
class pp1_Expression:

    pass
class ExpressionBlock:

    pass
class pp1_Lambda(ExpressionBlock):

    pass
class pp1_ElseExpression(ExpressionBlock):

    pass
class pp1_PuppetManifest(ExpressionBlock):

    pass