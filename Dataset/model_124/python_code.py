from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FunctionCallExpression:

    pass
class astm_sastm_DelphiFunctionCallExpression(FunctionCallExpression):

    pass
class BlockStatement:

    pass
class astm_sastm_DelphiBlockStatement(BlockStatement):

    pass
class NamedTypeReference:

    pass
class DelphiImplementationSection:

    pass
class DelphiInterfaceSection:

    pass
class astm_sastm_DelphiWithStatement(BlockStatement):

    pass
class ActualParameterExpression:

    pass
class astm_gastm_ByReferenceActualParameterExpression(ActualParameterExpression):

    pass
class astm_gastm_ByValueActualParameterExpression(ActualParameterExpression):

    pass
class UnaryOperator:

    pass
class astm_gastm_Negate(UnaryOperator):

    pass
class astm_gastm_UnaryPlus(UnaryOperator):

    pass
class Literal:

    pass
class astm_gastm_CharLiteral(Literal):

    pass
class astm_gastm_BooleanLiteral(Literal):

    pass
class astm_gastm_StringLiteral(Literal):

    pass
class astm_gastm_RealLiteral(Literal):

    pass
class astm_gastm_BitLiteral(Literal):

    pass
class astm_gastm_IntegerLiteral(Literal):

    pass
class QualifiedIdentifierReference:

    pass
class astm_gastm_QualifiedOverData(QualifiedIdentifierReference):

    pass
class astm_gastm_QualifiedOverPointer(QualifiedIdentifierReference):

    pass
class ForStatement:

    pass
class astm_gastm_ForCheckAfterStatement(ForStatement):

    pass
class astm_gastm_ForCheckBeforeStatement(ForStatement):

    pass
class AccessKind:

    pass
class astm_gastm_Protected(AccessKind):

    pass
class astm_gastm_Private(AccessKind):

    pass
class astm_gastm_Public(AccessKind):

    pass
class astm_gastm_PostDecrement(UnaryOperator):

    pass
class astm_gastm_PostIncrement(UnaryOperator):

    pass
class astm_gastm_Decrement(UnaryOperator):

    pass
class astm_gastm_Increment(UnaryOperator):

    pass
class astm_gastm_Deref(UnaryOperator):

    pass
class astm_gastm_AddressOf(UnaryOperator):

    pass
class astm_gastm_BitNot(UnaryOperator):

    pass
class astm_gastm_Not(UnaryOperator):

    pass
class PrimitiveType:

    pass
class astm_gastm_Integer(PrimitiveType):

    pass
class astm_gastm_Float(PrimitiveType):

    pass
class astm_gastm_String(PrimitiveType):

    pass
class astm_gastm_LongInteger(PrimitiveType):

    pass
class astm_gastm_Character(PrimitiveType):

    pass
class astm_gastm_WideCharacter(PrimitiveType):

    pass
class astm_gastm_ShortInteger(PrimitiveType):

    pass
class astm_gastm_LongDouble(PrimitiveType):

    pass
class astm_gastm_Double(PrimitiveType):

    pass
class astm_gastm_Byte(PrimitiveType):

    pass
class astm_gastm_Boolean(PrimitiveType):

    pass
class astm_gastm_Void(PrimitiveType):

    pass
class StorageSpecification:

    pass
class astm_gastm_FunctionPersistent(StorageSpecification):

    pass
class astm_gastm_NoDef(StorageSpecification):

    pass
class astm_gastm_FileLocal(StorageSpecification):

    pass
class astm_gastm_PerClassMember(StorageSpecification):

    pass
class astm_gastm_External(StorageSpecification):

    pass
class ActualParameter:

    pass
class astm_gastm_MissingActualParameter(ActualParameter):

    pass
class astm_gastm_ActualParameterExpression(ActualParameter):

    pass
class BinaryOperator:

    pass
class astm_gastm_Subtract(BinaryOperator):

    pass
class astm_gastm_Exponent(BinaryOperator):

    pass
class astm_gastm_Greater(BinaryOperator):

    pass
class astm_gastm_Assign(BinaryOperator):

    pass
class astm_gastm_BitLeftShift(BinaryOperator):

    pass
class astm_gastm_Equal(BinaryOperator):

    pass
class astm_gastm_Multiply(BinaryOperator):

    pass
class astm_gastm_SpecificLessEqual(BinaryOperator):

    pass
class astm_gastm_BitXor(BinaryOperator):

    pass
class astm_gastm_NotLess(BinaryOperator):

    pass
class astm_gastm_BitRightShift(BinaryOperator):

    pass
class astm_gastm_SpecificIn(BinaryOperator):

    pass
class astm_gastm_NotGreater(BinaryOperator):

    pass
class astm_gastm_And(BinaryOperator):

    pass
class astm_gastm_BitOr(BinaryOperator):

    pass
class astm_gastm_Modulus(BinaryOperator):

    pass
class astm_gastm_BitAnd(BinaryOperator):

    pass
class astm_gastm_SpecificConcatString(BinaryOperator):

    pass
class astm_gastm_Divide(BinaryOperator):

    pass
class astm_gastm_SpecificLike(BinaryOperator):

    pass
class astm_gastm_Less(BinaryOperator):

    pass
class astm_gastm_NotEqual(BinaryOperator):

    pass
class astm_gastm_Add(BinaryOperator):

    pass
class astm_gastm_Or(BinaryOperator):

    pass
class astm_gastm_SpecificGreaterEqual(BinaryOperator):

    pass
class astm_gastm_OperatorAssign(BinaryOperator):

    pass
class IdentifierReference:

    pass
class NameReference:

    pass
class astm_gastm_IdentifierReference(NameReference):

    pass
class astm_gastm_TypeQualifiedIdentifierReference(NameReference):

    pass
class astm_gastm_QualifiedIdentifierReference(NameReference):

    pass
class LoopStatement:

    pass
class astm_gastm_WhileStatement(LoopStatement):

    pass
class astm_gastm_DoWhileStatement(LoopStatement):

    pass
class astm_gastm_ForStatement(LoopStatement):

    pass
class SwitchCase:

    pass
class astm_gastm_CaseBlock(SwitchCase):

    pass
class astm_gastm_DefaultBlock(SwitchCase):

    pass
class CatchBlock:

    pass
class astm_gastm_VariableCatchBlock(CatchBlock):

    pass
class astm_gastm_TypesCatchBlock(CatchBlock):

    pass
class BlockScope:

    pass
class LabelDefinition:

    pass
class LabelAccess:

    pass
class DerivesFrom:

    pass
class FormalParameterType:

    pass
class astm_gastm_ByValueFormalParameterType(FormalParameterType):

    pass
class astm_gastm_ByReferenceFormalParameterType(FormalParameterType):

    pass
class EnumLiteralDefinition:

    pass
class DataType:

    pass
class astm_gastm_EnumType(DataType):

    pass
class astm_gastm_FormalParameterType(DataType):

    pass
class astm_gastm_ConstructedType(DataType):

    pass
class astm_gastm_NamedType(DataType):

    pass
class astm_gastm_AggregateType(DataType):

    pass
class astm_gastm_ExceptionType(DataType):

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

class MacroDefinition:

    pass
class Dimension:

    pass
class ConstructedType:

    pass
class astm_gastm_CollectionType(ConstructedType):

    pass
class astm_gastm_RangeType(ConstructedType):

    pass
class astm_gastm_PointerType(ConstructedType):

    pass
class astm_gastm_ReferenceType(ConstructedType):

    pass
class astm_gastm_ArrayType(ConstructedType):

    pass
class AggregateScope:

    pass
class NameSpaceType:

    pass
class AggregateType:

    pass
class astm_gastm_AnnotationType(AggregateType):

    pass
class astm_gastm_ClassType(AggregateType):

    pass
class astm_gastm_StructureType(AggregateType):

    pass
class astm_gastm_UnionType(AggregateType):

    pass
class NamedType:

    pass
class TypeDefinition:

    pass
class astm_gastm_AggregateTypeDefinition(TypeDefinition):

    pass
class astm_gastm_NamedTypeDefinition(TypeDefinition):

    pass
class LabelType:

    pass
class VirtualSpecification:

    pass
class astm_gastm_Virtual(VirtualSpecification):

    pass
class astm_gastm_NonVirtual(VirtualSpecification):

    pass
class astm_gastm_PureVirtual(VirtualSpecification):

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
class Statement:

    pass
class astm_gastm_ContinueStatement(Statement):

    pass
class astm_gastm_DeleteStatement(Statement):

    pass
class astm_gastm_SpecificSelectStatement(Statement):

    pass
class astm_gastm_SwitchStatement(Statement):

    pass
class astm_gastm_ExpressionStatement(Statement):

    pass
class astm_gastm_ReturnStatement(Statement):

    pass
class astm_gastm_EmptyStatement(Statement):

    pass
class astm_gastm_JumpStatement(Statement):

    pass
class astm_gastm_TerminateStatement(Statement):

    pass
class astm_gastm_LabeledStatement(Statement):

    pass
class astm_gastm_LoopStatement(Statement):

    pass
class astm_gastm_BlockStatement(Statement):

    pass
class astm_gastm_TryStatement(Statement):

    pass
class astm_gastm_DeclarationOrDefinitionStatement(Statement):

    pass
class astm_gastm_IfStatement(Statement):

    pass
class astm_gastm_BreakStatement(Statement):

    pass
class astm_gastm_ThrowStatement(Statement):

    pass
class FormalParameterDefinition:

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
class astm_gastm_AnnotationExpression(Expression):

    pass
class astm_gastm_ArrayAccess(Expression):

    pass
class astm_gastm_ConditionalExpression(Expression):

    pass
class astm_gastm_CastExpression(Expression):

    pass
class astm_gastm_BinaryExpression(Expression):

    pass
class astm_gastm_NewExpression(Expression):

    pass
class astm_gastm_AggregateExpression(Expression):

    pass
class astm_gastm_RangeExpression(Expression):

    pass
class astm_gastm_NameReference(Expression):

    pass
class astm_gastm_LabelAccess(Expression):

    pass
class astm_gastm_Literal(Expression):

    def __init__(self, value: str, Expression88: "astm_gastm_Dimension", Expression204: "astm_gastm_BinaryExpression", Expression182: "astm_gastm_QualifiedIdentifierReference", Expression194: "astm_gastm_CastExpression", Expression115: "astm_gastm_JumpStatement", Expression214: "astm_gastm_ConditionalExpression", Expression217: "astm_gastm_ConditionalExpression", Expression136: "astm_gastm_SwitchStatement", Expression154: "astm_gastm_ForStatement", Expression: "astm_gastm_DataDefinition", Expression224: "astm_gastm_FunctionCallExpression", Expression146: "astm_gastm_LoopStatement", Expression55: "astm_gastm_BitFieldDefinition", Expression180: "astm_gastm_ArrayAccess", Expression85: "astm_gastm_Dimension", Expression109: "astm_gastm_DeleteStatement", Expression177: "astm_gastm_ArrayAccess", Expression57: "astm_gastm_EnumLiteralDefinition", Expression222: "astm_gastm_RangeExpression", Expression142: "astm_gastm_CaseBlock", Expression199: "astm_gastm_UnaryExpression", Expression128: "astm_gastm_IfStatement", Expression243: "astm_gastm_AnnotationExpression", Expression113: "astm_gastm_ExpressionStatement", Expression228: "astm_gastm_ActualParameterExpression", Expression168: "astm_gastm_ThrowStatement", Expression144: "astm_gastm_ReturnStatement", Expression211: "astm_gastm_ConditionalExpression", Expression219: "astm_gastm_RangeExpression", Expression151: "astm_gastm_ForStatement", Expression207: "astm_gastm_BinaryExpression"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class astm_gastm_UnaryExpression(Expression):

    pass
class astm_gastm_FunctionCallExpression(Expression):

    pass
class Definition:

    pass
class astm_gastm_EntryDefinition(Definition):

    pass
class astm_gastm_EnumLiteralDefinition(Definition):

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

class astm_gastm_SpecificTriggerDefinition(Definition):

    pass
class astm_gastm_FunctionDefinition(Definition):

    pass
class TypeReference:

    pass
class astm_gastm_NamedTypeReference(TypeReference):

    pass
class astm_gastm_UnnamedTypeReference(TypeReference):

    pass
class Name:

    pass
class DeclarationOrDefinition:

    pass
class astm_gastm_Declaration(DeclarationOrDefinition):

    pass
class astm_gastm_Definition(DeclarationOrDefinition):

    pass
class ProgramScope:

    pass
class FunctionMemberAttributes:

    pass
class FormalParameterDeclaration:

    pass
class Declaration:

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

class astm_gastm_FormalParameterDeclaration(Declaration):

    pass
class astm_gastm_FunctionDeclaration(Declaration):

    pass
class PreprocessorElement:

    pass
class astm_gastm_IncludeUnit(PreprocessorElement):

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

class astm_gastm_MacroCall(PreprocessorElement):

    pass
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

class SourceLocation:

    pass
class GASTMObject:

    pass
class astm_gastm_GASTMSyntaxObject(GASTMObject):

    pass
class Scope:

    pass
class astm_gastm_GlobalScope(Scope):

    pass
class astm_gastm_AggregateScope(Scope):

    pass
class astm_gastm_ProgramScope(Scope):

    pass
class astm_gastm_FunctionScope(Scope):

    pass
class astm_gastm_BlockScope(Scope):

    pass
class DefinitionObject:

    pass
class astm_gastm_DeclarationOrDefinition(DefinitionObject):

    def __init__(self, isRegister: bool, linkageSpecifier: str, astm_gastm_DeclarationOrDefinition: "OtherSyntaxObject" = None, astm_gastm_DeclarationOrDefinition18: "OtherSyntaxObject" = None, DefinitionObject13: "astm_gastm_CompilationUnit", DefinitionObject264: "astm_sastm_DelphiFunctionCallExpression", DefinitionObject80: "astm_gastm_AggregateType", DefinitionObject66: "astm_gastm_NameSpaceDefinition", DefinitionObject262: "astm_sastm_DelphiBlockStatement", DefinitionObject266: "astm_sastm_DelphiWithStatement", DefinitionObject111: "astm_gastm_DeclarationOrDefinitionStatement", DefinitionObject: "astm_gastm_Scope", DefinitionObject175: "astm_gastm_NameReference"):
        self.isRegister = isRegister
        self.linkageSpecifier = linkageSpecifier
        self.astm_gastm_DeclarationOrDefinition = astm_gastm_DeclarationOrDefinition
        self.astm_gastm_DeclarationOrDefinition18 = astm_gastm_DeclarationOrDefinition18
        
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
class astm_gastm_LabelDefinition(DefinitionObject):

    pass
class astm_gastm_NameSpaceDefinition(DefinitionObject):

    pass
class GlobalScope:

    pass
class CompilationUnit:

    pass
class astm_sastm_DelphiImplementationSection(CompilationUnit):

    pass
class astm_sastm_DelphiUnit(CompilationUnit):

    pass
class astm_sastm_DelphiInterfaceSection(CompilationUnit):

    pass
class GASTMSemanticObject:

    pass
class astm_gastm_Scope(GASTMSemanticObject):

    pass
class astm_gastm_Project(GASTMSemanticObject):

    pass
class SourceFile:

    pass
class GASTMSourceObject:

    pass
class astm_gastm_SourceLocation(GASTMSourceObject):

    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int, astm_gastm_SourceLocation: "SourceFile" = None):
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.astm_gastm_SourceLocation = astm_gastm_SourceLocation
        
    @property
    def endLine(self) -> int:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine

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
    def endColumn(self) -> int:
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn

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
class OtherSyntaxObject:

    pass
class astm_gastm_Dimension(OtherSyntaxObject):

    pass
class astm_gastm_VirtualSpecification(OtherSyntaxObject):

    pass
class astm_gastm_DerivesFrom(OtherSyntaxObject):

    def __init__(self, isVirtual: bool, astm_gastm_DerivesFrom100: "NamedType" = None, astm_gastm_DerivesFrom: "OtherSyntaxObject" = None, OtherSyntaxObject233: "astm_gastm_NewExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject201: "astm_gastm_BinaryExpression", OtherSyntaxObject98: "astm_gastm_DerivesFrom", OtherSyntaxObject196: "astm_gastm_UnaryExpression", OtherSyntaxObject209: "astm_gastm_OperatorAssign"):
        self.isVirtual = isVirtual
        self.astm_gastm_DerivesFrom100 = astm_gastm_DerivesFrom100
        self.astm_gastm_DerivesFrom = astm_gastm_DerivesFrom
        
    @property
    def isVirtual(self) -> bool:
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual

    @property
    def astm_gastm_DerivesFrom100(self):
        return self.__astm_gastm_DerivesFrom100

    @astm_gastm_DerivesFrom100.setter
    def astm_gastm_DerivesFrom100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_gastm_DerivesFrom__astm_gastm_DerivesFrom100", None)
        self.__astm_gastm_DerivesFrom100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedType101"):
                opp_val = getattr(old_value, "NamedType101", None)
                if opp_val == self:
                    setattr(old_value, "NamedType101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedType101"):
                opp_val = getattr(value, "NamedType101", None)
                setattr(value, "NamedType101", self)

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
            if hasattr(old_value, "OtherSyntaxObject98"):
                opp_val = getattr(old_value, "OtherSyntaxObject98", None)
                if opp_val == self:
                    setattr(old_value, "OtherSyntaxObject98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OtherSyntaxObject98"):
                opp_val = getattr(value, "OtherSyntaxObject98", None)
                setattr(value, "OtherSyntaxObject98", self)

class astm_gastm_CatchBlock(OtherSyntaxObject):

    pass
class astm_gastm_FunctionMemberAttribute(OtherSyntaxObject):

    pass
class astm_gastm_SwitchCase(OtherSyntaxObject):

    pass
class astm_gastm_Name(OtherSyntaxObject):

    def __init__(self, nameString: str, OtherSyntaxObject233: "astm_gastm_NewExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject201: "astm_gastm_BinaryExpression", OtherSyntaxObject98: "astm_gastm_DerivesFrom", OtherSyntaxObject196: "astm_gastm_UnaryExpression", OtherSyntaxObject209: "astm_gastm_OperatorAssign"):
        self.nameString = nameString
        
    @property
    def nameString(self) -> str:
        return self.__nameString

    @nameString.setter
    def nameString(self, nameString: str):
        self.__nameString = nameString

class astm_gastm_CompilationUnit(OtherSyntaxObject):

    def __init__(self, language: str, astm_gastm_CompilationUnit: set["DefinitionObject"] = None, astm_gastm_CompilationUnit15: "ProgramScope" = None, OtherSyntaxObject233: "astm_gastm_NewExpression", OtherSyntaxObject: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject19: "astm_gastm_DeclarationOrDefinition", OtherSyntaxObject201: "astm_gastm_BinaryExpression", OtherSyntaxObject98: "astm_gastm_DerivesFrom", OtherSyntaxObject196: "astm_gastm_UnaryExpression", OtherSyntaxObject209: "astm_gastm_OperatorAssign"):
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

class AnnotationExpression:

    pass
class astm_gastm_AccessKind:

    pass
class Type:

    pass
class astm_gastm_TypeReference(Type):

    pass
class astm_gastm_LabelType(Type):

    pass
class astm_gastm_NameSpaceType(Type):

    pass
class astm_gastm_FunctionType(Type):

    pass
class astm_gastm_DataType(Type):

    pass
class astm_gastm_StorageSpecification(ABC):

    pass
class GASTMSyntaxObject:

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

class astm_gastm_DefinitionObject(GASTMSyntaxObject):

    pass
class astm_gastm_Expression(GASTMSyntaxObject):

    pass
class astm_gastm_OtherSyntaxObject(GASTMSyntaxObject):

    pass
class astm_gastm_GASTMSemanticObject(ABC):

    pass
class astm_gastm_GASTMSourceObject(ABC):

    pass
class astm_gastm_GASTMObject:

    pass