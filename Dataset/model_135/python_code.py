from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class TMethodCall:

    pass
class TUnaryOperator:

    pass
class simTL4J_simTL_TUnaryOperatorNOT(TUnaryOperator):

    pass
class simTL_TPlaceholder:

    pass
class simTL4J_simTL_TPlaceholder:

    pass
class simTL_TIf:

    pass
class simTL_TFor:

    pass
class simTL4J_simTL_TAbstractMethodStatement:

    pass
class simTL4J_simTL_TMethodCall:

    def __init__(self, methodName: str, params: str):
        self.methodName = methodName
        self.params = params
        
    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

class TForVariable:

    pass
class simTL4J_simTL_TModelImport:

    def __init__(self, uri: str, name: str):
        self.uri = uri
        self.name = name
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class simTL4J_simTL_TFor(ABC):

    pass
class TModelImport:

    pass
class simTL4J_simTL_TemplateHeader:

    pass
class TemplateHeader:

    pass
class simTL4J_simTL_Template:

    pass
class simTL4J_simTL_TForVariable:

    def __init__(self, name: str, simTL4J_simTL_TForVariable: "TAbstractMethodStatement" = None):
        self.name = name
        self.simTL4J_simTL_TForVariable = simTL4J_simTL_TForVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simTL4J_simTL_TForVariable(self):
        return self.__simTL4J_simTL_TForVariable

    @simTL4J_simTL_TForVariable.setter
    def simTL4J_simTL_TForVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_simTL_TForVariable__simTL4J_simTL_TForVariable", None)
        self.__simTL4J_simTL_TForVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TAbstractMethodStatement171"):
                opp_val = getattr(old_value, "TAbstractMethodStatement171", None)
                if opp_val == self:
                    setattr(old_value, "TAbstractMethodStatement171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TAbstractMethodStatement171"):
                opp_val = getattr(value, "TAbstractMethodStatement171", None)
                setattr(value, "TAbstractMethodStatement171", self)

class TAbstractMethodStatement:

    pass
class simTL4J_simTL_TMethodStatementImpl(TAbstractMethodStatement):

    def __init__(self, caller: str, simTL4J_simTL_TMethodStatementImpl: set["TMethodCall"] = None, TAbstractMethodStatement177: "simTL4J_simTL_TPlaceholder", TAbstractMethodStatement: "simTL4J_simTL_TIf", TAbstractMethodStatement179: "simTL4J_simTL_TUnaryOperator", TAbstractMethodStatement171: "simTL4J_simTL_TForVariable"):
        self.caller = caller
        self.simTL4J_simTL_TMethodStatementImpl = simTL4J_simTL_TMethodStatementImpl if simTL4J_simTL_TMethodStatementImpl is not None else set()
        
    @property
    def caller(self) -> str:
        return self.__caller

    @caller.setter
    def caller(self, caller: str):
        self.__caller = caller

    @property
    def simTL4J_simTL_TMethodStatementImpl(self):
        return self.__simTL4J_simTL_TMethodStatementImpl

    @simTL4J_simTL_TMethodStatementImpl.setter
    def simTL4J_simTL_TMethodStatementImpl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_simTL_TMethodStatementImpl__simTL4J_simTL_TMethodStatementImpl", None)
        self.__simTL4J_simTL_TMethodStatementImpl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TMethodCall"):
                    opp_val = getattr(item, "TMethodCall", None)
                    
                    if opp_val == self:
                        setattr(item, "TMethodCall", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TMethodCall"):
                    opp_val = getattr(item, "TMethodCall", None)
                    
                    setattr(item, "TMethodCall", self)
                    

class simTL4J_simTL_TUnaryOperator(TAbstractMethodStatement):

    pass
class simTL4J_simTL_TIf(ABC):

    pass
class AdditionalLocalVariable:

    pass
class statements_ForLoopInitializer:

    pass
class ClassifierReference:

    pass
class types_TypeReference:

    pass
class CatchBlock:

    pass
class Block:

    pass
class statements_SwitchCase:

    pass
class LocalVariable:

    pass
class JumpLabel:

    pass
class WhileLoop:

    pass
class simTL4J_statements_DoWhileLoop(WhileLoop):

    pass
class SwitchCase:

    pass
class simTL4J_statements_DefaultSwitchCase(SwitchCase):

    pass
class statements_StatementContainer:

    pass
class OrdinaryParameter:

    pass
class modifiers_Modifiable:

    pass
class Jump:

    pass
class simTL4J_statements_Continue(Jump):

    pass
class simTL4J_statements_Break(Jump):

    pass
class statements_Conditional:

    pass
class simTL4J_statements_NormalSwitchCase(statements_SwitchCase, statements_Conditional):

    pass
class StatementListContainer:

    pass
class simTL4J_statements_CatchBlock(StatementListContainer):

    pass
class simTL4J_statements_SwitchCase(StatementListContainer):

    pass
class Statement:

    pass
class simTL4J_statements_ExpressionStatement(Statement):

    pass
class simTL4J_statements_EmptyStatement(Statement):

    pass
class simTL4J_statements_LocalVariableStatement(Statement):

    pass
class simTL4J_statements_Jump(Statement):

    pass
class simTL4J_statements_Throw(Statement):

    pass
class simTL4J_statements_Switch(Statement):

    pass
class simTL4J_statements_Return(Statement):

    pass
class PrimitiveType:

    pass
class simTL4J_types_Int(PrimitiveType):

    pass
class simTL4J_types_Byte(PrimitiveType):

    pass
class simTL4J_types_Void(PrimitiveType):

    pass
class simTL4J_types_Short(PrimitiveType):

    pass
class simTL4J_types_Long(PrimitiveType):

    pass
class simTL4J_types_Float(PrimitiveType):

    pass
class simTL4J_types_Char(PrimitiveType):

    pass
class simTL4J_types_Double(PrimitiveType):

    pass
class simTL4J_types_Boolean(PrimitiveType):

    pass
class references_ElementReference:

    pass
class ElementReference:

    pass
class simTL4J_references_IdentifierReference(ElementReference):

    pass
class ArraySelector:

    pass
class expressions_PrimaryExpression:

    pass
class simTL4J_simTL_TPlaceholder_PrimaryExpression(expressions_PrimaryExpression, simTL_TPlaceholder):

    pass
class Parameter:

    pass
class simTL4J_parameters_VariableLengthParameter(Parameter):

    pass
class simTL4J_parameters_OrdinaryParameter(Parameter):

    pass
class operators_UnaryOperator:

    pass
class operators_AdditiveOperator:

    pass
class simTL4J_operators_Subtraction(operators_UnaryOperator, operators_AdditiveOperator):

    pass
class simTL4J_operators_Addition(operators_UnaryOperator, operators_AdditiveOperator):

    pass
class Operator:

    pass
class simTL4J_operators_MultiplicativeOperator(Operator):

    pass
class simTL4J_operators_UnaryModificationOperator(Operator):

    pass
class simTL4J_operators_UnaryOperator(Operator):

    pass
class simTL4J_operators_AssignmentOperator(Operator):

    pass
class simTL4J_operators_ShiftOperator(Operator):

    pass
class simTL4J_operators_RelationOperator(Operator):

    pass
class simTL4J_operators_EqualityOperator(Operator):

    pass
class simTL4J_operators_AdditiveOperator(Operator):

    pass
class members_Method:

    pass
class Method:

    pass
class simTL4J_members_InterfaceMethod(Method):

    pass
class Modifier:

    pass
class simTL4J_modifiers_Abstract(Modifier):

    pass
class simTL4J_modifiers_Protected(Modifier):

    pass
class simTL4J_modifiers_Native(Modifier):

    pass
class simTL4J_modifiers_Static(Modifier):

    pass
class simTL4J_modifiers_Synchronized(Modifier):

    pass
class simTL4J_modifiers_Private(Modifier):

    pass
class simTL4J_modifiers_Public(Modifier):

    pass
class simTL4J_modifiers_Final(Modifier):

    pass
class simTL4J_modifiers_Transient(Modifier):

    pass
class simTL4J_modifiers_Volatile(Modifier):

    pass
class simTL4J_modifiers_Strictfp(Modifier):

    pass
class AnnotationInstanceOrModifier:

    pass
class simTL4J_modifiers_Modifier(AnnotationInstanceOrModifier):

    pass
class instantiations_Initializable:

    pass
class Member:

    pass
class NamedElement:

    pass
class simTL4J_references_ReferenceableElement(NamedElement):

    pass
class simTL4J_members_Member(NamedElement):

    pass
class NamespaceClassifierReference:

    pass
class AdditionalField:

    pass
class LongLiteral:

    pass
class simTL4J_literals_HexLongLiteral(LongLiteral):

    def __init__(self, hexValue: str):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> str:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: str):
        self.__hexValue = hexValue

class simTL4J_literals_OctalLongLiteral(LongLiteral):

    def __init__(self, octalValue: str):
        self.octalValue = octalValue
        
    @property
    def octalValue(self) -> str:
        return self.__octalValue

    @octalValue.setter
    def octalValue(self, octalValue: str):
        self.__octalValue = octalValue

class simTL4J_literals_DecimalLongLiteral(LongLiteral):

    def __init__(self, decimalValue: str):
        self.decimalValue = decimalValue
        
    @property
    def decimalValue(self) -> str:
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: str):
        self.__decimalValue = decimalValue

class variables_Variable:

    pass
class simTL4J_members_EmptyMember(Member):

    pass
class members_ExceptionThrower:

    pass
class parameters_Parametrizable:

    pass
class statements_StatementListContainer:

    pass
class simTL4J_members_ClassMethod(members_Method, statements_StatementListContainer):

    pass
class DoubleLiteral:

    pass
class simTL4J_literals_HexDoubleLiteral(DoubleLiteral):

    def __init__(self, hexValue: float):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> float:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: float):
        self.__hexValue = hexValue

class simTL4J_literals_DecimalDoubleLiteral(DoubleLiteral):

    def __init__(self, decimalValue: float):
        self.decimalValue = decimalValue
        
    @property
    def decimalValue(self) -> float:
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: float):
        self.__decimalValue = decimalValue

class FloatLiteral:

    pass
class simTL4J_literals_HexFloatLiteral(FloatLiteral):

    def __init__(self, hexValue: float):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> float:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: float):
        self.__hexValue = hexValue

class simTL4J_literals_DecimalFloatLiteral(FloatLiteral):

    def __init__(self, decimalValue: float):
        self.decimalValue = decimalValue
        
    @property
    def decimalValue(self) -> float:
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: float):
        self.__decimalValue = decimalValue

class Literal:

    pass
class simTL4J_literals_DoubleLiteral(Literal):

    pass
class simTL4J_literals_NullLiteral(Literal):

    pass
class simTL4J_literals_LongLiteral(Literal):

    pass
class simTL4J_literals_FloatLiteral(Literal):

    pass
class simTL4J_literals_CharacterLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class simTL4J_literals_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class PrimaryExpression:

    pass
class simTL4J_literals_Literal(PrimaryExpression):

    def __init__(self):
        
    def getOneType(self, alternative: bool) -> str:
        # TODO: Implement getOneType method
        pass

class Self:

    pass
class simTL4J_literals_Super(Self):

    pass
class simTL4J_literals_This(Self):

    pass
class Instantiation:

    pass
class simTL4J_instantiations_ExplicitConstructorCall(Instantiation):

    pass
class AnonymousClass:

    pass
class generics_TypeArgumentable:

    pass
class simTL4J_references_Reference(expressions_PrimaryExpression, generics_TypeArgumentable):

    def __init__(self, simTL4J_references_Reference: "Reference" = None, simTL4J_references_Reference116: set["ArraySelector"] = None):
        self.simTL4J_references_Reference = simTL4J_references_Reference
        self.simTL4J_references_Reference116 = simTL4J_references_Reference116 if simTL4J_references_Reference116 is not None else set()
        
    @property
    def simTL4J_references_Reference116(self):
        return self.__simTL4J_references_Reference116

    @simTL4J_references_Reference116.setter
    def simTL4J_references_Reference116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_references_Reference__simTL4J_references_Reference116", None)
        self.__simTL4J_references_Reference116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArraySelector"):
                    opp_val = getattr(item, "ArraySelector", None)
                    
                    if opp_val == self:
                        setattr(item, "ArraySelector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArraySelector"):
                    opp_val = getattr(item, "ArraySelector", None)
                    
                    setattr(item, "ArraySelector", self)
                    

    @property
    def simTL4J_references_Reference(self):
        return self.__simTL4J_references_Reference

    @simTL4J_references_Reference.setter
    def simTL4J_references_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_references_Reference__simTL4J_references_Reference", None)
        self.__simTL4J_references_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reference"):
                opp_val = getattr(old_value, "Reference", None)
                if opp_val == self:
                    setattr(old_value, "Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reference"):
                opp_val = getattr(value, "Reference", None)
                setattr(value, "Reference", self)

    def getReferencedType(self) -> str:
        # TODO: Implement getReferencedType method
        pass

    def getPrevious(self) -> str:
        # TODO: Implement getPrevious method
        pass

class simTL4J_types_ClassifierReference(types_TypeReference, generics_TypeArgumentable):

    pass
class references_Argumentable:

    pass
class IntegerLiteral:

    pass
class simTL4J_literals_HexIntegerLiteral(IntegerLiteral):

    def __init__(self, hexValue: str):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> str:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: str):
        self.__hexValue = hexValue

class simTL4J_literals_OctalIntegerLiteral(IntegerLiteral):

    def __init__(self, octalValue: str):
        self.octalValue = octalValue
        
    @property
    def octalValue(self) -> str:
        return self.__octalValue

    @octalValue.setter
    def octalValue(self, octalValue: str):
        self.__octalValue = octalValue

class simTL4J_literals_DecimalIntegerLiteral(IntegerLiteral):

    def __init__(self, decimalValue: str):
        self.decimalValue = decimalValue
        
    @property
    def decimalValue(self) -> str:
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: str):
        self.__decimalValue = decimalValue

class simTL4J_literals_IntegerLiteral(Literal):

    pass
class ReferenceableElement:

    pass
class StaticImport:

    pass
class simTL4J_imports_StaticMemberImport(StaticImport):

    pass
class simTL4J_imports_StaticClassifierImport(StaticImport):

    pass
class Static:

    pass
class generics_CallTypeArgumentable:

    pass
class simTL4J_references_MethodCall(generics_CallTypeArgumentable, references_ElementReference, references_Argumentable):

    pass
class instantiations_Instantiation:

    pass
class simTL4J_instantiations_NewConstructorCall(generics_CallTypeArgumentable, instantiations_Instantiation):

    pass
class NamespaceAwareElement:

    pass
class simTL4J_imports_Import(NamespaceAwareElement):

    def __init__(self):
        
    def getImportedMembers(self) -> str:
        # TODO: Implement getImportedMembers method
        pass

    def getImportedClassifier(self, name: str) -> str:
        # TODO: Implement getImportedClassifier method
        pass

    def getImportedClassifiers(self) -> str:
        # TODO: Implement getImportedClassifiers method
        pass

class Import:

    pass
class simTL4J_imports_StaticImport(Import):

    pass
class simTL4J_imports_ClassifierImport(Import):

    pass
class simTL4J_imports_PackageImport(Import):

    pass
class generics_TypeArgument:

    pass
class TypeParameter:

    pass
class TypeArgument:

    pass
class simTL4J_generics_ExtendsTypeArgument(TypeArgument):

    pass
class simTL4J_generics_UnknownTypeArgument(TypeArgument):

    pass
class ArrayTypeable:

    pass
class simTL4J_generics_TypeArgument(ArrayTypeable):

    pass
class Reference:

    pass
class simTL4J_references_ReflectiveClassReference(Reference):

    pass
class simTL4J_references_ElementReference(Reference):

    pass
class simTL4J_references_SelfReference(Reference):

    pass
class simTL4J_references_PrimitiveTypeReference(Reference):

    pass
class simTL4J_references_StringReference(Reference):

    def __init__(self, value: str, Reference: "simTL4J_references_Reference"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class simTL4J_expressions_NestedExpression(Reference):

    pass
class simTL4J_generics_SuperTypeArgument(TypeArgument):

    pass
class UnaryModificationOperator:

    pass
class simTL4J_operators_MinusMinus(UnaryModificationOperator):

    pass
class simTL4J_operators_PlusPlus(UnaryModificationOperator):

    pass
class UnaryModificationExpressionChild:

    pass
class simTL4J_expressions_PrimaryExpression(UnaryModificationExpressionChild):

    pass
class UnaryExpressionChild:

    pass
class simTL4J_expressions_UnaryModificationExpression(UnaryExpressionChild):

    pass
class UnaryOperator:

    pass
class simTL4J_operators_Negate(UnaryOperator):

    pass
class simTL4J_operators_Complement(UnaryOperator):

    pass
class MultiplicativeOperator:

    pass
class simTL4J_operators_Multiplication(MultiplicativeOperator):

    pass
class simTL4J_operators_Division(MultiplicativeOperator):

    pass
class simTL4J_operators_Remainder(MultiplicativeOperator):

    pass
class MultiplicativeExpressionChild:

    pass
class simTL4J_expressions_UnaryExpressionChild(MultiplicativeExpressionChild):

    pass
class simTL4J_expressions_UnaryExpression(MultiplicativeExpressionChild):

    pass
class AdditiveOperator:

    pass
class AdditiveExpressionChild:

    pass
class simTL4J_expressions_MultiplicativeExpression(AdditiveExpressionChild):

    pass
class simTL4J_expressions_MultiplicativeExpressionChild(AdditiveExpressionChild):

    pass
class expressions_UnaryModificationExpressionChild:

    pass
class simTL4J_expressions_UnaryModificationExpressionChild(UnaryExpressionChild):

    pass
class UnaryModificationExpression:

    pass
class simTL4J_expressions_SuffixUnaryModificationExpression(UnaryModificationExpression):

    pass
class simTL4J_expressions_PrefixUnaryModificationExpression(UnaryModificationExpression):

    pass
class ShiftExpressionChild:

    pass
class simTL4J_expressions_AdditiveExpressionChild(ShiftExpressionChild):

    pass
class RelationOperator:

    pass
class simTL4J_operators_GreaterThanOrEqual(RelationOperator):

    pass
class simTL4J_operators_LessThan(RelationOperator):

    pass
class simTL4J_operators_LessThanOrEqual(RelationOperator):

    pass
class simTL4J_operators_GreaterThan(RelationOperator):

    pass
class RelationExpressionChild:

    pass
class simTL4J_expressions_ShiftExpression(RelationExpressionChild):

    pass
class InstanceOfExpressionChild:

    pass
class simTL4J_expressions_RelationExpressionChild(InstanceOfExpressionChild):

    pass
class simTL4J_expressions_RelationExpression(InstanceOfExpressionChild):

    pass
class expressions_EqualityExpressionChild:

    pass
class EqualityExpressionChild:

    pass
class simTL4J_expressions_InstanceOfExpressionChild(EqualityExpressionChild):

    pass
class EqualityOperator:

    pass
class simTL4J_operators_NotEqual(EqualityOperator):

    pass
class simTL4J_operators_Equal(EqualityOperator):

    pass
class AndExpressionChild:

    pass
class simTL4J_expressions_EqualityExpressionChild(AndExpressionChild):

    pass
class simTL4J_expressions_EqualityExpression(AndExpressionChild):

    pass
class simTL4J_expressions_AdditiveExpression(ShiftExpressionChild):

    pass
class simTL4J_expressions_ShiftExpressionChild(RelationExpressionChild):

    pass
class ShiftOperator:

    pass
class simTL4J_operators_UnsignedRightShift(ShiftOperator):

    pass
class simTL4J_operators_RightShift(ShiftOperator):

    pass
class simTL4J_operators_LeftShift(ShiftOperator):

    pass
class InclusiveOrExpressionChild:

    pass
class simTL4J_expressions_ExclusiveOrExpressionChild(InclusiveOrExpressionChild):

    pass
class simTL4J_expressions_ExclusiveOrExpression(InclusiveOrExpressionChild):

    pass
class ConditionalAndExpressionChild:

    pass
class simTL4J_expressions_InclusiveOrExpression(ConditionalAndExpressionChild):

    pass
class simTL4J_expressions_InclusiveOrExpressionChild(ConditionalAndExpressionChild):

    pass
class ConditionalOrExpressionChild:

    pass
class simTL4J_expressions_ConditionalAndExpression(ConditionalOrExpressionChild):

    pass
class simTL4J_expressions_ConditionalAndExpressionChild(ConditionalOrExpressionChild):

    pass
class ConditionalExpressionChild:

    pass
class simTL4J_expressions_ConditionalOrExpressionChild(ConditionalExpressionChild):

    pass
class simTL4J_expressions_ConditionalOrExpression(ConditionalExpressionChild):

    pass
class AssignmentOperator:

    pass
class simTL4J_operators_AssignmentModulo(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentUnsignedRightShift(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentRightShift(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentPlus(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentLeftShift(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentExclusiveOr(AssignmentOperator):

    pass
class simTL4J_operators_Assignment(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentOr(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentDivision(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentMinus(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentMultiplication(AssignmentOperator):

    pass
class simTL4J_operators_AssignmentAnd(AssignmentOperator):

    pass
class AssignmentExpressionChild:

    pass
class simTL4J_expressions_ConditionalExpressionChild(AssignmentExpressionChild):

    pass
class simTL4J_expressions_ConditionalExpression(AssignmentExpressionChild):

    pass
class ExclusiveOrExpressionChild:

    pass
class simTL4J_expressions_AndExpression(ExclusiveOrExpressionChild):

    pass
class simTL4J_expressions_AndExpressionChild(ExclusiveOrExpressionChild):

    pass
class ForLoopInitializer:

    pass
class simTL4J_expressions_ExpressionList(ForLoopInitializer):

    pass
class Package:

    pass
class CompilationUnit:

    pass
class annotations_Annotable:

    pass
class containers_JavaRoot:

    pass
class JavaRoot:

    pass
class simTL4J_containers_EmptyModel(JavaRoot):

    pass
class simTL4J_containers_CompilationUnit(JavaRoot):

    def __init__(self, simTL4J_containers_CompilationUnit: set["ConcreteClassifier"] = None, JavaRoot: "simTL4J_simTL_Template"):
        self.simTL4J_containers_CompilationUnit = simTL4J_containers_CompilationUnit if simTL4J_containers_CompilationUnit is not None else set()
        
    @property
    def simTL4J_containers_CompilationUnit(self):
        return self.__simTL4J_containers_CompilationUnit

    @simTL4J_containers_CompilationUnit.setter
    def simTL4J_containers_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_containers_CompilationUnit__simTL4J_containers_CompilationUnit", None)
        self.__simTL4J_containers_CompilationUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConcreteClassifier"):
                    opp_val = getattr(item, "ConcreteClassifier", None)
                    
                    if opp_val == self:
                        setattr(item, "ConcreteClassifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConcreteClassifier"):
                    opp_val = getattr(item, "ConcreteClassifier", None)
                    
                    setattr(item, "ConcreteClassifier", self)
                    

    def getClassifiersInSamePackage(self) -> str:
        # TODO: Implement getClassifiersInSamePackage method
        pass

    def getContainedClassifier(self, name: str) -> str:
        # TODO: Implement getContainedClassifier method
        pass

class TPlaceholder:

    pass
class imports_ImportingElement:

    pass
class commons_NamedElement:

    pass
class simTL4J_commons_Commentable(ABC):

    def __init__(self, comments: str):
        self.comments = comments
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    def getObjectClass(self) -> str:
        # TODO: Implement getObjectClass method
        pass

    def getContainingAnonymousClass(self) -> str:
        # TODO: Implement getContainingAnonymousClass method
        pass

    def getContainingCompilationUnit(self) -> str:
        # TODO: Implement getContainingCompilationUnit method
        pass

    def getClassClass(self) -> str:
        # TODO: Implement getClassClass method
        pass

    def getContainingAnnotationInstance(self) -> str:
        # TODO: Implement getContainingAnnotationInstance method
        pass

    def getLibClass(self, name: str) -> str:
        # TODO: Implement getLibClass method
        pass

    def getAnnotationInterface(self) -> str:
        # TODO: Implement getAnnotationInterface method
        pass

    def getContainingPackageName(self) -> str:
        # TODO: Implement getContainingPackageName method
        pass

    def getConcreteClassifiers(self, packageName: str, classifierQuery: str) -> str:
        # TODO: Implement getConcreteClassifiers method
        pass

    def getParentConcreteClassifier(self) -> str:
        # TODO: Implement getParentConcreteClassifier method
        pass

    def getLibInterface(self, name: str) -> str:
        # TODO: Implement getLibInterface method
        pass

    def getConcreteClassifier(self, name: str) -> str:
        # TODO: Implement getConcreteClassifier method
        pass

    def getStringClass(self) -> str:
        # TODO: Implement getStringClass method
        pass

    def getContainingConcreteClassifier(self) -> str:
        # TODO: Implement getContainingConcreteClassifier method
        pass

class EnumConstant:

    pass
class ConcreteClassifier:

    pass
class simTL4J_classifiers_Annotation(ConcreteClassifier):

    def __init__(self, ConcreteClassifier97: "simTL4J_imports_ClassifierImport", ConcreteClassifier: "simTL4J_containers_CompilationUnit"):
        
    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

class simTL4J_classifiers_Interface(ConcreteClassifier):

    def __init__(self, simTL4J_classifiers_Interface: set["TypeReference"] = None, simTL4J_classifiers_Interface30: set["TypeReference"] = None, ConcreteClassifier97: "simTL4J_imports_ClassifierImport", ConcreteClassifier: "simTL4J_containers_CompilationUnit"):
        self.simTL4J_classifiers_Interface = simTL4J_classifiers_Interface if simTL4J_classifiers_Interface is not None else set()
        self.simTL4J_classifiers_Interface30 = simTL4J_classifiers_Interface30 if simTL4J_classifiers_Interface30 is not None else set()
        
    @property
    def simTL4J_classifiers_Interface(self):
        return self.__simTL4J_classifiers_Interface

    @simTL4J_classifiers_Interface.setter
    def simTL4J_classifiers_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_classifiers_Interface__simTL4J_classifiers_Interface", None)
        self.__simTL4J_classifiers_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeReference28"):
                    opp_val = getattr(item, "TypeReference28", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeReference28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeReference28"):
                    opp_val = getattr(item, "TypeReference28", None)
                    
                    setattr(item, "TypeReference28", self)
                    

    @property
    def simTL4J_classifiers_Interface30(self):
        return self.__simTL4J_classifiers_Interface30

    @simTL4J_classifiers_Interface30.setter
    def simTL4J_classifiers_Interface30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_classifiers_Interface__simTL4J_classifiers_Interface30", None)
        self.__simTL4J_classifiers_Interface30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeReference31"):
                    opp_val = getattr(item, "TypeReference31", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeReference31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeReference31"):
                    opp_val = getattr(item, "TypeReference31", None)
                    
                    setattr(item, "TypeReference31", self)
                    

    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

class TypeReference:

    pass
class modifiers_AnnotableAndModifiable:

    pass
class simTL4J_parameters_Parameter(variables_Variable, modifiers_AnnotableAndModifiable):

    pass
class simTL4J_variables_LocalVariable(variables_Variable, instantiations_Initializable, modifiers_AnnotableAndModifiable, statements_ForLoopInitializer):

    pass
class statements_Statement:

    pass
class simTL4J_statements_ForEachLoop(statements_Statement, statements_StatementContainer):

    pass
class simTL4J_statements_ForLoop(statements_Statement, statements_StatementContainer, statements_Conditional):

    pass
class simTL4J_statements_TryBlock(statements_Statement, statements_StatementListContainer):

    pass
class simTL4J_statements_Assert(statements_Statement, statements_Conditional):

    pass
class simTL4J_statements_WhileLoop(statements_Statement, statements_StatementContainer):

    pass
class simTL4J_statements_SynchronizedBlock(statements_Statement, statements_StatementListContainer):

    pass
class simTL4J_statements_Condition(statements_Statement, statements_StatementContainer, statements_Conditional):

    pass
class simTL4J_simTL_TFor_StatementListContainer(statements_Statement, simTL_TFor, statements_StatementListContainer):

    pass
class simTL4J_simTL_TIf_StatementListContainer(statements_Statement, simTL_TIf, statements_StatementListContainer):

    pass
class simTL4J_statements_JumpLabel(statements_Statement, statements_StatementContainer, commons_NamedElement):

    pass
class members_Member:

    pass
class simTL4J_statements_Block(statements_Statement, members_Member, statements_StatementListContainer, modifiers_Modifiable):

    pass
class members_MemberContainer:

    pass
class simTL4J_simTL_TIf_MemberContainer(members_MemberContainer, simTL_TIf, members_Member):

    pass
class simTL4J_simTL_TFor_MemberContainer(members_MemberContainer, simTL_TFor, members_Member):

    pass
class generics_TypeParametrizable:

    pass
class simTL4J_members_Constructor(parameters_Parametrizable, modifiers_AnnotableAndModifiable, statements_StatementListContainer, members_Member, generics_TypeParametrizable, members_ExceptionThrower):

    pass
class classifiers_Implementor:

    pass
class classifiers_ConcreteClassifier:

    pass
class simTL4J_classifiers_Enumeration(classifiers_Implementor, classifiers_ConcreteClassifier):

    def __init__(self, simTL4J_classifiers_Enumeration: set["EnumConstant"] = None):
        self.simTL4J_classifiers_Enumeration = simTL4J_classifiers_Enumeration if simTL4J_classifiers_Enumeration is not None else set()
        
    @property
    def simTL4J_classifiers_Enumeration(self):
        return self.__simTL4J_classifiers_Enumeration

    @simTL4J_classifiers_Enumeration.setter
    def simTL4J_classifiers_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_classifiers_Enumeration__simTL4J_classifiers_Enumeration", None)
        self.__simTL4J_classifiers_Enumeration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EnumConstant"):
                    opp_val = getattr(item, "EnumConstant", None)
                    
                    if opp_val == self:
                        setattr(item, "EnumConstant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EnumConstant"):
                    opp_val = getattr(item, "EnumConstant", None)
                    
                    setattr(item, "EnumConstant", self)
                    

    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

class simTL4J_classifiers_Class(classifiers_Implementor, classifiers_ConcreteClassifier):

    def __init__(self, simTL4J_classifiers_Class: "TypeReference" = None, simTL4J_classifiers_Class25: "TypeReference" = None):
        self.simTL4J_classifiers_Class = simTL4J_classifiers_Class
        self.simTL4J_classifiers_Class25 = simTL4J_classifiers_Class25
        
    @property
    def simTL4J_classifiers_Class25(self):
        return self.__simTL4J_classifiers_Class25

    @simTL4J_classifiers_Class25.setter
    def simTL4J_classifiers_Class25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_classifiers_Class__simTL4J_classifiers_Class25", None)
        self.__simTL4J_classifiers_Class25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeReference26"):
                opp_val = getattr(old_value, "TypeReference26", None)
                if opp_val == self:
                    setattr(old_value, "TypeReference26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeReference26"):
                opp_val = getattr(value, "TypeReference26", None)
                setattr(value, "TypeReference26", self)

    @property
    def simTL4J_classifiers_Class(self):
        return self.__simTL4J_classifiers_Class

    @simTL4J_classifiers_Class.setter
    def simTL4J_classifiers_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_classifiers_Class__simTL4J_classifiers_Class", None)
        self.__simTL4J_classifiers_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypeReference23"):
                opp_val = getattr(old_value, "TypeReference23", None)
                if opp_val == self:
                    setattr(old_value, "TypeReference23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypeReference23"):
                opp_val = getattr(value, "TypeReference23", None)
                setattr(value, "TypeReference23", self)

    def unWrapPrimitiveType(self) -> str:
        # TODO: Implement unWrapPrimitiveType method
        pass

    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

    def getSuperClass(self) -> str:
        # TODO: Implement getSuperClass method
        pass

class references_ReferenceableElement:

    pass
class simTL4J_members_Field(instantiations_Initializable, references_ReferenceableElement, modifiers_AnnotableAndModifiable, members_Member, variables_Variable):

    pass
class simTL4J_members_EnumConstant(references_ReferenceableElement, annotations_Annotable, references_Argumentable):

    pass
class simTL4J_containers_Package(references_ReferenceableElement, containers_JavaRoot, annotations_Annotable):

    pass
class types_Type:

    pass
class simTL4J_types_PrimitiveType(types_TypeReference, types_Type):

    def __init__(self):
        
    def getAllMembers(self, context: str) -> str:
        # TODO: Implement getAllMembers method
        pass

    def wrapPrimitiveType(self) -> str:
        # TODO: Implement wrapPrimitiveType method
        pass

class simTL4J_classifiers_AnonymousClass(types_Type, members_MemberContainer):

    def __init__(self):
        
    def getAllMembers(self, context: str) -> str:
        # TODO: Implement getAllMembers method
        pass

    def getSuperClassifier(self) -> str:
        # TODO: Implement getSuperClassifier method
        pass

    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

class simTL4J_classifiers_Classifier(types_Type, references_ReferenceableElement):

    def __init__(self):
        
    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

class ArrayInitializer:

    pass
class arrays_ArrayTypeable:

    pass
class simTL4J_members_AdditionalField(arrays_ArrayTypeable, references_ReferenceableElement, instantiations_Initializable):

    def __init__(self):
        
    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class simTL4J_variables_AdditionalLocalVariable(arrays_ArrayTypeable, references_ReferenceableElement, instantiations_Initializable):

    def __init__(self):
        
    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class types_TypedElement:

    pass
class simTL4J_expressions_InstanceOfExpression(arrays_ArrayTypeable, types_TypedElement, expressions_EqualityExpressionChild):

    pass
class simTL4J_variables_Variable(arrays_ArrayTypeable, commons_NamedElement, references_ReferenceableElement, types_TypedElement, generics_TypeArgumentable):

    def __init__(self):
        
    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class simTL4J_members_Method(arrays_ArrayTypeable, parameters_Parametrizable, references_ReferenceableElement, modifiers_AnnotableAndModifiable, members_Member, generics_TypeParametrizable, members_ExceptionThrower, types_TypedElement):

    def __init__(self):
        
    def isBetterMethodForCall(self, otherMethod: str, methodCall: str) -> bool:
        # TODO: Implement isBetterMethodForCall method
        pass

    def isSomeMethodForCall(self, methodCall: str) -> bool:
        # TODO: Implement isSomeMethodForCall method
        pass

    def isMethodForCall(self, methodCall: str, needsPerfectMatch: bool) -> bool:
        # TODO: Implement isMethodForCall method
        pass

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class simTL4J_generics_QualifiedTypeArgument(generics_TypeArgument, types_TypedElement):

    pass
class simTL4J_expressions_CastExpression(arrays_ArrayTypeable, expressions_UnaryModificationExpressionChild, types_TypedElement):

    pass
class expressions_Expression:

    pass
class ArrayInitializationValue:

    pass
class classifiers_Classifier:

    pass
class simTL4J_classifiers_ConcreteClassifier(statements_Statement, classifiers_Classifier, modifiers_AnnotableAndModifiable, members_MemberContainer, members_Member, generics_TypeParametrizable):

    def __init__(self, fullName: str):
        self.fullName = fullName
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    def getSuperTypeReferences(self) -> str:
        # TODO: Implement getSuperTypeReferences method
        pass

    def getInnerClassifiers(self) -> str:
        # TODO: Implement getInnerClassifiers method
        pass

    def getAllInnerClassifiers(self) -> str:
        # TODO: Implement getAllInnerClassifiers method
        pass

    def getAllMembers(self, context: str) -> str:
        # TODO: Implement getAllMembers method
        pass

class ArrayDimension:

    pass
class Expression:

    pass
class simTL4J_expressions_AssignmentExpression(Expression):

    pass
class simTL4J_expressions_AssignmentExpressionChild(Expression):

    pass
class InterfaceMethod:

    pass
class simTL4J_annotations_AnnotationAttribute(InterfaceMethod):

    pass
class AnnotationAttributeSetting:

    pass
class annotations_AnnotationValue:

    pass
class arrays_ArrayInitializationValue:

    pass
class simTL4J_expressions_Expression(annotations_AnnotationValue, arrays_ArrayInitializationValue):

    def __init__(self):
        
    def getAlternativeType(self) -> str:
        # TODO: Implement getAlternativeType method
        pass

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getOneType(self, alternative: bool) -> str:
        # TODO: Implement getOneType method
        pass

class simTL4J_arrays_ArrayInitializer(annotations_AnnotationValue, arrays_ArrayInitializationValue):

    pass
class AnnotationParameter:

    pass
class simTL4J_annotations_AnnotationParameterList(AnnotationParameter):

    pass
class simTL4J_annotations_SingleAnnotationParameter(AnnotationParameter):

    pass
class Classifier:

    pass
class simTL4J_generics_TypeParameter(Classifier):

    def __init__(self, simTL4J_generics_TypeParameter: set["TypeReference"] = None, Classifier: "simTL4J_annotations_AnnotationInstance", Classifier165: "simTL4J_types_ClassifierReference"):
        self.simTL4J_generics_TypeParameter = simTL4J_generics_TypeParameter if simTL4J_generics_TypeParameter is not None else set()
        
    @property
    def simTL4J_generics_TypeParameter(self):
        return self.__simTL4J_generics_TypeParameter

    @simTL4J_generics_TypeParameter.setter
    def simTL4J_generics_TypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_generics_TypeParameter__simTL4J_generics_TypeParameter", None)
        self.__simTL4J_generics_TypeParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeReference93"):
                    opp_val = getattr(item, "TypeReference93", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeReference93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeReference93"):
                    opp_val = getattr(item, "TypeReference93", None)
                    
                    setattr(item, "TypeReference93", self)
                    

    def getBoundType(self, typeReference: str, reference: str) -> str:
        # TODO: Implement getBoundType method
        pass

    def getAllMembers(self, context: str) -> str:
        # TODO: Implement getAllMembers method
        pass

    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

class commons_NamespaceAwareElement:

    pass
class simTL4J_types_NamespaceClassifierReference(types_TypeReference, commons_NamespaceAwareElement):

    pass
class simTL4J_containers_JavaRoot(commons_NamespaceAwareElement, commons_NamedElement, imports_ImportingElement):

    def __init__(self):
        
    def getClassifiersInSamePackage(self) -> str:
        # TODO: Implement getClassifiersInSamePackage method
        pass

class modifiers_AnnotationInstanceOrModifier:

    pass
class references_Reference:

    pass
class simTL4J_instantiations_Instantiation(generics_TypeArgumentable, references_Argumentable, types_TypedElement, references_Reference):

    pass
class simTL4J_arrays_ArrayInstantiationBySize(arrays_ArrayTypeable, expressions_Expression, types_TypedElement, references_Reference):

    pass
class simTL4J_arrays_ArrayInstantiationByValues(arrays_ArrayTypeable, types_TypedElement, expressions_Expression, references_Reference):

    pass
class simTL4J_annotations_AnnotationInstance(commons_NamespaceAwareElement, modifiers_AnnotationInstanceOrModifier, references_Reference):

    pass
class AnnotationInstance:

    pass
class Commentable:

    pass
class simTL4J_arrays_ArrayDimension(Commentable):

    pass
class simTL4J_types_TypedElement(Commentable):

    pass
class simTL4J_arrays_ArraySelector(Commentable):

    pass
class simTL4J_instantiations_Initializable(Commentable):

    pass
class simTL4J_classifiers_Implementor(Commentable):

    pass
class simTL4J_imports_ImportingElement(Commentable):

    def __init__(self, simTL4J_imports_ImportingElement: set["Import"] = None):
        self.simTL4J_imports_ImportingElement = simTL4J_imports_ImportingElement if simTL4J_imports_ImportingElement is not None else set()
        
    @property
    def simTL4J_imports_ImportingElement(self):
        return self.__simTL4J_imports_ImportingElement

    @simTL4J_imports_ImportingElement.setter
    def simTL4J_imports_ImportingElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_imports_ImportingElement__simTL4J_imports_ImportingElement", None)
        self.__simTL4J_imports_ImportingElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    if opp_val == self:
                        setattr(item, "Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Import"):
                    opp_val = getattr(item, "Import", None)
                    
                    setattr(item, "Import", self)
                    

    def getDefaultImports(self) -> str:
        # TODO: Implement getDefaultImports method
        pass

class simTL4J_members_MemberContainer(Commentable):

    def __init__(self, simTL4J_members_MemberContainer: set["Member"] = None, simTL4J_members_MemberContainer106: set["Member"] = None):
        self.simTL4J_members_MemberContainer = simTL4J_members_MemberContainer if simTL4J_members_MemberContainer is not None else set()
        self.simTL4J_members_MemberContainer106 = simTL4J_members_MemberContainer106 if simTL4J_members_MemberContainer106 is not None else set()
        
    @property
    def simTL4J_members_MemberContainer106(self):
        return self.__simTL4J_members_MemberContainer106

    @simTL4J_members_MemberContainer106.setter
    def simTL4J_members_MemberContainer106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_members_MemberContainer__simTL4J_members_MemberContainer106", None)
        self.__simTL4J_members_MemberContainer106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member107"):
                    opp_val = getattr(item, "Member107", None)
                    
                    if opp_val == self:
                        setattr(item, "Member107", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member107"):
                    opp_val = getattr(item, "Member107", None)
                    
                    setattr(item, "Member107", self)
                    

    @property
    def simTL4J_members_MemberContainer(self):
        return self.__simTL4J_members_MemberContainer

    @simTL4J_members_MemberContainer.setter
    def simTL4J_members_MemberContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_members_MemberContainer__simTL4J_members_MemberContainer", None)
        self.__simTL4J_members_MemberContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    if opp_val == self:
                        setattr(item, "Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member"):
                    opp_val = getattr(item, "Member", None)
                    
                    setattr(item, "Member", self)
                    

    def getContainedField(self, name: str) -> str:
        # TODO: Implement getContainedField method
        pass

    def getContainedClassifier(self, name: str) -> str:
        # TODO: Implement getContainedClassifier method
        pass

    def getContainedMethod(self, name: str) -> str:
        # TODO: Implement getContainedMethod method
        pass

class simTL4J_generics_TypeArgumentable(Commentable):

    pass
class simTL4J_literals_Self(Commentable):

    pass
class simTL4J_modifiers_AnnotationInstanceOrModifier(Commentable):

    pass
class simTL4J_modifiers_AnnotableAndModifiable(Commentable):

    def __init__(self, simTL4J_modifiers_AnnotableAndModifiable: set["AnnotationInstanceOrModifier"] = None):
        self.simTL4J_modifiers_AnnotableAndModifiable = simTL4J_modifiers_AnnotableAndModifiable if simTL4J_modifiers_AnnotableAndModifiable is not None else set()
        
    @property
    def simTL4J_modifiers_AnnotableAndModifiable(self):
        return self.__simTL4J_modifiers_AnnotableAndModifiable

    @simTL4J_modifiers_AnnotableAndModifiable.setter
    def simTL4J_modifiers_AnnotableAndModifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_modifiers_AnnotableAndModifiable__simTL4J_modifiers_AnnotableAndModifiable", None)
        self.__simTL4J_modifiers_AnnotableAndModifiable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AnnotationInstanceOrModifier"):
                    opp_val = getattr(item, "AnnotationInstanceOrModifier", None)
                    
                    if opp_val == self:
                        setattr(item, "AnnotationInstanceOrModifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AnnotationInstanceOrModifier"):
                    opp_val = getattr(item, "AnnotationInstanceOrModifier", None)
                    
                    setattr(item, "AnnotationInstanceOrModifier", self)
                    

    def isStatic(self) -> bool:
        # TODO: Implement isStatic method
        pass

    def isHidden(self, context: str) -> bool:
        # TODO: Implement isHidden method
        pass

class simTL4J_annotations_AnnotationValue(Commentable):

    pass
class simTL4J_references_Argumentable(Commentable):

    def __init__(self, simTL4J_references_Argumentable: set["Expression"] = None):
        self.simTL4J_references_Argumentable = simTL4J_references_Argumentable if simTL4J_references_Argumentable is not None else set()
        
    @property
    def simTL4J_references_Argumentable(self):
        return self.__simTL4J_references_Argumentable

    @simTL4J_references_Argumentable.setter
    def simTL4J_references_Argumentable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_references_Argumentable__simTL4J_references_Argumentable", None)
        self.__simTL4J_references_Argumentable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression118"):
                    opp_val = getattr(item, "Expression118", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression118"):
                    opp_val = getattr(item, "Expression118", None)
                    
                    setattr(item, "Expression118", self)
                    

    def getArgumentTypes(self) -> str:
        # TODO: Implement getArgumentTypes method
        pass

class simTL4J_operators_Operator(Commentable):

    pass
class simTL4J_commons_NamedElement(Commentable):

    def __init__(self, name: str, simTL4J_commons_NamedElement: "TPlaceholder" = None):
        self.name = name
        self.simTL4J_commons_NamedElement = simTL4J_commons_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simTL4J_commons_NamedElement(self):
        return self.__simTL4J_commons_NamedElement

    @simTL4J_commons_NamedElement.setter
    def simTL4J_commons_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_commons_NamedElement__simTL4J_commons_NamedElement", None)
        self.__simTL4J_commons_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TPlaceholder"):
                opp_val = getattr(old_value, "TPlaceholder", None)
                if opp_val == self:
                    setattr(old_value, "TPlaceholder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TPlaceholder"):
                opp_val = getattr(value, "TPlaceholder", None)
                setattr(value, "TPlaceholder", self)

class simTL4J_parameters_Parametrizable(Commentable):

    pass
class simTL4J_arrays_ArrayInitializationValue(Commentable):

    pass
class simTL4J_members_ExceptionThrower(Commentable):

    pass
class simTL4J_annotations_AnnotationAttributeSetting(Commentable):

    pass
class simTL4J_modifiers_Modifiable(Commentable):

    pass
class simTL4J_statements_Conditional(Commentable):

    pass
class simTL4J_types_Type(Commentable):

    def __init__(self):
        
    def equalsType(self, otherType: str, otherArrayDimension: str, arrayDimension: str) -> bool:
        # TODO: Implement equalsType method
        pass

    def getAllMembers(self, context: str) -> str:
        # TODO: Implement getAllMembers method
        pass

    def isSuperType(self, arrayDimension: str, otherType: str, otherArrayType: str) -> bool:
        # TODO: Implement isSuperType method
        pass

class simTL4J_statements_StatementContainer(Commentable):

    pass
class simTL4J_commons_NamespaceAwareElement(Commentable):

    def __init__(self, namespaces: str):
        self.namespaces = namespaces
        
    @property
    def namespaces(self) -> str:
        return self.__namespaces

    @namespaces.setter
    def namespaces(self, namespaces: str):
        self.__namespaces = namespaces

    def getNamespacesAsString(self) -> str:
        # TODO: Implement getNamespacesAsString method
        pass

    def getClassifierAtNamespaces(self) -> str:
        # TODO: Implement getClassifierAtNamespaces method
        pass

class simTL4J_arrays_ArrayTypeable(Commentable):

    def __init__(self, simTL4J_arrays_ArrayTypeable: set["ArrayDimension"] = None, simTL4J_arrays_ArrayTypeable13: set["ArrayDimension"] = None):
        self.simTL4J_arrays_ArrayTypeable = simTL4J_arrays_ArrayTypeable if simTL4J_arrays_ArrayTypeable is not None else set()
        self.simTL4J_arrays_ArrayTypeable13 = simTL4J_arrays_ArrayTypeable13 if simTL4J_arrays_ArrayTypeable13 is not None else set()
        
    @property
    def simTL4J_arrays_ArrayTypeable13(self):
        return self.__simTL4J_arrays_ArrayTypeable13

    @simTL4J_arrays_ArrayTypeable13.setter
    def simTL4J_arrays_ArrayTypeable13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_arrays_ArrayTypeable__simTL4J_arrays_ArrayTypeable13", None)
        self.__simTL4J_arrays_ArrayTypeable13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArrayDimension14"):
                    opp_val = getattr(item, "ArrayDimension14", None)
                    
                    if opp_val == self:
                        setattr(item, "ArrayDimension14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArrayDimension14"):
                    opp_val = getattr(item, "ArrayDimension14", None)
                    
                    setattr(item, "ArrayDimension14", self)
                    

    @property
    def simTL4J_arrays_ArrayTypeable(self):
        return self.__simTL4J_arrays_ArrayTypeable

    @simTL4J_arrays_ArrayTypeable.setter
    def simTL4J_arrays_ArrayTypeable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simTL4J_arrays_ArrayTypeable__simTL4J_arrays_ArrayTypeable", None)
        self.__simTL4J_arrays_ArrayTypeable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ArrayDimension"):
                    opp_val = getattr(item, "ArrayDimension", None)
                    
                    if opp_val == self:
                        setattr(item, "ArrayDimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ArrayDimension"):
                    opp_val = getattr(item, "ArrayDimension", None)
                    
                    setattr(item, "ArrayDimension", self)
                    

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class simTL4J_statements_StatementListContainer(Commentable):

    pass
class simTL4J_generics_TypeParametrizable(Commentable):

    pass
class simTL4J_generics_CallTypeArgumentable(Commentable):

    pass
class simTL4J_statements_ForLoopInitializer(Commentable):

    pass
class simTL4J_types_TypeReference(Commentable):

    def __init__(self):
        
    def getTarget(self) -> str:
        # TODO: Implement getTarget method
        pass

    def getPureClassifierReference(self) -> str:
        # TODO: Implement getPureClassifierReference method
        pass

    def getBoundTarget(self, reference: str) -> str:
        # TODO: Implement getBoundTarget method
        pass

class simTL4J_statements_Statement(Commentable):

    pass
class simTL4J_annotations_AnnotationParameter(Commentable):

    pass
class simTL4J_annotations_Annotable(Commentable):

    pass
class AnnotationValue:

    pass