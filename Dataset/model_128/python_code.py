from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RDBHostVariableReference:

    pass
class RDBCursorStatement:

    pass
class sastm_RDBFetchCursorStatement(RDBCursorStatement):

    pass
class sastm_RDBCloseCursorStatement(RDBCursorStatement):

    pass
class sastm_RDBOpenCursorStatement(RDBCursorStatement):

    pass
class RDBModifyStatement:

    pass
class sastm_RDBDeleteStatement(RDBModifyStatement):

    pass
class sastm_RDBUpdateStatement(RDBModifyStatement):

    pass
class sastm_RDBHostVariableReference:

    pass
class NamedTypeDefinition:

    pass
class AggregateTypeDefinition:

    pass
class Project:

    pass
class IncludeUnit:

    pass
class RDBConstraint:

    pass
class sastm_RDBRefIntegrity(RDBConstraint):

    pass
class sastm_RDBUniqueKey(RDBConstraint):

    pass
class sastm_RDBCheckConstraint(RDBConstraint):

    def __init__(self, RDBConstraintText: str, RDBConstraintType: str):
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

class ActualParameterExpression:

    pass
class gastm_ByReferenceActualParameterExpression(ActualParameterExpression):

    pass
class gastm_ByValueActualParameterExpression(ActualParameterExpression):

    pass
class NameSpaceDefinition:

    pass
class sastm_RDBTableSpaceReference:

    pass
class RDBTableSpaceReference:

    pass
class UnaryOperator:

    pass
class gastm_Deref(UnaryOperator):

    pass
class gastm_AddressOf(UnaryOperator):

    pass
class gastm_Increment(UnaryOperator):

    pass
class gastm_PostDecrement(UnaryOperator):

    pass
class gastm_Not(UnaryOperator):

    pass
class gastm_Decrement(UnaryOperator):

    pass
class gastm_Negate(UnaryOperator):

    pass
class gastm_PostIncrement(UnaryOperator):

    pass
class gastm_BitNot(UnaryOperator):

    pass
class gastm_UnaryPlus(UnaryOperator):

    pass
class AccessKind:

    pass
class gastm_Private(AccessKind):

    pass
class gastm_Protected(AccessKind):

    pass
class gastm_Public(AccessKind):

    pass
class Literal:

    pass
class gastm_RealLiteral(Literal):

    pass
class gastm_StringLiteral(Literal):

    pass
class gastm_BitLiteral(Literal):

    pass
class gastm_CharLiteral(Literal):

    pass
class gastm_BooleanLiteral(Literal):

    pass
class gastm_IntegerlLiteral(Literal):

    pass
class QualifiedIdentifierReference:

    pass
class gastm_QualifiedOverData(QualifiedIdentifierReference):

    pass
class gastm_QualifiedOverPointer(QualifiedIdentifierReference):

    pass
class ForStatement:

    pass
class gastm_ForCheckAfterStatement(ForStatement):

    pass
class gastm_ForCheckBeforeStatement(ForStatement):

    pass
class PrimitiveType:

    pass
class gastm_Byte(PrimitiveType):

    pass
class gastm_Void(PrimitiveType):

    pass
class StorageSpecification:

    pass
class gastm_PerClassMember(StorageSpecification):

    pass
class gastm_FileLocal(StorageSpecification):

    pass
class gastm_NoDef(StorageSpecification):

    pass
class gastm_FunctionPersistent(StorageSpecification):

    pass
class gastm_External(StorageSpecification):

    pass
class gastm_WideCharacter(PrimitiveType):

    pass
class gastm_Boolean(PrimitiveType):

    pass
class gastm_String(PrimitiveType):

    pass
class gastm_Character(PrimitiveType):

    pass
class gastm_LongDouble(PrimitiveType):

    pass
class gastm_Double(PrimitiveType):

    pass
class gastm_Float(PrimitiveType):

    pass
class gastm_LongInteger(PrimitiveType):

    pass
class gastm_Integer(PrimitiveType):

    pass
class gastm_ShortInteger(PrimitiveType):

    pass
class ActualParameter:

    pass
class gastm_MissingActualParameter(ActualParameter):

    pass
class gastm_ActualParameterExpression(ActualParameter):

    pass
class BinaryOperator:

    pass
class gastm_Or(BinaryOperator):

    pass
class gastm_Greater(BinaryOperator):

    pass
class gastm_BitLeftShift(BinaryOperator):

    pass
class gastm_Equal(BinaryOperator):

    pass
class gastm_Exponent(BinaryOperator):

    pass
class gastm_SpecificIn(BinaryOperator):

    pass
class gastm_BitOr(BinaryOperator):

    pass
class gastm_SpecificGreaterEqual(BinaryOperator):

    pass
class gastm_And(BinaryOperator):

    pass
class gastm_BitAnd(BinaryOperator):

    pass
class gastm_SpecificLessEqual(BinaryOperator):

    pass
class gastm_Divide(BinaryOperator):

    pass
class gastm_NotLess(BinaryOperator):

    pass
class gastm_BitRightShift(BinaryOperator):

    pass
class gastm_Modulus(BinaryOperator):

    pass
class gastm_BitXor(BinaryOperator):

    pass
class gastm_Subtract(BinaryOperator):

    pass
class gastm_Multiply(BinaryOperator):

    pass
class gastm_Less(BinaryOperator):

    pass
class gastm_Add(BinaryOperator):

    pass
class gastm_NotGreater(BinaryOperator):

    pass
class gastm_SpecificConcatString(BinaryOperator):

    pass
class gastm_SpecificLike(BinaryOperator):

    pass
class gastm_Assign(BinaryOperator):

    pass
class gastm_NotEqual(BinaryOperator):

    pass
class gastm_OperatorAssign(BinaryOperator):

    pass
class IdentifierReference:

    pass
class sastm_RDBTableReference(IdentifierReference):

    pass
class sastm_RDBTableAlias(IdentifierReference):

    pass
class sastm_RDBColumnReference(IdentifierReference):

    pass
class NameReference:

    pass
class gastm_IdentifierReference(NameReference):

    pass
class gastm_TypeQualifiedIdentifierReference(NameReference):

    pass
class gastm_QualifiedIdentifierReference(NameReference):

    pass
class CatchBlock:

    pass
class gastm_VariableCatchBlock(CatchBlock):

    pass
class gastm_TypesCatchBlock(CatchBlock):

    pass
class LoopStatement:

    pass
class gastm_DoWhileStatement(LoopStatement):

    pass
class gastm_WhileStatement(LoopStatement):

    pass
class gastm_ForStatement(LoopStatement):

    pass
class BlockScope:

    pass
class LabelDefinition:

    pass
class SwitchCase:

    pass
class gastm_CaseBlock(SwitchCase):

    pass
class gastm_DefaultBlock(SwitchCase):

    pass
class DerivesFrom:

    pass
class LabelAccess:

    pass
class Type:

    pass
class gastm_NameSpaceType(Type):

    pass
class gastm_TypeReference(Type):

    pass
class gastm_LabelType(Type):

    pass
class gastm_FunctionType(Type):

    pass
class Dimension:

    pass
class ConstructedType:

    pass
class gastm_ReferenceType(ConstructedType):

    pass
class gastm_PointerType(ConstructedType):

    pass
class gastm_CollectionType(ConstructedType):

    pass
class gastm_RangeType(ConstructedType):

    pass
class gastm_ArrayType(ConstructedType):

    pass
class AggregateScope:

    pass
class EnumLiteralDefinition:

    pass
class DataType:

    pass
class sastm_RDBTableSpaceType(DataType):

    pass
class sastm_RDBLong(DataType):

    pass
class sastm_RDBNumber(DataType):

    pass
class sastm_RDBReal(DataType):

    pass
class sastm_RDBBlob(DataType):

    pass
class sastm_RDBBoolean(DataType):

    pass
class sastm_RDBUserType(DataType):

    pass
class sastm_RDBFloat(DataType):

    pass
class sastm_RDBBFile(DataType):

    pass
class sastm_RDBClob(DataType):

    pass
class gastm_EnumType(DataType):

    pass
class sastm_RDBDecimal(DataType):

    pass
class sastm_RDBDataBaseType(DataType):

    pass
class sastm_RDBTimestamp(DataType):

    pass
class gastm_AggregateType(DataType):

    pass
class gastm_ConstructedType(DataType):

    pass
class sastm_RDBInt(DataType):

    pass
class sastm_RDBRowid(DataType):

    pass
class sastm_RDBInteger(DataType):

    pass
class sastm_RDBRaw(DataType):

    pass
class sastm_RDBCursorType(DataType):

    pass
class sastm_RDBDate(DataType):

    pass
class sastm_RDBViewType(DataType):

    pass
class gastm_ExceptionType(DataType):

    pass
class sastm_RDBVarchar(DataType):

    pass
class sastm_RDBTableType(DataType):

    pass
class sastm_RDBString(DataType):

    pass
class sastm_RDBNClob(DataType):

    pass
class sastm_RDBChar(DataType):

    pass
class gastm_PrimitiveType(DataType):

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
class gastm_Expression(GASTMSyntaxObject):

    pass
class gastm_Statement(GASTMSyntaxObject):

    pass
class gastm_DefinitionObject(GASTMSyntaxObject):

    pass
class gastm_PreprocessorElement(GASTMSyntaxObject):

    pass
class gastm_Type(GASTMSyntaxObject):

    def __init__(self, isConst: bool, isVolatile: bool):
        self.isConst = isConst
        self.isVolatile = isVolatile
        
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

class gastm_NamedType(DataType):

    pass
class gastm_FormalParameterType(DataType):

    pass
class FormalParameterType:

    pass
class gastm_ByReferenceFormalParameterType(FormalParameterType):

    pass
class gastm_ByValueFormalParameterType(FormalParameterType):

    pass
class NameSpaceType:

    pass
class AggregateType:

    pass
class gastm_ClassType(AggregateType):

    pass
class gastm_UnionType(AggregateType):

    pass
class gastm_StructureType(AggregateType):

    pass
class gastm_AnnotationType(AggregateType):

    pass
class NamedType:

    pass
class TypeDefinition:

    pass
class gastm_AggregateTypeDefinition(TypeDefinition):

    pass
class gastm_NamedTypeDefinition(TypeDefinition):

    pass
class DataDefinition:

    pass
class gastm_FormalParameterDefinition(DataDefinition):

    pass
class gastm_VariableDefinition(DataDefinition):

    pass
class gastm_BitFieldDefinition(DataDefinition):

    pass
class Expression:

    pass
class gastm_FunctionCallExpression(Expression):

    pass
class gastm_LabelAccess(Expression):

    pass
class gastm_CastExpression(Expression):

    pass
class sastm_RDBHostVariableExpression(Expression):

    pass
class gastm_UnaryExpression(Expression):

    pass
class gastm_ArrayAccess(Expression):

    pass
class gastm_NewExpression(Expression):

    pass
class gastm_AnnotationExpression(Expression):

    pass
class gastm_NameReference(Expression):

    pass
class gastm_BinaryExpression(Expression):

    pass
class gastm_Literal(Expression):

    def __init__(self, value: str, Expression296: "sastm_RDBCursorStatement", Expression82: "gastm_Dimension", Expression196: "gastm_UnaryExpression", Expression174: "gastm_ArrayAccess", Expression304: "sastm_RDBHostVariableReference", Expression298: "sastm_RDBOpenCursorStatement", Expression52: "gastm_BitFieldDefinition", Expression219: "gastm_RangeExpression", Expression208: "gastm_ConditionalExpression", Expression139: "gastm_CaseBlock", Expression179: "gastm_QualifiedIdentifierReference", Expression54: "gastm_EnumLiteralDefinition", Expression292: "sastm_RDBModifyStatement", Expression221: "gastm_FunctionCallExpression", Expression133: "gastm_SwitchStatement", Expression110: "gastm_ExpressionStatement", Expression316: "sastm_RDBColumnReference", Expression106: "gastm_DeleteStatement", Expression294: "sastm_RDBUpdateStatement", Expression165: "gastm_ThrowStatement", Expression: "gastm_DataDefinition", Expression85: "gastm_Dimension", Expression211: "gastm_ConditionalExpression", Expression125: "gastm_IfStatement", Expression201: "gastm_BinaryExpression", Expression240: "gastm_AnnotationExpression", Expression148: "gastm_ForStatement", Expression191: "gastm_CastExpression", Expression141: "gastm_ReturnStatement", Expression112: "gastm_JumpStatement", Expression151: "gastm_ForStatement", Expression214: "gastm_ConditionalExpression", Expression204: "gastm_BinaryExpression", Expression287: "sastm_RDBInsertStatement", Expression143: "gastm_LoopStatement", Expression301: "sastm_RDBHostVariableReference", Expression312: "sastm_RDBSelectExpression", Expression216: "gastm_RangeExpression", Expression225: "gastm_ActualParameterExpression", Expression177: "gastm_ArrayAccess"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sastm_RDBSelectExpression(Expression):

    pass
class gastm_AggregateExpression(Expression):

    pass
class gastm_RangeExpression(Expression):

    pass
class gastm_ConditionalExpression(Expression):

    pass
class MacroDefinition:

    pass
class LabelType:

    pass
class Statement:

    pass
class gastm_ExpressionStatement(Statement):

    pass
class gastm_SwitchStatement(Statement):

    pass
class gastm_ContinueStatement(Statement):

    pass
class sastm_RDBConnectStatement(Statement):

    pass
class gastm_EmptyStatement(Statement):

    pass
class gastm_TerminateStatement(Statement):

    pass
class gastm_BreakStatement(Statement):

    pass
class sastm_RDBInsertStatement(Statement):

    pass
class gastm_BlockStatement(Statement):

    pass
class sastm_RDBSelectStatement(Statement):

    pass
class gastm_DeclarationOrDefinitionStatement(Statement):

    pass
class gastm_IfStatement(Statement):

    pass
class gastm_JumpStatement(Statement):

    pass
class gastm_LoopStatement(Statement):

    pass
class gastm_SpecificSelectStatement(Statement):

    pass
class sastm_RDBCursorStatement(Statement):

    pass
class gastm_ReturnStatement(Statement):

    pass
class gastm_LabeledStatement(Statement):

    pass
class gastm_ThrowStatement(Statement):

    pass
class gastm_TryStatement(Statement):

    pass
class sastm_RDBModifyStatement(Statement):

    pass
class gastm_DeleteStatement(Statement):

    pass
class FormalParameterDefinition:

    pass
class FunctionMemberAttributes:

    pass
class FormalParameterDeclaration:

    pass
class Declaration:

    pass
class gastm_FormalParameterDeclaration(Declaration):

    pass
class gastm_VariableDeclaration(Declaration):

    def __init__(self, isMutable: bool):
        self.isMutable = isMutable
        
    @property
    def isMutable(self) -> bool:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable

class gastm_FunctionDeclaration(Declaration):

    pass
class Definition:

    pass
class gastm_SpecificTriggerDefinition(Definition):

    pass
class sastm_RDBCursorDefinition(Definition):

    pass
class gastm_EntryDefinition(Definition):

    pass
class gastm_FunctionDefinition(Definition):

    pass
class gastm_DataDefinition(Definition):

    def __init__(self, isMutable: bool, gastm_DataDefinition: "Expression" = None, Definition: "gastm_Declaration"):
        self.isMutable = isMutable
        self.gastm_DataDefinition = gastm_DataDefinition
        
    @property
    def isMutable(self) -> bool:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable

    @property
    def gastm_DataDefinition(self):
        return self.__gastm_DataDefinition

    @gastm_DataDefinition.setter
    def gastm_DataDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_DataDefinition__gastm_DataDefinition", None)
        self.__gastm_DataDefinition = value
        
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

class sastm_RDBDatabaseDefinition(Definition):

    pass
class sastm_RDBColumnDefinition(Definition):

    def __init__(self, NotNull: bool, Definition: "gastm_Declaration"):
        self.NotNull = NotNull
        
    @property
    def NotNull(self) -> bool:
        return self.__NotNull

    @NotNull.setter
    def NotNull(self, NotNull: bool):
        self.__NotNull = NotNull

class sastm_RDBTableDefinition(Definition):

    pass
class sastm_RDBTableSpaceDefinition(Definition):

    pass
class gastm_EnumLiteralDefinition(Definition):

    pass
class sastm_RDBViewDefinition(Definition):

    pass
class sastm_RDBUserDefinition(Definition):

    pass
class VirtualSpecification:

    pass
class gastm_NonVirtual(VirtualSpecification):

    pass
class gastm_PureVirtual(VirtualSpecification):

    pass
class gastm_Virtual(VirtualSpecification):

    pass
class gastm_FunctionMemberAttributes:

    def __init__(self, isFriend: bool, isInline: bool, isThisConst: bool, gastm_FunctionMemberAttributes: "VirtualSpecification" = None):
        self.isFriend = isFriend
        self.isInline = isInline
        self.isThisConst = isThisConst
        self.gastm_FunctionMemberAttributes = gastm_FunctionMemberAttributes
        
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
    def gastm_FunctionMemberAttributes(self):
        return self.__gastm_FunctionMemberAttributes

    @gastm_FunctionMemberAttributes.setter
    def gastm_FunctionMemberAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_FunctionMemberAttributes__gastm_FunctionMemberAttributes", None)
        self.__gastm_FunctionMemberAttributes = value
        
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
class ProgramScope:

    pass
class OtherSyntaxObject:

    pass
class sastm_RDBIndex(OtherSyntaxObject):

    def __init__(self, NotNull: bool, IsUnique: bool, sastm_RDBIndex: set["Name"] = None, OtherSyntaxObject198: "gastm_BinaryExpression", OtherSyntaxObject: "gastm_DeclarationOrDefinition", OtherSyntaxObject230: "gastm_NewExpression", OtherSyntaxObject19: "gastm_DeclarationOrDefinition", OtherSyntaxObject193: "gastm_UnaryExpression", OtherSyntaxObject95: "gastm_DerivesFrom", OtherSyntaxObject206: "gastm_OperatorAssign"):
        self.NotNull = NotNull
        self.IsUnique = IsUnique
        self.sastm_RDBIndex = sastm_RDBIndex if sastm_RDBIndex is not None else set()
        
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
    def sastm_RDBIndex(self):
        return self.__sastm_RDBIndex

    @sastm_RDBIndex.setter
    def sastm_RDBIndex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sastm_RDBIndex__sastm_RDBIndex", None)
        self.__sastm_RDBIndex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Name261"):
                    opp_val = getattr(item, "Name261", None)
                    
                    if opp_val == self:
                        setattr(item, "Name261", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Name261"):
                    opp_val = getattr(item, "Name261", None)
                    
                    setattr(item, "Name261", self)
                    

class gastm_Name(OtherSyntaxObject):

    def __init__(self, nameString: str, OtherSyntaxObject198: "gastm_BinaryExpression", OtherSyntaxObject: "gastm_DeclarationOrDefinition", OtherSyntaxObject230: "gastm_NewExpression", OtherSyntaxObject19: "gastm_DeclarationOrDefinition", OtherSyntaxObject193: "gastm_UnaryExpression", OtherSyntaxObject95: "gastm_DerivesFrom", OtherSyntaxObject206: "gastm_OperatorAssign"):
        self.nameString = nameString
        
    @property
    def nameString(self) -> str:
        return self.__nameString

    @nameString.setter
    def nameString(self, nameString: str):
        self.__nameString = nameString

class sastm_RDBConstraint(OtherSyntaxObject):

    pass
class gastm_Dimension(OtherSyntaxObject):

    pass
class gastm_DerivesFrom(OtherSyntaxObject):

    def __init__(self, isVirtual: bool, gastm_DerivesFrom: "OtherSyntaxObject" = None, gastm_DerivesFrom97: "NamedType" = None, OtherSyntaxObject198: "gastm_BinaryExpression", OtherSyntaxObject: "gastm_DeclarationOrDefinition", OtherSyntaxObject230: "gastm_NewExpression", OtherSyntaxObject19: "gastm_DeclarationOrDefinition", OtherSyntaxObject193: "gastm_UnaryExpression", OtherSyntaxObject95: "gastm_DerivesFrom", OtherSyntaxObject206: "gastm_OperatorAssign"):
        self.isVirtual = isVirtual
        self.gastm_DerivesFrom = gastm_DerivesFrom
        self.gastm_DerivesFrom97 = gastm_DerivesFrom97
        
    @property
    def isVirtual(self) -> bool:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual

    @property
    def gastm_DerivesFrom97(self):
        return self.__gastm_DerivesFrom97

    @gastm_DerivesFrom97.setter
    def gastm_DerivesFrom97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_DerivesFrom__gastm_DerivesFrom97", None)
        self.__gastm_DerivesFrom97 = value
        
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

    @property
    def gastm_DerivesFrom(self):
        return self.__gastm_DerivesFrom

    @gastm_DerivesFrom.setter
    def gastm_DerivesFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_DerivesFrom__gastm_DerivesFrom", None)
        self.__gastm_DerivesFrom = value
        
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

class gastm_FunctionMemberAttribute(OtherSyntaxObject):

    pass
class sastm_RDBTrigger(OtherSyntaxObject):

    pass
class gastm_CatchBlock(OtherSyntaxObject):

    pass
class gastm_VirtualSpecification(OtherSyntaxObject):

    pass
class sastm_RDBIndexColumn(OtherSyntaxObject):

    def __init__(self, AscendingOrDescending: str, sastm_RDBIndexColumn: "IncludeUnit" = None, OtherSyntaxObject198: "gastm_BinaryExpression", OtherSyntaxObject: "gastm_DeclarationOrDefinition", OtherSyntaxObject230: "gastm_NewExpression", OtherSyntaxObject19: "gastm_DeclarationOrDefinition", OtherSyntaxObject193: "gastm_UnaryExpression", OtherSyntaxObject95: "gastm_DerivesFrom", OtherSyntaxObject206: "gastm_OperatorAssign"):
        self.AscendingOrDescending = AscendingOrDescending
        self.sastm_RDBIndexColumn = sastm_RDBIndexColumn
        
    @property
    def AscendingOrDescending(self) -> str:
        return self.__AscendingOrDescending

    @AscendingOrDescending.setter
    def AscendingOrDescending(self, AscendingOrDescending: str):
        self.__AscendingOrDescending = AscendingOrDescending

    @property
    def sastm_RDBIndexColumn(self):
        return self.__sastm_RDBIndexColumn

    @sastm_RDBIndexColumn.setter
    def sastm_RDBIndexColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sastm_RDBIndexColumn__sastm_RDBIndexColumn", None)
        self.__sastm_RDBIndexColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IncludeUnit263"):
                opp_val = getattr(old_value, "IncludeUnit263", None)
                if opp_val == self:
                    setattr(old_value, "IncludeUnit263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IncludeUnit263"):
                opp_val = getattr(value, "IncludeUnit263", None)
                setattr(value, "IncludeUnit263", self)

class gastm_SwitchCase(OtherSyntaxObject):

    pass
class gastm_CompilationUnit(OtherSyntaxObject):

    def __init__(self, language: str, gastm_CompilationUnit: set["DefinitionObject"] = None, gastm_CompilationUnit15: "ProgramScope" = None, OtherSyntaxObject198: "gastm_BinaryExpression", OtherSyntaxObject: "gastm_DeclarationOrDefinition", OtherSyntaxObject230: "gastm_NewExpression", OtherSyntaxObject19: "gastm_DeclarationOrDefinition", OtherSyntaxObject193: "gastm_UnaryExpression", OtherSyntaxObject95: "gastm_DerivesFrom", OtherSyntaxObject206: "gastm_OperatorAssign"):
        self.language = language
        self.gastm_CompilationUnit = gastm_CompilationUnit if gastm_CompilationUnit is not None else set()
        self.gastm_CompilationUnit15 = gastm_CompilationUnit15
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def gastm_CompilationUnit15(self):
        return self.__gastm_CompilationUnit15

    @gastm_CompilationUnit15.setter
    def gastm_CompilationUnit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_CompilationUnit__gastm_CompilationUnit15", None)
        self.__gastm_CompilationUnit15 = value
        
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
    def gastm_CompilationUnit(self):
        return self.__gastm_CompilationUnit

    @gastm_CompilationUnit.setter
    def gastm_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_CompilationUnit__gastm_CompilationUnit", None)
        self.__gastm_CompilationUnit = value if value is not None else set()
        
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
                    

class AnnotationExpression:

    pass
class PreprocessorElement:

    pass
class gastm_MacroDefinition(PreprocessorElement):

    def __init__(self, macroName: str, body: str, PreprocessorElement: "gastm_GASTMSyntaxObject"):
        self.macroName = macroName
        self.body = body
        
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

class gastm_IncludeUnit(PreprocessorElement):

    pass
class gastm_MacroCall(PreprocessorElement):

    pass
class gastm_Comment(PreprocessorElement):

    def __init__(self, text: str, PreprocessorElement: "gastm_GASTMSyntaxObject"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class SourceLocation:

    pass
class GASTMObject:

    pass
class gastm_GASTMSyntaxObject(GASTMObject):

    pass
class Scope:

    pass
class gastm_ProgramScope(Scope):

    pass
class gastm_FunctionScope(Scope):

    pass
class gastm_AggregateScope(Scope):

    pass
class gastm_GlobalScope(Scope):

    pass
class gastm_BlockScope(Scope):

    pass
class DefinitionObject:

    pass
class gastm_DeclarationOrDefinition(DefinitionObject):

    def __init__(self, isRegister: bool, linkageSpecifier: str, gastm_DeclarationOrDefinition: "OtherSyntaxObject" = None, gastm_DeclarationOrDefinition18: "OtherSyntaxObject" = None, DefinitionObject: "gastm_Scope", DefinitionObject13: "gastm_CompilationUnit", DefinitionObject63: "gastm_NameSpaceDefinition", DefinitionObject108: "gastm_DeclarationOrDefinitionStatement", DefinitionObject77: "gastm_AggregateType", DefinitionObject172: "gastm_NameReference"):
        self.isRegister = isRegister
        self.linkageSpecifier = linkageSpecifier
        self.gastm_DeclarationOrDefinition = gastm_DeclarationOrDefinition
        self.gastm_DeclarationOrDefinition18 = gastm_DeclarationOrDefinition18
        
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
    def gastm_DeclarationOrDefinition(self):
        return self.__gastm_DeclarationOrDefinition

    @gastm_DeclarationOrDefinition.setter
    def gastm_DeclarationOrDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_DeclarationOrDefinition__gastm_DeclarationOrDefinition", None)
        self.__gastm_DeclarationOrDefinition = value
        
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
    def gastm_DeclarationOrDefinition18(self):
        return self.__gastm_DeclarationOrDefinition18

    @gastm_DeclarationOrDefinition18.setter
    def gastm_DeclarationOrDefinition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_DeclarationOrDefinition__gastm_DeclarationOrDefinition18", None)
        self.__gastm_DeclarationOrDefinition18 = value
        
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

class gastm_TypeDefinition(DefinitionObject):

    pass
class gastm_LabelDefinition(DefinitionObject):

    pass
class gastm_NameSpaceDefinition(DefinitionObject):

    pass
class GlobalScope:

    pass
class CompilationUnit:

    pass
class GASTMSemanticObject:

    pass
class gastm_Scope(GASTMSemanticObject):

    pass
class gastm_Project(GASTMSemanticObject):

    pass
class SourceFile:

    pass
class TypeReference:

    pass
class gastm_NamedTypeReference(TypeReference):

    pass
class gastm_UnnamedTypeReference(TypeReference):

    pass
class Name:

    pass
class DeclarationOrDefinition:

    pass
class gastm_Declaration(DeclarationOrDefinition):

    pass
class gastm_Definition(DeclarationOrDefinition):

    pass
class gastm_GASTMSemanticObject(ABC):

    pass
class gastm_GASTMSourceObject(ABC):

    pass
class gastm_GASTMObject:

    pass
class GASTMSourceObject:

    pass
class gastm_SourceLocation(GASTMSourceObject):

    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int, gastm_SourceLocation: "SourceFile" = None):
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.gastm_SourceLocation = gastm_SourceLocation
        
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
    def startLine(self) -> int:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine

    @property
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

    @property
    def gastm_SourceLocation(self):
        return self.__gastm_SourceLocation

    @gastm_SourceLocation.setter
    def gastm_SourceLocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_SourceLocation__gastm_SourceLocation", None)
        self.__gastm_SourceLocation = value
        
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

class gastm_SourceFile(GASTMSourceObject):

    def __init__(self, pathName: str):
        self.pathName = pathName
        
    @property
    def pathName(self) -> str:
        return self.__pathName

    @pathName.setter
    def pathName(self, pathName: str):
        self.__pathName = pathName

class gastm_ActualParameter(ABC):

    pass
class gastm_BinaryOperator(ABC):

    pass
class gastm_UnaryOperator(ABC):

    pass
class gastm_AccessKind:

    pass
class gastm_DataType(ABC):

    pass
class gastm_StorageSpecification(ABC):

    pass
class gastm_OtherSyntaxObject(ABC):

    pass