from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ActualParameterExpression:

    pass
class gastm_ByReferenceActualParameterExpression(ActualParameterExpression):

    pass
class gastm_ByValueActualParameterExpression(ActualParameterExpression):

    pass
class BinaryOperator:

    pass
class gastm_Equal(BinaryOperator):

    pass
class gastm_NotGreater(BinaryOperator):

    pass
class gastm_Exponent(BinaryOperator):

    pass
class gastm_Divide(BinaryOperator):

    pass
class gastm_Modulus(BinaryOperator):

    pass
class gastm_Or(BinaryOperator):

    pass
class gastm_Greater(BinaryOperator):

    pass
class gastm_Subtract(BinaryOperator):

    pass
class gastm_And(BinaryOperator):

    pass
class gastm_Multiply(BinaryOperator):

    pass
class gastm_NotEqual(BinaryOperator):

    pass
class gastm_NotLess(BinaryOperator):

    pass
class gastm_Less(BinaryOperator):

    pass
class gastm_Add(BinaryOperator):

    pass
class ActualParameter:

    pass
class gastm_MissingActualParameter(ActualParameter):

    pass
class gastm_ActualParameterExpression(ActualParameter):

    pass
class gastm_OperatorAssign(BinaryOperator):

    pass
class gastm_Assign(BinaryOperator):

    pass
class gastm_BitRightShift(BinaryOperator):

    pass
class gastm_BitLeftShift(BinaryOperator):

    pass
class gastm_BitXor(BinaryOperator):

    pass
class gastm_BitOr(BinaryOperator):

    pass
class gastm_BitAnd(BinaryOperator):

    pass
class Literal:

    pass
class gastm_CharLiteral(Literal):

    pass
class gastm_RealLiteral(Literal):

    pass
class gastm_StringLiteral(Literal):

    pass
class gastm_IntegerLiteral(Literal):

    pass
class QualifiedIdentifierReference:

    pass
class gastm_QualifiedOverData(QualifiedIdentifierReference):

    pass
class gastm_QualifiedOverPointer(QualifiedIdentifierReference):

    pass
class NameReference:

    pass
class gastm_QualifiedIdentifierReference(NameReference):

    pass
class gastm_TypeQualifiedIdentifierReference(NameReference):

    pass
class gastm_IdentifierReference(NameReference):

    pass
class UnaryOperator:

    pass
class gastm_PostIncrement(UnaryOperator):

    pass
class gastm_PostDecrement(UnaryOperator):

    pass
class gastm_AddressOf(UnaryOperator):

    pass
class gastm_BitNot(UnaryOperator):

    pass
class gastm_Deref(UnaryOperator):

    pass
class gastm_Increment(UnaryOperator):

    pass
class gastm_UnaryMinus(UnaryOperator):

    pass
class gastm_Not(UnaryOperator):

    pass
class gastm_Decrement(UnaryOperator):

    pass
class gastm_UnaryPlus(UnaryOperator):

    pass
class gastm_EnumLiteral(Literal):

    pass
class gastm_BitLiteral(Literal):

    pass
class gastm_BooleanLiteral(Literal):

    pass
class Expression:

    pass
class gastm_ConditionalExpression(Expression):

    pass
class gastm_ArrayAccess(Expression):

    pass
class gastm_NameReference(Expression):

    pass
class gastm_CastExpression(Expression):

    pass
class gastm_FunctionCallExpression(Expression):

    pass
class gastm_CollectionExpression(Expression):

    pass
class gastm_RangeExpression(Expression):

    pass
class gastm_NewExpression(Expression):

    pass
class gastm_Literal(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class CatchBlock:

    pass
class gastm_VariableCatchBlock(CatchBlock):

    pass
class gastm_TypesCatchBlock(CatchBlock):

    pass
class ForStatement:

    pass
class gastm_ForCheckAfterStatement(ForStatement):

    pass
class gastm_ForCheckBeforeStatement(ForStatement):

    pass
class gastm_BinaryExpression(Expression):

    pass
class gastm_UnaryExpression(Expression):

    pass
class gastm_AggregateExpression(Expression):

    pass
class SwitchCase:

    pass
class gastm_DefaultBlock(SwitchCase):

    pass
class gastm_CaseBlock(SwitchCase):

    pass
class LoopStatement:

    pass
class gastm_DoWhileStatement(LoopStatement):

    pass
class gastm_ForStatement(LoopStatement):

    pass
class gastm_WhileStatement(LoopStatement):

    pass
class gastm_LabelAccess(Expression):

    pass
class Statement:

    pass
class gastm_TerminateStatement(Statement):

    pass
class gastm_ReturnStatement(Statement):

    pass
class gastm_JumpStatement(Statement):

    pass
class gastm_DeleteStatement(Statement):

    pass
class gastm_SwitchStatement(Statement):

    pass
class gastm_DeclarationOrDefinitionStatement(Statement):

    pass
class gastm_ContinueStatement(Statement):

    pass
class gastm_ThrowStatement(Statement):

    pass
class gastm_BreakStatement(Statement):

    pass
class gastm_TryStatement(Statement):

    pass
class gastm_LoopStatement(Statement):

    pass
class gastm_ExpressionStatement(Statement):

    pass
class TypeReference:

    pass
class gastm_UnnamedTypeReference(TypeReference):

    pass
class AccessKind:

    pass
class gastm_Private(AccessKind):

    pass
class gastm_Protected(AccessKind):

    pass
class gastm_Public(AccessKind):

    pass
class gastm_IfStatement(Statement):

    pass
class gastm_EmptyStatement(Statement):

    pass
class gastm_BlockStatement(Statement):

    pass
class gastm_LabeledStatement(Statement):

    pass
class ConstructedType:

    pass
class gastm_CollectionType(ConstructedType):

    pass
class RealType:

    pass
class gastm_LongDouble(RealType):

    pass
class gastm_Double(RealType):

    pass
class gastm_Real(RealType):

    pass
class IntegerLiteral:

    pass
class gastm_Integer(IntegerLiteral):

    pass
class IntegralType:

    pass
class gastm_LongInteger(IntegralType):

    pass
class gastm_ShortInteger(IntegralType):

    pass
class NumberType:

    pass
class gastm_Character(NumberType):

    pass
class gastm_RealType(NumberType):

    def __init__(self, precision: str):
        self.precision = precision
        
    @property
    def precision(self) -> str:
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision

class gastm_Byte(NumberType):

    pass
class gastm_IntegralType(NumberType):

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class PrimitiveType:

    pass
class gastm_Boolean(PrimitiveType):

    pass
class gastm_Void(PrimitiveType):

    pass
class gastm_NumberType(PrimitiveType):

    def __init__(self, isSigned: str):
        self.isSigned = isSigned
        
    @property
    def isSigned(self) -> str:
        return self.__isSigned

    @isSigned.setter
    def isSigned(self, isSigned: str):
        self.__isSigned = isSigned

class FormalParameterType:

    pass
class gastm_ByReferenceFormalParameterType(FormalParameterType):

    pass
class gastm_ByValueFormalParameterType(FormalParameterType):

    pass
class AggregateType:

    pass
class gastm_AnnotationType(AggregateType):

    pass
class gastm_UnionType(AggregateType):

    pass
class gastm_ClassType(AggregateType):

    pass
class gastm_StructureType(AggregateType):

    pass
class gastm_ArrayType(ConstructedType):

    pass
class gastm_RangeType(ConstructedType):

    pass
class gastm_ReferenceType(ConstructedType):

    pass
class gastm_PointerType(ConstructedType):

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class DataType:

    pass
class gastm_ConstructedType(DataType):

    pass
class gastm_PrimitiveType(DataType):

    pass
class gastm_ExceptionType(DataType):

    pass
class PreprocessorElement:

    pass
class gastm_MacroCall(PreprocessorElement):

    pass
class gastm_IncludeUnit(PreprocessorElement):

    pass
class TypeDeclaration:

    pass
class gastm_EnumTypeDeclaration(TypeDeclaration):

    pass
class gastm_AggregateTypeDeclaration(TypeDeclaration):

    pass
class gastm_EnumType(DataType):

    pass
class gastm_AggregateType(DataType):

    pass
class gastm_NamedType(DataType):

    pass
class TypeDefinition:

    pass
class gastm_AggregateTypeDefinition(TypeDefinition):

    pass
class gastm_EnumTypeDefinition(TypeDefinition):

    pass
class gastm_NamedTypeDefinition(TypeDefinition):

    pass
class gastm_FormalParameterType(DataType):

    pass
class Type:

    pass
class gastm_DataType(Type):

    pass
class gastm_FunctionType(Type):

    pass
class gastm_Comment(PreprocessorElement):

    def __init__(self, body: str):
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class gastm_MacroDefinition(PreprocessorElement):

    def __init__(self, macroName: str, body: str, gastm_MacroDefinition: "gastm_MacroCall" = None):
        self.macroName = macroName
        self.body = body
        self.gastm_MacroDefinition = gastm_MacroDefinition
        
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
    def gastm_MacroDefinition(self):
        return self.__gastm_MacroDefinition

    @gastm_MacroDefinition.setter
    def gastm_MacroDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_MacroDefinition__gastm_MacroDefinition", None)
        self.__gastm_MacroDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_MacroCall"):
                opp_val = getattr(old_value, "gastm_MacroCall", None)
                if opp_val == self:
                    setattr(old_value, "gastm_MacroCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_MacroCall"):
                opp_val = getattr(value, "gastm_MacroCall", None)
                setattr(value, "gastm_MacroCall", self)

class Declaration:

    pass
class gastm_VariableDeclaration(Declaration):

    def __init__(self, isMutable: str):
        self.isMutable = isMutable
        
    @property
    def isMutable(self) -> str:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: str):
        self.__isMutable = isMutable

class gastm_FormalParameterDeclaration(Declaration):

    pass
class gastm_FunctionDeclaration(Declaration):

    pass
class DataDefinition:

    pass
class gastm_BitFieldDefinition(DataDefinition):

    pass
class gastm_VariableDefinition(DataDefinition):

    pass
class VirtualSpecification:

    pass
class gastm_Virtual(VirtualSpecification):

    pass
class StorageSpecification:

    pass
class gastm_PerClassMember(StorageSpecification):

    pass
class gastm_NoDef(StorageSpecification):

    pass
class gastm_FunctionPersistent(StorageSpecification):

    pass
class gastm_FileLocal(StorageSpecification):

    pass
class gastm_External(StorageSpecification):

    pass
class DeclarationOrDefinition:

    pass
class gastm_Declaration(DeclarationOrDefinition):

    pass
class gastm_Definition(DeclarationOrDefinition):

    pass
class gastm_LabelType(Type):

    pass
class gastm_FormalParameterDefinition(DataDefinition):

    pass
class Definition:

    pass
class gastm_DataDefinition(Definition):

    def __init__(self, isMutable: str, gastm_DataDefinition: "gastm_Expression" = None, gastm_DataDefinition197: "gastm_VariableCatchBlock" = None):
        self.isMutable = isMutable
        self.gastm_DataDefinition = gastm_DataDefinition
        self.gastm_DataDefinition197 = gastm_DataDefinition197
        
    @property
    def isMutable(self) -> str:
        return self.__isMutable

    @isMutable.setter
    def isMutable(self, isMutable: str):
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
            if hasattr(old_value, "gastm_Expression91"):
                opp_val = getattr(old_value, "gastm_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "gastm_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_Expression91"):
                opp_val = getattr(value, "gastm_Expression91", None)
                setattr(value, "gastm_Expression91", self)

    @property
    def gastm_DataDefinition197(self):
        return self.__gastm_DataDefinition197

    @gastm_DataDefinition197.setter
    def gastm_DataDefinition197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_DataDefinition__gastm_DataDefinition197", None)
        self.__gastm_DataDefinition197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_VariableCatchBlock"):
                opp_val = getattr(old_value, "gastm_VariableCatchBlock", None)
                if opp_val == self:
                    setattr(old_value, "gastm_VariableCatchBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_VariableCatchBlock"):
                opp_val = getattr(value, "gastm_VariableCatchBlock", None)
                setattr(value, "gastm_VariableCatchBlock", self)

class gastm_EntryDefinition(Definition):

    pass
class gastm_EnumLiteralDefinition(Definition):

    pass
class gastm_FunctionDefinition(Definition):

    pass
class DefinitionObject:

    pass
class gastm_TypeDeclaration(DefinitionObject):

    pass
class gastm_DeclarationOrDefinition(DefinitionObject):

    def __init__(self, linkageSpecifier: str, gastm_DeclarationOrDefinition: "gastm_StorageSpecification" = None, gastm_DeclarationOrDefinition44: "gastm_AccessKind" = None):
        self.linkageSpecifier = linkageSpecifier
        self.gastm_DeclarationOrDefinition = gastm_DeclarationOrDefinition
        self.gastm_DeclarationOrDefinition44 = gastm_DeclarationOrDefinition44
        
    @property
    def linkageSpecifier(self) -> str:
        return self.__linkageSpecifier

    @linkageSpecifier.setter
    def linkageSpecifier(self, linkageSpecifier: str):
        self.__linkageSpecifier = linkageSpecifier

    @property
    def gastm_DeclarationOrDefinition44(self):
        return self.__gastm_DeclarationOrDefinition44

    @gastm_DeclarationOrDefinition44.setter
    def gastm_DeclarationOrDefinition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_DeclarationOrDefinition__gastm_DeclarationOrDefinition44", None)
        self.__gastm_DeclarationOrDefinition44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_AccessKind45"):
                opp_val = getattr(old_value, "gastm_AccessKind45", None)
                if opp_val == self:
                    setattr(old_value, "gastm_AccessKind45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_AccessKind45"):
                opp_val = getattr(value, "gastm_AccessKind45", None)
                setattr(value, "gastm_AccessKind45", self)

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
            if hasattr(old_value, "gastm_StorageSpecification"):
                opp_val = getattr(old_value, "gastm_StorageSpecification", None)
                if opp_val == self:
                    setattr(old_value, "gastm_StorageSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_StorageSpecification"):
                opp_val = getattr(value, "gastm_StorageSpecification", None)
                setattr(value, "gastm_StorageSpecification", self)

class gastm_NamedTypeReference(TypeReference):

    pass
class gastm_LabelDefinition(DefinitionObject):

    pass
class gastm_NameSpaceType(Type):

    pass
class gastm_NameSpaceDefinition(DefinitionObject):

    pass
class gastm_TypeDefinition(DefinitionObject):

    pass
class MinorSyntaxObject:

    pass
class gastm_MemberObject(MinorSyntaxObject):

    def __init__(self, offset: str, gastm_MemberObject: "gastm_DefinitionObject" = None, gastm_MemberObject117: "gastm_AggregateType" = None):
        self.offset = offset
        self.gastm_MemberObject = gastm_MemberObject
        self.gastm_MemberObject117 = gastm_MemberObject117
        
    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def gastm_MemberObject(self):
        return self.__gastm_MemberObject

    @gastm_MemberObject.setter
    def gastm_MemberObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_MemberObject__gastm_MemberObject", None)
        self.__gastm_MemberObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_DefinitionObject41"):
                opp_val = getattr(old_value, "gastm_DefinitionObject41", None)
                if opp_val == self:
                    setattr(old_value, "gastm_DefinitionObject41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_DefinitionObject41"):
                opp_val = getattr(value, "gastm_DefinitionObject41", None)
                setattr(value, "gastm_DefinitionObject41", self)

    @property
    def gastm_MemberObject117(self):
        return self.__gastm_MemberObject117

    @gastm_MemberObject117.setter
    def gastm_MemberObject117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_MemberObject__gastm_MemberObject117", None)
        self.__gastm_MemberObject117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_AggregateType116"):
                opp_val = getattr(old_value, "gastm_AggregateType116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_AggregateType116"):
                opp_val = getattr(value, "gastm_AggregateType116", None)
                if opp_val is None:
                    setattr(value, "gastm_AggregateType116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gastm_SwitchCase(MinorSyntaxObject):

    def __init__(self, isEvaluateAllCases: str, gastm_SwitchCase: set["gastm_Statement"] = None, gastm_SwitchCase165: "gastm_SwitchStatement" = None):
        self.isEvaluateAllCases = isEvaluateAllCases
        self.gastm_SwitchCase = gastm_SwitchCase if gastm_SwitchCase is not None else set()
        self.gastm_SwitchCase165 = gastm_SwitchCase165
        
    @property
    def isEvaluateAllCases(self) -> str:
        return self.__isEvaluateAllCases

    @isEvaluateAllCases.setter
    def isEvaluateAllCases(self, isEvaluateAllCases: str):
        self.__isEvaluateAllCases = isEvaluateAllCases

    @property
    def gastm_SwitchCase165(self):
        return self.__gastm_SwitchCase165

    @gastm_SwitchCase165.setter
    def gastm_SwitchCase165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_SwitchCase__gastm_SwitchCase165", None)
        self.__gastm_SwitchCase165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_SwitchStatement164"):
                opp_val = getattr(old_value, "gastm_SwitchStatement164", None)
                if opp_val == self:
                    setattr(old_value, "gastm_SwitchStatement164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_SwitchStatement164"):
                opp_val = getattr(value, "gastm_SwitchStatement164", None)
                setattr(value, "gastm_SwitchStatement164", self)

    @property
    def gastm_SwitchCase(self):
        return self.__gastm_SwitchCase

    @gastm_SwitchCase.setter
    def gastm_SwitchCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_SwitchCase__gastm_SwitchCase", None)
        self.__gastm_SwitchCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gastm_Statement"):
                    opp_val = getattr(item, "gastm_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "gastm_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gastm_Statement"):
                    opp_val = getattr(item, "gastm_Statement", None)
                    
                    setattr(item, "gastm_Statement", self)
                    

class gastm_CatchBlock(MinorSyntaxObject):

    pass
class gastm_DerivesFrom(MinorSyntaxObject):

    pass
class gastm_Name(MinorSyntaxObject):

    def __init__(self, nameString: str, gastm_Name: "gastm_TypeDefinition" = None, gastm_Name48: "gastm_NameSpaceDefinition" = None, gastm_Name55: "gastm_LabelDefinition" = None, gastm_Name61: "gastm_Definition" = None, gastm_Name69: "gastm_Declaration" = None, gastm_Name133: "gastm_NamedTypeReference" = None, gastm_Name239: "gastm_NameReference" = None, gastm_Name245: "gastm_LabelAccess" = None):
        self.nameString = nameString
        self.gastm_Name = gastm_Name
        self.gastm_Name48 = gastm_Name48
        self.gastm_Name55 = gastm_Name55
        self.gastm_Name61 = gastm_Name61
        self.gastm_Name69 = gastm_Name69
        self.gastm_Name133 = gastm_Name133
        self.gastm_Name239 = gastm_Name239
        self.gastm_Name245 = gastm_Name245
        
    @property
    def nameString(self) -> str:
        return self.__nameString

    @nameString.setter
    def nameString(self, nameString: str):
        self.__nameString = nameString

    @property
    def gastm_Name(self):
        return self.__gastm_Name

    @gastm_Name.setter
    def gastm_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name", None)
        self.__gastm_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_TypeDefinition"):
                opp_val = getattr(old_value, "gastm_TypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "gastm_TypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_TypeDefinition"):
                opp_val = getattr(value, "gastm_TypeDefinition", None)
                setattr(value, "gastm_TypeDefinition", self)

    @property
    def gastm_Name239(self):
        return self.__gastm_Name239

    @gastm_Name239.setter
    def gastm_Name239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name239", None)
        self.__gastm_Name239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_NameReference"):
                opp_val = getattr(old_value, "gastm_NameReference", None)
                if opp_val == self:
                    setattr(old_value, "gastm_NameReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_NameReference"):
                opp_val = getattr(value, "gastm_NameReference", None)
                setattr(value, "gastm_NameReference", self)

    @property
    def gastm_Name133(self):
        return self.__gastm_Name133

    @gastm_Name133.setter
    def gastm_Name133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name133", None)
        self.__gastm_Name133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_NamedTypeReference132"):
                opp_val = getattr(old_value, "gastm_NamedTypeReference132", None)
                if opp_val == self:
                    setattr(old_value, "gastm_NamedTypeReference132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_NamedTypeReference132"):
                opp_val = getattr(value, "gastm_NamedTypeReference132", None)
                setattr(value, "gastm_NamedTypeReference132", self)

    @property
    def gastm_Name48(self):
        return self.__gastm_Name48

    @gastm_Name48.setter
    def gastm_Name48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name48", None)
        self.__gastm_Name48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_NameSpaceDefinition"):
                opp_val = getattr(old_value, "gastm_NameSpaceDefinition", None)
                if opp_val == self:
                    setattr(old_value, "gastm_NameSpaceDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_NameSpaceDefinition"):
                opp_val = getattr(value, "gastm_NameSpaceDefinition", None)
                setattr(value, "gastm_NameSpaceDefinition", self)

    @property
    def gastm_Name55(self):
        return self.__gastm_Name55

    @gastm_Name55.setter
    def gastm_Name55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name55", None)
        self.__gastm_Name55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_LabelDefinition"):
                opp_val = getattr(old_value, "gastm_LabelDefinition", None)
                if opp_val == self:
                    setattr(old_value, "gastm_LabelDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_LabelDefinition"):
                opp_val = getattr(value, "gastm_LabelDefinition", None)
                setattr(value, "gastm_LabelDefinition", self)

    @property
    def gastm_Name69(self):
        return self.__gastm_Name69

    @gastm_Name69.setter
    def gastm_Name69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name69", None)
        self.__gastm_Name69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_Declaration68"):
                opp_val = getattr(old_value, "gastm_Declaration68", None)
                if opp_val == self:
                    setattr(old_value, "gastm_Declaration68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_Declaration68"):
                opp_val = getattr(value, "gastm_Declaration68", None)
                setattr(value, "gastm_Declaration68", self)

    @property
    def gastm_Name61(self):
        return self.__gastm_Name61

    @gastm_Name61.setter
    def gastm_Name61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name61", None)
        self.__gastm_Name61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_Definition"):
                opp_val = getattr(old_value, "gastm_Definition", None)
                if opp_val == self:
                    setattr(old_value, "gastm_Definition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_Definition"):
                opp_val = getattr(value, "gastm_Definition", None)
                setattr(value, "gastm_Definition", self)

    @property
    def gastm_Name245(self):
        return self.__gastm_Name245

    @gastm_Name245.setter
    def gastm_Name245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Name__gastm_Name245", None)
        self.__gastm_Name245 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_LabelAccess244"):
                opp_val = getattr(old_value, "gastm_LabelAccess244", None)
                if opp_val == self:
                    setattr(old_value, "gastm_LabelAccess244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_LabelAccess244"):
                opp_val = getattr(value, "gastm_LabelAccess244", None)
                setattr(value, "gastm_LabelAccess244", self)

class gastm_Dimension(MinorSyntaxObject):

    pass
class gastm_TypeReference(Type):

    pass
class gastm_FunctionMemberAttributes(MinorSyntaxObject):

    def __init__(self, isFriend: str, isInLine: str, isThisConst: str, gastm_FunctionMemberAttributes: "gastm_VirtualSpecification" = None, gastm_FunctionMemberAttributes82: "gastm_FunctionDefinition" = None, gastm_FunctionMemberAttributes97: "gastm_FunctionDeclaration" = None):
        self.isFriend = isFriend
        self.isInLine = isInLine
        self.isThisConst = isThisConst
        self.gastm_FunctionMemberAttributes = gastm_FunctionMemberAttributes
        self.gastm_FunctionMemberAttributes82 = gastm_FunctionMemberAttributes82
        self.gastm_FunctionMemberAttributes97 = gastm_FunctionMemberAttributes97
        
    @property
    def isFriend(self) -> str:
        return self.__isFriend

    @isFriend.setter
    def isFriend(self, isFriend: str):
        self.__isFriend = isFriend

    @property
    def isThisConst(self) -> str:
        return self.__isThisConst

    @isThisConst.setter
    def isThisConst(self, isThisConst: str):
        self.__isThisConst = isThisConst

    @property
    def isInLine(self) -> str:
        return self.__isInLine

    @isInLine.setter
    def isInLine(self, isInLine: str):
        self.__isInLine = isInLine

    @property
    def gastm_FunctionMemberAttributes97(self):
        return self.__gastm_FunctionMemberAttributes97

    @gastm_FunctionMemberAttributes97.setter
    def gastm_FunctionMemberAttributes97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_FunctionMemberAttributes__gastm_FunctionMemberAttributes97", None)
        self.__gastm_FunctionMemberAttributes97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_FunctionDeclaration96"):
                opp_val = getattr(old_value, "gastm_FunctionDeclaration96", None)
                if opp_val == self:
                    setattr(old_value, "gastm_FunctionDeclaration96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_FunctionDeclaration96"):
                opp_val = getattr(value, "gastm_FunctionDeclaration96", None)
                setattr(value, "gastm_FunctionDeclaration96", self)

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
            if hasattr(old_value, "gastm_VirtualSpecification"):
                opp_val = getattr(old_value, "gastm_VirtualSpecification", None)
                if opp_val == self:
                    setattr(old_value, "gastm_VirtualSpecification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_VirtualSpecification"):
                opp_val = getattr(value, "gastm_VirtualSpecification", None)
                setattr(value, "gastm_VirtualSpecification", self)

    @property
    def gastm_FunctionMemberAttributes82(self):
        return self.__gastm_FunctionMemberAttributes82

    @gastm_FunctionMemberAttributes82.setter
    def gastm_FunctionMemberAttributes82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_FunctionMemberAttributes__gastm_FunctionMemberAttributes82", None)
        self.__gastm_FunctionMemberAttributes82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_FunctionDefinition81"):
                opp_val = getattr(old_value, "gastm_FunctionDefinition81", None)
                if opp_val == self:
                    setattr(old_value, "gastm_FunctionDefinition81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_FunctionDefinition81"):
                opp_val = getattr(value, "gastm_FunctionDefinition81", None)
                setattr(value, "gastm_FunctionDefinition81", self)

class gastm_ActualParameter(MinorSyntaxObject):

    pass
class gastm_AccessKind(MinorSyntaxObject):

    pass
class gastm_VirtualSpecification(MinorSyntaxObject):

    pass
class gastm_StorageSpecification(MinorSyntaxObject):

    pass
class gastm_BinaryOperator(MinorSyntaxObject):

    pass
class gastm_UnaryOperator(MinorSyntaxObject):

    pass
class GASTMSemanticObject:

    pass
class gastm_Scope(GASTMSemanticObject):

    pass
class gastm_Project(GASTMSemanticObject):

    pass
class GASTMSyntaxObject:

    pass
class gastm_Expression(GASTMSyntaxObject):

    pass
class gastm_Type(GASTMSyntaxObject):

    def __init__(self, isConst: str, gastm_Type: "gastm_NamedType" = None, gastm_Type130: "gastm_UnnamedTypeReference" = None, gastm_Type195: "gastm_TypesCatchBlock" = None):
        self.isConst = isConst
        self.gastm_Type = gastm_Type
        self.gastm_Type130 = gastm_Type130
        self.gastm_Type195 = gastm_Type195
        
    @property
    def isConst(self) -> str:
        return self.__isConst

    @isConst.setter
    def isConst(self, isConst: str):
        self.__isConst = isConst

    @property
    def gastm_Type(self):
        return self.__gastm_Type

    @gastm_Type.setter
    def gastm_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Type__gastm_Type", None)
        self.__gastm_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_NamedType124"):
                opp_val = getattr(old_value, "gastm_NamedType124", None)
                if opp_val == self:
                    setattr(old_value, "gastm_NamedType124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_NamedType124"):
                opp_val = getattr(value, "gastm_NamedType124", None)
                setattr(value, "gastm_NamedType124", self)

    @property
    def gastm_Type130(self):
        return self.__gastm_Type130

    @gastm_Type130.setter
    def gastm_Type130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Type__gastm_Type130", None)
        self.__gastm_Type130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_UnnamedTypeReference"):
                opp_val = getattr(old_value, "gastm_UnnamedTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "gastm_UnnamedTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_UnnamedTypeReference"):
                opp_val = getattr(value, "gastm_UnnamedTypeReference", None)
                setattr(value, "gastm_UnnamedTypeReference", self)

    @property
    def gastm_Type195(self):
        return self.__gastm_Type195

    @gastm_Type195.setter
    def gastm_Type195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_Type__gastm_Type195", None)
        self.__gastm_Type195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_TypesCatchBlock"):
                opp_val = getattr(old_value, "gastm_TypesCatchBlock", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_TypesCatchBlock"):
                opp_val = getattr(value, "gastm_TypesCatchBlock", None)
                if opp_val is None:
                    setattr(value, "gastm_TypesCatchBlock", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gastm_MinorSyntaxObject(GASTMSyntaxObject):

    pass
class gastm_Statement(GASTMSyntaxObject):

    pass
class gastm_DefinitionObject(GASTMSyntaxObject):

    pass
class Scope:

    pass
class gastm_FunctionScope(Scope):

    pass
class gastm_BlockScope(Scope):

    pass
class gastm_ProgramScope(Scope):

    pass
class gastm_GlobalScope(Scope):

    pass
class gastm_AggregateScope(Scope):

    pass
class gastm_AnnotationExpression(Expression):

    pass
class gastm_PreprocessorElement(GASTMSyntaxObject):

    pass
class GASTMObject:

    pass
class gastm_GASTMSyntaxObject(GASTMObject):

    pass
class gastm_GASTMSemanticObject(GASTMObject):

    pass
class gastm_GASTMSourceObject(GASTMObject):

    pass
class gastm_GASTMObject:

    pass
class SourceFile:

    pass
class gastm_SourceFileReference(SourceFile):

    pass
class gastm_CompilationUnit(SourceFile):

    def __init__(self, language: str, gastm_CompilationUnit: set["gastm_DefinitionObject"] = None, gastm_CompilationUnit9: "gastm_ProgramScope" = None, gastm_CompilationUnit16: "gastm_Project" = None):
        self.language = language
        self.gastm_CompilationUnit = gastm_CompilationUnit if gastm_CompilationUnit is not None else set()
        self.gastm_CompilationUnit9 = gastm_CompilationUnit9
        self.gastm_CompilationUnit16 = gastm_CompilationUnit16
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def gastm_CompilationUnit9(self):
        return self.__gastm_CompilationUnit9

    @gastm_CompilationUnit9.setter
    def gastm_CompilationUnit9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_CompilationUnit__gastm_CompilationUnit9", None)
        self.__gastm_CompilationUnit9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_ProgramScope"):
                opp_val = getattr(old_value, "gastm_ProgramScope", None)
                if opp_val == self:
                    setattr(old_value, "gastm_ProgramScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_ProgramScope"):
                opp_val = getattr(value, "gastm_ProgramScope", None)
                setattr(value, "gastm_ProgramScope", self)

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
                if hasattr(item, "gastm_DefinitionObject"):
                    opp_val = getattr(item, "gastm_DefinitionObject", None)
                    
                    if opp_val == self:
                        setattr(item, "gastm_DefinitionObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gastm_DefinitionObject"):
                    opp_val = getattr(item, "gastm_DefinitionObject", None)
                    
                    setattr(item, "gastm_DefinitionObject", self)
                    

    @property
    def gastm_CompilationUnit16(self):
        return self.__gastm_CompilationUnit16

    @gastm_CompilationUnit16.setter
    def gastm_CompilationUnit16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_CompilationUnit__gastm_CompilationUnit16", None)
        self.__gastm_CompilationUnit16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_Project"):
                opp_val = getattr(old_value, "gastm_Project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_Project"):
                opp_val = getattr(value, "gastm_Project", None)
                if opp_val is None:
                    setattr(value, "gastm_Project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GASTMSourceObject:

    pass
class gastm_SourceLocation(GASTMSourceObject):

    def __init__(self, startLine: str, startPosition: str, endLine: str, endPosition: str, gastm_SourceLocation6: "gastm_SourceFile" = None, gastm_SourceLocation: "gastm_GASTMSyntaxObject" = None, gastm_SourceLocation11: "gastm_SourceFileReference" = None):
        self.startLine = startLine
        self.startPosition = startPosition
        self.endLine = endLine
        self.endPosition = endPosition
        self.gastm_SourceLocation6 = gastm_SourceLocation6
        self.gastm_SourceLocation = gastm_SourceLocation
        self.gastm_SourceLocation11 = gastm_SourceLocation11
        
    @property
    def endPosition(self) -> str:
        return self.__endPosition

    @endPosition.setter
    def endPosition(self, endPosition: str):
        self.__endPosition = endPosition

    @property
    def startPosition(self) -> str:
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: str):
        self.__startPosition = startPosition

    @property
    def startLine(self) -> str:
        return self.__startLine

    @startLine.setter
    def startLine(self, startLine: str):
        self.__startLine = startLine

    @property
    def endLine(self) -> str:
        return self.__endLine

    @endLine.setter
    def endLine(self, endLine: str):
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
            if hasattr(old_value, "gastm_GASTMSyntaxObject"):
                opp_val = getattr(old_value, "gastm_GASTMSyntaxObject", None)
                if opp_val == self:
                    setattr(old_value, "gastm_GASTMSyntaxObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_GASTMSyntaxObject"):
                opp_val = getattr(value, "gastm_GASTMSyntaxObject", None)
                setattr(value, "gastm_GASTMSyntaxObject", self)

    @property
    def gastm_SourceLocation6(self):
        return self.__gastm_SourceLocation6

    @gastm_SourceLocation6.setter
    def gastm_SourceLocation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_SourceLocation__gastm_SourceLocation6", None)
        self.__gastm_SourceLocation6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_SourceFile"):
                opp_val = getattr(old_value, "gastm_SourceFile", None)
                if opp_val == self:
                    setattr(old_value, "gastm_SourceFile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_SourceFile"):
                opp_val = getattr(value, "gastm_SourceFile", None)
                setattr(value, "gastm_SourceFile", self)

    @property
    def gastm_SourceLocation11(self):
        return self.__gastm_SourceLocation11

    @gastm_SourceLocation11.setter
    def gastm_SourceLocation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_SourceLocation__gastm_SourceLocation11", None)
        self.__gastm_SourceLocation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_SourceFileReference"):
                opp_val = getattr(old_value, "gastm_SourceFileReference", None)
                if opp_val == self:
                    setattr(old_value, "gastm_SourceFileReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_SourceFileReference"):
                opp_val = getattr(value, "gastm_SourceFileReference", None)
                setattr(value, "gastm_SourceFileReference", self)

class gastm_SourceFile(GASTMSourceObject):

    def __init__(self, path: str, gastm_SourceFile: "gastm_SourceLocation" = None, gastm_SourceFile14: "gastm_SourceFileReference" = None):
        self.path = path
        self.gastm_SourceFile = gastm_SourceFile
        self.gastm_SourceFile14 = gastm_SourceFile14
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def gastm_SourceFile14(self):
        return self.__gastm_SourceFile14

    @gastm_SourceFile14.setter
    def gastm_SourceFile14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_SourceFile__gastm_SourceFile14", None)
        self.__gastm_SourceFile14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_SourceFileReference13"):
                opp_val = getattr(old_value, "gastm_SourceFileReference13", None)
                if opp_val == self:
                    setattr(old_value, "gastm_SourceFileReference13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_SourceFileReference13"):
                opp_val = getattr(value, "gastm_SourceFileReference13", None)
                setattr(value, "gastm_SourceFileReference13", self)

    @property
    def gastm_SourceFile(self):
        return self.__gastm_SourceFile

    @gastm_SourceFile.setter
    def gastm_SourceFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gastm_SourceFile__gastm_SourceFile", None)
        self.__gastm_SourceFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gastm_SourceLocation6"):
                opp_val = getattr(old_value, "gastm_SourceLocation6", None)
                if opp_val == self:
                    setattr(old_value, "gastm_SourceLocation6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gastm_SourceLocation6"):
                opp_val = getattr(value, "gastm_SourceLocation6", None)
                setattr(value, "gastm_SourceLocation6", self)
