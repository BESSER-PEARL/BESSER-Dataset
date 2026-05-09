####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
AnnotationParameter = Class(name="AnnotationParameter")
annotations_AnnotationParameter = Class(name="annotations_AnnotationParameter", is_abstract=True)
annotations_SingleAnnotationParameter = Class(name="annotations_SingleAnnotationParameter")
AnnotationValue = Class(name="AnnotationValue")
annotations_AnnotationParameterList = Class(name="annotations_AnnotationParameterList")
AnnotationAttributeSetting = Class(name="AnnotationAttributeSetting")
annotations_AnnotationAttributeSetting = Class(name="annotations_AnnotationAttributeSetting")
InterfaceMethod = Class(name="InterfaceMethod")
annotations_AnnotationValue = Class(name="annotations_AnnotationValue", is_abstract=True)
annotations_AnnotationAttribute = Class(name="annotations_AnnotationAttribute")
annotations_Annotable = Class(name="annotations_Annotable", is_abstract=True)
Commentable = Class(name="Commentable")
AnnotationInstance = Class(name="AnnotationInstance")
annotations_AnnotationInstance = Class(name="annotations_AnnotationInstance")
Reference = Class(name="Reference")
AnnotationInstanceOrModifier = Class(name="AnnotationInstanceOrModifier")
NamespaceAwareElement = Class(name="NamespaceAwareElement")
Classifier = Class(name="Classifier")
ArrayInitializer = Class(name="ArrayInitializer")
arrays_ArraySelector = Class(name="arrays_ArraySelector")
classifiers_Classifier = Class(name="classifiers_Classifier", is_abstract=True)
Type = Class(name="Type")
ReferenceableElement = Class(name="ReferenceableElement")
classifiers_ConcreteClassifier = Class(name="classifiers_ConcreteClassifier", is_abstract=True)
TypeParametrizable = Class(name="TypeParametrizable")
MemberContainer = Class(name="MemberContainer")
Member = Class(name="Member")
Statement = Class(name="Statement")
AnnotableAndModifiable = Class(name="AnnotableAndModifiable")
classifiers_Implementor = Class(name="classifiers_Implementor", is_abstract=True)
Expression = Class(name="Expression")
arrays_ArrayTypeable = Class(name="arrays_ArrayTypeable", is_abstract=True)
ArrayDimension = Class(name="ArrayDimension")
arrays_ArrayDimension = Class(name="arrays_ArrayDimension")
arrays_ArrayInitializer = Class(name="arrays_ArrayInitializer")
ArrayInitializationValue = Class(name="ArrayInitializationValue")
arrays_ArrayInitializationValue = Class(name="arrays_ArrayInitializationValue", is_abstract=True)
arrays_ArrayInstantiationBySize = Class(name="arrays_ArrayInstantiationBySize")
TypedElement = Class(name="TypedElement")
ArrayTypeable = Class(name="ArrayTypeable")
arrays_ArrayInstantiationByValues = Class(name="arrays_ArrayInstantiationByValues")
EnumConstant = Class(name="EnumConstant")
classifiers_Annotation = Class(name="classifiers_Annotation")
classifiers_AnonymousClass = Class(name="classifiers_AnonymousClass")
commons_Commentable = Class(name="commons_Commentable", is_abstract=True)
TypeReference = Class(name="TypeReference")
classifiers_Class = Class(name="classifiers_Class")
ConcreteClassifier = Class(name="ConcreteClassifier")
Implementor = Class(name="Implementor")
classifiers_Interface = Class(name="classifiers_Interface")
classifiers_Enumeration = Class(name="classifiers_Enumeration")
containers_Package = Class(name="containers_Package")
Annotable = Class(name="Annotable")
CompilationUnit = Class(name="CompilationUnit")
Package = Class(name="Package")
containers_EmptyModel = Class(name="containers_EmptyModel")
expressions_ExpressionList = Class(name="expressions_ExpressionList")
ForLoopInitializer = Class(name="ForLoopInitializer")
expressions_Expression = Class(name="expressions_Expression", is_abstract=True)
commons_NamedElement = Class(name="commons_NamedElement", is_abstract=True)
commons_NamespaceAwareElement = Class(name="commons_NamespaceAwareElement", is_abstract=True)
containers_JavaRoot = Class(name="containers_JavaRoot", is_abstract=True)
NamedElement = Class(name="NamedElement")
ImportingElement = Class(name="ImportingElement")
containers_CompilationUnit = Class(name="containers_CompilationUnit")
JavaRoot = Class(name="JavaRoot")
ConditionalAndExpressionChild = Class(name="ConditionalAndExpressionChild")
expressions_ConditionalAndExpressionChild = Class(name="expressions_ConditionalAndExpressionChild", is_abstract=True)
expressions_InclusiveOrExpression = Class(name="expressions_InclusiveOrExpression")
InclusiveOrExpressionChild = Class(name="InclusiveOrExpressionChild")
expressions_InclusiveOrExpressionChild = Class(name="expressions_InclusiveOrExpressionChild", is_abstract=True)
expressions_ExclusiveOrExpression = Class(name="expressions_ExclusiveOrExpression")
ExclusiveOrExpressionChild = Class(name="ExclusiveOrExpressionChild")
expressions_ExclusiveOrExpressionChild = Class(name="expressions_ExclusiveOrExpressionChild", is_abstract=True)
expressions_AndExpression = Class(name="expressions_AndExpression")
AndExpressionChild = Class(name="AndExpressionChild")
expressions_AndExpressionChild = Class(name="expressions_AndExpressionChild", is_abstract=True)
expressions_EqualityExpression = Class(name="expressions_EqualityExpression")
EqualityOperator = Class(name="EqualityOperator")
expressions_AssignmentExpression = Class(name="expressions_AssignmentExpression")
AssignmentExpressionChild = Class(name="AssignmentExpressionChild")
AssignmentOperator = Class(name="AssignmentOperator")
expressions_AssignmentExpressionChild = Class(name="expressions_AssignmentExpressionChild", is_abstract=True)
expressions_ConditionalExpression = Class(name="expressions_ConditionalExpression")
ConditionalExpressionChild = Class(name="ConditionalExpressionChild")
expressions_ConditionalExpressionChild = Class(name="expressions_ConditionalExpressionChild", is_abstract=True)
expressions_ConditionalOrExpression = Class(name="expressions_ConditionalOrExpression")
ConditionalOrExpressionChild = Class(name="ConditionalOrExpressionChild")
expressions_ConditionalOrExpressionChild = Class(name="expressions_ConditionalOrExpressionChild", is_abstract=True)
expressions_ConditionalAndExpression = Class(name="expressions_ConditionalAndExpression")
AdditiveExpressionChild = Class(name="AdditiveExpressionChild")
AdditiveOperator = Class(name="AdditiveOperator")
expressions_AdditiveExpressionChild = Class(name="expressions_AdditiveExpressionChild", is_abstract=True)
expressions_MultiplicativeExpression = Class(name="expressions_MultiplicativeExpression")
MultiplicativeExpressionChild = Class(name="MultiplicativeExpressionChild")
MultiplicativeOperator = Class(name="MultiplicativeOperator")
expressions_MultiplicativeExpressionChild = Class(name="expressions_MultiplicativeExpressionChild", is_abstract=True)
expressions_UnaryExpression = Class(name="expressions_UnaryExpression")
UnaryOperator = Class(name="UnaryOperator")
UnaryExpressionChild = Class(name="UnaryExpressionChild")
EqualityExpressionChild = Class(name="EqualityExpressionChild")
expressions_EqualityExpressionChild = Class(name="expressions_EqualityExpressionChild", is_abstract=True)
expressions_InstanceOfExpression = Class(name="expressions_InstanceOfExpression")
InstanceOfExpressionChild = Class(name="InstanceOfExpressionChild")
expressions_InstanceOfExpressionChild = Class(name="expressions_InstanceOfExpressionChild", is_abstract=True)
expressions_RelationExpression = Class(name="expressions_RelationExpression")
RelationExpressionChild = Class(name="RelationExpressionChild")
RelationOperator = Class(name="RelationOperator")
expressions_RelationExpressionChild = Class(name="expressions_RelationExpressionChild", is_abstract=True)
expressions_ShiftExpression = Class(name="expressions_ShiftExpression")
ShiftExpressionChild = Class(name="ShiftExpressionChild")
ShiftOperator = Class(name="ShiftOperator")
expressions_ShiftExpressionChild = Class(name="expressions_ShiftExpressionChild", is_abstract=True)
expressions_AdditiveExpression = Class(name="expressions_AdditiveExpression")
generics_CallTypeArgumentable = Class(name="generics_CallTypeArgumentable", is_abstract=True)
generics_TypeParametrizable = Class(name="generics_TypeParametrizable", is_abstract=True)
TypeParameter = Class(name="TypeParameter")
generics_ExtendsTypeArgument = Class(name="generics_ExtendsTypeArgument")
generics_QualifiedTypeArgument = Class(name="generics_QualifiedTypeArgument")
generics_SuperTypeArgument = Class(name="generics_SuperTypeArgument")
generics_TypeParameter = Class(name="generics_TypeParameter")
expressions_UnaryExpressionChild = Class(name="expressions_UnaryExpressionChild", is_abstract=True)
expressions_UnaryModificationExpression = Class(name="expressions_UnaryModificationExpression", is_abstract=True)
UnaryModificationExpressionChild = Class(name="UnaryModificationExpressionChild")
UnaryModificationOperator = Class(name="UnaryModificationOperator")
expressions_PrefixUnaryModificationExpression = Class(name="expressions_PrefixUnaryModificationExpression")
UnaryModificationExpression = Class(name="UnaryModificationExpression")
expressions_SuffixUnaryModificationExpression = Class(name="expressions_SuffixUnaryModificationExpression")
expressions_UnaryModificationExpressionChild = Class(name="expressions_UnaryModificationExpressionChild", is_abstract=True)
expressions_CastExpression = Class(name="expressions_CastExpression")
expressions_PrimaryExpression = Class(name="expressions_PrimaryExpression", is_abstract=True)
expressions_NestedExpression = Class(name="expressions_NestedExpression")
generics_TypeArgument = Class(name="generics_TypeArgument", is_abstract=True)
generics_TypeArgumentable = Class(name="generics_TypeArgumentable", is_abstract=True)
TypeArgument = Class(name="TypeArgument")
imports_StaticClassifierImport = Class(name="imports_StaticClassifierImport")
StaticImport = Class(name="StaticImport")
imports_StaticMemberImport = Class(name="imports_StaticMemberImport")
instantiations_Initializable = Class(name="instantiations_Initializable", is_abstract=True)
instantiations_Instantiation = Class(name="instantiations_Instantiation", is_abstract=True)
Argumentable = Class(name="Argumentable")
TypeArgumentable = Class(name="TypeArgumentable")
instantiations_NewConstructorCall = Class(name="instantiations_NewConstructorCall")
Instantiation = Class(name="Instantiation")
CallTypeArgumentable = Class(name="CallTypeArgumentable")
AnonymousClass = Class(name="AnonymousClass")
instantiations_ExplicitConstructorCall = Class(name="instantiations_ExplicitConstructorCall")
Self = Class(name="Self")
generics_UnknownTypeArgument = Class(name="generics_UnknownTypeArgument")
imports_Import = Class(name="imports_Import", is_abstract=True)
imports_ImportingElement = Class(name="imports_ImportingElement", is_abstract=True)
Import = Class(name="Import")
imports_StaticImport = Class(name="imports_StaticImport", is_abstract=True)
Static = Class(name="Static")
imports_ClassifierImport = Class(name="imports_ClassifierImport")
imports_PackageImport = Class(name="imports_PackageImport")
literals_OctalIntegerLiteral = Class(name="literals_OctalIntegerLiteral")
literals_LongLiteral = Class(name="literals_LongLiteral", is_abstract=True)
literals_DecimalLongLiteral = Class(name="literals_DecimalLongLiteral")
LongLiteral = Class(name="LongLiteral")
literals_HexLongLiteral = Class(name="literals_HexLongLiteral")
literals_OctalLongLiteral = Class(name="literals_OctalLongLiteral")
literals_NullLiteral = Class(name="literals_NullLiteral")
literals_Super = Class(name="literals_Super")
literals_This = Class(name="literals_This")
members_ExceptionThrower = Class(name="members_ExceptionThrower", is_abstract=True)
NamespaceClassifierReference = Class(name="NamespaceClassifierReference")
literals_Literal = Class(name="literals_Literal", is_abstract=True)
PrimaryExpression = Class(name="PrimaryExpression")
literals_Self = Class(name="literals_Self", is_abstract=True)
literals_BooleanLiteral = Class(name="literals_BooleanLiteral")
Literal = Class(name="Literal")
literals_CharacterLiteral = Class(name="literals_CharacterLiteral")
literals_FloatLiteral = Class(name="literals_FloatLiteral", is_abstract=True)
literals_DecimalFloatLiteral = Class(name="literals_DecimalFloatLiteral")
FloatLiteral = Class(name="FloatLiteral")
literals_HexFloatLiteral = Class(name="literals_HexFloatLiteral")
literals_DoubleLiteral = Class(name="literals_DoubleLiteral", is_abstract=True)
literals_DecimalDoubleLiteral = Class(name="literals_DecimalDoubleLiteral")
DoubleLiteral = Class(name="DoubleLiteral")
literals_HexDoubleLiteral = Class(name="literals_HexDoubleLiteral")
literals_IntegerLiteral = Class(name="literals_IntegerLiteral", is_abstract=True)
literals_DecimalIntegerLiteral = Class(name="literals_DecimalIntegerLiteral")
IntegerLiteral = Class(name="IntegerLiteral")
literals_HexIntegerLiteral = Class(name="literals_HexIntegerLiteral")
members_Field = Class(name="members_Field")
Variable = Class(name="Variable")
AdditionalField = Class(name="AdditionalField")
members_Method = Class(name="members_Method", is_abstract=True)
members_Member = Class(name="members_Member", is_abstract=True)
members_MemberContainer = Class(name="members_MemberContainer", is_abstract=True)
members_AdditionalField = Class(name="members_AdditionalField")
Initializable = Class(name="Initializable")
members_Constructor = Class(name="members_Constructor")
StatementListContainer = Class(name="StatementListContainer")
Parametrizable = Class(name="Parametrizable")
ExceptionThrower = Class(name="ExceptionThrower")
members_EmptyMember = Class(name="members_EmptyMember")
modifiers_Native = Class(name="modifiers_Native")
modifiers_Protected = Class(name="modifiers_Protected")
modifiers_Public = Class(name="modifiers_Public")
modifiers_Private = Class(name="modifiers_Private")
modifiers_Static = Class(name="modifiers_Static")
modifiers_Strictfp = Class(name="modifiers_Strictfp")
modifiers_Synchronized = Class(name="modifiers_Synchronized")
modifiers_Transient = Class(name="modifiers_Transient")
modifiers_Volatile = Class(name="modifiers_Volatile")
operators_Operator = Class(name="operators_Operator", is_abstract=True)
operators_AdditiveOperator = Class(name="operators_AdditiveOperator", is_abstract=True)
Operator = Class(name="Operator")
operators_AssignmentOperator = Class(name="operators_AssignmentOperator", is_abstract=True)
operators_EqualityOperator = Class(name="operators_EqualityOperator", is_abstract=True)
operators_MultiplicativeOperator = Class(name="operators_MultiplicativeOperator", is_abstract=True)
operators_RelationOperator = Class(name="operators_RelationOperator", is_abstract=True)
operators_ShiftOperator = Class(name="operators_ShiftOperator", is_abstract=True)
members_InterfaceMethod = Class(name="members_InterfaceMethod")
Method_ = Class(name="Method")
members_ClassMethod = Class(name="members_ClassMethod")
members_EnumConstant = Class(name="members_EnumConstant")
modifiers_Modifier = Class(name="modifiers_Modifier", is_abstract=True)
modifiers_AnnotationInstanceOrModifier = Class(name="modifiers_AnnotationInstanceOrModifier", is_abstract=True)
modifiers_AnnotableAndModifiable = Class(name="modifiers_AnnotableAndModifiable", is_abstract=True)
modifiers_Modifiable = Class(name="modifiers_Modifiable", is_abstract=True)
Modifier = Class(name="Modifier")
modifiers_Abstract = Class(name="modifiers_Abstract")
modifiers_Final = Class(name="modifiers_Final")
operators_Multiplication = Class(name="operators_Multiplication")
operators_Remainder = Class(name="operators_Remainder")
operators_Complement = Class(name="operators_Complement")
operators_MinusMinus = Class(name="operators_MinusMinus")
operators_Negate = Class(name="operators_Negate")
operators_PlusPlus = Class(name="operators_PlusPlus")
operators_LeftShift = Class(name="operators_LeftShift")
operators_RightShift = Class(name="operators_RightShift")
operators_UnsignedRightShift = Class(name="operators_UnsignedRightShift")
parameters_Parameter = Class(name="parameters_Parameter", is_abstract=True)
parameters_Parametrizable = Class(name="parameters_Parametrizable", is_abstract=True)
Parameter_ = Class(name="Parameter")
parameters_OrdinaryParameter = Class(name="parameters_OrdinaryParameter")
parameters_VariableLengthParameter = Class(name="parameters_VariableLengthParameter")
operators_UnaryOperator = Class(name="operators_UnaryOperator", is_abstract=True)
operators_UnaryModificationOperator = Class(name="operators_UnaryModificationOperator", is_abstract=True)
operators_Assignment = Class(name="operators_Assignment")
operators_AssignmentAnd = Class(name="operators_AssignmentAnd")
operators_AssignmentDivision = Class(name="operators_AssignmentDivision")
operators_AssignmentExclusiveOr = Class(name="operators_AssignmentExclusiveOr")
operators_AssignmentMinus = Class(name="operators_AssignmentMinus")
operators_AssignmentModulo = Class(name="operators_AssignmentModulo")
operators_AssignmentMultiplication = Class(name="operators_AssignmentMultiplication")
operators_AssignmentLeftShift = Class(name="operators_AssignmentLeftShift")
operators_AssignmentOr = Class(name="operators_AssignmentOr")
operators_AssignmentPlus = Class(name="operators_AssignmentPlus")
operators_AssignmentRightShift = Class(name="operators_AssignmentRightShift")
operators_AssignmentUnsignedRightShift = Class(name="operators_AssignmentUnsignedRightShift")
operators_Equal = Class(name="operators_Equal")
operators_NotEqual = Class(name="operators_NotEqual")
operators_GreaterThan = Class(name="operators_GreaterThan")
operators_GreaterThanOrEqual = Class(name="operators_GreaterThanOrEqual")
operators_LessThan = Class(name="operators_LessThan")
operators_LessThanOrEqual = Class(name="operators_LessThanOrEqual")
operators_Addition = Class(name="operators_Addition")
operators_Subtraction = Class(name="operators_Subtraction")
operators_Division = Class(name="operators_Division")
references_PrimitiveTypeReference = Class(name="references_PrimitiveTypeReference")
PrimitiveType = Class(name="PrimitiveType")
references_StringReference = Class(name="references_StringReference")
references_SelfReference = Class(name="references_SelfReference")
statements_StatementContainer = Class(name="statements_StatementContainer", is_abstract=True)
statements_StatementListContainer = Class(name="statements_StatementListContainer", is_abstract=True)
references_Reference = Class(name="references_Reference", is_abstract=True)
ArraySelector = Class(name="ArraySelector")
references_Argumentable = Class(name="references_Argumentable", is_abstract=True)
references_ReferenceableElement = Class(name="references_ReferenceableElement", is_abstract=True)
references_ElementReference = Class(name="references_ElementReference", is_abstract=True)
references_IdentifierReference = Class(name="references_IdentifierReference")
ElementReference = Class(name="ElementReference")
references_MethodCall = Class(name="references_MethodCall")
references_ReflectiveClassReference = Class(name="references_ReflectiveClassReference")
statements_Continue = Class(name="statements_Continue")
statements_DefaultSwitchCase = Class(name="statements_DefaultSwitchCase")
SwitchCase = Class(name="SwitchCase")
statements_DoWhileLoop = Class(name="statements_DoWhileLoop")
WhileLoop = Class(name="WhileLoop")
statements_EmptyStatement = Class(name="statements_EmptyStatement")
statements_ExpressionStatement = Class(name="statements_ExpressionStatement")
statements_ForLoop = Class(name="statements_ForLoop")
statements_ForEachLoop = Class(name="statements_ForEachLoop")
statements_Conditional = Class(name="statements_Conditional", is_abstract=True)
statements_ForLoopInitializer = Class(name="statements_ForLoopInitializer", is_abstract=True)
statements_Statement = Class(name="statements_Statement", is_abstract=True)
statements_SwitchCase = Class(name="statements_SwitchCase", is_abstract=True)
statements_Assert = Class(name="statements_Assert")
Conditional = Class(name="Conditional")
statements_Break = Class(name="statements_Break")
Jump = Class(name="Jump")
statements_Block = Class(name="statements_Block")
Modifiable = Class(name="Modifiable")
statements_CatchBlock = Class(name="statements_CatchBlock")
OrdinaryParameter = Class(name="OrdinaryParameter")
statements_Condition = Class(name="statements_Condition")
StatementContainer = Class(name="StatementContainer")
statements_LocalVariableStatement = Class(name="statements_LocalVariableStatement")
statements_Jump = Class(name="statements_Jump", is_abstract=True)
JumpLabel = Class(name="JumpLabel")
statements_JumpLabel = Class(name="statements_JumpLabel")
statements_Throw = Class(name="statements_Throw")
statements_TryBlock = Class(name="statements_TryBlock")
CatchBlock = Class(name="CatchBlock")
Block = Class(name="Block")
statements_WhileLoop = Class(name="statements_WhileLoop")
types_Type = Class(name="types_Type", is_abstract=True)
LocalVariable = Class(name="LocalVariable")
statements_NormalSwitchCase = Class(name="statements_NormalSwitchCase")
statements_Return = Class(name="statements_Return")
statements_Switch = Class(name="statements_Switch")
statements_SynchronizedBlock = Class(name="statements_SynchronizedBlock")
ClassifierReference = Class(name="ClassifierReference")
types_PrimitiveType = Class(name="types_PrimitiveType", is_abstract=True)
types_Boolean = Class(name="types_Boolean")
types_Byte = Class(name="types_Byte")
types_Char = Class(name="types_Char")
types_Double = Class(name="types_Double")
types_Float = Class(name="types_Float")
types_Int = Class(name="types_Int")
types_Long = Class(name="types_Long")
types_Short = Class(name="types_Short")
types_Void = Class(name="types_Void")
types_TypedElement = Class(name="types_TypedElement", is_abstract=True)
types_TypeReference = Class(name="types_TypeReference", is_abstract=True)
types_ClassifierReference = Class(name="types_ClassifierReference")
types_NamespaceClassifierReference = Class(name="types_NamespaceClassifierReference")
variables_Variable = Class(name="variables_Variable", is_abstract=True)
variables_LocalVariable = Class(name="variables_LocalVariable")
AdditionalLocalVariable = Class(name="AdditionalLocalVariable")
variables_AdditionalLocalVariable = Class(name="variables_AdditionalLocalVariable")

# AnnotationParameter class attributes and methods

# annotations_AnnotationParameter class attributes and methods

# annotations_SingleAnnotationParameter class attributes and methods

# AnnotationValue class attributes and methods

# annotations_AnnotationParameterList class attributes and methods

# AnnotationAttributeSetting class attributes and methods

# annotations_AnnotationAttributeSetting class attributes and methods

# InterfaceMethod class attributes and methods

# annotations_AnnotationValue class attributes and methods

# annotations_AnnotationAttribute class attributes and methods

# annotations_Annotable class attributes and methods

# Commentable class attributes and methods

# AnnotationInstance class attributes and methods

# annotations_AnnotationInstance class attributes and methods

# Reference class attributes and methods

# AnnotationInstanceOrModifier class attributes and methods

# NamespaceAwareElement class attributes and methods

# Classifier class attributes and methods

# ArrayInitializer class attributes and methods

# arrays_ArraySelector class attributes and methods

# classifiers_Classifier class attributes and methods
classifiers_Classifier_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
classifiers_Classifier.methods={classifiers_Classifier_m_getAllSuperClassifiers}

# Type class attributes and methods

# ReferenceableElement class attributes and methods

# classifiers_ConcreteClassifier class attributes and methods
classifiers_ConcreteClassifier_fullName: Property = Property(name="fullName", type=StringType)
classifiers_ConcreteClassifier_m_getInnerClassifiers: Method = Method(name="getInnerClassifiers", parameters={}, type=StringType)
classifiers_ConcreteClassifier_m_getAllInnerClassifiers: Method = Method(name="getAllInnerClassifiers", parameters={}, type=StringType)
classifiers_ConcreteClassifier_m_getSuperTypeReferences: Method = Method(name="getSuperTypeReferences", parameters={}, type=StringType)
classifiers_ConcreteClassifier_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='classifiers_context', type=StringType)}, type=StringType)
classifiers_ConcreteClassifier.attributes={classifiers_ConcreteClassifier_fullName}
classifiers_ConcreteClassifier.methods={classifiers_ConcreteClassifier_m_getAllInnerClassifiers, classifiers_ConcreteClassifier_m_getSuperTypeReferences, classifiers_ConcreteClassifier_m_getAllMembers, classifiers_ConcreteClassifier_m_getInnerClassifiers}

# TypeParametrizable class attributes and methods

# MemberContainer class attributes and methods

# Member class attributes and methods

# Statement class attributes and methods

# AnnotableAndModifiable class attributes and methods

# classifiers_Implementor class attributes and methods

# Expression class attributes and methods

# arrays_ArrayTypeable class attributes and methods
arrays_ArrayTypeable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
arrays_ArrayTypeable.methods={arrays_ArrayTypeable_m_getArrayDimension}

# ArrayDimension class attributes and methods

# arrays_ArrayDimension class attributes and methods

# arrays_ArrayInitializer class attributes and methods

# ArrayInitializationValue class attributes and methods

# arrays_ArrayInitializationValue class attributes and methods

# arrays_ArrayInstantiationBySize class attributes and methods

# TypedElement class attributes and methods

# ArrayTypeable class attributes and methods

# arrays_ArrayInstantiationByValues class attributes and methods

# EnumConstant class attributes and methods

# classifiers_Annotation class attributes and methods
classifiers_Annotation_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
classifiers_Annotation.methods={classifiers_Annotation_m_getAllSuperClassifiers}

# classifiers_AnonymousClass class attributes and methods
classifiers_AnonymousClass_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
classifiers_AnonymousClass_m_getSuperClassifier: Method = Method(name="getSuperClassifier", parameters={}, type=StringType)
classifiers_AnonymousClass_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='classifiers_context', type=StringType)}, type=StringType)
classifiers_AnonymousClass.methods={classifiers_AnonymousClass_m_getSuperClassifier, classifiers_AnonymousClass_m_getAllMembers, classifiers_AnonymousClass_m_getAllSuperClassifiers}

# commons_Commentable class attributes and methods
commons_Commentable_comments: Property = Property(name="comments", type=StringType)
commons_Commentable_m_getConcreteClassifier: Method = Method(name="getConcreteClassifier", parameters={Parameter(name='commons_name', type=StringType)}, type=StringType)
commons_Commentable_m_getConcreteClassifierProxy: Method = Method(name="getConcreteClassifierProxy", parameters={Parameter(name='commons_name', type=StringType)}, type=StringType)
commons_Commentable_m_getConcreteClassifiers: Method = Method(name="getConcreteClassifiers", parameters={Parameter(name='commons_classifierQuery', type=StringType), Parameter(name='commons_packageName', type=StringType)}, type=StringType)
commons_Commentable_m_getConcreteClassifierProxies: Method = Method(name="getConcreteClassifierProxies", parameters={Parameter(name='commons_classifierQuery', type=StringType), Parameter(name='commons_packageName', type=StringType)}, type=StringType)
commons_Commentable_m_getLibClass: Method = Method(name="getLibClass", parameters={Parameter(name='commons_name', type=StringType)}, type=StringType)
commons_Commentable_m_getLibInterface: Method = Method(name="getLibInterface", parameters={Parameter(name='commons_name', type=StringType)}, type=StringType)
commons_Commentable_m_getClassClass: Method = Method(name="getClassClass", parameters={}, type=StringType)
commons_Commentable_m_getObjectClass: Method = Method(name="getObjectClass", parameters={}, type=StringType)
commons_Commentable_m_getStringClass: Method = Method(name="getStringClass", parameters={}, type=StringType)
commons_Commentable_m_getAnnotationInterface: Method = Method(name="getAnnotationInterface", parameters={}, type=StringType)
commons_Commentable_m_getContainingAnnotationInstance: Method = Method(name="getContainingAnnotationInstance", parameters={}, type=StringType)
commons_Commentable_m_getContainingAnonymousClass: Method = Method(name="getContainingAnonymousClass", parameters={}, type=StringType)
commons_Commentable_m_getContainingConcreteClassifier: Method = Method(name="getContainingConcreteClassifier", parameters={}, type=StringType)
commons_Commentable_m_getContainingCompilationUnit: Method = Method(name="getContainingCompilationUnit", parameters={}, type=StringType)
commons_Commentable_m_getContainingPackageName: Method = Method(name="getContainingPackageName", parameters={}, type=StringType)
commons_Commentable_m_getParentConcreteClassifier: Method = Method(name="getParentConcreteClassifier", parameters={}, type=StringType)
commons_Commentable.attributes={commons_Commentable_comments}
commons_Commentable.methods={commons_Commentable_m_getConcreteClassifierProxy, commons_Commentable_m_getContainingConcreteClassifier, commons_Commentable_m_getContainingPackageName, commons_Commentable_m_getClassClass, commons_Commentable_m_getObjectClass, commons_Commentable_m_getStringClass, commons_Commentable_m_getContainingAnnotationInstance, commons_Commentable_m_getAnnotationInterface, commons_Commentable_m_getParentConcreteClassifier, commons_Commentable_m_getContainingAnonymousClass, commons_Commentable_m_getConcreteClassifier, commons_Commentable_m_getConcreteClassifiers, commons_Commentable_m_getLibClass, commons_Commentable_m_getLibInterface, commons_Commentable_m_getContainingCompilationUnit, commons_Commentable_m_getConcreteClassifierProxies}

# TypeReference class attributes and methods

# classifiers_Class class attributes and methods
classifiers_Class_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
classifiers_Class_m_getSuperClass: Method = Method(name="getSuperClass", parameters={}, type=StringType)
classifiers_Class_m_unWrapPrimitiveType: Method = Method(name="unWrapPrimitiveType", parameters={}, type=StringType)
classifiers_Class.methods={classifiers_Class_m_getSuperClass, classifiers_Class_m_getAllSuperClassifiers, classifiers_Class_m_unWrapPrimitiveType}

# ConcreteClassifier class attributes and methods

# Implementor class attributes and methods

# classifiers_Interface class attributes and methods
classifiers_Interface_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
classifiers_Interface.methods={classifiers_Interface_m_getAllSuperClassifiers}

# classifiers_Enumeration class attributes and methods
classifiers_Enumeration_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
classifiers_Enumeration_m_getContainedConstant: Method = Method(name="getContainedConstant", parameters={Parameter(name='classifiers_name', type=StringType)}, type=StringType)
classifiers_Enumeration.methods={classifiers_Enumeration_m_getContainedConstant, classifiers_Enumeration_m_getAllSuperClassifiers}

# containers_Package class attributes and methods

# Annotable class attributes and methods

# CompilationUnit class attributes and methods

# Package class attributes and methods

# containers_EmptyModel class attributes and methods

# expressions_ExpressionList class attributes and methods

# ForLoopInitializer class attributes and methods

# expressions_Expression class attributes and methods
expressions_Expression_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
expressions_Expression_m_getAlternativeType: Method = Method(name="getAlternativeType", parameters={}, type=StringType)
expressions_Expression_m_getOneType: Method = Method(name="getOneType", parameters={Parameter(name='expressions_alternative', type=StringType)}, type=StringType)
expressions_Expression_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
expressions_Expression.methods={expressions_Expression_m_getAlternativeType, expressions_Expression_m_getArrayDimension, expressions_Expression_m_getOneType, expressions_Expression_m_getType}

# commons_NamedElement class attributes and methods
commons_NamedElement_name: Property = Property(name="name", type=StringType)
commons_NamedElement.attributes={commons_NamedElement_name}

# commons_NamespaceAwareElement class attributes and methods
commons_NamespaceAwareElement_namespaces: Property = Property(name="namespaces", type=StringType)
commons_NamespaceAwareElement_m_getNamespacesAsString: Method = Method(name="getNamespacesAsString", parameters={}, type=StringType)
commons_NamespaceAwareElement_m_getClassifierAtNamespaces: Method = Method(name="getClassifierAtNamespaces", parameters={}, type=StringType)
commons_NamespaceAwareElement.attributes={commons_NamespaceAwareElement_namespaces}
commons_NamespaceAwareElement.methods={commons_NamespaceAwareElement_m_getNamespacesAsString, commons_NamespaceAwareElement_m_getClassifierAtNamespaces}

# containers_JavaRoot class attributes and methods
containers_JavaRoot_m_getClassifiersInSamePackage: Method = Method(name="getClassifiersInSamePackage", parameters={}, type=StringType)
containers_JavaRoot.methods={containers_JavaRoot_m_getClassifiersInSamePackage}

# NamedElement class attributes and methods

# ImportingElement class attributes and methods

# containers_CompilationUnit class attributes and methods
containers_CompilationUnit_m_getContainedClassifier: Method = Method(name="getContainedClassifier", parameters={Parameter(name='containers_name', type=StringType)}, type=StringType)
containers_CompilationUnit_m_getClassifiersInSamePackage: Method = Method(name="getClassifiersInSamePackage", parameters={}, type=StringType)
containers_CompilationUnit.methods={containers_CompilationUnit_m_getClassifiersInSamePackage, containers_CompilationUnit_m_getContainedClassifier}

# JavaRoot class attributes and methods

# ConditionalAndExpressionChild class attributes and methods

# expressions_ConditionalAndExpressionChild class attributes and methods

# expressions_InclusiveOrExpression class attributes and methods

# InclusiveOrExpressionChild class attributes and methods

# expressions_InclusiveOrExpressionChild class attributes and methods

# expressions_ExclusiveOrExpression class attributes and methods

# ExclusiveOrExpressionChild class attributes and methods

# expressions_ExclusiveOrExpressionChild class attributes and methods

# expressions_AndExpression class attributes and methods

# AndExpressionChild class attributes and methods

# expressions_AndExpressionChild class attributes and methods

# expressions_EqualityExpression class attributes and methods

# EqualityOperator class attributes and methods

# expressions_AssignmentExpression class attributes and methods

# AssignmentExpressionChild class attributes and methods

# AssignmentOperator class attributes and methods

# expressions_AssignmentExpressionChild class attributes and methods

# expressions_ConditionalExpression class attributes and methods

# ConditionalExpressionChild class attributes and methods

# expressions_ConditionalExpressionChild class attributes and methods

# expressions_ConditionalOrExpression class attributes and methods

# ConditionalOrExpressionChild class attributes and methods

# expressions_ConditionalOrExpressionChild class attributes and methods

# expressions_ConditionalAndExpression class attributes and methods

# AdditiveExpressionChild class attributes and methods

# AdditiveOperator class attributes and methods

# expressions_AdditiveExpressionChild class attributes and methods

# expressions_MultiplicativeExpression class attributes and methods

# MultiplicativeExpressionChild class attributes and methods

# MultiplicativeOperator class attributes and methods

# expressions_MultiplicativeExpressionChild class attributes and methods

# expressions_UnaryExpression class attributes and methods

# UnaryOperator class attributes and methods

# UnaryExpressionChild class attributes and methods

# EqualityExpressionChild class attributes and methods

# expressions_EqualityExpressionChild class attributes and methods

# expressions_InstanceOfExpression class attributes and methods

# InstanceOfExpressionChild class attributes and methods

# expressions_InstanceOfExpressionChild class attributes and methods

# expressions_RelationExpression class attributes and methods

# RelationExpressionChild class attributes and methods

# RelationOperator class attributes and methods

# expressions_RelationExpressionChild class attributes and methods

# expressions_ShiftExpression class attributes and methods

# ShiftExpressionChild class attributes and methods

# ShiftOperator class attributes and methods

# expressions_ShiftExpressionChild class attributes and methods

# expressions_AdditiveExpression class attributes and methods

# generics_CallTypeArgumentable class attributes and methods

# generics_TypeParametrizable class attributes and methods

# TypeParameter class attributes and methods

# generics_ExtendsTypeArgument class attributes and methods

# generics_QualifiedTypeArgument class attributes and methods

# generics_SuperTypeArgument class attributes and methods

# generics_TypeParameter class attributes and methods
generics_TypeParameter_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
generics_TypeParameter_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='generics_context', type=StringType)}, type=StringType)
generics_TypeParameter_m_getBoundType: Method = Method(name="getBoundType", parameters={Parameter(name='generics_typeReference', type=StringType), Parameter(name='generics_reference', type=StringType)}, type=StringType)
generics_TypeParameter.methods={generics_TypeParameter_m_getBoundType, generics_TypeParameter_m_getAllSuperClassifiers, generics_TypeParameter_m_getAllMembers}

# expressions_UnaryExpressionChild class attributes and methods

# expressions_UnaryModificationExpression class attributes and methods

# UnaryModificationExpressionChild class attributes and methods

# UnaryModificationOperator class attributes and methods

# expressions_PrefixUnaryModificationExpression class attributes and methods

# UnaryModificationExpression class attributes and methods

# expressions_SuffixUnaryModificationExpression class attributes and methods

# expressions_UnaryModificationExpressionChild class attributes and methods

# expressions_CastExpression class attributes and methods

# expressions_PrimaryExpression class attributes and methods

# expressions_NestedExpression class attributes and methods

# generics_TypeArgument class attributes and methods

# generics_TypeArgumentable class attributes and methods

# TypeArgument class attributes and methods

# imports_StaticClassifierImport class attributes and methods

# StaticImport class attributes and methods

# imports_StaticMemberImport class attributes and methods

# instantiations_Initializable class attributes and methods

# instantiations_Instantiation class attributes and methods

# Argumentable class attributes and methods

# TypeArgumentable class attributes and methods

# instantiations_NewConstructorCall class attributes and methods

# Instantiation class attributes and methods

# CallTypeArgumentable class attributes and methods

# AnonymousClass class attributes and methods

# instantiations_ExplicitConstructorCall class attributes and methods

# Self class attributes and methods

# generics_UnknownTypeArgument class attributes and methods

# imports_Import class attributes and methods
imports_Import_m_getImportedClassifier: Method = Method(name="getImportedClassifier", parameters={Parameter(name='imports_name', type=StringType)}, type=StringType)
imports_Import_m_getImportedClassifiers: Method = Method(name="getImportedClassifiers", parameters={}, type=StringType)
imports_Import_m_getImportedMembers: Method = Method(name="getImportedMembers", parameters={}, type=StringType)
imports_Import.methods={imports_Import_m_getImportedMembers, imports_Import_m_getImportedClassifiers, imports_Import_m_getImportedClassifier}

# imports_ImportingElement class attributes and methods
imports_ImportingElement_m_getDefaultImports: Method = Method(name="getDefaultImports", parameters={}, type=StringType)
imports_ImportingElement.methods={imports_ImportingElement_m_getDefaultImports}

# Import class attributes and methods

# imports_StaticImport class attributes and methods

# Static class attributes and methods

# imports_ClassifierImport class attributes and methods

# imports_PackageImport class attributes and methods

# literals_OctalIntegerLiteral class attributes and methods
literals_OctalIntegerLiteral_octalValue: Property = Property(name="octalValue", type=StringType)
literals_OctalIntegerLiteral.attributes={literals_OctalIntegerLiteral_octalValue}

# literals_LongLiteral class attributes and methods

# literals_DecimalLongLiteral class attributes and methods
literals_DecimalLongLiteral_decimalValue: Property = Property(name="decimalValue", type=StringType)
literals_DecimalLongLiteral.attributes={literals_DecimalLongLiteral_decimalValue}

# LongLiteral class attributes and methods

# literals_HexLongLiteral class attributes and methods
literals_HexLongLiteral_hexValue: Property = Property(name="hexValue", type=StringType)
literals_HexLongLiteral.attributes={literals_HexLongLiteral_hexValue}

# literals_OctalLongLiteral class attributes and methods
literals_OctalLongLiteral_octalValue: Property = Property(name="octalValue", type=StringType)
literals_OctalLongLiteral.attributes={literals_OctalLongLiteral_octalValue}

# literals_NullLiteral class attributes and methods

# literals_Super class attributes and methods

# literals_This class attributes and methods

# members_ExceptionThrower class attributes and methods

# NamespaceClassifierReference class attributes and methods

# literals_Literal class attributes and methods
literals_Literal_m_getOneType: Method = Method(name="getOneType", parameters={Parameter(name='literals_alternative', type=StringType)}, type=StringType)
literals_Literal.methods={literals_Literal_m_getOneType}

# PrimaryExpression class attributes and methods

# literals_Self class attributes and methods

# literals_BooleanLiteral class attributes and methods
literals_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
literals_BooleanLiteral.attributes={literals_BooleanLiteral_value}

# Literal class attributes and methods

# literals_CharacterLiteral class attributes and methods
literals_CharacterLiteral_value: Property = Property(name="value", type=StringType)
literals_CharacterLiteral.attributes={literals_CharacterLiteral_value}

# literals_FloatLiteral class attributes and methods

# literals_DecimalFloatLiteral class attributes and methods
literals_DecimalFloatLiteral_decimalValue: Property = Property(name="decimalValue", type=FloatType)
literals_DecimalFloatLiteral.attributes={literals_DecimalFloatLiteral_decimalValue}

# FloatLiteral class attributes and methods

# literals_HexFloatLiteral class attributes and methods
literals_HexFloatLiteral_hexValue: Property = Property(name="hexValue", type=FloatType)
literals_HexFloatLiteral.attributes={literals_HexFloatLiteral_hexValue}

# literals_DoubleLiteral class attributes and methods

# literals_DecimalDoubleLiteral class attributes and methods
literals_DecimalDoubleLiteral_decimalValue: Property = Property(name="decimalValue", type=FloatType)
literals_DecimalDoubleLiteral.attributes={literals_DecimalDoubleLiteral_decimalValue}

# DoubleLiteral class attributes and methods

# literals_HexDoubleLiteral class attributes and methods
literals_HexDoubleLiteral_hexValue: Property = Property(name="hexValue", type=FloatType)
literals_HexDoubleLiteral.attributes={literals_HexDoubleLiteral_hexValue}

# literals_IntegerLiteral class attributes and methods

# literals_DecimalIntegerLiteral class attributes and methods
literals_DecimalIntegerLiteral_decimalValue: Property = Property(name="decimalValue", type=StringType)
literals_DecimalIntegerLiteral.attributes={literals_DecimalIntegerLiteral_decimalValue}

# IntegerLiteral class attributes and methods

# literals_HexIntegerLiteral class attributes and methods
literals_HexIntegerLiteral_hexValue: Property = Property(name="hexValue", type=StringType)
literals_HexIntegerLiteral.attributes={literals_HexIntegerLiteral_hexValue}

# members_Field class attributes and methods

# Variable class attributes and methods

# AdditionalField class attributes and methods

# members_Method class attributes and methods
members_Method_m_isMethodForCall: Method = Method(name="isMethodForCall", parameters={Parameter(name='members_methodCall', type=StringType), Parameter(name='members_needsPerfectMatch', type=StringType)}, type=BooleanType)
members_Method_m_isSomeMethodForCall: Method = Method(name="isSomeMethodForCall", parameters={Parameter(name='members_methodCall', type=StringType)}, type=BooleanType)
members_Method_m_isBetterMethodForCall: Method = Method(name="isBetterMethodForCall", parameters={Parameter(name='members_otherMethod', type=StringType), Parameter(name='members_methodCall', type=StringType)}, type=BooleanType)
members_Method_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
members_Method.methods={members_Method_m_isSomeMethodForCall, members_Method_m_isBetterMethodForCall, members_Method_m_isMethodForCall, members_Method_m_getArrayDimension}

# members_Member class attributes and methods

# members_MemberContainer class attributes and methods
members_MemberContainer_m_getContainedClassifier: Method = Method(name="getContainedClassifier", parameters={Parameter(name='members_name', type=StringType)}, type=StringType)
members_MemberContainer_m_getContainedField: Method = Method(name="getContainedField", parameters={Parameter(name='members_name', type=StringType)}, type=StringType)
members_MemberContainer_m_getContainedMethod: Method = Method(name="getContainedMethod", parameters={Parameter(name='members_name', type=StringType)}, type=StringType)
members_MemberContainer.methods={members_MemberContainer_m_getContainedMethod, members_MemberContainer_m_getContainedClassifier, members_MemberContainer_m_getContainedField}

# members_AdditionalField class attributes and methods
members_AdditionalField_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
members_AdditionalField.methods={members_AdditionalField_m_getArrayDimension}

# Initializable class attributes and methods

# members_Constructor class attributes and methods

# StatementListContainer class attributes and methods

# Parametrizable class attributes and methods

# ExceptionThrower class attributes and methods

# members_EmptyMember class attributes and methods

# modifiers_Native class attributes and methods

# modifiers_Protected class attributes and methods

# modifiers_Public class attributes and methods

# modifiers_Private class attributes and methods

# modifiers_Static class attributes and methods

# modifiers_Strictfp class attributes and methods

# modifiers_Synchronized class attributes and methods

# modifiers_Transient class attributes and methods

# modifiers_Volatile class attributes and methods

# operators_Operator class attributes and methods

# operators_AdditiveOperator class attributes and methods

# Operator class attributes and methods

# operators_AssignmentOperator class attributes and methods

# operators_EqualityOperator class attributes and methods

# operators_MultiplicativeOperator class attributes and methods

# operators_RelationOperator class attributes and methods

# operators_ShiftOperator class attributes and methods

# members_InterfaceMethod class attributes and methods

# Method class attributes and methods

# members_ClassMethod class attributes and methods

# members_EnumConstant class attributes and methods

# modifiers_Modifier class attributes and methods

# modifiers_AnnotationInstanceOrModifier class attributes and methods

# modifiers_AnnotableAndModifiable class attributes and methods
modifiers_AnnotableAndModifiable_m_isHidden: Method = Method(name="isHidden", parameters={Parameter(name='modifiers_context', type=StringType)}, type=BooleanType)
modifiers_AnnotableAndModifiable_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
modifiers_AnnotableAndModifiable.methods={modifiers_AnnotableAndModifiable_m_isStatic, modifiers_AnnotableAndModifiable_m_isHidden}

# modifiers_Modifiable class attributes and methods

# Modifier class attributes and methods

# modifiers_Abstract class attributes and methods

# modifiers_Final class attributes and methods

# operators_Multiplication class attributes and methods

# operators_Remainder class attributes and methods

# operators_Complement class attributes and methods

# operators_MinusMinus class attributes and methods

# operators_Negate class attributes and methods

# operators_PlusPlus class attributes and methods

# operators_LeftShift class attributes and methods

# operators_RightShift class attributes and methods

# operators_UnsignedRightShift class attributes and methods

# parameters_Parameter class attributes and methods

# parameters_Parametrizable class attributes and methods

# Parameter class attributes and methods

# parameters_OrdinaryParameter class attributes and methods

# parameters_VariableLengthParameter class attributes and methods

# operators_UnaryOperator class attributes and methods

# operators_UnaryModificationOperator class attributes and methods

# operators_Assignment class attributes and methods

# operators_AssignmentAnd class attributes and methods

# operators_AssignmentDivision class attributes and methods

# operators_AssignmentExclusiveOr class attributes and methods

# operators_AssignmentMinus class attributes and methods

# operators_AssignmentModulo class attributes and methods

# operators_AssignmentMultiplication class attributes and methods

# operators_AssignmentLeftShift class attributes and methods

# operators_AssignmentOr class attributes and methods

# operators_AssignmentPlus class attributes and methods

# operators_AssignmentRightShift class attributes and methods

# operators_AssignmentUnsignedRightShift class attributes and methods

# operators_Equal class attributes and methods

# operators_NotEqual class attributes and methods

# operators_GreaterThan class attributes and methods

# operators_GreaterThanOrEqual class attributes and methods

# operators_LessThan class attributes and methods

# operators_LessThanOrEqual class attributes and methods

# operators_Addition class attributes and methods

# operators_Subtraction class attributes and methods

# operators_Division class attributes and methods

# references_PrimitiveTypeReference class attributes and methods

# PrimitiveType class attributes and methods

# references_StringReference class attributes and methods
references_StringReference_value: Property = Property(name="value", type=StringType)
references_StringReference.attributes={references_StringReference_value}

# references_SelfReference class attributes and methods

# statements_StatementContainer class attributes and methods

# statements_StatementListContainer class attributes and methods

# references_Reference class attributes and methods
references_Reference_m_getReferencedType: Method = Method(name="getReferencedType", parameters={}, type=StringType)
references_Reference_m_getPrevious: Method = Method(name="getPrevious", parameters={}, type=StringType)
references_Reference.methods={references_Reference_m_getPrevious, references_Reference_m_getReferencedType}

# ArraySelector class attributes and methods

# references_Argumentable class attributes and methods
references_Argumentable_m_getArgumentTypes: Method = Method(name="getArgumentTypes", parameters={}, type=StringType)
references_Argumentable.methods={references_Argumentable_m_getArgumentTypes}

# references_ReferenceableElement class attributes and methods

# references_ElementReference class attributes and methods

# references_IdentifierReference class attributes and methods

# ElementReference class attributes and methods

# references_MethodCall class attributes and methods

# references_ReflectiveClassReference class attributes and methods

# statements_Continue class attributes and methods

# statements_DefaultSwitchCase class attributes and methods

# SwitchCase class attributes and methods

# statements_DoWhileLoop class attributes and methods

# WhileLoop class attributes and methods

# statements_EmptyStatement class attributes and methods

# statements_ExpressionStatement class attributes and methods

# statements_ForLoop class attributes and methods

# statements_ForEachLoop class attributes and methods

# statements_Conditional class attributes and methods

# statements_ForLoopInitializer class attributes and methods

# statements_Statement class attributes and methods

# statements_SwitchCase class attributes and methods

# statements_Assert class attributes and methods

# Conditional class attributes and methods

# statements_Break class attributes and methods

# Jump class attributes and methods

# statements_Block class attributes and methods

# Modifiable class attributes and methods

# statements_CatchBlock class attributes and methods

# OrdinaryParameter class attributes and methods

# statements_Condition class attributes and methods

# StatementContainer class attributes and methods

# statements_LocalVariableStatement class attributes and methods

# statements_Jump class attributes and methods

# JumpLabel class attributes and methods

# statements_JumpLabel class attributes and methods

# statements_Throw class attributes and methods

# statements_TryBlock class attributes and methods

# CatchBlock class attributes and methods

# Block class attributes and methods

# statements_WhileLoop class attributes and methods

# types_Type class attributes and methods
types_Type_m_equalsType: Method = Method(name="equalsType", parameters={Parameter(name='types_otherArrayDimension', type=StringType), Parameter(name='types_otherType', type=StringType), Parameter(name='types_arrayDimension', type=StringType)}, type=BooleanType)
types_Type_m_isSuperType: Method = Method(name="isSuperType", parameters={Parameter(name='types_arrayDimension', type=StringType), Parameter(name='types_otherArrayType', type=StringType), Parameter(name='types_otherType', type=StringType)}, type=BooleanType)
types_Type_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='types_context', type=StringType)}, type=StringType)
types_Type.methods={types_Type_m_isSuperType, types_Type_m_equalsType, types_Type_m_getAllMembers}

# LocalVariable class attributes and methods

# statements_NormalSwitchCase class attributes and methods

# statements_Return class attributes and methods

# statements_Switch class attributes and methods

# statements_SynchronizedBlock class attributes and methods

# ClassifierReference class attributes and methods

# types_PrimitiveType class attributes and methods
types_PrimitiveType_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='types_context', type=StringType)}, type=StringType)
types_PrimitiveType_m_wrapPrimitiveType: Method = Method(name="wrapPrimitiveType", parameters={}, type=StringType)
types_PrimitiveType.methods={types_PrimitiveType_m_getAllMembers, types_PrimitiveType_m_wrapPrimitiveType}

# types_Boolean class attributes and methods

# types_Byte class attributes and methods

# types_Char class attributes and methods

# types_Double class attributes and methods

# types_Float class attributes and methods

# types_Int class attributes and methods

# types_Long class attributes and methods

# types_Short class attributes and methods

# types_Void class attributes and methods

# types_TypedElement class attributes and methods

# types_TypeReference class attributes and methods
types_TypeReference_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
types_TypeReference_m_getBoundTarget: Method = Method(name="getBoundTarget", parameters={Parameter(name='types_reference', type=StringType)}, type=StringType)
types_TypeReference_m_getPureClassifierReference: Method = Method(name="getPureClassifierReference", parameters={}, type=StringType)
types_TypeReference.methods={types_TypeReference_m_getBoundTarget, types_TypeReference_m_getTarget, types_TypeReference_m_getPureClassifierReference}

# types_ClassifierReference class attributes and methods

# types_NamespaceClassifierReference class attributes and methods

# variables_Variable class attributes and methods
variables_Variable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
variables_Variable.methods={variables_Variable_m_getArrayDimension}

# variables_LocalVariable class attributes and methods

# AdditionalLocalVariable class attributes and methods

# variables_AdditionalLocalVariable class attributes and methods
variables_AdditionalLocalVariable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
variables_AdditionalLocalVariable.methods={variables_AdditionalLocalVariable_m_getArrayDimension}

# Relationships
parameter2: BinaryAssociation = BinaryAssociation(
    name="parameter2",
    ends={
        Property(name="AnnotationParameter", type=annotations_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_AnnotationInstance3", type=AnnotationParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value4: BinaryAssociation = BinaryAssociation(
    name="value4",
    ends={
        Property(name="AnnotationValue", type=annotations_SingleAnnotationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_SingleAnnotationParameter", type=AnnotationValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
settings5: BinaryAssociation = BinaryAssociation(
    name="settings5",
    ends={
        Property(name="AnnotationAttributeSetting", type=annotations_AnnotationParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_AnnotationParameterList", type=AnnotationAttributeSetting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute6: BinaryAssociation = BinaryAssociation(
    name="attribute6",
    ends={
        Property(name="InterfaceMethod", type=annotations_AnnotationAttributeSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_AnnotationAttributeSetting", type=InterfaceMethod, multiplicity=Multiplicity(1, 1))
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="AnnotationValue9", type=annotations_AnnotationAttributeSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_AnnotationAttributeSetting8", type=AnnotationValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="AnnotationInstance", type=annotations_Annotable, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_Annotable", type=AnnotationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation1: BinaryAssociation = BinaryAssociation(
    name="annotation1",
    ends={
        Property(name="Classifier", type=annotations_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_AnnotationInstance", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
arrayInitializer18: BinaryAssociation = BinaryAssociation(
    name="arrayInitializer18",
    ends={
        Property(name="ArrayInitializer", type=arrays_ArrayInstantiationByValues, multiplicity=Multiplicity(1, 1)),
        Property(name="arrays_ArrayInstantiationByValues", type=ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position19: BinaryAssociation = BinaryAssociation(
    name="position19",
    ends={
        Property(name="Expression20", type=arrays_ArraySelector, multiplicity=Multiplicity(1, 1)),
        Property(name="arrays_ArraySelector", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue10: BinaryAssociation = BinaryAssociation(
    name="defaultValue10",
    ends={
        Property(name="Expression", type=annotations_AnnotationAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations_AnnotationAttribute", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayDimensionsBefore11: BinaryAssociation = BinaryAssociation(
    name="arrayDimensionsBefore11",
    ends={
        Property(name="ArrayDimension", type=arrays_ArrayTypeable, multiplicity=Multiplicity(1, 1)),
        Property(name="arrays_ArrayTypeable", type=ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayDimensionsAfter12: BinaryAssociation = BinaryAssociation(
    name="arrayDimensionsAfter12",
    ends={
        Property(name="ArrayDimension14", type=arrays_ArrayTypeable, multiplicity=Multiplicity(1, 1)),
        Property(name="arrays_ArrayTypeable13", type=ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValues15: BinaryAssociation = BinaryAssociation(
    name="initialValues15",
    ends={
        Property(name="ArrayInitializationValue", type=arrays_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="arrays_ArrayInitializer", type=ArrayInitializationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sizes16: BinaryAssociation = BinaryAssociation(
    name="sizes16",
    ends={
        Property(name="Expression17", type=arrays_ArrayInstantiationBySize, multiplicity=Multiplicity(1, 1)),
        Property(name="arrays_ArrayInstantiationBySize", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants32: BinaryAssociation = BinaryAssociation(
    name="constants32",
    ends={
        Property(name="EnumConstant", type=classifiers_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="classifiers_Enumeration", type=EnumConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements21: BinaryAssociation = BinaryAssociation(
    name="implements21",
    ends={
        Property(name="TypeReference", type=classifiers_Implementor, multiplicity=Multiplicity(1, 1)),
        Property(name="classifiers_Implementor", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends22: BinaryAssociation = BinaryAssociation(
    name="extends22",
    ends={
        Property(name="TypeReference23", type=classifiers_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classifiers_Class", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExtends24: BinaryAssociation = BinaryAssociation(
    name="defaultExtends24",
    ends={
        Property(name="TypeReference26", type=classifiers_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="classifiers_Class25", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends27: BinaryAssociation = BinaryAssociation(
    name="extends27",
    ends={
        Property(name="TypeReference28", type=classifiers_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="classifiers_Interface", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultExtends29: BinaryAssociation = BinaryAssociation(
    name="defaultExtends29",
    ends={
        Property(name="TypeReference31", type=classifiers_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="classifiers_Interface30", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifiers33: BinaryAssociation = BinaryAssociation(
    name="classifiers33",
    ends={
        Property(name="ConcreteClassifier", type=containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="containers_CompilationUnit", type=ConcreteClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits34: BinaryAssociation = BinaryAssociation(
    name="compilationUnits34",
    ends={
        Property(name="CompilationUnit", type=containers_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="containers_Package", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subpackages35: BinaryAssociation = BinaryAssociation(
    name="subpackages35",
    ends={
        Property(name="Package", type=containers_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="containers_Package36", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions37: BinaryAssociation = BinaryAssociation(
    name="expressions37",
    ends={
        Property(name="Expression38", type=expressions_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ExpressionList", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children53: BinaryAssociation = BinaryAssociation(
    name="children53",
    ends={
        Property(name="ConditionalAndExpressionChild", type=expressions_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalAndExpression", type=ConditionalAndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children54: BinaryAssociation = BinaryAssociation(
    name="children54",
    ends={
        Property(name="InclusiveOrExpressionChild", type=expressions_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_InclusiveOrExpression", type=InclusiveOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children55: BinaryAssociation = BinaryAssociation(
    name="children55",
    ends={
        Property(name="ExclusiveOrExpressionChild", type=expressions_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ExclusiveOrExpression", type=ExclusiveOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children56: BinaryAssociation = BinaryAssociation(
    name="children56",
    ends={
        Property(name="AndExpressionChild", type=expressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AndExpression", type=AndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
equalityOperators57: BinaryAssociation = BinaryAssociation(
    name="equalityOperators57",
    ends={
        Property(name="EqualityOperator", type=expressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_EqualityExpression", type=EqualityOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child39: BinaryAssociation = BinaryAssociation(
    name="child39",
    ends={
        Property(name="AssignmentExpressionChild", type=expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AssignmentExpression", type=AssignmentExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignmentOperator40: BinaryAssociation = BinaryAssociation(
    name="assignmentOperator40",
    ends={
        Property(name="AssignmentOperator", type=expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AssignmentExpression41", type=AssignmentOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value42: BinaryAssociation = BinaryAssociation(
    name="value42",
    ends={
        Property(name="Expression44", type=expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AssignmentExpression43", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child45: BinaryAssociation = BinaryAssociation(
    name="child45",
    ends={
        Property(name="ConditionalExpressionChild", type=expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalExpression", type=ConditionalExpressionChild, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionIf46: BinaryAssociation = BinaryAssociation(
    name="expressionIf46",
    ends={
        Property(name="Expression48", type=expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalExpression47", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressionElse49: BinaryAssociation = BinaryAssociation(
    name="expressionElse49",
    ends={
        Property(name="AssignmentExpressionChild51", type=expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalExpression50", type=AssignmentExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children52: BinaryAssociation = BinaryAssociation(
    name="children52",
    ends={
        Property(name="ConditionalOrExpressionChild", type=expressions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConditionalOrExpression", type=ConditionalOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children67: BinaryAssociation = BinaryAssociation(
    name="children67",
    ends={
        Property(name="AdditiveExpressionChild", type=expressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AdditiveExpression", type=AdditiveExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additiveOperators68: BinaryAssociation = BinaryAssociation(
    name="additiveOperators68",
    ends={
        Property(name="AdditiveOperator", type=expressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AdditiveExpression69", type=AdditiveOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children70: BinaryAssociation = BinaryAssociation(
    name="children70",
    ends={
        Property(name="MultiplicativeExpressionChild", type=expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MultiplicativeExpression", type=MultiplicativeExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
multiplicativeOperators71: BinaryAssociation = BinaryAssociation(
    name="multiplicativeOperators71",
    ends={
        Property(name="MultiplicativeOperator", type=expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MultiplicativeExpression72", type=MultiplicativeOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operators73: BinaryAssociation = BinaryAssociation(
    name="operators73",
    ends={
        Property(name="UnaryOperator", type=expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryExpression", type=UnaryOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child74: BinaryAssociation = BinaryAssociation(
    name="child74",
    ends={
        Property(name="UnaryExpressionChild", type=expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryExpression75", type=UnaryExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children58: BinaryAssociation = BinaryAssociation(
    name="children58",
    ends={
        Property(name="EqualityExpressionChild", type=expressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_EqualityExpression59", type=EqualityExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child60: BinaryAssociation = BinaryAssociation(
    name="child60",
    ends={
        Property(name="InstanceOfExpressionChild", type=expressions_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_InstanceOfExpression", type=InstanceOfExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children61: BinaryAssociation = BinaryAssociation(
    name="children61",
    ends={
        Property(name="RelationExpressionChild", type=expressions_RelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_RelationExpression", type=RelationExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationOperators62: BinaryAssociation = BinaryAssociation(
    name="relationOperators62",
    ends={
        Property(name="RelationOperator", type=expressions_RelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_RelationExpression63", type=RelationOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children64: BinaryAssociation = BinaryAssociation(
    name="children64",
    ends={
        Property(name="ShiftExpressionChild", type=expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ShiftExpression", type=ShiftExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
shiftOperators65: BinaryAssociation = BinaryAssociation(
    name="shiftOperators65",
    ends={
        Property(name="ShiftOperator", type=expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ShiftExpression66", type=ShiftOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
callTypeArguments84: BinaryAssociation = BinaryAssociation(
    name="callTypeArguments84",
    ends={
        Property(name="TypeArgument85", type=generics_CallTypeArgumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="generics_CallTypeArgumentable", type=TypeArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters86: BinaryAssociation = BinaryAssociation(
    name="typeParameters86",
    ends={
        Property(name="TypeParameter", type=generics_TypeParametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="generics_TypeParametrizable", type=TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendTypes87: BinaryAssociation = BinaryAssociation(
    name="extendTypes87",
    ends={
        Property(name="TypeReference88", type=generics_ExtendsTypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="generics_ExtendsTypeArgument", type=TypeReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
superType89: BinaryAssociation = BinaryAssociation(
    name="superType89",
    ends={
        Property(name="TypeReference90", type=generics_SuperTypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="generics_SuperTypeArgument", type=TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child76: BinaryAssociation = BinaryAssociation(
    name="child76",
    ends={
        Property(name="UnaryModificationExpressionChild", type=expressions_UnaryModificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryModificationExpression", type=UnaryModificationExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator77: BinaryAssociation = BinaryAssociation(
    name="operator77",
    ends={
        Property(name="UnaryModificationOperator", type=expressions_UnaryModificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryModificationExpression78", type=UnaryModificationOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child79: BinaryAssociation = BinaryAssociation(
    name="child79",
    ends={
        Property(name="MultiplicativeExpressionChild80", type=expressions_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_CastExpression", type=MultiplicativeExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression81: BinaryAssociation = BinaryAssociation(
    name="expression81",
    ends={
        Property(name="Expression82", type=expressions_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_NestedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments83: BinaryAssociation = BinaryAssociation(
    name="typeArguments83",
    ends={
        Property(name="TypeArgument", type=generics_TypeArgumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="generics_TypeArgumentable", type=TypeArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticMembers97: BinaryAssociation = BinaryAssociation(
    name="staticMembers97",
    ends={
        Property(name="ReferenceableElement", type=imports_StaticMemberImport, multiplicity=Multiplicity(1, 1)),
        Property(name="imports_StaticMemberImport", type=ReferenceableElement, multiplicity=Multiplicity(1, 9999))
    }
)
initialValue98: BinaryAssociation = BinaryAssociation(
    name="initialValue98",
    ends={
        Property(name="Expression99", type=instantiations_Initializable, multiplicity=Multiplicity(1, 1)),
        Property(name="instantiations_Initializable", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousClass100: BinaryAssociation = BinaryAssociation(
    name="anonymousClass100",
    ends={
        Property(name="AnonymousClass", type=instantiations_NewConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="instantiations_NewConstructorCall", type=AnonymousClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callTarget101: BinaryAssociation = BinaryAssociation(
    name="callTarget101",
    ends={
        Property(name="Self", type=instantiations_ExplicitConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="instantiations_ExplicitConstructorCall", type=Self, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendTypes91: BinaryAssociation = BinaryAssociation(
    name="extendTypes91",
    ends={
        Property(name="TypeReference92", type=generics_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="generics_TypeParameter", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports93: BinaryAssociation = BinaryAssociation(
    name="imports93",
    ends={
        Property(name="Import", type=imports_ImportingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="imports_ImportingElement", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
static94: BinaryAssociation = BinaryAssociation(
    name="static94",
    ends={
        Property(name="Static", type=imports_StaticImport, multiplicity=Multiplicity(1, 1)),
        Property(name="imports_StaticImport", type=Static, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier95: BinaryAssociation = BinaryAssociation(
    name="classifier95",
    ends={
        Property(name="ConcreteClassifier96", type=imports_ClassifierImport, multiplicity=Multiplicity(1, 1)),
        Property(name="imports_ClassifierImport", type=ConcreteClassifier, multiplicity=Multiplicity(1, 1))
    }
)
exceptions102: BinaryAssociation = BinaryAssociation(
    name="exceptions102",
    ends={
        Property(name="NamespaceClassifierReference", type=members_ExceptionThrower, multiplicity=Multiplicity(1, 1)),
        Property(name="members_ExceptionThrower", type=NamespaceClassifierReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
additionalFields107: BinaryAssociation = BinaryAssociation(
    name="additionalFields107",
    ends={
        Property(name="AdditionalField", type=members_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="members_Field", type=AdditionalField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members103: BinaryAssociation = BinaryAssociation(
    name="members103",
    ends={
        Property(name="Member", type=members_MemberContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="members_MemberContainer", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultMembers104: BinaryAssociation = BinaryAssociation(
    name="defaultMembers104",
    ends={
        Property(name="Member106", type=members_MemberContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="members_MemberContainer105", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClass108: BinaryAssociation = BinaryAssociation(
    name="anonymousClass108",
    ends={
        Property(name="AnonymousClass109", type=members_EnumConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="members_EnumConstant", type=AnonymousClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationsAndModifiers110: BinaryAssociation = BinaryAssociation(
    name="annotationsAndModifiers110",
    ends={
        Property(name="AnnotationInstanceOrModifier", type=modifiers_AnnotableAndModifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiers_AnnotableAndModifiable", type=AnnotationInstanceOrModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers111: BinaryAssociation = BinaryAssociation(
    name="modifiers111",
    ends={
        Property(name="Modifier", type=modifiers_Modifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="modifiers_Modifiable", type=Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters112: BinaryAssociation = BinaryAssociation(
    name="parameters112",
    ends={
        Property(name="Parameter", type=parameters_Parametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters_Parametrizable", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveType120: BinaryAssociation = BinaryAssociation(
    name="primitiveType120",
    ends={
        Property(name="PrimitiveType", type=references_PrimitiveTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="references_PrimitiveTypeReference", type=PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
self121: BinaryAssociation = BinaryAssociation(
    name="self121",
    ends={
        Property(name="Self122", type=references_SelfReference, multiplicity=Multiplicity(1, 1)),
        Property(name="references_SelfReference", type=Self, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement123: BinaryAssociation = BinaryAssociation(
    name="statement123",
    ends={
        Property(name="Statement", type=statements_StatementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_StatementContainer", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements124: BinaryAssociation = BinaryAssociation(
    name="statements124",
    ends={
        Property(name="Statement125", type=statements_StatementListContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_StatementListContainer", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next113: BinaryAssociation = BinaryAssociation(
    name="next113",
    ends={
        Property(name="Reference", type=references_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="references_Reference", type=Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arraySelectors114: BinaryAssociation = BinaryAssociation(
    name="arraySelectors114",
    ends={
        Property(name="ArraySelector", type=references_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="references_Reference115", type=ArraySelector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments116: BinaryAssociation = BinaryAssociation(
    name="arguments116",
    ends={
        Property(name="Expression117", type=references_Argumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="references_Argumentable", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target118: BinaryAssociation = BinaryAssociation(
    name="target118",
    ends={
        Property(name="ReferenceableElement119", type=references_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="references_ElementReference", type=ReferenceableElement, multiplicity=Multiplicity(0, 1))
    }
)
elseStatement131: BinaryAssociation = BinaryAssociation(
    name="elseStatement131",
    ends={
        Property(name="Statement132", type=statements_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Condition", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression133: BinaryAssociation = BinaryAssociation(
    name="expression133",
    ends={
        Property(name="Expression134", type=statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init135: BinaryAssociation = BinaryAssociation(
    name="init135",
    ends={
        Property(name="ForLoopInitializer", type=statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_ForLoop", type=ForLoopInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updates136: BinaryAssociation = BinaryAssociation(
    name="updates136",
    ends={
        Property(name="Expression138", type=statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_ForLoop137", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition126: BinaryAssociation = BinaryAssociation(
    name="condition126",
    ends={
        Property(name="Expression127", type=statements_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Conditional", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
errorMessage128: BinaryAssociation = BinaryAssociation(
    name="errorMessage128",
    ends={
        Property(name="Expression129", type=statements_Assert, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Assert", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter130: BinaryAssociation = BinaryAssociation(
    name="parameter130",
    ends={
        Property(name="OrdinaryParameter", type=statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_CatchBlock", type=OrdinaryParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next139: BinaryAssociation = BinaryAssociation(
    name="next139",
    ends={
        Property(name="OrdinaryParameter140", type=statements_ForEachLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_ForEachLoop", type=OrdinaryParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection141: BinaryAssociation = BinaryAssociation(
    name="collection141",
    ends={
        Property(name="Expression143", type=statements_ForEachLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_ForEachLoop142", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target144: BinaryAssociation = BinaryAssociation(
    name="target144",
    ends={
        Property(name="JumpLabel", type=statements_Jump, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Jump", type=JumpLabel, multiplicity=Multiplicity(0, 1))
    }
)
lockProvider152: BinaryAssociation = BinaryAssociation(
    name="lockProvider152",
    ends={
        Property(name="Expression153", type=statements_SynchronizedBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_SynchronizedBlock", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throwable154: BinaryAssociation = BinaryAssociation(
    name="throwable154",
    ends={
        Property(name="Expression155", type=statements_Throw, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Throw", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catcheBlocks156: BinaryAssociation = BinaryAssociation(
    name="catcheBlocks156",
    ends={
        Property(name="CatchBlock", type=statements_TryBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_TryBlock", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyBlock157: BinaryAssociation = BinaryAssociation(
    name="finallyBlock157",
    ends={
        Property(name="Block", type=statements_TryBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_TryBlock158", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition159: BinaryAssociation = BinaryAssociation(
    name="condition159",
    ends={
        Property(name="Expression160", type=statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_WhileLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable145: BinaryAssociation = BinaryAssociation(
    name="variable145",
    ends={
        Property(name="LocalVariable", type=statements_LocalVariableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_LocalVariableStatement", type=LocalVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValue146: BinaryAssociation = BinaryAssociation(
    name="returnValue146",
    ends={
        Property(name="Expression147", type=statements_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Return", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases148: BinaryAssociation = BinaryAssociation(
    name="cases148",
    ends={
        Property(name="SwitchCase", type=statements_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Switch", type=SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable149: BinaryAssociation = BinaryAssociation(
    name="variable149",
    ends={
        Property(name="Expression151", type=statements_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="statements_Switch150", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierReferences165: BinaryAssociation = BinaryAssociation(
    name="classifierReferences165",
    ends={
        Property(name="ClassifierReference", type=types_NamespaceClassifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_NamespaceClassifierReference", type=ClassifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeReference161: BinaryAssociation = BinaryAssociation(
    name="typeReference161",
    ends={
        Property(name="TypeReference162", type=types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="types_TypedElement", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target163: BinaryAssociation = BinaryAssociation(
    name="target163",
    ends={
        Property(name="Classifier164", type=types_ClassifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_ClassifierReference", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
additionalLocalVariables166: BinaryAssociation = BinaryAssociation(
    name="additionalLocalVariables166",
    ends={
        Property(name="AdditionalLocalVariable", type=variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variables_LocalVariable", type=AdditionalLocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_annotations_AnnotationParameter_Commentable = Generalization(general=Commentable, specific=annotations_AnnotationParameter)
gen_annotations_SingleAnnotationParameter_AnnotationParameter = Generalization(general=AnnotationParameter, specific=annotations_SingleAnnotationParameter)
gen_annotations_AnnotationParameterList_AnnotationParameter = Generalization(general=AnnotationParameter, specific=annotations_AnnotationParameterList)
gen_annotations_AnnotationAttributeSetting_Commentable = Generalization(general=Commentable, specific=annotations_AnnotationAttributeSetting)
gen_annotations_AnnotationValue_Commentable = Generalization(general=Commentable, specific=annotations_AnnotationValue)
gen_annotations_AnnotationAttribute_InterfaceMethod = Generalization(general=InterfaceMethod, specific=annotations_AnnotationAttribute)
gen_annotations_Annotable_Commentable = Generalization(general=Commentable, specific=annotations_Annotable)
gen_annotations_AnnotationInstance_Reference = Generalization(general=Reference, specific=annotations_AnnotationInstance)
gen_annotations_AnnotationInstance_AnnotationInstanceOrModifier = Generalization(general=AnnotationInstanceOrModifier, specific=annotations_AnnotationInstance)
gen_annotations_AnnotationInstance_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=annotations_AnnotationInstance)
gen_arrays_ArraySelector_Commentable = Generalization(general=Commentable, specific=arrays_ArraySelector)
gen_classifiers_Classifier_Type = Generalization(general=Type, specific=classifiers_Classifier)
gen_classifiers_Classifier_ReferenceableElement = Generalization(general=ReferenceableElement, specific=classifiers_Classifier)
gen_classifiers_ConcreteClassifier_Classifier = Generalization(general=Classifier, specific=classifiers_ConcreteClassifier)
gen_classifiers_ConcreteClassifier_TypeParametrizable = Generalization(general=TypeParametrizable, specific=classifiers_ConcreteClassifier)
gen_classifiers_ConcreteClassifier_MemberContainer = Generalization(general=MemberContainer, specific=classifiers_ConcreteClassifier)
gen_classifiers_ConcreteClassifier_Member = Generalization(general=Member, specific=classifiers_ConcreteClassifier)
gen_classifiers_ConcreteClassifier_Statement = Generalization(general=Statement, specific=classifiers_ConcreteClassifier)
gen_classifiers_ConcreteClassifier_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=classifiers_ConcreteClassifier)
gen_arrays_ArrayTypeable_Commentable = Generalization(general=Commentable, specific=arrays_ArrayTypeable)
gen_arrays_ArrayDimension_Commentable = Generalization(general=Commentable, specific=arrays_ArrayDimension)
gen_arrays_ArrayInitializer_ArrayInitializationValue = Generalization(general=ArrayInitializationValue, specific=arrays_ArrayInitializer)
gen_arrays_ArrayInitializer_AnnotationValue = Generalization(general=AnnotationValue, specific=arrays_ArrayInitializer)
gen_arrays_ArrayInitializationValue_Commentable = Generalization(general=Commentable, specific=arrays_ArrayInitializationValue)
gen_arrays_ArrayInstantiationBySize_Expression = Generalization(general=Expression, specific=arrays_ArrayInstantiationBySize)
gen_arrays_ArrayInstantiationBySize_TypedElement = Generalization(general=TypedElement, specific=arrays_ArrayInstantiationBySize)
gen_arrays_ArrayInstantiationBySize_ArrayTypeable = Generalization(general=ArrayTypeable, specific=arrays_ArrayInstantiationBySize)
gen_arrays_ArrayInstantiationBySize_Reference = Generalization(general=Reference, specific=arrays_ArrayInstantiationBySize)
gen_arrays_ArrayInstantiationByValues_Expression = Generalization(general=Expression, specific=arrays_ArrayInstantiationByValues)
gen_arrays_ArrayInstantiationByValues_TypedElement = Generalization(general=TypedElement, specific=arrays_ArrayInstantiationByValues)
gen_arrays_ArrayInstantiationByValues_ArrayTypeable = Generalization(general=ArrayTypeable, specific=arrays_ArrayInstantiationByValues)
gen_arrays_ArrayInstantiationByValues_Reference = Generalization(general=Reference, specific=arrays_ArrayInstantiationByValues)
gen_classifiers_Annotation_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=classifiers_Annotation)
gen_classifiers_AnonymousClass_Type = Generalization(general=Type, specific=classifiers_AnonymousClass)
gen_classifiers_AnonymousClass_MemberContainer = Generalization(general=MemberContainer, specific=classifiers_AnonymousClass)
gen_classifiers_Implementor_Commentable = Generalization(general=Commentable, specific=classifiers_Implementor)
gen_classifiers_Class_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=classifiers_Class)
gen_classifiers_Class_Implementor = Generalization(general=Implementor, specific=classifiers_Class)
gen_classifiers_Interface_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=classifiers_Interface)
gen_classifiers_Enumeration_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=classifiers_Enumeration)
gen_classifiers_Enumeration_Implementor = Generalization(general=Implementor, specific=classifiers_Enumeration)
gen_containers_Package_JavaRoot = Generalization(general=JavaRoot, specific=containers_Package)
gen_containers_Package_Annotable = Generalization(general=Annotable, specific=containers_Package)
gen_containers_Package_ReferenceableElement = Generalization(general=ReferenceableElement, specific=containers_Package)
gen_containers_EmptyModel_JavaRoot = Generalization(general=JavaRoot, specific=containers_EmptyModel)
gen_expressions_ExpressionList_ForLoopInitializer = Generalization(general=ForLoopInitializer, specific=expressions_ExpressionList)
gen_expressions_Expression_ArrayInitializationValue = Generalization(general=ArrayInitializationValue, specific=expressions_Expression)
gen_expressions_Expression_AnnotationValue = Generalization(general=AnnotationValue, specific=expressions_Expression)
gen_commons_NamedElement_Commentable = Generalization(general=Commentable, specific=commons_NamedElement)
gen_commons_NamespaceAwareElement_Commentable = Generalization(general=Commentable, specific=commons_NamespaceAwareElement)
gen_containers_JavaRoot_NamedElement = Generalization(general=NamedElement, specific=containers_JavaRoot)
gen_containers_JavaRoot_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=containers_JavaRoot)
gen_containers_JavaRoot_ImportingElement = Generalization(general=ImportingElement, specific=containers_JavaRoot)
gen_containers_CompilationUnit_JavaRoot = Generalization(general=JavaRoot, specific=containers_CompilationUnit)
gen_expressions_ConditionalAndExpressionChild_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=expressions_ConditionalAndExpressionChild)
gen_expressions_InclusiveOrExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=expressions_InclusiveOrExpression)
gen_expressions_InclusiveOrExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=expressions_InclusiveOrExpressionChild)
gen_expressions_ExclusiveOrExpression_InclusiveOrExpressionChild = Generalization(general=InclusiveOrExpressionChild, specific=expressions_ExclusiveOrExpression)
gen_expressions_ExclusiveOrExpressionChild_InclusiveOrExpressionChild = Generalization(general=InclusiveOrExpressionChild, specific=expressions_ExclusiveOrExpressionChild)
gen_expressions_AndExpression_ExclusiveOrExpressionChild = Generalization(general=ExclusiveOrExpressionChild, specific=expressions_AndExpression)
gen_expressions_AndExpressionChild_ExclusiveOrExpressionChild = Generalization(general=ExclusiveOrExpressionChild, specific=expressions_AndExpressionChild)
gen_expressions_EqualityExpression_AndExpressionChild = Generalization(general=AndExpressionChild, specific=expressions_EqualityExpression)
gen_expressions_AssignmentExpression_Expression = Generalization(general=Expression, specific=expressions_AssignmentExpression)
gen_expressions_AssignmentExpressionChild_Expression = Generalization(general=Expression, specific=expressions_AssignmentExpressionChild)
gen_expressions_ConditionalExpression_AssignmentExpressionChild = Generalization(general=AssignmentExpressionChild, specific=expressions_ConditionalExpression)
gen_expressions_ConditionalExpressionChild_AssignmentExpressionChild = Generalization(general=AssignmentExpressionChild, specific=expressions_ConditionalExpressionChild)
gen_expressions_ConditionalOrExpression_ConditionalExpressionChild = Generalization(general=ConditionalExpressionChild, specific=expressions_ConditionalOrExpression)
gen_expressions_ConditionalOrExpressionChild_ConditionalExpressionChild = Generalization(general=ConditionalExpressionChild, specific=expressions_ConditionalOrExpressionChild)
gen_expressions_ConditionalAndExpression_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=expressions_ConditionalAndExpression)
gen_expressions_AdditiveExpressionChild_ShiftExpressionChild = Generalization(general=ShiftExpressionChild, specific=expressions_AdditiveExpressionChild)
gen_expressions_MultiplicativeExpression_AdditiveExpressionChild = Generalization(general=AdditiveExpressionChild, specific=expressions_MultiplicativeExpression)
gen_expressions_MultiplicativeExpressionChild_AdditiveExpressionChild = Generalization(general=AdditiveExpressionChild, specific=expressions_MultiplicativeExpressionChild)
gen_expressions_UnaryExpression_MultiplicativeExpressionChild = Generalization(general=MultiplicativeExpressionChild, specific=expressions_UnaryExpression)
gen_expressions_EqualityExpressionChild_AndExpressionChild = Generalization(general=AndExpressionChild, specific=expressions_EqualityExpressionChild)
gen_expressions_InstanceOfExpression_ArrayTypeable = Generalization(general=ArrayTypeable, specific=expressions_InstanceOfExpression)
gen_expressions_InstanceOfExpression_TypedElement = Generalization(general=TypedElement, specific=expressions_InstanceOfExpression)
gen_expressions_InstanceOfExpression_EqualityExpressionChild = Generalization(general=EqualityExpressionChild, specific=expressions_InstanceOfExpression)
gen_expressions_InstanceOfExpressionChild_EqualityExpressionChild = Generalization(general=EqualityExpressionChild, specific=expressions_InstanceOfExpressionChild)
gen_expressions_RelationExpression_InstanceOfExpressionChild = Generalization(general=InstanceOfExpressionChild, specific=expressions_RelationExpression)
gen_expressions_RelationExpressionChild_InstanceOfExpressionChild = Generalization(general=InstanceOfExpressionChild, specific=expressions_RelationExpressionChild)
gen_expressions_ShiftExpression_RelationExpressionChild = Generalization(general=RelationExpressionChild, specific=expressions_ShiftExpression)
gen_expressions_ShiftExpressionChild_RelationExpressionChild = Generalization(general=RelationExpressionChild, specific=expressions_ShiftExpressionChild)
gen_expressions_AdditiveExpression_ShiftExpressionChild = Generalization(general=ShiftExpressionChild, specific=expressions_AdditiveExpression)
gen_generics_CallTypeArgumentable_Commentable = Generalization(general=Commentable, specific=generics_CallTypeArgumentable)
gen_generics_TypeParametrizable_Commentable = Generalization(general=Commentable, specific=generics_TypeParametrizable)
gen_generics_ExtendsTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=generics_ExtendsTypeArgument)
gen_generics_QualifiedTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=generics_QualifiedTypeArgument)
gen_generics_QualifiedTypeArgument_TypedElement = Generalization(general=TypedElement, specific=generics_QualifiedTypeArgument)
gen_generics_SuperTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=generics_SuperTypeArgument)
gen_generics_TypeParameter_Classifier = Generalization(general=Classifier, specific=generics_TypeParameter)
gen_expressions_UnaryExpressionChild_MultiplicativeExpressionChild = Generalization(general=MultiplicativeExpressionChild, specific=expressions_UnaryExpressionChild)
gen_expressions_UnaryModificationExpression_UnaryExpressionChild = Generalization(general=UnaryExpressionChild, specific=expressions_UnaryModificationExpression)
gen_expressions_PrefixUnaryModificationExpression_UnaryModificationExpression = Generalization(general=UnaryModificationExpression, specific=expressions_PrefixUnaryModificationExpression)
gen_expressions_SuffixUnaryModificationExpression_UnaryModificationExpression = Generalization(general=UnaryModificationExpression, specific=expressions_SuffixUnaryModificationExpression)
gen_expressions_UnaryModificationExpressionChild_UnaryExpressionChild = Generalization(general=UnaryExpressionChild, specific=expressions_UnaryModificationExpressionChild)
gen_expressions_CastExpression_TypedElement = Generalization(general=TypedElement, specific=expressions_CastExpression)
gen_expressions_CastExpression_ArrayTypeable = Generalization(general=ArrayTypeable, specific=expressions_CastExpression)
gen_expressions_CastExpression_UnaryModificationExpressionChild = Generalization(general=UnaryModificationExpressionChild, specific=expressions_CastExpression)
gen_expressions_PrimaryExpression_UnaryModificationExpressionChild = Generalization(general=UnaryModificationExpressionChild, specific=expressions_PrimaryExpression)
gen_expressions_NestedExpression_Reference = Generalization(general=Reference, specific=expressions_NestedExpression)
gen_generics_TypeArgument_ArrayTypeable = Generalization(general=ArrayTypeable, specific=generics_TypeArgument)
gen_generics_TypeArgumentable_Commentable = Generalization(general=Commentable, specific=generics_TypeArgumentable)
gen_imports_StaticClassifierImport_StaticImport = Generalization(general=StaticImport, specific=imports_StaticClassifierImport)
gen_imports_StaticMemberImport_StaticImport = Generalization(general=StaticImport, specific=imports_StaticMemberImport)
gen_instantiations_Initializable_Commentable = Generalization(general=Commentable, specific=instantiations_Initializable)
gen_instantiations_Instantiation_TypedElement = Generalization(general=TypedElement, specific=instantiations_Instantiation)
gen_instantiations_Instantiation_Reference = Generalization(general=Reference, specific=instantiations_Instantiation)
gen_instantiations_Instantiation_Argumentable = Generalization(general=Argumentable, specific=instantiations_Instantiation)
gen_instantiations_Instantiation_TypeArgumentable = Generalization(general=TypeArgumentable, specific=instantiations_Instantiation)
gen_instantiations_NewConstructorCall_Instantiation = Generalization(general=Instantiation, specific=instantiations_NewConstructorCall)
gen_instantiations_NewConstructorCall_CallTypeArgumentable = Generalization(general=CallTypeArgumentable, specific=instantiations_NewConstructorCall)
gen_instantiations_ExplicitConstructorCall_Instantiation = Generalization(general=Instantiation, specific=instantiations_ExplicitConstructorCall)
gen_generics_UnknownTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=generics_UnknownTypeArgument)
gen_imports_Import_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=imports_Import)
gen_imports_ImportingElement_Commentable = Generalization(general=Commentable, specific=imports_ImportingElement)
gen_imports_StaticImport_Import = Generalization(general=Import, specific=imports_StaticImport)
gen_imports_ClassifierImport_Import = Generalization(general=Import, specific=imports_ClassifierImport)
gen_imports_PackageImport_Import = Generalization(general=Import, specific=imports_PackageImport)
gen_literals_HexIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=literals_HexIntegerLiteral)
gen_literals_OctalIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=literals_OctalIntegerLiteral)
gen_literals_LongLiteral_Literal = Generalization(general=Literal, specific=literals_LongLiteral)
gen_literals_DecimalLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=literals_DecimalLongLiteral)
gen_literals_HexLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=literals_HexLongLiteral)
gen_literals_OctalLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=literals_OctalLongLiteral)
gen_literals_NullLiteral_Literal = Generalization(general=Literal, specific=literals_NullLiteral)
gen_literals_Super_Self = Generalization(general=Self, specific=literals_Super)
gen_literals_This_Self = Generalization(general=Self, specific=literals_This)
gen_members_ExceptionThrower_Commentable = Generalization(general=Commentable, specific=members_ExceptionThrower)
gen_literals_Literal_PrimaryExpression = Generalization(general=PrimaryExpression, specific=literals_Literal)
gen_literals_Self_Commentable = Generalization(general=Commentable, specific=literals_Self)
gen_literals_BooleanLiteral_Literal = Generalization(general=Literal, specific=literals_BooleanLiteral)
gen_literals_CharacterLiteral_Literal = Generalization(general=Literal, specific=literals_CharacterLiteral)
gen_literals_FloatLiteral_Literal = Generalization(general=Literal, specific=literals_FloatLiteral)
gen_literals_DecimalFloatLiteral_FloatLiteral = Generalization(general=FloatLiteral, specific=literals_DecimalFloatLiteral)
gen_literals_HexFloatLiteral_FloatLiteral = Generalization(general=FloatLiteral, specific=literals_HexFloatLiteral)
gen_literals_DoubleLiteral_Literal = Generalization(general=Literal, specific=literals_DoubleLiteral)
gen_literals_DecimalDoubleLiteral_DoubleLiteral = Generalization(general=DoubleLiteral, specific=literals_DecimalDoubleLiteral)
gen_literals_HexDoubleLiteral_DoubleLiteral = Generalization(general=DoubleLiteral, specific=literals_HexDoubleLiteral)
gen_literals_IntegerLiteral_Literal = Generalization(general=Literal, specific=literals_IntegerLiteral)
gen_literals_DecimalIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=literals_DecimalIntegerLiteral)
gen_members_Field_Member = Generalization(general=Member, specific=members_Field)
gen_members_Field_Initializable = Generalization(general=Initializable, specific=members_Field)
gen_members_Field_Variable = Generalization(general=Variable, specific=members_Field)
gen_members_Field_ReferenceableElement = Generalization(general=ReferenceableElement, specific=members_Field)
gen_members_Field_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=members_Field)
gen_members_Method_Member = Generalization(general=Member, specific=members_Method)
gen_members_Method_TypedElement = Generalization(general=TypedElement, specific=members_Method)
gen_members_Method_ArrayTypeable = Generalization(general=ArrayTypeable, specific=members_Method)
gen_members_Method_TypeParametrizable = Generalization(general=TypeParametrizable, specific=members_Method)
gen_members_Method_Parametrizable = Generalization(general=Parametrizable, specific=members_Method)
gen_members_Method_ReferenceableElement = Generalization(general=ReferenceableElement, specific=members_Method)
gen_members_Method_ExceptionThrower = Generalization(general=ExceptionThrower, specific=members_Method)
gen_members_Method_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=members_Method)
gen_members_Member_NamedElement = Generalization(general=NamedElement, specific=members_Member)
gen_members_MemberContainer_Commentable = Generalization(general=Commentable, specific=members_MemberContainer)
gen_members_AdditionalField_ReferenceableElement = Generalization(general=ReferenceableElement, specific=members_AdditionalField)
gen_members_AdditionalField_ArrayTypeable = Generalization(general=ArrayTypeable, specific=members_AdditionalField)
gen_members_AdditionalField_Initializable = Generalization(general=Initializable, specific=members_AdditionalField)
gen_members_Constructor_Member = Generalization(general=Member, specific=members_Constructor)
gen_members_Constructor_StatementListContainer = Generalization(general=StatementListContainer, specific=members_Constructor)
gen_members_Constructor_Parametrizable = Generalization(general=Parametrizable, specific=members_Constructor)
gen_members_Constructor_TypeParametrizable = Generalization(general=TypeParametrizable, specific=members_Constructor)
gen_members_Constructor_ExceptionThrower = Generalization(general=ExceptionThrower, specific=members_Constructor)
gen_members_Constructor_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=members_Constructor)
gen_members_EmptyMember_Member = Generalization(general=Member, specific=members_EmptyMember)
gen_modifiers_Native_Modifier = Generalization(general=Modifier, specific=modifiers_Native)
gen_modifiers_Protected_Modifier = Generalization(general=Modifier, specific=modifiers_Protected)
gen_modifiers_Public_Modifier = Generalization(general=Modifier, specific=modifiers_Public)
gen_modifiers_Private_Modifier = Generalization(general=Modifier, specific=modifiers_Private)
gen_modifiers_Static_Modifier = Generalization(general=Modifier, specific=modifiers_Static)
gen_modifiers_Strictfp_Modifier = Generalization(general=Modifier, specific=modifiers_Strictfp)
gen_modifiers_Synchronized_Modifier = Generalization(general=Modifier, specific=modifiers_Synchronized)
gen_modifiers_Transient_Modifier = Generalization(general=Modifier, specific=modifiers_Transient)
gen_modifiers_Volatile_Modifier = Generalization(general=Modifier, specific=modifiers_Volatile)
gen_operators_Operator_Commentable = Generalization(general=Commentable, specific=operators_Operator)
gen_operators_AdditiveOperator_Operator = Generalization(general=Operator, specific=operators_AdditiveOperator)
gen_operators_AssignmentOperator_Operator = Generalization(general=Operator, specific=operators_AssignmentOperator)
gen_operators_EqualityOperator_Operator = Generalization(general=Operator, specific=operators_EqualityOperator)
gen_operators_MultiplicativeOperator_Operator = Generalization(general=Operator, specific=operators_MultiplicativeOperator)
gen_operators_RelationOperator_Operator = Generalization(general=Operator, specific=operators_RelationOperator)
gen_operators_ShiftOperator_Operator = Generalization(general=Operator, specific=operators_ShiftOperator)
gen_members_InterfaceMethod_Method = Generalization(general=Method_, specific=members_InterfaceMethod)
gen_members_ClassMethod_Method = Generalization(general=Method_, specific=members_ClassMethod)
gen_members_ClassMethod_StatementListContainer = Generalization(general=StatementListContainer, specific=members_ClassMethod)
gen_members_EnumConstant_ReferenceableElement = Generalization(general=ReferenceableElement, specific=members_EnumConstant)
gen_members_EnumConstant_Argumentable = Generalization(general=Argumentable, specific=members_EnumConstant)
gen_members_EnumConstant_Annotable = Generalization(general=Annotable, specific=members_EnumConstant)
gen_modifiers_Modifier_AnnotationInstanceOrModifier = Generalization(general=AnnotationInstanceOrModifier, specific=modifiers_Modifier)
gen_modifiers_AnnotationInstanceOrModifier_Commentable = Generalization(general=Commentable, specific=modifiers_AnnotationInstanceOrModifier)
gen_modifiers_AnnotableAndModifiable_Commentable = Generalization(general=Commentable, specific=modifiers_AnnotableAndModifiable)
gen_modifiers_Modifiable_Commentable = Generalization(general=Commentable, specific=modifiers_Modifiable)
gen_modifiers_Abstract_Modifier = Generalization(general=Modifier, specific=modifiers_Abstract)
gen_modifiers_Final_Modifier = Generalization(general=Modifier, specific=modifiers_Final)
gen_operators_Multiplication_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=operators_Multiplication)
gen_operators_Remainder_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=operators_Remainder)
gen_operators_Complement_UnaryOperator = Generalization(general=UnaryOperator, specific=operators_Complement)
gen_operators_MinusMinus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=operators_MinusMinus)
gen_operators_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=operators_Negate)
gen_operators_PlusPlus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=operators_PlusPlus)
gen_operators_LeftShift_ShiftOperator = Generalization(general=ShiftOperator, specific=operators_LeftShift)
gen_operators_RightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=operators_RightShift)
gen_operators_UnsignedRightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=operators_UnsignedRightShift)
gen_parameters_Parameter_Variable = Generalization(general=Variable, specific=parameters_Parameter)
gen_parameters_Parameter_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=parameters_Parameter)
gen_parameters_Parametrizable_Commentable = Generalization(general=Commentable, specific=parameters_Parametrizable)
gen_parameters_OrdinaryParameter_Parameter = Generalization(general=Parameter_, specific=parameters_OrdinaryParameter)
gen_parameters_VariableLengthParameter_Parameter = Generalization(general=Parameter_, specific=parameters_VariableLengthParameter)
gen_operators_UnaryOperator_Operator = Generalization(general=Operator, specific=operators_UnaryOperator)
gen_operators_UnaryModificationOperator_Operator = Generalization(general=Operator, specific=operators_UnaryModificationOperator)
gen_operators_Assignment_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_Assignment)
gen_operators_AssignmentAnd_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentAnd)
gen_operators_AssignmentDivision_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentDivision)
gen_operators_AssignmentExclusiveOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentExclusiveOr)
gen_operators_AssignmentMinus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentMinus)
gen_operators_AssignmentModulo_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentModulo)
gen_operators_AssignmentMultiplication_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentMultiplication)
gen_operators_AssignmentLeftShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentLeftShift)
gen_operators_AssignmentOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentOr)
gen_operators_AssignmentPlus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentPlus)
gen_operators_AssignmentRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentRightShift)
gen_operators_AssignmentUnsignedRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=operators_AssignmentUnsignedRightShift)
gen_operators_Equal_EqualityOperator = Generalization(general=EqualityOperator, specific=operators_Equal)
gen_operators_NotEqual_EqualityOperator = Generalization(general=EqualityOperator, specific=operators_NotEqual)
gen_operators_GreaterThan_RelationOperator = Generalization(general=RelationOperator, specific=operators_GreaterThan)
gen_operators_GreaterThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=operators_GreaterThanOrEqual)
gen_operators_LessThan_RelationOperator = Generalization(general=RelationOperator, specific=operators_LessThan)
gen_operators_LessThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=operators_LessThanOrEqual)
gen_operators_Addition_AdditiveOperator = Generalization(general=AdditiveOperator, specific=operators_Addition)
gen_operators_Addition_UnaryOperator = Generalization(general=UnaryOperator, specific=operators_Addition)
gen_operators_Subtraction_AdditiveOperator = Generalization(general=AdditiveOperator, specific=operators_Subtraction)
gen_operators_Subtraction_UnaryOperator = Generalization(general=UnaryOperator, specific=operators_Subtraction)
gen_operators_Division_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=operators_Division)
gen_references_PrimitiveTypeReference_Reference = Generalization(general=Reference, specific=references_PrimitiveTypeReference)
gen_references_StringReference_Reference = Generalization(general=Reference, specific=references_StringReference)
gen_references_SelfReference_Reference = Generalization(general=Reference, specific=references_SelfReference)
gen_statements_StatementContainer_Commentable = Generalization(general=Commentable, specific=statements_StatementContainer)
gen_statements_StatementListContainer_Commentable = Generalization(general=Commentable, specific=statements_StatementListContainer)
gen_references_Reference_PrimaryExpression = Generalization(general=PrimaryExpression, specific=references_Reference)
gen_references_Reference_TypeArgumentable = Generalization(general=TypeArgumentable, specific=references_Reference)
gen_references_Argumentable_Commentable = Generalization(general=Commentable, specific=references_Argumentable)
gen_references_ReferenceableElement_NamedElement = Generalization(general=NamedElement, specific=references_ReferenceableElement)
gen_references_ElementReference_Reference = Generalization(general=Reference, specific=references_ElementReference)
gen_references_IdentifierReference_ElementReference = Generalization(general=ElementReference, specific=references_IdentifierReference)
gen_references_MethodCall_ElementReference = Generalization(general=ElementReference, specific=references_MethodCall)
gen_references_MethodCall_Argumentable = Generalization(general=Argumentable, specific=references_MethodCall)
gen_references_MethodCall_CallTypeArgumentable = Generalization(general=CallTypeArgumentable, specific=references_MethodCall)
gen_references_ReflectiveClassReference_Reference = Generalization(general=Reference, specific=references_ReflectiveClassReference)
gen_statements_Continue_Jump = Generalization(general=Jump, specific=statements_Continue)
gen_statements_DefaultSwitchCase_SwitchCase = Generalization(general=SwitchCase, specific=statements_DefaultSwitchCase)
gen_statements_DoWhileLoop_WhileLoop = Generalization(general=WhileLoop, specific=statements_DoWhileLoop)
gen_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=statements_EmptyStatement)
gen_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=statements_ExpressionStatement)
gen_statements_ForLoop_Statement = Generalization(general=Statement, specific=statements_ForLoop)
gen_statements_ForLoop_StatementContainer = Generalization(general=StatementContainer, specific=statements_ForLoop)
gen_statements_ForLoop_Conditional = Generalization(general=Conditional, specific=statements_ForLoop)
gen_statements_ForEachLoop_Statement = Generalization(general=Statement, specific=statements_ForEachLoop)
gen_statements_Conditional_Commentable = Generalization(general=Commentable, specific=statements_Conditional)
gen_statements_ForLoopInitializer_Commentable = Generalization(general=Commentable, specific=statements_ForLoopInitializer)
gen_statements_Statement_Commentable = Generalization(general=Commentable, specific=statements_Statement)
gen_statements_SwitchCase_StatementListContainer = Generalization(general=StatementListContainer, specific=statements_SwitchCase)
gen_statements_Assert_Statement = Generalization(general=Statement, specific=statements_Assert)
gen_statements_Assert_Conditional = Generalization(general=Conditional, specific=statements_Assert)
gen_statements_Break_Jump = Generalization(general=Jump, specific=statements_Break)
gen_statements_Block_Member = Generalization(general=Member, specific=statements_Block)
gen_statements_Block_Statement = Generalization(general=Statement, specific=statements_Block)
gen_statements_Block_StatementListContainer = Generalization(general=StatementListContainer, specific=statements_Block)
gen_statements_Block_Modifiable = Generalization(general=Modifiable, specific=statements_Block)
gen_statements_CatchBlock_StatementListContainer = Generalization(general=StatementListContainer, specific=statements_CatchBlock)
gen_statements_Condition_Statement = Generalization(general=Statement, specific=statements_Condition)
gen_statements_Condition_StatementContainer = Generalization(general=StatementContainer, specific=statements_Condition)
gen_statements_Condition_Conditional = Generalization(general=Conditional, specific=statements_Condition)
gen_statements_LocalVariableStatement_Statement = Generalization(general=Statement, specific=statements_LocalVariableStatement)
gen_statements_ForEachLoop_StatementContainer = Generalization(general=StatementContainer, specific=statements_ForEachLoop)
gen_statements_Jump_Statement = Generalization(general=Statement, specific=statements_Jump)
gen_statements_JumpLabel_Statement = Generalization(general=Statement, specific=statements_JumpLabel)
gen_statements_JumpLabel_StatementContainer = Generalization(general=StatementContainer, specific=statements_JumpLabel)
gen_statements_JumpLabel_NamedElement = Generalization(general=NamedElement, specific=statements_JumpLabel)
gen_statements_Throw_Statement = Generalization(general=Statement, specific=statements_Throw)
gen_statements_TryBlock_Statement = Generalization(general=Statement, specific=statements_TryBlock)
gen_statements_TryBlock_StatementListContainer = Generalization(general=StatementListContainer, specific=statements_TryBlock)
gen_statements_WhileLoop_Statement = Generalization(general=Statement, specific=statements_WhileLoop)
gen_statements_WhileLoop_StatementContainer = Generalization(general=StatementContainer, specific=statements_WhileLoop)
gen_types_Type_Commentable = Generalization(general=Commentable, specific=types_Type)
gen_statements_NormalSwitchCase_SwitchCase = Generalization(general=SwitchCase, specific=statements_NormalSwitchCase)
gen_statements_NormalSwitchCase_Conditional = Generalization(general=Conditional, specific=statements_NormalSwitchCase)
gen_statements_Return_Statement = Generalization(general=Statement, specific=statements_Return)
gen_statements_Switch_Statement = Generalization(general=Statement, specific=statements_Switch)
gen_statements_SynchronizedBlock_Statement = Generalization(general=Statement, specific=statements_SynchronizedBlock)
gen_statements_SynchronizedBlock_StatementListContainer = Generalization(general=StatementListContainer, specific=statements_SynchronizedBlock)
gen_types_NamespaceClassifierReference_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=types_NamespaceClassifierReference)
gen_types_PrimitiveType_Type = Generalization(general=Type, specific=types_PrimitiveType)
gen_types_PrimitiveType_TypeReference = Generalization(general=TypeReference, specific=types_PrimitiveType)
gen_types_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Boolean)
gen_types_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Byte)
gen_types_Char_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Char)
gen_types_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Double)
gen_types_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Float)
gen_types_Int_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Int)
gen_types_Long_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Long)
gen_types_Short_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Short)
gen_types_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=types_Void)
gen_types_TypedElement_Commentable = Generalization(general=Commentable, specific=types_TypedElement)
gen_types_TypeReference_Commentable = Generalization(general=Commentable, specific=types_TypeReference)
gen_types_ClassifierReference_TypeReference = Generalization(general=TypeReference, specific=types_ClassifierReference)
gen_types_ClassifierReference_TypeArgumentable = Generalization(general=TypeArgumentable, specific=types_ClassifierReference)
gen_types_NamespaceClassifierReference_TypeReference = Generalization(general=TypeReference, specific=types_NamespaceClassifierReference)
gen_variables_Variable_NamedElement = Generalization(general=NamedElement, specific=variables_Variable)
gen_variables_Variable_TypedElement = Generalization(general=TypedElement, specific=variables_Variable)
gen_variables_Variable_ArrayTypeable = Generalization(general=ArrayTypeable, specific=variables_Variable)
gen_variables_Variable_ReferenceableElement = Generalization(general=ReferenceableElement, specific=variables_Variable)
gen_variables_Variable_TypeArgumentable = Generalization(general=TypeArgumentable, specific=variables_Variable)
gen_variables_LocalVariable_Variable = Generalization(general=Variable, specific=variables_LocalVariable)
gen_variables_LocalVariable_Initializable = Generalization(general=Initializable, specific=variables_LocalVariable)
gen_variables_LocalVariable_ForLoopInitializer = Generalization(general=ForLoopInitializer, specific=variables_LocalVariable)
gen_variables_LocalVariable_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=variables_LocalVariable)
gen_variables_AdditionalLocalVariable_ReferenceableElement = Generalization(general=ReferenceableElement, specific=variables_AdditionalLocalVariable)
gen_variables_AdditionalLocalVariable_ArrayTypeable = Generalization(general=ArrayTypeable, specific=variables_AdditionalLocalVariable)
gen_variables_AdditionalLocalVariable_Initializable = Generalization(general=Initializable, specific=variables_AdditionalLocalVariable)

# Domain Model
domain_model = DomainModel(
    name="variables",
    types={AnnotationParameter, annotations_AnnotationParameter, annotations_SingleAnnotationParameter, AnnotationValue, annotations_AnnotationParameterList, AnnotationAttributeSetting, annotations_AnnotationAttributeSetting, InterfaceMethod, annotations_AnnotationValue, annotations_AnnotationAttribute, annotations_Annotable, Commentable, AnnotationInstance, annotations_AnnotationInstance, Reference, AnnotationInstanceOrModifier, NamespaceAwareElement, Classifier, ArrayInitializer, arrays_ArraySelector, classifiers_Classifier, Type, ReferenceableElement, classifiers_ConcreteClassifier, TypeParametrizable, MemberContainer, Member, Statement, AnnotableAndModifiable, classifiers_Implementor, Expression, arrays_ArrayTypeable, ArrayDimension, arrays_ArrayDimension, arrays_ArrayInitializer, ArrayInitializationValue, arrays_ArrayInitializationValue, arrays_ArrayInstantiationBySize, TypedElement, ArrayTypeable, arrays_ArrayInstantiationByValues, EnumConstant, classifiers_Annotation, classifiers_AnonymousClass, commons_Commentable, TypeReference, classifiers_Class, ConcreteClassifier, Implementor, classifiers_Interface, classifiers_Enumeration, containers_Package, Annotable, CompilationUnit, Package, containers_EmptyModel, expressions_ExpressionList, ForLoopInitializer, expressions_Expression, commons_NamedElement, commons_NamespaceAwareElement, containers_JavaRoot, NamedElement, ImportingElement, containers_CompilationUnit, JavaRoot, ConditionalAndExpressionChild, expressions_ConditionalAndExpressionChild, expressions_InclusiveOrExpression, InclusiveOrExpressionChild, expressions_InclusiveOrExpressionChild, expressions_ExclusiveOrExpression, ExclusiveOrExpressionChild, expressions_ExclusiveOrExpressionChild, expressions_AndExpression, AndExpressionChild, expressions_AndExpressionChild, expressions_EqualityExpression, EqualityOperator, expressions_AssignmentExpression, AssignmentExpressionChild, AssignmentOperator, expressions_AssignmentExpressionChild, expressions_ConditionalExpression, ConditionalExpressionChild, expressions_ConditionalExpressionChild, expressions_ConditionalOrExpression, ConditionalOrExpressionChild, expressions_ConditionalOrExpressionChild, expressions_ConditionalAndExpression, AdditiveExpressionChild, AdditiveOperator, expressions_AdditiveExpressionChild, expressions_MultiplicativeExpression, MultiplicativeExpressionChild, MultiplicativeOperator, expressions_MultiplicativeExpressionChild, expressions_UnaryExpression, UnaryOperator, UnaryExpressionChild, EqualityExpressionChild, expressions_EqualityExpressionChild, expressions_InstanceOfExpression, InstanceOfExpressionChild, expressions_InstanceOfExpressionChild, expressions_RelationExpression, RelationExpressionChild, RelationOperator, expressions_RelationExpressionChild, expressions_ShiftExpression, ShiftExpressionChild, ShiftOperator, expressions_ShiftExpressionChild, expressions_AdditiveExpression, generics_CallTypeArgumentable, generics_TypeParametrizable, TypeParameter, generics_ExtendsTypeArgument, generics_QualifiedTypeArgument, generics_SuperTypeArgument, generics_TypeParameter, expressions_UnaryExpressionChild, expressions_UnaryModificationExpression, UnaryModificationExpressionChild, UnaryModificationOperator, expressions_PrefixUnaryModificationExpression, UnaryModificationExpression, expressions_SuffixUnaryModificationExpression, expressions_UnaryModificationExpressionChild, expressions_CastExpression, expressions_PrimaryExpression, expressions_NestedExpression, generics_TypeArgument, generics_TypeArgumentable, TypeArgument, imports_StaticClassifierImport, StaticImport, imports_StaticMemberImport, instantiations_Initializable, instantiations_Instantiation, Argumentable, TypeArgumentable, instantiations_NewConstructorCall, Instantiation, CallTypeArgumentable, AnonymousClass, instantiations_ExplicitConstructorCall, Self, generics_UnknownTypeArgument, imports_Import, imports_ImportingElement, Import, imports_StaticImport, Static, imports_ClassifierImport, imports_PackageImport, literals_OctalIntegerLiteral, literals_LongLiteral, literals_DecimalLongLiteral, LongLiteral, literals_HexLongLiteral, literals_OctalLongLiteral, literals_NullLiteral, literals_Super, literals_This, members_ExceptionThrower, NamespaceClassifierReference, literals_Literal, PrimaryExpression, literals_Self, literals_BooleanLiteral, Literal, literals_CharacterLiteral, literals_FloatLiteral, literals_DecimalFloatLiteral, FloatLiteral, literals_HexFloatLiteral, literals_DoubleLiteral, literals_DecimalDoubleLiteral, DoubleLiteral, literals_HexDoubleLiteral, literals_IntegerLiteral, literals_DecimalIntegerLiteral, IntegerLiteral, literals_HexIntegerLiteral, members_Field, Variable, AdditionalField, members_Method, members_Member, members_MemberContainer, members_AdditionalField, Initializable, members_Constructor, StatementListContainer, Parametrizable, ExceptionThrower, members_EmptyMember, modifiers_Native, modifiers_Protected, modifiers_Public, modifiers_Private, modifiers_Static, modifiers_Strictfp, modifiers_Synchronized, modifiers_Transient, modifiers_Volatile, operators_Operator, operators_AdditiveOperator, Operator, operators_AssignmentOperator, operators_EqualityOperator, operators_MultiplicativeOperator, operators_RelationOperator, operators_ShiftOperator, members_InterfaceMethod, Method_, members_ClassMethod, members_EnumConstant, modifiers_Modifier, modifiers_AnnotationInstanceOrModifier, modifiers_AnnotableAndModifiable, modifiers_Modifiable, Modifier, modifiers_Abstract, modifiers_Final, operators_Multiplication, operators_Remainder, operators_Complement, operators_MinusMinus, operators_Negate, operators_PlusPlus, operators_LeftShift, operators_RightShift, operators_UnsignedRightShift, parameters_Parameter, parameters_Parametrizable, Parameter_, parameters_OrdinaryParameter, parameters_VariableLengthParameter, operators_UnaryOperator, operators_UnaryModificationOperator, operators_Assignment, operators_AssignmentAnd, operators_AssignmentDivision, operators_AssignmentExclusiveOr, operators_AssignmentMinus, operators_AssignmentModulo, operators_AssignmentMultiplication, operators_AssignmentLeftShift, operators_AssignmentOr, operators_AssignmentPlus, operators_AssignmentRightShift, operators_AssignmentUnsignedRightShift, operators_Equal, operators_NotEqual, operators_GreaterThan, operators_GreaterThanOrEqual, operators_LessThan, operators_LessThanOrEqual, operators_Addition, operators_Subtraction, operators_Division, references_PrimitiveTypeReference, PrimitiveType, references_StringReference, references_SelfReference, statements_StatementContainer, statements_StatementListContainer, references_Reference, ArraySelector, references_Argumentable, references_ReferenceableElement, references_ElementReference, references_IdentifierReference, ElementReference, references_MethodCall, references_ReflectiveClassReference, statements_Continue, statements_DefaultSwitchCase, SwitchCase, statements_DoWhileLoop, WhileLoop, statements_EmptyStatement, statements_ExpressionStatement, statements_ForLoop, statements_ForEachLoop, statements_Conditional, statements_ForLoopInitializer, statements_Statement, statements_SwitchCase, statements_Assert, Conditional, statements_Break, Jump, statements_Block, Modifiable, statements_CatchBlock, OrdinaryParameter, statements_Condition, StatementContainer, statements_LocalVariableStatement, statements_Jump, JumpLabel, statements_JumpLabel, statements_Throw, statements_TryBlock, CatchBlock, Block, statements_WhileLoop, types_Type, LocalVariable, statements_NormalSwitchCase, statements_Return, statements_Switch, statements_SynchronizedBlock, ClassifierReference, types_PrimitiveType, types_Boolean, types_Byte, types_Char, types_Double, types_Float, types_Int, types_Long, types_Short, types_Void, types_TypedElement, types_TypeReference, types_ClassifierReference, types_NamespaceClassifierReference, variables_Variable, variables_LocalVariable, AdditionalLocalVariable, variables_AdditionalLocalVariable},
    associations={parameter2, value4, settings5, attribute6, value7, annotations0, annotation1, arrayInitializer18, position19, defaultValue10, arrayDimensionsBefore11, arrayDimensionsAfter12, initialValues15, sizes16, constants32, implements21, extends22, defaultExtends24, extends27, defaultExtends29, classifiers33, compilationUnits34, subpackages35, expressions37, children53, children54, children55, children56, equalityOperators57, child39, assignmentOperator40, value42, child45, expressionIf46, expressionElse49, children52, children67, additiveOperators68, children70, multiplicativeOperators71, operators73, child74, children58, child60, children61, relationOperators62, children64, shiftOperators65, callTypeArguments84, typeParameters86, extendTypes87, superType89, child76, operator77, child79, expression81, typeArguments83, staticMembers97, initialValue98, anonymousClass100, callTarget101, extendTypes91, imports93, static94, classifier95, exceptions102, additionalFields107, members103, defaultMembers104, anonymousClass108, annotationsAndModifiers110, modifiers111, parameters112, primitiveType120, self121, statement123, statements124, next113, arraySelectors114, arguments116, target118, elseStatement131, expression133, init135, updates136, condition126, errorMessage128, parameter130, next139, collection141, target144, lockProvider152, throwable154, catcheBlocks156, finallyBlock157, condition159, variable145, returnValue146, cases148, variable149, classifierReferences165, typeReference161, target163, additionalLocalVariables166},
    generalizations={gen_annotations_AnnotationParameter_Commentable, gen_annotations_SingleAnnotationParameter_AnnotationParameter, gen_annotations_AnnotationParameterList_AnnotationParameter, gen_annotations_AnnotationAttributeSetting_Commentable, gen_annotations_AnnotationValue_Commentable, gen_annotations_AnnotationAttribute_InterfaceMethod, gen_annotations_Annotable_Commentable, gen_annotations_AnnotationInstance_Reference, gen_annotations_AnnotationInstance_AnnotationInstanceOrModifier, gen_annotations_AnnotationInstance_NamespaceAwareElement, gen_arrays_ArraySelector_Commentable, gen_classifiers_Classifier_Type, gen_classifiers_Classifier_ReferenceableElement, gen_classifiers_ConcreteClassifier_Classifier, gen_classifiers_ConcreteClassifier_TypeParametrizable, gen_classifiers_ConcreteClassifier_MemberContainer, gen_classifiers_ConcreteClassifier_Member, gen_classifiers_ConcreteClassifier_Statement, gen_classifiers_ConcreteClassifier_AnnotableAndModifiable, gen_arrays_ArrayTypeable_Commentable, gen_arrays_ArrayDimension_Commentable, gen_arrays_ArrayInitializer_ArrayInitializationValue, gen_arrays_ArrayInitializer_AnnotationValue, gen_arrays_ArrayInitializationValue_Commentable, gen_arrays_ArrayInstantiationBySize_Expression, gen_arrays_ArrayInstantiationBySize_TypedElement, gen_arrays_ArrayInstantiationBySize_ArrayTypeable, gen_arrays_ArrayInstantiationBySize_Reference, gen_arrays_ArrayInstantiationByValues_Expression, gen_arrays_ArrayInstantiationByValues_TypedElement, gen_arrays_ArrayInstantiationByValues_ArrayTypeable, gen_arrays_ArrayInstantiationByValues_Reference, gen_classifiers_Annotation_ConcreteClassifier, gen_classifiers_AnonymousClass_Type, gen_classifiers_AnonymousClass_MemberContainer, gen_classifiers_Implementor_Commentable, gen_classifiers_Class_ConcreteClassifier, gen_classifiers_Class_Implementor, gen_classifiers_Interface_ConcreteClassifier, gen_classifiers_Enumeration_ConcreteClassifier, gen_classifiers_Enumeration_Implementor, gen_containers_Package_JavaRoot, gen_containers_Package_Annotable, gen_containers_Package_ReferenceableElement, gen_containers_EmptyModel_JavaRoot, gen_expressions_ExpressionList_ForLoopInitializer, gen_expressions_Expression_ArrayInitializationValue, gen_expressions_Expression_AnnotationValue, gen_commons_NamedElement_Commentable, gen_commons_NamespaceAwareElement_Commentable, gen_containers_JavaRoot_NamedElement, gen_containers_JavaRoot_NamespaceAwareElement, gen_containers_JavaRoot_ImportingElement, gen_containers_CompilationUnit_JavaRoot, gen_expressions_ConditionalAndExpressionChild_ConditionalOrExpressionChild, gen_expressions_InclusiveOrExpression_ConditionalAndExpressionChild, gen_expressions_InclusiveOrExpressionChild_ConditionalAndExpressionChild, gen_expressions_ExclusiveOrExpression_InclusiveOrExpressionChild, gen_expressions_ExclusiveOrExpressionChild_InclusiveOrExpressionChild, gen_expressions_AndExpression_ExclusiveOrExpressionChild, gen_expressions_AndExpressionChild_ExclusiveOrExpressionChild, gen_expressions_EqualityExpression_AndExpressionChild, gen_expressions_AssignmentExpression_Expression, gen_expressions_AssignmentExpressionChild_Expression, gen_expressions_ConditionalExpression_AssignmentExpressionChild, gen_expressions_ConditionalExpressionChild_AssignmentExpressionChild, gen_expressions_ConditionalOrExpression_ConditionalExpressionChild, gen_expressions_ConditionalOrExpressionChild_ConditionalExpressionChild, gen_expressions_ConditionalAndExpression_ConditionalOrExpressionChild, gen_expressions_AdditiveExpressionChild_ShiftExpressionChild, gen_expressions_MultiplicativeExpression_AdditiveExpressionChild, gen_expressions_MultiplicativeExpressionChild_AdditiveExpressionChild, gen_expressions_UnaryExpression_MultiplicativeExpressionChild, gen_expressions_EqualityExpressionChild_AndExpressionChild, gen_expressions_InstanceOfExpression_ArrayTypeable, gen_expressions_InstanceOfExpression_TypedElement, gen_expressions_InstanceOfExpression_EqualityExpressionChild, gen_expressions_InstanceOfExpressionChild_EqualityExpressionChild, gen_expressions_RelationExpression_InstanceOfExpressionChild, gen_expressions_RelationExpressionChild_InstanceOfExpressionChild, gen_expressions_ShiftExpression_RelationExpressionChild, gen_expressions_ShiftExpressionChild_RelationExpressionChild, gen_expressions_AdditiveExpression_ShiftExpressionChild, gen_generics_CallTypeArgumentable_Commentable, gen_generics_TypeParametrizable_Commentable, gen_generics_ExtendsTypeArgument_TypeArgument, gen_generics_QualifiedTypeArgument_TypeArgument, gen_generics_QualifiedTypeArgument_TypedElement, gen_generics_SuperTypeArgument_TypeArgument, gen_generics_TypeParameter_Classifier, gen_expressions_UnaryExpressionChild_MultiplicativeExpressionChild, gen_expressions_UnaryModificationExpression_UnaryExpressionChild, gen_expressions_PrefixUnaryModificationExpression_UnaryModificationExpression, gen_expressions_SuffixUnaryModificationExpression_UnaryModificationExpression, gen_expressions_UnaryModificationExpressionChild_UnaryExpressionChild, gen_expressions_CastExpression_TypedElement, gen_expressions_CastExpression_ArrayTypeable, gen_expressions_CastExpression_UnaryModificationExpressionChild, gen_expressions_PrimaryExpression_UnaryModificationExpressionChild, gen_expressions_NestedExpression_Reference, gen_generics_TypeArgument_ArrayTypeable, gen_generics_TypeArgumentable_Commentable, gen_imports_StaticClassifierImport_StaticImport, gen_imports_StaticMemberImport_StaticImport, gen_instantiations_Initializable_Commentable, gen_instantiations_Instantiation_TypedElement, gen_instantiations_Instantiation_Reference, gen_instantiations_Instantiation_Argumentable, gen_instantiations_Instantiation_TypeArgumentable, gen_instantiations_NewConstructorCall_Instantiation, gen_instantiations_NewConstructorCall_CallTypeArgumentable, gen_instantiations_ExplicitConstructorCall_Instantiation, gen_generics_UnknownTypeArgument_TypeArgument, gen_imports_Import_NamespaceAwareElement, gen_imports_ImportingElement_Commentable, gen_imports_StaticImport_Import, gen_imports_ClassifierImport_Import, gen_imports_PackageImport_Import, gen_literals_HexIntegerLiteral_IntegerLiteral, gen_literals_OctalIntegerLiteral_IntegerLiteral, gen_literals_LongLiteral_Literal, gen_literals_DecimalLongLiteral_LongLiteral, gen_literals_HexLongLiteral_LongLiteral, gen_literals_OctalLongLiteral_LongLiteral, gen_literals_NullLiteral_Literal, gen_literals_Super_Self, gen_literals_This_Self, gen_members_ExceptionThrower_Commentable, gen_literals_Literal_PrimaryExpression, gen_literals_Self_Commentable, gen_literals_BooleanLiteral_Literal, gen_literals_CharacterLiteral_Literal, gen_literals_FloatLiteral_Literal, gen_literals_DecimalFloatLiteral_FloatLiteral, gen_literals_HexFloatLiteral_FloatLiteral, gen_literals_DoubleLiteral_Literal, gen_literals_DecimalDoubleLiteral_DoubleLiteral, gen_literals_HexDoubleLiteral_DoubleLiteral, gen_literals_IntegerLiteral_Literal, gen_literals_DecimalIntegerLiteral_IntegerLiteral, gen_members_Field_Member, gen_members_Field_Initializable, gen_members_Field_Variable, gen_members_Field_ReferenceableElement, gen_members_Field_AnnotableAndModifiable, gen_members_Method_Member, gen_members_Method_TypedElement, gen_members_Method_ArrayTypeable, gen_members_Method_TypeParametrizable, gen_members_Method_Parametrizable, gen_members_Method_ReferenceableElement, gen_members_Method_ExceptionThrower, gen_members_Method_AnnotableAndModifiable, gen_members_Member_NamedElement, gen_members_MemberContainer_Commentable, gen_members_AdditionalField_ReferenceableElement, gen_members_AdditionalField_ArrayTypeable, gen_members_AdditionalField_Initializable, gen_members_Constructor_Member, gen_members_Constructor_StatementListContainer, gen_members_Constructor_Parametrizable, gen_members_Constructor_TypeParametrizable, gen_members_Constructor_ExceptionThrower, gen_members_Constructor_AnnotableAndModifiable, gen_members_EmptyMember_Member, gen_modifiers_Native_Modifier, gen_modifiers_Protected_Modifier, gen_modifiers_Public_Modifier, gen_modifiers_Private_Modifier, gen_modifiers_Static_Modifier, gen_modifiers_Strictfp_Modifier, gen_modifiers_Synchronized_Modifier, gen_modifiers_Transient_Modifier, gen_modifiers_Volatile_Modifier, gen_operators_Operator_Commentable, gen_operators_AdditiveOperator_Operator, gen_operators_AssignmentOperator_Operator, gen_operators_EqualityOperator_Operator, gen_operators_MultiplicativeOperator_Operator, gen_operators_RelationOperator_Operator, gen_operators_ShiftOperator_Operator, gen_members_InterfaceMethod_Method, gen_members_ClassMethod_Method, gen_members_ClassMethod_StatementListContainer, gen_members_EnumConstant_ReferenceableElement, gen_members_EnumConstant_Argumentable, gen_members_EnumConstant_Annotable, gen_modifiers_Modifier_AnnotationInstanceOrModifier, gen_modifiers_AnnotationInstanceOrModifier_Commentable, gen_modifiers_AnnotableAndModifiable_Commentable, gen_modifiers_Modifiable_Commentable, gen_modifiers_Abstract_Modifier, gen_modifiers_Final_Modifier, gen_operators_Multiplication_MultiplicativeOperator, gen_operators_Remainder_MultiplicativeOperator, gen_operators_Complement_UnaryOperator, gen_operators_MinusMinus_UnaryModificationOperator, gen_operators_Negate_UnaryOperator, gen_operators_PlusPlus_UnaryModificationOperator, gen_operators_LeftShift_ShiftOperator, gen_operators_RightShift_ShiftOperator, gen_operators_UnsignedRightShift_ShiftOperator, gen_parameters_Parameter_Variable, gen_parameters_Parameter_AnnotableAndModifiable, gen_parameters_Parametrizable_Commentable, gen_parameters_OrdinaryParameter_Parameter, gen_parameters_VariableLengthParameter_Parameter, gen_operators_UnaryOperator_Operator, gen_operators_UnaryModificationOperator_Operator, gen_operators_Assignment_AssignmentOperator, gen_operators_AssignmentAnd_AssignmentOperator, gen_operators_AssignmentDivision_AssignmentOperator, gen_operators_AssignmentExclusiveOr_AssignmentOperator, gen_operators_AssignmentMinus_AssignmentOperator, gen_operators_AssignmentModulo_AssignmentOperator, gen_operators_AssignmentMultiplication_AssignmentOperator, gen_operators_AssignmentLeftShift_AssignmentOperator, gen_operators_AssignmentOr_AssignmentOperator, gen_operators_AssignmentPlus_AssignmentOperator, gen_operators_AssignmentRightShift_AssignmentOperator, gen_operators_AssignmentUnsignedRightShift_AssignmentOperator, gen_operators_Equal_EqualityOperator, gen_operators_NotEqual_EqualityOperator, gen_operators_GreaterThan_RelationOperator, gen_operators_GreaterThanOrEqual_RelationOperator, gen_operators_LessThan_RelationOperator, gen_operators_LessThanOrEqual_RelationOperator, gen_operators_Addition_AdditiveOperator, gen_operators_Addition_UnaryOperator, gen_operators_Subtraction_AdditiveOperator, gen_operators_Subtraction_UnaryOperator, gen_operators_Division_MultiplicativeOperator, gen_references_PrimitiveTypeReference_Reference, gen_references_StringReference_Reference, gen_references_SelfReference_Reference, gen_statements_StatementContainer_Commentable, gen_statements_StatementListContainer_Commentable, gen_references_Reference_PrimaryExpression, gen_references_Reference_TypeArgumentable, gen_references_Argumentable_Commentable, gen_references_ReferenceableElement_NamedElement, gen_references_ElementReference_Reference, gen_references_IdentifierReference_ElementReference, gen_references_MethodCall_ElementReference, gen_references_MethodCall_Argumentable, gen_references_MethodCall_CallTypeArgumentable, gen_references_ReflectiveClassReference_Reference, gen_statements_Continue_Jump, gen_statements_DefaultSwitchCase_SwitchCase, gen_statements_DoWhileLoop_WhileLoop, gen_statements_EmptyStatement_Statement, gen_statements_ExpressionStatement_Statement, gen_statements_ForLoop_Statement, gen_statements_ForLoop_StatementContainer, gen_statements_ForLoop_Conditional, gen_statements_ForEachLoop_Statement, gen_statements_Conditional_Commentable, gen_statements_ForLoopInitializer_Commentable, gen_statements_Statement_Commentable, gen_statements_SwitchCase_StatementListContainer, gen_statements_Assert_Statement, gen_statements_Assert_Conditional, gen_statements_Break_Jump, gen_statements_Block_Member, gen_statements_Block_Statement, gen_statements_Block_StatementListContainer, gen_statements_Block_Modifiable, gen_statements_CatchBlock_StatementListContainer, gen_statements_Condition_Statement, gen_statements_Condition_StatementContainer, gen_statements_Condition_Conditional, gen_statements_LocalVariableStatement_Statement, gen_statements_ForEachLoop_StatementContainer, gen_statements_Jump_Statement, gen_statements_JumpLabel_Statement, gen_statements_JumpLabel_StatementContainer, gen_statements_JumpLabel_NamedElement, gen_statements_Throw_Statement, gen_statements_TryBlock_Statement, gen_statements_TryBlock_StatementListContainer, gen_statements_WhileLoop_Statement, gen_statements_WhileLoop_StatementContainer, gen_types_Type_Commentable, gen_statements_NormalSwitchCase_SwitchCase, gen_statements_NormalSwitchCase_Conditional, gen_statements_Return_Statement, gen_statements_Switch_Statement, gen_statements_SynchronizedBlock_Statement, gen_statements_SynchronizedBlock_StatementListContainer, gen_types_NamespaceClassifierReference_NamespaceAwareElement, gen_types_PrimitiveType_Type, gen_types_PrimitiveType_TypeReference, gen_types_Boolean_PrimitiveType, gen_types_Byte_PrimitiveType, gen_types_Char_PrimitiveType, gen_types_Double_PrimitiveType, gen_types_Float_PrimitiveType, gen_types_Int_PrimitiveType, gen_types_Long_PrimitiveType, gen_types_Short_PrimitiveType, gen_types_Void_PrimitiveType, gen_types_TypedElement_Commentable, gen_types_TypeReference_Commentable, gen_types_ClassifierReference_TypeReference, gen_types_ClassifierReference_TypeArgumentable, gen_types_NamespaceClassifierReference_TypeReference, gen_variables_Variable_NamedElement, gen_variables_Variable_TypedElement, gen_variables_Variable_ArrayTypeable, gen_variables_Variable_ReferenceableElement, gen_variables_Variable_TypeArgumentable, gen_variables_LocalVariable_Variable, gen_variables_LocalVariable_Initializable, gen_variables_LocalVariable_ForLoopInitializer, gen_variables_LocalVariable_AnnotableAndModifiable, gen_variables_AdditionalLocalVariable_ReferenceableElement, gen_variables_AdditionalLocalVariable_ArrayTypeable, gen_variables_AdditionalLocalVariable_Initializable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)