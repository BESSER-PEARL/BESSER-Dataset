from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AdditionalLocalVariable:

    pass
class ClassifierReference:

    pass
class Block:

    pass
class CatchBlock:

    pass
class LocalVariable:

    pass
class JumpLabel:

    pass
class Modifiable:

    pass
class Jump:

    pass
class statements_Break(Jump):

    pass
class Conditional:

    pass
class PrimitiveType:

    pass
class types_Short(PrimitiveType):

    pass
class types_Double(PrimitiveType):

    pass
class types_Byte(PrimitiveType):

    pass
class types_Long(PrimitiveType):

    pass
class types_Float(PrimitiveType):

    pass
class types_Int(PrimitiveType):

    pass
class types_Void(PrimitiveType):

    pass
class types_Bool(PrimitiveType):

    pass
class types_Char(PrimitiveType):

    pass
class ElementReference:

    pass
class WhileLoop:

    pass
class statements_DoWhileLoop(WhileLoop):

    pass
class SwitchCase:

    pass
class statements_NormalSwitchCase(SwitchCase, Conditional):

    pass
class statements_DefaultSwitchCase(SwitchCase):

    pass
class statements_Continue(Jump):

    pass
class StatementContainer:

    pass
class OrdinaryParameter:

    pass
class ArraySelector:

    pass
class Parameter:

    pass
class parameters_VariableLengthParameter(Parameter):

    pass
class parameters_OrdinaryParameter(Parameter):

    pass
class Modifier:

    pass
class modifiers_Strictfp(Modifier):

    pass
class modifiers_Synchronized(Modifier):

    pass
class modifiers_Final(Modifier):

    pass
class modifiers_Transient(Modifier):

    pass
class modifiers_Abstract(Modifier):

    pass
class modifiers_Static(Modifier):

    pass
class modifiers_Public(Modifier):

    pass
class modifiers_Protected(Modifier):

    pass
class modifiers_Native(Modifier):

    pass
class modifiers_Private(Modifier):

    pass
class AdditionalField:

    pass
class Variable:

    pass
class ExceptionThrower:

    pass
class Parametrizable:

    pass
class StatementListContainer:

    pass
class statements_SwitchCase(StatementListContainer):

    pass
class statements_CatchBlock(StatementListContainer):

    pass
class Initializable:

    pass
class NamespaceClassifierReference:

    pass
class Method:

    pass
class members_ClassMethod(Method, StatementListContainer):

    pass
class members_InterfaceMethod(Method):

    pass
class DoubleLiteral:

    pass
class literals_HexDoubleLiteral(DoubleLiteral):

    def __init__(self, hexValue: float):
        self.hexValue = hexValue
        
        pass
    @property
    def hexValue(self):
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: float):
        self.__hexValue = hexValue


class literals_DecimalDoubleLiteral(DoubleLiteral):

    def __init__(self, decimalValue: float):
        self.decimalValue = decimalValue
        
        pass
    @property
    def decimalValue(self):
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: float):
        self.__decimalValue = decimalValue


class FloatLiteral:

    pass
class literals_HexFloatLiteral(FloatLiteral):

    def __init__(self, hexValue: float):
        self.hexValue = hexValue
        
        pass
    @property
    def hexValue(self):
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: float):
        self.__hexValue = hexValue


class literals_DecimalFloatLiteral(FloatLiteral):

    def __init__(self, decimalValue: float):
        self.decimalValue = decimalValue
        
        pass
    @property
    def decimalValue(self):
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: float):
        self.__decimalValue = decimalValue


class Literal:

    pass
class literals_NullLiteral(Literal):

    pass
class literals_DoubleLiteral(Literal):

    pass
class literals_IntegerLiteral(Literal):

    pass
class literals_CharacterLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class literals_FloatLiteral(Literal):

    pass
class literals_BooleanLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class PrimaryExpression:

    pass
class literals_Literal(PrimaryExpression):

    def __init__(self):
        
        pass
    def getOneType(self, literals_alternative) :
        # TODO: Implement getOneType method
        pass

class Self:

    pass
class literals_Super(Self):

    pass
class literals_This(Self):

    pass
class AnonymousClass:

    pass
class CallTypeArgumentable:

    pass
class Instantiation:

    pass
class instantiations_ExplicitConstructorCall(Instantiation):

    pass
class instantiations_NewConstructorCall(Instantiation, CallTypeArgumentable):

    pass
class TypeArgumentable:

    pass
class references_Reference(PrimaryExpression, TypeArgumentable):

    def __init__(self, references_Reference115: set["ArraySelector"] = None, references_Reference: "Reference" = None):
        self.references_Reference115 = references_Reference115 if references_Reference115 is not None else set()
        self.references_Reference = references_Reference
        
        pass
    @property
    def references_Reference115(self):
        return self.__references_Reference115

    @references_Reference115.setter
    def references_Reference115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_references_Reference__references_Reference115", None)
        self.__references_Reference115 = value if value is not None else set()
        
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
    def references_Reference(self):
        return self.__references_Reference

    @references_Reference.setter
    def references_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_references_Reference__references_Reference", None)
        self.__references_Reference = value
        
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

    def getPrevious(self) :
        # TODO: Implement getPrevious method
        pass

    def getReferencedType(self) :
        # TODO: Implement getReferencedType method
        pass

class Argumentable:

    pass
class references_MethodCall(Argumentable, CallTypeArgumentable, ElementReference):

    pass
class LongLiteral:

    pass
class literals_OctalLongLiteral(LongLiteral):

    def __init__(self, octalValue: str):
        self.octalValue = octalValue
        
        pass
    @property
    def octalValue(self):
        return self.__octalValue

    @octalValue.setter
    def octalValue(self, octalValue: str):
        self.__octalValue = octalValue


class literals_HexLongLiteral(LongLiteral):

    def __init__(self, hexValue: str):
        self.hexValue = hexValue
        
        pass
    @property
    def hexValue(self):
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: str):
        self.__hexValue = hexValue


class literals_DecimalLongLiteral(LongLiteral):

    def __init__(self, decimalValue: str):
        self.decimalValue = decimalValue
        
        pass
    @property
    def decimalValue(self):
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: str):
        self.__decimalValue = decimalValue


class literals_LongLiteral(Literal):

    pass
class IntegerLiteral:

    pass
class literals_OctalIntegerLiteral(IntegerLiteral):

    def __init__(self, octalValue: str):
        self.octalValue = octalValue
        
        pass
    @property
    def octalValue(self):
        return self.__octalValue

    @octalValue.setter
    def octalValue(self, octalValue: str):
        self.__octalValue = octalValue


class literals_HexIntegerLiteral(IntegerLiteral):

    def __init__(self, hexValue: str):
        self.hexValue = hexValue
        
        pass
    @property
    def hexValue(self):
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: str):
        self.__hexValue = hexValue


class literals_DecimalIntegerLiteral(IntegerLiteral):

    def __init__(self, decimalValue: str):
        self.decimalValue = decimalValue
        
        pass
    @property
    def decimalValue(self):
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: str):
        self.__decimalValue = decimalValue


class references_IdentifierReference(ElementReference):

    pass
class Operator:

    pass
class operators_EqualityOperator(Operator):

    pass
class operators_AssignmentOperator(Operator):

    pass
class operators_UnaryOperator(Operator):

    pass
class operators_RelationOperator(Operator):

    pass
class operators_ShiftOperator(Operator):

    pass
class operators_MultiplicativeOperator(Operator):

    pass
class operators_UnaryModificationOperator(Operator):

    pass
class operators_AdditiveOperator(Operator):

    pass
class modifiers_Volatile(Modifier):

    pass
class Commentable:

    pass
class types_Type(Commentable):

    def __init__(self):
        
        pass
    def getAllMembers(self, types_context) :
        # TODO: Implement getAllMembers method
        pass

    def isSuperType(self, types_otherArrayType, types_otherType, types_arrayDimension) :
        # TODO: Implement isSuperType method
        pass

    def equalsType(self, types_otherType, types_arrayDimension, types_otherArrayDimension) :
        # TODO: Implement equalsType method
        pass

class types_TypeReference(Commentable):

    def __init__(self):
        
        pass
    def getTarget(self) :
        # TODO: Implement getTarget method
        pass

    def getBoundTarget(self, types_reference) :
        # TODO: Implement getBoundTarget method
        pass

    def getPureClassifierReference(self) :
        # TODO: Implement getPureClassifierReference method
        pass

class modifiers_Modifiable(Commentable):

    pass
class members_MemberContainer(Commentable):

    def __init__(self, members_MemberContainer: set["Member"] = None, members_MemberContainer105: set["Member"] = None):
        self.members_MemberContainer = members_MemberContainer if members_MemberContainer is not None else set()
        self.members_MemberContainer105 = members_MemberContainer105 if members_MemberContainer105 is not None else set()
        
        pass
    @property
    def members_MemberContainer(self):
        return self.__members_MemberContainer

    @members_MemberContainer.setter
    def members_MemberContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_members_MemberContainer__members_MemberContainer", None)
        self.__members_MemberContainer = value if value is not None else set()
        
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
                    

    @property
    def members_MemberContainer105(self):
        return self.__members_MemberContainer105

    @members_MemberContainer105.setter
    def members_MemberContainer105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_members_MemberContainer__members_MemberContainer105", None)
        self.__members_MemberContainer105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Member106"):
                    opp_val = getattr(item, "Member106", None)
                    
                    if opp_val == self:
                        setattr(item, "Member106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Member106"):
                    opp_val = getattr(item, "Member106", None)
                    
                    setattr(item, "Member106", self)
                    

    def getContainedField(self, members_name) :
        # TODO: Implement getContainedField method
        pass

    def getContainedMethod(self, members_name) :
        # TODO: Implement getContainedMethod method
        pass

    def getContainedClassifier(self, members_name) :
        # TODO: Implement getContainedClassifier method
        pass

class members_ExceptionThrower(Commentable):

    pass
class statements_StatementContainer(Commentable):

    pass
class literals_Self(Commentable):

    pass
class instantiations_Initializable(Commentable):

    pass
class statements_Conditional(Commentable):

    pass
class statements_Statement(Commentable):

    pass
class imports_ImportingElement(Commentable):

    def __init__(self, imports_ImportingElement: set["Import"] = None):
        self.imports_ImportingElement = imports_ImportingElement if imports_ImportingElement is not None else set()
        
        pass
    @property
    def imports_ImportingElement(self):
        return self.__imports_ImportingElement

    @imports_ImportingElement.setter
    def imports_ImportingElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imports_ImportingElement__imports_ImportingElement", None)
        self.__imports_ImportingElement = value if value is not None else set()
        
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
                    

    def getDefaultImports(self) :
        # TODO: Implement getDefaultImports method
        pass

class types_TypedElement(Commentable):

    pass
class statements_ForLoopInitializer(Commentable):

    pass
class parameters_Parametrizable(Commentable):

    pass
class references_Argumentable(Commentable):

    def __init__(self, references_Argumentable: set["Expression"] = None):
        self.references_Argumentable = references_Argumentable if references_Argumentable is not None else set()
        
        pass
    @property
    def references_Argumentable(self):
        return self.__references_Argumentable

    @references_Argumentable.setter
    def references_Argumentable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_references_Argumentable__references_Argumentable", None)
        self.__references_Argumentable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Expression117"):
                    opp_val = getattr(item, "Expression117", None)
                    
                    if opp_val == self:
                        setattr(item, "Expression117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Expression117"):
                    opp_val = getattr(item, "Expression117", None)
                    
                    setattr(item, "Expression117", self)
                    

    def getArgumentTypes(self) :
        # TODO: Implement getArgumentTypes method
        pass

class modifiers_AnnotableAndModifiable(Commentable):

    def __init__(self, modifiers_AnnotableAndModifiable: set["AnnotationInstanceOrModifier"] = None):
        self.modifiers_AnnotableAndModifiable = modifiers_AnnotableAndModifiable if modifiers_AnnotableAndModifiable is not None else set()
        
        pass
    @property
    def modifiers_AnnotableAndModifiable(self):
        return self.__modifiers_AnnotableAndModifiable

    @modifiers_AnnotableAndModifiable.setter
    def modifiers_AnnotableAndModifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_modifiers_AnnotableAndModifiable__modifiers_AnnotableAndModifiable", None)
        self.__modifiers_AnnotableAndModifiable = value if value is not None else set()
        
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
                    

    def isStatic(self) :
        # TODO: Implement isStatic method
        pass

    def isHidden(self, modifiers_context) :
        # TODO: Implement isHidden method
        pass

class operators_Operator(Commentable):

    pass
class statements_StatementListContainer(Commentable):

    pass
class modifiers_AnnotationInstanceOrModifier(Commentable):

    pass
class annotations_Annotable(Commentable):

    pass
class AnnotationValue:

    pass
class annotations_AnnotationParameter(Commentable):

    pass
class AnnotationParameter:

    pass
class annotations_SingleAnnotationParameter(AnnotationParameter):

    pass
class Classifier:

    pass
class NamespaceAwareElement:

    pass
class imports_Import(NamespaceAwareElement):

    def __init__(self):
        
        pass
    def getImportedClassifiers(self) :
        # TODO: Implement getImportedClassifiers method
        pass

    def getImportedClassifier(self, imports_name) :
        # TODO: Implement getImportedClassifier method
        pass

    def getImportedMembers(self) :
        # TODO: Implement getImportedMembers method
        pass

class AnnotationInstanceOrModifier:

    pass
class modifiers_Modifier(AnnotationInstanceOrModifier):

    pass
class Reference:

    pass
class references_SelfReference(Reference):

    pass
class references_StringReference(Reference):

    def __init__(self, value: str, Reference: "references_Reference" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class references_ReflectiveClassReference(Reference):

    pass
class references_ElementReference(Reference):

    pass
class references_PrimitiveTypeReference(Reference):

    pass
class expressions_NestedExpression(Reference):

    pass
class ShiftOperator:

    pass
class operators_LeftShift(ShiftOperator):

    pass
class operators_UnsignedRightShift(ShiftOperator):

    pass
class operators_RightShift(ShiftOperator):

    pass
class ShiftExpressionChild:

    pass
class expressions_AdditiveExpression(ShiftExpressionChild):

    pass
class RelationOperator:

    pass
class operators_GreaterThanOrEqual(RelationOperator):

    pass
class operators_GreaterThan(RelationOperator):

    pass
class operators_LessThan(RelationOperator):

    pass
class operators_LessThanOrEqual(RelationOperator):

    pass
class RelationExpressionChild:

    pass
class expressions_ShiftExpressionChild(RelationExpressionChild):

    pass
class expressions_ShiftExpression(RelationExpressionChild):

    pass
class InstanceOfExpressionChild:

    pass
class expressions_RelationExpression(InstanceOfExpressionChild):

    pass
class expressions_RelationExpressionChild(InstanceOfExpressionChild):

    pass
class EqualityExpressionChild:

    pass
class expressions_InstanceOfExpressionChild(EqualityExpressionChild):

    pass
class EqualityOperator:

    pass
class operators_NotEqual(EqualityOperator):

    pass
class operators_Equal(EqualityOperator):

    pass
class AndExpressionChild:

    pass
class expressions_EqualityExpression(AndExpressionChild):

    pass
class expressions_EqualityExpressionChild(AndExpressionChild):

    pass
class ExclusiveOrExpressionChild:

    pass
class expressions_AndExpressionChild(ExclusiveOrExpressionChild):

    pass
class expressions_AndExpression(ExclusiveOrExpressionChild):

    pass
class MultiplicativeOperator:

    pass
class operators_Multiplication(MultiplicativeOperator):

    pass
class operators_Division(MultiplicativeOperator):

    pass
class operators_Remainder(MultiplicativeOperator):

    pass
class MultiplicativeExpressionChild:

    pass
class expressions_AdditiveExpressionChild(ShiftExpressionChild):

    pass
class AdditiveOperator:

    pass
class AdditiveExpressionChild:

    pass
class expressions_MultiplicativeExpressionChild(AdditiveExpressionChild):

    pass
class expressions_MultiplicativeExpression(AdditiveExpressionChild):

    pass
class ConditionalExpressionChild:

    pass
class expressions_ConditionalOrExpression(ConditionalExpressionChild):

    pass
class AssignmentOperator:

    pass
class operators_AssignmentMultiplication(AssignmentOperator):

    pass
class operators_AssignmentRightShift(AssignmentOperator):

    pass
class operators_AssignmentAnd(AssignmentOperator):

    pass
class operators_AssignmentDivision(AssignmentOperator):

    pass
class operators_AssignmentLeftShift(AssignmentOperator):

    pass
class operators_AssignmentExclusiveOr(AssignmentOperator):

    pass
class operators_AssignmentMinus(AssignmentOperator):

    pass
class operators_AssignmentUnsignedRightShift(AssignmentOperator):

    pass
class operators_Assignment(AssignmentOperator):

    pass
class operators_AssignmentPlus(AssignmentOperator):

    pass
class operators_AssignmentOr(AssignmentOperator):

    pass
class operators_AssignmentModulo(AssignmentOperator):

    pass
class AssignmentExpressionChild:

    pass
class expressions_ConditionalExpression(AssignmentExpressionChild):

    pass
class expressions_ConditionalExpressionChild(AssignmentExpressionChild):

    pass
class ForLoopInitializer:

    pass
class expressions_ExpressionList(ForLoopInitializer):

    pass
class Package:

    pass
class CompilationUnit:

    pass
class Annotable:

    pass
class InclusiveOrExpressionChild:

    pass
class expressions_ExclusiveOrExpressionChild(InclusiveOrExpressionChild):

    pass
class expressions_ExclusiveOrExpression(InclusiveOrExpressionChild):

    pass
class ConditionalAndExpressionChild:

    pass
class expressions_InclusiveOrExpression(ConditionalAndExpressionChild):

    pass
class expressions_InclusiveOrExpressionChild(ConditionalAndExpressionChild):

    pass
class expressions_ConditionalOrExpressionChild(ConditionalExpressionChild):

    pass
class ConditionalOrExpressionChild:

    pass
class expressions_ConditionalAndExpression(ConditionalOrExpressionChild):

    pass
class expressions_ConditionalAndExpressionChild(ConditionalOrExpressionChild):

    pass
class commons_NamespaceAwareElement(Commentable):

    def __init__(self, namespaces: str):
        self.namespaces = namespaces
        
        pass
    @property
    def namespaces(self):
        return self.__namespaces

    @namespaces.setter
    def namespaces(self, namespaces: str):
        self.__namespaces = namespaces


    def getNamespacesAsString(self) :
        # TODO: Implement getNamespacesAsString method
        pass

    def getClassifierAtNamespaces(self) :
        # TODO: Implement getClassifierAtNamespaces method
        pass

class commons_NamedElement(Commentable):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class commons_Commentable(ABC):

    def __init__(self, comments: str):
        self.comments = comments
        
        pass
    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments


    def getContainingAnonymousClass(self) :
        # TODO: Implement getContainingAnonymousClass method
        pass

    def getAnnotationInterface(self) :
        # TODO: Implement getAnnotationInterface method
        pass

    def getConcreteClassifierProxy(self, commons_name) :
        # TODO: Implement getConcreteClassifierProxy method
        pass

    def getConcreteClassifierProxies(self, commons_packageName, commons_classifierQuery) :
        # TODO: Implement getConcreteClassifierProxies method
        pass

    def getContainingPackageName(self) :
        # TODO: Implement getContainingPackageName method
        pass

    def getObjectClass(self) :
        # TODO: Implement getObjectClass method
        pass

    def getContainingCompilationUnit(self) :
        # TODO: Implement getContainingCompilationUnit method
        pass

    def getLibClass(self, commons_name) :
        # TODO: Implement getLibClass method
        pass

    def getStringClass(self) :
        # TODO: Implement getStringClass method
        pass

    def getParentConcreteClassifier(self) :
        # TODO: Implement getParentConcreteClassifier method
        pass

    def getConcreteClassifiers(self, commons_packageName, commons_classifierQuery) :
        # TODO: Implement getConcreteClassifiers method
        pass

    def getLibInterface(self, commons_name) :
        # TODO: Implement getLibInterface method
        pass

    def getContainingConcreteClassifier(self) :
        # TODO: Implement getContainingConcreteClassifier method
        pass

    def getClassClass(self) :
        # TODO: Implement getClassClass method
        pass

    def getContainingAnnotationInstance(self) :
        # TODO: Implement getContainingAnnotationInstance method
        pass

    def getConcreteClassifier(self, commons_name) :
        # TODO: Implement getConcreteClassifier method
        pass

class JavaRoot:

    pass
class containers_EmptyModel(JavaRoot):

    pass
class containers_CompilationUnit(JavaRoot):

    def __init__(self, containers_CompilationUnit: set["ConcreteClassifier"] = None):
        self.containers_CompilationUnit = containers_CompilationUnit if containers_CompilationUnit is not None else set()
        
        pass
    @property
    def containers_CompilationUnit(self):
        return self.__containers_CompilationUnit

    @containers_CompilationUnit.setter
    def containers_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_containers_CompilationUnit__containers_CompilationUnit", None)
        self.__containers_CompilationUnit = value if value is not None else set()
        
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
                    

    def getClassifiersInSamePackage(self) :
        # TODO: Implement getClassifiersInSamePackage method
        pass

    def getContainedClassifier(self, containers_name) :
        # TODO: Implement getContainedClassifier method
        pass

class ImportingElement:

    pass
class NamedElement:

    pass
class members_Member(NamedElement):

    pass
class references_ReferenceableElement(NamedElement):

    pass
class containers_JavaRoot(NamespaceAwareElement, ImportingElement, NamedElement):

    def __init__(self):
        
        pass
    def getClassifiersInSamePackage(self) :
        # TODO: Implement getClassifiersInSamePackage method
        pass

class Implementor:

    pass
class ConcreteClassifier:

    pass
class classifiers_Annotation(ConcreteClassifier):

    def __init__(self, ConcreteClassifier96: "imports_ClassifierImport" = None, ConcreteClassifier: "containers_CompilationUnit" = None):
        
        pass
    def getAllSuperClassifiers(self) :
        # TODO: Implement getAllSuperClassifiers method
        pass

class classifiers_Interface(ConcreteClassifier):

    def __init__(self, classifiers_Interface30: set["TypeReference"] = None, classifiers_Interface: set["TypeReference"] = None, ConcreteClassifier96: "imports_ClassifierImport" = None, ConcreteClassifier: "containers_CompilationUnit" = None):
        self.classifiers_Interface30 = classifiers_Interface30 if classifiers_Interface30 is not None else set()
        self.classifiers_Interface = classifiers_Interface if classifiers_Interface is not None else set()
        
        pass
    @property
    def classifiers_Interface30(self):
        return self.__classifiers_Interface30

    @classifiers_Interface30.setter
    def classifiers_Interface30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classifiers_Interface__classifiers_Interface30", None)
        self.__classifiers_Interface30 = value if value is not None else set()
        
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
                    

    @property
    def classifiers_Interface(self):
        return self.__classifiers_Interface

    @classifiers_Interface.setter
    def classifiers_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classifiers_Interface__classifiers_Interface", None)
        self.__classifiers_Interface = value if value is not None else set()
        
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
                    

    def getAllSuperClassifiers(self) :
        # TODO: Implement getAllSuperClassifiers method
        pass

class classifiers_Class(ConcreteClassifier, Implementor):

    def __init__(self, classifiers_Class: "TypeReference" = None, classifiers_Class25: "TypeReference" = None, ConcreteClassifier96: "imports_ClassifierImport" = None, ConcreteClassifier: "containers_CompilationUnit" = None):
        self.classifiers_Class = classifiers_Class
        self.classifiers_Class25 = classifiers_Class25
        
        pass
    @property
    def classifiers_Class25(self):
        return self.__classifiers_Class25

    @classifiers_Class25.setter
    def classifiers_Class25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classifiers_Class__classifiers_Class25", None)
        self.__classifiers_Class25 = value
        
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
    def classifiers_Class(self):
        return self.__classifiers_Class

    @classifiers_Class.setter
    def classifiers_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classifiers_Class__classifiers_Class", None)
        self.__classifiers_Class = value
        
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

    def getSuperClass(self) :
        # TODO: Implement getSuperClass method
        pass

    def getAllSuperClassifiers(self) :
        # TODO: Implement getAllSuperClassifiers method
        pass

    def unWrapPrimitiveType(self) :
        # TODO: Implement unWrapPrimitiveType method
        pass

class TypeReference:

    pass
class types_ClassifierReference(TypeReference, TypeArgumentable):

    pass
class types_NamespaceClassifierReference(TypeReference, NamespaceAwareElement):

    pass
class classifiers_Implementor(Commentable):

    pass
class AnnotableAndModifiable:

    pass
class variables_LocalVariable(Variable, AnnotableAndModifiable, Initializable, ForLoopInitializer):

    pass
class parameters_Parameter(Variable, AnnotableAndModifiable):

    pass
class generics_TypeParameter(Classifier):

    def __init__(self, generics_TypeParameter: set["TypeReference"] = None, Classifier: "annotations_AnnotationInstance" = None, Classifier164: "types_ClassifierReference" = None):
        self.generics_TypeParameter = generics_TypeParameter if generics_TypeParameter is not None else set()
        
        pass
    @property
    def generics_TypeParameter(self):
        return self.__generics_TypeParameter

    @generics_TypeParameter.setter
    def generics_TypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_generics_TypeParameter__generics_TypeParameter", None)
        self.__generics_TypeParameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TypeReference92"):
                    opp_val = getattr(item, "TypeReference92", None)
                    
                    if opp_val == self:
                        setattr(item, "TypeReference92", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TypeReference92"):
                    opp_val = getattr(item, "TypeReference92", None)
                    
                    setattr(item, "TypeReference92", self)
                    

    def getAllSuperClassifiers(self) :
        # TODO: Implement getAllSuperClassifiers method
        pass

    def getAllMembers(self, generics_context) :
        # TODO: Implement getAllMembers method
        pass

    def getBoundType(self, generics_reference, generics_typeReference) :
        # TODO: Implement getBoundType method
        pass

class Statement:

    pass
class statements_Condition(StatementContainer, Statement, Conditional):

    pass
class statements_Throw(Statement):

    pass
class statements_TryBlock(StatementListContainer, Statement):

    pass
class statements_ExpressionStatement(Statement):

    pass
class statements_EmptyStatement(Statement):

    pass
class statements_Switch(Statement):

    pass
class statements_ForEachLoop(StatementContainer, Statement):

    pass
class statements_WhileLoop(StatementContainer, Statement):

    pass
class statements_ForLoop(StatementContainer, Statement, Conditional):

    pass
class statements_Return(Statement):

    pass
class statements_LocalVariableStatement(Statement):

    pass
class statements_JumpLabel(StatementContainer, Statement, NamedElement):

    pass
class statements_Jump(Statement):

    pass
class statements_SynchronizedBlock(StatementListContainer, Statement):

    pass
class statements_Assert(Statement, Conditional):

    pass
class Member:

    pass
class members_EmptyMember(Member):

    pass
class statements_Block(Modifiable, StatementListContainer, Statement, Member):

    pass
class MemberContainer:

    pass
class TypeParametrizable:

    pass
class members_Constructor(AnnotableAndModifiable, Parametrizable, ExceptionThrower, TypeParametrizable, Member, StatementListContainer):

    pass
class classifiers_ConcreteClassifier(AnnotableAndModifiable, MemberContainer, TypeParametrizable, Classifier, Member, Statement):

    def __init__(self, fullName: str, Member: "members_MemberContainer" = None, Member106: "members_MemberContainer" = None, Statement: "statements_StatementContainer" = None, Statement132: "statements_Condition" = None, Statement125: "statements_StatementListContainer" = None, Classifier: "annotations_AnnotationInstance" = None, Classifier164: "types_ClassifierReference" = None):
        self.fullName = fullName
        
        pass
    @property
    def fullName(self):
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName


    def getAllMembers(self, classifiers_context) :
        # TODO: Implement getAllMembers method
        pass

    def getAllInnerClassifiers(self) :
        # TODO: Implement getAllInnerClassifiers method
        pass

    def getSuperTypeReferences(self) :
        # TODO: Implement getSuperTypeReferences method
        pass

    def getInnerClassifiers(self) :
        # TODO: Implement getInnerClassifiers method
        pass

class ReferenceableElement:

    pass
class members_EnumConstant(ReferenceableElement, Annotable, Argumentable):

    pass
class containers_Package(ReferenceableElement, JavaRoot, Annotable):

    pass
class members_Field(AnnotableAndModifiable, Member, ReferenceableElement, Variable, Initializable):

    pass
class TypeParameter:

    pass
class generics_TypeParametrizable(Commentable):

    pass
class Type:

    pass
class types_PrimitiveType(TypeReference, Type):

    def __init__(self, TypeReference162: "types_TypedElement" = None, TypeReference31: "classifiers_Interface" = None, TypeReference: "classifiers_Implementor" = None, TypeReference23: "classifiers_Class" = None, TypeReference28: "classifiers_Interface" = None, TypeReference90: "generics_SuperTypeArgument" = None, TypeReference26: "classifiers_Class" = None, TypeReference92: "generics_TypeParameter" = None, TypeReference88: "generics_ExtendsTypeArgument" = None):
        
        pass
    def getAllMembers(self, types_context) :
        # TODO: Implement getAllMembers method
        pass

    def wrapPrimitiveType(self) :
        # TODO: Implement wrapPrimitiveType method
        pass

class classifiers_AnonymousClass(MemberContainer, Type):

    def __init__(self):
        
        pass
    def getAllSuperClassifiers(self) :
        # TODO: Implement getAllSuperClassifiers method
        pass

    def getAllMembers(self, classifiers_context) :
        # TODO: Implement getAllMembers method
        pass

    def getSuperClassifier(self) :
        # TODO: Implement getSuperClassifier method
        pass

class generics_CallTypeArgumentable(Commentable):

    pass
class classifiers_Classifier(ReferenceableElement, Type):

    def __init__(self, ReferenceableElement119: "references_ElementReference" = None, ReferenceableElement: "imports_StaticMemberImport" = None):
        
        pass
    def getAllSuperClassifiers(self) :
        # TODO: Implement getAllSuperClassifiers method
        pass

class TypeArgument:

    pass
class generics_SuperTypeArgument(TypeArgument):

    pass
class generics_ExtendsTypeArgument(TypeArgument):

    pass
class generics_UnknownTypeArgument(TypeArgument):

    pass
class EnumConstant:

    pass
class generics_TypeArgumentable(Commentable):

    pass
class arrays_ArraySelector(Commentable):

    pass
class classifiers_Enumeration(Implementor, ConcreteClassifier):

    def __init__(self, classifiers_Enumeration: set["EnumConstant"] = None, ConcreteClassifier96: "imports_ClassifierImport" = None, ConcreteClassifier: "containers_CompilationUnit" = None):
        self.classifiers_Enumeration = classifiers_Enumeration if classifiers_Enumeration is not None else set()
        
        pass
    @property
    def classifiers_Enumeration(self):
        return self.__classifiers_Enumeration

    @classifiers_Enumeration.setter
    def classifiers_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classifiers_Enumeration__classifiers_Enumeration", None)
        self.__classifiers_Enumeration = value if value is not None else set()
        
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
                    

    def getContainedConstant(self, classifiers_name) :
        # TODO: Implement getContainedConstant method
        pass

    def getAllSuperClassifiers(self) :
        # TODO: Implement getAllSuperClassifiers method
        pass

class StaticImport:

    pass
class imports_StaticMemberImport(StaticImport):

    pass
class imports_StaticClassifierImport(StaticImport):

    pass
class arrays_ArrayInitializationValue(Commentable):

    pass
class ArrayInitializationValue:

    pass
class expressions_Expression(ArrayInitializationValue, AnnotationValue):

    def __init__(self, ArrayInitializationValue: "arrays_ArrayInitializer" = None, AnnotationValue9: "annotations_AnnotationAttributeSetting" = None, AnnotationValue: "annotations_SingleAnnotationParameter" = None):
        
        pass
    def getAlternativeType(self) :
        # TODO: Implement getAlternativeType method
        pass

    def getType(self) :
        # TODO: Implement getType method
        pass

    def getOneType(self, expressions_alternative) :
        # TODO: Implement getOneType method
        pass

    def getArrayDimension(self) :
        # TODO: Implement getArrayDimension method
        pass

class arrays_ArrayInitializer(ArrayInitializationValue, AnnotationValue):

    pass
class Static:

    pass
class arrays_ArrayDimension(Commentable):

    pass
class ArrayDimension:

    pass
class Import:

    pass
class imports_PackageImport(Import):

    pass
class imports_ClassifierImport(Import):

    pass
class imports_StaticImport(Import):

    pass
class arrays_ArrayTypeable(Commentable):

    def __init__(self, arrays_ArrayTypeable: set["ArrayDimension"] = None, arrays_ArrayTypeable13: set["ArrayDimension"] = None):
        self.arrays_ArrayTypeable = arrays_ArrayTypeable if arrays_ArrayTypeable is not None else set()
        self.arrays_ArrayTypeable13 = arrays_ArrayTypeable13 if arrays_ArrayTypeable13 is not None else set()
        
        pass
    @property
    def arrays_ArrayTypeable13(self):
        return self.__arrays_ArrayTypeable13

    @arrays_ArrayTypeable13.setter
    def arrays_ArrayTypeable13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arrays_ArrayTypeable__arrays_ArrayTypeable13", None)
        self.__arrays_ArrayTypeable13 = value if value is not None else set()
        
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
    def arrays_ArrayTypeable(self):
        return self.__arrays_ArrayTypeable

    @arrays_ArrayTypeable.setter
    def arrays_ArrayTypeable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arrays_ArrayTypeable__arrays_ArrayTypeable", None)
        self.__arrays_ArrayTypeable = value if value is not None else set()
        
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
                    

    def getArrayDimension(self) :
        # TODO: Implement getArrayDimension method
        pass

class Expression:

    pass
class expressions_AssignmentExpression(Expression):

    pass
class expressions_AssignmentExpressionChild(Expression):

    pass
class annotations_AnnotationValue(Commentable):

    pass
class UnaryModificationExpression:

    pass
class expressions_SuffixUnaryModificationExpression(UnaryModificationExpression):

    pass
class InterfaceMethod:

    pass
class annotations_AnnotationAttribute(InterfaceMethod):

    pass
class expressions_PrefixUnaryModificationExpression(UnaryModificationExpression):

    pass
class annotations_AnnotationAttributeSetting(Commentable):

    pass
class UnaryModificationOperator:

    pass
class operators_PlusPlus(UnaryModificationOperator):

    pass
class operators_MinusMinus(UnaryModificationOperator):

    pass
class AnnotationAttributeSetting:

    pass
class UnaryModificationExpressionChild:

    pass
class expressions_PrimaryExpression(UnaryModificationExpressionChild):

    pass
class annotations_AnnotationParameterList(AnnotationParameter):

    pass
class ArrayInitializer:

    pass
class expressions_UnaryExpressionChild(MultiplicativeExpressionChild):

    pass
class UnaryExpressionChild:

    pass
class expressions_UnaryModificationExpressionChild(UnaryExpressionChild):

    pass
class expressions_UnaryModificationExpression(UnaryExpressionChild):

    pass
class ArrayTypeable:

    pass
class members_AdditionalField(ReferenceableElement, Initializable, ArrayTypeable):

    def __init__(self, ReferenceableElement119: "references_ElementReference" = None, ReferenceableElement: "imports_StaticMemberImport" = None):
        
        pass
    def getArrayDimension(self) :
        # TODO: Implement getArrayDimension method
        pass

class variables_AdditionalLocalVariable(ReferenceableElement, Initializable, ArrayTypeable):

    def __init__(self, ReferenceableElement119: "references_ElementReference" = None, ReferenceableElement: "imports_StaticMemberImport" = None):
        
        pass
    def getArrayDimension(self) :
        # TODO: Implement getArrayDimension method
        pass

class UnaryOperator:

    pass
class operators_Subtraction(UnaryOperator, AdditiveOperator):

    pass
class operators_Complement(UnaryOperator):

    pass
class operators_Addition(UnaryOperator, AdditiveOperator):

    pass
class operators_Negate(UnaryOperator):

    pass
class TypedElement:

    pass
class instantiations_Instantiation(Argumentable, Reference, TypedElement, TypeArgumentable):

    pass
class expressions_CastExpression(UnaryModificationExpressionChild, TypedElement, ArrayTypeable):

    pass
class variables_Variable(TypedElement, TypeArgumentable, ArrayTypeable, NamedElement, ReferenceableElement):

    def __init__(self, ReferenceableElement119: "references_ElementReference" = None, ReferenceableElement: "imports_StaticMemberImport" = None):
        
        pass
    def getArrayDimension(self) :
        # TODO: Implement getArrayDimension method
        pass

class arrays_ArrayInstantiationBySize(Expression, Reference, TypedElement, ArrayTypeable):

    pass
class arrays_ArrayInstantiationByValues(Expression, Reference, TypedElement, ArrayTypeable):

    pass
class expressions_InstanceOfExpression(EqualityExpressionChild, TypedElement, ArrayTypeable):

    pass
class members_Method(AnnotableAndModifiable, Parametrizable, ExceptionThrower, TypeParametrizable, TypedElement, Member, ArrayTypeable, ReferenceableElement):

    def __init__(self, ReferenceableElement119: "references_ElementReference" = None, ReferenceableElement: "imports_StaticMemberImport" = None, Member: "members_MemberContainer" = None, Member106: "members_MemberContainer" = None):
        
        pass
    def isMethodForCall(self, members_needsPerfectMatch, members_methodCall) :
        # TODO: Implement isMethodForCall method
        pass

    def isSomeMethodForCall(self, members_methodCall) :
        # TODO: Implement isSomeMethodForCall method
        pass

    def getArrayDimension(self) :
        # TODO: Implement getArrayDimension method
        pass

    def isBetterMethodForCall(self, members_methodCall, members_otherMethod) :
        # TODO: Implement isBetterMethodForCall method
        pass

class generics_QualifiedTypeArgument(TypeArgument, TypedElement):

    pass
class expressions_UnaryExpression(MultiplicativeExpressionChild):

    pass
class generics_TypeArgument(ArrayTypeable):

    pass
class annotations_AnnotationInstance(Reference, AnnotationInstanceOrModifier, NamespaceAwareElement):

    pass
class AnnotationInstance:

    pass