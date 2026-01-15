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
java_Annotable = Class(name="java::Annotable", is_abstract=True)
Commentable = Class(name="Commentable")
java_AnnotationInstance = Class(name="java::AnnotationInstance")
Reference = Class(name="Reference")
AnnotationInstanceOrModifier = Class(name="AnnotationInstanceOrModifier")
NamespaceAwareElement = Class(name="NamespaceAwareElement")
java_Classifier = Class(name="java::Classifier", is_abstract=True)
java_AnnotationParameter = Class(name="java::AnnotationParameter", is_abstract=True)
java_AnnotationAttribute = Class(name="java::AnnotationAttribute")
InterfaceMethod = Class(name="InterfaceMethod")
java_Expression = Class(name="java::Expression", is_abstract=True)
java_ArrayTypeable = Class(name="java::ArrayTypeable", is_abstract=True)
java_ArrayDimension = Class(name="java::ArrayDimension")
java_ArrayInitializer = Class(name="java::ArrayInitializer")
ArrayInitializationValue = Class(name="ArrayInitializationValue")
AnnotationValue = Class(name="AnnotationValue")
java_ArrayInitializationValue = Class(name="java::ArrayInitializationValue", is_abstract=True)
java_SingleAnnotationParameter = Class(name="java::SingleAnnotationParameter")
AnnotationParameter = Class(name="AnnotationParameter")
java_AnnotationValue = Class(name="java::AnnotationValue", is_abstract=True)
java_AnnotationParameterList = Class(name="java::AnnotationParameterList")
java_AnnotationAttributeSetting = Class(name="java::AnnotationAttributeSetting")
java_InterfaceMethod = Class(name="java::InterfaceMethod")
java_ArrayInstantiationByValuesTyped = Class(name="java::ArrayInstantiationByValuesTyped")
java_ArraySelector = Class(name="java::ArraySelector")
Type = Class(name="Type")
ReferenceableElement = Class(name="ReferenceableElement")
java_ConcreteClassifier = Class(name="java::ConcreteClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
TypeParametrizable = Class(name="TypeParametrizable")
MemberContainer = Class(name="MemberContainer")
Member = Class(name="Member")
Statement = Class(name="Statement")
AnnotableAndModifiable = Class(name="AnnotableAndModifiable")
java_ArrayInstantiation = Class(name="java::ArrayInstantiation", is_abstract=True)
Expression = Class(name="Expression")
java_ArrayInstantiationBySize = Class(name="java::ArrayInstantiationBySize")
ArrayInstantiation = Class(name="ArrayInstantiation")
TypedElement = Class(name="TypedElement")
ArrayTypeable = Class(name="ArrayTypeable")
java_ArrayInstantiationByValues = Class(name="java::ArrayInstantiationByValues", is_abstract=True)
java_ArrayInstantiationByValuesUntyped = Class(name="java::ArrayInstantiationByValuesUntyped")
ArrayInstantiationByValues = Class(name="ArrayInstantiationByValues")
java_Interface = Class(name="java::Interface")
java_Implementor = Class(name="java::Implementor", is_abstract=True)
java_TypeReference = Class(name="java::TypeReference", is_abstract=True)
java_Class = Class(name="java::Class")
ConcreteClassifier = Class(name="ConcreteClassifier")
Implementor = Class(name="Implementor")
java_Enumeration = Class(name="java::Enumeration")
java_EnumConstant = Class(name="java::EnumConstant")
java_Annotation = Class(name="java::Annotation")
java_Commentable = Class(name="java::Commentable", is_abstract=True)
java_AnonymousClass = Class(name="java::AnonymousClass")
java_JavaRoot = Class(name="java::JavaRoot", is_abstract=True)
NamedElement = Class(name="NamedElement")
ImportingElement = Class(name="ImportingElement")
java_LayoutInformation = Class(name="java::LayoutInformation")
java_NamedElement = Class(name="java::NamedElement", is_abstract=True)
java_NamespaceAwareElement = Class(name="java::NamespaceAwareElement", is_abstract=True)
java_Package = Class(name="java::Package")
Annotable = Class(name="Annotable")
java_CompilationUnit = Class(name="java::CompilationUnit")
JavaRoot = Class(name="JavaRoot")
java_EmptyModel = Class(name="java::EmptyModel")
java_ExpressionList = Class(name="java::ExpressionList")
ForLoopInitializer = Class(name="ForLoopInitializer")
java_ConditionalExpression = Class(name="java::ConditionalExpression")
AssignmentExpressionChild = Class(name="AssignmentExpressionChild")
java_ConditionalExpressionChild = Class(name="java::ConditionalExpressionChild", is_abstract=True)
java_AssignmentExpression = Class(name="java::AssignmentExpression")
java_AssignmentExpressionChild = Class(name="java::AssignmentExpressionChild", is_abstract=True)
java_AssignmentOperator = Class(name="java::AssignmentOperator", is_abstract=True)
java_InclusiveOrExpression = Class(name="java::InclusiveOrExpression")
ConditionalAndExpressionChild = Class(name="ConditionalAndExpressionChild")
java_InclusiveOrExpressionChild = Class(name="java::InclusiveOrExpressionChild", is_abstract=True)
java_ExclusiveOrExpression = Class(name="java::ExclusiveOrExpression")
InclusiveOrExpressionChild = Class(name="InclusiveOrExpressionChild")
java_ExclusiveOrExpressionChild = Class(name="java::ExclusiveOrExpressionChild", is_abstract=True)
java_ConditionalOrExpression = Class(name="java::ConditionalOrExpression")
ConditionalExpressionChild = Class(name="ConditionalExpressionChild")
java_ConditionalOrExpressionChild = Class(name="java::ConditionalOrExpressionChild", is_abstract=True)
java_ConditionalAndExpression = Class(name="java::ConditionalAndExpression")
ConditionalOrExpressionChild = Class(name="ConditionalOrExpressionChild")
java_ConditionalAndExpressionChild = Class(name="java::ConditionalAndExpressionChild", is_abstract=True)
java_EqualityExpressionChild = Class(name="java::EqualityExpressionChild", is_abstract=True)
java_InstanceOfExpression = Class(name="java::InstanceOfExpression")
EqualityExpressionChild = Class(name="EqualityExpressionChild")
java_InstanceOfExpressionChild = Class(name="java::InstanceOfExpressionChild", is_abstract=True)
java_AndExpression = Class(name="java::AndExpression")
ExclusiveOrExpressionChild = Class(name="ExclusiveOrExpressionChild")
java_AndExpressionChild = Class(name="java::AndExpressionChild", is_abstract=True)
java_EqualityExpression = Class(name="java::EqualityExpression")
AndExpressionChild = Class(name="AndExpressionChild")
java_EqualityOperator = Class(name="java::EqualityOperator", is_abstract=True)
java_ShiftOperator = Class(name="java::ShiftOperator", is_abstract=True)
java_AdditiveExpression = Class(name="java::AdditiveExpression")
ShiftExpressionChild = Class(name="ShiftExpressionChild")
java_AdditiveExpressionChild = Class(name="java::AdditiveExpressionChild", is_abstract=True)
java_AdditiveOperator = Class(name="java::AdditiveOperator", is_abstract=True)
java_RelationExpression = Class(name="java::RelationExpression")
InstanceOfExpressionChild = Class(name="InstanceOfExpressionChild")
java_RelationExpressionChild = Class(name="java::RelationExpressionChild", is_abstract=True)
java_RelationOperator = Class(name="java::RelationOperator", is_abstract=True)
java_ShiftExpression = Class(name="java::ShiftExpression")
RelationExpressionChild = Class(name="RelationExpressionChild")
java_ShiftExpressionChild = Class(name="java::ShiftExpressionChild", is_abstract=True)
java_UnaryExpressionChild = Class(name="java::UnaryExpressionChild", is_abstract=True)
java_UnaryModificationExpression = Class(name="java::UnaryModificationExpression", is_abstract=True)
UnaryExpressionChild = Class(name="UnaryExpressionChild")
java_UnaryModificationExpressionChild = Class(name="java::UnaryModificationExpressionChild", is_abstract=True)
java_UnaryModificationOperator = Class(name="java::UnaryModificationOperator", is_abstract=True)
java_PrefixUnaryModificationExpression = Class(name="java::PrefixUnaryModificationExpression")
UnaryModificationExpression = Class(name="UnaryModificationExpression")
java_MultiplicativeExpression = Class(name="java::MultiplicativeExpression")
AdditiveExpressionChild = Class(name="AdditiveExpressionChild")
java_MultiplicativeExpressionChild = Class(name="java::MultiplicativeExpressionChild", is_abstract=True)
java_MultiplicativeOperator = Class(name="java::MultiplicativeOperator", is_abstract=True)
java_UnaryExpression = Class(name="java::UnaryExpression")
MultiplicativeExpressionChild = Class(name="MultiplicativeExpressionChild")
java_UnaryOperator = Class(name="java::UnaryOperator", is_abstract=True)
java_TypeArgument = Class(name="java::TypeArgument", is_abstract=True)
java_TypeArgumentable = Class(name="java::TypeArgumentable", is_abstract=True)
java_CallTypeArgumentable = Class(name="java::CallTypeArgumentable", is_abstract=True)
java_TypeParametrizable = Class(name="java::TypeParametrizable", is_abstract=True)
java_TypeParameter = Class(name="java::TypeParameter")
java_ExtendsTypeArgument = Class(name="java::ExtendsTypeArgument")
TypeArgument = Class(name="TypeArgument")
java_SuffixUnaryModificationExpression = Class(name="java::SuffixUnaryModificationExpression")
java_CastExpression = Class(name="java::CastExpression")
UnaryModificationExpressionChild = Class(name="UnaryModificationExpressionChild")
java_PrimaryExpression = Class(name="java::PrimaryExpression", is_abstract=True)
java_NestedExpression = Class(name="java::NestedExpression")
java_UnknownTypeArgument = Class(name="java::UnknownTypeArgument")
java_Import = Class(name="java::Import", is_abstract=True)
java_QualifiedTypeArgument = Class(name="java::QualifiedTypeArgument")
java_SuperTypeArgument = Class(name="java::SuperTypeArgument")
java_ImportingElement = Class(name="java::ImportingElement", is_abstract=True)
java_Static = Class(name="java::Static")
java_ClassifierImport = Class(name="java::ClassifierImport")
java_PackageImport = Class(name="java::PackageImport")
java_StaticClassifierImport = Class(name="java::StaticClassifierImport")
StaticImport = Class(name="StaticImport")
java_StaticImport = Class(name="java::StaticImport", is_abstract=True)
Import = Class(name="Import")
java_Instantiation = Class(name="java::Instantiation", is_abstract=True)
Argumentable = Class(name="Argumentable")
java_NewConstructorCall = Class(name="java::NewConstructorCall")
Instantiation = Class(name="Instantiation")
CallTypeArgumentable = Class(name="CallTypeArgumentable")
java_StaticMemberImport = Class(name="java::StaticMemberImport")
java_ReferenceableElement = Class(name="java::ReferenceableElement", is_abstract=True)
java_Initializable = Class(name="java::Initializable", is_abstract=True)
java_Literal = Class(name="java::Literal", is_abstract=True)
PrimaryExpression = Class(name="PrimaryExpression")
java_BooleanLiteral = Class(name="java::BooleanLiteral")
java_ExplicitConstructorCall = Class(name="java::ExplicitConstructorCall")
Literal = Class(name="Literal")
java_Self = Class(name="java::Self", is_abstract=True)
java_DecimalFloatLiteral = Class(name="java::DecimalFloatLiteral")
FloatLiteral = Class(name="FloatLiteral")
java_HexFloatLiteral = Class(name="java::HexFloatLiteral")
java_DoubleLiteral = Class(name="java::DoubleLiteral", is_abstract=True)
java_DecimalDoubleLiteral = Class(name="java::DecimalDoubleLiteral")
DoubleLiteral = Class(name="DoubleLiteral")
java_CharacterLiteral = Class(name="java::CharacterLiteral")
java_FloatLiteral = Class(name="java::FloatLiteral", is_abstract=True)
IntegerLiteral = Class(name="IntegerLiteral")
java_HexIntegerLiteral = Class(name="java::HexIntegerLiteral")
java_OctalIntegerLiteral = Class(name="java::OctalIntegerLiteral")
java_LongLiteral = Class(name="java::LongLiteral", is_abstract=True)
java_DecimalLongLiteral = Class(name="java::DecimalLongLiteral")
LongLiteral = Class(name="LongLiteral")
java_HexDoubleLiteral = Class(name="java::HexDoubleLiteral")
java_IntegerLiteral = Class(name="java::IntegerLiteral", is_abstract=True)
java_DecimalIntegerLiteral = Class(name="java::DecimalIntegerLiteral")
java_OctalLongLiteral = Class(name="java::OctalLongLiteral")
java_NullLiteral = Class(name="java::NullLiteral")
java_Super = Class(name="java::Super")
Self = Class(name="Self")
java_This = Class(name="java::This")
java_ExceptionThrower = Class(name="java::ExceptionThrower", is_abstract=True)
java_NamespaceClassifierReference = Class(name="java::NamespaceClassifierReference")
java_HexLongLiteral = Class(name="java::HexLongLiteral")
java_Member = Class(name="java::Member", is_abstract=True)
java_MemberContainer = Class(name="java::MemberContainer", is_abstract=True)
java_AdditionalField = Class(name="java::AdditionalField")
Initializable = Class(name="Initializable")
java_Constructor = Class(name="java::Constructor")
StatementListContainer = Class(name="StatementListContainer")
Parametrizable = Class(name="Parametrizable")
ExceptionThrower = Class(name="ExceptionThrower")
java_Method = Class(name="java::Method", is_abstract=True)
java_EmptyMember = Class(name="java::EmptyMember")
java_Field = Class(name="java::Field")
Variable = Class(name="Variable")
Method_ = Class(name="Method")
java_ClassMethod = Class(name="java::ClassMethod")
java_Modifier = Class(name="java::Modifier", is_abstract=True)
java_AnnotationInstanceOrModifier = Class(name="java::AnnotationInstanceOrModifier", is_abstract=True)
java_AnnotableAndModifiable = Class(name="java::AnnotableAndModifiable", is_abstract=True)
java_Modifiable = Class(name="java::Modifiable", is_abstract=True)
java_Protected = Class(name="java::Protected")
java_Public = Class(name="java::Public")
java_Private = Class(name="java::Private")
java_Strictfp = Class(name="java::Strictfp")
java_Synchronized = Class(name="java::Synchronized")
java_Transient = Class(name="java::Transient")
java_Volatile = Class(name="java::Volatile")
java_Operator = Class(name="java::Operator", is_abstract=True)
Operator = Class(name="Operator")
java_Abstract = Class(name="java::Abstract")
Modifier = Class(name="Modifier")
java_Final = Class(name="java::Final")
java_Native = Class(name="java::Native")
java_Assignment = Class(name="java::Assignment")
AssignmentOperator = Class(name="AssignmentOperator")
java_AssignmentAnd = Class(name="java::AssignmentAnd")
java_AssignmentDivision = Class(name="java::AssignmentDivision")
java_AssignmentExclusiveOr = Class(name="java::AssignmentExclusiveOr")
java_AssignmentMinus = Class(name="java::AssignmentMinus")
java_AssignmentModulo = Class(name="java::AssignmentModulo")
java_AssignmentMultiplication = Class(name="java::AssignmentMultiplication")
java_AssignmentLeftShift = Class(name="java::AssignmentLeftShift")
java_NotEqual = Class(name="java::NotEqual")
java_GreaterThan = Class(name="java::GreaterThan")
RelationOperator = Class(name="RelationOperator")
java_GreaterThanOrEqual = Class(name="java::GreaterThanOrEqual")
java_LessThan = Class(name="java::LessThan")
java_LessThanOrEqual = Class(name="java::LessThanOrEqual")
java_Addition = Class(name="java::Addition")
AdditiveOperator = Class(name="AdditiveOperator")
UnaryOperator = Class(name="UnaryOperator")
java_Subtraction = Class(name="java::Subtraction")
java_Division = Class(name="java::Division")
MultiplicativeOperator = Class(name="MultiplicativeOperator")
java_AssignmentOr = Class(name="java::AssignmentOr")
java_AssignmentPlus = Class(name="java::AssignmentPlus")
java_AssignmentRightShift = Class(name="java::AssignmentRightShift")
java_AssignmentUnsignedRightShift = Class(name="java::AssignmentUnsignedRightShift")
java_PlusPlus = Class(name="java::PlusPlus")
java_Equal = Class(name="java::Equal")
EqualityOperator = Class(name="EqualityOperator")
java_LeftShift = Class(name="java::LeftShift")
ShiftOperator = Class(name="ShiftOperator")
java_RightShift = Class(name="java::RightShift")
java_UnsignedRightShift = Class(name="java::UnsignedRightShift")
java_Reference = Class(name="java::Reference", is_abstract=True)
TypeArgumentable = Class(name="TypeArgumentable")
java_Multiplication = Class(name="java::Multiplication")
java_Remainder = Class(name="java::Remainder")
java_Complement = Class(name="java::Complement")
java_MinusMinus = Class(name="java::MinusMinus")
UnaryModificationOperator = Class(name="UnaryModificationOperator")
java_Negate = Class(name="java::Negate")
java_ElementReference = Class(name="java::ElementReference", is_abstract=True)
java_SelfReference = Class(name="java::SelfReference")
java_Parameter = Class(name="java::Parameter", is_abstract=True)
java_Parametrizable = Class(name="java::Parametrizable", is_abstract=True)
java_Argumentable = Class(name="java::Argumentable", is_abstract=True)
java_OrdinaryParameter = Class(name="java::OrdinaryParameter")
Parameter_ = Class(name="Parameter")
java_VariableLengthParameter = Class(name="java::VariableLengthParameter")
java_IdentifierReference = Class(name="java::IdentifierReference")
ElementReference = Class(name="ElementReference")
java_StatementContainer = Class(name="java::StatementContainer", is_abstract=True)
java_MethodCall = Class(name="java::MethodCall")
java_ReflectiveClassReference = Class(name="java::ReflectiveClassReference")
java_PrimitiveTypeReference = Class(name="java::PrimitiveTypeReference")
java_PrimitiveType = Class(name="java::PrimitiveType", is_abstract=True)
java_StringReference = Class(name="java::StringReference")
java_Assert = Class(name="java::Assert")
Conditional = Class(name="Conditional")
java_Break = Class(name="java::Break")
Jump = Class(name="Jump")
java_Block = Class(name="java::Block")
Modifiable = Class(name="Modifiable")
java_CatchBlock = Class(name="java::CatchBlock")
java_Condition = Class(name="java::Condition")
java_Statement = Class(name="java::Statement", is_abstract=True)
java_StatementListContainer = Class(name="java::StatementListContainer", is_abstract=True)
java_Conditional = Class(name="java::Conditional", is_abstract=True)
java_ForLoopInitializer = Class(name="java::ForLoopInitializer", is_abstract=True)
java_ForEachLoop = Class(name="java::ForEachLoop")
java_SwitchCase = Class(name="java::SwitchCase", is_abstract=True)
java_Jump = Class(name="java::Jump", is_abstract=True)
java_JumpLabel = Class(name="java::JumpLabel")
StatementContainer = Class(name="StatementContainer")
java_Continue = Class(name="java::Continue")
java_DefaultSwitchCase = Class(name="java::DefaultSwitchCase")
SwitchCase = Class(name="SwitchCase")
java_DoWhileLoop = Class(name="java::DoWhileLoop")
WhileLoop = Class(name="WhileLoop")
java_EmptyStatement = Class(name="java::EmptyStatement")
java_ExpressionStatement = Class(name="java::ExpressionStatement")
java_ForLoop = Class(name="java::ForLoop")
java_Throw = Class(name="java::Throw")
java_TryBlock = Class(name="java::TryBlock")
java_WhileLoop = Class(name="java::WhileLoop")
java_LocalVariableStatement = Class(name="java::LocalVariableStatement")
java_LocalVariable = Class(name="java::LocalVariable")
java_NormalSwitchCase = Class(name="java::NormalSwitchCase")
java_Return = Class(name="java::Return")
java_Switch = Class(name="java::Switch")
java_SynchronizedBlock = Class(name="java::SynchronizedBlock")
java_ClassifierReference = Class(name="java::ClassifierReference")
TypeReference = Class(name="TypeReference")
java_Type = Class(name="java::Type", is_abstract=True)
java_TypedElement = Class(name="java::TypedElement", is_abstract=True)
java_Void = Class(name="java::Void")
java_PackageReference = Class(name="java::PackageReference")
java_Variable = Class(name="java::Variable", is_abstract=True)
java_Boolean = Class(name="java::Boolean")
PrimitiveType = Class(name="PrimitiveType")
java_Byte = Class(name="java::Byte")
java_Char = Class(name="java::Char")
java_Double = Class(name="java::Double")
java_Float = Class(name="java::Float")
java_Int = Class(name="java::Int")
java_Long = Class(name="java::Long")
java_Short = Class(name="java::Short")
java_AdditionalLocalVariable = Class(name="java::AdditionalLocalVariable")

# java_Annotable class attributes and methods

# Commentable class attributes and methods

# java_AnnotationInstance class attributes and methods

# Reference class attributes and methods

# AnnotationInstanceOrModifier class attributes and methods

# NamespaceAwareElement class attributes and methods

# java_Classifier class attributes and methods
java_Classifier_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
java_Classifier.methods={java_Classifier_m_getAllSuperClassifiers}

# java_AnnotationParameter class attributes and methods

# java_AnnotationAttribute class attributes and methods

# InterfaceMethod class attributes and methods

# java_Expression class attributes and methods
java_Expression_m_getType: Method = Method(name="getType", parameters={}, type=Type)
java_Expression_m_getAlternativeType: Method = Method(name="getAlternativeType", parameters={}, type=Type)
java_Expression_m_getOneType: Method = Method(name="getOneType", parameters={Parameter(name='alternative')}, type=Type)
java_Expression_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
java_Expression.methods={java_Expression_m_getOneType, java_Expression_m_getType, java_Expression_m_getAlternativeType, java_Expression_m_getArrayDimension}

# java_ArrayTypeable class attributes and methods
java_ArrayTypeable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
java_ArrayTypeable.methods={java_ArrayTypeable_m_getArrayDimension}

# java_ArrayDimension class attributes and methods

# java_ArrayInitializer class attributes and methods

# ArrayInitializationValue class attributes and methods

# AnnotationValue class attributes and methods

# java_ArrayInitializationValue class attributes and methods

# java_SingleAnnotationParameter class attributes and methods

# AnnotationParameter class attributes and methods

# java_AnnotationValue class attributes and methods

# java_AnnotationParameterList class attributes and methods

# java_AnnotationAttributeSetting class attributes and methods

# java_InterfaceMethod class attributes and methods

# java_ArrayInstantiationByValuesTyped class attributes and methods

# java_ArraySelector class attributes and methods

# Type class attributes and methods

# ReferenceableElement class attributes and methods

# java_ConcreteClassifier class attributes and methods
java_ConcreteClassifier_m_getInnerClassifiers: Method = Method(name="getInnerClassifiers", parameters={}, type=StringType)
java_ConcreteClassifier_m_getAllInnerClassifiers: Method = Method(name="getAllInnerClassifiers", parameters={}, type=StringType)
java_ConcreteClassifier_m_getSuperTypeReferences: Method = Method(name="getSuperTypeReferences", parameters={}, type=StringType)
java_ConcreteClassifier_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=Member)
java_ConcreteClassifier.methods={java_ConcreteClassifier_m_getSuperTypeReferences, java_ConcreteClassifier_m_getInnerClassifiers, java_ConcreteClassifier_m_getAllMembers, java_ConcreteClassifier_m_getAllInnerClassifiers}

# Classifier class attributes and methods

# TypeParametrizable class attributes and methods

# MemberContainer class attributes and methods

# Member class attributes and methods

# Statement class attributes and methods

# AnnotableAndModifiable class attributes and methods

# java_ArrayInstantiation class attributes and methods

# Expression class attributes and methods

# java_ArrayInstantiationBySize class attributes and methods

# ArrayInstantiation class attributes and methods

# TypedElement class attributes and methods

# ArrayTypeable class attributes and methods

# java_ArrayInstantiationByValues class attributes and methods

# java_ArrayInstantiationByValuesUntyped class attributes and methods

# ArrayInstantiationByValues class attributes and methods

# java_Interface class attributes and methods
java_Interface_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=ConcreteClassifier)
java_Interface.methods={java_Interface_m_getAllSuperClassifiers}

# java_Implementor class attributes and methods

# java_TypeReference class attributes and methods
java_TypeReference_m_getTarget: Method = Method(name="getTarget", parameters={}, type=Type)
java_TypeReference_m_getBoundTarget: Method = Method(name="getBoundTarget", parameters={Parameter(name='reference')}, type=Type)
java_TypeReference_m_getPureClassifierReference: Method = Method(name="getPureClassifierReference", parameters={}, type=StringType)
java_TypeReference.methods={java_TypeReference_m_getPureClassifierReference, java_TypeReference_m_getTarget, java_TypeReference_m_getBoundTarget}

# java_Class class attributes and methods
java_Class_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=ConcreteClassifier)
java_Class_m_getSuperClass: Method = Method(name="getSuperClass", parameters={}, type=StringType)
java_Class_m_unWrapPrimitiveType: Method = Method(name="unWrapPrimitiveType", parameters={}, type=StringType)
java_Class.methods={java_Class_m_unWrapPrimitiveType, java_Class_m_getAllSuperClassifiers, java_Class_m_getSuperClass}

# ConcreteClassifier class attributes and methods

# Implementor class attributes and methods

# java_Enumeration class attributes and methods
java_Enumeration_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=ConcreteClassifier)
java_Enumeration_m_getContainedConstant: Method = Method(name="getContainedConstant", parameters={Parameter(name='name')}, type=StringType)
java_Enumeration.methods={java_Enumeration_m_getContainedConstant, java_Enumeration_m_getAllSuperClassifiers}

# java_EnumConstant class attributes and methods

# java_Annotation class attributes and methods
java_Annotation_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=ConcreteClassifier)
java_Annotation.methods={java_Annotation_m_getAllSuperClassifiers}

# java_Commentable class attributes and methods
java_Commentable_m_getConcreteClassifier: Method = Method(name="getConcreteClassifier", parameters={Parameter(name='name')}, type=ConcreteClassifier)
java_Commentable_m_getConcreteClassifierProxies: Method = Method(name="getConcreteClassifierProxies", parameters={Parameter(name='packageName'), Parameter(name='classifierQuery')}, type=ConcreteClassifier)
java_Commentable_m_getLibClass: Method = Method(name="getLibClass", parameters={Parameter(name='name')}, type=StringType)
java_Commentable_m_getConcreteClassifierProxy: Method = Method(name="getConcreteClassifierProxy", parameters={Parameter(name='name')}, type=ConcreteClassifier)
java_Commentable_m_getConcreteClassifiers: Method = Method(name="getConcreteClassifiers", parameters={Parameter(name='classifierQuery'), Parameter(name='packageName')}, type=ConcreteClassifier)
java_Commentable_m_getObjectClass: Method = Method(name="getObjectClass", parameters={}, type=StringType)
java_Commentable_m_getStringClass: Method = Method(name="getStringClass", parameters={}, type=StringType)
java_Commentable_m_getAnnotationInterface: Method = Method(name="getAnnotationInterface", parameters={}, type=StringType)
java_Commentable_m_getLibInterface: Method = Method(name="getLibInterface", parameters={Parameter(name='name')}, type=StringType)
java_Commentable_m_getClassClass: Method = Method(name="getClassClass", parameters={}, type=StringType)
java_Commentable_m_getContainingConcreteClassifier: Method = Method(name="getContainingConcreteClassifier", parameters={}, type=ConcreteClassifier)
java_Commentable_m_getContainingCompilationUnit: Method = Method(name="getContainingCompilationUnit", parameters={}, type=StringType)
java_Commentable_m_getContainingPackageName: Method = Method(name="getContainingPackageName", parameters={}, type=StringType)
java_Commentable_m_getContainingAnnotationInstance: Method = Method(name="getContainingAnnotationInstance", parameters={}, type=StringType)
java_Commentable_m_getContainingAnonymousClass: Method = Method(name="getContainingAnonymousClass", parameters={}, type=StringType)
java_Commentable_m_getParentByType: Method = Method(name="getParentByType", parameters={Parameter(name='type')})
java_Commentable_m_getFirstChildByType: Method = Method(name="getFirstChildByType", parameters={Parameter(name='type')})
java_Commentable_m_getParentConcreteClassifier: Method = Method(name="getParentConcreteClassifier", parameters={}, type=ConcreteClassifier)
java_Commentable_m_getParentByEType: Method = Method(name="getParentByEType", parameters={Parameter(name='type')}, type=StringType)
java_Commentable_m_getFirstChildByEType: Method = Method(name="getFirstChildByEType", parameters={Parameter(name='type')}, type=StringType)
java_Commentable_m_getComments: Method = Method(name="getComments", parameters={}, type=StringType)
java_Commentable_m_addBeforeContainingStatement: Method = Method(name="addBeforeContainingStatement", parameters={Parameter(name='statementToAdd')})
java_Commentable_m_addAfterContainingStatement: Method = Method(name="addAfterContainingStatement", parameters={Parameter(name='statementToAdd')})
java_Commentable_m_getChildrenByEType: Method = Method(name="getChildrenByEType", parameters={Parameter(name='type')}, type=StringType)
java_Commentable_m_getChildrenByType: Method = Method(name="getChildrenByType", parameters={Parameter(name='type')})
java_Commentable.methods={java_Commentable_m_getAnnotationInterface, java_Commentable_m_getConcreteClassifiers, java_Commentable_m_getConcreteClassifierProxy, java_Commentable_m_getContainingCompilationUnit, java_Commentable_m_getParentByEType, java_Commentable_m_getChildrenByEType, java_Commentable_m_getContainingPackageName, java_Commentable_m_getContainingAnonymousClass, java_Commentable_m_getLibInterface, java_Commentable_m_getConcreteClassifier, java_Commentable_m_getContainingConcreteClassifier, java_Commentable_m_getContainingAnnotationInstance, java_Commentable_m_getParentByType, java_Commentable_m_getComments, java_Commentable_m_getConcreteClassifierProxies, java_Commentable_m_getChildrenByType, java_Commentable_m_getFirstChildByEType, java_Commentable_m_getStringClass, java_Commentable_m_getLibClass, java_Commentable_m_addBeforeContainingStatement, java_Commentable_m_getClassClass, java_Commentable_m_addAfterContainingStatement, java_Commentable_m_getFirstChildByType, java_Commentable_m_getParentConcreteClassifier, java_Commentable_m_getObjectClass}

# java_AnonymousClass class attributes and methods
java_AnonymousClass_m_getSuperClassifier: Method = Method(name="getSuperClassifier", parameters={}, type=ConcreteClassifier)
java_AnonymousClass_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=Member)
java_AnonymousClass_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=ConcreteClassifier)
java_AnonymousClass.methods={java_AnonymousClass_m_getSuperClassifier, java_AnonymousClass_m_getAllMembers, java_AnonymousClass_m_getAllSuperClassifiers}

# java_JavaRoot class attributes and methods
java_JavaRoot_m_getClassifiersInSamePackage: Method = Method(name="getClassifiersInSamePackage", parameters={}, type=ConcreteClassifier)
java_JavaRoot.methods={java_JavaRoot_m_getClassifiersInSamePackage}

# NamedElement class attributes and methods

# ImportingElement class attributes and methods

# java_LayoutInformation class attributes and methods

# java_NamedElement class attributes and methods
java_NamedElement_name: Property = Property(name="name", type=StringType)
java_NamedElement.attributes={java_NamedElement_name}

# java_NamespaceAwareElement class attributes and methods
java_NamespaceAwareElement_namespaces: Property = Property(name="namespaces", type=StringType)
java_NamespaceAwareElement_m_getClassifierAtNamespaces: Method = Method(name="getClassifierAtNamespaces", parameters={}, type=ConcreteClassifier)
java_NamespaceAwareElement_m_getNamespacesAsString: Method = Method(name="getNamespacesAsString", parameters={}, type=StringType)
java_NamespaceAwareElement.attributes={java_NamespaceAwareElement_namespaces}
java_NamespaceAwareElement.methods={java_NamespaceAwareElement_m_getClassifierAtNamespaces, java_NamespaceAwareElement_m_getNamespacesAsString}

# java_Package class attributes and methods
java_Package_m_getNamespacesAsString: Method = Method(name="getNamespacesAsString", parameters={}, type=StringType)
java_Package_m_getClassifiersInSamePackage: Method = Method(name="getClassifiersInSamePackage", parameters={}, type=ConcreteClassifier)
java_Package.methods={java_Package_m_getClassifiersInSamePackage, java_Package_m_getNamespacesAsString}

# Annotable class attributes and methods

# java_CompilationUnit class attributes and methods
java_CompilationUnit_m_getContainedClassifier: Method = Method(name="getContainedClassifier", parameters={Parameter(name='name')}, type=ConcreteClassifier)
java_CompilationUnit_m_getClassifiersInSamePackage: Method = Method(name="getClassifiersInSamePackage", parameters={}, type=ConcreteClassifier)
java_CompilationUnit.methods={java_CompilationUnit_m_getClassifiersInSamePackage, java_CompilationUnit_m_getContainedClassifier}

# JavaRoot class attributes and methods

# java_EmptyModel class attributes and methods

# java_ExpressionList class attributes and methods

# ForLoopInitializer class attributes and methods

# java_ConditionalExpression class attributes and methods

# AssignmentExpressionChild class attributes and methods

# java_ConditionalExpressionChild class attributes and methods

# java_AssignmentExpression class attributes and methods

# java_AssignmentExpressionChild class attributes and methods

# java_AssignmentOperator class attributes and methods

# java_InclusiveOrExpression class attributes and methods

# ConditionalAndExpressionChild class attributes and methods

# java_InclusiveOrExpressionChild class attributes and methods

# java_ExclusiveOrExpression class attributes and methods

# InclusiveOrExpressionChild class attributes and methods

# java_ExclusiveOrExpressionChild class attributes and methods

# java_ConditionalOrExpression class attributes and methods

# ConditionalExpressionChild class attributes and methods

# java_ConditionalOrExpressionChild class attributes and methods

# java_ConditionalAndExpression class attributes and methods

# ConditionalOrExpressionChild class attributes and methods

# java_ConditionalAndExpressionChild class attributes and methods

# java_EqualityExpressionChild class attributes and methods

# java_InstanceOfExpression class attributes and methods

# EqualityExpressionChild class attributes and methods

# java_InstanceOfExpressionChild class attributes and methods

# java_AndExpression class attributes and methods

# ExclusiveOrExpressionChild class attributes and methods

# java_AndExpressionChild class attributes and methods

# java_EqualityExpression class attributes and methods

# AndExpressionChild class attributes and methods

# java_EqualityOperator class attributes and methods

# java_ShiftOperator class attributes and methods

# java_AdditiveExpression class attributes and methods

# ShiftExpressionChild class attributes and methods

# java_AdditiveExpressionChild class attributes and methods

# java_AdditiveOperator class attributes and methods

# java_RelationExpression class attributes and methods

# InstanceOfExpressionChild class attributes and methods

# java_RelationExpressionChild class attributes and methods

# java_RelationOperator class attributes and methods

# java_ShiftExpression class attributes and methods

# RelationExpressionChild class attributes and methods

# java_ShiftExpressionChild class attributes and methods

# java_UnaryExpressionChild class attributes and methods

# java_UnaryModificationExpression class attributes and methods

# UnaryExpressionChild class attributes and methods

# java_UnaryModificationExpressionChild class attributes and methods

# java_UnaryModificationOperator class attributes and methods

# java_PrefixUnaryModificationExpression class attributes and methods

# UnaryModificationExpression class attributes and methods

# java_MultiplicativeExpression class attributes and methods

# AdditiveExpressionChild class attributes and methods

# java_MultiplicativeExpressionChild class attributes and methods

# java_MultiplicativeOperator class attributes and methods

# java_UnaryExpression class attributes and methods

# MultiplicativeExpressionChild class attributes and methods

# java_UnaryOperator class attributes and methods

# java_TypeArgument class attributes and methods

# java_TypeArgumentable class attributes and methods

# java_CallTypeArgumentable class attributes and methods

# java_TypeParametrizable class attributes and methods

# java_TypeParameter class attributes and methods
java_TypeParameter_m_getBoundType: Method = Method(name="getBoundType", parameters={Parameter(name='reference'), Parameter(name='typeReference')}, type=Type)
java_TypeParameter_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=ConcreteClassifier)
java_TypeParameter_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=Member)
java_TypeParameter.methods={java_TypeParameter_m_getBoundType, java_TypeParameter_m_getAllMembers, java_TypeParameter_m_getAllSuperClassifiers}

# java_ExtendsTypeArgument class attributes and methods

# TypeArgument class attributes and methods

# java_SuffixUnaryModificationExpression class attributes and methods

# java_CastExpression class attributes and methods

# UnaryModificationExpressionChild class attributes and methods

# java_PrimaryExpression class attributes and methods

# java_NestedExpression class attributes and methods

# java_UnknownTypeArgument class attributes and methods

# java_Import class attributes and methods
java_Import_m_getImportedClassifiers: Method = Method(name="getImportedClassifiers", parameters={}, type=ConcreteClassifier)
java_Import_m_getImportedMembers: Method = Method(name="getImportedMembers", parameters={}, type=NamedElement)
java_Import_m_getImportedClassifier: Method = Method(name="getImportedClassifier", parameters={Parameter(name='name')}, type=ConcreteClassifier)
java_Import.methods={java_Import_m_getImportedClassifiers, java_Import_m_getImportedClassifier, java_Import_m_getImportedMembers}

# java_QualifiedTypeArgument class attributes and methods

# java_SuperTypeArgument class attributes and methods

# java_ImportingElement class attributes and methods
java_ImportingElement_m_getDefaultImports: Method = Method(name="getDefaultImports", parameters={}, type=ConcreteClassifier)
java_ImportingElement.methods={java_ImportingElement_m_getDefaultImports}

# java_Static class attributes and methods

# java_ClassifierImport class attributes and methods

# java_PackageImport class attributes and methods

# java_StaticClassifierImport class attributes and methods

# StaticImport class attributes and methods

# java_StaticImport class attributes and methods

# Import class attributes and methods

# java_Instantiation class attributes and methods

# Argumentable class attributes and methods

# java_NewConstructorCall class attributes and methods

# Instantiation class attributes and methods

# CallTypeArgumentable class attributes and methods

# java_StaticMemberImport class attributes and methods

# java_ReferenceableElement class attributes and methods

# java_Initializable class attributes and methods

# java_Literal class attributes and methods
java_Literal_m_getOneType: Method = Method(name="getOneType", parameters={Parameter(name='alternative')}, type=Type)
java_Literal.methods={java_Literal_m_getOneType}

# PrimaryExpression class attributes and methods

# java_BooleanLiteral class attributes and methods
java_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
java_BooleanLiteral.attributes={java_BooleanLiteral_value}

# java_ExplicitConstructorCall class attributes and methods

# Literal class attributes and methods

# java_Self class attributes and methods

# java_DecimalFloatLiteral class attributes and methods
java_DecimalFloatLiteral_decimalValue: Property = Property(name="decimalValue", type=FloatType)
java_DecimalFloatLiteral.attributes={java_DecimalFloatLiteral_decimalValue}

# FloatLiteral class attributes and methods

# java_HexFloatLiteral class attributes and methods
java_HexFloatLiteral_hexValue: Property = Property(name="hexValue", type=FloatType)
java_HexFloatLiteral.attributes={java_HexFloatLiteral_hexValue}

# java_DoubleLiteral class attributes and methods

# java_DecimalDoubleLiteral class attributes and methods
java_DecimalDoubleLiteral_decimalValue: Property = Property(name="decimalValue", type=FloatType)
java_DecimalDoubleLiteral.attributes={java_DecimalDoubleLiteral_decimalValue}

# DoubleLiteral class attributes and methods

# java_CharacterLiteral class attributes and methods
java_CharacterLiteral_value: Property = Property(name="value", type=StringType)
java_CharacterLiteral.attributes={java_CharacterLiteral_value}

# java_FloatLiteral class attributes and methods

# IntegerLiteral class attributes and methods

# java_HexIntegerLiteral class attributes and methods
java_HexIntegerLiteral_hexValue: Property = Property(name="hexValue", type=StringType)
java_HexIntegerLiteral.attributes={java_HexIntegerLiteral_hexValue}

# java_OctalIntegerLiteral class attributes and methods
java_OctalIntegerLiteral_octalValue: Property = Property(name="octalValue", type=StringType)
java_OctalIntegerLiteral.attributes={java_OctalIntegerLiteral_octalValue}

# java_LongLiteral class attributes and methods

# java_DecimalLongLiteral class attributes and methods
java_DecimalLongLiteral_decimalValue: Property = Property(name="decimalValue", type=StringType)
java_DecimalLongLiteral.attributes={java_DecimalLongLiteral_decimalValue}

# LongLiteral class attributes and methods

# java_HexDoubleLiteral class attributes and methods
java_HexDoubleLiteral_hexValue: Property = Property(name="hexValue", type=FloatType)
java_HexDoubleLiteral.attributes={java_HexDoubleLiteral_hexValue}

# java_IntegerLiteral class attributes and methods

# java_DecimalIntegerLiteral class attributes and methods
java_DecimalIntegerLiteral_decimalValue: Property = Property(name="decimalValue", type=StringType)
java_DecimalIntegerLiteral.attributes={java_DecimalIntegerLiteral_decimalValue}

# java_OctalLongLiteral class attributes and methods
java_OctalLongLiteral_octalValue: Property = Property(name="octalValue", type=StringType)
java_OctalLongLiteral.attributes={java_OctalLongLiteral_octalValue}

# java_NullLiteral class attributes and methods

# java_Super class attributes and methods

# Self class attributes and methods

# java_This class attributes and methods

# java_ExceptionThrower class attributes and methods

# java_NamespaceClassifierReference class attributes and methods

# java_HexLongLiteral class attributes and methods
java_HexLongLiteral_hexValue: Property = Property(name="hexValue", type=StringType)
java_HexLongLiteral.attributes={java_HexLongLiteral_hexValue}

# java_Member class attributes and methods

# java_MemberContainer class attributes and methods
java_MemberContainer_m_getContainedField: Method = Method(name="getContainedField", parameters={Parameter(name='name')}, type=StringType)
java_MemberContainer_m_getContainedMethod: Method = Method(name="getContainedMethod", parameters={Parameter(name='name')}, type=StringType)
java_MemberContainer_m_getMethods: Method = Method(name="getMethods", parameters={}, type=StringType)
java_MemberContainer_m_getContainedClassifier: Method = Method(name="getContainedClassifier", parameters={Parameter(name='name')}, type=ConcreteClassifier)
java_MemberContainer_m_getMembersByName: Method = Method(name="getMembersByName", parameters={Parameter(name='name')}, type=Member)
java_MemberContainer_m_createField: Method = Method(name="createField", parameters={Parameter(name='name'), Parameter(name='qualifiedTypeName')}, type=StringType)
java_MemberContainer_m_getFields: Method = Method(name="getFields", parameters={}, type=StringType)
java_MemberContainer_m_removeMethods: Method = Method(name="removeMethods", parameters={Parameter(name='name')})
java_MemberContainer.methods={java_MemberContainer_m_getContainedClassifier, java_MemberContainer_m_getMethods, java_MemberContainer_m_getContainedField, java_MemberContainer_m_removeMethods, java_MemberContainer_m_createField, java_MemberContainer_m_getFields, java_MemberContainer_m_getContainedMethod, java_MemberContainer_m_getMembersByName}

# java_AdditionalField class attributes and methods
java_AdditionalField_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
java_AdditionalField.methods={java_AdditionalField_m_getArrayDimension}

# Initializable class attributes and methods

# java_Constructor class attributes and methods

# StatementListContainer class attributes and methods

# Parametrizable class attributes and methods

# ExceptionThrower class attributes and methods

# java_Method class attributes and methods
java_Method_m_isMethodForCall: Method = Method(name="isMethodForCall", parameters={Parameter(name='methodCall'), Parameter(name='needsPerfectMatch')}, type=BooleanType)
java_Method_m_isSomeMethodForCall: Method = Method(name="isSomeMethodForCall", parameters={Parameter(name='methodCall')}, type=BooleanType)
java_Method_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
java_Method_m_isBetterMethodForCall: Method = Method(name="isBetterMethodForCall", parameters={Parameter(name='otherMethod'), Parameter(name='methodCall')}, type=BooleanType)
java_Method.methods={java_Method_m_getArrayDimension, java_Method_m_isSomeMethodForCall, java_Method_m_isMethodForCall, java_Method_m_isBetterMethodForCall}

# java_EmptyMember class attributes and methods

# java_Field class attributes and methods

# Variable class attributes and methods

# Method class attributes and methods

# java_ClassMethod class attributes and methods

# java_Modifier class attributes and methods

# java_AnnotationInstanceOrModifier class attributes and methods

# java_AnnotableAndModifiable class attributes and methods
java_AnnotableAndModifiable_m_removeModifier: Method = Method(name="removeModifier", parameters={Parameter(name='modifierType')})
java_AnnotableAndModifiable_m_makePublic: Method = Method(name="makePublic", parameters={})
java_AnnotableAndModifiable_m_makePrivate: Method = Method(name="makePrivate", parameters={})
java_AnnotableAndModifiable_m_makeProtected: Method = Method(name="makeProtected", parameters={})
java_AnnotableAndModifiable_m_getModifiers: Method = Method(name="getModifiers", parameters={}, type=StringType)
java_AnnotableAndModifiable_m_removeAllModifiers: Method = Method(name="removeAllModifiers", parameters={})
java_AnnotableAndModifiable_m_isHidden: Method = Method(name="isHidden", parameters={Parameter(name='context')}, type=BooleanType)
java_AnnotableAndModifiable_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
java_AnnotableAndModifiable_m_isPrivate: Method = Method(name="isPrivate", parameters={}, type=BooleanType)
java_AnnotableAndModifiable_m_isProtected: Method = Method(name="isProtected", parameters={}, type=BooleanType)
java_AnnotableAndModifiable_m_addModifier: Method = Method(name="addModifier", parameters={Parameter(name='newModifier')})
java_AnnotableAndModifiable_m_hasModifier: Method = Method(name="hasModifier", parameters={Parameter(name='type')}, type=BooleanType)
java_AnnotableAndModifiable_m_isPublic: Method = Method(name="isPublic", parameters={}, type=BooleanType)
java_AnnotableAndModifiable.methods={java_AnnotableAndModifiable_m_hasModifier, java_AnnotableAndModifiable_m_isPublic, java_AnnotableAndModifiable_m_getModifiers, java_AnnotableAndModifiable_m_isPrivate, java_AnnotableAndModifiable_m_makeProtected, java_AnnotableAndModifiable_m_removeAllModifiers, java_AnnotableAndModifiable_m_isStatic, java_AnnotableAndModifiable_m_isHidden, java_AnnotableAndModifiable_m_makePrivate, java_AnnotableAndModifiable_m_removeModifier, java_AnnotableAndModifiable_m_isProtected, java_AnnotableAndModifiable_m_addModifier, java_AnnotableAndModifiable_m_makePublic}

# java_Modifiable class attributes and methods

# java_Protected class attributes and methods

# java_Public class attributes and methods

# java_Private class attributes and methods

# java_Strictfp class attributes and methods

# java_Synchronized class attributes and methods

# java_Transient class attributes and methods

# java_Volatile class attributes and methods

# java_Operator class attributes and methods

# Operator class attributes and methods

# java_Abstract class attributes and methods

# Modifier class attributes and methods

# java_Final class attributes and methods

# java_Native class attributes and methods

# java_Assignment class attributes and methods

# AssignmentOperator class attributes and methods

# java_AssignmentAnd class attributes and methods

# java_AssignmentDivision class attributes and methods

# java_AssignmentExclusiveOr class attributes and methods

# java_AssignmentMinus class attributes and methods

# java_AssignmentModulo class attributes and methods

# java_AssignmentMultiplication class attributes and methods

# java_AssignmentLeftShift class attributes and methods

# java_NotEqual class attributes and methods

# java_GreaterThan class attributes and methods

# RelationOperator class attributes and methods

# java_GreaterThanOrEqual class attributes and methods

# java_LessThan class attributes and methods

# java_LessThanOrEqual class attributes and methods

# java_Addition class attributes and methods

# AdditiveOperator class attributes and methods

# UnaryOperator class attributes and methods

# java_Subtraction class attributes and methods

# java_Division class attributes and methods

# MultiplicativeOperator class attributes and methods

# java_AssignmentOr class attributes and methods

# java_AssignmentPlus class attributes and methods

# java_AssignmentRightShift class attributes and methods

# java_AssignmentUnsignedRightShift class attributes and methods

# java_PlusPlus class attributes and methods

# java_Equal class attributes and methods

# EqualityOperator class attributes and methods

# java_LeftShift class attributes and methods

# ShiftOperator class attributes and methods

# java_RightShift class attributes and methods

# java_UnsignedRightShift class attributes and methods

# java_Reference class attributes and methods
java_Reference_m_getReferencedType: Method = Method(name="getReferencedType", parameters={}, type=Type)
java_Reference_m_getPrevious: Method = Method(name="getPrevious", parameters={}, type=Reference)
java_Reference.methods={java_Reference_m_getReferencedType, java_Reference_m_getPrevious}

# TypeArgumentable class attributes and methods

# java_Multiplication class attributes and methods

# java_Remainder class attributes and methods

# java_Complement class attributes and methods

# java_MinusMinus class attributes and methods

# UnaryModificationOperator class attributes and methods

# java_Negate class attributes and methods

# java_ElementReference class attributes and methods

# java_SelfReference class attributes and methods

# java_Parameter class attributes and methods

# java_Parametrizable class attributes and methods

# java_Argumentable class attributes and methods
java_Argumentable_m_getArgumentTypes: Method = Method(name="getArgumentTypes", parameters={}, type=Type)
java_Argumentable.methods={java_Argumentable_m_getArgumentTypes}

# java_OrdinaryParameter class attributes and methods

# Parameter class attributes and methods

# java_VariableLengthParameter class attributes and methods

# java_IdentifierReference class attributes and methods

# ElementReference class attributes and methods

# java_StatementContainer class attributes and methods

# java_MethodCall class attributes and methods

# java_ReflectiveClassReference class attributes and methods

# java_PrimitiveTypeReference class attributes and methods

# java_PrimitiveType class attributes and methods
java_PrimitiveType_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=Member)
java_PrimitiveType_m_wrapPrimitiveType: Method = Method(name="wrapPrimitiveType", parameters={}, type=StringType)
java_PrimitiveType.methods={java_PrimitiveType_m_getAllMembers, java_PrimitiveType_m_wrapPrimitiveType}

# java_StringReference class attributes and methods
java_StringReference_value: Property = Property(name="value", type=StringType)
java_StringReference.attributes={java_StringReference_value}

# java_Assert class attributes and methods

# Conditional class attributes and methods

# java_Break class attributes and methods

# Jump class attributes and methods

# java_Block class attributes and methods

# Modifiable class attributes and methods

# java_CatchBlock class attributes and methods

# java_Condition class attributes and methods

# java_Statement class attributes and methods

# java_StatementListContainer class attributes and methods
java_StatementListContainer_m_getLocalVariable: Method = Method(name="getLocalVariable", parameters={Parameter(name='name')}, type=StringType)
java_StatementListContainer.methods={java_StatementListContainer_m_getLocalVariable}

# java_Conditional class attributes and methods

# java_ForLoopInitializer class attributes and methods

# java_ForEachLoop class attributes and methods

# java_SwitchCase class attributes and methods

# java_Jump class attributes and methods

# java_JumpLabel class attributes and methods

# StatementContainer class attributes and methods

# java_Continue class attributes and methods

# java_DefaultSwitchCase class attributes and methods

# SwitchCase class attributes and methods

# java_DoWhileLoop class attributes and methods

# WhileLoop class attributes and methods

# java_EmptyStatement class attributes and methods

# java_ExpressionStatement class attributes and methods

# java_ForLoop class attributes and methods

# java_Throw class attributes and methods

# java_TryBlock class attributes and methods

# java_WhileLoop class attributes and methods

# java_LocalVariableStatement class attributes and methods

# java_LocalVariable class attributes and methods

# java_NormalSwitchCase class attributes and methods

# java_Return class attributes and methods

# java_Switch class attributes and methods

# java_SynchronizedBlock class attributes and methods

# java_ClassifierReference class attributes and methods

# TypeReference class attributes and methods

# java_Type class attributes and methods
java_Type_m_equalsType: Method = Method(name="equalsType", parameters={Parameter(name='otherType'), Parameter(name='arrayDimension'), Parameter(name='otherArrayDimension')}, type=BooleanType)
java_Type_m_isSuperType: Method = Method(name="isSuperType", parameters={Parameter(name='otherArrayType'), Parameter(name='otherType'), Parameter(name='arrayDimension')}, type=BooleanType)
java_Type_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=Member)
java_Type.methods={java_Type_m_equalsType, java_Type_m_isSuperType, java_Type_m_getAllMembers}

# java_TypedElement class attributes and methods

# java_Void class attributes and methods

# java_PackageReference class attributes and methods

# java_Variable class attributes and methods
java_Variable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
java_Variable_m_createMethodCallStatement: Method = Method(name="createMethodCallStatement", parameters={Parameter(name='arguments'), Parameter(name='methodName')}, type=Statement)
java_Variable_m_createMethodCall: Method = Method(name="createMethodCall", parameters={Parameter(name='methodName'), Parameter(name='arguments')}, type=Expression)
java_Variable.methods={java_Variable_m_createMethodCallStatement, java_Variable_m_createMethodCall, java_Variable_m_getArrayDimension}

# java_Boolean class attributes and methods

# PrimitiveType class attributes and methods

# java_Byte class attributes and methods

# java_Char class attributes and methods

# java_Double class attributes and methods

# java_Float class attributes and methods

# java_Int class attributes and methods

# java_Long class attributes and methods

# java_Short class attributes and methods

# java_AdditionalLocalVariable class attributes and methods
java_AdditionalLocalVariable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
java_AdditionalLocalVariable.methods={java_AdditionalLocalVariable_m_getArrayDimension}

# Relationships
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="java_AnnotationInstance", type=java_Annotable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Annotable", type=java_AnnotationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation1: BinaryAssociation = BinaryAssociation(
    name="annotation1",
    ends={
        Property(name="java_Classifier", type=java_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationInstance2", type=java_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
parameter3: BinaryAssociation = BinaryAssociation(
    name="parameter3",
    ends={
        Property(name="java_AnnotationParameter", type=java_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationInstance4", type=java_AnnotationParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="java_AnnotationAttributeSetting10", type=java_AnnotationValue, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="java_AnnotationValue11", type=java_AnnotationAttributeSetting, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue12: BinaryAssociation = BinaryAssociation(
    name="defaultValue12",
    ends={
        Property(name="java_Expression", type=java_AnnotationAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationAttribute", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arrayDimensionsBefore13: BinaryAssociation = BinaryAssociation(
    name="arrayDimensionsBefore13",
    ends={
        Property(name="java_ArrayDimension", type=java_ArrayTypeable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayTypeable", type=java_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayDimensionsAfter14: BinaryAssociation = BinaryAssociation(
    name="arrayDimensionsAfter14",
    ends={
        Property(name="java_ArrayDimension16", type=java_ArrayTypeable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayTypeable15", type=java_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValues17: BinaryAssociation = BinaryAssociation(
    name="initialValues17",
    ends={
        Property(name="java_ArrayInitializationValue", type=java_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayInitializer", type=java_ArrayInitializationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value5: BinaryAssociation = BinaryAssociation(
    name="value5",
    ends={
        Property(name="java_AnnotationValue", type=java_SingleAnnotationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SingleAnnotationParameter", type=java_AnnotationValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
settings6: BinaryAssociation = BinaryAssociation(
    name="settings6",
    ends={
        Property(name="java_AnnotationAttributeSetting", type=java_AnnotationParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationParameterList", type=java_AnnotationAttributeSetting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute7: BinaryAssociation = BinaryAssociation(
    name="attribute7",
    ends={
        Property(name="java_InterfaceMethod", type=java_AnnotationAttributeSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotationAttributeSetting8", type=java_InterfaceMethod, multiplicity=Multiplicity(1, 1))
    }
)
position22: BinaryAssociation = BinaryAssociation(
    name="position22",
    ends={
        Property(name="java_Expression23", type=java_ArraySelector, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArraySelector", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizes18: BinaryAssociation = BinaryAssociation(
    name="sizes18",
    ends={
        Property(name="java_Expression19", type=java_ArrayInstantiationBySize, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayInstantiationBySize", type=java_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arrayInitializer20: BinaryAssociation = BinaryAssociation(
    name="arrayInitializer20",
    ends={
        Property(name="java_ArrayInitializer21", type=java_ArrayInstantiationByValues, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ArrayInstantiationByValues", type=java_ArrayInitializer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extends25: BinaryAssociation = BinaryAssociation(
    name="extends25",
    ends={
        Property(name="java_TypeReference26", type=java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Class", type=java_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExtends27: BinaryAssociation = BinaryAssociation(
    name="defaultExtends27",
    ends={
        Property(name="java_TypeReference29", type=java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Class28", type=java_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implements24: BinaryAssociation = BinaryAssociation(
    name="implements24",
    ends={
        Property(name="java_TypeReference", type=java_Implementor, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Implementor", type=java_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants35: BinaryAssociation = BinaryAssociation(
    name="constants35",
    ends={
        Property(name="java_EnumConstant", type=java_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Enumeration", type=java_EnumConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends30: BinaryAssociation = BinaryAssociation(
    name="extends30",
    ends={
        Property(name="java_TypeReference31", type=java_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Interface", type=java_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultExtends32: BinaryAssociation = BinaryAssociation(
    name="defaultExtends32",
    ends={
        Property(name="java_TypeReference34", type=java_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Interface33", type=java_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layoutInformations36: BinaryAssociation = BinaryAssociation(
    name="layoutInformations36",
    ends={
        Property(name="java_LayoutInformation", type=java_Commentable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Commentable", type=java_LayoutInformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits38: BinaryAssociation = BinaryAssociation(
    name="compilationUnits38",
    ends={
        Property(name="java_CompilationUnit39", type=java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Package", type=java_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifiers37: BinaryAssociation = BinaryAssociation(
    name="classifiers37",
    ends={
        Property(name="java_ConcreteClassifier", type=java_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CompilationUnit", type=java_ConcreteClassifier, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expressions40: BinaryAssociation = BinaryAssociation(
    name="expressions40",
    ends={
        Property(name="java_Expression41", type=java_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExpressionList", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child48: BinaryAssociation = BinaryAssociation(
    name="child48",
    ends={
        Property(name="java_ConditionalExpressionChild", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression", type=java_ConditionalExpressionChild, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionIf49: BinaryAssociation = BinaryAssociation(
    name="expressionIf49",
    ends={
        Property(name="java_Expression51", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression50", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressionElse52: BinaryAssociation = BinaryAssociation(
    name="expressionElse52",
    ends={
        Property(name="java_AssignmentExpressionChild54", type=java_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalExpression53", type=java_AssignmentExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child42: BinaryAssociation = BinaryAssociation(
    name="child42",
    ends={
        Property(name="java_AssignmentExpressionChild", type=java_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssignmentExpression", type=java_AssignmentExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignmentOperator43: BinaryAssociation = BinaryAssociation(
    name="assignmentOperator43",
    ends={
        Property(name="java_AssignmentOperator", type=java_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssignmentExpression44", type=java_AssignmentOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value45: BinaryAssociation = BinaryAssociation(
    name="value45",
    ends={
        Property(name="java_Expression47", type=java_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AssignmentExpression46", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children56: BinaryAssociation = BinaryAssociation(
    name="children56",
    ends={
        Property(name="java_ConditionalAndExpression", type=java_ConditionalAndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="java_ConditionalAndExpressionChild", type=java_ConditionalAndExpression, multiplicity=Multiplicity(1, 1))
    }
)
children57: BinaryAssociation = BinaryAssociation(
    name="children57",
    ends={
        Property(name="java_InclusiveOrExpressionChild", type=java_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InclusiveOrExpression", type=java_InclusiveOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children55: BinaryAssociation = BinaryAssociation(
    name="children55",
    ends={
        Property(name="java_ConditionalOrExpressionChild", type=java_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ConditionalOrExpression", type=java_ConditionalOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
equalityOperators60: BinaryAssociation = BinaryAssociation(
    name="equalityOperators60",
    ends={
        Property(name="java_EqualityOperator", type=java_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EqualityExpression", type=java_EqualityOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children61: BinaryAssociation = BinaryAssociation(
    name="children61",
    ends={
        Property(name="java_EqualityExpressionChild", type=java_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EqualityExpression62", type=java_EqualityExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child63: BinaryAssociation = BinaryAssociation(
    name="child63",
    ends={
        Property(name="java_InstanceOfExpressionChild", type=java_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_InstanceOfExpression", type=java_InstanceOfExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children58: BinaryAssociation = BinaryAssociation(
    name="children58",
    ends={
        Property(name="java_ExclusiveOrExpressionChild", type=java_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExclusiveOrExpression", type=java_ExclusiveOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children59: BinaryAssociation = BinaryAssociation(
    name="children59",
    ends={
        Property(name="java_AndExpressionChild", type=java_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AndExpression", type=java_AndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children67: BinaryAssociation = BinaryAssociation(
    name="children67",
    ends={
        Property(name="java_ShiftExpression", type=java_ShiftExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="java_ShiftExpressionChild", type=java_ShiftExpression, multiplicity=Multiplicity(1, 1))
    }
)
shiftOperators68: BinaryAssociation = BinaryAssociation(
    name="shiftOperators68",
    ends={
        Property(name="java_ShiftOperator", type=java_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ShiftExpression69", type=java_ShiftOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children70: BinaryAssociation = BinaryAssociation(
    name="children70",
    ends={
        Property(name="java_AdditiveExpressionChild", type=java_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AdditiveExpression", type=java_AdditiveExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additiveOperators71: BinaryAssociation = BinaryAssociation(
    name="additiveOperators71",
    ends={
        Property(name="java_AdditiveOperator", type=java_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AdditiveExpression72", type=java_AdditiveOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children64: BinaryAssociation = BinaryAssociation(
    name="children64",
    ends={
        Property(name="java_RelationExpressionChild", type=java_RelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_RelationExpression", type=java_RelationExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationOperators65: BinaryAssociation = BinaryAssociation(
    name="relationOperators65",
    ends={
        Property(name="java_RelationOperator", type=java_RelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_RelationExpression66", type=java_RelationOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operators76: BinaryAssociation = BinaryAssociation(
    name="operators76",
    ends={
        Property(name="java_UnaryOperator", type=java_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnaryExpression", type=java_UnaryOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child77: BinaryAssociation = BinaryAssociation(
    name="child77",
    ends={
        Property(name="java_UnaryExpressionChild", type=java_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnaryExpression78", type=java_UnaryExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child79: BinaryAssociation = BinaryAssociation(
    name="child79",
    ends={
        Property(name="java_UnaryModificationExpressionChild", type=java_UnaryModificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnaryModificationExpression", type=java_UnaryModificationExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator80: BinaryAssociation = BinaryAssociation(
    name="operator80",
    ends={
        Property(name="java_UnaryModificationOperator", type=java_UnaryModificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_UnaryModificationExpression81", type=java_UnaryModificationOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children73: BinaryAssociation = BinaryAssociation(
    name="children73",
    ends={
        Property(name="java_MultiplicativeExpressionChild", type=java_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MultiplicativeExpression", type=java_MultiplicativeExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
multiplicativeOperators74: BinaryAssociation = BinaryAssociation(
    name="multiplicativeOperators74",
    ends={
        Property(name="java_MultiplicativeOperator", type=java_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MultiplicativeExpression75", type=java_MultiplicativeOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
typeArguments86: BinaryAssociation = BinaryAssociation(
    name="typeArguments86",
    ends={
        Property(name="java_TypeArgument", type=java_TypeArgumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeArgumentable", type=java_TypeArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callTypeArguments87: BinaryAssociation = BinaryAssociation(
    name="callTypeArguments87",
    ends={
        Property(name="java_TypeArgument88", type=java_CallTypeArgumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CallTypeArgumentable", type=java_TypeArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters89: BinaryAssociation = BinaryAssociation(
    name="typeParameters89",
    ends={
        Property(name="java_TypeParameter", type=java_TypeParametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeParametrizable", type=java_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child82: BinaryAssociation = BinaryAssociation(
    name="child82",
    ends={
        Property(name="java_MultiplicativeExpressionChild83", type=java_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CastExpression", type=java_MultiplicativeExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression84: BinaryAssociation = BinaryAssociation(
    name="expression84",
    ends={
        Property(name="java_Expression85", type=java_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_NestedExpression", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendTypes94: BinaryAssociation = BinaryAssociation(
    name="extendTypes94",
    ends={
        Property(name="java_TypeReference96", type=java_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypeParameter95", type=java_TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendTypes90: BinaryAssociation = BinaryAssociation(
    name="extendTypes90",
    ends={
        Property(name="java_TypeReference91", type=java_ExtendsTypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExtendsTypeArgument", type=java_TypeReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
superType92: BinaryAssociation = BinaryAssociation(
    name="superType92",
    ends={
        Property(name="java_TypeReference93", type=java_SuperTypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SuperTypeArgument", type=java_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
static98: BinaryAssociation = BinaryAssociation(
    name="static98",
    ends={
        Property(name="java_Static", type=java_StaticImport, multiplicity=Multiplicity(1, 1)),
        Property(name="java_StaticImport", type=java_Static, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier99: BinaryAssociation = BinaryAssociation(
    name="classifier99",
    ends={
        Property(name="java_ConcreteClassifier100", type=java_ClassifierImport, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassifierImport", type=java_ConcreteClassifier, multiplicity=Multiplicity(1, 1))
    }
)
imports97: BinaryAssociation = BinaryAssociation(
    name="imports97",
    ends={
        Property(name="java_Import", type=java_ImportingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ImportingElement", type=java_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue102: BinaryAssociation = BinaryAssociation(
    name="initialValue102",
    ends={
        Property(name="java_Initializable", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="java_Expression103", type=java_Initializable, multiplicity=Multiplicity(1, 1))
    }
)
anonymousClass104: BinaryAssociation = BinaryAssociation(
    name="anonymousClass104",
    ends={
        Property(name="java_AnonymousClass", type=java_NewConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="java_NewConstructorCall", type=java_AnonymousClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticMembers101: BinaryAssociation = BinaryAssociation(
    name="staticMembers101",
    ends={
        Property(name="java_ReferenceableElement", type=java_StaticMemberImport, multiplicity=Multiplicity(1, 1)),
        Property(name="java_StaticMemberImport", type=java_ReferenceableElement, multiplicity=Multiplicity(1, 9999))
    }
)
callTarget105: BinaryAssociation = BinaryAssociation(
    name="callTarget105",
    ends={
        Property(name="java_Self", type=java_ExplicitConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExplicitConstructorCall", type=java_Self, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exceptions106: BinaryAssociation = BinaryAssociation(
    name="exceptions106",
    ends={
        Property(name="java_NamespaceClassifierReference", type=java_ExceptionThrower, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExceptionThrower", type=java_NamespaceClassifierReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members107: BinaryAssociation = BinaryAssociation(
    name="members107",
    ends={
        Property(name="java_Member", type=java_MemberContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MemberContainer", type=java_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultMembers108: BinaryAssociation = BinaryAssociation(
    name="defaultMembers108",
    ends={
        Property(name="java_Member110", type=java_MemberContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_MemberContainer109", type=java_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
additionalFields111: BinaryAssociation = BinaryAssociation(
    name="additionalFields111",
    ends={
        Property(name="java_AdditionalField", type=java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Field", type=java_AdditionalField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClass112: BinaryAssociation = BinaryAssociation(
    name="anonymousClass112",
    ends={
        Property(name="java_AnonymousClass114", type=java_EnumConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="java_EnumConstant113", type=java_AnonymousClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationsAndModifiers115: BinaryAssociation = BinaryAssociation(
    name="annotationsAndModifiers115",
    ends={
        Property(name="java_AnnotationInstanceOrModifier", type=java_AnnotableAndModifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_AnnotableAndModifiable", type=java_AnnotationInstanceOrModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers116: BinaryAssociation = BinaryAssociation(
    name="modifiers116",
    ends={
        Property(name="java_Modifier", type=java_Modifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Modifiable", type=java_Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next118: BinaryAssociation = BinaryAssociation(
    name="next118",
    ends={
        Property(name="java_Reference", type=java_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Reference117", type=java_Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments122: BinaryAssociation = BinaryAssociation(
    name="arguments122",
    ends={
        Property(name="java_Expression123", type=java_Argumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Argumentable", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target124: BinaryAssociation = BinaryAssociation(
    name="target124",
    ends={
        Property(name="java_ReferenceableElement125", type=java_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ElementReference", type=java_ReferenceableElement, multiplicity=Multiplicity(1, 1))
    }
)
self127: BinaryAssociation = BinaryAssociation(
    name="self127",
    ends={
        Property(name="java_Self128", type=java_SelfReference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SelfReference", type=java_Self, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arraySelectors119: BinaryAssociation = BinaryAssociation(
    name="arraySelectors119",
    ends={
        Property(name="java_ArraySelector121", type=java_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Reference120", type=java_ArraySelector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters129: BinaryAssociation = BinaryAssociation(
    name="parameters129",
    ends={
        Property(name="java_Parameter", type=java_Parametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Parametrizable", type=java_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveType126: BinaryAssociation = BinaryAssociation(
    name="primitiveType126",
    ends={
        Property(name="java_PrimitiveType", type=java_PrimitiveTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PrimitiveTypeReference", type=java_PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
errorMessage135: BinaryAssociation = BinaryAssociation(
    name="errorMessage135",
    ends={
        Property(name="java_Expression136", type=java_Assert, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Assert", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter137: BinaryAssociation = BinaryAssociation(
    name="parameter137",
    ends={
        Property(name="java_OrdinaryParameter", type=java_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="java_CatchBlock", type=java_OrdinaryParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement130: BinaryAssociation = BinaryAssociation(
    name="statement130",
    ends={
        Property(name="java_Statement", type=java_StatementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_StatementContainer", type=java_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements131: BinaryAssociation = BinaryAssociation(
    name="statements131",
    ends={
        Property(name="java_Statement132", type=java_StatementListContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_StatementListContainer", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition133: BinaryAssociation = BinaryAssociation(
    name="condition133",
    ends={
        Property(name="java_Expression134", type=java_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Conditional", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next146: BinaryAssociation = BinaryAssociation(
    name="next146",
    ends={
        Property(name="java_OrdinaryParameter147", type=java_ForEachLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForEachLoop", type=java_OrdinaryParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection148: BinaryAssociation = BinaryAssociation(
    name="collection148",
    ends={
        Property(name="java_Expression150", type=java_ForEachLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForEachLoop149", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target151: BinaryAssociation = BinaryAssociation(
    name="target151",
    ends={
        Property(name="java_JumpLabel", type=java_Jump, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Jump", type=java_JumpLabel, multiplicity=Multiplicity(0, 1))
    }
)
elseStatement138: BinaryAssociation = BinaryAssociation(
    name="elseStatement138",
    ends={
        Property(name="java_Statement139", type=java_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Condition", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression140: BinaryAssociation = BinaryAssociation(
    name="expression140",
    ends={
        Property(name="java_Expression141", type=java_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ExpressionStatement", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init142: BinaryAssociation = BinaryAssociation(
    name="init142",
    ends={
        Property(name="java_ForLoopInitializer", type=java_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForLoop", type=java_ForLoopInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updates143: BinaryAssociation = BinaryAssociation(
    name="updates143",
    ends={
        Property(name="java_Expression145", type=java_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ForLoop144", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throwable161: BinaryAssociation = BinaryAssociation(
    name="throwable161",
    ends={
        Property(name="java_Expression162", type=java_Throw, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Throw", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catcheBlocks163: BinaryAssociation = BinaryAssociation(
    name="catcheBlocks163",
    ends={
        Property(name="java_CatchBlock164", type=java_TryBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryBlock", type=java_CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyBlock165: BinaryAssociation = BinaryAssociation(
    name="finallyBlock165",
    ends={
        Property(name="java_Block", type=java_TryBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TryBlock166", type=java_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable152: BinaryAssociation = BinaryAssociation(
    name="variable152",
    ends={
        Property(name="java_LocalVariable", type=java_LocalVariableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_LocalVariableStatement", type=java_LocalVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnValue153: BinaryAssociation = BinaryAssociation(
    name="returnValue153",
    ends={
        Property(name="java_Expression154", type=java_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Return", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases155: BinaryAssociation = BinaryAssociation(
    name="cases155",
    ends={
        Property(name="java_SwitchCase", type=java_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Switch", type=java_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable156: BinaryAssociation = BinaryAssociation(
    name="variable156",
    ends={
        Property(name="java_Expression158", type=java_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Switch157", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lockProvider159: BinaryAssociation = BinaryAssociation(
    name="lockProvider159",
    ends={
        Property(name="java_Expression160", type=java_SynchronizedBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="java_SynchronizedBlock", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target171: BinaryAssociation = BinaryAssociation(
    name="target171",
    ends={
        Property(name="java_Classifier172", type=java_ClassifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_ClassifierReference", type=java_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
condition167: BinaryAssociation = BinaryAssociation(
    name="condition167",
    ends={
        Property(name="java_Expression168", type=java_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="java_WhileLoop", type=java_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeReference169: BinaryAssociation = BinaryAssociation(
    name="typeReference169",
    ends={
        Property(name="java_TypeReference170", type=java_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_TypedElement", type=java_TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subpackages177: BinaryAssociation = BinaryAssociation(
    name="subpackages177",
    ends={
        Property(name="java_PackageReference", type=java_PackageReference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_PackageReference176", type=java_PackageReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierReferences173: BinaryAssociation = BinaryAssociation(
    name="classifierReferences173",
    ends={
        Property(name="java_ClassifierReference175", type=java_NamespaceClassifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="java_NamespaceClassifierReference174", type=java_ClassifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additionalLocalVariables178: BinaryAssociation = BinaryAssociation(
    name="additionalLocalVariables178",
    ends={
        Property(name="java_AdditionalLocalVariable", type=java_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="java_LocalVariable179", type=java_AdditionalLocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_java_Annotable_Commentable = Generalization(general=Commentable, specific=java_Annotable)
gen_java_AnnotationInstance_Reference = Generalization(general=Reference, specific=java_AnnotationInstance)
gen_java_AnnotationInstance_AnnotationInstanceOrModifier = Generalization(general=AnnotationInstanceOrModifier, specific=java_AnnotationInstance)
gen_java_AnnotationInstance_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=java_AnnotationInstance)
gen_java_AnnotationValue_Commentable = Generalization(general=Commentable, specific=java_AnnotationValue)
gen_java_AnnotationAttribute_InterfaceMethod = Generalization(general=InterfaceMethod, specific=java_AnnotationAttribute)
gen_java_ArrayTypeable_Commentable = Generalization(general=Commentable, specific=java_ArrayTypeable)
gen_java_ArrayDimension_Commentable = Generalization(general=Commentable, specific=java_ArrayDimension)
gen_java_ArrayInitializer_ArrayInitializationValue = Generalization(general=ArrayInitializationValue, specific=java_ArrayInitializer)
gen_java_ArrayInitializer_AnnotationValue = Generalization(general=AnnotationValue, specific=java_ArrayInitializer)
gen_java_AnnotationParameter_Commentable = Generalization(general=Commentable, specific=java_AnnotationParameter)
gen_java_SingleAnnotationParameter_AnnotationParameter = Generalization(general=AnnotationParameter, specific=java_SingleAnnotationParameter)
gen_java_AnnotationParameterList_AnnotationParameter = Generalization(general=AnnotationParameter, specific=java_AnnotationParameterList)
gen_java_AnnotationAttributeSetting_Commentable = Generalization(general=Commentable, specific=java_AnnotationAttributeSetting)
gen_java_ArrayInstantiationByValuesTyped_ArrayInstantiationByValues = Generalization(general=ArrayInstantiationByValues, specific=java_ArrayInstantiationByValuesTyped)
gen_java_ArrayInstantiationByValuesTyped_TypedElement = Generalization(general=TypedElement, specific=java_ArrayInstantiationByValuesTyped)
gen_java_ArrayInstantiationByValuesTyped_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_ArrayInstantiationByValuesTyped)
gen_java_ArraySelector_Commentable = Generalization(general=Commentable, specific=java_ArraySelector)
gen_java_Classifier_Type = Generalization(general=Type, specific=java_Classifier)
gen_java_Classifier_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_Classifier)
gen_java_ConcreteClassifier_Classifier = Generalization(general=Classifier, specific=java_ConcreteClassifier)
gen_java_ConcreteClassifier_TypeParametrizable = Generalization(general=TypeParametrizable, specific=java_ConcreteClassifier)
gen_java_ConcreteClassifier_MemberContainer = Generalization(general=MemberContainer, specific=java_ConcreteClassifier)
gen_java_ConcreteClassifier_Member = Generalization(general=Member, specific=java_ConcreteClassifier)
gen_java_ConcreteClassifier_Statement = Generalization(general=Statement, specific=java_ConcreteClassifier)
gen_java_ConcreteClassifier_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=java_ConcreteClassifier)
gen_java_ArrayInitializationValue_Commentable = Generalization(general=Commentable, specific=java_ArrayInitializationValue)
gen_java_ArrayInstantiation_Expression = Generalization(general=Expression, specific=java_ArrayInstantiation)
gen_java_ArrayInstantiation_Reference = Generalization(general=Reference, specific=java_ArrayInstantiation)
gen_java_ArrayInstantiationBySize_ArrayInstantiation = Generalization(general=ArrayInstantiation, specific=java_ArrayInstantiationBySize)
gen_java_ArrayInstantiationBySize_TypedElement = Generalization(general=TypedElement, specific=java_ArrayInstantiationBySize)
gen_java_ArrayInstantiationBySize_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_ArrayInstantiationBySize)
gen_java_ArrayInstantiationByValues_ArrayInstantiation = Generalization(general=ArrayInstantiation, specific=java_ArrayInstantiationByValues)
gen_java_ArrayInstantiationByValuesUntyped_ArrayInstantiationByValues = Generalization(general=ArrayInstantiationByValues, specific=java_ArrayInstantiationByValuesUntyped)
gen_java_Interface_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=java_Interface)
gen_java_Implementor_Commentable = Generalization(general=Commentable, specific=java_Implementor)
gen_java_Class_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=java_Class)
gen_java_Class_Implementor = Generalization(general=Implementor, specific=java_Class)
gen_java_Enumeration_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=java_Enumeration)
gen_java_Enumeration_Implementor = Generalization(general=Implementor, specific=java_Enumeration)
gen_java_Annotation_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=java_Annotation)
gen_java_AnonymousClass_Type = Generalization(general=Type, specific=java_AnonymousClass)
gen_java_AnonymousClass_MemberContainer = Generalization(general=MemberContainer, specific=java_AnonymousClass)
gen_java_JavaRoot_NamedElement = Generalization(general=NamedElement, specific=java_JavaRoot)
gen_java_JavaRoot_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=java_JavaRoot)
gen_java_JavaRoot_ImportingElement = Generalization(general=ImportingElement, specific=java_JavaRoot)
gen_java_NamedElement_Commentable = Generalization(general=Commentable, specific=java_NamedElement)
gen_java_NamespaceAwareElement_Commentable = Generalization(general=Commentable, specific=java_NamespaceAwareElement)
gen_java_Package_JavaRoot = Generalization(general=JavaRoot, specific=java_Package)
gen_java_Package_Annotable = Generalization(general=Annotable, specific=java_Package)
gen_java_CompilationUnit_JavaRoot = Generalization(general=JavaRoot, specific=java_CompilationUnit)
gen_java_EmptyModel_JavaRoot = Generalization(general=JavaRoot, specific=java_EmptyModel)
gen_java_ExpressionList_ForLoopInitializer = Generalization(general=ForLoopInitializer, specific=java_ExpressionList)
gen_java_Expression_ArrayInitializationValue = Generalization(general=ArrayInitializationValue, specific=java_Expression)
gen_java_Expression_AnnotationValue = Generalization(general=AnnotationValue, specific=java_Expression)
gen_java_AssignmentExpressionChild_Expression = Generalization(general=Expression, specific=java_AssignmentExpressionChild)
gen_java_ConditionalExpression_AssignmentExpressionChild = Generalization(general=AssignmentExpressionChild, specific=java_ConditionalExpression)
gen_java_AssignmentExpression_Expression = Generalization(general=Expression, specific=java_AssignmentExpression)
gen_java_ConditionalAndExpressionChild_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=java_ConditionalAndExpressionChild)
gen_java_InclusiveOrExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=java_InclusiveOrExpression)
gen_java_InclusiveOrExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=java_InclusiveOrExpressionChild)
gen_java_ExclusiveOrExpression_InclusiveOrExpressionChild = Generalization(general=InclusiveOrExpressionChild, specific=java_ExclusiveOrExpression)
gen_java_ConditionalExpressionChild_AssignmentExpressionChild = Generalization(general=AssignmentExpressionChild, specific=java_ConditionalExpressionChild)
gen_java_ConditionalOrExpression_ConditionalExpressionChild = Generalization(general=ConditionalExpressionChild, specific=java_ConditionalOrExpression)
gen_java_ConditionalOrExpressionChild_ConditionalExpressionChild = Generalization(general=ConditionalExpressionChild, specific=java_ConditionalOrExpressionChild)
gen_java_ConditionalAndExpression_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=java_ConditionalAndExpression)
gen_java_EqualityExpressionChild_AndExpressionChild = Generalization(general=AndExpressionChild, specific=java_EqualityExpressionChild)
gen_java_InstanceOfExpression_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_InstanceOfExpression)
gen_java_InstanceOfExpression_TypedElement = Generalization(general=TypedElement, specific=java_InstanceOfExpression)
gen_java_InstanceOfExpression_EqualityExpressionChild = Generalization(general=EqualityExpressionChild, specific=java_InstanceOfExpression)
gen_java_InstanceOfExpressionChild_EqualityExpressionChild = Generalization(general=EqualityExpressionChild, specific=java_InstanceOfExpressionChild)
gen_java_ExclusiveOrExpressionChild_InclusiveOrExpressionChild = Generalization(general=InclusiveOrExpressionChild, specific=java_ExclusiveOrExpressionChild)
gen_java_AndExpression_ExclusiveOrExpressionChild = Generalization(general=ExclusiveOrExpressionChild, specific=java_AndExpression)
gen_java_AndExpressionChild_ExclusiveOrExpressionChild = Generalization(general=ExclusiveOrExpressionChild, specific=java_AndExpressionChild)
gen_java_EqualityExpression_AndExpressionChild = Generalization(general=AndExpressionChild, specific=java_EqualityExpression)
gen_java_ShiftExpressionChild_RelationExpressionChild = Generalization(general=RelationExpressionChild, specific=java_ShiftExpressionChild)
gen_java_AdditiveExpression_ShiftExpressionChild = Generalization(general=ShiftExpressionChild, specific=java_AdditiveExpression)
gen_java_RelationExpression_InstanceOfExpressionChild = Generalization(general=InstanceOfExpressionChild, specific=java_RelationExpression)
gen_java_RelationExpressionChild_InstanceOfExpressionChild = Generalization(general=InstanceOfExpressionChild, specific=java_RelationExpressionChild)
gen_java_ShiftExpression_RelationExpressionChild = Generalization(general=RelationExpressionChild, specific=java_ShiftExpression)
gen_java_UnaryExpressionChild_MultiplicativeExpressionChild = Generalization(general=MultiplicativeExpressionChild, specific=java_UnaryExpressionChild)
gen_java_UnaryModificationExpression_UnaryExpressionChild = Generalization(general=UnaryExpressionChild, specific=java_UnaryModificationExpression)
gen_java_PrefixUnaryModificationExpression_UnaryModificationExpression = Generalization(general=UnaryModificationExpression, specific=java_PrefixUnaryModificationExpression)
gen_java_AdditiveExpressionChild_ShiftExpressionChild = Generalization(general=ShiftExpressionChild, specific=java_AdditiveExpressionChild)
gen_java_MultiplicativeExpression_AdditiveExpressionChild = Generalization(general=AdditiveExpressionChild, specific=java_MultiplicativeExpression)
gen_java_MultiplicativeExpressionChild_AdditiveExpressionChild = Generalization(general=AdditiveExpressionChild, specific=java_MultiplicativeExpressionChild)
gen_java_UnaryExpression_MultiplicativeExpressionChild = Generalization(general=MultiplicativeExpressionChild, specific=java_UnaryExpression)
gen_java_TypeArgument_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_TypeArgument)
gen_java_TypeArgumentable_Commentable = Generalization(general=Commentable, specific=java_TypeArgumentable)
gen_java_CallTypeArgumentable_Commentable = Generalization(general=Commentable, specific=java_CallTypeArgumentable)
gen_java_TypeParametrizable_Commentable = Generalization(general=Commentable, specific=java_TypeParametrizable)
gen_java_ExtendsTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=java_ExtendsTypeArgument)
gen_java_SuffixUnaryModificationExpression_UnaryModificationExpression = Generalization(general=UnaryModificationExpression, specific=java_SuffixUnaryModificationExpression)
gen_java_UnaryModificationExpressionChild_UnaryExpressionChild = Generalization(general=UnaryExpressionChild, specific=java_UnaryModificationExpressionChild)
gen_java_CastExpression_TypedElement = Generalization(general=TypedElement, specific=java_CastExpression)
gen_java_CastExpression_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_CastExpression)
gen_java_CastExpression_UnaryModificationExpressionChild = Generalization(general=UnaryModificationExpressionChild, specific=java_CastExpression)
gen_java_PrimaryExpression_UnaryModificationExpressionChild = Generalization(general=UnaryModificationExpressionChild, specific=java_PrimaryExpression)
gen_java_NestedExpression_Reference = Generalization(general=Reference, specific=java_NestedExpression)
gen_java_UnknownTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=java_UnknownTypeArgument)
gen_java_Import_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=java_Import)
gen_java_QualifiedTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=java_QualifiedTypeArgument)
gen_java_QualifiedTypeArgument_TypedElement = Generalization(general=TypedElement, specific=java_QualifiedTypeArgument)
gen_java_SuperTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=java_SuperTypeArgument)
gen_java_TypeParameter_Classifier = Generalization(general=Classifier, specific=java_TypeParameter)
gen_java_ImportingElement_Commentable = Generalization(general=Commentable, specific=java_ImportingElement)
gen_java_ClassifierImport_Import = Generalization(general=Import, specific=java_ClassifierImport)
gen_java_PackageImport_Import = Generalization(general=Import, specific=java_PackageImport)
gen_java_StaticClassifierImport_StaticImport = Generalization(general=StaticImport, specific=java_StaticClassifierImport)
gen_java_StaticImport_Import = Generalization(general=Import, specific=java_StaticImport)
gen_java_Instantiation_Reference = Generalization(general=Reference, specific=java_Instantiation)
gen_java_Instantiation_Argumentable = Generalization(general=Argumentable, specific=java_Instantiation)
gen_java_NewConstructorCall_TypedElement = Generalization(general=TypedElement, specific=java_NewConstructorCall)
gen_java_NewConstructorCall_Instantiation = Generalization(general=Instantiation, specific=java_NewConstructorCall)
gen_java_NewConstructorCall_CallTypeArgumentable = Generalization(general=CallTypeArgumentable, specific=java_NewConstructorCall)
gen_java_StaticMemberImport_StaticImport = Generalization(general=StaticImport, specific=java_StaticMemberImport)
gen_java_Initializable_Commentable = Generalization(general=Commentable, specific=java_Initializable)
gen_java_Literal_PrimaryExpression = Generalization(general=PrimaryExpression, specific=java_Literal)
gen_java_Self_Commentable = Generalization(general=Commentable, specific=java_Self)
gen_java_ExplicitConstructorCall_Instantiation = Generalization(general=Instantiation, specific=java_ExplicitConstructorCall)
gen_java_BooleanLiteral_Literal = Generalization(general=Literal, specific=java_BooleanLiteral)
gen_java_FloatLiteral_Literal = Generalization(general=Literal, specific=java_FloatLiteral)
gen_java_DecimalFloatLiteral_FloatLiteral = Generalization(general=FloatLiteral, specific=java_DecimalFloatLiteral)
gen_java_HexFloatLiteral_FloatLiteral = Generalization(general=FloatLiteral, specific=java_HexFloatLiteral)
gen_java_DoubleLiteral_Literal = Generalization(general=Literal, specific=java_DoubleLiteral)
gen_java_DecimalDoubleLiteral_DoubleLiteral = Generalization(general=DoubleLiteral, specific=java_DecimalDoubleLiteral)
gen_java_CharacterLiteral_Literal = Generalization(general=Literal, specific=java_CharacterLiteral)
gen_java_DecimalIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=java_DecimalIntegerLiteral)
gen_java_HexIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=java_HexIntegerLiteral)
gen_java_OctalIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=java_OctalIntegerLiteral)
gen_java_LongLiteral_Literal = Generalization(general=Literal, specific=java_LongLiteral)
gen_java_DecimalLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=java_DecimalLongLiteral)
gen_java_HexDoubleLiteral_DoubleLiteral = Generalization(general=DoubleLiteral, specific=java_HexDoubleLiteral)
gen_java_IntegerLiteral_Literal = Generalization(general=Literal, specific=java_IntegerLiteral)
gen_java_OctalLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=java_OctalLongLiteral)
gen_java_NullLiteral_Literal = Generalization(general=Literal, specific=java_NullLiteral)
gen_java_Super_Self = Generalization(general=Self, specific=java_Super)
gen_java_This_Self = Generalization(general=Self, specific=java_This)
gen_java_ExceptionThrower_Commentable = Generalization(general=Commentable, specific=java_ExceptionThrower)
gen_java_HexLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=java_HexLongLiteral)
gen_java_Member_NamedElement = Generalization(general=NamedElement, specific=java_Member)
gen_java_MemberContainer_Commentable = Generalization(general=Commentable, specific=java_MemberContainer)
gen_java_AdditionalField_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_AdditionalField)
gen_java_AdditionalField_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_AdditionalField)
gen_java_AdditionalField_Initializable = Generalization(general=Initializable, specific=java_AdditionalField)
gen_java_Constructor_Member = Generalization(general=Member, specific=java_Constructor)
gen_java_Constructor_StatementListContainer = Generalization(general=StatementListContainer, specific=java_Constructor)
gen_java_Constructor_Parametrizable = Generalization(general=Parametrizable, specific=java_Constructor)
gen_java_Constructor_TypeParametrizable = Generalization(general=TypeParametrizable, specific=java_Constructor)
gen_java_Constructor_ExceptionThrower = Generalization(general=ExceptionThrower, specific=java_Constructor)
gen_java_Method_Member = Generalization(general=Member, specific=java_Method)
gen_java_Method_TypedElement = Generalization(general=TypedElement, specific=java_Method)
gen_java_Method_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_Method)
gen_java_Method_TypeParametrizable = Generalization(general=TypeParametrizable, specific=java_Method)
gen_java_Method_Parametrizable = Generalization(general=Parametrizable, specific=java_Method)
gen_java_Method_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_Method)
gen_java_Method_ExceptionThrower = Generalization(general=ExceptionThrower, specific=java_Method)
gen_java_Method_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=java_Method)
gen_java_Constructor_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=java_Constructor)
gen_java_EmptyMember_Member = Generalization(general=Member, specific=java_EmptyMember)
gen_java_Field_Member = Generalization(general=Member, specific=java_Field)
gen_java_Field_Initializable = Generalization(general=Initializable, specific=java_Field)
gen_java_Field_Variable = Generalization(general=Variable, specific=java_Field)
gen_java_Field_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_Field)
gen_java_Field_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=java_Field)
gen_java_InterfaceMethod_Method = Generalization(general=Method_, specific=java_InterfaceMethod)
gen_java_ClassMethod_Method = Generalization(general=Method_, specific=java_ClassMethod)
gen_java_ClassMethod_StatementListContainer = Generalization(general=StatementListContainer, specific=java_ClassMethod)
gen_java_EnumConstant_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_EnumConstant)
gen_java_EnumConstant_Argumentable = Generalization(general=Argumentable, specific=java_EnumConstant)
gen_java_EnumConstant_Annotable = Generalization(general=Annotable, specific=java_EnumConstant)
gen_java_Modifier_AnnotationInstanceOrModifier = Generalization(general=AnnotationInstanceOrModifier, specific=java_Modifier)
gen_java_AnnotationInstanceOrModifier_Commentable = Generalization(general=Commentable, specific=java_AnnotationInstanceOrModifier)
gen_java_AnnotableAndModifiable_Commentable = Generalization(general=Commentable, specific=java_AnnotableAndModifiable)
gen_java_Modifiable_Commentable = Generalization(general=Commentable, specific=java_Modifiable)
gen_java_Protected_Modifier = Generalization(general=Modifier, specific=java_Protected)
gen_java_Public_Modifier = Generalization(general=Modifier, specific=java_Public)
gen_java_Private_Modifier = Generalization(general=Modifier, specific=java_Private)
gen_java_Static_Modifier = Generalization(general=Modifier, specific=java_Static)
gen_java_Strictfp_Modifier = Generalization(general=Modifier, specific=java_Strictfp)
gen_java_Synchronized_Modifier = Generalization(general=Modifier, specific=java_Synchronized)
gen_java_Transient_Modifier = Generalization(general=Modifier, specific=java_Transient)
gen_java_Volatile_Modifier = Generalization(general=Modifier, specific=java_Volatile)
gen_java_Operator_Commentable = Generalization(general=Commentable, specific=java_Operator)
gen_java_AdditiveOperator_Operator = Generalization(general=Operator, specific=java_AdditiveOperator)
gen_java_Abstract_Modifier = Generalization(general=Modifier, specific=java_Abstract)
gen_java_Final_Modifier = Generalization(general=Modifier, specific=java_Final)
gen_java_Native_Modifier = Generalization(general=Modifier, specific=java_Native)
gen_java_ShiftOperator_Operator = Generalization(general=Operator, specific=java_ShiftOperator)
gen_java_UnaryOperator_Operator = Generalization(general=Operator, specific=java_UnaryOperator)
gen_java_UnaryModificationOperator_Operator = Generalization(general=Operator, specific=java_UnaryModificationOperator)
gen_java_Assignment_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_Assignment)
gen_java_AssignmentAnd_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentAnd)
gen_java_AssignmentDivision_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentDivision)
gen_java_AssignmentExclusiveOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentExclusiveOr)
gen_java_AssignmentMinus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentMinus)
gen_java_AssignmentModulo_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentModulo)
gen_java_AssignmentMultiplication_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentMultiplication)
gen_java_AssignmentLeftShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentLeftShift)
gen_java_AssignmentOperator_Operator = Generalization(general=Operator, specific=java_AssignmentOperator)
gen_java_EqualityOperator_Operator = Generalization(general=Operator, specific=java_EqualityOperator)
gen_java_MultiplicativeOperator_Operator = Generalization(general=Operator, specific=java_MultiplicativeOperator)
gen_java_RelationOperator_Operator = Generalization(general=Operator, specific=java_RelationOperator)
gen_java_Equal_EqualityOperator = Generalization(general=EqualityOperator, specific=java_Equal)
gen_java_NotEqual_EqualityOperator = Generalization(general=EqualityOperator, specific=java_NotEqual)
gen_java_GreaterThan_RelationOperator = Generalization(general=RelationOperator, specific=java_GreaterThan)
gen_java_GreaterThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=java_GreaterThanOrEqual)
gen_java_LessThan_RelationOperator = Generalization(general=RelationOperator, specific=java_LessThan)
gen_java_LessThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=java_LessThanOrEqual)
gen_java_Addition_AdditiveOperator = Generalization(general=AdditiveOperator, specific=java_Addition)
gen_java_Addition_UnaryOperator = Generalization(general=UnaryOperator, specific=java_Addition)
gen_java_Subtraction_AdditiveOperator = Generalization(general=AdditiveOperator, specific=java_Subtraction)
gen_java_Subtraction_UnaryOperator = Generalization(general=UnaryOperator, specific=java_Subtraction)
gen_java_AssignmentOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentOr)
gen_java_AssignmentPlus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentPlus)
gen_java_AssignmentRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentRightShift)
gen_java_AssignmentUnsignedRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=java_AssignmentUnsignedRightShift)
gen_java_PlusPlus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=java_PlusPlus)
gen_java_LeftShift_ShiftOperator = Generalization(general=ShiftOperator, specific=java_LeftShift)
gen_java_RightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=java_RightShift)
gen_java_UnsignedRightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=java_UnsignedRightShift)
gen_java_Reference_PrimaryExpression = Generalization(general=PrimaryExpression, specific=java_Reference)
gen_java_Reference_TypeArgumentable = Generalization(general=TypeArgumentable, specific=java_Reference)
gen_java_Division_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=java_Division)
gen_java_Multiplication_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=java_Multiplication)
gen_java_Remainder_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=java_Remainder)
gen_java_Complement_UnaryOperator = Generalization(general=UnaryOperator, specific=java_Complement)
gen_java_MinusMinus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=java_MinusMinus)
gen_java_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=java_Negate)
gen_java_ReferenceableElement_NamedElement = Generalization(general=NamedElement, specific=java_ReferenceableElement)
gen_java_ElementReference_Reference = Generalization(general=Reference, specific=java_ElementReference)
gen_java_SelfReference_Reference = Generalization(general=Reference, specific=java_SelfReference)
gen_java_Parameter_Variable = Generalization(general=Variable, specific=java_Parameter)
gen_java_Parameter_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=java_Parameter)
gen_java_Parametrizable_Commentable = Generalization(general=Commentable, specific=java_Parametrizable)
gen_java_Argumentable_Commentable = Generalization(general=Commentable, specific=java_Argumentable)
gen_java_OrdinaryParameter_Parameter = Generalization(general=Parameter_, specific=java_OrdinaryParameter)
gen_java_VariableLengthParameter_Parameter = Generalization(general=Parameter_, specific=java_VariableLengthParameter)
gen_java_StatementContainer_Commentable = Generalization(general=Commentable, specific=java_StatementContainer)
gen_java_IdentifierReference_ElementReference = Generalization(general=ElementReference, specific=java_IdentifierReference)
gen_java_MethodCall_ElementReference = Generalization(general=ElementReference, specific=java_MethodCall)
gen_java_MethodCall_Argumentable = Generalization(general=Argumentable, specific=java_MethodCall)
gen_java_MethodCall_CallTypeArgumentable = Generalization(general=CallTypeArgumentable, specific=java_MethodCall)
gen_java_ReflectiveClassReference_Reference = Generalization(general=Reference, specific=java_ReflectiveClassReference)
gen_java_PrimitiveTypeReference_Reference = Generalization(general=Reference, specific=java_PrimitiveTypeReference)
gen_java_StringReference_Reference = Generalization(general=Reference, specific=java_StringReference)
gen_java_Assert_Statement = Generalization(general=Statement, specific=java_Assert)
gen_java_Assert_Conditional = Generalization(general=Conditional, specific=java_Assert)
gen_java_Break_Jump = Generalization(general=Jump, specific=java_Break)
gen_java_Block_Member = Generalization(general=Member, specific=java_Block)
gen_java_Block_Statement = Generalization(general=Statement, specific=java_Block)
gen_java_Block_StatementListContainer = Generalization(general=StatementListContainer, specific=java_Block)
gen_java_Block_Modifiable = Generalization(general=Modifiable, specific=java_Block)
gen_java_CatchBlock_StatementListContainer = Generalization(general=StatementListContainer, specific=java_CatchBlock)
gen_java_StatementListContainer_Commentable = Generalization(general=Commentable, specific=java_StatementListContainer)
gen_java_Conditional_Commentable = Generalization(general=Commentable, specific=java_Conditional)
gen_java_ForLoopInitializer_Commentable = Generalization(general=Commentable, specific=java_ForLoopInitializer)
gen_java_ForEachLoop_Statement = Generalization(general=Statement, specific=java_ForEachLoop)
gen_java_ForEachLoop_StatementContainer = Generalization(general=StatementContainer, specific=java_ForEachLoop)
gen_java_Statement_Commentable = Generalization(general=Commentable, specific=java_Statement)
gen_java_SwitchCase_StatementListContainer = Generalization(general=StatementListContainer, specific=java_SwitchCase)
gen_java_Jump_Statement = Generalization(general=Statement, specific=java_Jump)
gen_java_Condition_Statement = Generalization(general=Statement, specific=java_Condition)
gen_java_Condition_StatementContainer = Generalization(general=StatementContainer, specific=java_Condition)
gen_java_JumpLabel_Statement = Generalization(general=Statement, specific=java_JumpLabel)
gen_java_Condition_Conditional = Generalization(general=Conditional, specific=java_Condition)
gen_java_JumpLabel_StatementContainer = Generalization(general=StatementContainer, specific=java_JumpLabel)
gen_java_JumpLabel_NamedElement = Generalization(general=NamedElement, specific=java_JumpLabel)
gen_java_Continue_Jump = Generalization(general=Jump, specific=java_Continue)
gen_java_DefaultSwitchCase_SwitchCase = Generalization(general=SwitchCase, specific=java_DefaultSwitchCase)
gen_java_DoWhileLoop_WhileLoop = Generalization(general=WhileLoop, specific=java_DoWhileLoop)
gen_java_EmptyStatement_Statement = Generalization(general=Statement, specific=java_EmptyStatement)
gen_java_ExpressionStatement_Statement = Generalization(general=Statement, specific=java_ExpressionStatement)
gen_java_ForLoop_Statement = Generalization(general=Statement, specific=java_ForLoop)
gen_java_ForLoop_StatementContainer = Generalization(general=StatementContainer, specific=java_ForLoop)
gen_java_ForLoop_Conditional = Generalization(general=Conditional, specific=java_ForLoop)
gen_java_Throw_Statement = Generalization(general=Statement, specific=java_Throw)
gen_java_TryBlock_Statement = Generalization(general=Statement, specific=java_TryBlock)
gen_java_TryBlock_StatementListContainer = Generalization(general=StatementListContainer, specific=java_TryBlock)
gen_java_WhileLoop_Statement = Generalization(general=Statement, specific=java_WhileLoop)
gen_java_WhileLoop_StatementContainer = Generalization(general=StatementContainer, specific=java_WhileLoop)
gen_java_LocalVariableStatement_Statement = Generalization(general=Statement, specific=java_LocalVariableStatement)
gen_java_NormalSwitchCase_SwitchCase = Generalization(general=SwitchCase, specific=java_NormalSwitchCase)
gen_java_NormalSwitchCase_Conditional = Generalization(general=Conditional, specific=java_NormalSwitchCase)
gen_java_Return_Statement = Generalization(general=Statement, specific=java_Return)
gen_java_Switch_Statement = Generalization(general=Statement, specific=java_Switch)
gen_java_SynchronizedBlock_Statement = Generalization(general=Statement, specific=java_SynchronizedBlock)
gen_java_SynchronizedBlock_StatementListContainer = Generalization(general=StatementListContainer, specific=java_SynchronizedBlock)
gen_java_TypeReference_Commentable = Generalization(general=Commentable, specific=java_TypeReference)
gen_java_ClassifierReference_TypeReference = Generalization(general=TypeReference, specific=java_ClassifierReference)
gen_java_ClassifierReference_TypeArgumentable = Generalization(general=TypeArgumentable, specific=java_ClassifierReference)
gen_java_NamespaceClassifierReference_TypeReference = Generalization(general=TypeReference, specific=java_NamespaceClassifierReference)
gen_java_NamespaceClassifierReference_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=java_NamespaceClassifierReference)
gen_java_Type_Commentable = Generalization(general=Commentable, specific=java_Type)
gen_java_TypedElement_Commentable = Generalization(general=Commentable, specific=java_TypedElement)
gen_java_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Void)
gen_java_PackageReference_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_PackageReference)
gen_java_Variable_NamedElement = Generalization(general=NamedElement, specific=java_Variable)
gen_java_Variable_TypedElement = Generalization(general=TypedElement, specific=java_Variable)
gen_java_Variable_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_Variable)
gen_java_Variable_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_Variable)
gen_java_Variable_TypeArgumentable = Generalization(general=TypeArgumentable, specific=java_Variable)
gen_java_PrimitiveType_Type = Generalization(general=Type, specific=java_PrimitiveType)
gen_java_PrimitiveType_TypeReference = Generalization(general=TypeReference, specific=java_PrimitiveType)
gen_java_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Boolean)
gen_java_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Byte)
gen_java_Char_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Char)
gen_java_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Double)
gen_java_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Float)
gen_java_Int_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Int)
gen_java_Long_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Long)
gen_java_Short_PrimitiveType = Generalization(general=PrimitiveType, specific=java_Short)
gen_java_LocalVariable_Variable = Generalization(general=Variable, specific=java_LocalVariable)
gen_java_LocalVariable_Initializable = Generalization(general=Initializable, specific=java_LocalVariable)
gen_java_LocalVariable_ForLoopInitializer = Generalization(general=ForLoopInitializer, specific=java_LocalVariable)
gen_java_LocalVariable_AnnotableAndModifiable = Generalization(general=AnnotableAndModifiable, specific=java_LocalVariable)
gen_java_AdditionalLocalVariable_ReferenceableElement = Generalization(general=ReferenceableElement, specific=java_AdditionalLocalVariable)
gen_java_AdditionalLocalVariable_ArrayTypeable = Generalization(general=ArrayTypeable, specific=java_AdditionalLocalVariable)
gen_java_AdditionalLocalVariable_Initializable = Generalization(general=Initializable, specific=java_AdditionalLocalVariable)

# Domain Model
domain_model = DomainModel(
    name="java",
    types={java_Annotable, Commentable, java_AnnotationInstance, Reference, AnnotationInstanceOrModifier, NamespaceAwareElement, java_Classifier, java_AnnotationParameter, java_AnnotationAttribute, InterfaceMethod, java_Expression, java_ArrayTypeable, java_ArrayDimension, java_ArrayInitializer, ArrayInitializationValue, AnnotationValue, java_ArrayInitializationValue, java_SingleAnnotationParameter, AnnotationParameter, java_AnnotationValue, java_AnnotationParameterList, java_AnnotationAttributeSetting, java_InterfaceMethod, java_ArrayInstantiationByValuesTyped, java_ArraySelector, Type, ReferenceableElement, java_ConcreteClassifier, Classifier, TypeParametrizable, MemberContainer, Member, Statement, AnnotableAndModifiable, java_ArrayInstantiation, Expression, java_ArrayInstantiationBySize, ArrayInstantiation, TypedElement, ArrayTypeable, java_ArrayInstantiationByValues, java_ArrayInstantiationByValuesUntyped, ArrayInstantiationByValues, java_Interface, java_Implementor, java_TypeReference, java_Class, ConcreteClassifier, Implementor, java_Enumeration, java_EnumConstant, java_Annotation, java_Commentable, java_AnonymousClass, java_JavaRoot, NamedElement, ImportingElement, java_LayoutInformation, java_NamedElement, java_NamespaceAwareElement, java_Package, Annotable, java_CompilationUnit, JavaRoot, java_EmptyModel, java_ExpressionList, ForLoopInitializer, java_ConditionalExpression, AssignmentExpressionChild, java_ConditionalExpressionChild, java_AssignmentExpression, java_AssignmentExpressionChild, java_AssignmentOperator, java_InclusiveOrExpression, ConditionalAndExpressionChild, java_InclusiveOrExpressionChild, java_ExclusiveOrExpression, InclusiveOrExpressionChild, java_ExclusiveOrExpressionChild, java_ConditionalOrExpression, ConditionalExpressionChild, java_ConditionalOrExpressionChild, java_ConditionalAndExpression, ConditionalOrExpressionChild, java_ConditionalAndExpressionChild, java_EqualityExpressionChild, java_InstanceOfExpression, EqualityExpressionChild, java_InstanceOfExpressionChild, java_AndExpression, ExclusiveOrExpressionChild, java_AndExpressionChild, java_EqualityExpression, AndExpressionChild, java_EqualityOperator, java_ShiftOperator, java_AdditiveExpression, ShiftExpressionChild, java_AdditiveExpressionChild, java_AdditiveOperator, java_RelationExpression, InstanceOfExpressionChild, java_RelationExpressionChild, java_RelationOperator, java_ShiftExpression, RelationExpressionChild, java_ShiftExpressionChild, java_UnaryExpressionChild, java_UnaryModificationExpression, UnaryExpressionChild, java_UnaryModificationExpressionChild, java_UnaryModificationOperator, java_PrefixUnaryModificationExpression, UnaryModificationExpression, java_MultiplicativeExpression, AdditiveExpressionChild, java_MultiplicativeExpressionChild, java_MultiplicativeOperator, java_UnaryExpression, MultiplicativeExpressionChild, java_UnaryOperator, java_TypeArgument, java_TypeArgumentable, java_CallTypeArgumentable, java_TypeParametrizable, java_TypeParameter, java_ExtendsTypeArgument, TypeArgument, java_SuffixUnaryModificationExpression, java_CastExpression, UnaryModificationExpressionChild, java_PrimaryExpression, java_NestedExpression, java_UnknownTypeArgument, java_Import, java_QualifiedTypeArgument, java_SuperTypeArgument, java_ImportingElement, java_Static, java_ClassifierImport, java_PackageImport, java_StaticClassifierImport, StaticImport, java_StaticImport, Import, java_Instantiation, Argumentable, java_NewConstructorCall, Instantiation, CallTypeArgumentable, java_StaticMemberImport, java_ReferenceableElement, java_Initializable, java_Literal, PrimaryExpression, java_BooleanLiteral, java_ExplicitConstructorCall, Literal, java_Self, java_DecimalFloatLiteral, FloatLiteral, java_HexFloatLiteral, java_DoubleLiteral, java_DecimalDoubleLiteral, DoubleLiteral, java_CharacterLiteral, java_FloatLiteral, IntegerLiteral, java_HexIntegerLiteral, java_OctalIntegerLiteral, java_LongLiteral, java_DecimalLongLiteral, LongLiteral, java_HexDoubleLiteral, java_IntegerLiteral, java_DecimalIntegerLiteral, java_OctalLongLiteral, java_NullLiteral, java_Super, Self, java_This, java_ExceptionThrower, java_NamespaceClassifierReference, java_HexLongLiteral, java_Member, java_MemberContainer, java_AdditionalField, Initializable, java_Constructor, StatementListContainer, Parametrizable, ExceptionThrower, java_Method, java_EmptyMember, java_Field, Variable, Method_, java_ClassMethod, java_Modifier, java_AnnotationInstanceOrModifier, java_AnnotableAndModifiable, java_Modifiable, java_Protected, java_Public, java_Private, java_Strictfp, java_Synchronized, java_Transient, java_Volatile, java_Operator, Operator, java_Abstract, Modifier, java_Final, java_Native, java_Assignment, AssignmentOperator, java_AssignmentAnd, java_AssignmentDivision, java_AssignmentExclusiveOr, java_AssignmentMinus, java_AssignmentModulo, java_AssignmentMultiplication, java_AssignmentLeftShift, java_NotEqual, java_GreaterThan, RelationOperator, java_GreaterThanOrEqual, java_LessThan, java_LessThanOrEqual, java_Addition, AdditiveOperator, UnaryOperator, java_Subtraction, java_Division, MultiplicativeOperator, java_AssignmentOr, java_AssignmentPlus, java_AssignmentRightShift, java_AssignmentUnsignedRightShift, java_PlusPlus, java_Equal, EqualityOperator, java_LeftShift, ShiftOperator, java_RightShift, java_UnsignedRightShift, java_Reference, TypeArgumentable, java_Multiplication, java_Remainder, java_Complement, java_MinusMinus, UnaryModificationOperator, java_Negate, java_ElementReference, java_SelfReference, java_Parameter, java_Parametrizable, java_Argumentable, java_OrdinaryParameter, Parameter_, java_VariableLengthParameter, java_IdentifierReference, ElementReference, java_StatementContainer, java_MethodCall, java_ReflectiveClassReference, java_PrimitiveTypeReference, java_PrimitiveType, java_StringReference, java_Assert, Conditional, java_Break, Jump, java_Block, Modifiable, java_CatchBlock, java_Condition, java_Statement, java_StatementListContainer, java_Conditional, java_ForLoopInitializer, java_ForEachLoop, java_SwitchCase, java_Jump, java_JumpLabel, StatementContainer, java_Continue, java_DefaultSwitchCase, SwitchCase, java_DoWhileLoop, WhileLoop, java_EmptyStatement, java_ExpressionStatement, java_ForLoop, java_Throw, java_TryBlock, java_WhileLoop, java_LocalVariableStatement, java_LocalVariable, java_NormalSwitchCase, java_Return, java_Switch, java_SynchronizedBlock, java_ClassifierReference, TypeReference, java_Type, java_TypedElement, java_Void, java_PackageReference, java_Variable, java_Boolean, PrimitiveType, java_Byte, java_Char, java_Double, java_Float, java_Int, java_Long, java_Short, java_AdditionalLocalVariable},
    associations={annotations0, annotation1, parameter3, value9, defaultValue12, arrayDimensionsBefore13, arrayDimensionsAfter14, initialValues17, value5, settings6, attribute7, position22, sizes18, arrayInitializer20, extends25, defaultExtends27, implements24, constants35, extends30, defaultExtends32, layoutInformations36, compilationUnits38, classifiers37, expressions40, child48, expressionIf49, expressionElse52, child42, assignmentOperator43, value45, children56, children57, children55, equalityOperators60, children61, child63, children58, children59, children67, shiftOperators68, children70, additiveOperators71, children64, relationOperators65, operators76, child77, child79, operator80, children73, multiplicativeOperators74, typeArguments86, callTypeArguments87, typeParameters89, child82, expression84, extendTypes94, extendTypes90, superType92, static98, classifier99, imports97, initialValue102, anonymousClass104, staticMembers101, callTarget105, exceptions106, members107, defaultMembers108, additionalFields111, anonymousClass112, annotationsAndModifiers115, modifiers116, next118, arguments122, target124, self127, arraySelectors119, parameters129, primitiveType126, errorMessage135, parameter137, statement130, statements131, condition133, next146, collection148, target151, elseStatement138, expression140, init142, updates143, throwable161, catcheBlocks163, finallyBlock165, variable152, returnValue153, cases155, variable156, lockProvider159, target171, condition167, typeReference169, subpackages177, classifierReferences173, additionalLocalVariables178},
    generalizations={gen_java_Annotable_Commentable, gen_java_AnnotationInstance_Reference, gen_java_AnnotationInstance_AnnotationInstanceOrModifier, gen_java_AnnotationInstance_NamespaceAwareElement, gen_java_AnnotationValue_Commentable, gen_java_AnnotationAttribute_InterfaceMethod, gen_java_ArrayTypeable_Commentable, gen_java_ArrayDimension_Commentable, gen_java_ArrayInitializer_ArrayInitializationValue, gen_java_ArrayInitializer_AnnotationValue, gen_java_AnnotationParameter_Commentable, gen_java_SingleAnnotationParameter_AnnotationParameter, gen_java_AnnotationParameterList_AnnotationParameter, gen_java_AnnotationAttributeSetting_Commentable, gen_java_ArrayInstantiationByValuesTyped_ArrayInstantiationByValues, gen_java_ArrayInstantiationByValuesTyped_TypedElement, gen_java_ArrayInstantiationByValuesTyped_ArrayTypeable, gen_java_ArraySelector_Commentable, gen_java_Classifier_Type, gen_java_Classifier_ReferenceableElement, gen_java_ConcreteClassifier_Classifier, gen_java_ConcreteClassifier_TypeParametrizable, gen_java_ConcreteClassifier_MemberContainer, gen_java_ConcreteClassifier_Member, gen_java_ConcreteClassifier_Statement, gen_java_ConcreteClassifier_AnnotableAndModifiable, gen_java_ArrayInitializationValue_Commentable, gen_java_ArrayInstantiation_Expression, gen_java_ArrayInstantiation_Reference, gen_java_ArrayInstantiationBySize_ArrayInstantiation, gen_java_ArrayInstantiationBySize_TypedElement, gen_java_ArrayInstantiationBySize_ArrayTypeable, gen_java_ArrayInstantiationByValues_ArrayInstantiation, gen_java_ArrayInstantiationByValuesUntyped_ArrayInstantiationByValues, gen_java_Interface_ConcreteClassifier, gen_java_Implementor_Commentable, gen_java_Class_ConcreteClassifier, gen_java_Class_Implementor, gen_java_Enumeration_ConcreteClassifier, gen_java_Enumeration_Implementor, gen_java_Annotation_ConcreteClassifier, gen_java_AnonymousClass_Type, gen_java_AnonymousClass_MemberContainer, gen_java_JavaRoot_NamedElement, gen_java_JavaRoot_NamespaceAwareElement, gen_java_JavaRoot_ImportingElement, gen_java_NamedElement_Commentable, gen_java_NamespaceAwareElement_Commentable, gen_java_Package_JavaRoot, gen_java_Package_Annotable, gen_java_CompilationUnit_JavaRoot, gen_java_EmptyModel_JavaRoot, gen_java_ExpressionList_ForLoopInitializer, gen_java_Expression_ArrayInitializationValue, gen_java_Expression_AnnotationValue, gen_java_AssignmentExpressionChild_Expression, gen_java_ConditionalExpression_AssignmentExpressionChild, gen_java_AssignmentExpression_Expression, gen_java_ConditionalAndExpressionChild_ConditionalOrExpressionChild, gen_java_InclusiveOrExpression_ConditionalAndExpressionChild, gen_java_InclusiveOrExpressionChild_ConditionalAndExpressionChild, gen_java_ExclusiveOrExpression_InclusiveOrExpressionChild, gen_java_ConditionalExpressionChild_AssignmentExpressionChild, gen_java_ConditionalOrExpression_ConditionalExpressionChild, gen_java_ConditionalOrExpressionChild_ConditionalExpressionChild, gen_java_ConditionalAndExpression_ConditionalOrExpressionChild, gen_java_EqualityExpressionChild_AndExpressionChild, gen_java_InstanceOfExpression_ArrayTypeable, gen_java_InstanceOfExpression_TypedElement, gen_java_InstanceOfExpression_EqualityExpressionChild, gen_java_InstanceOfExpressionChild_EqualityExpressionChild, gen_java_ExclusiveOrExpressionChild_InclusiveOrExpressionChild, gen_java_AndExpression_ExclusiveOrExpressionChild, gen_java_AndExpressionChild_ExclusiveOrExpressionChild, gen_java_EqualityExpression_AndExpressionChild, gen_java_ShiftExpressionChild_RelationExpressionChild, gen_java_AdditiveExpression_ShiftExpressionChild, gen_java_RelationExpression_InstanceOfExpressionChild, gen_java_RelationExpressionChild_InstanceOfExpressionChild, gen_java_ShiftExpression_RelationExpressionChild, gen_java_UnaryExpressionChild_MultiplicativeExpressionChild, gen_java_UnaryModificationExpression_UnaryExpressionChild, gen_java_PrefixUnaryModificationExpression_UnaryModificationExpression, gen_java_AdditiveExpressionChild_ShiftExpressionChild, gen_java_MultiplicativeExpression_AdditiveExpressionChild, gen_java_MultiplicativeExpressionChild_AdditiveExpressionChild, gen_java_UnaryExpression_MultiplicativeExpressionChild, gen_java_TypeArgument_ArrayTypeable, gen_java_TypeArgumentable_Commentable, gen_java_CallTypeArgumentable_Commentable, gen_java_TypeParametrizable_Commentable, gen_java_ExtendsTypeArgument_TypeArgument, gen_java_SuffixUnaryModificationExpression_UnaryModificationExpression, gen_java_UnaryModificationExpressionChild_UnaryExpressionChild, gen_java_CastExpression_TypedElement, gen_java_CastExpression_ArrayTypeable, gen_java_CastExpression_UnaryModificationExpressionChild, gen_java_PrimaryExpression_UnaryModificationExpressionChild, gen_java_NestedExpression_Reference, gen_java_UnknownTypeArgument_TypeArgument, gen_java_Import_NamespaceAwareElement, gen_java_QualifiedTypeArgument_TypeArgument, gen_java_QualifiedTypeArgument_TypedElement, gen_java_SuperTypeArgument_TypeArgument, gen_java_TypeParameter_Classifier, gen_java_ImportingElement_Commentable, gen_java_ClassifierImport_Import, gen_java_PackageImport_Import, gen_java_StaticClassifierImport_StaticImport, gen_java_StaticImport_Import, gen_java_Instantiation_Reference, gen_java_Instantiation_Argumentable, gen_java_NewConstructorCall_TypedElement, gen_java_NewConstructorCall_Instantiation, gen_java_NewConstructorCall_CallTypeArgumentable, gen_java_StaticMemberImport_StaticImport, gen_java_Initializable_Commentable, gen_java_Literal_PrimaryExpression, gen_java_Self_Commentable, gen_java_ExplicitConstructorCall_Instantiation, gen_java_BooleanLiteral_Literal, gen_java_FloatLiteral_Literal, gen_java_DecimalFloatLiteral_FloatLiteral, gen_java_HexFloatLiteral_FloatLiteral, gen_java_DoubleLiteral_Literal, gen_java_DecimalDoubleLiteral_DoubleLiteral, gen_java_CharacterLiteral_Literal, gen_java_DecimalIntegerLiteral_IntegerLiteral, gen_java_HexIntegerLiteral_IntegerLiteral, gen_java_OctalIntegerLiteral_IntegerLiteral, gen_java_LongLiteral_Literal, gen_java_DecimalLongLiteral_LongLiteral, gen_java_HexDoubleLiteral_DoubleLiteral, gen_java_IntegerLiteral_Literal, gen_java_OctalLongLiteral_LongLiteral, gen_java_NullLiteral_Literal, gen_java_Super_Self, gen_java_This_Self, gen_java_ExceptionThrower_Commentable, gen_java_HexLongLiteral_LongLiteral, gen_java_Member_NamedElement, gen_java_MemberContainer_Commentable, gen_java_AdditionalField_ReferenceableElement, gen_java_AdditionalField_ArrayTypeable, gen_java_AdditionalField_Initializable, gen_java_Constructor_Member, gen_java_Constructor_StatementListContainer, gen_java_Constructor_Parametrizable, gen_java_Constructor_TypeParametrizable, gen_java_Constructor_ExceptionThrower, gen_java_Method_Member, gen_java_Method_TypedElement, gen_java_Method_ArrayTypeable, gen_java_Method_TypeParametrizable, gen_java_Method_Parametrizable, gen_java_Method_ReferenceableElement, gen_java_Method_ExceptionThrower, gen_java_Method_AnnotableAndModifiable, gen_java_Constructor_AnnotableAndModifiable, gen_java_EmptyMember_Member, gen_java_Field_Member, gen_java_Field_Initializable, gen_java_Field_Variable, gen_java_Field_ReferenceableElement, gen_java_Field_AnnotableAndModifiable, gen_java_InterfaceMethod_Method, gen_java_ClassMethod_Method, gen_java_ClassMethod_StatementListContainer, gen_java_EnumConstant_ReferenceableElement, gen_java_EnumConstant_Argumentable, gen_java_EnumConstant_Annotable, gen_java_Modifier_AnnotationInstanceOrModifier, gen_java_AnnotationInstanceOrModifier_Commentable, gen_java_AnnotableAndModifiable_Commentable, gen_java_Modifiable_Commentable, gen_java_Protected_Modifier, gen_java_Public_Modifier, gen_java_Private_Modifier, gen_java_Static_Modifier, gen_java_Strictfp_Modifier, gen_java_Synchronized_Modifier, gen_java_Transient_Modifier, gen_java_Volatile_Modifier, gen_java_Operator_Commentable, gen_java_AdditiveOperator_Operator, gen_java_Abstract_Modifier, gen_java_Final_Modifier, gen_java_Native_Modifier, gen_java_ShiftOperator_Operator, gen_java_UnaryOperator_Operator, gen_java_UnaryModificationOperator_Operator, gen_java_Assignment_AssignmentOperator, gen_java_AssignmentAnd_AssignmentOperator, gen_java_AssignmentDivision_AssignmentOperator, gen_java_AssignmentExclusiveOr_AssignmentOperator, gen_java_AssignmentMinus_AssignmentOperator, gen_java_AssignmentModulo_AssignmentOperator, gen_java_AssignmentMultiplication_AssignmentOperator, gen_java_AssignmentLeftShift_AssignmentOperator, gen_java_AssignmentOperator_Operator, gen_java_EqualityOperator_Operator, gen_java_MultiplicativeOperator_Operator, gen_java_RelationOperator_Operator, gen_java_Equal_EqualityOperator, gen_java_NotEqual_EqualityOperator, gen_java_GreaterThan_RelationOperator, gen_java_GreaterThanOrEqual_RelationOperator, gen_java_LessThan_RelationOperator, gen_java_LessThanOrEqual_RelationOperator, gen_java_Addition_AdditiveOperator, gen_java_Addition_UnaryOperator, gen_java_Subtraction_AdditiveOperator, gen_java_Subtraction_UnaryOperator, gen_java_AssignmentOr_AssignmentOperator, gen_java_AssignmentPlus_AssignmentOperator, gen_java_AssignmentRightShift_AssignmentOperator, gen_java_AssignmentUnsignedRightShift_AssignmentOperator, gen_java_PlusPlus_UnaryModificationOperator, gen_java_LeftShift_ShiftOperator, gen_java_RightShift_ShiftOperator, gen_java_UnsignedRightShift_ShiftOperator, gen_java_Reference_PrimaryExpression, gen_java_Reference_TypeArgumentable, gen_java_Division_MultiplicativeOperator, gen_java_Multiplication_MultiplicativeOperator, gen_java_Remainder_MultiplicativeOperator, gen_java_Complement_UnaryOperator, gen_java_MinusMinus_UnaryModificationOperator, gen_java_Negate_UnaryOperator, gen_java_ReferenceableElement_NamedElement, gen_java_ElementReference_Reference, gen_java_SelfReference_Reference, gen_java_Parameter_Variable, gen_java_Parameter_AnnotableAndModifiable, gen_java_Parametrizable_Commentable, gen_java_Argumentable_Commentable, gen_java_OrdinaryParameter_Parameter, gen_java_VariableLengthParameter_Parameter, gen_java_StatementContainer_Commentable, gen_java_IdentifierReference_ElementReference, gen_java_MethodCall_ElementReference, gen_java_MethodCall_Argumentable, gen_java_MethodCall_CallTypeArgumentable, gen_java_ReflectiveClassReference_Reference, gen_java_PrimitiveTypeReference_Reference, gen_java_StringReference_Reference, gen_java_Assert_Statement, gen_java_Assert_Conditional, gen_java_Break_Jump, gen_java_Block_Member, gen_java_Block_Statement, gen_java_Block_StatementListContainer, gen_java_Block_Modifiable, gen_java_CatchBlock_StatementListContainer, gen_java_StatementListContainer_Commentable, gen_java_Conditional_Commentable, gen_java_ForLoopInitializer_Commentable, gen_java_ForEachLoop_Statement, gen_java_ForEachLoop_StatementContainer, gen_java_Statement_Commentable, gen_java_SwitchCase_StatementListContainer, gen_java_Jump_Statement, gen_java_Condition_Statement, gen_java_Condition_StatementContainer, gen_java_JumpLabel_Statement, gen_java_Condition_Conditional, gen_java_JumpLabel_StatementContainer, gen_java_JumpLabel_NamedElement, gen_java_Continue_Jump, gen_java_DefaultSwitchCase_SwitchCase, gen_java_DoWhileLoop_WhileLoop, gen_java_EmptyStatement_Statement, gen_java_ExpressionStatement_Statement, gen_java_ForLoop_Statement, gen_java_ForLoop_StatementContainer, gen_java_ForLoop_Conditional, gen_java_Throw_Statement, gen_java_TryBlock_Statement, gen_java_TryBlock_StatementListContainer, gen_java_WhileLoop_Statement, gen_java_WhileLoop_StatementContainer, gen_java_LocalVariableStatement_Statement, gen_java_NormalSwitchCase_SwitchCase, gen_java_NormalSwitchCase_Conditional, gen_java_Return_Statement, gen_java_Switch_Statement, gen_java_SynchronizedBlock_Statement, gen_java_SynchronizedBlock_StatementListContainer, gen_java_TypeReference_Commentable, gen_java_ClassifierReference_TypeReference, gen_java_ClassifierReference_TypeArgumentable, gen_java_NamespaceClassifierReference_TypeReference, gen_java_NamespaceClassifierReference_NamespaceAwareElement, gen_java_Type_Commentable, gen_java_TypedElement_Commentable, gen_java_Void_PrimitiveType, gen_java_PackageReference_ReferenceableElement, gen_java_Variable_NamedElement, gen_java_Variable_TypedElement, gen_java_Variable_ArrayTypeable, gen_java_Variable_ReferenceableElement, gen_java_Variable_TypeArgumentable, gen_java_PrimitiveType_Type, gen_java_PrimitiveType_TypeReference, gen_java_Boolean_PrimitiveType, gen_java_Byte_PrimitiveType, gen_java_Char_PrimitiveType, gen_java_Double_PrimitiveType, gen_java_Float_PrimitiveType, gen_java_Int_PrimitiveType, gen_java_Long_PrimitiveType, gen_java_Short_PrimitiveType, gen_java_LocalVariable_Variable, gen_java_LocalVariable_Initializable, gen_java_LocalVariable_ForLoopInitializer, gen_java_LocalVariable_AnnotableAndModifiable, gen_java_AdditionalLocalVariable_ReferenceableElement, gen_java_AdditionalLocalVariable_ArrayTypeable, gen_java_AdditionalLocalVariable_Initializable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)