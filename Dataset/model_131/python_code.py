from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class astm_Visitable(ABC):

    pass
class RDBColumnType:

    pass
class astm_RDBClob(RDBColumnType):

    pass
class astm_RDBDecimal(RDBColumnType):

    pass
class astm_RDBReal(RDBColumnType):

    pass
class astm_RDBInt(RDBColumnType):

    pass
class astm_RDBVarchar(RDBColumnType):

    pass
class astm_RDBNClob(RDBColumnType):

    pass
class astm_RDBLong(RDBColumnType):

    pass
class astm_RDBBFile(RDBColumnType):

    pass
class astm_RDBNumber(RDBColumnType):

    pass
class astm_RDBBlob(RDBColumnType):

    pass
class astm_RDBChar(RDBColumnType):

    pass
class astm_RDBFloat(RDBColumnType):

    pass
class astm_RDBInteger(RDBColumnType):

    pass
class astm_RDBBoolean(RDBColumnType):

    pass
class astm_RDBRowid(RDBColumnType):

    pass
class astm_RDBTimestamp(RDBColumnType):

    pass
class astm_RDBDate(RDBColumnType):

    pass
class astm_RDBRaw(RDBColumnType):

    pass
class astm_RDBString(RDBColumnType):

    pass
class IdentifierReference:

    pass
class astm_RDBTableAlias(IdentifierReference):

    pass
class RDBCursorStatement:

    pass
class astm_RDBCloseCursorStatement(RDBCursorStatement):

    pass
class astm_RDBOpenCursorStatement(RDBCursorStatement):

    pass
class RDBModifyStatement:

    pass
class astm_RDBDeleteStatement(RDBModifyStatement):

    pass
class astm_RDBUpdateStatement(RDBModifyStatement):

    pass
class astm_RDBFetchCursorStatement(RDBCursorStatement):

    pass
class astm_RDBTableReference(IdentifierReference):

    pass
class RDBConstraint:

    pass
class astm_RDBUniqueKey(RDBConstraint):

    pass
class astm_RDBCheckConstraint(RDBConstraint):

    def __init__(self, RDBConstraintType: str, RDBConstraintText: str):
        self.RDBConstraintType = RDBConstraintType
        self.RDBConstraintText = RDBConstraintText
        
    @property
    def RDBConstraintText(self) -> str:
        return self.__RDBConstraintText

    @RDBConstraintText.setter
    def RDBConstraintText(self, RDBConstraintText: str):
        self.__RDBConstraintText = RDBConstraintText

    @property
    def RDBConstraintType(self) -> str:
        return self.__RDBConstraintType

    @RDBConstraintType.setter
    def RDBConstraintType(self, RDBConstraintType: str):
        self.__RDBConstraintType = RDBConstraintType

class astm_RDBRefIntegrity(RDBConstraint):

    pass
class astm_RDBColumnReference(IdentifierReference):

    pass
class ActualParameterExpression:

    pass
class astm_ByReferenceActualParameterExpression(ActualParameterExpression):

    pass
class astm_ByValueActualParameterExpression(ActualParameterExpression):

    pass
class UnaryOperator:

    pass
class astm_PostDecrement(UnaryOperator):

    pass
class astm_Negate(UnaryOperator):

    pass
class astm_Not(UnaryOperator):

    pass
class astm_Decrement(UnaryOperator):

    pass
class astm_PostIncrement(UnaryOperator):

    pass
class astm_BitNot(UnaryOperator):

    pass
class astm_Deref(UnaryOperator):

    pass
class astm_AddressOf(UnaryOperator):

    pass
class astm_Increment(UnaryOperator):

    pass
class astm_UnaryPlus(UnaryOperator):

    pass
class AccessKind:

    pass
class astm_Protected(AccessKind):

    pass
class astm_Private(AccessKind):

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
class astm_Byte(PrimitiveType):

    pass
class astm_WideCharacter(PrimitiveType):

    pass
class astm_Character(PrimitiveType):

    pass
class astm_LongInteger(PrimitiveType):

    pass
class astm_Integer(PrimitiveType):

    pass
class astm_ShortInteger(PrimitiveType):

    pass
class astm_Boolean(PrimitiveType):

    pass
class astm_String(PrimitiveType):

    pass
class astm_LongDouble(PrimitiveType):

    pass
class astm_Float(PrimitiveType):

    pass
class astm_Double(PrimitiveType):

    pass
class astm_Void(PrimitiveType):

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
class astm_BitLiteral(Literal):

    pass
class astm_IntegerlLiteral(Literal):

    pass
class QualifiedIdentifierReference:

    pass
class astm_QualifiedOverData(QualifiedIdentifierReference):

    pass
class astm_QualifiedOverPointer(QualifiedIdentifierReference):

    pass
class ForStatement:

    pass
class astm_ForCheckAfterStatement(ForStatement):

    pass
class astm_ForCheckBeforeStatement(ForStatement):

    pass
class Scope:

    pass
class VirtualSpecification:

    pass
class astm_NonVirtual(VirtualSpecification):

    pass
class astm_PureVirtual(VirtualSpecification):

    pass
class astm_Virtual(VirtualSpecification):

    pass
class StorageSpecification:

    pass
class astm_PerClassMember(StorageSpecification):

    pass
class astm_FileLocal(StorageSpecification):

    pass
class astm_NoDef(StorageSpecification):

    pass
class astm_FunctionPersistent(StorageSpecification):

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
class astm_OperatorAssign(BinaryOperator):

    pass
class NameReference:

    pass
class astm_TypeQualifiedIdentifierReference(NameReference):

    pass
class astm_IdentifierReference(NameReference):

    pass
class astm_QualifiedIdentifierReference(NameReference):

    pass
class Expression:

    pass
class astm_ConditionalExpression(Expression):

    pass
class astm_RDBHostVariableExpression(Expression):

    pass
class astm_RDBSelectExpression(Expression):

    pass
class astm_NewExpression(Expression):

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

class astm_UnaryExpression(Expression):

    pass
class astm_CastExpression(Expression):

    pass
class astm_RangeExpression(Expression):

    pass
class astm_FunctionCallExpression(Expression):

    pass
class astm_NameReference(Expression):

    pass
class CatchBlock:

    pass
class astm_VariableCatchBlock(CatchBlock):

    pass
class astm_TypesCatchBlock(CatchBlock):

    pass
class astm_ArrayAccess(Expression):

    pass
class SwitchCase:

    pass
class astm_DefaultBlock(SwitchCase):

    pass
class astm_CaseBlock(SwitchCase):

    pass
class LoopStatement:

    pass
class astm_DoWhileStatement(LoopStatement):

    pass
class astm_WhileStatement(LoopStatement):

    pass
class astm_ForStatement(LoopStatement):

    pass
class astm_BlockScope(Scope):

    pass
class Statement:

    pass
class astm_BlockStatement(Statement):

    pass
class astm_ThrowStatement(Statement):

    pass
class astm_ReturnStatement(Statement):

    pass
class astm_SpecificSelectStatement(Statement):

    pass
class astm_LabeledStatement(Statement):

    pass
class astm_RDBInsertStatement(Statement):

    pass
class astm_RDBSelectStatement(Statement):

    pass
class astm_LoopStatement(Statement):

    pass
class astm_DeclarationOrDefinitionStatement(Statement):

    pass
class astm_EmptyStatement(Statement):

    pass
class astm_IfStatement(Statement):

    pass
class astm_RDBCursorStatement(Statement):

    pass
class astm_TryStatement(Statement):

    pass
class astm_SwitchStatement(Statement):

    pass
class astm_RDBModifyStatement(Statement):

    pass
class astm_TerminateStatement(Statement):

    pass
class astm_RDBConnectStatement(Statement):

    pass
class astm_DeleteStatement(Statement):

    pass
class astm_ContinueStatement(Statement):

    pass
class astm_LabelAccess(Expression):

    pass
class astm_BreakStatement(Statement):

    pass
class astm_JumpStatement(Statement):

    pass
class astm_ExpressionStatement(Statement):

    pass
class Type:

    pass
class astm_FunctionType(Type):

    pass
class TypeReference:

    pass
class astm_NamedTypeReference(TypeReference):

    pass
class astm_UnnamedTypeReference(TypeReference):

    pass
class AggregateType:

    pass
class astm_UnionType(AggregateType):

    pass
class astm_StructureType(AggregateType):

    pass
class astm_AnnotationType(AggregateType):

    pass
class astm_ClassType(AggregateType):

    pass
class DataType:

    pass
class astm_RDBColumnType(DataType):

    pass
class astm_RDBViewType(DataType):

    pass
class astm_RDBTableSpaceType(DataType):

    pass
class astm_RDBUserType(DataType):

    pass
class astm_RDBTableType(DataType):

    pass
class astm_RDBDataBaseType(DataType):

    pass
class astm_FormalParameterType(DataType):

    pass
class astm_EnumType(DataType):

    pass
class astm_RDBCursorType(DataType):

    pass
class astm_ExceptionType(DataType):

    pass
class astm_ConstructedType(DataType):

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

class GASTMSyntaxObject:

    pass
class astm_Type(GASTMSyntaxObject):

    def __init__(self, isConst: bool, isVolatile: bool, astm_Type: "astm_NamedType" = None, astm_Type111: "astm_UnnamedTypeReference" = None, astm_Type177: "astm_TypesCatchBlock" = None):
        self.isConst = isConst
        self.isVolatile = isVolatile
        self.astm_Type = astm_Type
        self.astm_Type111 = astm_Type111
        self.astm_Type177 = astm_Type177
        
    @property
    def isConst(self) -> bool:
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: bool):
        self.__isConst = isConst

    @property
    def isVolatile(self) -> bool:
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: bool):
        self.__isVolatile = isVolatile

    @property
    def astm_Type177(self):
        return self.__astm_Type177

    @astm_Type177.setter
    def astm_Type177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Type__astm_Type177", None)
        self.__astm_Type177 = value
        
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
    def astm_Type111(self):
        return self.__astm_Type111

    @astm_Type111.setter
    def astm_Type111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Type__astm_Type111", None)
        self.__astm_Type111 = value
        
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
            if hasattr(old_value, "astm_NamedType102"):
                opp_val = getattr(old_value, "astm_NamedType102", None)
                if opp_val == self:
                    setattr(old_value, "astm_NamedType102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NamedType102"):
                opp_val = getattr(value, "astm_NamedType102", None)
                setattr(value, "astm_NamedType102", self)

class ConstructedType:

    pass
class astm_ReferenceType(ConstructedType):

    pass
class astm_PointerType(ConstructedType):

    pass
class astm_CollectionType(ConstructedType):

    pass
class astm_RangeType(ConstructedType):

    pass
class astm_ArrayType(ConstructedType):

    pass
class astm_AggregateScope(Scope):

    pass
class astm_NameSpaceType(Type):

    pass
class astm_AggregateType(DataType):

    pass
class PreprocessorElement:

    pass
class astm_MacroCall(PreprocessorElement):

    pass
class astm_Comment(PreprocessorElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class astm_MacroDefinition(PreprocessorElement):

    def __init__(self, macroName: str, body: str, astm_MacroDefinition: "astm_MacroCall" = None):
        self.macroName = macroName
        self.body = body
        self.astm_MacroDefinition = astm_MacroDefinition
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def macroName(self) -> str:
        return self.__macroName

    @macroName.setter
    def macroName(self, macroName: str):
        self.__macroName = macroName

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

class astm_IncludeUnit(PreprocessorElement):

    pass
class astm_LabelType(Type):

    pass
class astm_Expression(GASTMSyntaxObject):

    pass
class astm_NamedType(DataType):

    pass
class TypeDefinition:

    pass
class astm_AggregateTypeDefinition(TypeDefinition):

    pass
class astm_NamedTypeDefinition(TypeDefinition):

    pass
class DataDefinition:

    pass
class astm_VariableDefinition(DataDefinition):

    pass
class astm_BitFieldDefinition(DataDefinition):

    pass
class Definition:

    pass
class astm_RDBTableSpaceDefinition(Definition):

    pass
class astm_RDBDatabaseDefinition(Definition):

    pass
class astm_DataDefinition(Definition):

    def __init__(self, isMutable: bool, astm_DataDefinition: "astm_Expression" = None, astm_DataDefinition179: "astm_VariableCatchBlock" = None):
        self.isMutable = isMutable
        self.astm_DataDefinition = astm_DataDefinition
        self.astm_DataDefinition179 = astm_DataDefinition179
        
    @property
    def isMutable(self) -> bool:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable

    @property
    def astm_DataDefinition179(self):
        return self.__astm_DataDefinition179

    @astm_DataDefinition179.setter
    def astm_DataDefinition179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DataDefinition__astm_DataDefinition179", None)
        self.__astm_DataDefinition179 = value
        
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

class astm_RDBUserDefinition(Definition):

    pass
class astm_EnumLiteralDefinition(Definition):

    pass
class astm_RDBViewDefinition(Definition):

    pass
class astm_RDBColumnDefinition(Definition):

    def __init__(self, NotNull: bool, astm_RDBColumnDefinition: "astm_RDBTableDefinition" = None, astm_RDBColumnDefinition277: "astm_Name" = None, astm_RDBColumnDefinition280: "astm_RDBColumnType" = None):
        self.NotNull = NotNull
        self.astm_RDBColumnDefinition = astm_RDBColumnDefinition
        self.astm_RDBColumnDefinition277 = astm_RDBColumnDefinition277
        self.astm_RDBColumnDefinition280 = astm_RDBColumnDefinition280
        
    @property
    def NotNull(self) -> bool:
        return self.__NotNull

    @NotNull.setter
    def NotNull(self, NotNull: bool):
        self.__NotNull = NotNull

    @property
    def astm_RDBColumnDefinition277(self):
        return self.__astm_RDBColumnDefinition277

    @astm_RDBColumnDefinition277.setter
    def astm_RDBColumnDefinition277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_RDBColumnDefinition__astm_RDBColumnDefinition277", None)
        self.__astm_RDBColumnDefinition277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_Name278"):
                opp_val = getattr(old_value, "astm_Name278", None)
                if opp_val == self:
                    setattr(old_value, "astm_Name278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_Name278"):
                opp_val = getattr(value, "astm_Name278", None)
                setattr(value, "astm_Name278", self)

    @property
    def astm_RDBColumnDefinition280(self):
        return self.__astm_RDBColumnDefinition280

    @astm_RDBColumnDefinition280.setter
    def astm_RDBColumnDefinition280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_RDBColumnDefinition__astm_RDBColumnDefinition280", None)
        self.__astm_RDBColumnDefinition280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_RDBColumnType"):
                opp_val = getattr(old_value, "astm_RDBColumnType", None)
                if opp_val == self:
                    setattr(old_value, "astm_RDBColumnType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_RDBColumnType"):
                opp_val = getattr(value, "astm_RDBColumnType", None)
                setattr(value, "astm_RDBColumnType", self)

    @property
    def astm_RDBColumnDefinition(self):
        return self.__astm_RDBColumnDefinition

    @astm_RDBColumnDefinition.setter
    def astm_RDBColumnDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_RDBColumnDefinition__astm_RDBColumnDefinition", None)
        self.__astm_RDBColumnDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_RDBTableDefinition269"):
                opp_val = getattr(old_value, "astm_RDBTableDefinition269", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_RDBTableDefinition269"):
                opp_val = getattr(value, "astm_RDBTableDefinition269", None)
                if opp_val is None:
                    setattr(value, "astm_RDBTableDefinition269", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class astm_RDBCursorDefinition(Definition):

    pass
class astm_SpecificTriggerDefinition(Definition):

    pass
class astm_EntryDefinition(Definition):

    pass
class astm_RDBTableDefinition(Definition):

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
class astm_FunctionScope(Scope):

    pass
class astm_Statement(GASTMSyntaxObject):

    pass
class astm_FormalParameterDefinition(DataDefinition):

    pass
class DefinitionObject:

    pass
class astm_LabelDefinition(DefinitionObject):

    pass
class astm_NameSpaceDefinition(DefinitionObject):

    pass
class astm_TypeDefinition(DefinitionObject):

    pass
class astm_DeclarationOrDefinition(DefinitionObject):

    def __init__(self, isRegister: bool, linkageSpecifier: str, astm_DeclarationOrDefinition21: "astm_OtherSyntaxObject" = None, astm_DeclarationOrDefinition: "astm_OtherSyntaxObject" = None):
        self.isRegister = isRegister
        self.linkageSpecifier = linkageSpecifier
        self.astm_DeclarationOrDefinition21 = astm_DeclarationOrDefinition21
        self.astm_DeclarationOrDefinition = astm_DeclarationOrDefinition
        
    @property
    def linkageSpecifier(self) -> str:
        return self.__linkageSpecifier

    @linkageSpecifier.setter
    def linkageSpecifier(self, linkageSpecifier: str):
        self.__linkageSpecifier = linkageSpecifier

    @property
    def isRegister(self) -> bool:
        return self.__isRegister

    @isRegister.setter
    def isRegister(self, isRegister: bool):
        self.__isRegister = isRegister

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

    @property
    def astm_DeclarationOrDefinition21(self):
        return self.__astm_DeclarationOrDefinition21

    @astm_DeclarationOrDefinition21.setter
    def astm_DeclarationOrDefinition21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DeclarationOrDefinition__astm_DeclarationOrDefinition21", None)
        self.__astm_DeclarationOrDefinition21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_OtherSyntaxObject22"):
                opp_val = getattr(old_value, "astm_OtherSyntaxObject22", None)
                if opp_val == self:
                    setattr(old_value, "astm_OtherSyntaxObject22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_OtherSyntaxObject22"):
                opp_val = getattr(value, "astm_OtherSyntaxObject22", None)
                setattr(value, "astm_OtherSyntaxObject22", self)

class astm_ProgramScope(Scope):

    pass
class astm_TypeReference(Type):

    pass
class DeclarationOrDefinition:

    pass
class astm_Declaration(DeclarationOrDefinition):

    pass
class astm_Definition(DeclarationOrDefinition):

    pass
class astm_DefinitionObject(GASTMSyntaxObject):

    pass
class astm_GlobalScope(Scope):

    pass
class GASTMSemanticObject:

    pass
class astm_Scope(GASTMSemanticObject):

    pass
class astm_Project(GASTMSemanticObject):

    pass
class OtherSyntaxObject:

    pass
class astm_RDBTrigger(Definition, OtherSyntaxObject):

    pass
class astm_SwitchCase(OtherSyntaxObject):

    pass
class astm_Dimension(OtherSyntaxObject):

    pass
class astm_VirtualSpecification(OtherSyntaxObject):

    pass
class astm_RDBIndexColumn(OtherSyntaxObject):

    def __init__(self, AscendingOrDescending: str, astm_RDBIndexColumn: "astm_IncludeUnit" = None):
        self.AscendingOrDescending = AscendingOrDescending
        self.astm_RDBIndexColumn = astm_RDBIndexColumn
        
    @property
    def AscendingOrDescending(self) -> str:
        return self.__AscendingOrDescending

    @AscendingOrDescending.setter
    def AscendingOrDescending(self, AscendingOrDescending: str):
        self.__AscendingOrDescending = AscendingOrDescending

    @property
    def astm_RDBIndexColumn(self):
        return self.__astm_RDBIndexColumn

    @astm_RDBIndexColumn.setter
    def astm_RDBIndexColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_RDBIndexColumn__astm_RDBIndexColumn", None)
        self.__astm_RDBIndexColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_IncludeUnit289"):
                opp_val = getattr(old_value, "astm_IncludeUnit289", None)
                if opp_val == self:
                    setattr(old_value, "astm_IncludeUnit289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_IncludeUnit289"):
                opp_val = getattr(value, "astm_IncludeUnit289", None)
                setattr(value, "astm_IncludeUnit289", self)

class astm_FunctionMemberAttribute(OtherSyntaxObject):

    pass
class astm_DerivesFrom(OtherSyntaxObject):

    def __init__(self, isVirtual: bool, astm_DerivesFrom: "astm_ClassType" = None, astm_DerivesFrom105: "astm_OtherSyntaxObject" = None, astm_DerivesFrom108: "astm_NamedType" = None):
        self.isVirtual = isVirtual
        self.astm_DerivesFrom = astm_DerivesFrom
        self.astm_DerivesFrom105 = astm_DerivesFrom105
        self.astm_DerivesFrom108 = astm_DerivesFrom108
        
    @property
    def isVirtual(self) -> bool:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual

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
    def astm_DerivesFrom105(self):
        return self.__astm_DerivesFrom105

    @astm_DerivesFrom105.setter
    def astm_DerivesFrom105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DerivesFrom__astm_DerivesFrom105", None)
        self.__astm_DerivesFrom105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_OtherSyntaxObject106"):
                opp_val = getattr(old_value, "astm_OtherSyntaxObject106", None)
                if opp_val == self:
                    setattr(old_value, "astm_OtherSyntaxObject106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_OtherSyntaxObject106"):
                opp_val = getattr(value, "astm_OtherSyntaxObject106", None)
                setattr(value, "astm_OtherSyntaxObject106", self)

    @property
    def astm_DerivesFrom108(self):
        return self.__astm_DerivesFrom108

    @astm_DerivesFrom108.setter
    def astm_DerivesFrom108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DerivesFrom__astm_DerivesFrom108", None)
        self.__astm_DerivesFrom108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_NamedType109"):
                opp_val = getattr(old_value, "astm_NamedType109", None)
                if opp_val == self:
                    setattr(old_value, "astm_NamedType109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NamedType109"):
                opp_val = getattr(value, "astm_NamedType109", None)
                setattr(value, "astm_NamedType109", self)

class astm_Name(OtherSyntaxObject):

    def __init__(self, nameString: str, astm_Name: "astm_Definition" = None, astm_Name30: "astm_Declaration" = None, astm_Name61: "astm_TypeDefinition" = None, astm_Name65: "astm_NameSpaceDefinition" = None, astm_Name72: "astm_LabelDefinition" = None, astm_Name113: "astm_NamedTypeReference" = None, astm_Name186: "astm_NameReference" = None, astm_Name250: "astm_LabelAccess" = None, astm_Name278: "astm_RDBColumnDefinition" = None, astm_Name287: "astm_RDBIndex" = None):
        self.nameString = nameString
        self.astm_Name = astm_Name
        self.astm_Name30 = astm_Name30
        self.astm_Name61 = astm_Name61
        self.astm_Name65 = astm_Name65
        self.astm_Name72 = astm_Name72
        self.astm_Name113 = astm_Name113
        self.astm_Name186 = astm_Name186
        self.astm_Name250 = astm_Name250
        self.astm_Name278 = astm_Name278
        self.astm_Name287 = astm_Name287
        
    @property
    def nameString(self) -> str:
        return self.__nameString

    @nameString.setter
    def nameString(self, nameString: str):
        self.__nameString = nameString

    @property
    def astm_Name61(self):
        return self.__astm_Name61

    @astm_Name61.setter
    def astm_Name61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name61", None)
        self.__astm_Name61 = value
        
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
    def astm_Name250(self):
        return self.__astm_Name250

    @astm_Name250.setter
    def astm_Name250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name250", None)
        self.__astm_Name250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_LabelAccess249"):
                opp_val = getattr(old_value, "astm_LabelAccess249", None)
                if opp_val == self:
                    setattr(old_value, "astm_LabelAccess249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_LabelAccess249"):
                opp_val = getattr(value, "astm_LabelAccess249", None)
                setattr(value, "astm_LabelAccess249", self)

    @property
    def astm_Name30(self):
        return self.__astm_Name30

    @astm_Name30.setter
    def astm_Name30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name30", None)
        self.__astm_Name30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_Declaration29"):
                opp_val = getattr(old_value, "astm_Declaration29", None)
                if opp_val == self:
                    setattr(old_value, "astm_Declaration29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_Declaration29"):
                opp_val = getattr(value, "astm_Declaration29", None)
                setattr(value, "astm_Declaration29", self)

    @property
    def astm_Name65(self):
        return self.__astm_Name65

    @astm_Name65.setter
    def astm_Name65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name65", None)
        self.__astm_Name65 = value
        
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

    @property
    def astm_Name186(self):
        return self.__astm_Name186

    @astm_Name186.setter
    def astm_Name186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name186", None)
        self.__astm_Name186 = value
        
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
    def astm_Name113(self):
        return self.__astm_Name113

    @astm_Name113.setter
    def astm_Name113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name113", None)
        self.__astm_Name113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_NamedTypeReference"):
                opp_val = getattr(old_value, "astm_NamedTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "astm_NamedTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_NamedTypeReference"):
                opp_val = getattr(value, "astm_NamedTypeReference", None)
                setattr(value, "astm_NamedTypeReference", self)

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
    def astm_Name72(self):
        return self.__astm_Name72

    @astm_Name72.setter
    def astm_Name72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name72", None)
        self.__astm_Name72 = value
        
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
    def astm_Name287(self):
        return self.__astm_Name287

    @astm_Name287.setter
    def astm_Name287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name287", None)
        self.__astm_Name287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_RDBIndex286"):
                opp_val = getattr(old_value, "astm_RDBIndex286", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_RDBIndex286"):
                opp_val = getattr(value, "astm_RDBIndex286", None)
                if opp_val is None:
                    setattr(value, "astm_RDBIndex286", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def astm_Name278(self):
        return self.__astm_Name278

    @astm_Name278.setter
    def astm_Name278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_Name__astm_Name278", None)
        self.__astm_Name278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_RDBColumnDefinition277"):
                opp_val = getattr(old_value, "astm_RDBColumnDefinition277", None)
                if opp_val == self:
                    setattr(old_value, "astm_RDBColumnDefinition277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_RDBColumnDefinition277"):
                opp_val = getattr(value, "astm_RDBColumnDefinition277", None)
                setattr(value, "astm_RDBColumnDefinition277", self)

class astm_RDBConstraint(OtherSyntaxObject):

    pass
class astm_CatchBlock(OtherSyntaxObject):

    pass
class astm_CompilationUnit(OtherSyntaxObject):

    def __init__(self, language: str, astm_CompilationUnit: "astm_Project" = None, astm_CompilationUnit15: set["astm_DefinitionObject"] = None, astm_CompilationUnit18: "astm_ProgramScope" = None):
        self.language = language
        self.astm_CompilationUnit = astm_CompilationUnit
        self.astm_CompilationUnit15 = astm_CompilationUnit15 if astm_CompilationUnit15 is not None else set()
        self.astm_CompilationUnit18 = astm_CompilationUnit18
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def astm_CompilationUnit18(self):
        return self.__astm_CompilationUnit18

    @astm_CompilationUnit18.setter
    def astm_CompilationUnit18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_CompilationUnit__astm_CompilationUnit18", None)
        self.__astm_CompilationUnit18 = value
        
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

    @property
    def astm_CompilationUnit15(self):
        return self.__astm_CompilationUnit15

    @astm_CompilationUnit15.setter
    def astm_CompilationUnit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_CompilationUnit__astm_CompilationUnit15", None)
        self.__astm_CompilationUnit15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "astm_DefinitionObject16"):
                    opp_val = getattr(item, "astm_DefinitionObject16", None)
                    
                    if opp_val == self:
                        setattr(item, "astm_DefinitionObject16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "astm_DefinitionObject16"):
                    opp_val = getattr(item, "astm_DefinitionObject16", None)
                    
                    setattr(item, "astm_DefinitionObject16", self)
                    

class astm_RDBIndex(OtherSyntaxObject):

    def __init__(self, NotNull: bool, IsUnique: bool, astm_RDBIndex: "astm_RDBTableDefinition" = None, astm_RDBIndex286: set["astm_Name"] = None):
        self.NotNull = NotNull
        self.IsUnique = IsUnique
        self.astm_RDBIndex = astm_RDBIndex
        self.astm_RDBIndex286 = astm_RDBIndex286 if astm_RDBIndex286 is not None else set()
        
    @property
    def NotNull(self) -> bool:
        return self.__NotNull

    @NotNull.setter
    def NotNull(self, NotNull: bool):
        self.__NotNull = NotNull

    @property
    def IsUnique(self) -> bool:
        return self.__IsUnique

    @IsUnique.setter
    def IsUnique(self, IsUnique: bool):
        self.__IsUnique = IsUnique

    @property
    def astm_RDBIndex286(self):
        return self.__astm_RDBIndex286

    @astm_RDBIndex286.setter
    def astm_RDBIndex286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_RDBIndex__astm_RDBIndex286", None)
        self.__astm_RDBIndex286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "astm_Name287"):
                    opp_val = getattr(item, "astm_Name287", None)
                    
                    if opp_val == self:
                        setattr(item, "astm_Name287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "astm_Name287"):
                    opp_val = getattr(item, "astm_Name287", None)
                    
                    setattr(item, "astm_Name287", self)
                    

    @property
    def astm_RDBIndex(self):
        return self.__astm_RDBIndex

    @astm_RDBIndex.setter
    def astm_RDBIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_RDBIndex__astm_RDBIndex", None)
        self.__astm_RDBIndex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_RDBTableDefinition273"):
                opp_val = getattr(old_value, "astm_RDBTableDefinition273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_RDBTableDefinition273"):
                opp_val = getattr(value, "astm_RDBTableDefinition273", None)
                if opp_val is None:
                    setattr(value, "astm_RDBTableDefinition273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class astm_AnnotationExpression(Expression):

    pass
class astm_PreprocessorElement(GASTMSyntaxObject):

    pass
class GASTMObject:

    pass
class astm_GASTMSyntaxObject(GASTMObject):

    pass
class GASTMSourceObject:

    pass
class astm_SourceLocation(GASTMSourceObject):

    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int, astm_SourceLocation9: "astm_GASTMSyntaxObject" = None, astm_SourceLocation: "astm_SourceFile" = None):
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.astm_SourceLocation9 = astm_SourceLocation9
        self.astm_SourceLocation = astm_SourceLocation
        
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
    def astm_SourceLocation9(self):
        return self.__astm_SourceLocation9

    @astm_SourceLocation9.setter
    def astm_SourceLocation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_SourceLocation__astm_SourceLocation9", None)
        self.__astm_SourceLocation9 = value
        
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

    def __init__(self, pathName: str, astm_SourceFile: "astm_SourceLocation" = None, astm_SourceFile76: "astm_IncludeUnit" = None):
        self.pathName = pathName
        self.astm_SourceFile = astm_SourceFile
        self.astm_SourceFile76 = astm_SourceFile76
        
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
    def astm_SourceFile76(self):
        return self.__astm_SourceFile76

    @astm_SourceFile76.setter
    def astm_SourceFile76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_SourceFile__astm_SourceFile76", None)
        self.__astm_SourceFile76 = value
        
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

class Visitable:

    pass
class astm_AccessKind(Visitable):

    pass
class astm_StorageSpecification(Visitable):

    pass
class astm_GASTMSemanticObject(Visitable):

    pass
class astm_RDBHostVariableReference(Visitable):

    pass
class astm_ActualParameter(Visitable):

    pass
class astm_RDBTableSpaceReference(Visitable):

    pass
class astm_UnaryOperator(Visitable):

    pass
class astm_BinaryOperator(Visitable):

    pass
class astm_DataType(Visitable):

    pass
class astm_GASTMSourceObject(Visitable):

    pass
class astm_OtherSyntaxObject(Visitable):

    pass
class astm_FunctionMemberAttributes(Visitable):

    def __init__(self, isFriend: bool, isInline: bool, isThisConst: bool, astm_FunctionMemberAttributes45: "astm_FunctionDefinition" = None, astm_FunctionMemberAttributes: "astm_FunctionDeclaration" = None, astm_FunctionMemberAttributes49: "astm_VirtualSpecification" = None):
        self.isFriend = isFriend
        self.isInline = isInline
        self.isThisConst = isThisConst
        self.astm_FunctionMemberAttributes45 = astm_FunctionMemberAttributes45
        self.astm_FunctionMemberAttributes = astm_FunctionMemberAttributes
        self.astm_FunctionMemberAttributes49 = astm_FunctionMemberAttributes49
        
    @property
    def isThisConst(self) -> bool:
        return self.__isThisConst

    @isThisConst.setter
    def isThisConst(self, isThisConst: bool):
        self.__isThisConst = isThisConst

    @property
    def isInline(self) -> bool:
        return self.__isInline

    @isInline.setter
    def isInline(self, isInline: bool):
        self.__isInline = isInline

    @property
    def isFriend(self) -> bool:
        return self.__isFriend

    @isFriend.setter
    def isFriend(self, isFriend: bool):
        self.__isFriend = isFriend

    @property
    def astm_FunctionMemberAttributes49(self):
        return self.__astm_FunctionMemberAttributes49

    @astm_FunctionMemberAttributes49.setter
    def astm_FunctionMemberAttributes49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_FunctionMemberAttributes__astm_FunctionMemberAttributes49", None)
        self.__astm_FunctionMemberAttributes49 = value
        
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
            if hasattr(old_value, "astm_FunctionDeclaration36"):
                opp_val = getattr(old_value, "astm_FunctionDeclaration36", None)
                if opp_val == self:
                    setattr(old_value, "astm_FunctionDeclaration36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_FunctionDeclaration36"):
                opp_val = getattr(value, "astm_FunctionDeclaration36", None)
                setattr(value, "astm_FunctionDeclaration36", self)

    @property
    def astm_FunctionMemberAttributes45(self):
        return self.__astm_FunctionMemberAttributes45

    @astm_FunctionMemberAttributes45.setter
    def astm_FunctionMemberAttributes45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_FunctionMemberAttributes__astm_FunctionMemberAttributes45", None)
        self.__astm_FunctionMemberAttributes45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "astm_FunctionDefinition44"):
                opp_val = getattr(old_value, "astm_FunctionDefinition44", None)
                if opp_val == self:
                    setattr(old_value, "astm_FunctionDefinition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "astm_FunctionDefinition44"):
                opp_val = getattr(value, "astm_FunctionDefinition44", None)
                setattr(value, "astm_FunctionDefinition44", self)

class astm_GASTMObject(Visitable):

    pass