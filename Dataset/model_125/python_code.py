from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PrimitiveType:

    pass
class astm_WideCharacter(PrimitiveType):

    pass
class astm_Character(PrimitiveType):

    pass
class astm_Double(PrimitiveType):

    pass
class astm_Integer(PrimitiveType):

    pass
class astm_Byte(PrimitiveType):

    pass
class astm_LongInteger(PrimitiveType):

    pass
class astm_Boolean(PrimitiveType):

    pass
class astm_String(PrimitiveType):

    pass
class astm_LongDouble(PrimitiveType):

    pass
class astm_ShortInteger(PrimitiveType):

    pass
class astm_Float(PrimitiveType):

    pass
class astm_Void(PrimitiveType):

    pass
class StorageSpecification:

    pass
class astm_FunctionPersistent(StorageSpecification):

    pass
class astm_NoDef(StorageSpecification):

    pass
class astm_PerClassMember(StorageSpecification):

    pass
class astm_FileLocal(StorageSpecification):

    pass
class astm_External(StorageSpecification):

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
class AccessKind:

    pass
class astm_Private(AccessKind):

    pass
class astm_Protected(AccessKind):

    pass
class astm_Public(AccessKind):

    pass
class BinaryOperator:

    pass
class astm_BitXor(BinaryOperator):

    pass
class astm_BitAnd(BinaryOperator):

    pass
class astm_BitLeftShift(BinaryOperator):

    pass
class astm_BitRightShift(BinaryOperator):

    pass
class astm_BitOr(BinaryOperator):

    pass
class astm_OperatorAssign(BinaryOperator):

    pass
class ActualParameter:

    pass
class astm_ActualParameterExpression(ActualParameter):

    pass
class IdentifierReference:

    pass
class NameReference:

    pass
class astm_TypeQualifiedIdentifierReference(NameReference):

    pass
class astm_IdentifierReference(NameReference):

    pass
class astm_QualifiedIdentifierReference(NameReference):

    pass
class CatchBlock:

    pass
class LoopStatement:

    pass
class astm_DoWhileStatement(LoopStatement):

    pass
class astm_WhileStatement(LoopStatement):

    pass
class astm_ForStatement(LoopStatement):

    pass
class SwitchCase:

    pass
class astm_CaseBlock(SwitchCase):

    pass
class astm_DefaultBlock(SwitchCase):

    pass
class astm_VariableCatchBlock(CatchBlock):

    pass
class astm_TypesCatchBlock(CatchBlock):

    pass
class BlockScope:

    pass
class DerivesFrom:

    pass
class astm_SpecificConcatString(BinaryOperator):

    pass
class astm_SpecificLike(BinaryOperator):

    pass
class astm_SpecificIn(BinaryOperator):

    pass
class astm_SpecificGreaterEqual(BinaryOperator):

    pass
class astm_SpecificLessEqual(BinaryOperator):

    pass
class ActualParameterExpression:

    pass
class astm_ByReferenceActualParameterExpression(ActualParameterExpression):

    pass
class astm_ByValueActualParameterExpression(ActualParameterExpression):

    pass
class astm_MissingActualParameter(ActualParameter):

    pass
class astm_NotLess(BinaryOperator):

    pass
class astm_Less(BinaryOperator):

    pass
class astm_NotGreater(BinaryOperator):

    pass
class astm_Greater(BinaryOperator):

    pass
class astm_NotEqual(BinaryOperator):

    pass
class astm_Equal(BinaryOperator):

    pass
class astm_Or(BinaryOperator):

    pass
class astm_And(BinaryOperator):

    pass
class astm_Exponent(BinaryOperator):

    pass
class astm_Modulus(BinaryOperator):

    pass
class astm_Divide(BinaryOperator):

    pass
class astm_Multiply(BinaryOperator):

    pass
class astm_Subtract(BinaryOperator):

    pass
class astm_Add(BinaryOperator):

    pass
class UnaryOperator:

    pass
class astm_BitNot(UnaryOperator):

    pass
class astm_Not(UnaryOperator):

    pass
class astm_Decrement(UnaryOperator):

    pass
class astm_Negate(UnaryOperator):

    pass
class astm_Deref(UnaryOperator):

    pass
class astm_Increment(UnaryOperator):

    pass
class astm_PostDecrement(UnaryOperator):

    pass
class astm_PostIncrement(UnaryOperator):

    pass
class astm_AddressOf(UnaryOperator):

    pass
class astm_UnaryPlus(UnaryOperator):

    pass
class Literal:

    pass
class astm_StringLiteral(Literal):

    pass
class astm_BitLiteral(Literal):

    pass
class astm_CharLiteral(Literal):

    pass
class astm_RealLiteral(Literal):

    pass
class astm_BooleanLiteral(Literal):

    pass
class astm_IntegerlLiteral(Literal):

    pass
class astm_Assign(BinaryOperator):

    pass
class LabelDefinition:

    pass
class LabelAccess:

    pass
class Dimension:

    pass
class ConstructedType:

    pass
class astm_PointerType(ConstructedType):

    pass
class astm_ReferenceType(ConstructedType):

    pass
class astm_RangeType(ConstructedType):

    pass
class astm_CollectionType(ConstructedType):

    pass
class astm_ArrayType(ConstructedType):

    pass
class AggregateScope:

    pass
class EnumLiteralDefinition:

    pass
class DataType:

    pass
class astm_ExceptionType(DataType):

    pass
class astm_EnumType(DataType):

    pass
class astm_AggregateType(DataType):

    pass
class astm_ConstructedType(DataType):

    pass
class astm_FormalParameterType(DataType):

    pass
class astm_NamedType(DataType):

    pass
class astm_PrimitiveType(DataType):

    def __init__(self, isSigned: bool):
        self.isSigned = isSigned
        
        pass
    @property
    def isSigned(self):
        return self.__isSigned

    @isSigned.setter
    def isSigned(self, isSigned: bool):
        self.__isSigned = isSigned


class FormalParameterType:

    pass
class astm_ByReferenceFormalParameterType(FormalParameterType):

    pass
class astm_ByValueFormalParameterType(FormalParameterType):

    pass
class Type:

    pass
class astm_NameSpaceType(Type):

    pass
class astm_TypeReference(Type):

    pass
class astm_LabelType(Type):

    pass
class astm_FunctionType(Type):

    pass
class MacroDefinition:

    pass
class LabelType:

    pass
class NameSpaceType:

    pass
class AggregateType:

    pass
class astm_ClassType(AggregateType):

    pass
class astm_AnnotationType(AggregateType):

    pass
class astm_StructureType(AggregateType):

    pass
class astm_UnionType(AggregateType):

    pass
class NamedType:

    pass
class TypeDefinition:

    pass
class astm_AggregateTypeDefinition(TypeDefinition):

    pass
class astm_NamedTypeDefinition(TypeDefinition):

    pass
class DataDefinition:

    pass
class astm_FormalParameterDefinition(DataDefinition):

    pass
class astm_VariableDefinition(DataDefinition):

    pass
class astm_BitFieldDefinition(DataDefinition):

    pass
class Expression:

    pass
class astm_RangeExpression(Expression):

    pass
class astm_NewExpression(Expression):

    pass
class astm_ConditionalExpression(Expression):

    pass
class astm_AnnotationExpression(Expression):

    pass
class astm_NameReference(Expression):

    pass
class astm_ArrayAccess(Expression):

    pass
class astm_CastExpression(Expression):

    pass
class astm_BinaryExpression(Expression):

    pass
class astm_AggregateExpression(Expression):

    pass
class astm_Literal(Expression):

    def __init__(self, value: str, Expression141: "astm_ReturnStatement" = None, Expression208: "astm_ConditionalExpression" = None, Expression196: "astm_UnaryExpression" = None, Expression211: "astm_ConditionalExpression" = None, Expression225: "astm_ActualParameterExpression" = None, Expression165: "astm_ThrowStatement" = None, Expression133: "astm_SwitchStatement" = None, Expression82: "astm_Dimension" = None, Expression214: "astm_ConditionalExpression" = None, Expression177: "astm_ArrayAccess" = None, Expression112: "astm_JumpStatement" = None, Expression204: "astm_BinaryExpression" = None, Expression191: "astm_CastExpression" = None, Expression240: "astm_AnnotationExpression" = None, Expression143: "astm_LoopStatement" = None, Expression221: "astm_FunctionCallExpression" = None, Expression139: "astm_CaseBlock" = None, Expression110: "astm_ExpressionStatement" = None, Expression54: "astm_EnumLiteralDefinition" = None, Expression174: "astm_ArrayAccess" = None, Expression106: "astm_DeleteStatement" = None, Expression179: "astm_QualifiedIdentifierReference" = None, Expression219: "astm_RangeExpression" = None, Expression: "astm_DataDefinition" = None, Expression125: "astm_IfStatement" = None, Expression201: "astm_BinaryExpression" = None, Expression216: "astm_RangeExpression" = None, Expression148: "astm_ForStatement" = None, Expression151: "astm_ForStatement" = None, Expression52: "astm_BitFieldDefinition" = None, Expression85: "astm_Dimension" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class astm_UnaryExpression(Expression):

    pass
class astm_FunctionCallExpression(Expression):

    pass
class astm_LabelAccess(Expression):

    pass
class GASTMSyntaxObject:

    pass
class astm_Expression(GASTMSyntaxObject):

    pass
class astm_PreprocessorElement(GASTMSyntaxObject):

    pass
class astm_DefinitionObject(GASTMSyntaxObject):

    pass
class astm_Statement(GASTMSyntaxObject):

    pass
class astm_Type(GASTMSyntaxObject):

    def __init__(self, isConst: bool, isVolatile: bool):
        self.isConst = isConst
        self.isVolatile = isVolatile
        
        pass
    @property
    def isVolatile(self):
        return self.__isVolatile

    @isVolatile.setter
    def isVolatile(self, isVolatile: bool):
        self.__isVolatile = isVolatile


    @property
    def isConst(self):
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: bool):
        self.__isConst = isConst


class Statement:

    pass
class astm_TryStatement(Statement):

    pass
class astm_BlockStatement(Statement):

    pass
class astm_ReturnStatement(Statement):

    pass
class astm_BreakStatement(Statement):

    pass
class astm_ContinueStatement(Statement):

    pass
class astm_EmptyStatement(Statement):

    pass
class astm_JumpStatement(Statement):

    pass
class astm_DeclarationOrDefinitionStatement(Statement):

    pass
class astm_SwitchStatement(Statement):

    pass
class astm_LabeledStatement(Statement):

    pass
class astm_DeleteStatement(Statement):

    pass
class astm_TerminateStatement(Statement):

    pass
class astm_SpecificSelectStatement(Statement):

    pass
class astm_ThrowStatement(Statement):

    pass
class astm_LoopStatement(Statement):

    pass
class astm_IfStatement(Statement):

    pass
class astm_ExpressionStatement(Statement):

    pass
class FormalParameterDefinition:

    pass
class FunctionMemberAttributes:

    pass
class FormalParameterDeclaration:

    pass
class Declaration:

    pass
class astm_FormalParameterDeclaration(Declaration):

    pass
class astm_VariableDeclaration(Declaration):

    def __init__(self, isMutable: bool):
        self.isMutable = isMutable
        
        pass
    @property
    def isMutable(self):
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable


class astm_FunctionDeclaration(Declaration):

    pass
class Definition:

    pass
class astm_FunctionDefinition(Definition):

    pass
class astm_SpecificTriggerDefinition(Definition):

    pass
class astm_DataDefinition(Definition):

    def __init__(self, isMutable: bool, astm_DataDefinition: "Expression" = None, Definition: "astm_Declaration" = None):
        self.isMutable = isMutable
        self.astm_DataDefinition = astm_DataDefinition
        
        pass
    @property
    def isMutable(self):
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: bool):
        self.__isMutable = isMutable


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
            if hasattr(old_value, "Expression"):
                opp_val = getattr(old_value, "Expression", None)
                if opp_val == self:
                    setattr(old_value, "Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression"):
                opp_val = getattr(value, "Expression", None)
                setattr(value, "Expression", self)

class astm_EnumLiteralDefinition(Definition):

    pass
class TypeReference:

    pass
class astm_UnnamedTypeReference(TypeReference):

    pass
class astm_NamedTypeReference(TypeReference):

    pass
class Name:

    pass
class DeclarationOrDefinition:

    pass
class astm_Declaration(DeclarationOrDefinition):

    pass
class astm_Definition(DeclarationOrDefinition):

    pass
class ProgramScope:

    pass
class OtherSyntaxObject:

    pass
class astm_Dimension(OtherSyntaxObject):

    pass
class astm_CatchBlock(OtherSyntaxObject):

    pass
class astm_DerivesFrom(OtherSyntaxObject):

    def __init__(self, isVirtual: bool, astm_DerivesFrom: "OtherSyntaxObject" = None, astm_DerivesFrom97: "NamedType" = None, OtherSyntaxObject198: "astm_BinaryExpression" = None, OtherSyntaxObject: "astm_DeclarationOrDefinition" = None, OtherSyntaxObject230: "astm_NewExpression" = None, OtherSyntaxObject95: "astm_DerivesFrom" = None, OtherSyntaxObject206: "astm_OperatorAssign" = None, OtherSyntaxObject19: "astm_DeclarationOrDefinition" = None, OtherSyntaxObject193: "astm_UnaryExpression" = None):
        self.isVirtual = isVirtual
        self.astm_DerivesFrom = astm_DerivesFrom
        self.astm_DerivesFrom97 = astm_DerivesFrom97
        
        pass
    @property
    def isVirtual(self):
        return self.__isVirtual

    @isVirtual.setter
    def isVirtual(self, isVirtual: bool):
        self.__isVirtual = isVirtual


    @property
    def astm_DerivesFrom97(self):
        return self.__astm_DerivesFrom97

    @astm_DerivesFrom97.setter
    def astm_DerivesFrom97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DerivesFrom__astm_DerivesFrom97", None)
        self.__astm_DerivesFrom97 = value
        
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
    def astm_DerivesFrom(self):
        return self.__astm_DerivesFrom

    @astm_DerivesFrom.setter
    def astm_DerivesFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DerivesFrom__astm_DerivesFrom", None)
        self.__astm_DerivesFrom = value
        
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

class astm_Name(OtherSyntaxObject):

    def __init__(self, nameString: str, OtherSyntaxObject198: "astm_BinaryExpression" = None, OtherSyntaxObject: "astm_DeclarationOrDefinition" = None, OtherSyntaxObject230: "astm_NewExpression" = None, OtherSyntaxObject95: "astm_DerivesFrom" = None, OtherSyntaxObject206: "astm_OperatorAssign" = None, OtherSyntaxObject19: "astm_DeclarationOrDefinition" = None, OtherSyntaxObject193: "astm_UnaryExpression" = None):
        self.nameString = nameString
        
        pass
    @property
    def nameString(self):
        return self.__nameString

    @nameString.setter
    def nameString(self, nameString: str):
        self.__nameString = nameString


class astm_FunctionMemberAttribute(OtherSyntaxObject):

    pass
class astm_SwitchCase(OtherSyntaxObject):

    pass
class astm_VirtualSpecification(OtherSyntaxObject):

    pass
class astm_CompilationUnit(OtherSyntaxObject):

    def __init__(self, language: str, astm_CompilationUnit: set["DefinitionObject"] = None, astm_CompilationUnit15: "ProgramScope" = None, OtherSyntaxObject198: "astm_BinaryExpression" = None, OtherSyntaxObject: "astm_DeclarationOrDefinition" = None, OtherSyntaxObject230: "astm_NewExpression" = None, OtherSyntaxObject95: "astm_DerivesFrom" = None, OtherSyntaxObject206: "astm_OperatorAssign" = None, OtherSyntaxObject19: "astm_DeclarationOrDefinition" = None, OtherSyntaxObject193: "astm_UnaryExpression" = None):
        self.language = language
        self.astm_CompilationUnit = astm_CompilationUnit if astm_CompilationUnit is not None else set()
        self.astm_CompilationUnit15 = astm_CompilationUnit15
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def astm_CompilationUnit(self):
        return self.__astm_CompilationUnit

    @astm_CompilationUnit.setter
    def astm_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_CompilationUnit__astm_CompilationUnit", None)
        self.__astm_CompilationUnit = value if value is not None else set()
        
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
    def astm_CompilationUnit15(self):
        return self.__astm_CompilationUnit15

    @astm_CompilationUnit15.setter
    def astm_CompilationUnit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_CompilationUnit__astm_CompilationUnit15", None)
        self.__astm_CompilationUnit15 = value
        
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

class astm_EntryDefinition(Definition):

    pass
class VirtualSpecification:

    pass
class astm_NonVirtual(VirtualSpecification):

    pass
class astm_Virtual(VirtualSpecification):

    pass
class astm_PureVirtual(VirtualSpecification):

    pass
class astm_FunctionMemberAttributes:

    def __init__(self, isFriend: bool, isInline: bool, isThisConst: bool, astm_FunctionMemberAttributes: "VirtualSpecification" = None):
        self.isFriend = isFriend
        self.isInline = isInline
        self.isThisConst = isThisConst
        self.astm_FunctionMemberAttributes = astm_FunctionMemberAttributes
        
        pass
    @property
    def isInline(self):
        return self.__isInline

    @isInline.setter
    def isInline(self, isInline: bool):
        self.__isInline = isInline


    @property
    def isFriend(self):
        return self.__isFriend

    @isFriend.setter
    def isFriend(self, isFriend: bool):
        self.__isFriend = isFriend


    @property
    def isThisConst(self):
        return self.__isThisConst

    @isThisConst.setter
    def isThisConst(self, isThisConst: bool):
        self.__isThisConst = isThisConst


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
class Scope:

    pass
class astm_GlobalScope(Scope):

    pass
class astm_ProgramScope(Scope):

    pass
class astm_AggregateScope(Scope):

    pass
class astm_FunctionScope(Scope):

    pass
class astm_BlockScope(Scope):

    pass
class DefinitionObject:

    pass
class astm_LabelDefinition(DefinitionObject):

    pass
class astm_DeclarationOrDefinition(DefinitionObject):

    def __init__(self, isRegister: bool, linkageSpecifier: str, astm_DeclarationOrDefinition: "OtherSyntaxObject" = None, astm_DeclarationOrDefinition18: "OtherSyntaxObject" = None, DefinitionObject: "astm_Scope" = None, DefinitionObject63: "astm_NameSpaceDefinition" = None, DefinitionObject172: "astm_NameReference" = None, DefinitionObject108: "astm_DeclarationOrDefinitionStatement" = None, DefinitionObject77: "astm_AggregateType" = None, DefinitionObject13: "astm_CompilationUnit" = None):
        self.isRegister = isRegister
        self.linkageSpecifier = linkageSpecifier
        self.astm_DeclarationOrDefinition = astm_DeclarationOrDefinition
        self.astm_DeclarationOrDefinition18 = astm_DeclarationOrDefinition18
        
        pass
    @property
    def linkageSpecifier(self):
        return self.__linkageSpecifier

    @linkageSpecifier.setter
    def linkageSpecifier(self, linkageSpecifier: str):
        self.__linkageSpecifier = linkageSpecifier


    @property
    def isRegister(self):
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
    def astm_DeclarationOrDefinition18(self):
        return self.__astm_DeclarationOrDefinition18

    @astm_DeclarationOrDefinition18.setter
    def astm_DeclarationOrDefinition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_astm_DeclarationOrDefinition__astm_DeclarationOrDefinition18", None)
        self.__astm_DeclarationOrDefinition18 = value
        
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

class astm_NameSpaceDefinition(DefinitionObject):

    pass
class astm_TypeDefinition(DefinitionObject):

    pass
class GlobalScope:

    pass
class CompilationUnit:

    pass
class GASTMSemanticObject:

    pass
class astm_Scope(GASTMSemanticObject):

    pass
class astm_Project(GASTMSemanticObject):

    pass
class SourceFile:

    pass
class GASTMSourceObject:

    pass
class astm_SourceLocation(GASTMSourceObject):

    def __init__(self, startLine: int, startColumn: int, endLine: int, endColumn: int, astm_SourceLocation: "SourceFile" = None):
        self.startLine = startLine
        self.startColumn = startColumn
        self.endLine = endLine
        self.endColumn = endColumn
        self.astm_SourceLocation = astm_SourceLocation
        
        pass
    @property
    def startColumn(self):
        return self.__startColumn

    @startColumn.setter
    def startColumn(self, startColumn: int):
        self.__startColumn = startColumn


    @property
    def startLine(self):
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: int):
        self.__startLine = startLine


    @property
    def endLine(self):
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: int):
        self.__endLine = endLine


    @property
    def endColumn(self):
        return self.__endColumn

    @endColumn.setter
    def endColumn(self, endColumn: int):
        self.__endColumn = endColumn


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
            if hasattr(old_value, "SourceFile"):
                opp_val = getattr(old_value, "SourceFile", None)
                if opp_val == self:
                    setattr(old_value, "SourceFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SourceFile"):
                opp_val = getattr(value, "SourceFile", None)
                setattr(value, "SourceFile", self)

class astm_SourceFile(GASTMSourceObject):

    def __init__(self, pathName: str):
        self.pathName = pathName
        
        pass
    @property
    def pathName(self):
        return self.__pathName

    @pathName.setter
    def pathName(self, pathName: str):
        self.__pathName = pathName


class astm_ActualParameter(ABC):

    pass
class astm_BinaryOperator(ABC):

    pass
class astm_UnaryOperator(ABC):

    pass
class astm_AccessKind:

    pass
class astm_DataType(ABC):

    pass
class astm_StorageSpecification(ABC):

    pass
class astm_OtherSyntaxObject(ABC):

    pass
class astm_GASTMSemanticObject(ABC):

    pass
class astm_GASTMSourceObject(ABC):

    pass
class astm_GASTMObject:

    pass
class AnnotationExpression:

    pass
class PreprocessorElement:

    pass
class astm_IncludeUnit(PreprocessorElement):

    pass
class astm_MacroCall(PreprocessorElement):

    pass
class astm_MacroDefinition(PreprocessorElement):

    def __init__(self, macroName: str, body: str, PreprocessorElement: "astm_GASTMSyntaxObject" = None):
        self.macroName = macroName
        self.body = body
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def macroName(self):
        return self.__macroName

    @macroName.setter
    def macroName(self, macroName: str):
        self.__macroName = macroName


class astm_Comment(PreprocessorElement):

    def __init__(self, text: str, PreprocessorElement: "astm_GASTMSyntaxObject" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class SourceLocation:

    pass
class GASTMObject:

    pass
class astm_GASTMSyntaxObject(GASTMObject):

    pass