from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RDBCursorStatement:

    pass
class astm_sastm_RDBCloseCursorStatement(RDBCursorStatement):

    pass
class astm_sastm_RDBOpenCursorStatement(RDBCursorStatement):

    pass
class astm_sastm_RDBHostVariableReference:

    pass
class astm_sastm_RDBFetchCursorStatement(RDBCursorStatement):

    pass
class RDBModifyStatement:

    pass
class astm_sastm_RDBDeleteStatement(RDBModifyStatement):

    pass
class astm_sastm_RDBUpdateStatement(RDBModifyStatement):

    pass
class RDBTableReference:

    pass
class RDBHostVariableReference:

    pass
class RDBSelectExpression:

    pass
class NamedTypeDefinition:

    pass
class IncludeUnit:

    pass
class gastm_Definition:

    pass
class gastm_OtherSyntaxObject:

    pass
class astm_sastm_RDBTrigger(gastm_OtherSyntaxObject, gastm_Definition):

    pass
class RDBIndex:

    pass
class RDBConstraint:

    pass
class astm_sastm_RDBCheckConstraint(RDBConstraint):

    def __init__(self, RDBConstraintText: str, RDBConstraintType: str, RDBConstraint: "astm_sastm_RDBTableDefinition"):
        self.RDBConstraintText = RDBConstraintText
        self.RDBConstraintType = RDBConstraintType
        
    @property
    def RDBConstraintType(self) -> str:
        return self.__RDBConstraintType

    @RDBConstraintType.setter
    def RDBConstraintType(self, RDBConstraintType: str):
        self.__RDBConstraintType = RDBConstraintType

    @property
    def RDBConstraintText(self) -> str:
        return self.__RDBConstraintText

    @RDBConstraintText.setter
    def RDBConstraintText(self, RDBConstraintText: str):
        self.__RDBConstraintText = RDBConstraintText

class astm_sastm_RDBRefIntegrity(RDBConstraint):

    pass
class astm_sastm_RDBUniqueKey(RDBConstraint):

    pass
class RDBColumnDefinition:

    pass
class AggregateTypeDefinition:

    pass
class RDBColumnType:

    pass
class astm_sastm_RDBBlob(RDBColumnType):

    pass
class astm_sastm_RDBChar(RDBColumnType):

    pass
class astm_sastm_RDBBoolean(RDBColumnType):

    pass
class astm_sastm_RDBFloat(RDBColumnType):

    pass
class astm_sastm_RDBDecimal(RDBColumnType):

    pass
class astm_sastm_RDBTimestamp(RDBColumnType):

    pass
class astm_sastm_RDBReal(RDBColumnType):

    pass
class astm_sastm_RDBInteger(RDBColumnType):

    pass
class astm_sastm_RDBRowid(RDBColumnType):

    pass
class astm_sastm_RDBInt(RDBColumnType):

    pass
class astm_sastm_RDBRaw(RDBColumnType):

    pass
class astm_sastm_RDBDate(RDBColumnType):

    pass
class astm_sastm_RDBVarchar(RDBColumnType):

    pass
class astm_sastm_RDBString(RDBColumnType):

    pass
class astm_sastm_RDBNClob(RDBColumnType):

    pass
class astm_sastm_RDBLong(RDBColumnType):

    pass
class astm_sastm_RDBBFile(RDBColumnType):

    pass
class astm_sastm_RDBClob(RDBColumnType):

    pass
class astm_sastm_RDBNumber(RDBColumnType):

    pass
class RDBTrigger:

    pass
class RDBColumnReference:

    pass
class NameSpaceDefinition:

    pass
class ActualParameterExpression:

    pass
class astm_gastm_ByReferenceActualParameterExpression(ActualParameterExpression):

    pass
class astm_gastm_ByValueActualParameterExpression(ActualParameterExpression):

    pass
class astm_sastm_RDBTableSpaceReference:

    pass
class RDBTableSpaceReference:

    pass
class UnaryOperator:

    pass
class astm_gastm_BitNot(UnaryOperator):

    pass
class astm_gastm_Deref(UnaryOperator):

    pass
class astm_gastm_AddressOf(UnaryOperator):

    pass
class astm_gastm_Increment(UnaryOperator):

    pass
class astm_gastm_Negate(UnaryOperator):

    pass
class astm_gastm_Not(UnaryOperator):

    pass
class astm_gastm_UnaryPlus(UnaryOperator):

    pass
class Literal:

    pass
class astm_gastm_BooleanLiteral(Literal):

    pass
class astm_gastm_CharLiteral(Literal):

    pass
class astm_gastm_RealLiteral(Literal):

    pass
class astm_gastm_StringLiteral(Literal):

    pass
class astm_gastm_BitLiteral(Literal):

    pass
class astm_gastm_IntegerlLiteral(Literal):

    pass
class QualifiedIdentifierReference:

    pass
class astm_gastm_QualifiedOverData(QualifiedIdentifierReference):

    pass
class astm_gastm_QualifiedOverPointer(QualifiedIdentifierReference):

    pass
class astm_gastm_PostDecrement(UnaryOperator):

    pass
class astm_gastm_PostIncrement(UnaryOperator):

    pass
class astm_gastm_Decrement(UnaryOperator):

    pass
class AccessKind:

    pass
class astm_gastm_Private(AccessKind):

    pass
class astm_gastm_Protected(AccessKind):

    pass
class astm_gastm_Public(AccessKind):

    pass
class ForStatement:

    pass
class astm_gastm_ForCheckAfterStatement(ForStatement):

    pass
class astm_gastm_ForCheckBeforeStatement(ForStatement):

    pass
class PrimitiveType:

    pass
class astm_gastm_LongDouble(PrimitiveType):

    pass
class astm_gastm_Float(PrimitiveType):

    pass
class astm_gastm_Double(PrimitiveType):

    pass
class astm_gastm_Byte(PrimitiveType):

    pass
class astm_gastm_Character(PrimitiveType):

    pass
class astm_gastm_LongInteger(PrimitiveType):

    pass
class astm_gastm_Integer(PrimitiveType):

    pass
class astm_gastm_ShortInteger(PrimitiveType):

    pass
class astm_gastm_Void(PrimitiveType):

    pass
class astm_gastm_WideCharacter(PrimitiveType):

    pass
class astm_gastm_Boolean(PrimitiveType):

    pass
class astm_gastm_String(PrimitiveType):

    pass
class StorageSpecification:

    pass
class astm_gastm_FunctionPersistent(StorageSpecification):

    pass
class astm_gastm_PerClassMember(StorageSpecification):

    pass
class astm_gastm_External(StorageSpecification):

    pass
class astm_gastm_FileLocal(StorageSpecification):

    pass
class astm_gastm_NoDef(StorageSpecification):

    pass
class ActualParameter:

    pass
class astm_gastm_ActualParameterExpression(ActualParameter):

    pass
class astm_gastm_MissingActualParameter(ActualParameter):

    pass
class BinaryOperator:

    pass
class astm_gastm_SpecificLike(BinaryOperator):

    pass
class astm_gastm_Assign(BinaryOperator):

    pass
class astm_gastm_Or(BinaryOperator):

    pass
class astm_gastm_NotEqual(BinaryOperator):

    pass
class astm_gastm_BitLeftShift(BinaryOperator):

    pass
class astm_gastm_Equal(BinaryOperator):

    pass
class astm_gastm_Exponent(BinaryOperator):

    pass
class astm_gastm_SpecificIn(BinaryOperator):

    pass
class astm_gastm_BitOr(BinaryOperator):

    pass
class astm_gastm_SpecificGreaterEqual(BinaryOperator):

    pass
class astm_gastm_And(BinaryOperator):

    pass
class astm_gastm_BitAnd(BinaryOperator):

    pass
class astm_gastm_SpecificLessEqual(BinaryOperator):

    pass
class astm_gastm_NotLess(BinaryOperator):

    pass
class astm_gastm_Divide(BinaryOperator):

    pass
class astm_gastm_BitRightShift(BinaryOperator):

    pass
class astm_gastm_Modulus(BinaryOperator):

    pass
class astm_gastm_BitXor(BinaryOperator):

    pass
class astm_gastm_Subtract(BinaryOperator):

    pass
class astm_gastm_Multiply(BinaryOperator):

    pass
class astm_gastm_Less(BinaryOperator):

    pass
class astm_gastm_Add(BinaryOperator):

    pass
class astm_gastm_NotGreater(BinaryOperator):

    pass
class astm_gastm_SpecificConcatString(BinaryOperator):

    pass
class astm_gastm_Greater(BinaryOperator):

    pass
class astm_gastm_OperatorAssign(BinaryOperator):

    pass
class IdentifierReference:

    pass
class astm_sastm_RDBTableAlias(IdentifierReference):

    pass
class astm_sastm_RDBTableReference(IdentifierReference):

    pass
class astm_sastm_RDBColumnReference(IdentifierReference):

    pass
class NameReference:

    pass
class astm_gastm_TypeQualifiedIdentifierReference(NameReference):

    pass
class astm_gastm_IdentifierReference(NameReference):

    pass
class astm_gastm_QualifiedIdentifierReference(NameReference):

    pass
class CatchBlock:

    pass
class astm_gastm_VariableCatchBlock(CatchBlock):

    pass
class astm_gastm_TypesCatchBlock(CatchBlock):

    pass
class LoopStatement:

    pass
class astm_gastm_DoWhileStatement(LoopStatement):

    pass
class astm_gastm_WhileStatement(LoopStatement):

    pass
class astm_gastm_ForStatement(LoopStatement):

    pass
class BlockScope:

    pass
class SwitchCase:

    pass
class astm_gastm_DefaultBlock(SwitchCase):

    pass
class astm_gastm_CaseBlock(SwitchCase):

    pass
class LabelDefinition:

    pass
class LabelAccess:

    pass
class DerivesFrom:

    pass
class FormalParameterType:

    pass
class astm_gastm_ByReferenceFormalParameterType(FormalParameterType):

    pass
class astm_gastm_ByValueFormalParameterType(FormalParameterType):

    pass
class Type:

    pass
class astm_gastm_NameSpaceType(Type):

    pass
class astm_gastm_TypeReference(Type):

    pass
class astm_gastm_LabelType(Type):

    pass
class astm_gastm_FunctionType(Type):

    pass
class Dimension:

    pass
class ConstructedType:

    pass
class astm_gastm_CollectionType(ConstructedType):

    pass
class astm_gastm_RangeType(ConstructedType):

    pass
class astm_gastm_ReferenceType(ConstructedType):

    pass
class astm_gastm_PointerType(ConstructedType):

    pass
class astm_gastm_ArrayType(ConstructedType):

    pass
class AggregateScope:

    pass
class EnumLiteralDefinition:

    pass
class DataType:

    pass
class astm_gastm_ConstructedType(DataType):

    pass
class astm_gastm_NamedType(DataType):

    pass
class astm_sastm_RDBTableType(DataType):

    pass
class astm_gastm_ExceptionType(DataType):

    pass
class astm_sastm_RDBDataBaseType(DataType):

    pass
class astm_gastm_FormalParameterType(DataType):

    pass
class astm_gastm_AggregateType(DataType):

    pass
class astm_sastm_RDBCursorType(DataType):

    pass
class astm_sastm_RDBViewType(DataType):

    pass
class astm_sastm_RDBTableSpaceType(DataType):

    pass
class astm_gastm_EnumType(DataType):

    pass
class astm_sastm_RDBUserType(DataType):

    pass
class astm_sastm_RDBColumnType(DataType):

    pass
class MacroDefinition:

    pass
class LabelType:

    pass
class astm_gastm_PrimitiveType(DataType):

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
class astm_gastm_Expression(GASTMSyntaxObject):

    pass
class astm_gastm_DefinitionObject(GASTMSyntaxObject):

    pass
class astm_gastm_Statement(GASTMSyntaxObject):

    pass
class astm_gastm_PreprocessorElement(GASTMSyntaxObject):

    pass
class astm_gastm_Type(GASTMSyntaxObject):

    def __init__(self, isConst: bool, isVolatile: bool):
        self.isConst = isConst
        self.isVolatile = isVolatile
        
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

class AggregateType:

    pass
class astm_gastm_AnnotationType(AggregateType):

    pass
class astm_gastm_UnionType(AggregateType):

    pass
class astm_gastm_ClassType(AggregateType):

    pass
class astm_gastm_StructureType(AggregateType):

    pass
class NamedType:

    pass
class TypeDefinition:

    pass
class astm_gastm_AggregateTypeDefinition(TypeDefinition):

    pass
class astm_gastm_NamedTypeDefinition(TypeDefinition):

    pass
class NameSpaceType:

    pass
class VirtualSpecification:

    pass
class astm_gastm_NonVirtual(VirtualSpecification):

    pass
class astm_gastm_PureVirtual(VirtualSpecification):

    pass
class astm_gastm_Virtual(VirtualSpecification):

    pass
class astm_gastm_FunctionMemberAttributes:

    def __init__(self, isFriend: bool, isInline: bool, isThisConst: bool, astm_gastm_FunctionMemberAttributes: "VirtualSpecification" = None):
        self.isFriend = isFriend
        self.isInline = isInline
        self.isThisConst = isThisConst
        self.astm_gastm_FunctionMemberAttributes = astm_gastm_FunctionMemberAttributes
        
    @property
    def isThisConst(self) -> bool:
        return self.__isThisConst

    @isThisConst.setter
    def isThisConst(self, isThisConst: bool):
        self.__isThisConst = isThisConst

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
    def astm_gastm_FunctionMemberAttributes(self):
        return self.__astm_gastm_FunctionMemberAttributes

    @astm_gastm_FunctionMemberAttributes.setter
    def astm_gastm_FunctionMemberAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_FunctionMemberAttributes__astm_gastm_FunctionMemberAttributes", None)
        self.__astm_gastm_FunctionMemberAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VirtualSpecification"):
                opp_val = getattr(old_value, "VirtualSpecification", None)
                if opp_val == self:
                    setattr(old_value, "VirtualSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VirtualSpecification"):
                opp_val = getattr(value, "VirtualSpecification", None)
                setattr(value, "VirtualSpecification", self)

class FunctionScope:

    pass
class DataDefinition:

    pass
class astm_gastm_FormalParameterDefinition(DataDefinition):

    pass
class astm_gastm_VariableDefinition(DataDefinition):

    pass
class astm_gastm_BitFieldDefinition(DataDefinition):

    pass
class Expression:

    pass
class astm_gastm_Literal(Expression):

    def __init__(self, value: str, Expression106: "astm_gastm_DeleteStatement", Expression288: "astm_sastm_RDBInsertStatement", Expression314: "astm_sastm_RDBSelectExpression", Expression110: "astm_gastm_ExpressionStatement", Expression303: "astm_sastm_RDBHostVariableReference", Expression112: "astm_gastm_JumpStatement", Expression208: "astm_gastm_ConditionalExpression", Expression191: "astm_gastm_CastExpression", Expression219: "astm_gastm_RangeExpression", Expression179: "astm_gastm_QualifiedIdentifierReference", Expression177: "astm_gastm_ArrayAccess", Expression297: "astm_sastm_RDBCursorStatement", Expression54: "astm_gastm_EnumLiteralDefinition", Expression: "astm_gastm_DataDefinition", Expression306: "astm_sastm_RDBHostVariableReference", Expression201: "astm_gastm_BinaryExpression", Expression139: "astm_gastm_CaseBlock", Expression82: "astm_gastm_Dimension", Expression299: "astm_sastm_RDBOpenCursorStatement", Expression204: "astm_gastm_BinaryExpression", Expression52: "astm_gastm_BitFieldDefinition", Expression174: "astm_gastm_ArrayAccess", Expression240: "astm_gastm_AnnotationExpression", Expression133: "astm_gastm_SwitchStatement", Expression318: "astm_sastm_RDBColumnReference", Expression293: "astm_sastm_RDBModifyStatement", Expression125: "astm_gastm_IfStatement", Expression165: "astm_gastm_ThrowStatement", Expression143: "astm_gastm_LoopStatement", Expression295: "astm_sastm_RDBUpdateStatement", Expression85: "astm_gastm_Dimension", Expression211: "astm_gastm_ConditionalExpression", Expression225: "astm_gastm_ActualParameterExpression", Expression214: "astm_gastm_ConditionalExpression", Expression148: "astm_gastm_ForStatement", Expression151: "astm_gastm_ForStatement", Expression196: "astm_gastm_UnaryExpression", Expression141: "astm_gastm_ReturnStatement", Expression221: "astm_gastm_FunctionCallExpression", Expression216: "astm_gastm_RangeExpression"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class astm_gastm_RangeExpression(Expression):

    pass
class astm_gastm_BinaryExpression(Expression):

    pass
class astm_gastm_AggregateExpression(Expression):

    pass
class astm_gastm_UnaryExpression(Expression):

    pass
class astm_gastm_FunctionCallExpression(Expression):

    pass
class astm_gastm_CastExpression(Expression):

    pass
class astm_sastm_RDBSelectExpression(Expression):

    pass
class astm_gastm_ArrayAccess(Expression):

    pass
class astm_gastm_ConditionalExpression(Expression):

    pass
class astm_gastm_NewExpression(Expression):

    pass
class astm_gastm_AnnotationExpression(Expression):

    pass
class astm_sastm_RDBHostVariableExpression(Expression):

    pass
class astm_gastm_LabelAccess(Expression):

    pass
class astm_gastm_NameReference(Expression):

    pass
class FunctionMemberAttributes:

    pass
class FormalParameterDeclaration:

    pass
class Declaration:

    pass
class astm_gastm_FormalParameterDeclaration(Declaration):

    pass
class astm_gastm_VariableDeclaration(Declaration):

    def __init__(self, isMutable: bool):
        self.isMutable = isMutable
        
    @property
    def isMutable(self) -> bool:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable

class astm_gastm_FunctionDeclaration(Declaration):

    pass
class Definition:

    pass
class astm_sastm_RDBUserDefinition(Definition):

    pass
class astm_gastm_EntryDefinition(Definition):

    pass
class astm_sastm_RDBColumnDefinition(Definition):

    def __init__(self, NotNull: bool, astm_sastm_RDBColumnDefinition: "Name" = None, astm_sastm_RDBColumnDefinition259: "RDBColumnType" = None, Definition: "astm_gastm_Declaration"):
        self.NotNull = NotNull
        self.astm_sastm_RDBColumnDefinition = astm_sastm_RDBColumnDefinition
        self.astm_sastm_RDBColumnDefinition259 = astm_sastm_RDBColumnDefinition259
        
    @property
    def NotNull(self) -> bool:
        return self.__NotNull

    @NotNull.setter
    def NotNull(self, NotNull: bool):
        self.__NotNull = NotNull

    @property
    def astm_sastm_RDBColumnDefinition(self):
        return self.__astm_sastm_RDBColumnDefinition

    @astm_sastm_RDBColumnDefinition.setter
    def astm_sastm_RDBColumnDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_sastm_RDBColumnDefinition__astm_sastm_RDBColumnDefinition", None)
        self.__astm_sastm_RDBColumnDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Name257"):
                opp_val = getattr(old_value, "Name257", None)
                if opp_val == self:
                    setattr(old_value, "Name257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Name257"):
                opp_val = getattr(value, "Name257", None)
                setattr(value, "Name257", self)

    @property
    def astm_sastm_RDBColumnDefinition259(self):
        return self.__astm_sastm_RDBColumnDefinition259

    @astm_sastm_RDBColumnDefinition259.setter
    def astm_sastm_RDBColumnDefinition259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_sastm_RDBColumnDefinition__astm_sastm_RDBColumnDefinition259", None)
        self.__astm_sastm_RDBColumnDefinition259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RDBColumnType"):
                opp_val = getattr(old_value, "RDBColumnType", None)
                if opp_val == self:
                    setattr(old_value, "RDBColumnType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RDBColumnType"):
                opp_val = getattr(value, "RDBColumnType", None)
                setattr(value, "RDBColumnType", self)

class astm_gastm_FunctionDefinition(Definition):

    pass
class astm_gastm_SpecificTriggerDefinition(Definition):

    pass
class astm_sastm_RDBViewDefinition(Definition):

    pass
class astm_gastm_EnumLiteralDefinition(Definition):

    pass
class astm_sastm_RDBCursorDefinition(Definition):

    pass
class astm_sastm_RDBDatabaseDefinition(Definition):

    pass
class astm_gastm_DataDefinition(Definition):

    def __init__(self, isMutable: bool, astm_gastm_DataDefinition: "Expression" = None, Definition: "astm_gastm_Declaration"):
        self.isMutable = isMutable
        self.astm_gastm_DataDefinition = astm_gastm_DataDefinition
        
    @property
    def isMutable(self) -> bool:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable

    @property
    def astm_gastm_DataDefinition(self):
        return self.__astm_gastm_DataDefinition

    @astm_gastm_DataDefinition.setter
    def astm_gastm_DataDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_DataDefinition__astm_gastm_DataDefinition", None)
        self.__astm_gastm_DataDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression"):
                opp_val = getattr(old_value, "Expression", None)
                if opp_val == self:
                    setattr(old_value, "Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression"):
                opp_val = getattr(value, "Expression", None)
                setattr(value, "Expression", self)

class astm_sastm_RDBTableDefinition(Definition):

    pass
class astm_sastm_RDBTableSpaceDefinition(Definition):

    pass
class Statement:

    pass
class astm_gastm_LabeledStatement(Statement):

    pass
class astm_gastm_LoopStatement(Statement):

    pass
class astm_gastm_BlockStatement(Statement):

    pass
class astm_gastm_BreakStatement(Statement):

    pass
class astm_sastm_RDBSelectStatement(Statement):

    pass
class astm_sastm_RDBConnectStatement(Statement):

    pass
class astm_gastm_JumpStatement(Statement):

    pass
class astm_gastm_EmptyStatement(Statement):

    pass
class astm_gastm_ReturnStatement(Statement):

    pass
class astm_sastm_RDBInsertStatement(Statement):

    pass
class astm_gastm_TerminateStatement(Statement):

    pass
class astm_gastm_DeclarationOrDefinitionStatement(Statement):

    pass
class astm_gastm_TryStatement(Statement):

    pass
class astm_gastm_SwitchStatement(Statement):

    pass
class astm_gastm_DeleteStatement(Statement):

    pass
class astm_gastm_ContinueStatement(Statement):

    pass
class astm_sastm_RDBCursorStatement(Statement):

    pass
class astm_gastm_ThrowStatement(Statement):

    pass
class astm_gastm_SpecificSelectStatement(Statement):

    pass
class astm_gastm_ExpressionStatement(Statement):

    pass
class astm_sastm_RDBModifyStatement(Statement):

    pass
class astm_gastm_IfStatement(Statement):

    pass
class FormalParameterDefinition:

    pass
class ProgramScope:

    pass
class OtherSyntaxObject:

    pass
class astm_gastm_VirtualSpecification(OtherSyntaxObject):

    pass
class astm_gastm_CatchBlock(OtherSyntaxObject):

    pass
class astm_gastm_SwitchCase(OtherSyntaxObject):

    pass
class astm_gastm_Name(OtherSyntaxObject):

    def __init__(self, nameString: str, OtherSyntaxObject198: "astm_gastm_BinaryExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject95: "astm_gastm_DerivesFrom", OtherSyntaxObject193: "astm_gastm_UnaryExpression", OtherSyntaxObject230: "astm_gastm_NewExpression", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject206: "astm_gastm_OperatorAssign"):
        self.nameString = nameString
        
    @property
    def nameString(self) -> str:
        return self.__nameString

    @nameString.setter
    def nameString(self, nameString: str):
        self.__nameString = nameString

class astm_sastm_RDBIndexColumn(OtherSyntaxObject):

    def __init__(self, AscendingOrDescending: str, astm_sastm_RDBIndexColumn: "IncludeUnit" = None, OtherSyntaxObject198: "astm_gastm_BinaryExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject95: "astm_gastm_DerivesFrom", OtherSyntaxObject193: "astm_gastm_UnaryExpression", OtherSyntaxObject230: "astm_gastm_NewExpression", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject206: "astm_gastm_OperatorAssign"):
        self.AscendingOrDescending = AscendingOrDescending
        self.astm_sastm_RDBIndexColumn = astm_sastm_RDBIndexColumn
        
    @property
    def AscendingOrDescending(self) -> str:
        return self.__AscendingOrDescending

    @AscendingOrDescending.setter
    def AscendingOrDescending(self, AscendingOrDescending: str):
        self.__AscendingOrDescending = AscendingOrDescending

    @property
    def astm_sastm_RDBIndexColumn(self):
        return self.__astm_sastm_RDBIndexColumn

    @astm_sastm_RDBIndexColumn.setter
    def astm_sastm_RDBIndexColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_sastm_RDBIndexColumn__astm_sastm_RDBIndexColumn", None)
        self.__astm_sastm_RDBIndexColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IncludeUnit"):
                opp_val = getattr(old_value, "IncludeUnit", None)
                if opp_val == self:
                    setattr(old_value, "IncludeUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IncludeUnit"):
                opp_val = getattr(value, "IncludeUnit", None)
                setattr(value, "IncludeUnit", self)

class astm_sastm_RDBConstraint(OtherSyntaxObject):

    pass
class astm_gastm_DerivesFrom(OtherSyntaxObject):

    def __init__(self, isVirtual: bool, astm_gastm_DerivesFrom: "OtherSyntaxObject" = None, astm_gastm_DerivesFrom97: "NamedType" = None, OtherSyntaxObject198: "astm_gastm_BinaryExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject95: "astm_gastm_DerivesFrom", OtherSyntaxObject193: "astm_gastm_UnaryExpression", OtherSyntaxObject230: "astm_gastm_NewExpression", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject206: "astm_gastm_OperatorAssign"):
        self.isVirtual = isVirtual
        self.astm_gastm_DerivesFrom = astm_gastm_DerivesFrom
        self.astm_gastm_DerivesFrom97 = astm_gastm_DerivesFrom97
        
    @property
    def isVirtual(self) -> bool:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual

    @property
    def astm_gastm_DerivesFrom(self):
        return self.__astm_gastm_DerivesFrom

    @astm_gastm_DerivesFrom.setter
    def astm_gastm_DerivesFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_DerivesFrom__astm_gastm_DerivesFrom", None)
        self.__astm_gastm_DerivesFrom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OtherSyntaxObject95"):
                opp_val = getattr(old_value, "OtherSyntaxObject95", None)
                if opp_val == self:
                    setattr(old_value, "OtherSyntaxObject95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OtherSyntaxObject95"):
                opp_val = getattr(value, "OtherSyntaxObject95", None)
                setattr(value, "OtherSyntaxObject95", self)

    @property
    def astm_gastm_DerivesFrom97(self):
        return self.__astm_gastm_DerivesFrom97

    @astm_gastm_DerivesFrom97.setter
    def astm_gastm_DerivesFrom97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_DerivesFrom__astm_gastm_DerivesFrom97", None)
        self.__astm_gastm_DerivesFrom97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedType98"):
                opp_val = getattr(old_value, "NamedType98", None)
                if opp_val == self:
                    setattr(old_value, "NamedType98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedType98"):
                opp_val = getattr(value, "NamedType98", None)
                setattr(value, "NamedType98", self)

class astm_gastm_Dimension(OtherSyntaxObject):

    pass
class astm_sastm_RDBIndex(OtherSyntaxObject):

    def __init__(self, NotNull: bool, IsUnique: bool, astm_sastm_RDBIndex: set["Name"] = None, OtherSyntaxObject198: "astm_gastm_BinaryExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject95: "astm_gastm_DerivesFrom", OtherSyntaxObject193: "astm_gastm_UnaryExpression", OtherSyntaxObject230: "astm_gastm_NewExpression", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject206: "astm_gastm_OperatorAssign"):
        self.NotNull = NotNull
        self.IsUnique = IsUnique
        self.astm_sastm_RDBIndex = astm_sastm_RDBIndex if astm_sastm_RDBIndex is not None else set()
        
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
    def astm_sastm_RDBIndex(self):
        return self.__astm_sastm_RDBIndex

    @astm_sastm_RDBIndex.setter
    def astm_sastm_RDBIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_sastm_RDBIndex__astm_sastm_RDBIndex", None)
        self.__astm_sastm_RDBIndex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Name264"):
                    opp_val = getattr(item, "Name264", None)
                    
                    if opp_val == self:
                        setattr(item, "Name264", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Name264"):
                    opp_val = getattr(item, "Name264", None)
                    
                    setattr(item, "Name264", self)
                    

class astm_gastm_FunctionMemberAttribute(OtherSyntaxObject):

    pass
class astm_gastm_CompilationUnit(OtherSyntaxObject):

    def __init__(self, language: str, astm_gastm_CompilationUnit: set["DefinitionObject"] = None, astm_gastm_CompilationUnit15: "ProgramScope" = None, OtherSyntaxObject198: "astm_gastm_BinaryExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject95: "astm_gastm_DerivesFrom", OtherSyntaxObject193: "astm_gastm_UnaryExpression", OtherSyntaxObject230: "astm_gastm_NewExpression", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject206: "astm_gastm_OperatorAssign"):
        self.language = language
        self.astm_gastm_CompilationUnit = astm_gastm_CompilationUnit if astm_gastm_CompilationUnit is not None else set()
        self.astm_gastm_CompilationUnit15 = astm_gastm_CompilationUnit15
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def astm_gastm_CompilationUnit15(self):
        return self.__astm_gastm_CompilationUnit15

    @astm_gastm_CompilationUnit15.setter
    def astm_gastm_CompilationUnit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_CompilationUnit__astm_gastm_CompilationUnit15", None)
        self.__astm_gastm_CompilationUnit15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProgramScope"):
                opp_val = getattr(old_value, "ProgramScope", None)
                if opp_val == self:
                    setattr(old_value, "ProgramScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProgramScope"):
                opp_val = getattr(value, "ProgramScope", None)
                setattr(value, "ProgramScope", self)

    @property
    def astm_gastm_CompilationUnit(self):
        return self.__astm_gastm_CompilationUnit

    @astm_gastm_CompilationUnit.setter
    def astm_gastm_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_CompilationUnit__astm_gastm_CompilationUnit", None)
        self.__astm_gastm_CompilationUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DefinitionObject13"):
                    opp_val = getattr(item, "DefinitionObject13", None)
                    
                    if opp_val == self:
                        setattr(item, "DefinitionObject13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DefinitionObject13"):
                    opp_val = getattr(item, "DefinitionObject13", None)
                    
                    setattr(item, "DefinitionObject13", self)
                    

class TypeReference:

    pass
class astm_gastm_UnnamedTypeReference(TypeReference):

    pass
class astm_gastm_NamedTypeReference(TypeReference):

    pass
class Name:

    pass
class DeclarationOrDefinition:

    pass
class astm_gastm_Declaration(DeclarationOrDefinition):

    pass
class astm_gastm_Definition(DeclarationOrDefinition):

    pass
class GASTMObject:

    pass
class astm_gastm_GASTMSyntaxObject(GASTMObject):

    pass
class Scope:

    pass
class astm_gastm_BlockScope(Scope):

    pass
class astm_gastm_ProgramScope(Scope):

    pass
class astm_gastm_AggregateScope(Scope):

    pass
class astm_gastm_FunctionScope(Scope):

    pass
class astm_gastm_GlobalScope(Scope):

    pass
class DefinitionObject:

    pass
class astm_gastm_LabelDefinition(DefinitionObject):

    pass
class astm_gastm_NameSpaceDefinition(DefinitionObject):

    pass
class astm_gastm_DeclarationOrDefinition(DefinitionObject):

    def __init__(self, isRegister: bool, linkageSpecifier: str, astm_gastm_DeclarationOrDefinition: "OtherSyntaxObject" = None, astm_gastm_DeclarationOrDefinition18: "OtherSyntaxObject" = None, DefinitionObject63: "astm_gastm_NameSpaceDefinition", DefinitionObject172: "astm_gastm_NameReference", DefinitionObject: "astm_gastm_Scope", DefinitionObject77: "astm_gastm_AggregateType", DefinitionObject13: "astm_gastm_CompilationUnit", DefinitionObject108: "astm_gastm_DeclarationOrDefinitionStatement"):
        self.isRegister = isRegister
        self.linkageSpecifier = linkageSpecifier
        self.astm_gastm_DeclarationOrDefinition = astm_gastm_DeclarationOrDefinition
        self.astm_gastm_DeclarationOrDefinition18 = astm_gastm_DeclarationOrDefinition18
        
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
    def astm_gastm_DeclarationOrDefinition(self):
        return self.__astm_gastm_DeclarationOrDefinition

    @astm_gastm_DeclarationOrDefinition.setter
    def astm_gastm_DeclarationOrDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_DeclarationOrDefinition__astm_gastm_DeclarationOrDefinition", None)
        self.__astm_gastm_DeclarationOrDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OtherSyntaxObject"):
                opp_val = getattr(old_value, "OtherSyntaxObject", None)
                if opp_val == self:
                    setattr(old_value, "OtherSyntaxObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OtherSyntaxObject"):
                opp_val = getattr(value, "OtherSyntaxObject", None)
                setattr(value, "OtherSyntaxObject", self)

    @property
    def astm_gastm_DeclarationOrDefinition18(self):
        return self.__astm_gastm_DeclarationOrDefinition18

    @astm_gastm_DeclarationOrDefinition18.setter
    def astm_gastm_DeclarationOrDefinition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_DeclarationOrDefinition__astm_gastm_DeclarationOrDefinition18", None)
        self.__astm_gastm_DeclarationOrDefinition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OtherSyntaxObject19"):
                opp_val = getattr(old_value, "OtherSyntaxObject19", None)
                if opp_val == self:
                    setattr(old_value, "OtherSyntaxObject19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OtherSyntaxObject19"):
                opp_val = getattr(value, "OtherSyntaxObject19", None)
                setattr(value, "OtherSyntaxObject19", self)

class astm_gastm_TypeDefinition(DefinitionObject):

    pass
class GlobalScope:

    pass
class CompilationUnit:

    pass
class GASTMSemanticObject:

    pass
class astm_gastm_Scope(GASTMSemanticObject):

    pass
class astm_gastm_Project(GASTMSemanticObject):

    pass
class SourceFile:

    pass
class AnnotationExpression:

    pass
class PreprocessorElement:

    pass
class astm_gastm_Comment(PreprocessorElement):

    def __init__(self, text: str, PreprocessorElement: "astm_gastm_GASTMSyntaxObject"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class astm_gastm_MacroDefinition(PreprocessorElement):

    def __init__(self, macroName: str, body: str, PreprocessorElement: "astm_gastm_GASTMSyntaxObject"):
        self.macroName = macroName
        self.body = body
        
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

class astm_gastm_MacroCall(PreprocessorElement):

    pass
class astm_gastm_IncludeUnit(PreprocessorElement):

    pass
class SourceLocation:

    pass
class GASTMSourceObject:

    pass
class astm_gastm_SourceFile(GASTMSourceObject):

    def __init__(self, pathName: str):
        self.pathName = pathName
        
    @property
    def pathName(self) -> str:
        return self.__pathName

    @pathName.setter
    def pathName(self, pathName: str):
        self.__pathName = pathName

class astm_gastm_ActualParameter(ABC):

    pass
class astm_gastm_BinaryOperator(ABC):

    pass
class astm_gastm_UnaryOperator(ABC):

    pass
class astm_gastm_AccessKind:

    pass
class astm_gastm_DataType(ABC):

    pass
class astm_gastm_StorageSpecification(ABC):

    pass
class astm_gastm_OtherSyntaxObject(ABC):

    pass
class astm_gastm_GASTMSemanticObject(ABC):

    pass
class astm_gastm_GASTMSourceObject(ABC):

    pass
class astm_gastm_GASTMObject:

    pass
class astm_gastm_SourceLocation(GASTMSourceObject):

    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int, astm_gastm_SourceLocation: "SourceFile" = None):
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.astm_gastm_SourceLocation = astm_gastm_SourceLocation
        
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
    def astm_gastm_SourceLocation(self):
        return self.__astm_gastm_SourceLocation

    @astm_gastm_SourceLocation.setter
    def astm_gastm_SourceLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_SourceLocation__astm_gastm_SourceLocation", None)
        self.__astm_gastm_SourceLocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SourceFile"):
                opp_val = getattr(old_value, "SourceFile", None)
                if opp_val == self:
                    setattr(old_value, "SourceFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceFile"):
                opp_val = getattr(value, "SourceFile", None)
                setattr(value, "SourceFile", self)
