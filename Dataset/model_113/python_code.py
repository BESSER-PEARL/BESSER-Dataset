from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PrimitiveType:

    pass
class java_Char(PrimitiveType):

    pass
class java_Long(PrimitiveType):

    pass
class java_Float(PrimitiveType):

    pass
class java_Byte(PrimitiveType):

    pass
class java_Int(PrimitiveType):

    pass
class java_Double(PrimitiveType):

    pass
class java_Short(PrimitiveType):

    pass
class java_Boolean(PrimitiveType):

    pass
class java_Void(PrimitiveType):

    pass
class TypeReference:

    pass
class WhileLoop:

    pass
class java_DoWhileLoop(WhileLoop):

    pass
class SwitchCase:

    pass
class java_DefaultSwitchCase(SwitchCase):

    pass
class StatementContainer:

    pass
class Modifiable:

    pass
class Jump:

    pass
class java_Continue(Jump):

    pass
class java_Break(Jump):

    pass
class Conditional:

    pass
class java_NormalSwitchCase(Conditional, SwitchCase):

    pass
class ElementReference:

    pass
class java_IdentifierReference(ElementReference):

    pass
class Parameter:

    pass
class java_VariableLengthParameter(Parameter):

    pass
class java_OrdinaryParameter(Parameter):

    pass
class UnaryModificationOperator:

    pass
class java_MinusMinus(UnaryModificationOperator):

    pass
class TypeArgumentable:

    pass
class java_ClassifierReference(TypeArgumentable, TypeReference):

    pass
class ShiftOperator:

    pass
class java_UnsignedRightShift(ShiftOperator):

    pass
class java_RightShift(ShiftOperator):

    pass
class java_LeftShift(ShiftOperator):

    pass
class EqualityOperator:

    pass
class java_Equal(EqualityOperator):

    pass
class java_PlusPlus(UnaryModificationOperator):

    pass
class MultiplicativeOperator:

    pass
class java_Remainder(MultiplicativeOperator):

    pass
class java_Multiplication(MultiplicativeOperator):

    pass
class java_Division(MultiplicativeOperator):

    pass
class UnaryOperator:

    pass
class java_Negate(UnaryOperator):

    pass
class java_Complement(UnaryOperator):

    pass
class AdditiveOperator:

    pass
class java_Subtraction(AdditiveOperator, UnaryOperator):

    pass
class java_Addition(AdditiveOperator, UnaryOperator):

    pass
class RelationOperator:

    pass
class java_GreaterThanOrEqual(RelationOperator):

    pass
class java_LessThanOrEqual(RelationOperator):

    pass
class java_LessThan(RelationOperator):

    pass
class java_GreaterThan(RelationOperator):

    pass
class java_NotEqual(EqualityOperator):

    pass
class AssignmentOperator:

    pass
class java_AssignmentAnd(AssignmentOperator):

    pass
class java_AssignmentRightShift(AssignmentOperator):

    pass
class java_AssignmentModulo(AssignmentOperator):

    pass
class java_AssignmentPlus(AssignmentOperator):

    pass
class java_AssignmentMultiplication(AssignmentOperator):

    pass
class java_AssignmentExclusiveOr(AssignmentOperator):

    pass
class java_AssignmentMinus(AssignmentOperator):

    pass
class java_AssignmentDivision(AssignmentOperator):

    pass
class java_AssignmentUnsignedRightShift(AssignmentOperator):

    pass
class java_AssignmentLeftShift(AssignmentOperator):

    pass
class java_AssignmentOr(AssignmentOperator):

    pass
class java_Assignment(AssignmentOperator):

    pass
class Modifier:

    pass
class java_Native(Modifier):

    pass
class java_Final(Modifier):

    pass
class java_Abstract(Modifier):

    pass
class Operator:

    pass
class java_Volatile(Modifier):

    pass
class java_Transient(Modifier):

    pass
class java_Synchronized(Modifier):

    pass
class java_Strictfp(Modifier):

    pass
class java_Private(Modifier):

    pass
class java_Public(Modifier):

    pass
class java_Protected(Modifier):

    pass
class Method:

    pass
class Variable:

    pass
class ExceptionThrower:

    pass
class Parametrizable:

    pass
class StatementListContainer:

    pass
class java_SwitchCase(StatementListContainer):

    pass
class java_ClassMethod(Method, StatementListContainer):

    pass
class java_CatchBlock(StatementListContainer):

    pass
class Initializable:

    pass
class Self:

    pass
class java_This(Self):

    pass
class java_Super(Self):

    pass
class LongLiteral:

    pass
class java_OctalLongLiteral(LongLiteral):

    def __init__(self, octalValue: str):
        self.octalValue = octalValue
        
    @property
    def octalValue(self) -> str:
        return self.__octalValue

    @octalValue.setter
    def octalValue(self, octalValue: str):
        self.__octalValue = octalValue

class java_HexLongLiteral(LongLiteral):

    def __init__(self, hexValue: str):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> str:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: str):
        self.__hexValue = hexValue

class java_DecimalLongLiteral(LongLiteral):

    def __init__(self, decimalValue: str):
        self.decimalValue = decimalValue
        
    @property
    def decimalValue(self) -> str:
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: str):
        self.__decimalValue = decimalValue

class IntegerLiteral:

    pass
class java_DecimalIntegerLiteral(IntegerLiteral):

    def __init__(self, decimalValue: str):
        self.decimalValue = decimalValue
        
    @property
    def decimalValue(self) -> str:
        return self.__decimalValue

    @decimalValue.setter
    def decimalValue(self, decimalValue: str):
        self.__decimalValue = decimalValue

class java_OctalIntegerLiteral(IntegerLiteral):

    def __init__(self, octalValue: str):
        self.octalValue = octalValue
        
    @property
    def octalValue(self) -> str:
        return self.__octalValue

    @octalValue.setter
    def octalValue(self, octalValue: str):
        self.__octalValue = octalValue

class java_HexIntegerLiteral(IntegerLiteral):

    def __init__(self, hexValue: str):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> str:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: str):
        self.__hexValue = hexValue

class DoubleLiteral:

    pass
class java_HexDoubleLiteral(DoubleLiteral):

    def __init__(self, hexValue: float):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> float:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: float):
        self.__hexValue = hexValue

class java_DecimalDoubleLiteral(DoubleLiteral):

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
class java_HexFloatLiteral(FloatLiteral):

    def __init__(self, hexValue: float):
        self.hexValue = hexValue
        
    @property
    def hexValue(self) -> float:
        return self.__hexValue

    @hexValue.setter
    def hexValue(self, hexValue: float):
        self.__hexValue = hexValue

class java_DecimalFloatLiteral(FloatLiteral):

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
class java_FloatLiteral(Literal):

    pass
class java_NullLiteral(Literal):

    pass
class java_DoubleLiteral(Literal):

    pass
class java_IntegerLiteral(Literal):

    pass
class java_LongLiteral(Literal):

    pass
class java_CharacterLiteral(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class java_BooleanLiteral(Literal):

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
class java_Reference(TypeArgumentable, PrimaryExpression):

    def __init__(self, java_Reference: "java_Reference" = None, java_Reference117: "java_Reference" = None, java_Reference120: set["java_ArraySelector"] = None):
        self.java_Reference = java_Reference
        self.java_Reference117 = java_Reference117
        self.java_Reference120 = java_Reference120 if java_Reference120 is not None else set()
        
    @property
    def java_Reference(self):
        return self.__java_Reference

    @java_Reference.setter
    def java_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Reference__java_Reference", None)
        self.__java_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Reference117"):
                opp_val = getattr(old_value, "java_Reference117", None)
                if opp_val == self:
                    setattr(old_value, "java_Reference117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Reference117"):
                opp_val = getattr(value, "java_Reference117", None)
                setattr(value, "java_Reference117", self)

    @property
    def java_Reference117(self):
        return self.__java_Reference117

    @java_Reference117.setter
    def java_Reference117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Reference__java_Reference117", None)
        self.__java_Reference117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Reference"):
                opp_val = getattr(old_value, "java_Reference", None)
                if opp_val == self:
                    setattr(old_value, "java_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Reference"):
                opp_val = getattr(value, "java_Reference", None)
                setattr(value, "java_Reference", self)

    @property
    def java_Reference120(self):
        return self.__java_Reference120

    @java_Reference120.setter
    def java_Reference120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Reference__java_Reference120", None)
        self.__java_Reference120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ArraySelector121"):
                    opp_val = getattr(item, "java_ArraySelector121", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ArraySelector121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ArraySelector121"):
                    opp_val = getattr(item, "java_ArraySelector121", None)
                    
                    setattr(item, "java_ArraySelector121", self)
                    

    def getReferencedType(self) -> Type:
        # TODO: Implement getReferencedType method
        pass

    def getPrevious(self) -> Reference:
        # TODO: Implement getPrevious method
        pass

class java_Literal(PrimaryExpression):

    def __init__(self):
        
    def getOneType(self, alternative: bool) -> Type:
        # TODO: Implement getOneType method
        pass

class CallTypeArgumentable:

    pass
class Instantiation:

    pass
class java_ExplicitConstructorCall(Instantiation):

    pass
class Argumentable:

    pass
class java_MethodCall(ElementReference, CallTypeArgumentable, Argumentable):

    pass
class Import:

    pass
class java_StaticImport(Import):

    pass
class StaticImport:

    pass
class java_StaticMemberImport(StaticImport):

    pass
class java_StaticClassifierImport(StaticImport):

    pass
class java_PackageImport(Import):

    pass
class java_ClassifierImport(Import):

    pass
class java_Static(Modifier):

    pass
class UnaryModificationExpressionChild:

    pass
class java_PrimaryExpression(UnaryModificationExpressionChild):

    pass
class TypeArgument:

    pass
class java_UnknownTypeArgument(TypeArgument):

    pass
class java_SuperTypeArgument(TypeArgument):

    pass
class java_ExtendsTypeArgument(TypeArgument):

    pass
class java_UnaryOperator(Operator):

    pass
class MultiplicativeExpressionChild:

    pass
class java_UnaryExpression(MultiplicativeExpressionChild):

    pass
class java_MultiplicativeOperator(Operator):

    pass
class AdditiveExpressionChild:

    pass
class java_MultiplicativeExpressionChild(AdditiveExpressionChild):

    pass
class java_MultiplicativeExpression(AdditiveExpressionChild):

    pass
class UnaryModificationExpression:

    pass
class java_SuffixUnaryModificationExpression(UnaryModificationExpression):

    pass
class java_PrefixUnaryModificationExpression(UnaryModificationExpression):

    pass
class java_UnaryModificationOperator(Operator):

    pass
class UnaryExpressionChild:

    pass
class java_UnaryModificationExpressionChild(UnaryExpressionChild):

    pass
class java_UnaryModificationExpression(UnaryExpressionChild):

    pass
class java_UnaryExpressionChild(MultiplicativeExpressionChild):

    pass
class RelationExpressionChild:

    pass
class java_ShiftExpressionChild(RelationExpressionChild):

    pass
class java_ShiftExpression(RelationExpressionChild):

    pass
class java_RelationOperator(Operator):

    pass
class InstanceOfExpressionChild:

    pass
class java_RelationExpressionChild(InstanceOfExpressionChild):

    pass
class java_RelationExpression(InstanceOfExpressionChild):

    pass
class java_AdditiveOperator(Operator):

    pass
class ShiftExpressionChild:

    pass
class java_AdditiveExpressionChild(ShiftExpressionChild):

    pass
class java_AdditiveExpression(ShiftExpressionChild):

    pass
class java_ShiftOperator(Operator):

    pass
class java_EqualityOperator(Operator):

    pass
class AndExpressionChild:

    pass
class java_EqualityExpression(AndExpressionChild):

    pass
class ExclusiveOrExpressionChild:

    pass
class java_AndExpressionChild(ExclusiveOrExpressionChild):

    pass
class java_AndExpression(ExclusiveOrExpressionChild):

    pass
class EqualityExpressionChild:

    pass
class java_InstanceOfExpressionChild(EqualityExpressionChild):

    pass
class java_EqualityExpressionChild(AndExpressionChild):

    pass
class ConditionalOrExpressionChild:

    pass
class java_ConditionalAndExpressionChild(ConditionalOrExpressionChild):

    pass
class java_ConditionalAndExpression(ConditionalOrExpressionChild):

    pass
class ConditionalExpressionChild:

    pass
class java_ConditionalOrExpressionChild(ConditionalExpressionChild):

    pass
class java_ConditionalOrExpression(ConditionalExpressionChild):

    pass
class InclusiveOrExpressionChild:

    pass
class java_ExclusiveOrExpressionChild(InclusiveOrExpressionChild):

    pass
class java_ExclusiveOrExpression(InclusiveOrExpressionChild):

    pass
class ConditionalAndExpressionChild:

    pass
class java_InclusiveOrExpressionChild(ConditionalAndExpressionChild):

    pass
class java_InclusiveOrExpression(ConditionalAndExpressionChild):

    pass
class java_AssignmentOperator(Operator):

    pass
class AssignmentExpressionChild:

    pass
class java_ConditionalExpressionChild(AssignmentExpressionChild):

    pass
class java_ConditionalExpression(AssignmentExpressionChild):

    pass
class ForLoopInitializer:

    pass
class java_ExpressionList(ForLoopInitializer):

    pass
class JavaRoot:

    pass
class java_EmptyModel(JavaRoot):

    pass
class java_CompilationUnit(JavaRoot):

    def __init__(self, java_CompilationUnit39: "java_Package" = None, java_CompilationUnit: set["java_ConcreteClassifier"] = None):
        self.java_CompilationUnit39 = java_CompilationUnit39
        self.java_CompilationUnit = java_CompilationUnit if java_CompilationUnit is not None else set()
        
    @property
    def java_CompilationUnit(self):
        return self.__java_CompilationUnit

    @java_CompilationUnit.setter
    def java_CompilationUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit", None)
        self.__java_CompilationUnit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ConcreteClassifier"):
                    opp_val = getattr(item, "java_ConcreteClassifier", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ConcreteClassifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ConcreteClassifier"):
                    opp_val = getattr(item, "java_ConcreteClassifier", None)
                    
                    setattr(item, "java_ConcreteClassifier", self)
                    

    @property
    def java_CompilationUnit39(self):
        return self.__java_CompilationUnit39

    @java_CompilationUnit39.setter
    def java_CompilationUnit39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_CompilationUnit__java_CompilationUnit39", None)
        self.__java_CompilationUnit39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Package"):
                opp_val = getattr(old_value, "java_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Package"):
                opp_val = getattr(value, "java_Package", None)
                if opp_val is None:
                    setattr(value, "java_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getClassifiersInSamePackage(self) -> ConcreteClassifier:
        # TODO: Implement getClassifiersInSamePackage method
        pass

    def getContainedClassifier(self, name: str) -> ConcreteClassifier:
        # TODO: Implement getContainedClassifier method
        pass

class Annotable:

    pass
class java_Package(Annotable, JavaRoot):

    def __init__(self, java_Package: set["java_CompilationUnit"] = None):
        self.java_Package = java_Package if java_Package is not None else set()
        
    @property
    def java_Package(self):
        return self.__java_Package

    @java_Package.setter
    def java_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Package__java_Package", None)
        self.__java_Package = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_CompilationUnit39"):
                    opp_val = getattr(item, "java_CompilationUnit39", None)
                    
                    if opp_val == self:
                        setattr(item, "java_CompilationUnit39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_CompilationUnit39"):
                    opp_val = getattr(item, "java_CompilationUnit39", None)
                    
                    setattr(item, "java_CompilationUnit39", self)
                    

    def getClassifiersInSamePackage(self) -> ConcreteClassifier:
        # TODO: Implement getClassifiersInSamePackage method
        pass

    def getNamespacesAsString(self) -> str:
        # TODO: Implement getNamespacesAsString method
        pass

class java_LayoutInformation:

    pass
class ImportingElement:

    pass
class NamedElement:

    pass
class java_Member(NamedElement):

    pass
class java_ReferenceableElement(NamedElement):

    pass
class java_Commentable(ABC):

    def __init__(self, java_Commentable: set["java_LayoutInformation"] = None):
        self.java_Commentable = java_Commentable if java_Commentable is not None else set()
        
    @property
    def java_Commentable(self):
        return self.__java_Commentable

    @java_Commentable.setter
    def java_Commentable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Commentable__java_Commentable", None)
        self.__java_Commentable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_LayoutInformation"):
                    opp_val = getattr(item, "java_LayoutInformation", None)
                    
                    if opp_val == self:
                        setattr(item, "java_LayoutInformation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_LayoutInformation"):
                    opp_val = getattr(item, "java_LayoutInformation", None)
                    
                    setattr(item, "java_LayoutInformation", self)
                    

    def getAnnotationInterface(self) -> str:
        # TODO: Implement getAnnotationInterface method
        pass

    def getConcreteClassifiers(self, classifierQuery: str, packageName: str) -> ConcreteClassifier:
        # TODO: Implement getConcreteClassifiers method
        pass

    def getConcreteClassifierProxy(self, name: str) -> ConcreteClassifier:
        # TODO: Implement getConcreteClassifierProxy method
        pass

    def getContainingCompilationUnit(self) -> str:
        # TODO: Implement getContainingCompilationUnit method
        pass

    def getParentByEType(self, type: str) -> str:
        # TODO: Implement getParentByEType method
        pass

    def getChildrenByEType(self, type: str) -> str:
        # TODO: Implement getChildrenByEType method
        pass

    def getContainingPackageName(self) -> str:
        # TODO: Implement getContainingPackageName method
        pass

    def getContainingAnonymousClass(self) -> str:
        # TODO: Implement getContainingAnonymousClass method
        pass

    def getLibInterface(self, name: str) -> str:
        # TODO: Implement getLibInterface method
        pass

    def getConcreteClassifier(self, name: str) -> ConcreteClassifier:
        # TODO: Implement getConcreteClassifier method
        pass

    def getContainingConcreteClassifier(self) -> ConcreteClassifier:
        # TODO: Implement getContainingConcreteClassifier method
        pass

    def getContainingAnnotationInstance(self) -> str:
        # TODO: Implement getContainingAnnotationInstance method
        pass

    def getParentByType(self, type: str):
        # TODO: Implement getParentByType method
        pass

    def getComments(self) -> str:
        # TODO: Implement getComments method
        pass

    def getConcreteClassifierProxies(self, packageName: str, classifierQuery: str) -> ConcreteClassifier:
        # TODO: Implement getConcreteClassifierProxies method
        pass

    def getChildrenByType(self, type: str):
        # TODO: Implement getChildrenByType method
        pass

    def getFirstChildByEType(self, type: str) -> str:
        # TODO: Implement getFirstChildByEType method
        pass

    def getStringClass(self) -> str:
        # TODO: Implement getStringClass method
        pass

    def getLibClass(self, name: str) -> str:
        # TODO: Implement getLibClass method
        pass

    def addBeforeContainingStatement(self, statementToAdd: Statement):
        # TODO: Implement addBeforeContainingStatement method
        pass

    def getClassClass(self) -> str:
        # TODO: Implement getClassClass method
        pass

    def addAfterContainingStatement(self, statementToAdd: Statement):
        # TODO: Implement addAfterContainingStatement method
        pass

    def getFirstChildByType(self, type: str):
        # TODO: Implement getFirstChildByType method
        pass

    def getParentConcreteClassifier(self) -> ConcreteClassifier:
        # TODO: Implement getParentConcreteClassifier method
        pass

    def getObjectClass(self) -> str:
        # TODO: Implement getObjectClass method
        pass

class Implementor:

    pass
class ConcreteClassifier:

    pass
class java_Annotation(ConcreteClassifier):

    def __init__(self):
        
    def getAllSuperClassifiers(self) -> ConcreteClassifier:
        # TODO: Implement getAllSuperClassifiers method
        pass

class java_Enumeration(ConcreteClassifier, Implementor):

    def __init__(self, java_Enumeration: set["java_EnumConstant"] = None):
        self.java_Enumeration = java_Enumeration if java_Enumeration is not None else set()
        
    @property
    def java_Enumeration(self):
        return self.__java_Enumeration

    @java_Enumeration.setter
    def java_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Enumeration__java_Enumeration", None)
        self.__java_Enumeration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_EnumConstant"):
                    opp_val = getattr(item, "java_EnumConstant", None)
                    
                    if opp_val == self:
                        setattr(item, "java_EnumConstant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_EnumConstant"):
                    opp_val = getattr(item, "java_EnumConstant", None)
                    
                    setattr(item, "java_EnumConstant", self)
                    

    def getContainedConstant(self, name: str) -> str:
        # TODO: Implement getContainedConstant method
        pass

    def getAllSuperClassifiers(self) -> ConcreteClassifier:
        # TODO: Implement getAllSuperClassifiers method
        pass

class java_Class(ConcreteClassifier, Implementor):

    def __init__(self, java_Class: "java_TypeReference" = None, java_Class28: "java_TypeReference" = None):
        self.java_Class = java_Class
        self.java_Class28 = java_Class28
        
    @property
    def java_Class28(self):
        return self.__java_Class28

    @java_Class28.setter
    def java_Class28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class__java_Class28", None)
        self.__java_Class28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeReference29"):
                opp_val = getattr(old_value, "java_TypeReference29", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeReference29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeReference29"):
                opp_val = getattr(value, "java_TypeReference29", None)
                setattr(value, "java_TypeReference29", self)

    @property
    def java_Class(self):
        return self.__java_Class

    @java_Class.setter
    def java_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class__java_Class", None)
        self.__java_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeReference26"):
                opp_val = getattr(old_value, "java_TypeReference26", None)
                if opp_val == self:
                    setattr(old_value, "java_TypeReference26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeReference26"):
                opp_val = getattr(value, "java_TypeReference26", None)
                setattr(value, "java_TypeReference26", self)

    def unWrapPrimitiveType(self) -> str:
        # TODO: Implement unWrapPrimitiveType method
        pass

    def getAllSuperClassifiers(self) -> ConcreteClassifier:
        # TODO: Implement getAllSuperClassifiers method
        pass

    def getSuperClass(self) -> str:
        # TODO: Implement getSuperClass method
        pass

class java_Interface(ConcreteClassifier):

    def __init__(self, java_Interface: set["java_TypeReference"] = None, java_Interface33: set["java_TypeReference"] = None):
        self.java_Interface = java_Interface if java_Interface is not None else set()
        self.java_Interface33 = java_Interface33 if java_Interface33 is not None else set()
        
    @property
    def java_Interface33(self):
        return self.__java_Interface33

    @java_Interface33.setter
    def java_Interface33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Interface__java_Interface33", None)
        self.__java_Interface33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_TypeReference34"):
                    opp_val = getattr(item, "java_TypeReference34", None)
                    
                    if opp_val == self:
                        setattr(item, "java_TypeReference34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_TypeReference34"):
                    opp_val = getattr(item, "java_TypeReference34", None)
                    
                    setattr(item, "java_TypeReference34", self)
                    

    @property
    def java_Interface(self):
        return self.__java_Interface

    @java_Interface.setter
    def java_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Interface__java_Interface", None)
        self.__java_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_TypeReference31"):
                    opp_val = getattr(item, "java_TypeReference31", None)
                    
                    if opp_val == self:
                        setattr(item, "java_TypeReference31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_TypeReference31"):
                    opp_val = getattr(item, "java_TypeReference31", None)
                    
                    setattr(item, "java_TypeReference31", self)
                    

    def getAllSuperClassifiers(self) -> ConcreteClassifier:
        # TODO: Implement getAllSuperClassifiers method
        pass

class ArrayInstantiationByValues:

    pass
class java_ArrayInstantiationByValuesUntyped(ArrayInstantiationByValues):

    pass
class ArrayTypeable:

    pass
class java_TypeArgument(ArrayTypeable):

    pass
class TypedElement:

    pass
class java_CastExpression(ArrayTypeable, TypedElement, UnaryModificationExpressionChild):

    pass
class java_InstanceOfExpression(EqualityExpressionChild, ArrayTypeable, TypedElement):

    pass
class java_NewConstructorCall(Instantiation, CallTypeArgumentable, TypedElement):

    pass
class java_QualifiedTypeArgument(TypeArgument, TypedElement):

    pass
class ArrayInstantiation:

    pass
class java_ArrayInstantiationByValues(ArrayInstantiation):

    pass
class java_ArrayInstantiationBySize(ArrayTypeable, ArrayInstantiation, TypedElement):

    pass
class Expression:

    pass
class java_AssignmentExpression(Expression):

    pass
class java_AssignmentExpressionChild(Expression):

    pass
class AnnotableAndModifiable:

    pass
class java_Parameter(AnnotableAndModifiable, Variable):

    pass
class java_LocalVariable(Variable, Initializable, AnnotableAndModifiable, ForLoopInitializer):

    pass
class Statement:

    pass
class java_Assert(Conditional, Statement):

    pass
class java_Switch(Statement):

    pass
class java_ForLoop(Conditional, StatementContainer, Statement):

    pass
class java_Throw(Statement):

    pass
class java_Jump(Statement):

    pass
class java_Condition(Conditional, StatementContainer, Statement):

    pass
class java_EmptyStatement(Statement):

    pass
class java_SynchronizedBlock(StatementListContainer, Statement):

    pass
class java_WhileLoop(StatementContainer, Statement):

    pass
class java_Return(Statement):

    pass
class java_LocalVariableStatement(Statement):

    pass
class java_ExpressionStatement(Statement):

    pass
class java_TryBlock(StatementListContainer, Statement):

    pass
class java_JumpLabel(NamedElement, StatementContainer, Statement):

    pass
class java_ForEachLoop(StatementContainer, Statement):

    pass
class Member:

    pass
class java_Block(StatementListContainer, Member, Modifiable, Statement):

    pass
class java_EmptyMember(Member):

    pass
class MemberContainer:

    pass
class TypeParametrizable:

    pass
class java_Constructor(AnnotableAndModifiable, StatementListContainer, Parametrizable, TypeParametrizable, ExceptionThrower, Member):

    pass
class Classifier:

    pass
class java_TypeParameter(Classifier):

    def __init__(self, java_TypeParameter: "java_TypeParametrizable" = None, java_TypeParameter95: set["java_TypeReference"] = None):
        self.java_TypeParameter = java_TypeParameter
        self.java_TypeParameter95 = java_TypeParameter95 if java_TypeParameter95 is not None else set()
        
    @property
    def java_TypeParameter95(self):
        return self.__java_TypeParameter95

    @java_TypeParameter95.setter
    def java_TypeParameter95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeParameter__java_TypeParameter95", None)
        self.__java_TypeParameter95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_TypeReference96"):
                    opp_val = getattr(item, "java_TypeReference96", None)
                    
                    if opp_val == self:
                        setattr(item, "java_TypeReference96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_TypeReference96"):
                    opp_val = getattr(item, "java_TypeReference96", None)
                    
                    setattr(item, "java_TypeReference96", self)
                    

    @property
    def java_TypeParameter(self):
        return self.__java_TypeParameter

    @java_TypeParameter.setter
    def java_TypeParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeParameter__java_TypeParameter", None)
        self.__java_TypeParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeParametrizable"):
                opp_val = getattr(old_value, "java_TypeParametrizable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeParametrizable"):
                opp_val = getattr(value, "java_TypeParametrizable", None)
                if opp_val is None:
                    setattr(value, "java_TypeParametrizable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getBoundType(self, reference: Reference, typeReference: str) -> Type:
        # TODO: Implement getBoundType method
        pass

    def getAllMembers(self, context: Commentable) -> Member:
        # TODO: Implement getAllMembers method
        pass

    def getAllSuperClassifiers(self) -> ConcreteClassifier:
        # TODO: Implement getAllSuperClassifiers method
        pass

class java_ConcreteClassifier(AnnotableAndModifiable, TypeParametrizable, Member, Statement, Classifier, MemberContainer):

    def __init__(self, java_ConcreteClassifier: "java_CompilationUnit" = None, java_ConcreteClassifier100: "java_ClassifierImport" = None):
        self.java_ConcreteClassifier = java_ConcreteClassifier
        self.java_ConcreteClassifier100 = java_ConcreteClassifier100
        
    @property
    def java_ConcreteClassifier(self):
        return self.__java_ConcreteClassifier

    @java_ConcreteClassifier.setter
    def java_ConcreteClassifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ConcreteClassifier__java_ConcreteClassifier", None)
        self.__java_ConcreteClassifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_CompilationUnit"):
                opp_val = getattr(old_value, "java_CompilationUnit", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_CompilationUnit"):
                opp_val = getattr(value, "java_CompilationUnit", None)
                if opp_val is None:
                    setattr(value, "java_CompilationUnit", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_ConcreteClassifier100(self):
        return self.__java_ConcreteClassifier100

    @java_ConcreteClassifier100.setter
    def java_ConcreteClassifier100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ConcreteClassifier__java_ConcreteClassifier100", None)
        self.__java_ConcreteClassifier100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ClassifierImport"):
                opp_val = getattr(old_value, "java_ClassifierImport", None)
                if opp_val == self:
                    setattr(old_value, "java_ClassifierImport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ClassifierImport"):
                opp_val = getattr(value, "java_ClassifierImport", None)
                setattr(value, "java_ClassifierImport", self)

    def getSuperTypeReferences(self) -> str:
        # TODO: Implement getSuperTypeReferences method
        pass

    def getInnerClassifiers(self) -> str:
        # TODO: Implement getInnerClassifiers method
        pass

    def getAllMembers(self, context: Commentable) -> Member:
        # TODO: Implement getAllMembers method
        pass

    def getAllInnerClassifiers(self) -> str:
        # TODO: Implement getAllInnerClassifiers method
        pass

class ReferenceableElement:

    pass
class java_Method(AnnotableAndModifiable, TypeParametrizable, Parametrizable, ArrayTypeable, ExceptionThrower, Member, ReferenceableElement, TypedElement):

    def __init__(self):
        
    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

    def isSomeMethodForCall(self, methodCall: str) -> bool:
        # TODO: Implement isSomeMethodForCall method
        pass

    def isMethodForCall(self, methodCall: str, needsPerfectMatch: bool) -> bool:
        # TODO: Implement isMethodForCall method
        pass

    def isBetterMethodForCall(self, otherMethod: str, methodCall: str) -> bool:
        # TODO: Implement isBetterMethodForCall method
        pass

class java_AdditionalField(Initializable, ReferenceableElement, ArrayTypeable):

    def __init__(self, java_AdditionalField: "java_Field" = None):
        self.java_AdditionalField = java_AdditionalField
        
    @property
    def java_AdditionalField(self):
        return self.__java_AdditionalField

    @java_AdditionalField.setter
    def java_AdditionalField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AdditionalField__java_AdditionalField", None)
        self.__java_AdditionalField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Field"):
                opp_val = getattr(old_value, "java_Field", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Field"):
                opp_val = getattr(value, "java_Field", None)
                if opp_val is None:
                    setattr(value, "java_Field", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class java_Variable(TypeArgumentable, NamedElement, ArrayTypeable, ReferenceableElement, TypedElement):

    def __init__(self):
        
    def createMethodCallStatement(self, arguments: Expression, methodName: str) -> Statement:
        # TODO: Implement createMethodCallStatement method
        pass

    def createMethodCall(self, methodName: str, arguments: Expression) -> Expression:
        # TODO: Implement createMethodCall method
        pass

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class java_Field(AnnotableAndModifiable, Member, Initializable, Variable, ReferenceableElement):

    pass
class java_PackageReference(ReferenceableElement):

    pass
class java_AdditionalLocalVariable(Initializable, ReferenceableElement, ArrayTypeable):

    def __init__(self, java_AdditionalLocalVariable: "java_LocalVariable" = None):
        self.java_AdditionalLocalVariable = java_AdditionalLocalVariable
        
    @property
    def java_AdditionalLocalVariable(self):
        return self.__java_AdditionalLocalVariable

    @java_AdditionalLocalVariable.setter
    def java_AdditionalLocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AdditionalLocalVariable__java_AdditionalLocalVariable", None)
        self.__java_AdditionalLocalVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_LocalVariable179"):
                opp_val = getattr(old_value, "java_LocalVariable179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_LocalVariable179"):
                opp_val = getattr(value, "java_LocalVariable179", None)
                if opp_val is None:
                    setattr(value, "java_LocalVariable179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class java_EnumConstant(Annotable, ReferenceableElement, Argumentable):

    pass
class Type:

    pass
class java_PrimitiveType(Type, TypeReference):

    def __init__(self, java_PrimitiveType: "java_PrimitiveTypeReference" = None):
        self.java_PrimitiveType = java_PrimitiveType
        
    @property
    def java_PrimitiveType(self):
        return self.__java_PrimitiveType

    @java_PrimitiveType.setter
    def java_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_PrimitiveType__java_PrimitiveType", None)
        self.__java_PrimitiveType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_PrimitiveTypeReference"):
                opp_val = getattr(old_value, "java_PrimitiveTypeReference", None)
                if opp_val == self:
                    setattr(old_value, "java_PrimitiveTypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_PrimitiveTypeReference"):
                opp_val = getattr(value, "java_PrimitiveTypeReference", None)
                setattr(value, "java_PrimitiveTypeReference", self)

    def getAllMembers(self, context: Commentable) -> Member:
        # TODO: Implement getAllMembers method
        pass

    def wrapPrimitiveType(self) -> str:
        # TODO: Implement wrapPrimitiveType method
        pass

class java_AnonymousClass(Type, MemberContainer):

    def __init__(self, java_AnonymousClass: "java_NewConstructorCall" = None, java_AnonymousClass114: "java_EnumConstant" = None):
        self.java_AnonymousClass = java_AnonymousClass
        self.java_AnonymousClass114 = java_AnonymousClass114
        
    @property
    def java_AnonymousClass(self):
        return self.__java_AnonymousClass

    @java_AnonymousClass.setter
    def java_AnonymousClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnonymousClass__java_AnonymousClass", None)
        self.__java_AnonymousClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_NewConstructorCall"):
                opp_val = getattr(old_value, "java_NewConstructorCall", None)
                if opp_val == self:
                    setattr(old_value, "java_NewConstructorCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_NewConstructorCall"):
                opp_val = getattr(value, "java_NewConstructorCall", None)
                setattr(value, "java_NewConstructorCall", self)

    @property
    def java_AnonymousClass114(self):
        return self.__java_AnonymousClass114

    @java_AnonymousClass114.setter
    def java_AnonymousClass114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnonymousClass__java_AnonymousClass114", None)
        self.__java_AnonymousClass114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_EnumConstant113"):
                opp_val = getattr(old_value, "java_EnumConstant113", None)
                if opp_val == self:
                    setattr(old_value, "java_EnumConstant113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_EnumConstant113"):
                opp_val = getattr(value, "java_EnumConstant113", None)
                setattr(value, "java_EnumConstant113", self)

    def getSuperClassifier(self) -> ConcreteClassifier:
        # TODO: Implement getSuperClassifier method
        pass

    def getAllMembers(self, context: Commentable) -> Member:
        # TODO: Implement getAllMembers method
        pass

    def getAllSuperClassifiers(self) -> ConcreteClassifier:
        # TODO: Implement getAllSuperClassifiers method
        pass

class java_ArrayInstantiationByValuesTyped(ArrayTypeable, TypedElement, ArrayInstantiationByValues):

    pass
class java_InterfaceMethod(Method):

    pass
class AnnotationParameter:

    pass
class java_AnnotationParameterList(AnnotationParameter):

    pass
class java_SingleAnnotationParameter(AnnotationParameter):

    pass
class AnnotationValue:

    pass
class ArrayInitializationValue:

    pass
class java_ArrayInitializer(ArrayInitializationValue, AnnotationValue):

    pass
class java_Expression(ArrayInitializationValue, AnnotationValue):

    def __init__(self, java_Expression: "java_AnnotationAttribute" = None, java_Expression23: "java_ArraySelector" = None, java_Expression19: "java_ArrayInstantiationBySize" = None, java_Expression41: "java_ExpressionList" = None, java_Expression51: "java_ConditionalExpression" = None, java_Expression47: "java_AssignmentExpression" = None, java_Expression85: "java_NestedExpression" = None, java_Expression103: "java_Initializable" = None, java_Expression123: "java_Argumentable" = None, java_Expression136: "java_Assert" = None, java_Expression134: "java_Conditional" = None, java_Expression150: "java_ForEachLoop" = None, java_Expression141: "java_ExpressionStatement" = None, java_Expression145: "java_ForLoop" = None, java_Expression162: "java_Throw" = None, java_Expression154: "java_Return" = None, java_Expression158: "java_Switch" = None, java_Expression160: "java_SynchronizedBlock" = None, java_Expression168: "java_WhileLoop" = None):
        self.java_Expression = java_Expression
        self.java_Expression23 = java_Expression23
        self.java_Expression19 = java_Expression19
        self.java_Expression41 = java_Expression41
        self.java_Expression51 = java_Expression51
        self.java_Expression47 = java_Expression47
        self.java_Expression85 = java_Expression85
        self.java_Expression103 = java_Expression103
        self.java_Expression123 = java_Expression123
        self.java_Expression136 = java_Expression136
        self.java_Expression134 = java_Expression134
        self.java_Expression150 = java_Expression150
        self.java_Expression141 = java_Expression141
        self.java_Expression145 = java_Expression145
        self.java_Expression162 = java_Expression162
        self.java_Expression154 = java_Expression154
        self.java_Expression158 = java_Expression158
        self.java_Expression160 = java_Expression160
        self.java_Expression168 = java_Expression168
        
    @property
    def java_Expression136(self):
        return self.__java_Expression136

    @java_Expression136.setter
    def java_Expression136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression136", None)
        self.__java_Expression136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Assert"):
                opp_val = getattr(old_value, "java_Assert", None)
                if opp_val == self:
                    setattr(old_value, "java_Assert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Assert"):
                opp_val = getattr(value, "java_Assert", None)
                setattr(value, "java_Assert", self)

    @property
    def java_Expression168(self):
        return self.__java_Expression168

    @java_Expression168.setter
    def java_Expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression168", None)
        self.__java_Expression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_WhileLoop"):
                opp_val = getattr(old_value, "java_WhileLoop", None)
                if opp_val == self:
                    setattr(old_value, "java_WhileLoop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_WhileLoop"):
                opp_val = getattr(value, "java_WhileLoop", None)
                setattr(value, "java_WhileLoop", self)

    @property
    def java_Expression47(self):
        return self.__java_Expression47

    @java_Expression47.setter
    def java_Expression47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression47", None)
        self.__java_Expression47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AssignmentExpression46"):
                opp_val = getattr(old_value, "java_AssignmentExpression46", None)
                if opp_val == self:
                    setattr(old_value, "java_AssignmentExpression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AssignmentExpression46"):
                opp_val = getattr(value, "java_AssignmentExpression46", None)
                setattr(value, "java_AssignmentExpression46", self)

    @property
    def java_Expression41(self):
        return self.__java_Expression41

    @java_Expression41.setter
    def java_Expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression41", None)
        self.__java_Expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ExpressionList"):
                opp_val = getattr(old_value, "java_ExpressionList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ExpressionList"):
                opp_val = getattr(value, "java_ExpressionList", None)
                if opp_val is None:
                    setattr(value, "java_ExpressionList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Expression134(self):
        return self.__java_Expression134

    @java_Expression134.setter
    def java_Expression134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression134", None)
        self.__java_Expression134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Conditional"):
                opp_val = getattr(old_value, "java_Conditional", None)
                if opp_val == self:
                    setattr(old_value, "java_Conditional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Conditional"):
                opp_val = getattr(value, "java_Conditional", None)
                setattr(value, "java_Conditional", self)

    @property
    def java_Expression162(self):
        return self.__java_Expression162

    @java_Expression162.setter
    def java_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression162", None)
        self.__java_Expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Throw"):
                opp_val = getattr(old_value, "java_Throw", None)
                if opp_val == self:
                    setattr(old_value, "java_Throw", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Throw"):
                opp_val = getattr(value, "java_Throw", None)
                setattr(value, "java_Throw", self)

    @property
    def java_Expression(self):
        return self.__java_Expression

    @java_Expression.setter
    def java_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression", None)
        self.__java_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AnnotationAttribute"):
                opp_val = getattr(old_value, "java_AnnotationAttribute", None)
                if opp_val == self:
                    setattr(old_value, "java_AnnotationAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AnnotationAttribute"):
                opp_val = getattr(value, "java_AnnotationAttribute", None)
                setattr(value, "java_AnnotationAttribute", self)

    @property
    def java_Expression85(self):
        return self.__java_Expression85

    @java_Expression85.setter
    def java_Expression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression85", None)
        self.__java_Expression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_NestedExpression"):
                opp_val = getattr(old_value, "java_NestedExpression", None)
                if opp_val == self:
                    setattr(old_value, "java_NestedExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_NestedExpression"):
                opp_val = getattr(value, "java_NestedExpression", None)
                setattr(value, "java_NestedExpression", self)

    @property
    def java_Expression154(self):
        return self.__java_Expression154

    @java_Expression154.setter
    def java_Expression154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression154", None)
        self.__java_Expression154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Return"):
                opp_val = getattr(old_value, "java_Return", None)
                if opp_val == self:
                    setattr(old_value, "java_Return", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Return"):
                opp_val = getattr(value, "java_Return", None)
                setattr(value, "java_Return", self)

    @property
    def java_Expression123(self):
        return self.__java_Expression123

    @java_Expression123.setter
    def java_Expression123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression123", None)
        self.__java_Expression123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Argumentable"):
                opp_val = getattr(old_value, "java_Argumentable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Argumentable"):
                opp_val = getattr(value, "java_Argumentable", None)
                if opp_val is None:
                    setattr(value, "java_Argumentable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Expression150(self):
        return self.__java_Expression150

    @java_Expression150.setter
    def java_Expression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression150", None)
        self.__java_Expression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ForEachLoop149"):
                opp_val = getattr(old_value, "java_ForEachLoop149", None)
                if opp_val == self:
                    setattr(old_value, "java_ForEachLoop149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ForEachLoop149"):
                opp_val = getattr(value, "java_ForEachLoop149", None)
                setattr(value, "java_ForEachLoop149", self)

    @property
    def java_Expression19(self):
        return self.__java_Expression19

    @java_Expression19.setter
    def java_Expression19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression19", None)
        self.__java_Expression19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ArrayInstantiationBySize"):
                opp_val = getattr(old_value, "java_ArrayInstantiationBySize", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ArrayInstantiationBySize"):
                opp_val = getattr(value, "java_ArrayInstantiationBySize", None)
                if opp_val is None:
                    setattr(value, "java_ArrayInstantiationBySize", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Expression158(self):
        return self.__java_Expression158

    @java_Expression158.setter
    def java_Expression158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression158", None)
        self.__java_Expression158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Switch157"):
                opp_val = getattr(old_value, "java_Switch157", None)
                if opp_val == self:
                    setattr(old_value, "java_Switch157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Switch157"):
                opp_val = getattr(value, "java_Switch157", None)
                setattr(value, "java_Switch157", self)

    @property
    def java_Expression145(self):
        return self.__java_Expression145

    @java_Expression145.setter
    def java_Expression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression145", None)
        self.__java_Expression145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ForLoop144"):
                opp_val = getattr(old_value, "java_ForLoop144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ForLoop144"):
                opp_val = getattr(value, "java_ForLoop144", None)
                if opp_val is None:
                    setattr(value, "java_ForLoop144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Expression51(self):
        return self.__java_Expression51

    @java_Expression51.setter
    def java_Expression51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression51", None)
        self.__java_Expression51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ConditionalExpression50"):
                opp_val = getattr(old_value, "java_ConditionalExpression50", None)
                if opp_val == self:
                    setattr(old_value, "java_ConditionalExpression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ConditionalExpression50"):
                opp_val = getattr(value, "java_ConditionalExpression50", None)
                setattr(value, "java_ConditionalExpression50", self)

    @property
    def java_Expression23(self):
        return self.__java_Expression23

    @java_Expression23.setter
    def java_Expression23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression23", None)
        self.__java_Expression23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ArraySelector"):
                opp_val = getattr(old_value, "java_ArraySelector", None)
                if opp_val == self:
                    setattr(old_value, "java_ArraySelector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ArraySelector"):
                opp_val = getattr(value, "java_ArraySelector", None)
                setattr(value, "java_ArraySelector", self)

    @property
    def java_Expression103(self):
        return self.__java_Expression103

    @java_Expression103.setter
    def java_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression103", None)
        self.__java_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Initializable"):
                opp_val = getattr(old_value, "java_Initializable", None)
                if opp_val == self:
                    setattr(old_value, "java_Initializable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Initializable"):
                opp_val = getattr(value, "java_Initializable", None)
                setattr(value, "java_Initializable", self)

    @property
    def java_Expression141(self):
        return self.__java_Expression141

    @java_Expression141.setter
    def java_Expression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression141", None)
        self.__java_Expression141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ExpressionStatement"):
                opp_val = getattr(old_value, "java_ExpressionStatement", None)
                if opp_val == self:
                    setattr(old_value, "java_ExpressionStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ExpressionStatement"):
                opp_val = getattr(value, "java_ExpressionStatement", None)
                setattr(value, "java_ExpressionStatement", self)

    @property
    def java_Expression160(self):
        return self.__java_Expression160

    @java_Expression160.setter
    def java_Expression160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression160", None)
        self.__java_Expression160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_SynchronizedBlock"):
                opp_val = getattr(old_value, "java_SynchronizedBlock", None)
                if opp_val == self:
                    setattr(old_value, "java_SynchronizedBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_SynchronizedBlock"):
                opp_val = getattr(value, "java_SynchronizedBlock", None)
                setattr(value, "java_SynchronizedBlock", self)

    def getOneType(self, alternative: bool) -> Type:
        # TODO: Implement getOneType method
        pass

    def getType(self) -> Type:
        # TODO: Implement getType method
        pass

    def getAlternativeType(self) -> Type:
        # TODO: Implement getAlternativeType method
        pass

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class InterfaceMethod:

    pass
class java_AnnotationAttribute(InterfaceMethod):

    pass
class java_Classifier(ReferenceableElement, Type):

    def __init__(self, java_Classifier: "java_AnnotationInstance" = None, java_Classifier172: "java_ClassifierReference" = None):
        self.java_Classifier = java_Classifier
        self.java_Classifier172 = java_Classifier172
        
    @property
    def java_Classifier172(self):
        return self.__java_Classifier172

    @java_Classifier172.setter
    def java_Classifier172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier172", None)
        self.__java_Classifier172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ClassifierReference"):
                opp_val = getattr(old_value, "java_ClassifierReference", None)
                if opp_val == self:
                    setattr(old_value, "java_ClassifierReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ClassifierReference"):
                opp_val = getattr(value, "java_ClassifierReference", None)
                setattr(value, "java_ClassifierReference", self)

    @property
    def java_Classifier(self):
        return self.__java_Classifier

    @java_Classifier.setter
    def java_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Classifier__java_Classifier", None)
        self.__java_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_AnnotationInstance2"):
                opp_val = getattr(old_value, "java_AnnotationInstance2", None)
                if opp_val == self:
                    setattr(old_value, "java_AnnotationInstance2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_AnnotationInstance2"):
                opp_val = getattr(value, "java_AnnotationInstance2", None)
                setattr(value, "java_AnnotationInstance2", self)

    def getAllSuperClassifiers(self) -> str:
        # TODO: Implement getAllSuperClassifiers method
        pass

class NamespaceAwareElement:

    pass
class java_Import(NamespaceAwareElement):

    def __init__(self, java_Import: "java_ImportingElement" = None):
        self.java_Import = java_Import
        
    @property
    def java_Import(self):
        return self.__java_Import

    @java_Import.setter
    def java_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Import__java_Import", None)
        self.__java_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ImportingElement"):
                opp_val = getattr(old_value, "java_ImportingElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ImportingElement"):
                opp_val = getattr(value, "java_ImportingElement", None)
                if opp_val is None:
                    setattr(value, "java_ImportingElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getImportedClassifiers(self) -> ConcreteClassifier:
        # TODO: Implement getImportedClassifiers method
        pass

    def getImportedClassifier(self, name: str) -> ConcreteClassifier:
        # TODO: Implement getImportedClassifier method
        pass

    def getImportedMembers(self) -> NamedElement:
        # TODO: Implement getImportedMembers method
        pass

class java_NamespaceClassifierReference(NamespaceAwareElement, TypeReference):

    pass
class java_JavaRoot(NamespaceAwareElement, NamedElement, ImportingElement):

    def __init__(self):
        
    def getClassifiersInSamePackage(self) -> ConcreteClassifier:
        # TODO: Implement getClassifiersInSamePackage method
        pass

class AnnotationInstanceOrModifier:

    pass
class java_Modifier(AnnotationInstanceOrModifier):

    pass
class Reference:

    pass
class java_ElementReference(Reference):

    pass
class java_SelfReference(Reference):

    pass
class java_PrimitiveTypeReference(Reference):

    pass
class java_NestedExpression(Reference):

    pass
class java_ArrayInstantiation(Reference, Expression):

    pass
class java_StringReference(Reference):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class java_ReflectiveClassReference(Reference):

    pass
class java_Instantiation(Reference, Argumentable):

    pass
class java_AnnotationInstance(NamespaceAwareElement, AnnotationInstanceOrModifier, Reference):

    pass
class Commentable:

    pass
class java_ArraySelector(Commentable):

    pass
class java_CallTypeArgumentable(Commentable):

    pass
class java_Type(Commentable):

    def __init__(self):
        
    def equalsType(self, otherType: Type, arrayDimension: str, otherArrayDimension: str) -> bool:
        # TODO: Implement equalsType method
        pass

    def isSuperType(self, otherArrayType: ArrayTypeable, otherType: Type, arrayDimension: str) -> bool:
        # TODO: Implement isSuperType method
        pass

    def getAllMembers(self, context: Commentable) -> Member:
        # TODO: Implement getAllMembers method
        pass

class java_TypeArgumentable(Commentable):

    pass
class java_AnnotableAndModifiable(Commentable):

    def __init__(self, java_AnnotableAndModifiable: set["java_AnnotationInstanceOrModifier"] = None):
        self.java_AnnotableAndModifiable = java_AnnotableAndModifiable if java_AnnotableAndModifiable is not None else set()
        
    @property
    def java_AnnotableAndModifiable(self):
        return self.__java_AnnotableAndModifiable

    @java_AnnotableAndModifiable.setter
    def java_AnnotableAndModifiable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_AnnotableAndModifiable__java_AnnotableAndModifiable", None)
        self.__java_AnnotableAndModifiable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_AnnotationInstanceOrModifier"):
                    opp_val = getattr(item, "java_AnnotationInstanceOrModifier", None)
                    
                    if opp_val == self:
                        setattr(item, "java_AnnotationInstanceOrModifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_AnnotationInstanceOrModifier"):
                    opp_val = getattr(item, "java_AnnotationInstanceOrModifier", None)
                    
                    setattr(item, "java_AnnotationInstanceOrModifier", self)
                    

    def hasModifier(self, type: str) -> bool:
        # TODO: Implement hasModifier method
        pass

    def isPublic(self) -> bool:
        # TODO: Implement isPublic method
        pass

    def getModifiers(self) -> str:
        # TODO: Implement getModifiers method
        pass

    def isPrivate(self) -> bool:
        # TODO: Implement isPrivate method
        pass

    def makeProtected(self):
        # TODO: Implement makeProtected method
        pass

    def removeAllModifiers(self):
        # TODO: Implement removeAllModifiers method
        pass

    def isStatic(self) -> bool:
        # TODO: Implement isStatic method
        pass

    def isHidden(self, context: Commentable) -> bool:
        # TODO: Implement isHidden method
        pass

    def makePrivate(self):
        # TODO: Implement makePrivate method
        pass

    def removeModifier(self, modifierType: str):
        # TODO: Implement removeModifier method
        pass

    def isProtected(self) -> bool:
        # TODO: Implement isProtected method
        pass

    def addModifier(self, newModifier: str):
        # TODO: Implement addModifier method
        pass

    def makePublic(self):
        # TODO: Implement makePublic method
        pass

class java_MemberContainer(Commentable):

    def __init__(self, java_MemberContainer: set["java_Member"] = None, java_MemberContainer109: set["java_Member"] = None):
        self.java_MemberContainer = java_MemberContainer if java_MemberContainer is not None else set()
        self.java_MemberContainer109 = java_MemberContainer109 if java_MemberContainer109 is not None else set()
        
    @property
    def java_MemberContainer(self):
        return self.__java_MemberContainer

    @java_MemberContainer.setter
    def java_MemberContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MemberContainer__java_MemberContainer", None)
        self.__java_MemberContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Member"):
                    opp_val = getattr(item, "java_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Member"):
                    opp_val = getattr(item, "java_Member", None)
                    
                    setattr(item, "java_Member", self)
                    

    @property
    def java_MemberContainer109(self):
        return self.__java_MemberContainer109

    @java_MemberContainer109.setter
    def java_MemberContainer109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_MemberContainer__java_MemberContainer109", None)
        self.__java_MemberContainer109 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Member110"):
                    opp_val = getattr(item, "java_Member110", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Member110", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Member110"):
                    opp_val = getattr(item, "java_Member110", None)
                    
                    setattr(item, "java_Member110", self)
                    

    def getContainedClassifier(self, name: str) -> ConcreteClassifier:
        # TODO: Implement getContainedClassifier method
        pass

    def getMethods(self) -> str:
        # TODO: Implement getMethods method
        pass

    def getContainedField(self, name: str) -> str:
        # TODO: Implement getContainedField method
        pass

    def removeMethods(self, name: str):
        # TODO: Implement removeMethods method
        pass

    def createField(self, name: str, qualifiedTypeName: str) -> str:
        # TODO: Implement createField method
        pass

    def getFields(self) -> str:
        # TODO: Implement getFields method
        pass

    def getContainedMethod(self, name: str) -> str:
        # TODO: Implement getContainedMethod method
        pass

    def getMembersByName(self, name: str) -> Member:
        # TODO: Implement getMembersByName method
        pass

class java_TypedElement(Commentable):

    pass
class java_Parametrizable(Commentable):

    pass
class java_ArrayInitializationValue(Commentable):

    pass
class java_ExceptionThrower(Commentable):

    pass
class java_Self(Commentable):

    pass
class java_StatementContainer(Commentable):

    pass
class java_AnnotationValue(Commentable):

    pass
class java_Operator(Commentable):

    pass
class java_Modifiable(Commentable):

    pass
class java_NamespaceAwareElement(Commentable):

    def __init__(self, namespaces: str):
        self.namespaces = namespaces
        
    @property
    def namespaces(self) -> str:
        return self.__namespaces

    @namespaces.setter
    def namespaces(self, namespaces: str):
        self.__namespaces = namespaces

    def getClassifierAtNamespaces(self) -> ConcreteClassifier:
        # TODO: Implement getClassifierAtNamespaces method
        pass

    def getNamespacesAsString(self) -> str:
        # TODO: Implement getNamespacesAsString method
        pass

class java_Initializable(Commentable):

    pass
class java_TypeReference(Commentable):

    def __init__(self, java_TypeReference26: "java_Class" = None, java_TypeReference29: "java_Class" = None, java_TypeReference: "java_Implementor" = None, java_TypeReference31: "java_Interface" = None, java_TypeReference34: "java_Interface" = None, java_TypeReference96: "java_TypeParameter" = None, java_TypeReference91: "java_ExtendsTypeArgument" = None, java_TypeReference93: "java_SuperTypeArgument" = None, java_TypeReference170: "java_TypedElement" = None):
        self.java_TypeReference26 = java_TypeReference26
        self.java_TypeReference29 = java_TypeReference29
        self.java_TypeReference = java_TypeReference
        self.java_TypeReference31 = java_TypeReference31
        self.java_TypeReference34 = java_TypeReference34
        self.java_TypeReference96 = java_TypeReference96
        self.java_TypeReference91 = java_TypeReference91
        self.java_TypeReference93 = java_TypeReference93
        self.java_TypeReference170 = java_TypeReference170
        
    @property
    def java_TypeReference29(self):
        return self.__java_TypeReference29

    @java_TypeReference29.setter
    def java_TypeReference29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference29", None)
        self.__java_TypeReference29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Class28"):
                opp_val = getattr(old_value, "java_Class28", None)
                if opp_val == self:
                    setattr(old_value, "java_Class28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Class28"):
                opp_val = getattr(value, "java_Class28", None)
                setattr(value, "java_Class28", self)

    @property
    def java_TypeReference26(self):
        return self.__java_TypeReference26

    @java_TypeReference26.setter
    def java_TypeReference26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference26", None)
        self.__java_TypeReference26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Class"):
                opp_val = getattr(old_value, "java_Class", None)
                if opp_val == self:
                    setattr(old_value, "java_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Class"):
                opp_val = getattr(value, "java_Class", None)
                setattr(value, "java_Class", self)

    @property
    def java_TypeReference(self):
        return self.__java_TypeReference

    @java_TypeReference.setter
    def java_TypeReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference", None)
        self.__java_TypeReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Implementor"):
                opp_val = getattr(old_value, "java_Implementor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Implementor"):
                opp_val = getattr(value, "java_Implementor", None)
                if opp_val is None:
                    setattr(value, "java_Implementor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_TypeReference96(self):
        return self.__java_TypeReference96

    @java_TypeReference96.setter
    def java_TypeReference96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference96", None)
        self.__java_TypeReference96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypeParameter95"):
                opp_val = getattr(old_value, "java_TypeParameter95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypeParameter95"):
                opp_val = getattr(value, "java_TypeParameter95", None)
                if opp_val is None:
                    setattr(value, "java_TypeParameter95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_TypeReference91(self):
        return self.__java_TypeReference91

    @java_TypeReference91.setter
    def java_TypeReference91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference91", None)
        self.__java_TypeReference91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_ExtendsTypeArgument"):
                opp_val = getattr(old_value, "java_ExtendsTypeArgument", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_ExtendsTypeArgument"):
                opp_val = getattr(value, "java_ExtendsTypeArgument", None)
                if opp_val is None:
                    setattr(value, "java_ExtendsTypeArgument", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_TypeReference34(self):
        return self.__java_TypeReference34

    @java_TypeReference34.setter
    def java_TypeReference34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference34", None)
        self.__java_TypeReference34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Interface33"):
                opp_val = getattr(old_value, "java_Interface33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Interface33"):
                opp_val = getattr(value, "java_Interface33", None)
                if opp_val is None:
                    setattr(value, "java_Interface33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_TypeReference31(self):
        return self.__java_TypeReference31

    @java_TypeReference31.setter
    def java_TypeReference31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference31", None)
        self.__java_TypeReference31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Interface"):
                opp_val = getattr(old_value, "java_Interface", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Interface"):
                opp_val = getattr(value, "java_Interface", None)
                if opp_val is None:
                    setattr(value, "java_Interface", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_TypeReference170(self):
        return self.__java_TypeReference170

    @java_TypeReference170.setter
    def java_TypeReference170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference170", None)
        self.__java_TypeReference170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_TypedElement"):
                opp_val = getattr(old_value, "java_TypedElement", None)
                if opp_val == self:
                    setattr(old_value, "java_TypedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_TypedElement"):
                opp_val = getattr(value, "java_TypedElement", None)
                setattr(value, "java_TypedElement", self)

    @property
    def java_TypeReference93(self):
        return self.__java_TypeReference93

    @java_TypeReference93.setter
    def java_TypeReference93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_TypeReference__java_TypeReference93", None)
        self.__java_TypeReference93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_SuperTypeArgument"):
                opp_val = getattr(old_value, "java_SuperTypeArgument", None)
                if opp_val == self:
                    setattr(old_value, "java_SuperTypeArgument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_SuperTypeArgument"):
                opp_val = getattr(value, "java_SuperTypeArgument", None)
                setattr(value, "java_SuperTypeArgument", self)

    def getPureClassifierReference(self) -> str:
        # TODO: Implement getPureClassifierReference method
        pass

    def getTarget(self) -> Type:
        # TODO: Implement getTarget method
        pass

    def getBoundTarget(self, reference: Reference) -> Type:
        # TODO: Implement getBoundTarget method
        pass

class java_Implementor(Commentable):

    pass
class java_NamedElement(Commentable):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class java_Statement(Commentable):

    pass
class java_ArrayDimension(Commentable):

    pass
class java_AnnotationInstanceOrModifier(Commentable):

    pass
class java_AnnotationAttributeSetting(Commentable):

    pass
class java_Argumentable(Commentable):

    def __init__(self, java_Argumentable: set["java_Expression"] = None):
        self.java_Argumentable = java_Argumentable if java_Argumentable is not None else set()
        
    @property
    def java_Argumentable(self):
        return self.__java_Argumentable

    @java_Argumentable.setter
    def java_Argumentable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Argumentable__java_Argumentable", None)
        self.__java_Argumentable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Expression123"):
                    opp_val = getattr(item, "java_Expression123", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Expression123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Expression123"):
                    opp_val = getattr(item, "java_Expression123", None)
                    
                    setattr(item, "java_Expression123", self)
                    

    def getArgumentTypes(self) -> Type:
        # TODO: Implement getArgumentTypes method
        pass

class java_AnnotationParameter(Commentable):

    pass
class java_ImportingElement(Commentable):

    def __init__(self, java_ImportingElement: set["java_Import"] = None):
        self.java_ImportingElement = java_ImportingElement if java_ImportingElement is not None else set()
        
    @property
    def java_ImportingElement(self):
        return self.__java_ImportingElement

    @java_ImportingElement.setter
    def java_ImportingElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ImportingElement__java_ImportingElement", None)
        self.__java_ImportingElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Import"):
                    opp_val = getattr(item, "java_Import", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Import", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Import"):
                    opp_val = getattr(item, "java_Import", None)
                    
                    setattr(item, "java_Import", self)
                    

    def getDefaultImports(self) -> ConcreteClassifier:
        # TODO: Implement getDefaultImports method
        pass

class java_ArrayTypeable(Commentable):

    def __init__(self, java_ArrayTypeable: set["java_ArrayDimension"] = None, java_ArrayTypeable15: set["java_ArrayDimension"] = None):
        self.java_ArrayTypeable = java_ArrayTypeable if java_ArrayTypeable is not None else set()
        self.java_ArrayTypeable15 = java_ArrayTypeable15 if java_ArrayTypeable15 is not None else set()
        
    @property
    def java_ArrayTypeable15(self):
        return self.__java_ArrayTypeable15

    @java_ArrayTypeable15.setter
    def java_ArrayTypeable15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ArrayTypeable__java_ArrayTypeable15", None)
        self.__java_ArrayTypeable15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ArrayDimension16"):
                    opp_val = getattr(item, "java_ArrayDimension16", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ArrayDimension16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ArrayDimension16"):
                    opp_val = getattr(item, "java_ArrayDimension16", None)
                    
                    setattr(item, "java_ArrayDimension16", self)
                    

    @property
    def java_ArrayTypeable(self):
        return self.__java_ArrayTypeable

    @java_ArrayTypeable.setter
    def java_ArrayTypeable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_ArrayTypeable__java_ArrayTypeable", None)
        self.__java_ArrayTypeable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_ArrayDimension"):
                    opp_val = getattr(item, "java_ArrayDimension", None)
                    
                    if opp_val == self:
                        setattr(item, "java_ArrayDimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_ArrayDimension"):
                    opp_val = getattr(item, "java_ArrayDimension", None)
                    
                    setattr(item, "java_ArrayDimension", self)
                    

    def getArrayDimension(self) -> str:
        # TODO: Implement getArrayDimension method
        pass

class java_ForLoopInitializer(Commentable):

    pass
class java_TypeParametrizable(Commentable):

    pass
class java_Conditional(Commentable):

    pass
class java_StatementListContainer(Commentable):

    def __init__(self, java_StatementListContainer: set["java_Statement"] = None):
        self.java_StatementListContainer = java_StatementListContainer if java_StatementListContainer is not None else set()
        
    @property
    def java_StatementListContainer(self):
        return self.__java_StatementListContainer

    @java_StatementListContainer.setter
    def java_StatementListContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_StatementListContainer__java_StatementListContainer", None)
        self.__java_StatementListContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Statement132"):
                    opp_val = getattr(item, "java_Statement132", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Statement132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Statement132"):
                    opp_val = getattr(item, "java_Statement132", None)
                    
                    setattr(item, "java_Statement132", self)
                    

    def getLocalVariable(self, name: str) -> str:
        # TODO: Implement getLocalVariable method
        pass

class java_Annotable(Commentable):

    pass