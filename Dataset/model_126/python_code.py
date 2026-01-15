from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ActualParameterExpression:

    pass
class astm_ByReferenceActualParameterExpression(ActualParameterExpression):

    pass
class astm_ByValueActualParameterExpression(ActualParameterExpression):

    pass
class astm_Visitable(ABC):

    pass
class Literal:

    pass
class astm_BooleanLiteral(Literal):

    pass
class astm_RealLiteral(Literal):

    pass
class astm_StringLiteral(Literal):

    pass
class astm_CharLiteral(Literal):

    pass
class astm_IntegerLiteral(Literal):

    pass
class QualifiedIdentifierReference:

    pass
class astm_QualifiedOverData(QualifiedIdentifierReference):

    pass
class astm_QualifiedOverPointer(QualifiedIdentifierReference):

    pass
class UnaryOperator:

    pass
class astm_BitNot(UnaryOperator):

    pass
class astm_Deref(UnaryOperator):

    pass
class astm_AddressOf(UnaryOperator):

    pass
class astm_Increment(UnaryOperator):

    pass
class astm_Negate(UnaryOperator):

    pass
class astm_PostDecrement(UnaryOperator):

    pass
class astm_Not(UnaryOperator):

    pass
class astm_Decrement(UnaryOperator):

    pass
class astm_PostIncrement(UnaryOperator):

    pass
class astm_UnaryPlus(UnaryOperator):

    pass
class astm_BitLiteral(Literal):

    pass
class ForStatement:

    pass
class astm_ForCheckAfterStatement(ForStatement):

    pass
class astm_ForCheckBeforeStatement(ForStatement):

    pass
class AccessKind:

    pass
class astm_Private(AccessKind):

    pass
class astm_Protected(AccessKind):

    pass
class astm_Public(AccessKind):

    pass
class FormalParameterType:

    pass
class astm_ByReferenceFormalParameterType(FormalParameterType):

    pass
class astm_ByValueFormalParameterType(FormalParameterType):

    pass
class PrimitiveType:

    pass
class astm_Void(PrimitiveType):

    pass
class VirtualSpecification:

    pass
class astm_NonVirtual(VirtualSpecification):

    pass
class astm_PureVirtual(VirtualSpecification):

    pass
class astm_Virtual(VirtualSpecification):

    pass
class astm_WideCharacter(PrimitiveType):

    pass
class astm_Boolean(PrimitiveType):

    pass
class astm_String(PrimitiveType):

    pass
class astm_Character(PrimitiveType):

    pass
class astm_LongDouble(PrimitiveType):

    pass
class astm_Double(PrimitiveType):

    pass
class astm_Float(PrimitiveType):

    pass
class astm_LongInteger(PrimitiveType):

    pass
class astm_Integer(PrimitiveType):

    pass
class astm_ShortInteger(PrimitiveType):

    pass
class astm_Byte(PrimitiveType):

    pass
class Scope:

    pass
class StorageSpecification:

    pass
class astm_NoDef(StorageSpecification):

    pass
class astm_FunctionPersistent(StorageSpecification):

    pass
class astm_PerClassMember(StorageSpecification):

    pass
class astm_FileLocal(StorageSpecification):

    pass
class astm_External(StorageSpecification):

    pass
class ActualParameter:

    pass
class astm_MissingActualParameter(ActualParameter):

    pass
class astm_ActualParameterExpression(ActualParameter):

    pass
class BinaryOperator:

    pass
class astm_Assign(BinaryOperator):

    pass
class astm_Or(BinaryOperator):

    pass
class astm_Greater(BinaryOperator):

    pass
class astm_BitLeftShift(BinaryOperator):

    pass
class astm_Equal(BinaryOperator):

    pass
class astm_Exponent(BinaryOperator):

    pass
class astm_SpecificIn(BinaryOperator):

    pass
class astm_BitOr(BinaryOperator):

    pass
class astm_SpecificGreaterEqual(BinaryOperator):

    pass
class astm_And(BinaryOperator):

    pass
class astm_BitAnd(BinaryOperator):

    pass
class astm_SpecificLessEqual(BinaryOperator):

    pass
class astm_NotLess(BinaryOperator):

    pass
class astm_Divide(BinaryOperator):

    pass
class astm_BitRightShift(BinaryOperator):

    pass
class astm_Modulus(BinaryOperator):

    pass
class astm_BitXor(BinaryOperator):

    pass
class astm_Subtract(BinaryOperator):

    pass
class astm_Multiply(BinaryOperator):

    pass
class astm_Less(BinaryOperator):

    pass
class astm_Add(BinaryOperator):

    pass
class astm_NotGreater(BinaryOperator):

    pass
class astm_SpecificConcatString(BinaryOperator):

    pass
class astm_SpecificLike(BinaryOperator):

    pass
class astm_NotEqual(BinaryOperator):

    pass
class astm_OperatorAssign(BinaryOperator):

    pass
class Expression:

    pass
class astm_AggregateExpression(Expression):

    pass
class astm_BinaryExpression(Expression):

    pass
class astm_Literal(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class astm_ArrayAccess(Expression):

    pass
class astm_NewExpression(Expression):

    pass
class astm_RangeExpression(Expression):

    pass
class astm_ConditionalExpression(Expression):

    pass
class astm_UnaryExpression(Expression):

    pass
class astm_FunctionCallExpression(Expression):

    pass
class astm_CastExpression(Expression):

    pass
class astm_NameReference(Expression):

    pass
class NameReference:

    pass
class astm_IdentifierReference(NameReference):

    pass
class astm_TypeQualifiedIdentifierReference(NameReference):

    pass
class astm_QualifiedIdentifierReference(NameReference):

    pass
class CatchBlock:

    pass
class astm_TypesCatchBlock(CatchBlock):

    pass
class astm_VariableCatchBlock(CatchBlock):

    pass
class SwitchCase:

    pass
class astm_DefaultBlock(SwitchCase):

    pass
class astm_CaseBlock(SwitchCase):

    pass
class LoopStatement:

    pass
class astm_WhileStatement(LoopStatement):

    pass
class astm_DoWhileStatement(LoopStatement):

    pass
class astm_ForStatement(LoopStatement):

    pass
class Statement:

    pass
class astm_ExpressionStatement(Statement):

    pass
class astm_SpecificSelectStatement(Statement):

    pass
class astm_LoopStatement(Statement):

    pass
class astm_ReturnStatement(Statement):

    pass
class astm_DeclarationOrDefinitionStatement(Statement):

    pass
class astm_ThrowStatement(Statement):

    pass
class astm_TryStatement(Statement):

    pass
class astm_JumpStatement(Statement):

    pass
class astm_TerminateStatement(Statement):

    pass
class astm_SwitchStatement(Statement):

    pass
class astm_EmptyStatement(Statement):

    pass
class astm_IfStatement(Statement):

    pass
class astm_DeleteStatement(Statement):

    pass
class astm_BlockScope(Scope):

    pass
class astm_BlockStatement(Statement):

    pass
class astm_LabeledStatement(Statement):

    pass
class astm_ContinueStatement(Statement):

    pass
class astm_LabelAccess(Expression):

    pass
class astm_BreakStatement(Statement):

    pass
class TypeReference:

    pass
class astm_UnnamedTypeReference(TypeReference):

    pass
class AggregateType:

    pass
class astm_AnnotationType(AggregateType):

    pass
class astm_UnionType(AggregateType):

    pass
class astm_StructureType(AggregateType):

    pass
class astm_ClassType(AggregateType):

    pass
class DataType:

    pass
class astm_ExceptionType(DataType):

    pass
class astm_FormalParameterType(DataType):

    pass
class astm_PrimitiveType(DataType):

    def __init__(self, isSigned: bool):
        self.isSigned = isSigned
        
    @property
    def isSigned(self) -> bool:
        return self.__isSigned

    @isSigned.setter
    def isSigned(self, isSigned: bool):
        self.__isSigned = isSigned

class ConstructedType:

    pass
class astm_PointerType(ConstructedType):

    pass
class astm_CollectionType(ConstructedType):

    pass
class astm_RangeType(ConstructedType):

    pass
class astm_ReferenceType(ConstructedType):

    pass
class astm_ArrayType(ConstructedType):

    pass
class astm_AggregateScope(Scope):

    pass
class astm_ConstructedType(DataType):

    pass
class astm_EnumType(DataType):

    pass
class astm_AggregateType(DataType):

    pass
class astm_NamedType(DataType):

    pass
class TypeDefinition:

    pass
class astm_AggregateTypeDefinition(TypeDefinition):

    pass
class astm_NamedTypeDefinition(TypeDefinition):

    pass
class PreprocessorElement:

    pass
class astm_MacroDefinition(PreprocessorElement):

    def __init__(self, macroName: str, body: str, astm_MacroDefinition: "astm_MacroCall" = None):
        self.macroName = macroName
        self.body = body
        self.astm_MacroDefinition = astm_MacroDefinition
        
    @property
    def macroName(self) -> str:
        return self.__macroName

    @macroName.setter
    def macroName(self, macroName: str):
        self.__macroName = macroName

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def astm_MacroDefinition(self):
        return self.__astm_MacroDefinition

    @astm_MacroDefinition.setter
    def astm_MacroDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_MacroDefinition__astm_MacroDefinition", None)
        self.__astm_MacroDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_MacroCall"):
                opp_val = getattr(old_value, "astm_MacroCall", None)
                if opp_val == self:
                    setattr(old_value, "astm_MacroCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_MacroCall"):
                opp_val = getattr(value, "astm_MacroCall", None)
                setattr(value, "astm_MacroCall", self)

class astm_Comment(PreprocessorElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class astm_MacroCall(PreprocessorElement):

    pass
class astm_IncludeUnit(PreprocessorElement):

    pass
class astm_FunctionScope(Scope):

    pass
class DataDefinition:

    pass
class astm_VariableDefinition(DataDefinition):

    pass
class astm_BitFieldDefinition(DataDefinition):

    pass
class DeclarationOrDefinition:

    pass
class astm_Declaration(DeclarationOrDefinition):

    pass
class astm_Definition(DeclarationOrDefinition):

    pass
class astm_FormalParameterDefinition(DataDefinition):

    pass
class Definition:

    pass
class astm_DataDefinition(Definition):

    def __init__(self, isMutable: bool, astm_DataDefinition: "astm_Expression" = None, astm_DataDefinition206: "astm_VariableCatchBlock" = None):
        self.isMutable = isMutable
        self.astm_DataDefinition = astm_DataDefinition
        self.astm_DataDefinition206 = astm_DataDefinition206
        
    @property
    def isMutable(self) -> bool:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable

    @property
    def astm_DataDefinition206(self):
        return self.__astm_DataDefinition206

    @astm_DataDefinition206.setter
    def astm_DataDefinition206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DataDefinition__astm_DataDefinition206", None)
        self.__astm_DataDefinition206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_VariableCatchBlock"):
                opp_val = getattr(old_value, "astm_VariableCatchBlock", None)
                if opp_val == self:
                    setattr(old_value, "astm_VariableCatchBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_VariableCatchBlock"):
                opp_val = getattr(value, "astm_VariableCatchBlock", None)
                setattr(value, "astm_VariableCatchBlock", self)

    @property
    def astm_DataDefinition(self):
        return self.__astm_DataDefinition

    @astm_DataDefinition.setter
    def astm_DataDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DataDefinition__astm_DataDefinition", None)
        self.__astm_DataDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_Expression"):
                opp_val = getattr(old_value, "astm_Expression", None)
                if opp_val == self:
                    setattr(old_value, "astm_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_Expression"):
                opp_val = getattr(value, "astm_Expression", None)
                setattr(value, "astm_Expression", self)

class astm_SpecificTriggerDefinition(Definition):

    pass
class astm_EntryDefinition(Definition):

    pass
class astm_EnumLiteralDefinition(Definition):

    pass
class astm_FunctionDefinition(Definition):

    pass
class Declaration:

    pass
class astm_VariableDeclaration(Declaration):

    def __init__(self, isMutable: bool):
        self.isMutable = isMutable
        
    @property
    def isMutable(self) -> bool:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable

class astm_FormalParameterDeclaration(Declaration):

    pass
class astm_FunctionDeclaration(Declaration):

    pass
class GASTMObject:

    pass
class astm_GASTMSyntaxObject(GASTMObject):

    pass
class astm_GlobalScope(Scope):

    pass
class DefinitionObject:

    pass
class astm_LabelDefinition(DefinitionObject):

    pass
class astm_TypeDefinition(DefinitionObject):

    pass
class astm_NameSpaceDefinition(DefinitionObject):

    pass
class astm_DeclarationOrDefinition(DefinitionObject):

    def __init__(self, isRegister: bool, linkageSpecifier: str, astm_DeclarationOrDefinition: "astm_OtherSyntaxObject" = None, astm_DeclarationOrDefinition43: "astm_OtherSyntaxObject" = None):
        self.isRegister = isRegister
        self.linkageSpecifier = linkageSpecifier
        self.astm_DeclarationOrDefinition = astm_DeclarationOrDefinition
        self.astm_DeclarationOrDefinition43 = astm_DeclarationOrDefinition43
        
    @property
    def isRegister(self) -> bool:
        return self.__isRegister

    @isRegister.setter
    def isRegister(self, isRegister: bool):
        self.__isRegister = isRegister

    @property
    def linkageSpecifier(self) -> str:
        return self.__linkageSpecifier

    @linkageSpecifier.setter
    def linkageSpecifier(self, linkageSpecifier: str):
        self.__linkageSpecifier = linkageSpecifier

    @property
    def astm_DeclarationOrDefinition43(self):
        return self.__astm_DeclarationOrDefinition43

    @astm_DeclarationOrDefinition43.setter
    def astm_DeclarationOrDefinition43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DeclarationOrDefinition__astm_DeclarationOrDefinition43", None)
        self.__astm_DeclarationOrDefinition43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_OtherSyntaxObject44"):
                opp_val = getattr(old_value, "astm_OtherSyntaxObject44", None)
                if opp_val == self:
                    setattr(old_value, "astm_OtherSyntaxObject44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_OtherSyntaxObject44"):
                opp_val = getattr(value, "astm_OtherSyntaxObject44", None)
                setattr(value, "astm_OtherSyntaxObject44", self)

    @property
    def astm_DeclarationOrDefinition(self):
        return self.__astm_DeclarationOrDefinition

    @astm_DeclarationOrDefinition.setter
    def astm_DeclarationOrDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DeclarationOrDefinition__astm_DeclarationOrDefinition", None)
        self.__astm_DeclarationOrDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_OtherSyntaxObject"):
                opp_val = getattr(old_value, "astm_OtherSyntaxObject", None)
                if opp_val == self:
                    setattr(old_value, "astm_OtherSyntaxObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_OtherSyntaxObject"):
                opp_val = getattr(value, "astm_OtherSyntaxObject", None)
                setattr(value, "astm_OtherSyntaxObject", self)

class astm_ProgramScope(Scope):

    pass
class OtherSyntaxObject:

    pass
class astm_VirtualSpecification(OtherSyntaxObject):

    pass
class astm_Operator(OtherSyntaxObject):

    pass
class astm_Dimension(OtherSyntaxObject):

    pass
class astm_SwitchCase(OtherSyntaxObject):

    pass
class astm_CatchBlock(OtherSyntaxObject):

    pass
class astm_DerivesFrom(OtherSyntaxObject):

    def __init__(self, isVirtual: bool, astm_DerivesFrom: "astm_ClassType" = None, astm_DerivesFrom131: "astm_OtherSyntaxObject" = None, astm_DerivesFrom134: "astm_NamedType" = None):
        self.isVirtual = isVirtual
        self.astm_DerivesFrom = astm_DerivesFrom
        self.astm_DerivesFrom131 = astm_DerivesFrom131
        self.astm_DerivesFrom134 = astm_DerivesFrom134
        
    @property
    def isVirtual(self) -> bool:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual

    @property
    def astm_DerivesFrom131(self):
        return self.__astm_DerivesFrom131

    @astm_DerivesFrom131.setter
    def astm_DerivesFrom131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DerivesFrom__astm_DerivesFrom131", None)
        self.__astm_DerivesFrom131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_OtherSyntaxObject132"):
                opp_val = getattr(old_value, "astm_OtherSyntaxObject132", None)
                if opp_val == self:
                    setattr(old_value, "astm_OtherSyntaxObject132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_OtherSyntaxObject132"):
                opp_val = getattr(value, "astm_OtherSyntaxObject132", None)
                setattr(value, "astm_OtherSyntaxObject132", self)

    @property
    def astm_DerivesFrom(self):
        return self.__astm_DerivesFrom

    @astm_DerivesFrom.setter
    def astm_DerivesFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DerivesFrom__astm_DerivesFrom", None)
        self.__astm_DerivesFrom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_ClassType"):
                opp_val = getattr(old_value, "astm_ClassType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_ClassType"):
                opp_val = getattr(value, "astm_ClassType", None)
                if opp_val is None:
                    setattr(value, "astm_ClassType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def astm_DerivesFrom134(self):
        return self.__astm_DerivesFrom134

    @astm_DerivesFrom134.setter
    def astm_DerivesFrom134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DerivesFrom__astm_DerivesFrom134", None)
        self.__astm_DerivesFrom134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_NamedType135"):
                opp_val = getattr(old_value, "astm_NamedType135", None)
                if opp_val == self:
                    setattr(old_value, "astm_NamedType135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NamedType135"):
                opp_val = getattr(value, "astm_NamedType135", None)
                setattr(value, "astm_NamedType135", self)

class astm_FunctionMemberAttribute(OtherSyntaxObject):

    pass
class astm_AnnotationExpression(Expression):

    pass
class GASTMSyntaxObject:

    pass
class astm_Type(GASTMSyntaxObject):

    def __init__(self, isConst: bool, isVolatile: bool, astm_Type: "astm_NamedType" = None, astm_Type137: "astm_UnnamedTypeReference" = None, astm_Type204: "astm_TypesCatchBlock" = None):
        self.isConst = isConst
        self.isVolatile = isVolatile
        self.astm_Type = astm_Type
        self.astm_Type137 = astm_Type137
        self.astm_Type204 = astm_Type204
        
    @property
    def isVolatile(self) -> bool:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: bool):
        self.__isVolatile = isVolatile

    @property
    def isConst(self) -> bool:
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: bool):
        self.__isConst = isConst

    @property
    def astm_Type(self):
        return self.__astm_Type

    @astm_Type.setter
    def astm_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Type__astm_Type", None)
        self.__astm_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_NamedType128"):
                opp_val = getattr(old_value, "astm_NamedType128", None)
                if opp_val == self:
                    setattr(old_value, "astm_NamedType128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NamedType128"):
                opp_val = getattr(value, "astm_NamedType128", None)
                setattr(value, "astm_NamedType128", self)

    @property
    def astm_Type204(self):
        return self.__astm_Type204

    @astm_Type204.setter
    def astm_Type204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Type__astm_Type204", None)
        self.__astm_Type204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_TypesCatchBlock"):
                opp_val = getattr(old_value, "astm_TypesCatchBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_TypesCatchBlock"):
                opp_val = getattr(value, "astm_TypesCatchBlock", None)
                if opp_val is None:
                    setattr(value, "astm_TypesCatchBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def astm_Type137(self):
        return self.__astm_Type137

    @astm_Type137.setter
    def astm_Type137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Type__astm_Type137", None)
        self.__astm_Type137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_UnnamedTypeReference"):
                opp_val = getattr(old_value, "astm_UnnamedTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "astm_UnnamedTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_UnnamedTypeReference"):
                opp_val = getattr(value, "astm_UnnamedTypeReference", None)
                setattr(value, "astm_UnnamedTypeReference", self)

class astm_Expression(GASTMSyntaxObject):

    pass
class astm_Statement(GASTMSyntaxObject):

    pass
class astm_PreprocessorElement(GASTMSyntaxObject):

    pass
class astm_OtherSyntaxObject(GASTMSyntaxObject):

    pass
class Visitable:

    pass
class astm_StorageSpecification(Visitable):

    pass
class astm_FunctionMemberAttributes(Visitable):

    def __init__(self, isInline: bool, isThisConst: bool, isFriend: bool, astm_FunctionMemberAttributes: "astm_FunctionDeclaration" = None, astm_FunctionMemberAttributes75: "astm_VirtualSpecification" = None, astm_FunctionMemberAttributes71: "astm_FunctionDefinition" = None):
        self.isInline = isInline
        self.isThisConst = isThisConst
        self.isFriend = isFriend
        self.astm_FunctionMemberAttributes = astm_FunctionMemberAttributes
        self.astm_FunctionMemberAttributes75 = astm_FunctionMemberAttributes75
        self.astm_FunctionMemberAttributes71 = astm_FunctionMemberAttributes71
        
    @property
    def isFriend(self) -> bool:
        return self.__isFriend

    @isFriend.setter
    def isFriend(self, isFriend: bool):
        self.__isFriend = isFriend

    @property
    def isInline(self) -> bool:
        return self.__isInline

    @isInline.setter
    def isInline(self, isInline: bool):
        self.__isInline = isInline

    @property
    def isThisConst(self) -> bool:
        return self.__isThisConst

    @isThisConst.setter
    def isThisConst(self, isThisConst: bool):
        self.__isThisConst = isThisConst

    @property
    def astm_FunctionMemberAttributes71(self):
        return self.__astm_FunctionMemberAttributes71

    @astm_FunctionMemberAttributes71.setter
    def astm_FunctionMemberAttributes71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_FunctionMemberAttributes__astm_FunctionMemberAttributes71", None)
        self.__astm_FunctionMemberAttributes71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_FunctionDefinition70"):
                opp_val = getattr(old_value, "astm_FunctionDefinition70", None)
                if opp_val == self:
                    setattr(old_value, "astm_FunctionDefinition70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_FunctionDefinition70"):
                opp_val = getattr(value, "astm_FunctionDefinition70", None)
                setattr(value, "astm_FunctionDefinition70", self)

    @property
    def astm_FunctionMemberAttributes(self):
        return self.__astm_FunctionMemberAttributes

    @astm_FunctionMemberAttributes.setter
    def astm_FunctionMemberAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_FunctionMemberAttributes__astm_FunctionMemberAttributes", None)
        self.__astm_FunctionMemberAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_FunctionDeclaration59"):
                opp_val = getattr(old_value, "astm_FunctionDeclaration59", None)
                if opp_val == self:
                    setattr(old_value, "astm_FunctionDeclaration59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_FunctionDeclaration59"):
                opp_val = getattr(value, "astm_FunctionDeclaration59", None)
                setattr(value, "astm_FunctionDeclaration59", self)

    @property
    def astm_FunctionMemberAttributes75(self):
        return self.__astm_FunctionMemberAttributes75

    @astm_FunctionMemberAttributes75.setter
    def astm_FunctionMemberAttributes75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_FunctionMemberAttributes__astm_FunctionMemberAttributes75", None)
        self.__astm_FunctionMemberAttributes75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_VirtualSpecification"):
                opp_val = getattr(old_value, "astm_VirtualSpecification", None)
                if opp_val == self:
                    setattr(old_value, "astm_VirtualSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_VirtualSpecification"):
                opp_val = getattr(value, "astm_VirtualSpecification", None)
                setattr(value, "astm_VirtualSpecification", self)

class astm_GASTMSemanticObject(Visitable):

    pass
class astm_GASTMSourceObject(Visitable):

    pass
class astm_GASTMObject(Visitable):

    pass
class astm_CompilationUnit(OtherSyntaxObject):

    def __init__(self, language: str, astm_CompilationUnit37: set["astm_DefinitionObject"] = None, astm_CompilationUnit40: "astm_ProgramScope" = None, astm_CompilationUnit: "astm_Project" = None):
        self.language = language
        self.astm_CompilationUnit37 = astm_CompilationUnit37 if astm_CompilationUnit37 is not None else set()
        self.astm_CompilationUnit40 = astm_CompilationUnit40
        self.astm_CompilationUnit = astm_CompilationUnit
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def astm_CompilationUnit37(self):
        return self.__astm_CompilationUnit37

    @astm_CompilationUnit37.setter
    def astm_CompilationUnit37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_CompilationUnit__astm_CompilationUnit37", None)
        self.__astm_CompilationUnit37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "astm_DefinitionObject38"):
                    opp_val = getattr(item, "astm_DefinitionObject38", None)
                    
                    if opp_val == self:
                        setattr(item, "astm_DefinitionObject38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "astm_DefinitionObject38"):
                    opp_val = getattr(item, "astm_DefinitionObject38", None)
                    
                    setattr(item, "astm_DefinitionObject38", self)
                    

    @property
    def astm_CompilationUnit40(self):
        return self.__astm_CompilationUnit40

    @astm_CompilationUnit40.setter
    def astm_CompilationUnit40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_CompilationUnit__astm_CompilationUnit40", None)
        self.__astm_CompilationUnit40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_ProgramScope"):
                opp_val = getattr(old_value, "astm_ProgramScope", None)
                if opp_val == self:
                    setattr(old_value, "astm_ProgramScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_ProgramScope"):
                opp_val = getattr(value, "astm_ProgramScope", None)
                setattr(value, "astm_ProgramScope", self)

    @property
    def astm_CompilationUnit(self):
        return self.__astm_CompilationUnit

    @astm_CompilationUnit.setter
    def astm_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_CompilationUnit__astm_CompilationUnit", None)
        self.__astm_CompilationUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_Project"):
                opp_val = getattr(old_value, "astm_Project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_Project"):
                opp_val = getattr(value, "astm_Project", None)
                if opp_val is None:
                    setattr(value, "astm_Project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GASTMSemanticObject:

    pass
class astm_Scope(GASTMSemanticObject):

    pass
class astm_Project(GASTMSemanticObject):

    pass
class GASTMSourceObject:

    pass
class astm_SourceLocation(GASTMSourceObject):

    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int, astm_SourceLocation: "astm_SourceFile" = None, astm_SourceLocation31: "astm_GASTMSyntaxObject" = None):
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.astm_SourceLocation = astm_SourceLocation
        self.astm_SourceLocation31 = astm_SourceLocation31
        
    @property
    def endColumn(self) -> int:
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn

    @property
    def startColumn(self) -> int:
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: int):
        self.__startColumn = startColumn

    @property
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

    @property
    def startLine(self) -> int:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine

    @property
    def astm_SourceLocation31(self):
        return self.__astm_SourceLocation31

    @astm_SourceLocation31.setter
    def astm_SourceLocation31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_SourceLocation__astm_SourceLocation31", None)
        self.__astm_SourceLocation31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_GASTMSyntaxObject"):
                opp_val = getattr(old_value, "astm_GASTMSyntaxObject", None)
                if opp_val == self:
                    setattr(old_value, "astm_GASTMSyntaxObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_GASTMSyntaxObject"):
                opp_val = getattr(value, "astm_GASTMSyntaxObject", None)
                setattr(value, "astm_GASTMSyntaxObject", self)

    @property
    def astm_SourceLocation(self):
        return self.__astm_SourceLocation

    @astm_SourceLocation.setter
    def astm_SourceLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_SourceLocation__astm_SourceLocation", None)
        self.__astm_SourceLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_SourceFile"):
                opp_val = getattr(old_value, "astm_SourceFile", None)
                if opp_val == self:
                    setattr(old_value, "astm_SourceFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_SourceFile"):
                opp_val = getattr(value, "astm_SourceFile", None)
                setattr(value, "astm_SourceFile", self)

class astm_SourceFile(GASTMSourceObject):

    def __init__(self, pathName: str, astm_SourceFile: "astm_SourceLocation" = None, astm_SourceFile102: "astm_IncludeUnit" = None):
        self.pathName = pathName
        self.astm_SourceFile = astm_SourceFile
        self.astm_SourceFile102 = astm_SourceFile102
        
    @property
    def pathName(self) -> str:
        return self.__pathName

    @pathName.setter
    def pathName(self, pathName: str):
        self.__pathName = pathName

    @property
    def astm_SourceFile(self):
        return self.__astm_SourceFile

    @astm_SourceFile.setter
    def astm_SourceFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_SourceFile__astm_SourceFile", None)
        self.__astm_SourceFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_SourceLocation"):
                opp_val = getattr(old_value, "astm_SourceLocation", None)
                if opp_val == self:
                    setattr(old_value, "astm_SourceLocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_SourceLocation"):
                opp_val = getattr(value, "astm_SourceLocation", None)
                setattr(value, "astm_SourceLocation", self)

    @property
    def astm_SourceFile102(self):
        return self.__astm_SourceFile102

    @astm_SourceFile102.setter
    def astm_SourceFile102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_SourceFile__astm_SourceFile102", None)
        self.__astm_SourceFile102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_IncludeUnit"):
                opp_val = getattr(old_value, "astm_IncludeUnit", None)
                if opp_val == self:
                    setattr(old_value, "astm_IncludeUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_IncludeUnit"):
                opp_val = getattr(value, "astm_IncludeUnit", None)
                setattr(value, "astm_IncludeUnit", self)

class astm_ActualParameter(Visitable):

    pass
class Operator:

    pass
class astm_BinaryOperator(Operator):

    pass
class astm_UnaryOperator(Operator):

    pass
class astm_AccessKind(Visitable):

    pass
class Type:

    pass
class astm_TypeReference(Type):

    pass
class astm_FunctionType(Type):

    pass
class astm_LabelType(Type):

    pass
class astm_NameSpaceType(Type):

    pass
class astm_DataType(Type):

    pass
class astm_Name(OtherSyntaxObject):

    def __init__(self, nameString: str, astm_Name: "astm_DelphiUnit" = None, astm_Name53: "astm_Declaration" = None, astm_Name46: "astm_Definition" = None, astm_Name91: "astm_NameSpaceDefinition" = None, astm_Name98: "astm_LabelDefinition" = None, astm_Name87: "astm_TypeDefinition" = None, astm_Name140: "astm_NamedTypeReference" = None, astm_Name213: "astm_NameReference" = None, astm_Name277: "astm_LabelAccess" = None):
        self.nameString = nameString
        self.astm_Name = astm_Name
        self.astm_Name53 = astm_Name53
        self.astm_Name46 = astm_Name46
        self.astm_Name91 = astm_Name91
        self.astm_Name98 = astm_Name98
        self.astm_Name87 = astm_Name87
        self.astm_Name140 = astm_Name140
        self.astm_Name213 = astm_Name213
        self.astm_Name277 = astm_Name277
        
    @property
    def nameString(self) -> str:
        return self.__nameString

    @nameString.setter
    def nameString(self, nameString: str):
        self.__nameString = nameString

    @property
    def astm_Name46(self):
        return self.__astm_Name46

    @astm_Name46.setter
    def astm_Name46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name46", None)
        self.__astm_Name46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_Definition"):
                opp_val = getattr(old_value, "astm_Definition", None)
                if opp_val == self:
                    setattr(old_value, "astm_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_Definition"):
                opp_val = getattr(value, "astm_Definition", None)
                setattr(value, "astm_Definition", self)

    @property
    def astm_Name140(self):
        return self.__astm_Name140

    @astm_Name140.setter
    def astm_Name140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name140", None)
        self.__astm_Name140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_NamedTypeReference139"):
                opp_val = getattr(old_value, "astm_NamedTypeReference139", None)
                if opp_val == self:
                    setattr(old_value, "astm_NamedTypeReference139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NamedTypeReference139"):
                opp_val = getattr(value, "astm_NamedTypeReference139", None)
                setattr(value, "astm_NamedTypeReference139", self)

    @property
    def astm_Name(self):
        return self.__astm_Name

    @astm_Name.setter
    def astm_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name", None)
        self.__astm_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_DelphiUnit"):
                opp_val = getattr(old_value, "astm_DelphiUnit", None)
                if opp_val == self:
                    setattr(old_value, "astm_DelphiUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_DelphiUnit"):
                opp_val = getattr(value, "astm_DelphiUnit", None)
                setattr(value, "astm_DelphiUnit", self)

    @property
    def astm_Name87(self):
        return self.__astm_Name87

    @astm_Name87.setter
    def astm_Name87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name87", None)
        self.__astm_Name87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_TypeDefinition"):
                opp_val = getattr(old_value, "astm_TypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "astm_TypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_TypeDefinition"):
                opp_val = getattr(value, "astm_TypeDefinition", None)
                setattr(value, "astm_TypeDefinition", self)

    @property
    def astm_Name213(self):
        return self.__astm_Name213

    @astm_Name213.setter
    def astm_Name213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name213", None)
        self.__astm_Name213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_NameReference"):
                opp_val = getattr(old_value, "astm_NameReference", None)
                if opp_val == self:
                    setattr(old_value, "astm_NameReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NameReference"):
                opp_val = getattr(value, "astm_NameReference", None)
                setattr(value, "astm_NameReference", self)

    @property
    def astm_Name53(self):
        return self.__astm_Name53

    @astm_Name53.setter
    def astm_Name53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name53", None)
        self.__astm_Name53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_Declaration52"):
                opp_val = getattr(old_value, "astm_Declaration52", None)
                if opp_val == self:
                    setattr(old_value, "astm_Declaration52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_Declaration52"):
                opp_val = getattr(value, "astm_Declaration52", None)
                setattr(value, "astm_Declaration52", self)

    @property
    def astm_Name277(self):
        return self.__astm_Name277

    @astm_Name277.setter
    def astm_Name277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name277", None)
        self.__astm_Name277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_LabelAccess276"):
                opp_val = getattr(old_value, "astm_LabelAccess276", None)
                if opp_val == self:
                    setattr(old_value, "astm_LabelAccess276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_LabelAccess276"):
                opp_val = getattr(value, "astm_LabelAccess276", None)
                setattr(value, "astm_LabelAccess276", self)

    @property
    def astm_Name98(self):
        return self.__astm_Name98

    @astm_Name98.setter
    def astm_Name98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name98", None)
        self.__astm_Name98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_LabelDefinition"):
                opp_val = getattr(old_value, "astm_LabelDefinition", None)
                if opp_val == self:
                    setattr(old_value, "astm_LabelDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_LabelDefinition"):
                opp_val = getattr(value, "astm_LabelDefinition", None)
                setattr(value, "astm_LabelDefinition", self)

    @property
    def astm_Name91(self):
        return self.__astm_Name91

    @astm_Name91.setter
    def astm_Name91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name91", None)
        self.__astm_Name91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_NameSpaceDefinition"):
                opp_val = getattr(old_value, "astm_NameSpaceDefinition", None)
                if opp_val == self:
                    setattr(old_value, "astm_NameSpaceDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NameSpaceDefinition"):
                opp_val = getattr(value, "astm_NameSpaceDefinition", None)
                setattr(value, "astm_NameSpaceDefinition", self)

class CompilationUnit:

    pass
class astm_DelphiInterfaceSection(CompilationUnit):

    pass
class astm_DelphiUnit(CompilationUnit):

    pass
class FunctionCallExpression:

    pass
class astm_DelphiFunctionCallExpression(FunctionCallExpression):

    pass
class astm_DefinitionObject(GASTMSyntaxObject):

    pass
class BlockStatement:

    pass
class astm_DelphiWithStatement(BlockStatement):

    pass
class astm_DelphiBlockStatement(BlockStatement):

    pass
class astm_NamedTypeReference(TypeReference):

    pass
class astm_DelphiImplementationSection(CompilationUnit):

    pass