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
simTL4J_annotations_Annotable = Class(name="simTL4J::annotations::Annotable", is_abstract=True)
Commentable = Class(name="Commentable")
simTL4J_annotations_AnnotationInstance = Class(name="simTL4J::annotations::AnnotationInstance")
references_Reference = Class(name="references::Reference")
modifiers_AnnotationInstanceOrModifier = Class(name="modifiers::AnnotationInstanceOrModifier")
commons_NamespaceAwareElement = Class(name="commons::NamespaceAwareElement")
Classifier = Class(name="Classifier")
AnnotationParameter = Class(name="AnnotationParameter")
simTL4J_annotations_AnnotationParameter = Class(name="simTL4J::annotations::AnnotationParameter", is_abstract=True)
simTL4J_annotations_SingleAnnotationParameter = Class(name="simTL4J::annotations::SingleAnnotationParameter")
AnnotationValue = Class(name="AnnotationValue")
simTL4J_annotations_AnnotationParameterList = Class(name="simTL4J::annotations::AnnotationParameterList")
AnnotationInstance = Class(name="AnnotationInstance")
simTL4J_annotations_AnnotationAttributeSetting = Class(name="simTL4J::annotations::AnnotationAttributeSetting")
InterfaceMethod = Class(name="InterfaceMethod")
simTL4J_annotations_AnnotationValue = Class(name="simTL4J::annotations::AnnotationValue", is_abstract=True)
AnnotationAttributeSetting = Class(name="AnnotationAttributeSetting")
simTL4J_arrays_ArrayTypeable = Class(name="simTL4J::arrays::ArrayTypeable", is_abstract=True)
ArrayDimension = Class(name="ArrayDimension")
simTL4J_annotations_AnnotationAttribute = Class(name="simTL4J::annotations::AnnotationAttribute")
Expression = Class(name="Expression")
types_TypedElement = Class(name="types::TypedElement")
arrays_ArrayTypeable = Class(name="arrays::ArrayTypeable")
simTL4J_arrays_ArrayInstantiationByValues = Class(name="simTL4J::arrays::ArrayInstantiationByValues")
ArrayInitializer = Class(name="ArrayInitializer")
simTL4J_arrays_ArraySelector = Class(name="simTL4J::arrays::ArraySelector")
simTL4J_classifiers_Classifier = Class(name="simTL4J::classifiers::Classifier", is_abstract=True)
types_Type = Class(name="types::Type")
references_ReferenceableElement = Class(name="references::ReferenceableElement")
simTL4J_arrays_ArrayDimension = Class(name="simTL4J::arrays::ArrayDimension")
simTL4J_arrays_ArrayInitializer = Class(name="simTL4J::arrays::ArrayInitializer")
arrays_ArrayInitializationValue = Class(name="arrays::ArrayInitializationValue")
annotations_AnnotationValue = Class(name="annotations::AnnotationValue")
ArrayInitializationValue = Class(name="ArrayInitializationValue")
simTL4J_arrays_ArrayInitializationValue = Class(name="simTL4J::arrays::ArrayInitializationValue", is_abstract=True)
simTL4J_arrays_ArrayInstantiationBySize = Class(name="simTL4J::arrays::ArrayInstantiationBySize")
expressions_Expression = Class(name="expressions::Expression")
simTL4J_classifiers_Implementor = Class(name="simTL4J::classifiers::Implementor", is_abstract=True)
TypeReference = Class(name="TypeReference")
simTL4J_classifiers_ConcreteClassifier = Class(name="simTL4J::classifiers::ConcreteClassifier", is_abstract=True)
classifiers_Classifier = Class(name="classifiers::Classifier")
generics_TypeParametrizable = Class(name="generics::TypeParametrizable")
members_MemberContainer = Class(name="members::MemberContainer")
members_Member = Class(name="members::Member")
statements_Statement = Class(name="statements::Statement")
modifiers_AnnotableAndModifiable = Class(name="modifiers::AnnotableAndModifiable")
simTL4J_classifiers_Interface = Class(name="simTL4J::classifiers::Interface")
ConcreteClassifier = Class(name="ConcreteClassifier")
simTL4J_classifiers_Enumeration = Class(name="simTL4J::classifiers::Enumeration")
simTL4J_classifiers_Class = Class(name="simTL4J::classifiers::Class")
classifiers_ConcreteClassifier = Class(name="classifiers::ConcreteClassifier")
classifiers_Implementor = Class(name="classifiers::Implementor")
simTL4J_classifiers_AnonymousClass = Class(name="simTL4J::classifiers::AnonymousClass")
simTL4J_commons_Commentable = Class(name="simTL4J::commons::Commentable", is_abstract=True)
EnumConstant = Class(name="EnumConstant")
simTL4J_classifiers_Annotation = Class(name="simTL4J::classifiers::Annotation")
simTL4J_commons_NamedElement = Class(name="simTL4J::commons::NamedElement", is_abstract=True)
TPlaceholder = Class(name="TPlaceholder")
simTL4J_commons_NamespaceAwareElement = Class(name="simTL4J::commons::NamespaceAwareElement", is_abstract=True)
simTL4J_containers_JavaRoot = Class(name="simTL4J::containers::JavaRoot", is_abstract=True)
commons_NamedElement = Class(name="commons::NamedElement")
imports_ImportingElement = Class(name="imports::ImportingElement")
simTL4J_containers_CompilationUnit = Class(name="simTL4J::containers::CompilationUnit")
JavaRoot = Class(name="JavaRoot")
simTL4J_containers_EmptyModel = Class(name="simTL4J::containers::EmptyModel")
simTL4J_expressions_ExpressionList = Class(name="simTL4J::expressions::ExpressionList")
ForLoopInitializer = Class(name="ForLoopInitializer")
simTL4J_expressions_Expression = Class(name="simTL4J::expressions::Expression", is_abstract=True)
simTL4J_expressions_AssignmentExpression = Class(name="simTL4J::expressions::AssignmentExpression")
AssignmentExpressionChild = Class(name="AssignmentExpressionChild")
AssignmentOperator = Class(name="AssignmentOperator")
simTL4J_expressions_AssignmentExpressionChild = Class(name="simTL4J::expressions::AssignmentExpressionChild", is_abstract=True)
simTL4J_expressions_ConditionalExpression = Class(name="simTL4J::expressions::ConditionalExpression")
ConditionalExpressionChild = Class(name="ConditionalExpressionChild")
simTL4J_containers_Package = Class(name="simTL4J::containers::Package")
containers_JavaRoot = Class(name="containers::JavaRoot")
annotations_Annotable = Class(name="annotations::Annotable")
CompilationUnit = Class(name="CompilationUnit")
Package = Class(name="Package")
ConditionalAndExpressionChild = Class(name="ConditionalAndExpressionChild")
simTL4J_expressions_ConditionalAndExpressionChild = Class(name="simTL4J::expressions::ConditionalAndExpressionChild", is_abstract=True)
simTL4J_expressions_InclusiveOrExpression = Class(name="simTL4J::expressions::InclusiveOrExpression")
InclusiveOrExpressionChild = Class(name="InclusiveOrExpressionChild")
simTL4J_expressions_InclusiveOrExpressionChild = Class(name="simTL4J::expressions::InclusiveOrExpressionChild", is_abstract=True)
simTL4J_expressions_ExclusiveOrExpression = Class(name="simTL4J::expressions::ExclusiveOrExpression")
ExclusiveOrExpressionChild = Class(name="ExclusiveOrExpressionChild")
simTL4J_expressions_ExclusiveOrExpressionChild = Class(name="simTL4J::expressions::ExclusiveOrExpressionChild", is_abstract=True)
simTL4J_expressions_AndExpression = Class(name="simTL4J::expressions::AndExpression")
AndExpressionChild = Class(name="AndExpressionChild")
simTL4J_expressions_AndExpressionChild = Class(name="simTL4J::expressions::AndExpressionChild", is_abstract=True)
simTL4J_expressions_EqualityExpression = Class(name="simTL4J::expressions::EqualityExpression")
EqualityOperator = Class(name="EqualityOperator")
EqualityExpressionChild = Class(name="EqualityExpressionChild")
simTL4J_expressions_EqualityExpressionChild = Class(name="simTL4J::expressions::EqualityExpressionChild", is_abstract=True)
simTL4J_expressions_InstanceOfExpression = Class(name="simTL4J::expressions::InstanceOfExpression")
expressions_EqualityExpressionChild = Class(name="expressions::EqualityExpressionChild")
InstanceOfExpressionChild = Class(name="InstanceOfExpressionChild")
simTL4J_expressions_InstanceOfExpressionChild = Class(name="simTL4J::expressions::InstanceOfExpressionChild", is_abstract=True)
simTL4J_expressions_ConditionalExpressionChild = Class(name="simTL4J::expressions::ConditionalExpressionChild", is_abstract=True)
simTL4J_expressions_ConditionalOrExpression = Class(name="simTL4J::expressions::ConditionalOrExpression")
ConditionalOrExpressionChild = Class(name="ConditionalOrExpressionChild")
simTL4J_expressions_ConditionalOrExpressionChild = Class(name="simTL4J::expressions::ConditionalOrExpressionChild", is_abstract=True)
simTL4J_expressions_ConditionalAndExpression = Class(name="simTL4J::expressions::ConditionalAndExpression")
ShiftExpressionChild = Class(name="ShiftExpressionChild")
ShiftOperator = Class(name="ShiftOperator")
simTL4J_expressions_ShiftExpressionChild = Class(name="simTL4J::expressions::ShiftExpressionChild", is_abstract=True)
simTL4J_expressions_AdditiveExpression = Class(name="simTL4J::expressions::AdditiveExpression")
AdditiveExpressionChild = Class(name="AdditiveExpressionChild")
AdditiveOperator = Class(name="AdditiveOperator")
simTL4J_expressions_AdditiveExpressionChild = Class(name="simTL4J::expressions::AdditiveExpressionChild", is_abstract=True)
simTL4J_expressions_MultiplicativeExpression = Class(name="simTL4J::expressions::MultiplicativeExpression")
MultiplicativeExpressionChild = Class(name="MultiplicativeExpressionChild")
MultiplicativeOperator = Class(name="MultiplicativeOperator")
simTL4J_expressions_MultiplicativeExpressionChild = Class(name="simTL4J::expressions::MultiplicativeExpressionChild", is_abstract=True)
simTL4J_expressions_UnaryExpression = Class(name="simTL4J::expressions::UnaryExpression")
simTL4J_expressions_RelationExpression = Class(name="simTL4J::expressions::RelationExpression")
RelationExpressionChild = Class(name="RelationExpressionChild")
RelationOperator = Class(name="RelationOperator")
simTL4J_expressions_RelationExpressionChild = Class(name="simTL4J::expressions::RelationExpressionChild", is_abstract=True)
simTL4J_expressions_ShiftExpression = Class(name="simTL4J::expressions::ShiftExpression")
UnaryModificationExpressionChild = Class(name="UnaryModificationExpressionChild")
UnaryModificationOperator = Class(name="UnaryModificationOperator")
simTL4J_expressions_PrefixUnaryModificationExpression = Class(name="simTL4J::expressions::PrefixUnaryModificationExpression")
UnaryModificationExpression = Class(name="UnaryModificationExpression")
simTL4J_expressions_SuffixUnaryModificationExpression = Class(name="simTL4J::expressions::SuffixUnaryModificationExpression")
simTL4J_expressions_UnaryModificationExpressionChild = Class(name="simTL4J::expressions::UnaryModificationExpressionChild", is_abstract=True)
simTL4J_expressions_CastExpression = Class(name="simTL4J::expressions::CastExpression")
expressions_UnaryModificationExpressionChild = Class(name="expressions::UnaryModificationExpressionChild")
simTL4J_expressions_PrimaryExpression = Class(name="simTL4J::expressions::PrimaryExpression", is_abstract=True)
simTL4J_expressions_NestedExpression = Class(name="simTL4J::expressions::NestedExpression")
Reference = Class(name="Reference")
UnaryOperator = Class(name="UnaryOperator")
UnaryExpressionChild = Class(name="UnaryExpressionChild")
simTL4J_expressions_UnaryExpressionChild = Class(name="simTL4J::expressions::UnaryExpressionChild", is_abstract=True)
simTL4J_expressions_UnaryModificationExpression = Class(name="simTL4J::expressions::UnaryModificationExpression", is_abstract=True)
simTL4J_generics_TypeParametrizable = Class(name="simTL4J::generics::TypeParametrizable", is_abstract=True)
TypeParameter = Class(name="TypeParameter")
simTL4J_generics_ExtendsTypeArgument = Class(name="simTL4J::generics::ExtendsTypeArgument")
simTL4J_generics_QualifiedTypeArgument = Class(name="simTL4J::generics::QualifiedTypeArgument")
generics_TypeArgument = Class(name="generics::TypeArgument")
simTL4J_generics_SuperTypeArgument = Class(name="simTL4J::generics::SuperTypeArgument")
simTL4J_generics_TypeParameter = Class(name="simTL4J::generics::TypeParameter")
simTL4J_generics_TypeArgument = Class(name="simTL4J::generics::TypeArgument", is_abstract=True)
ArrayTypeable = Class(name="ArrayTypeable")
simTL4J_generics_TypeArgumentable = Class(name="simTL4J::generics::TypeArgumentable", is_abstract=True)
TypeArgument = Class(name="TypeArgument")
simTL4J_generics_CallTypeArgumentable = Class(name="simTL4J::generics::CallTypeArgumentable", is_abstract=True)
simTL4J_imports_Import = Class(name="simTL4J::imports::Import", is_abstract=True)
NamespaceAwareElement = Class(name="NamespaceAwareElement")
simTL4J_imports_ImportingElement = Class(name="simTL4J::imports::ImportingElement", is_abstract=True)
Import = Class(name="Import")
simTL4J_imports_StaticImport = Class(name="simTL4J::imports::StaticImport", is_abstract=True)
Static = Class(name="Static")
simTL4J_generics_UnknownTypeArgument = Class(name="simTL4J::generics::UnknownTypeArgument")
simTL4J_imports_PackageImport = Class(name="simTL4J::imports::PackageImport")
simTL4J_imports_StaticClassifierImport = Class(name="simTL4J::imports::StaticClassifierImport")
StaticImport = Class(name="StaticImport")
simTL4J_imports_StaticMemberImport = Class(name="simTL4J::imports::StaticMemberImport")
ReferenceableElement = Class(name="ReferenceableElement")
simTL4J_instantiations_Initializable = Class(name="simTL4J::instantiations::Initializable", is_abstract=True)
simTL4J_instantiations_Instantiation = Class(name="simTL4J::instantiations::Instantiation", is_abstract=True)
references_Argumentable = Class(name="references::Argumentable")
generics_TypeArgumentable = Class(name="generics::TypeArgumentable")
simTL4J_imports_ClassifierImport = Class(name="simTL4J::imports::ClassifierImport")
simTL4J_literals_Self = Class(name="simTL4J::literals::Self", is_abstract=True)
simTL4J_literals_BooleanLiteral = Class(name="simTL4J::literals::BooleanLiteral")
Literal = Class(name="Literal")
simTL4J_literals_CharacterLiteral = Class(name="simTL4J::literals::CharacterLiteral")
simTL4J_literals_FloatLiteral = Class(name="simTL4J::literals::FloatLiteral", is_abstract=True)
simTL4J_literals_DecimalFloatLiteral = Class(name="simTL4J::literals::DecimalFloatLiteral")
FloatLiteral = Class(name="FloatLiteral")
simTL4J_literals_HexFloatLiteral = Class(name="simTL4J::literals::HexFloatLiteral")
simTL4J_literals_DoubleLiteral = Class(name="simTL4J::literals::DoubleLiteral", is_abstract=True)
simTL4J_literals_DecimalDoubleLiteral = Class(name="simTL4J::literals::DecimalDoubleLiteral")
DoubleLiteral = Class(name="DoubleLiteral")
simTL4J_literals_HexDoubleLiteral = Class(name="simTL4J::literals::HexDoubleLiteral")
simTL4J_instantiations_NewConstructorCall = Class(name="simTL4J::instantiations::NewConstructorCall")
instantiations_Instantiation = Class(name="instantiations::Instantiation")
generics_CallTypeArgumentable = Class(name="generics::CallTypeArgumentable")
simTL4J_literals_IntegerLiteral = Class(name="simTL4J::literals::IntegerLiteral", is_abstract=True)
AnonymousClass = Class(name="AnonymousClass")
simTL4J_instantiations_ExplicitConstructorCall = Class(name="simTL4J::instantiations::ExplicitConstructorCall")
Instantiation = Class(name="Instantiation")
Self = Class(name="Self")
simTL4J_literals_Literal = Class(name="simTL4J::literals::Literal", is_abstract=True)
PrimaryExpression = Class(name="PrimaryExpression")
simTL4J_literals_OctalLongLiteral = Class(name="simTL4J::literals::OctalLongLiteral")
simTL4J_literals_NullLiteral = Class(name="simTL4J::literals::NullLiteral")
simTL4J_literals_Super = Class(name="simTL4J::literals::Super")
simTL4J_literals_This = Class(name="simTL4J::literals::This")
simTL4J_members_ExceptionThrower = Class(name="simTL4J::members::ExceptionThrower", is_abstract=True)
NamespaceClassifierReference = Class(name="NamespaceClassifierReference")
simTL4J_members_Member = Class(name="simTL4J::members::Member", is_abstract=True)
NamedElement = Class(name="NamedElement")
simTL4J_members_MemberContainer = Class(name="simTL4J::members::MemberContainer", is_abstract=True)
Member = Class(name="Member")
simTL4J_members_AdditionalField = Class(name="simTL4J::members::AdditionalField")
instantiations_Initializable = Class(name="instantiations::Initializable")
simTL4J_members_Constructor = Class(name="simTL4J::members::Constructor")
statements_StatementListContainer = Class(name="statements::StatementListContainer")
simTL4J_literals_DecimalIntegerLiteral = Class(name="simTL4J::literals::DecimalIntegerLiteral")
IntegerLiteral = Class(name="IntegerLiteral")
simTL4J_literals_HexIntegerLiteral = Class(name="simTL4J::literals::HexIntegerLiteral")
simTL4J_literals_OctalIntegerLiteral = Class(name="simTL4J::literals::OctalIntegerLiteral")
simTL4J_literals_LongLiteral = Class(name="simTL4J::literals::LongLiteral", is_abstract=True)
simTL4J_literals_DecimalLongLiteral = Class(name="simTL4J::literals::DecimalLongLiteral")
LongLiteral = Class(name="LongLiteral")
simTL4J_literals_HexLongLiteral = Class(name="simTL4J::literals::HexLongLiteral")
simTL4J_members_Method = Class(name="simTL4J::members::Method", is_abstract=True)
simTL4J_members_InterfaceMethod = Class(name="simTL4J::members::InterfaceMethod")
Method_ = Class(name="Method")
simTL4J_members_ClassMethod = Class(name="simTL4J::members::ClassMethod")
members_Method = Class(name="members::Method")
simTL4J_members_EnumConstant = Class(name="simTL4J::members::EnumConstant")
simTL4J_modifiers_Modifier = Class(name="simTL4J::modifiers::Modifier", is_abstract=True)
AnnotationInstanceOrModifier = Class(name="AnnotationInstanceOrModifier")
simTL4J_modifiers_AnnotationInstanceOrModifier = Class(name="simTL4J::modifiers::AnnotationInstanceOrModifier", is_abstract=True)
parameters_Parametrizable = Class(name="parameters::Parametrizable")
members_ExceptionThrower = Class(name="members::ExceptionThrower")
simTL4J_members_EmptyMember = Class(name="simTL4J::members::EmptyMember")
simTL4J_members_Field = Class(name="simTL4J::members::Field")
variables_Variable = Class(name="variables::Variable")
AdditionalField = Class(name="AdditionalField")
simTL4J_modifiers_Modifiable = Class(name="simTL4J::modifiers::Modifiable", is_abstract=True)
Modifier = Class(name="Modifier")
simTL4J_modifiers_Abstract = Class(name="simTL4J::modifiers::Abstract")
simTL4J_modifiers_Final = Class(name="simTL4J::modifiers::Final")
simTL4J_modifiers_Native = Class(name="simTL4J::modifiers::Native")
simTL4J_modifiers_Protected = Class(name="simTL4J::modifiers::Protected")
simTL4J_modifiers_Public = Class(name="simTL4J::modifiers::Public")
simTL4J_modifiers_Private = Class(name="simTL4J::modifiers::Private")
simTL4J_modifiers_Static = Class(name="simTL4J::modifiers::Static")
simTL4J_modifiers_Strictfp = Class(name="simTL4J::modifiers::Strictfp")
simTL4J_modifiers_Synchronized = Class(name="simTL4J::modifiers::Synchronized")
simTL4J_modifiers_Transient = Class(name="simTL4J::modifiers::Transient")
simTL4J_modifiers_Volatile = Class(name="simTL4J::modifiers::Volatile")
simTL4J_operators_Operator = Class(name="simTL4J::operators::Operator", is_abstract=True)
simTL4J_operators_AdditiveOperator = Class(name="simTL4J::operators::AdditiveOperator", is_abstract=True)
Operator = Class(name="Operator")
simTL4J_modifiers_AnnotableAndModifiable = Class(name="simTL4J::modifiers::AnnotableAndModifiable", is_abstract=True)
simTL4J_operators_UnaryModificationOperator = Class(name="simTL4J::operators::UnaryModificationOperator", is_abstract=True)
simTL4J_operators_Assignment = Class(name="simTL4J::operators::Assignment")
simTL4J_operators_AssignmentAnd = Class(name="simTL4J::operators::AssignmentAnd")
simTL4J_operators_AssignmentDivision = Class(name="simTL4J::operators::AssignmentDivision")
simTL4J_operators_AssignmentExclusiveOr = Class(name="simTL4J::operators::AssignmentExclusiveOr")
simTL4J_operators_AssignmentMinus = Class(name="simTL4J::operators::AssignmentMinus")
simTL4J_operators_AssignmentModulo = Class(name="simTL4J::operators::AssignmentModulo")
simTL4J_operators_AssignmentMultiplication = Class(name="simTL4J::operators::AssignmentMultiplication")
simTL4J_operators_AssignmentLeftShift = Class(name="simTL4J::operators::AssignmentLeftShift")
simTL4J_operators_AssignmentOr = Class(name="simTL4J::operators::AssignmentOr")
simTL4J_operators_AssignmentPlus = Class(name="simTL4J::operators::AssignmentPlus")
simTL4J_operators_AssignmentRightShift = Class(name="simTL4J::operators::AssignmentRightShift")
simTL4J_operators_AssignmentUnsignedRightShift = Class(name="simTL4J::operators::AssignmentUnsignedRightShift")
simTL4J_operators_Equal = Class(name="simTL4J::operators::Equal")
simTL4J_operators_NotEqual = Class(name="simTL4J::operators::NotEqual")
simTL4J_operators_GreaterThan = Class(name="simTL4J::operators::GreaterThan")
simTL4J_operators_GreaterThanOrEqual = Class(name="simTL4J::operators::GreaterThanOrEqual")
simTL4J_operators_LessThan = Class(name="simTL4J::operators::LessThan")
simTL4J_operators_AssignmentOperator = Class(name="simTL4J::operators::AssignmentOperator", is_abstract=True)
simTL4J_operators_EqualityOperator = Class(name="simTL4J::operators::EqualityOperator", is_abstract=True)
simTL4J_operators_MultiplicativeOperator = Class(name="simTL4J::operators::MultiplicativeOperator", is_abstract=True)
simTL4J_operators_RelationOperator = Class(name="simTL4J::operators::RelationOperator", is_abstract=True)
simTL4J_operators_ShiftOperator = Class(name="simTL4J::operators::ShiftOperator", is_abstract=True)
simTL4J_operators_UnaryOperator = Class(name="simTL4J::operators::UnaryOperator", is_abstract=True)
simTL4J_operators_Complement = Class(name="simTL4J::operators::Complement")
simTL4J_operators_MinusMinus = Class(name="simTL4J::operators::MinusMinus")
simTL4J_operators_Negate = Class(name="simTL4J::operators::Negate")
simTL4J_operators_PlusPlus = Class(name="simTL4J::operators::PlusPlus")
simTL4J_operators_LeftShift = Class(name="simTL4J::operators::LeftShift")
simTL4J_operators_RightShift = Class(name="simTL4J::operators::RightShift")
simTL4J_operators_UnsignedRightShift = Class(name="simTL4J::operators::UnsignedRightShift")
simTL4J_parameters_Parameter = Class(name="simTL4J::parameters::Parameter", is_abstract=True)
simTL4J_parameters_Parametrizable = Class(name="simTL4J::parameters::Parametrizable", is_abstract=True)
Parameter_ = Class(name="Parameter")
simTL4J_parameters_OrdinaryParameter = Class(name="simTL4J::parameters::OrdinaryParameter")
simTL4J_parameters_VariableLengthParameter = Class(name="simTL4J::parameters::VariableLengthParameter")
simTL4J_references_Reference = Class(name="simTL4J::references::Reference", is_abstract=True)
expressions_PrimaryExpression = Class(name="expressions::PrimaryExpression")
simTL4J_operators_LessThanOrEqual = Class(name="simTL4J::operators::LessThanOrEqual")
simTL4J_operators_Addition = Class(name="simTL4J::operators::Addition")
operators_AdditiveOperator = Class(name="operators::AdditiveOperator")
operators_UnaryOperator = Class(name="operators::UnaryOperator")
simTL4J_operators_Subtraction = Class(name="simTL4J::operators::Subtraction")
simTL4J_operators_Division = Class(name="simTL4J::operators::Division")
simTL4J_operators_Multiplication = Class(name="simTL4J::operators::Multiplication")
simTL4J_operators_Remainder = Class(name="simTL4J::operators::Remainder")
simTL4J_references_Argumentable = Class(name="simTL4J::references::Argumentable", is_abstract=True)
simTL4J_references_ReferenceableElement = Class(name="simTL4J::references::ReferenceableElement", is_abstract=True)
simTL4J_references_ElementReference = Class(name="simTL4J::references::ElementReference", is_abstract=True)
simTL4J_references_IdentifierReference = Class(name="simTL4J::references::IdentifierReference")
ElementReference = Class(name="ElementReference")
simTL4J_references_MethodCall = Class(name="simTL4J::references::MethodCall")
references_ElementReference = Class(name="references::ElementReference")
simTL4J_references_ReflectiveClassReference = Class(name="simTL4J::references::ReflectiveClassReference")
simTL4J_references_PrimitiveTypeReference = Class(name="simTL4J::references::PrimitiveTypeReference")
PrimitiveType = Class(name="PrimitiveType")
simTL4J_references_StringReference = Class(name="simTL4J::references::StringReference")
ArraySelector = Class(name="ArraySelector")
simTL4J_references_SelfReference = Class(name="simTL4J::references::SelfReference")
simTL4J_statements_StatementContainer = Class(name="simTL4J::statements::StatementContainer", is_abstract=True)
Statement = Class(name="Statement")
simTL4J_statements_Conditional = Class(name="simTL4J::statements::Conditional", is_abstract=True)
simTL4J_statements_ForLoopInitializer = Class(name="simTL4J::statements::ForLoopInitializer", is_abstract=True)
simTL4J_statements_Statement = Class(name="simTL4J::statements::Statement", is_abstract=True)
simTL4J_statements_SwitchCase = Class(name="simTL4J::statements::SwitchCase", is_abstract=True)
StatementListContainer = Class(name="StatementListContainer")
simTL4J_statements_Assert = Class(name="simTL4J::statements::Assert")
statements_Conditional = Class(name="statements::Conditional")
simTL4J_statements_Break = Class(name="simTL4J::statements::Break")
Jump = Class(name="Jump")
simTL4J_statements_Block = Class(name="simTL4J::statements::Block")
modifiers_Modifiable = Class(name="modifiers::Modifiable")
simTL4J_statements_CatchBlock = Class(name="simTL4J::statements::CatchBlock")
simTL4J_statements_StatementListContainer = Class(name="simTL4J::statements::StatementListContainer", is_abstract=True)
simTL4J_statements_EmptyStatement = Class(name="simTL4J::statements::EmptyStatement")
simTL4J_statements_ExpressionStatement = Class(name="simTL4J::statements::ExpressionStatement")
simTL4J_statements_ForLoop = Class(name="simTL4J::statements::ForLoop")
simTL4J_statements_ForEachLoop = Class(name="simTL4J::statements::ForEachLoop")
OrdinaryParameter = Class(name="OrdinaryParameter")
simTL4J_statements_Condition = Class(name="simTL4J::statements::Condition")
statements_StatementContainer = Class(name="statements::StatementContainer")
simTL4J_statements_Continue = Class(name="simTL4J::statements::Continue")
simTL4J_statements_DefaultSwitchCase = Class(name="simTL4J::statements::DefaultSwitchCase")
SwitchCase = Class(name="SwitchCase")
simTL4J_statements_DoWhileLoop = Class(name="simTL4J::statements::DoWhileLoop")
WhileLoop = Class(name="WhileLoop")
simTL4J_statements_Return = Class(name="simTL4J::statements::Return")
simTL4J_statements_Switch = Class(name="simTL4J::statements::Switch")
simTL4J_statements_SynchronizedBlock = Class(name="simTL4J::statements::SynchronizedBlock")
simTL4J_statements_Throw = Class(name="simTL4J::statements::Throw")
simTL4J_statements_TryBlock = Class(name="simTL4J::statements::TryBlock")
CatchBlock = Class(name="CatchBlock")
Block = Class(name="Block")
simTL4J_statements_WhileLoop = Class(name="simTL4J::statements::WhileLoop")
simTL4J_statements_Jump = Class(name="simTL4J::statements::Jump", is_abstract=True)
JumpLabel = Class(name="JumpLabel")
simTL4J_statements_JumpLabel = Class(name="simTL4J::statements::JumpLabel")
simTL4J_statements_LocalVariableStatement = Class(name="simTL4J::statements::LocalVariableStatement")
LocalVariable = Class(name="LocalVariable")
simTL4J_statements_NormalSwitchCase = Class(name="simTL4J::statements::NormalSwitchCase")
statements_SwitchCase = Class(name="statements::SwitchCase")
simTL4J_types_TypedElement = Class(name="simTL4J::types::TypedElement", is_abstract=True)
simTL4J_types_TypeReference = Class(name="simTL4J::types::TypeReference", is_abstract=True)
simTL4J_types_ClassifierReference = Class(name="simTL4J::types::ClassifierReference")
types_TypeReference = Class(name="types::TypeReference")
simTL4J_types_NamespaceClassifierReference = Class(name="simTL4J::types::NamespaceClassifierReference")
ClassifierReference = Class(name="ClassifierReference")
simTL4J_types_PrimitiveType = Class(name="simTL4J::types::PrimitiveType", is_abstract=True)
simTL4J_types_Type = Class(name="simTL4J::types::Type", is_abstract=True)
simTL4J_variables_LocalVariable = Class(name="simTL4J::variables::LocalVariable")
statements_ForLoopInitializer = Class(name="statements::ForLoopInitializer")
AdditionalLocalVariable = Class(name="AdditionalLocalVariable")
simTL4J_variables_AdditionalLocalVariable = Class(name="simTL4J::variables::AdditionalLocalVariable")
simTL4J_simTL_TIf = Class(name="simTL4J::simTL::TIf", is_abstract=True)
TAbstractMethodStatement = Class(name="TAbstractMethodStatement")
simTL4J_simTL_TFor = Class(name="simTL4J::simTL::TFor", is_abstract=True)
TForVariable = Class(name="TForVariable")
simTL4J_simTL_TForVariable = Class(name="simTL4J::simTL::TForVariable")
simTL4J_types_Boolean = Class(name="simTL4J::types::Boolean")
simTL4J_types_Byte = Class(name="simTL4J::types::Byte")
simTL4J_types_Char = Class(name="simTL4J::types::Char")
simTL4J_types_Double = Class(name="simTL4J::types::Double")
simTL4J_types_Float = Class(name="simTL4J::types::Float")
simTL4J_types_Int = Class(name="simTL4J::types::Int")
simTL4J_types_Long = Class(name="simTL4J::types::Long")
simTL4J_types_Short = Class(name="simTL4J::types::Short")
simTL4J_types_Void = Class(name="simTL4J::types::Void")
simTL4J_variables_Variable = Class(name="simTL4J::variables::Variable", is_abstract=True)
TModelImport = Class(name="TModelImport")
simTL4J_simTL_TModelImport = Class(name="simTL4J::simTL::TModelImport")
simTL4J_simTL_TMethodCall = Class(name="simTL4J::simTL::TMethodCall")
simTL4J_simTL_TAbstractMethodStatement = Class(name="simTL4J::simTL::TAbstractMethodStatement")
simTL4J_simTL_TFor_MemberContainer = Class(name="simTL4J::simTL::TFor::MemberContainer")
simTL_TFor = Class(name="simTL::TFor")
simTL4J_simTL_TFor_StatementListContainer = Class(name="simTL4J::simTL::TFor::StatementListContainer")
simTL4J_simTL_Template = Class(name="simTL4J::simTL::Template")
TemplateHeader = Class(name="TemplateHeader")
simTL4J_simTL_TemplateHeader = Class(name="simTL4J::simTL::TemplateHeader")
simTL_TIf = Class(name="simTL::TIf")
simTL4J_simTL_TIf_StatementListContainer = Class(name="simTL4J::simTL::TIf::StatementListContainer")
simTL4J_simTL_TPlaceholder = Class(name="simTL4J::simTL::TPlaceholder")
simTL4J_simTL_TPlaceholder_PrimaryExpression = Class(name="simTL4J::simTL::TPlaceholder::PrimaryExpression")
simTL_TPlaceholder = Class(name="simTL::TPlaceholder")
simTL4J_simTL_TUnaryOperator = Class(name="simTL4J::simTL::TUnaryOperator", is_abstract=True)
simTL4J_simTL_TIf_MemberContainer = Class(name="simTL4J::simTL::TIf::MemberContainer")
simTL4J_simTL_TUnaryOperatorNOT = Class(name="simTL4J::simTL::TUnaryOperatorNOT")
TUnaryOperator = Class(name="TUnaryOperator")
simTL4J_simTL_TMethodStatementImpl = Class(name="simTL4J::simTL::TMethodStatementImpl")
TMethodCall = Class(name="TMethodCall")

# simTL4J_annotations_Annotable class attributes and methods

# Commentable class attributes and methods

# simTL4J_annotations_AnnotationInstance class attributes and methods

# references_Reference class attributes and methods

# modifiers_AnnotationInstanceOrModifier class attributes and methods

# commons_NamespaceAwareElement class attributes and methods

# Classifier class attributes and methods

# AnnotationParameter class attributes and methods

# simTL4J_annotations_AnnotationParameter class attributes and methods

# simTL4J_annotations_SingleAnnotationParameter class attributes and methods

# AnnotationValue class attributes and methods

# simTL4J_annotations_AnnotationParameterList class attributes and methods

# AnnotationInstance class attributes and methods

# simTL4J_annotations_AnnotationAttributeSetting class attributes and methods

# InterfaceMethod class attributes and methods

# simTL4J_annotations_AnnotationValue class attributes and methods

# AnnotationAttributeSetting class attributes and methods

# simTL4J_arrays_ArrayTypeable class attributes and methods
simTL4J_arrays_ArrayTypeable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
simTL4J_arrays_ArrayTypeable.methods={simTL4J_arrays_ArrayTypeable_m_getArrayDimension}

# ArrayDimension class attributes and methods

# simTL4J_annotations_AnnotationAttribute class attributes and methods

# Expression class attributes and methods

# types_TypedElement class attributes and methods

# arrays_ArrayTypeable class attributes and methods

# simTL4J_arrays_ArrayInstantiationByValues class attributes and methods

# ArrayInitializer class attributes and methods

# simTL4J_arrays_ArraySelector class attributes and methods

# simTL4J_classifiers_Classifier class attributes and methods
simTL4J_classifiers_Classifier_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_Classifier.methods={simTL4J_classifiers_Classifier_m_getAllSuperClassifiers}

# types_Type class attributes and methods

# references_ReferenceableElement class attributes and methods

# simTL4J_arrays_ArrayDimension class attributes and methods

# simTL4J_arrays_ArrayInitializer class attributes and methods

# arrays_ArrayInitializationValue class attributes and methods

# annotations_AnnotationValue class attributes and methods

# ArrayInitializationValue class attributes and methods

# simTL4J_arrays_ArrayInitializationValue class attributes and methods

# simTL4J_arrays_ArrayInstantiationBySize class attributes and methods

# expressions_Expression class attributes and methods

# simTL4J_classifiers_Implementor class attributes and methods

# TypeReference class attributes and methods

# simTL4J_classifiers_ConcreteClassifier class attributes and methods
simTL4J_classifiers_ConcreteClassifier_fullName: Property = Property(name="fullName", type=StringType)
simTL4J_classifiers_ConcreteClassifier_m_getAllInnerClassifiers: Method = Method(name="getAllInnerClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_ConcreteClassifier_m_getSuperTypeReferences: Method = Method(name="getSuperTypeReferences", parameters={}, type=StringType)
simTL4J_classifiers_ConcreteClassifier_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=StringType)
simTL4J_classifiers_ConcreteClassifier_m_getInnerClassifiers: Method = Method(name="getInnerClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_ConcreteClassifier.attributes={simTL4J_classifiers_ConcreteClassifier_fullName}
simTL4J_classifiers_ConcreteClassifier.methods={simTL4J_classifiers_ConcreteClassifier_m_getAllInnerClassifiers, simTL4J_classifiers_ConcreteClassifier_m_getInnerClassifiers, simTL4J_classifiers_ConcreteClassifier_m_getAllMembers, simTL4J_classifiers_ConcreteClassifier_m_getSuperTypeReferences}

# classifiers_Classifier class attributes and methods

# generics_TypeParametrizable class attributes and methods

# members_MemberContainer class attributes and methods

# members_Member class attributes and methods

# statements_Statement class attributes and methods

# modifiers_AnnotableAndModifiable class attributes and methods

# simTL4J_classifiers_Interface class attributes and methods
simTL4J_classifiers_Interface_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_Interface.methods={simTL4J_classifiers_Interface_m_getAllSuperClassifiers}

# ConcreteClassifier class attributes and methods

# simTL4J_classifiers_Enumeration class attributes and methods
simTL4J_classifiers_Enumeration_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_Enumeration.methods={simTL4J_classifiers_Enumeration_m_getAllSuperClassifiers}

# simTL4J_classifiers_Class class attributes and methods
simTL4J_classifiers_Class_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_Class_m_getSuperClass: Method = Method(name="getSuperClass", parameters={}, type=StringType)
simTL4J_classifiers_Class_m_unWrapPrimitiveType: Method = Method(name="unWrapPrimitiveType", parameters={}, type=StringType)
simTL4J_classifiers_Class.methods={simTL4J_classifiers_Class_m_unWrapPrimitiveType, simTL4J_classifiers_Class_m_getSuperClass, simTL4J_classifiers_Class_m_getAllSuperClassifiers}

# classifiers_ConcreteClassifier class attributes and methods

# classifiers_Implementor class attributes and methods

# simTL4J_classifiers_AnonymousClass class attributes and methods
simTL4J_classifiers_AnonymousClass_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_AnonymousClass_m_getSuperClassifier: Method = Method(name="getSuperClassifier", parameters={}, type=StringType)
simTL4J_classifiers_AnonymousClass_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=StringType)
simTL4J_classifiers_AnonymousClass.methods={simTL4J_classifiers_AnonymousClass_m_getAllSuperClassifiers, simTL4J_classifiers_AnonymousClass_m_getSuperClassifier, simTL4J_classifiers_AnonymousClass_m_getAllMembers}

# simTL4J_commons_Commentable class attributes and methods
simTL4J_commons_Commentable_comments: Property = Property(name="comments", type=StringType)
simTL4J_commons_Commentable_m_getConcreteClassifier: Method = Method(name="getConcreteClassifier", parameters={Parameter(name='name')}, type=StringType)
simTL4J_commons_Commentable_m_getClassClass: Method = Method(name="getClassClass", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getObjectClass: Method = Method(name="getObjectClass", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getStringClass: Method = Method(name="getStringClass", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getAnnotationInterface: Method = Method(name="getAnnotationInterface", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getContainingAnnotationInstance: Method = Method(name="getContainingAnnotationInstance", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getContainingAnonymousClass: Method = Method(name="getContainingAnonymousClass", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getConcreteClassifiers: Method = Method(name="getConcreteClassifiers", parameters={Parameter(name='packageName'), Parameter(name='classifierQuery')}, type=StringType)
simTL4J_commons_Commentable_m_getLibClass: Method = Method(name="getLibClass", parameters={Parameter(name='name')}, type=StringType)
simTL4J_commons_Commentable_m_getLibInterface: Method = Method(name="getLibInterface", parameters={Parameter(name='name')}, type=StringType)
simTL4J_commons_Commentable_m_getContainingConcreteClassifier: Method = Method(name="getContainingConcreteClassifier", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getContainingCompilationUnit: Method = Method(name="getContainingCompilationUnit", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getContainingPackageName: Method = Method(name="getContainingPackageName", parameters={}, type=StringType)
simTL4J_commons_Commentable_m_getParentConcreteClassifier: Method = Method(name="getParentConcreteClassifier", parameters={}, type=StringType)
simTL4J_commons_Commentable.attributes={simTL4J_commons_Commentable_comments}
simTL4J_commons_Commentable.methods={simTL4J_commons_Commentable_m_getContainingAnnotationInstance, simTL4J_commons_Commentable_m_getParentConcreteClassifier, simTL4J_commons_Commentable_m_getLibInterface, simTL4J_commons_Commentable_m_getClassClass, simTL4J_commons_Commentable_m_getContainingCompilationUnit, simTL4J_commons_Commentable_m_getContainingConcreteClassifier, simTL4J_commons_Commentable_m_getObjectClass, simTL4J_commons_Commentable_m_getLibClass, simTL4J_commons_Commentable_m_getAnnotationInterface, simTL4J_commons_Commentable_m_getContainingPackageName, simTL4J_commons_Commentable_m_getConcreteClassifier, simTL4J_commons_Commentable_m_getStringClass, simTL4J_commons_Commentable_m_getContainingAnonymousClass, simTL4J_commons_Commentable_m_getConcreteClassifiers}

# EnumConstant class attributes and methods

# simTL4J_classifiers_Annotation class attributes and methods
simTL4J_classifiers_Annotation_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
simTL4J_classifiers_Annotation.methods={simTL4J_classifiers_Annotation_m_getAllSuperClassifiers}

# simTL4J_commons_NamedElement class attributes and methods
simTL4J_commons_NamedElement_name: Property = Property(name="name", type=StringType)
simTL4J_commons_NamedElement.attributes={simTL4J_commons_NamedElement_name}

# TPlaceholder class attributes and methods

# simTL4J_commons_NamespaceAwareElement class attributes and methods
simTL4J_commons_NamespaceAwareElement_namespaces: Property = Property(name="namespaces", type=StringType)
simTL4J_commons_NamespaceAwareElement_m_getNamespacesAsString: Method = Method(name="getNamespacesAsString", parameters={}, type=StringType)
simTL4J_commons_NamespaceAwareElement_m_getClassifierAtNamespaces: Method = Method(name="getClassifierAtNamespaces", parameters={}, type=StringType)
simTL4J_commons_NamespaceAwareElement.attributes={simTL4J_commons_NamespaceAwareElement_namespaces}
simTL4J_commons_NamespaceAwareElement.methods={simTL4J_commons_NamespaceAwareElement_m_getNamespacesAsString, simTL4J_commons_NamespaceAwareElement_m_getClassifierAtNamespaces}

# simTL4J_containers_JavaRoot class attributes and methods
simTL4J_containers_JavaRoot_m_getClassifiersInSamePackage: Method = Method(name="getClassifiersInSamePackage", parameters={}, type=StringType)
simTL4J_containers_JavaRoot.methods={simTL4J_containers_JavaRoot_m_getClassifiersInSamePackage}

# commons_NamedElement class attributes and methods

# imports_ImportingElement class attributes and methods

# simTL4J_containers_CompilationUnit class attributes and methods
simTL4J_containers_CompilationUnit_m_getContainedClassifier: Method = Method(name="getContainedClassifier", parameters={Parameter(name='name')}, type=StringType)
simTL4J_containers_CompilationUnit_m_getClassifiersInSamePackage: Method = Method(name="getClassifiersInSamePackage", parameters={}, type=StringType)
simTL4J_containers_CompilationUnit.methods={simTL4J_containers_CompilationUnit_m_getClassifiersInSamePackage, simTL4J_containers_CompilationUnit_m_getContainedClassifier}

# JavaRoot class attributes and methods

# simTL4J_containers_EmptyModel class attributes and methods

# simTL4J_expressions_ExpressionList class attributes and methods

# ForLoopInitializer class attributes and methods

# simTL4J_expressions_Expression class attributes and methods
simTL4J_expressions_Expression_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
simTL4J_expressions_Expression_m_getAlternativeType: Method = Method(name="getAlternativeType", parameters={}, type=StringType)
simTL4J_expressions_Expression_m_getOneType: Method = Method(name="getOneType", parameters={Parameter(name='alternative')}, type=StringType)
simTL4J_expressions_Expression_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
simTL4J_expressions_Expression.methods={simTL4J_expressions_Expression_m_getType, simTL4J_expressions_Expression_m_getOneType, simTL4J_expressions_Expression_m_getArrayDimension, simTL4J_expressions_Expression_m_getAlternativeType}

# simTL4J_expressions_AssignmentExpression class attributes and methods

# AssignmentExpressionChild class attributes and methods

# AssignmentOperator class attributes and methods

# simTL4J_expressions_AssignmentExpressionChild class attributes and methods

# simTL4J_expressions_ConditionalExpression class attributes and methods

# ConditionalExpressionChild class attributes and methods

# simTL4J_containers_Package class attributes and methods

# containers_JavaRoot class attributes and methods

# annotations_Annotable class attributes and methods

# CompilationUnit class attributes and methods

# Package class attributes and methods

# ConditionalAndExpressionChild class attributes and methods

# simTL4J_expressions_ConditionalAndExpressionChild class attributes and methods

# simTL4J_expressions_InclusiveOrExpression class attributes and methods

# InclusiveOrExpressionChild class attributes and methods

# simTL4J_expressions_InclusiveOrExpressionChild class attributes and methods

# simTL4J_expressions_ExclusiveOrExpression class attributes and methods

# ExclusiveOrExpressionChild class attributes and methods

# simTL4J_expressions_ExclusiveOrExpressionChild class attributes and methods

# simTL4J_expressions_AndExpression class attributes and methods

# AndExpressionChild class attributes and methods

# simTL4J_expressions_AndExpressionChild class attributes and methods

# simTL4J_expressions_EqualityExpression class attributes and methods

# EqualityOperator class attributes and methods

# EqualityExpressionChild class attributes and methods

# simTL4J_expressions_EqualityExpressionChild class attributes and methods

# simTL4J_expressions_InstanceOfExpression class attributes and methods

# expressions_EqualityExpressionChild class attributes and methods

# InstanceOfExpressionChild class attributes and methods

# simTL4J_expressions_InstanceOfExpressionChild class attributes and methods

# simTL4J_expressions_ConditionalExpressionChild class attributes and methods

# simTL4J_expressions_ConditionalOrExpression class attributes and methods

# ConditionalOrExpressionChild class attributes and methods

# simTL4J_expressions_ConditionalOrExpressionChild class attributes and methods

# simTL4J_expressions_ConditionalAndExpression class attributes and methods

# ShiftExpressionChild class attributes and methods

# ShiftOperator class attributes and methods

# simTL4J_expressions_ShiftExpressionChild class attributes and methods

# simTL4J_expressions_AdditiveExpression class attributes and methods

# AdditiveExpressionChild class attributes and methods

# AdditiveOperator class attributes and methods

# simTL4J_expressions_AdditiveExpressionChild class attributes and methods

# simTL4J_expressions_MultiplicativeExpression class attributes and methods

# MultiplicativeExpressionChild class attributes and methods

# MultiplicativeOperator class attributes and methods

# simTL4J_expressions_MultiplicativeExpressionChild class attributes and methods

# simTL4J_expressions_UnaryExpression class attributes and methods

# simTL4J_expressions_RelationExpression class attributes and methods

# RelationExpressionChild class attributes and methods

# RelationOperator class attributes and methods

# simTL4J_expressions_RelationExpressionChild class attributes and methods

# simTL4J_expressions_ShiftExpression class attributes and methods

# UnaryModificationExpressionChild class attributes and methods

# UnaryModificationOperator class attributes and methods

# simTL4J_expressions_PrefixUnaryModificationExpression class attributes and methods

# UnaryModificationExpression class attributes and methods

# simTL4J_expressions_SuffixUnaryModificationExpression class attributes and methods

# simTL4J_expressions_UnaryModificationExpressionChild class attributes and methods

# simTL4J_expressions_CastExpression class attributes and methods

# expressions_UnaryModificationExpressionChild class attributes and methods

# simTL4J_expressions_PrimaryExpression class attributes and methods

# simTL4J_expressions_NestedExpression class attributes and methods

# Reference class attributes and methods

# UnaryOperator class attributes and methods

# UnaryExpressionChild class attributes and methods

# simTL4J_expressions_UnaryExpressionChild class attributes and methods

# simTL4J_expressions_UnaryModificationExpression class attributes and methods

# simTL4J_generics_TypeParametrizable class attributes and methods

# TypeParameter class attributes and methods

# simTL4J_generics_ExtendsTypeArgument class attributes and methods

# simTL4J_generics_QualifiedTypeArgument class attributes and methods

# generics_TypeArgument class attributes and methods

# simTL4J_generics_SuperTypeArgument class attributes and methods

# simTL4J_generics_TypeParameter class attributes and methods
simTL4J_generics_TypeParameter_m_getAllSuperClassifiers: Method = Method(name="getAllSuperClassifiers", parameters={}, type=StringType)
simTL4J_generics_TypeParameter_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=StringType)
simTL4J_generics_TypeParameter_m_getBoundType: Method = Method(name="getBoundType", parameters={Parameter(name='typeReference'), Parameter(name='reference')}, type=StringType)
simTL4J_generics_TypeParameter.methods={simTL4J_generics_TypeParameter_m_getAllSuperClassifiers, simTL4J_generics_TypeParameter_m_getBoundType, simTL4J_generics_TypeParameter_m_getAllMembers}

# simTL4J_generics_TypeArgument class attributes and methods

# ArrayTypeable class attributes and methods

# simTL4J_generics_TypeArgumentable class attributes and methods

# TypeArgument class attributes and methods

# simTL4J_generics_CallTypeArgumentable class attributes and methods

# simTL4J_imports_Import class attributes and methods
simTL4J_imports_Import_m_getImportedClassifier: Method = Method(name="getImportedClassifier", parameters={Parameter(name='name')}, type=StringType)
simTL4J_imports_Import_m_getImportedClassifiers: Method = Method(name="getImportedClassifiers", parameters={}, type=StringType)
simTL4J_imports_Import_m_getImportedMembers: Method = Method(name="getImportedMembers", parameters={}, type=StringType)
simTL4J_imports_Import.methods={simTL4J_imports_Import_m_getImportedClassifier, simTL4J_imports_Import_m_getImportedClassifiers, simTL4J_imports_Import_m_getImportedMembers}

# NamespaceAwareElement class attributes and methods

# simTL4J_imports_ImportingElement class attributes and methods
simTL4J_imports_ImportingElement_m_getDefaultImports: Method = Method(name="getDefaultImports", parameters={}, type=StringType)
simTL4J_imports_ImportingElement.methods={simTL4J_imports_ImportingElement_m_getDefaultImports}

# Import class attributes and methods

# simTL4J_imports_StaticImport class attributes and methods

# Static class attributes and methods

# simTL4J_generics_UnknownTypeArgument class attributes and methods

# simTL4J_imports_PackageImport class attributes and methods

# simTL4J_imports_StaticClassifierImport class attributes and methods

# StaticImport class attributes and methods

# simTL4J_imports_StaticMemberImport class attributes and methods

# ReferenceableElement class attributes and methods

# simTL4J_instantiations_Initializable class attributes and methods

# simTL4J_instantiations_Instantiation class attributes and methods

# references_Argumentable class attributes and methods

# generics_TypeArgumentable class attributes and methods

# simTL4J_imports_ClassifierImport class attributes and methods

# simTL4J_literals_Self class attributes and methods

# simTL4J_literals_BooleanLiteral class attributes and methods
simTL4J_literals_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
simTL4J_literals_BooleanLiteral.attributes={simTL4J_literals_BooleanLiteral_value}

# Literal class attributes and methods

# simTL4J_literals_CharacterLiteral class attributes and methods
simTL4J_literals_CharacterLiteral_value: Property = Property(name="value", type=StringType)
simTL4J_literals_CharacterLiteral.attributes={simTL4J_literals_CharacterLiteral_value}

# simTL4J_literals_FloatLiteral class attributes and methods

# simTL4J_literals_DecimalFloatLiteral class attributes and methods
simTL4J_literals_DecimalFloatLiteral_decimalValue: Property = Property(name="decimalValue", type=FloatType)
simTL4J_literals_DecimalFloatLiteral.attributes={simTL4J_literals_DecimalFloatLiteral_decimalValue}

# FloatLiteral class attributes and methods

# simTL4J_literals_HexFloatLiteral class attributes and methods
simTL4J_literals_HexFloatLiteral_hexValue: Property = Property(name="hexValue", type=FloatType)
simTL4J_literals_HexFloatLiteral.attributes={simTL4J_literals_HexFloatLiteral_hexValue}

# simTL4J_literals_DoubleLiteral class attributes and methods

# simTL4J_literals_DecimalDoubleLiteral class attributes and methods
simTL4J_literals_DecimalDoubleLiteral_decimalValue: Property = Property(name="decimalValue", type=FloatType)
simTL4J_literals_DecimalDoubleLiteral.attributes={simTL4J_literals_DecimalDoubleLiteral_decimalValue}

# DoubleLiteral class attributes and methods

# simTL4J_literals_HexDoubleLiteral class attributes and methods
simTL4J_literals_HexDoubleLiteral_hexValue: Property = Property(name="hexValue", type=FloatType)
simTL4J_literals_HexDoubleLiteral.attributes={simTL4J_literals_HexDoubleLiteral_hexValue}

# simTL4J_instantiations_NewConstructorCall class attributes and methods

# instantiations_Instantiation class attributes and methods

# generics_CallTypeArgumentable class attributes and methods

# simTL4J_literals_IntegerLiteral class attributes and methods

# AnonymousClass class attributes and methods

# simTL4J_instantiations_ExplicitConstructorCall class attributes and methods

# Instantiation class attributes and methods

# Self class attributes and methods

# simTL4J_literals_Literal class attributes and methods
simTL4J_literals_Literal_m_getOneType: Method = Method(name="getOneType", parameters={Parameter(name='alternative')}, type=StringType)
simTL4J_literals_Literal.methods={simTL4J_literals_Literal_m_getOneType}

# PrimaryExpression class attributes and methods

# simTL4J_literals_OctalLongLiteral class attributes and methods
simTL4J_literals_OctalLongLiteral_octalValue: Property = Property(name="octalValue", type=StringType)
simTL4J_literals_OctalLongLiteral.attributes={simTL4J_literals_OctalLongLiteral_octalValue}

# simTL4J_literals_NullLiteral class attributes and methods

# simTL4J_literals_Super class attributes and methods

# simTL4J_literals_This class attributes and methods

# simTL4J_members_ExceptionThrower class attributes and methods

# NamespaceClassifierReference class attributes and methods

# simTL4J_members_Member class attributes and methods

# NamedElement class attributes and methods

# simTL4J_members_MemberContainer class attributes and methods
simTL4J_members_MemberContainer_m_getContainedClassifier: Method = Method(name="getContainedClassifier", parameters={Parameter(name='name')}, type=StringType)
simTL4J_members_MemberContainer_m_getContainedField: Method = Method(name="getContainedField", parameters={Parameter(name='name')}, type=StringType)
simTL4J_members_MemberContainer_m_getContainedMethod: Method = Method(name="getContainedMethod", parameters={Parameter(name='name')}, type=StringType)
simTL4J_members_MemberContainer.methods={simTL4J_members_MemberContainer_m_getContainedField, simTL4J_members_MemberContainer_m_getContainedClassifier, simTL4J_members_MemberContainer_m_getContainedMethod}

# Member class attributes and methods

# simTL4J_members_AdditionalField class attributes and methods
simTL4J_members_AdditionalField_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
simTL4J_members_AdditionalField.methods={simTL4J_members_AdditionalField_m_getArrayDimension}

# instantiations_Initializable class attributes and methods

# simTL4J_members_Constructor class attributes and methods

# statements_StatementListContainer class attributes and methods

# simTL4J_literals_DecimalIntegerLiteral class attributes and methods
simTL4J_literals_DecimalIntegerLiteral_decimalValue: Property = Property(name="decimalValue", type=StringType)
simTL4J_literals_DecimalIntegerLiteral.attributes={simTL4J_literals_DecimalIntegerLiteral_decimalValue}

# IntegerLiteral class attributes and methods

# simTL4J_literals_HexIntegerLiteral class attributes and methods
simTL4J_literals_HexIntegerLiteral_hexValue: Property = Property(name="hexValue", type=StringType)
simTL4J_literals_HexIntegerLiteral.attributes={simTL4J_literals_HexIntegerLiteral_hexValue}

# simTL4J_literals_OctalIntegerLiteral class attributes and methods
simTL4J_literals_OctalIntegerLiteral_octalValue: Property = Property(name="octalValue", type=StringType)
simTL4J_literals_OctalIntegerLiteral.attributes={simTL4J_literals_OctalIntegerLiteral_octalValue}

# simTL4J_literals_LongLiteral class attributes and methods

# simTL4J_literals_DecimalLongLiteral class attributes and methods
simTL4J_literals_DecimalLongLiteral_decimalValue: Property = Property(name="decimalValue", type=StringType)
simTL4J_literals_DecimalLongLiteral.attributes={simTL4J_literals_DecimalLongLiteral_decimalValue}

# LongLiteral class attributes and methods

# simTL4J_literals_HexLongLiteral class attributes and methods
simTL4J_literals_HexLongLiteral_hexValue: Property = Property(name="hexValue", type=StringType)
simTL4J_literals_HexLongLiteral.attributes={simTL4J_literals_HexLongLiteral_hexValue}

# simTL4J_members_Method class attributes and methods
simTL4J_members_Method_m_isMethodForCall: Method = Method(name="isMethodForCall", parameters={Parameter(name='needsPerfectMatch'), Parameter(name='methodCall')}, type=BooleanType)
simTL4J_members_Method_m_isSomeMethodForCall: Method = Method(name="isSomeMethodForCall", parameters={Parameter(name='methodCall')}, type=BooleanType)
simTL4J_members_Method_m_isBetterMethodForCall: Method = Method(name="isBetterMethodForCall", parameters={Parameter(name='methodCall'), Parameter(name='otherMethod')}, type=BooleanType)
simTL4J_members_Method_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
simTL4J_members_Method.methods={simTL4J_members_Method_m_isBetterMethodForCall, simTL4J_members_Method_m_isMethodForCall, simTL4J_members_Method_m_isSomeMethodForCall, simTL4J_members_Method_m_getArrayDimension}

# simTL4J_members_InterfaceMethod class attributes and methods

# Method class attributes and methods

# simTL4J_members_ClassMethod class attributes and methods

# members_Method class attributes and methods

# simTL4J_members_EnumConstant class attributes and methods

# simTL4J_modifiers_Modifier class attributes and methods

# AnnotationInstanceOrModifier class attributes and methods

# simTL4J_modifiers_AnnotationInstanceOrModifier class attributes and methods

# parameters_Parametrizable class attributes and methods

# members_ExceptionThrower class attributes and methods

# simTL4J_members_EmptyMember class attributes and methods

# simTL4J_members_Field class attributes and methods

# variables_Variable class attributes and methods

# AdditionalField class attributes and methods

# simTL4J_modifiers_Modifiable class attributes and methods

# Modifier class attributes and methods

# simTL4J_modifiers_Abstract class attributes and methods

# simTL4J_modifiers_Final class attributes and methods

# simTL4J_modifiers_Native class attributes and methods

# simTL4J_modifiers_Protected class attributes and methods

# simTL4J_modifiers_Public class attributes and methods

# simTL4J_modifiers_Private class attributes and methods

# simTL4J_modifiers_Static class attributes and methods

# simTL4J_modifiers_Strictfp class attributes and methods

# simTL4J_modifiers_Synchronized class attributes and methods

# simTL4J_modifiers_Transient class attributes and methods

# simTL4J_modifiers_Volatile class attributes and methods

# simTL4J_operators_Operator class attributes and methods

# simTL4J_operators_AdditiveOperator class attributes and methods

# Operator class attributes and methods

# simTL4J_modifiers_AnnotableAndModifiable class attributes and methods
simTL4J_modifiers_AnnotableAndModifiable_m_isHidden: Method = Method(name="isHidden", parameters={Parameter(name='context')}, type=BooleanType)
simTL4J_modifiers_AnnotableAndModifiable_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
simTL4J_modifiers_AnnotableAndModifiable.methods={simTL4J_modifiers_AnnotableAndModifiable_m_isStatic, simTL4J_modifiers_AnnotableAndModifiable_m_isHidden}

# simTL4J_operators_UnaryModificationOperator class attributes and methods

# simTL4J_operators_Assignment class attributes and methods

# simTL4J_operators_AssignmentAnd class attributes and methods

# simTL4J_operators_AssignmentDivision class attributes and methods

# simTL4J_operators_AssignmentExclusiveOr class attributes and methods

# simTL4J_operators_AssignmentMinus class attributes and methods

# simTL4J_operators_AssignmentModulo class attributes and methods

# simTL4J_operators_AssignmentMultiplication class attributes and methods

# simTL4J_operators_AssignmentLeftShift class attributes and methods

# simTL4J_operators_AssignmentOr class attributes and methods

# simTL4J_operators_AssignmentPlus class attributes and methods

# simTL4J_operators_AssignmentRightShift class attributes and methods

# simTL4J_operators_AssignmentUnsignedRightShift class attributes and methods

# simTL4J_operators_Equal class attributes and methods

# simTL4J_operators_NotEqual class attributes and methods

# simTL4J_operators_GreaterThan class attributes and methods

# simTL4J_operators_GreaterThanOrEqual class attributes and methods

# simTL4J_operators_LessThan class attributes and methods

# simTL4J_operators_AssignmentOperator class attributes and methods

# simTL4J_operators_EqualityOperator class attributes and methods

# simTL4J_operators_MultiplicativeOperator class attributes and methods

# simTL4J_operators_RelationOperator class attributes and methods

# simTL4J_operators_ShiftOperator class attributes and methods

# simTL4J_operators_UnaryOperator class attributes and methods

# simTL4J_operators_Complement class attributes and methods

# simTL4J_operators_MinusMinus class attributes and methods

# simTL4J_operators_Negate class attributes and methods

# simTL4J_operators_PlusPlus class attributes and methods

# simTL4J_operators_LeftShift class attributes and methods

# simTL4J_operators_RightShift class attributes and methods

# simTL4J_operators_UnsignedRightShift class attributes and methods

# simTL4J_parameters_Parameter class attributes and methods

# simTL4J_parameters_Parametrizable class attributes and methods

# Parameter class attributes and methods

# simTL4J_parameters_OrdinaryParameter class attributes and methods

# simTL4J_parameters_VariableLengthParameter class attributes and methods

# simTL4J_references_Reference class attributes and methods
simTL4J_references_Reference_m_getReferencedType: Method = Method(name="getReferencedType", parameters={}, type=StringType)
simTL4J_references_Reference_m_getPrevious: Method = Method(name="getPrevious", parameters={}, type=StringType)
simTL4J_references_Reference.methods={simTL4J_references_Reference_m_getPrevious, simTL4J_references_Reference_m_getReferencedType}

# expressions_PrimaryExpression class attributes and methods

# simTL4J_operators_LessThanOrEqual class attributes and methods

# simTL4J_operators_Addition class attributes and methods

# operators_AdditiveOperator class attributes and methods

# operators_UnaryOperator class attributes and methods

# simTL4J_operators_Subtraction class attributes and methods

# simTL4J_operators_Division class attributes and methods

# simTL4J_operators_Multiplication class attributes and methods

# simTL4J_operators_Remainder class attributes and methods

# simTL4J_references_Argumentable class attributes and methods
simTL4J_references_Argumentable_m_getArgumentTypes: Method = Method(name="getArgumentTypes", parameters={}, type=StringType)
simTL4J_references_Argumentable.methods={simTL4J_references_Argumentable_m_getArgumentTypes}

# simTL4J_references_ReferenceableElement class attributes and methods

# simTL4J_references_ElementReference class attributes and methods

# simTL4J_references_IdentifierReference class attributes and methods

# ElementReference class attributes and methods

# simTL4J_references_MethodCall class attributes and methods

# references_ElementReference class attributes and methods

# simTL4J_references_ReflectiveClassReference class attributes and methods

# simTL4J_references_PrimitiveTypeReference class attributes and methods

# PrimitiveType class attributes and methods

# simTL4J_references_StringReference class attributes and methods
simTL4J_references_StringReference_value: Property = Property(name="value", type=StringType)
simTL4J_references_StringReference.attributes={simTL4J_references_StringReference_value}

# ArraySelector class attributes and methods

# simTL4J_references_SelfReference class attributes and methods

# simTL4J_statements_StatementContainer class attributes and methods

# Statement class attributes and methods

# simTL4J_statements_Conditional class attributes and methods

# simTL4J_statements_ForLoopInitializer class attributes and methods

# simTL4J_statements_Statement class attributes and methods

# simTL4J_statements_SwitchCase class attributes and methods

# StatementListContainer class attributes and methods

# simTL4J_statements_Assert class attributes and methods

# statements_Conditional class attributes and methods

# simTL4J_statements_Break class attributes and methods

# Jump class attributes and methods

# simTL4J_statements_Block class attributes and methods

# modifiers_Modifiable class attributes and methods

# simTL4J_statements_CatchBlock class attributes and methods

# simTL4J_statements_StatementListContainer class attributes and methods

# simTL4J_statements_EmptyStatement class attributes and methods

# simTL4J_statements_ExpressionStatement class attributes and methods

# simTL4J_statements_ForLoop class attributes and methods

# simTL4J_statements_ForEachLoop class attributes and methods

# OrdinaryParameter class attributes and methods

# simTL4J_statements_Condition class attributes and methods

# statements_StatementContainer class attributes and methods

# simTL4J_statements_Continue class attributes and methods

# simTL4J_statements_DefaultSwitchCase class attributes and methods

# SwitchCase class attributes and methods

# simTL4J_statements_DoWhileLoop class attributes and methods

# WhileLoop class attributes and methods

# simTL4J_statements_Return class attributes and methods

# simTL4J_statements_Switch class attributes and methods

# simTL4J_statements_SynchronizedBlock class attributes and methods

# simTL4J_statements_Throw class attributes and methods

# simTL4J_statements_TryBlock class attributes and methods

# CatchBlock class attributes and methods

# Block class attributes and methods

# simTL4J_statements_WhileLoop class attributes and methods

# simTL4J_statements_Jump class attributes and methods

# JumpLabel class attributes and methods

# simTL4J_statements_JumpLabel class attributes and methods

# simTL4J_statements_LocalVariableStatement class attributes and methods

# LocalVariable class attributes and methods

# simTL4J_statements_NormalSwitchCase class attributes and methods

# statements_SwitchCase class attributes and methods

# simTL4J_types_TypedElement class attributes and methods

# simTL4J_types_TypeReference class attributes and methods
simTL4J_types_TypeReference_m_getTarget: Method = Method(name="getTarget", parameters={}, type=StringType)
simTL4J_types_TypeReference_m_getBoundTarget: Method = Method(name="getBoundTarget", parameters={Parameter(name='reference')}, type=StringType)
simTL4J_types_TypeReference_m_getPureClassifierReference: Method = Method(name="getPureClassifierReference", parameters={}, type=StringType)
simTL4J_types_TypeReference.methods={simTL4J_types_TypeReference_m_getBoundTarget, simTL4J_types_TypeReference_m_getPureClassifierReference, simTL4J_types_TypeReference_m_getTarget}

# simTL4J_types_ClassifierReference class attributes and methods

# types_TypeReference class attributes and methods

# simTL4J_types_NamespaceClassifierReference class attributes and methods

# ClassifierReference class attributes and methods

# simTL4J_types_PrimitiveType class attributes and methods
simTL4J_types_PrimitiveType_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=StringType)
simTL4J_types_PrimitiveType_m_wrapPrimitiveType: Method = Method(name="wrapPrimitiveType", parameters={}, type=StringType)
simTL4J_types_PrimitiveType.methods={simTL4J_types_PrimitiveType_m_wrapPrimitiveType, simTL4J_types_PrimitiveType_m_getAllMembers}

# simTL4J_types_Type class attributes and methods
simTL4J_types_Type_m_equalsType: Method = Method(name="equalsType", parameters={Parameter(name='otherArrayDimension'), Parameter(name='arrayDimension'), Parameter(name='otherType')}, type=BooleanType)
simTL4J_types_Type_m_isSuperType: Method = Method(name="isSuperType", parameters={Parameter(name='otherArrayType'), Parameter(name='arrayDimension'), Parameter(name='otherType')}, type=BooleanType)
simTL4J_types_Type_m_getAllMembers: Method = Method(name="getAllMembers", parameters={Parameter(name='context')}, type=StringType)
simTL4J_types_Type.methods={simTL4J_types_Type_m_equalsType, simTL4J_types_Type_m_isSuperType, simTL4J_types_Type_m_getAllMembers}

# simTL4J_variables_LocalVariable class attributes and methods

# statements_ForLoopInitializer class attributes and methods

# AdditionalLocalVariable class attributes and methods

# simTL4J_variables_AdditionalLocalVariable class attributes and methods
simTL4J_variables_AdditionalLocalVariable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
simTL4J_variables_AdditionalLocalVariable.methods={simTL4J_variables_AdditionalLocalVariable_m_getArrayDimension}

# simTL4J_simTL_TIf class attributes and methods

# TAbstractMethodStatement class attributes and methods

# simTL4J_simTL_TFor class attributes and methods

# TForVariable class attributes and methods

# simTL4J_simTL_TForVariable class attributes and methods
simTL4J_simTL_TForVariable_name: Property = Property(name="name", type=StringType)
simTL4J_simTL_TForVariable.attributes={simTL4J_simTL_TForVariable_name}

# simTL4J_types_Boolean class attributes and methods

# simTL4J_types_Byte class attributes and methods

# simTL4J_types_Char class attributes and methods

# simTL4J_types_Double class attributes and methods

# simTL4J_types_Float class attributes and methods

# simTL4J_types_Int class attributes and methods

# simTL4J_types_Long class attributes and methods

# simTL4J_types_Short class attributes and methods

# simTL4J_types_Void class attributes and methods

# simTL4J_variables_Variable class attributes and methods
simTL4J_variables_Variable_m_getArrayDimension: Method = Method(name="getArrayDimension", parameters={}, type=StringType)
simTL4J_variables_Variable.methods={simTL4J_variables_Variable_m_getArrayDimension}

# TModelImport class attributes and methods

# simTL4J_simTL_TModelImport class attributes and methods
simTL4J_simTL_TModelImport_name: Property = Property(name="name", type=StringType)
simTL4J_simTL_TModelImport_uri: Property = Property(name="uri", type=StringType)
simTL4J_simTL_TModelImport.attributes={simTL4J_simTL_TModelImport_uri, simTL4J_simTL_TModelImport_name}

# simTL4J_simTL_TMethodCall class attributes and methods
simTL4J_simTL_TMethodCall_methodName: Property = Property(name="methodName", type=StringType)
simTL4J_simTL_TMethodCall_params: Property = Property(name="params", type=StringType)
simTL4J_simTL_TMethodCall.attributes={simTL4J_simTL_TMethodCall_params, simTL4J_simTL_TMethodCall_methodName}

# simTL4J_simTL_TAbstractMethodStatement class attributes and methods

# simTL4J_simTL_TFor_MemberContainer class attributes and methods

# simTL_TFor class attributes and methods

# simTL4J_simTL_TFor_StatementListContainer class attributes and methods

# simTL4J_simTL_Template class attributes and methods

# TemplateHeader class attributes and methods

# simTL4J_simTL_TemplateHeader class attributes and methods

# simTL_TIf class attributes and methods

# simTL4J_simTL_TIf_StatementListContainer class attributes and methods

# simTL4J_simTL_TPlaceholder class attributes and methods

# simTL4J_simTL_TPlaceholder_PrimaryExpression class attributes and methods

# simTL_TPlaceholder class attributes and methods

# simTL4J_simTL_TUnaryOperator class attributes and methods

# simTL4J_simTL_TIf_MemberContainer class attributes and methods

# simTL4J_simTL_TUnaryOperatorNOT class attributes and methods

# TUnaryOperator class attributes and methods

# simTL4J_simTL_TMethodStatementImpl class attributes and methods
simTL4J_simTL_TMethodStatementImpl_caller: Property = Property(name="caller", type=StringType)
simTL4J_simTL_TMethodStatementImpl.attributes={simTL4J_simTL_TMethodStatementImpl_caller}

# TMethodCall class attributes and methods

# Relationships
annotation1: BinaryAssociation = BinaryAssociation(
    name="annotation1",
    ends={
        Property(name="Classifier", type=simTL4J_annotations_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_AnnotationInstance", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
parameter2: BinaryAssociation = BinaryAssociation(
    name="parameter2",
    ends={
        Property(name="AnnotationParameter", type=simTL4J_annotations_AnnotationInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_AnnotationInstance3", type=AnnotationParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value4: BinaryAssociation = BinaryAssociation(
    name="value4",
    ends={
        Property(name="AnnotationValue", type=simTL4J_annotations_SingleAnnotationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_SingleAnnotationParameter", type=AnnotationValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations0: BinaryAssociation = BinaryAssociation(
    name="annotations0",
    ends={
        Property(name="AnnotationInstance", type=simTL4J_annotations_Annotable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_Annotable", type=AnnotationInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
settings5: BinaryAssociation = BinaryAssociation(
    name="settings5",
    ends={
        Property(name="AnnotationAttributeSetting", type=simTL4J_annotations_AnnotationParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_AnnotationParameterList", type=AnnotationAttributeSetting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute6: BinaryAssociation = BinaryAssociation(
    name="attribute6",
    ends={
        Property(name="InterfaceMethod", type=simTL4J_annotations_AnnotationAttributeSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_AnnotationAttributeSetting", type=InterfaceMethod, multiplicity=Multiplicity(1, 1))
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="AnnotationValue9", type=simTL4J_annotations_AnnotationAttributeSetting, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_AnnotationAttributeSetting8", type=AnnotationValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arrayDimensionsBefore11: BinaryAssociation = BinaryAssociation(
    name="arrayDimensionsBefore11",
    ends={
        Property(name="ArrayDimension", type=simTL4J_arrays_ArrayTypeable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_arrays_ArrayTypeable", type=ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayDimensionsAfter12: BinaryAssociation = BinaryAssociation(
    name="arrayDimensionsAfter12",
    ends={
        Property(name="ArrayDimension14", type=simTL4J_arrays_ArrayTypeable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_arrays_ArrayTypeable13", type=ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue10: BinaryAssociation = BinaryAssociation(
    name="defaultValue10",
    ends={
        Property(name="Expression", type=simTL4J_annotations_AnnotationAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_annotations_AnnotationAttribute", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sizes16: BinaryAssociation = BinaryAssociation(
    name="sizes16",
    ends={
        Property(name="Expression17", type=simTL4J_arrays_ArrayInstantiationBySize, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_arrays_ArrayInstantiationBySize", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayInitializer18: BinaryAssociation = BinaryAssociation(
    name="arrayInitializer18",
    ends={
        Property(name="ArrayInitializer", type=simTL4J_arrays_ArrayInstantiationByValues, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_arrays_ArrayInstantiationByValues", type=ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position19: BinaryAssociation = BinaryAssociation(
    name="position19",
    ends={
        Property(name="Expression20", type=simTL4J_arrays_ArraySelector, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_arrays_ArraySelector", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValues15: BinaryAssociation = BinaryAssociation(
    name="initialValues15",
    ends={
        Property(name="ArrayInitializationValue", type=simTL4J_arrays_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_arrays_ArrayInitializer", type=ArrayInitializationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements21: BinaryAssociation = BinaryAssociation(
    name="implements21",
    ends={
        Property(name="TypeReference", type=simTL4J_classifiers_Implementor, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_classifiers_Implementor", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends22: BinaryAssociation = BinaryAssociation(
    name="extends22",
    ends={
        Property(name="TypeReference23", type=simTL4J_classifiers_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_classifiers_Class", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExtends24: BinaryAssociation = BinaryAssociation(
    name="defaultExtends24",
    ends={
        Property(name="TypeReference26", type=simTL4J_classifiers_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_classifiers_Class25", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends27: BinaryAssociation = BinaryAssociation(
    name="extends27",
    ends={
        Property(name="TypeReference28", type=simTL4J_classifiers_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_classifiers_Interface", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultExtends29: BinaryAssociation = BinaryAssociation(
    name="defaultExtends29",
    ends={
        Property(name="TypeReference31", type=simTL4J_classifiers_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_classifiers_Interface30", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constants32: BinaryAssociation = BinaryAssociation(
    name="constants32",
    ends={
        Property(name="EnumConstant", type=simTL4J_classifiers_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_classifiers_Enumeration", type=EnumConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name_PH33: BinaryAssociation = BinaryAssociation(
    name="name_PH33",
    ends={
        Property(name="TPlaceholder", type=simTL4J_commons_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_commons_NamedElement", type=TPlaceholder, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions38: BinaryAssociation = BinaryAssociation(
    name="expressions38",
    ends={
        Property(name="Expression39", type=simTL4J_expressions_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ExpressionList", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child40: BinaryAssociation = BinaryAssociation(
    name="child40",
    ends={
        Property(name="AssignmentExpressionChild", type=simTL4J_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_AssignmentExpression", type=AssignmentExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignmentOperator41: BinaryAssociation = BinaryAssociation(
    name="assignmentOperator41",
    ends={
        Property(name="AssignmentOperator", type=simTL4J_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_AssignmentExpression42", type=AssignmentOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value43: BinaryAssociation = BinaryAssociation(
    name="value43",
    ends={
        Property(name="Expression45", type=simTL4J_expressions_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_AssignmentExpression44", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child46: BinaryAssociation = BinaryAssociation(
    name="child46",
    ends={
        Property(name="ConditionalExpressionChild", type=simTL4J_expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ConditionalExpression", type=ConditionalExpressionChild, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifiers34: BinaryAssociation = BinaryAssociation(
    name="classifiers34",
    ends={
        Property(name="ConcreteClassifier", type=simTL4J_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_containers_CompilationUnit", type=ConcreteClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compilationUnits35: BinaryAssociation = BinaryAssociation(
    name="compilationUnits35",
    ends={
        Property(name="CompilationUnit", type=simTL4J_containers_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_containers_Package", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subpackages36: BinaryAssociation = BinaryAssociation(
    name="subpackages36",
    ends={
        Property(name="Package", type=simTL4J_containers_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_containers_Package37", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children54: BinaryAssociation = BinaryAssociation(
    name="children54",
    ends={
        Property(name="ConditionalAndExpressionChild", type=simTL4J_expressions_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ConditionalAndExpression", type=ConditionalAndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children55: BinaryAssociation = BinaryAssociation(
    name="children55",
    ends={
        Property(name="InclusiveOrExpressionChild", type=simTL4J_expressions_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_InclusiveOrExpression", type=InclusiveOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children56: BinaryAssociation = BinaryAssociation(
    name="children56",
    ends={
        Property(name="ExclusiveOrExpressionChild", type=simTL4J_expressions_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ExclusiveOrExpression", type=ExclusiveOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children57: BinaryAssociation = BinaryAssociation(
    name="children57",
    ends={
        Property(name="AndExpressionChild", type=simTL4J_expressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_AndExpression", type=AndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
equalityOperators58: BinaryAssociation = BinaryAssociation(
    name="equalityOperators58",
    ends={
        Property(name="EqualityOperator", type=simTL4J_expressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_EqualityExpression", type=EqualityOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children59: BinaryAssociation = BinaryAssociation(
    name="children59",
    ends={
        Property(name="EqualityExpressionChild", type=simTL4J_expressions_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_EqualityExpression60", type=EqualityExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child61: BinaryAssociation = BinaryAssociation(
    name="child61",
    ends={
        Property(name="InstanceOfExpressionChild", type=simTL4J_expressions_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_InstanceOfExpression", type=InstanceOfExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressionIf47: BinaryAssociation = BinaryAssociation(
    name="expressionIf47",
    ends={
        Property(name="Expression49", type=simTL4J_expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ConditionalExpression48", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressionElse50: BinaryAssociation = BinaryAssociation(
    name="expressionElse50",
    ends={
        Property(name="AssignmentExpressionChild52", type=simTL4J_expressions_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ConditionalExpression51", type=AssignmentExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children53: BinaryAssociation = BinaryAssociation(
    name="children53",
    ends={
        Property(name="ConditionalOrExpressionChild", type=simTL4J_expressions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ConditionalOrExpression", type=ConditionalOrExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children65: BinaryAssociation = BinaryAssociation(
    name="children65",
    ends={
        Property(name="ShiftExpressionChild", type=simTL4J_expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ShiftExpression", type=ShiftExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
shiftOperators66: BinaryAssociation = BinaryAssociation(
    name="shiftOperators66",
    ends={
        Property(name="ShiftOperator", type=simTL4J_expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_ShiftExpression67", type=ShiftOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children68: BinaryAssociation = BinaryAssociation(
    name="children68",
    ends={
        Property(name="AdditiveExpressionChild", type=simTL4J_expressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_AdditiveExpression", type=AdditiveExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additiveOperators69: BinaryAssociation = BinaryAssociation(
    name="additiveOperators69",
    ends={
        Property(name="AdditiveOperator", type=simTL4J_expressions_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_AdditiveExpression70", type=AdditiveOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children71: BinaryAssociation = BinaryAssociation(
    name="children71",
    ends={
        Property(name="MultiplicativeExpressionChild", type=simTL4J_expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_MultiplicativeExpression", type=MultiplicativeExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
multiplicativeOperators72: BinaryAssociation = BinaryAssociation(
    name="multiplicativeOperators72",
    ends={
        Property(name="MultiplicativeOperator", type=simTL4J_expressions_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_MultiplicativeExpression73", type=MultiplicativeOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children62: BinaryAssociation = BinaryAssociation(
    name="children62",
    ends={
        Property(name="RelationExpressionChild", type=simTL4J_expressions_RelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_RelationExpression", type=RelationExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationOperators63: BinaryAssociation = BinaryAssociation(
    name="relationOperators63",
    ends={
        Property(name="RelationOperator", type=simTL4J_expressions_RelationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_RelationExpression64", type=RelationOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child77: BinaryAssociation = BinaryAssociation(
    name="child77",
    ends={
        Property(name="UnaryModificationExpressionChild", type=simTL4J_expressions_UnaryModificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_UnaryModificationExpression", type=UnaryModificationExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator78: BinaryAssociation = BinaryAssociation(
    name="operator78",
    ends={
        Property(name="UnaryModificationOperator", type=simTL4J_expressions_UnaryModificationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_UnaryModificationExpression79", type=UnaryModificationOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child80: BinaryAssociation = BinaryAssociation(
    name="child80",
    ends={
        Property(name="MultiplicativeExpressionChild81", type=simTL4J_expressions_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_CastExpression", type=MultiplicativeExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression82: BinaryAssociation = BinaryAssociation(
    name="expression82",
    ends={
        Property(name="Expression83", type=simTL4J_expressions_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_NestedExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operators74: BinaryAssociation = BinaryAssociation(
    name="operators74",
    ends={
        Property(name="UnaryOperator", type=simTL4J_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_UnaryExpression", type=UnaryOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child75: BinaryAssociation = BinaryAssociation(
    name="child75",
    ends={
        Property(name="UnaryExpressionChild", type=simTL4J_expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_expressions_UnaryExpression76", type=UnaryExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeParameters87: BinaryAssociation = BinaryAssociation(
    name="typeParameters87",
    ends={
        Property(name="TypeParameter", type=simTL4J_generics_TypeParametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_generics_TypeParametrizable", type=TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendTypes88: BinaryAssociation = BinaryAssociation(
    name="extendTypes88",
    ends={
        Property(name="TypeReference89", type=simTL4J_generics_ExtendsTypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_generics_ExtendsTypeArgument", type=TypeReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
superType90: BinaryAssociation = BinaryAssociation(
    name="superType90",
    ends={
        Property(name="TypeReference91", type=simTL4J_generics_SuperTypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_generics_SuperTypeArgument", type=TypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeArguments84: BinaryAssociation = BinaryAssociation(
    name="typeArguments84",
    ends={
        Property(name="TypeArgument", type=simTL4J_generics_TypeArgumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_generics_TypeArgumentable", type=TypeArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callTypeArguments85: BinaryAssociation = BinaryAssociation(
    name="callTypeArguments85",
    ends={
        Property(name="TypeArgument86", type=simTL4J_generics_CallTypeArgumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_generics_CallTypeArgumentable", type=TypeArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports94: BinaryAssociation = BinaryAssociation(
    name="imports94",
    ends={
        Property(name="Import", type=simTL4J_imports_ImportingElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_imports_ImportingElement", type=Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
static95: BinaryAssociation = BinaryAssociation(
    name="static95",
    ends={
        Property(name="Static", type=simTL4J_imports_StaticImport, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_imports_StaticImport", type=Static, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendTypes92: BinaryAssociation = BinaryAssociation(
    name="extendTypes92",
    ends={
        Property(name="TypeReference93", type=simTL4J_generics_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_generics_TypeParameter", type=TypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier96: BinaryAssociation = BinaryAssociation(
    name="classifier96",
    ends={
        Property(name="ConcreteClassifier97", type=simTL4J_imports_ClassifierImport, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_imports_ClassifierImport", type=ConcreteClassifier, multiplicity=Multiplicity(1, 1))
    }
)
staticMembers98: BinaryAssociation = BinaryAssociation(
    name="staticMembers98",
    ends={
        Property(name="ReferenceableElement", type=simTL4J_imports_StaticMemberImport, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_imports_StaticMemberImport", type=ReferenceableElement, multiplicity=Multiplicity(1, 9999))
    }
)
initialValue99: BinaryAssociation = BinaryAssociation(
    name="initialValue99",
    ends={
        Property(name="Expression100", type=simTL4J_instantiations_Initializable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_instantiations_Initializable", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousClass101: BinaryAssociation = BinaryAssociation(
    name="anonymousClass101",
    ends={
        Property(name="AnonymousClass", type=simTL4J_instantiations_NewConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_instantiations_NewConstructorCall", type=AnonymousClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callTarget102: BinaryAssociation = BinaryAssociation(
    name="callTarget102",
    ends={
        Property(name="Self", type=simTL4J_instantiations_ExplicitConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_instantiations_ExplicitConstructorCall", type=Self, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions103: BinaryAssociation = BinaryAssociation(
    name="exceptions103",
    ends={
        Property(name="NamespaceClassifierReference", type=simTL4J_members_ExceptionThrower, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_members_ExceptionThrower", type=NamespaceClassifierReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members104: BinaryAssociation = BinaryAssociation(
    name="members104",
    ends={
        Property(name="Member", type=simTL4J_members_MemberContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_members_MemberContainer", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultMembers105: BinaryAssociation = BinaryAssociation(
    name="defaultMembers105",
    ends={
        Property(name="Member107", type=simTL4J_members_MemberContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_members_MemberContainer106", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anonymousClass109: BinaryAssociation = BinaryAssociation(
    name="anonymousClass109",
    ends={
        Property(name="AnonymousClass110", type=simTL4J_members_EnumConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_members_EnumConstant", type=AnonymousClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additionalFields108: BinaryAssociation = BinaryAssociation(
    name="additionalFields108",
    ends={
        Property(name="AdditionalField", type=simTL4J_members_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_members_Field", type=AdditionalField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationsAndModifiers111: BinaryAssociation = BinaryAssociation(
    name="annotationsAndModifiers111",
    ends={
        Property(name="AnnotationInstanceOrModifier", type=simTL4J_modifiers_AnnotableAndModifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_modifiers_AnnotableAndModifiable", type=AnnotationInstanceOrModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifiers112: BinaryAssociation = BinaryAssociation(
    name="modifiers112",
    ends={
        Property(name="Modifier", type=simTL4J_modifiers_Modifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_modifiers_Modifiable", type=Modifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters113: BinaryAssociation = BinaryAssociation(
    name="parameters113",
    ends={
        Property(name="Parameter", type=simTL4J_parameters_Parametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_parameters_Parametrizable", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments117: BinaryAssociation = BinaryAssociation(
    name="arguments117",
    ends={
        Property(name="Expression118", type=simTL4J_references_Argumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_references_Argumentable", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target119: BinaryAssociation = BinaryAssociation(
    name="target119",
    ends={
        Property(name="ReferenceableElement120", type=simTL4J_references_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_references_ElementReference", type=ReferenceableElement, multiplicity=Multiplicity(0, 1))
    }
)
primitiveType121: BinaryAssociation = BinaryAssociation(
    name="primitiveType121",
    ends={
        Property(name="PrimitiveType", type=simTL4J_references_PrimitiveTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_references_PrimitiveTypeReference", type=PrimitiveType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
next114: BinaryAssociation = BinaryAssociation(
    name="next114",
    ends={
        Property(name="Reference", type=simTL4J_references_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_references_Reference", type=Reference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arraySelectors115: BinaryAssociation = BinaryAssociation(
    name="arraySelectors115",
    ends={
        Property(name="ArraySelector", type=simTL4J_references_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_references_Reference116", type=ArraySelector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement124: BinaryAssociation = BinaryAssociation(
    name="statement124",
    ends={
        Property(name="Statement", type=simTL4J_statements_StatementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_StatementContainer", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
self122: BinaryAssociation = BinaryAssociation(
    name="self122",
    ends={
        Property(name="Self123", type=simTL4J_references_SelfReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_references_SelfReference", type=Self, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition127: BinaryAssociation = BinaryAssociation(
    name="condition127",
    ends={
        Property(name="Expression128", type=simTL4J_statements_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Conditional", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
errorMessage129: BinaryAssociation = BinaryAssociation(
    name="errorMessage129",
    ends={
        Property(name="Expression130", type=simTL4J_statements_Assert, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Assert", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements125: BinaryAssociation = BinaryAssociation(
    name="statements125",
    ends={
        Property(name="Statement126", type=simTL4J_statements_StatementListContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_StatementListContainer", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression134: BinaryAssociation = BinaryAssociation(
    name="expression134",
    ends={
        Property(name="Expression135", type=simTL4J_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init136: BinaryAssociation = BinaryAssociation(
    name="init136",
    ends={
        Property(name="ForLoopInitializer", type=simTL4J_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_ForLoop", type=ForLoopInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
updates137: BinaryAssociation = BinaryAssociation(
    name="updates137",
    ends={
        Property(name="Expression139", type=simTL4J_statements_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_ForLoop138", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next140: BinaryAssociation = BinaryAssociation(
    name="next140",
    ends={
        Property(name="OrdinaryParameter141", type=simTL4J_statements_ForEachLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_ForEachLoop", type=OrdinaryParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection142: BinaryAssociation = BinaryAssociation(
    name="collection142",
    ends={
        Property(name="Expression144", type=simTL4J_statements_ForEachLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_ForEachLoop143", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter131: BinaryAssociation = BinaryAssociation(
    name="parameter131",
    ends={
        Property(name="OrdinaryParameter", type=simTL4J_statements_CatchBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_CatchBlock", type=OrdinaryParameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement132: BinaryAssociation = BinaryAssociation(
    name="elseStatement132",
    ends={
        Property(name="Statement133", type=simTL4J_statements_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Condition", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValue147: BinaryAssociation = BinaryAssociation(
    name="returnValue147",
    ends={
        Property(name="Expression148", type=simTL4J_statements_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Return", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases149: BinaryAssociation = BinaryAssociation(
    name="cases149",
    ends={
        Property(name="SwitchCase", type=simTL4J_statements_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Switch", type=SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable150: BinaryAssociation = BinaryAssociation(
    name="variable150",
    ends={
        Property(name="Expression152", type=simTL4J_statements_Switch, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Switch151", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lockProvider153: BinaryAssociation = BinaryAssociation(
    name="lockProvider153",
    ends={
        Property(name="Expression154", type=simTL4J_statements_SynchronizedBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_SynchronizedBlock", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throwable155: BinaryAssociation = BinaryAssociation(
    name="throwable155",
    ends={
        Property(name="Expression156", type=simTL4J_statements_Throw, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Throw", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catcheBlocks157: BinaryAssociation = BinaryAssociation(
    name="catcheBlocks157",
    ends={
        Property(name="CatchBlock", type=simTL4J_statements_TryBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_TryBlock", type=CatchBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyBlock158: BinaryAssociation = BinaryAssociation(
    name="finallyBlock158",
    ends={
        Property(name="Block", type=simTL4J_statements_TryBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_TryBlock159", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target145: BinaryAssociation = BinaryAssociation(
    name="target145",
    ends={
        Property(name="JumpLabel", type=simTL4J_statements_Jump, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_Jump", type=JumpLabel, multiplicity=Multiplicity(0, 1))
    }
)
variable146: BinaryAssociation = BinaryAssociation(
    name="variable146",
    ends={
        Property(name="LocalVariable", type=simTL4J_statements_LocalVariableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_LocalVariableStatement", type=LocalVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeReference162: BinaryAssociation = BinaryAssociation(
    name="typeReference162",
    ends={
        Property(name="TypeReference163", type=simTL4J_types_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_types_TypedElement", type=TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target164: BinaryAssociation = BinaryAssociation(
    name="target164",
    ends={
        Property(name="Classifier165", type=simTL4J_types_ClassifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_types_ClassifierReference", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
classifierReferences166: BinaryAssociation = BinaryAssociation(
    name="classifierReferences166",
    ends={
        Property(name="ClassifierReference", type=simTL4J_types_NamespaceClassifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_types_NamespaceClassifierReference", type=ClassifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition160: BinaryAssociation = BinaryAssociation(
    name="condition160",
    ends={
        Property(name="Expression161", type=simTL4J_statements_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_statements_WhileLoop", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
additionalLocalVariables167: BinaryAssociation = BinaryAssociation(
    name="additionalLocalVariables167",
    ends={
        Property(name="AdditionalLocalVariable", type=simTL4J_variables_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_variables_LocalVariable", type=AdditionalLocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition168: BinaryAssociation = BinaryAssociation(
    name="condition168",
    ends={
        Property(name="TAbstractMethodStatement", type=simTL4J_simTL_TIf, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_TIf", type=TAbstractMethodStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
count169: BinaryAssociation = BinaryAssociation(
    name="count169",
    ends={
        Property(name="TForVariable", type=simTL4J_simTL_TFor, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_TFor", type=TForVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelImports175: BinaryAssociation = BinaryAssociation(
    name="modelImports175",
    ends={
        Property(name="TModelImport", type=simTL4J_simTL_TemplateHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_TemplateHeader", type=TModelImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
setToBeIterated170: BinaryAssociation = BinaryAssociation(
    name="setToBeIterated170",
    ends={
        Property(name="TAbstractMethodStatement171", type=simTL4J_simTL_TForVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_TForVariable", type=TAbstractMethodStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
templateHeader172: BinaryAssociation = BinaryAssociation(
    name="templateHeader172",
    ends={
        Property(name="TemplateHeader", type=simTL4J_simTL_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_Template", type=TemplateHeader, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class173: BinaryAssociation = BinaryAssociation(
    name="class173",
    ends={
        Property(name="JavaRoot", type=simTL4J_simTL_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_Template174", type=JavaRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodStatement176: BinaryAssociation = BinaryAssociation(
    name="methodStatement176",
    ends={
        Property(name="TAbstractMethodStatement177", type=simTL4J_simTL_TPlaceholder, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_TPlaceholder", type=TAbstractMethodStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodStatement178: BinaryAssociation = BinaryAssociation(
    name="methodStatement178",
    ends={
        Property(name="TAbstractMethodStatement179", type=simTL4J_simTL_TUnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="simTL4J_simTL_TUnaryOperator", type=TAbstractMethodStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callee180: BinaryAssociation = BinaryAssociation(
    name="callee180",
    ends={
        Property(name="simTL4J_simTL_TMethodStatementImpl", type=TMethodCall, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="TMethodCall", type=simTL4J_simTL_TMethodStatementImpl, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simTL4J_annotations_Annotable_Commentable = Generalization(general=Commentable, specific=simTL4J_annotations_Annotable)
gen_simTL4J_annotations_AnnotationInstance_references_Reference = Generalization(general=references_Reference, specific=simTL4J_annotations_AnnotationInstance)
gen_simTL4J_annotations_AnnotationInstance_modifiers_AnnotationInstanceOrModifier = Generalization(general=modifiers_AnnotationInstanceOrModifier, specific=simTL4J_annotations_AnnotationInstance)
gen_simTL4J_annotations_AnnotationInstance_commons_NamespaceAwareElement = Generalization(general=commons_NamespaceAwareElement, specific=simTL4J_annotations_AnnotationInstance)
gen_simTL4J_annotations_AnnotationParameter_Commentable = Generalization(general=Commentable, specific=simTL4J_annotations_AnnotationParameter)
gen_simTL4J_annotations_SingleAnnotationParameter_AnnotationParameter = Generalization(general=AnnotationParameter, specific=simTL4J_annotations_SingleAnnotationParameter)
gen_simTL4J_annotations_AnnotationAttributeSetting_Commentable = Generalization(general=Commentable, specific=simTL4J_annotations_AnnotationAttributeSetting)
gen_simTL4J_annotations_AnnotationValue_Commentable = Generalization(general=Commentable, specific=simTL4J_annotations_AnnotationValue)
gen_simTL4J_annotations_AnnotationParameterList_AnnotationParameter = Generalization(general=AnnotationParameter, specific=simTL4J_annotations_AnnotationParameterList)
gen_simTL4J_arrays_ArrayTypeable_Commentable = Generalization(general=Commentable, specific=simTL4J_arrays_ArrayTypeable)
gen_simTL4J_annotations_AnnotationAttribute_InterfaceMethod = Generalization(general=InterfaceMethod, specific=simTL4J_annotations_AnnotationAttribute)
gen_simTL4J_arrays_ArrayInstantiationBySize_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_arrays_ArrayInstantiationBySize)
gen_simTL4J_arrays_ArrayInstantiationBySize_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_arrays_ArrayInstantiationBySize)
gen_simTL4J_arrays_ArrayInstantiationBySize_references_Reference = Generalization(general=references_Reference, specific=simTL4J_arrays_ArrayInstantiationBySize)
gen_simTL4J_arrays_ArrayInstantiationByValues_expressions_Expression = Generalization(general=expressions_Expression, specific=simTL4J_arrays_ArrayInstantiationByValues)
gen_simTL4J_arrays_ArrayInstantiationByValues_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_arrays_ArrayInstantiationByValues)
gen_simTL4J_arrays_ArrayInstantiationByValues_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_arrays_ArrayInstantiationByValues)
gen_simTL4J_arrays_ArrayInstantiationByValues_references_Reference = Generalization(general=references_Reference, specific=simTL4J_arrays_ArrayInstantiationByValues)
gen_simTL4J_arrays_ArraySelector_Commentable = Generalization(general=Commentable, specific=simTL4J_arrays_ArraySelector)
gen_simTL4J_classifiers_Classifier_types_Type = Generalization(general=types_Type, specific=simTL4J_classifiers_Classifier)
gen_simTL4J_arrays_ArrayDimension_Commentable = Generalization(general=Commentable, specific=simTL4J_arrays_ArrayDimension)
gen_simTL4J_arrays_ArrayInitializer_arrays_ArrayInitializationValue = Generalization(general=arrays_ArrayInitializationValue, specific=simTL4J_arrays_ArrayInitializer)
gen_simTL4J_arrays_ArrayInitializer_annotations_AnnotationValue = Generalization(general=annotations_AnnotationValue, specific=simTL4J_arrays_ArrayInitializer)
gen_simTL4J_arrays_ArrayInitializationValue_Commentable = Generalization(general=Commentable, specific=simTL4J_arrays_ArrayInitializationValue)
gen_simTL4J_arrays_ArrayInstantiationBySize_expressions_Expression = Generalization(general=expressions_Expression, specific=simTL4J_arrays_ArrayInstantiationBySize)
gen_simTL4J_classifiers_Implementor_Commentable = Generalization(general=Commentable, specific=simTL4J_classifiers_Implementor)
gen_simTL4J_classifiers_Classifier_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_classifiers_Classifier)
gen_simTL4J_classifiers_ConcreteClassifier_classifiers_Classifier = Generalization(general=classifiers_Classifier, specific=simTL4J_classifiers_ConcreteClassifier)
gen_simTL4J_classifiers_ConcreteClassifier_generics_TypeParametrizable = Generalization(general=generics_TypeParametrizable, specific=simTL4J_classifiers_ConcreteClassifier)
gen_simTL4J_classifiers_ConcreteClassifier_members_MemberContainer = Generalization(general=members_MemberContainer, specific=simTL4J_classifiers_ConcreteClassifier)
gen_simTL4J_classifiers_ConcreteClassifier_members_Member = Generalization(general=members_Member, specific=simTL4J_classifiers_ConcreteClassifier)
gen_simTL4J_classifiers_ConcreteClassifier_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_classifiers_ConcreteClassifier)
gen_simTL4J_classifiers_ConcreteClassifier_modifiers_AnnotableAndModifiable = Generalization(general=modifiers_AnnotableAndModifiable, specific=simTL4J_classifiers_ConcreteClassifier)
gen_simTL4J_classifiers_Interface_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=simTL4J_classifiers_Interface)
gen_simTL4J_classifiers_Enumeration_classifiers_ConcreteClassifier = Generalization(general=classifiers_ConcreteClassifier, specific=simTL4J_classifiers_Enumeration)
gen_simTL4J_classifiers_Enumeration_classifiers_Implementor = Generalization(general=classifiers_Implementor, specific=simTL4J_classifiers_Enumeration)
gen_simTL4J_classifiers_Class_classifiers_ConcreteClassifier = Generalization(general=classifiers_ConcreteClassifier, specific=simTL4J_classifiers_Class)
gen_simTL4J_classifiers_Class_classifiers_Implementor = Generalization(general=classifiers_Implementor, specific=simTL4J_classifiers_Class)
gen_simTL4J_classifiers_AnonymousClass_types_Type = Generalization(general=types_Type, specific=simTL4J_classifiers_AnonymousClass)
gen_simTL4J_classifiers_AnonymousClass_members_MemberContainer = Generalization(general=members_MemberContainer, specific=simTL4J_classifiers_AnonymousClass)
gen_simTL4J_classifiers_Annotation_ConcreteClassifier = Generalization(general=ConcreteClassifier, specific=simTL4J_classifiers_Annotation)
gen_simTL4J_commons_NamedElement_Commentable = Generalization(general=Commentable, specific=simTL4J_commons_NamedElement)
gen_simTL4J_commons_NamespaceAwareElement_Commentable = Generalization(general=Commentable, specific=simTL4J_commons_NamespaceAwareElement)
gen_simTL4J_containers_JavaRoot_commons_NamedElement = Generalization(general=commons_NamedElement, specific=simTL4J_containers_JavaRoot)
gen_simTL4J_containers_JavaRoot_commons_NamespaceAwareElement = Generalization(general=commons_NamespaceAwareElement, specific=simTL4J_containers_JavaRoot)
gen_simTL4J_containers_JavaRoot_imports_ImportingElement = Generalization(general=imports_ImportingElement, specific=simTL4J_containers_JavaRoot)
gen_simTL4J_containers_CompilationUnit_JavaRoot = Generalization(general=JavaRoot, specific=simTL4J_containers_CompilationUnit)
gen_simTL4J_containers_EmptyModel_JavaRoot = Generalization(general=JavaRoot, specific=simTL4J_containers_EmptyModel)
gen_simTL4J_expressions_ExpressionList_ForLoopInitializer = Generalization(general=ForLoopInitializer, specific=simTL4J_expressions_ExpressionList)
gen_simTL4J_expressions_Expression_arrays_ArrayInitializationValue = Generalization(general=arrays_ArrayInitializationValue, specific=simTL4J_expressions_Expression)
gen_simTL4J_expressions_Expression_annotations_AnnotationValue = Generalization(general=annotations_AnnotationValue, specific=simTL4J_expressions_Expression)
gen_simTL4J_expressions_AssignmentExpression_Expression = Generalization(general=Expression, specific=simTL4J_expressions_AssignmentExpression)
gen_simTL4J_expressions_AssignmentExpressionChild_Expression = Generalization(general=Expression, specific=simTL4J_expressions_AssignmentExpressionChild)
gen_simTL4J_expressions_ConditionalExpression_AssignmentExpressionChild = Generalization(general=AssignmentExpressionChild, specific=simTL4J_expressions_ConditionalExpression)
gen_simTL4J_containers_Package_containers_JavaRoot = Generalization(general=containers_JavaRoot, specific=simTL4J_containers_Package)
gen_simTL4J_containers_Package_annotations_Annotable = Generalization(general=annotations_Annotable, specific=simTL4J_containers_Package)
gen_simTL4J_containers_Package_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_containers_Package)
gen_simTL4J_expressions_ConditionalAndExpressionChild_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=simTL4J_expressions_ConditionalAndExpressionChild)
gen_simTL4J_expressions_InclusiveOrExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=simTL4J_expressions_InclusiveOrExpression)
gen_simTL4J_expressions_InclusiveOrExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=simTL4J_expressions_InclusiveOrExpressionChild)
gen_simTL4J_expressions_ExclusiveOrExpression_InclusiveOrExpressionChild = Generalization(general=InclusiveOrExpressionChild, specific=simTL4J_expressions_ExclusiveOrExpression)
gen_simTL4J_expressions_ExclusiveOrExpressionChild_InclusiveOrExpressionChild = Generalization(general=InclusiveOrExpressionChild, specific=simTL4J_expressions_ExclusiveOrExpressionChild)
gen_simTL4J_expressions_AndExpression_ExclusiveOrExpressionChild = Generalization(general=ExclusiveOrExpressionChild, specific=simTL4J_expressions_AndExpression)
gen_simTL4J_expressions_AndExpressionChild_ExclusiveOrExpressionChild = Generalization(general=ExclusiveOrExpressionChild, specific=simTL4J_expressions_AndExpressionChild)
gen_simTL4J_expressions_EqualityExpression_AndExpressionChild = Generalization(general=AndExpressionChild, specific=simTL4J_expressions_EqualityExpression)
gen_simTL4J_expressions_EqualityExpressionChild_AndExpressionChild = Generalization(general=AndExpressionChild, specific=simTL4J_expressions_EqualityExpressionChild)
gen_simTL4J_expressions_InstanceOfExpression_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_expressions_InstanceOfExpression)
gen_simTL4J_expressions_InstanceOfExpression_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_expressions_InstanceOfExpression)
gen_simTL4J_expressions_InstanceOfExpression_expressions_EqualityExpressionChild = Generalization(general=expressions_EqualityExpressionChild, specific=simTL4J_expressions_InstanceOfExpression)
gen_simTL4J_expressions_InstanceOfExpressionChild_EqualityExpressionChild = Generalization(general=EqualityExpressionChild, specific=simTL4J_expressions_InstanceOfExpressionChild)
gen_simTL4J_expressions_ConditionalExpressionChild_AssignmentExpressionChild = Generalization(general=AssignmentExpressionChild, specific=simTL4J_expressions_ConditionalExpressionChild)
gen_simTL4J_expressions_ConditionalOrExpression_ConditionalExpressionChild = Generalization(general=ConditionalExpressionChild, specific=simTL4J_expressions_ConditionalOrExpression)
gen_simTL4J_expressions_ConditionalOrExpressionChild_ConditionalExpressionChild = Generalization(general=ConditionalExpressionChild, specific=simTL4J_expressions_ConditionalOrExpressionChild)
gen_simTL4J_expressions_ConditionalAndExpression_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=simTL4J_expressions_ConditionalAndExpression)
gen_simTL4J_expressions_ShiftExpressionChild_RelationExpressionChild = Generalization(general=RelationExpressionChild, specific=simTL4J_expressions_ShiftExpressionChild)
gen_simTL4J_expressions_AdditiveExpression_ShiftExpressionChild = Generalization(general=ShiftExpressionChild, specific=simTL4J_expressions_AdditiveExpression)
gen_simTL4J_expressions_AdditiveExpressionChild_ShiftExpressionChild = Generalization(general=ShiftExpressionChild, specific=simTL4J_expressions_AdditiveExpressionChild)
gen_simTL4J_expressions_MultiplicativeExpression_AdditiveExpressionChild = Generalization(general=AdditiveExpressionChild, specific=simTL4J_expressions_MultiplicativeExpression)
gen_simTL4J_expressions_MultiplicativeExpressionChild_AdditiveExpressionChild = Generalization(general=AdditiveExpressionChild, specific=simTL4J_expressions_MultiplicativeExpressionChild)
gen_simTL4J_expressions_UnaryExpression_MultiplicativeExpressionChild = Generalization(general=MultiplicativeExpressionChild, specific=simTL4J_expressions_UnaryExpression)
gen_simTL4J_expressions_RelationExpression_InstanceOfExpressionChild = Generalization(general=InstanceOfExpressionChild, specific=simTL4J_expressions_RelationExpression)
gen_simTL4J_expressions_RelationExpressionChild_InstanceOfExpressionChild = Generalization(general=InstanceOfExpressionChild, specific=simTL4J_expressions_RelationExpressionChild)
gen_simTL4J_expressions_ShiftExpression_RelationExpressionChild = Generalization(general=RelationExpressionChild, specific=simTL4J_expressions_ShiftExpression)
gen_simTL4J_expressions_PrefixUnaryModificationExpression_UnaryModificationExpression = Generalization(general=UnaryModificationExpression, specific=simTL4J_expressions_PrefixUnaryModificationExpression)
gen_simTL4J_expressions_SuffixUnaryModificationExpression_UnaryModificationExpression = Generalization(general=UnaryModificationExpression, specific=simTL4J_expressions_SuffixUnaryModificationExpression)
gen_simTL4J_expressions_UnaryModificationExpressionChild_UnaryExpressionChild = Generalization(general=UnaryExpressionChild, specific=simTL4J_expressions_UnaryModificationExpressionChild)
gen_simTL4J_expressions_CastExpression_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_expressions_CastExpression)
gen_simTL4J_expressions_CastExpression_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_expressions_CastExpression)
gen_simTL4J_expressions_CastExpression_expressions_UnaryModificationExpressionChild = Generalization(general=expressions_UnaryModificationExpressionChild, specific=simTL4J_expressions_CastExpression)
gen_simTL4J_expressions_PrimaryExpression_UnaryModificationExpressionChild = Generalization(general=UnaryModificationExpressionChild, specific=simTL4J_expressions_PrimaryExpression)
gen_simTL4J_expressions_NestedExpression_Reference = Generalization(general=Reference, specific=simTL4J_expressions_NestedExpression)
gen_simTL4J_expressions_UnaryExpressionChild_MultiplicativeExpressionChild = Generalization(general=MultiplicativeExpressionChild, specific=simTL4J_expressions_UnaryExpressionChild)
gen_simTL4J_expressions_UnaryModificationExpression_UnaryExpressionChild = Generalization(general=UnaryExpressionChild, specific=simTL4J_expressions_UnaryModificationExpression)
gen_simTL4J_generics_TypeParametrizable_Commentable = Generalization(general=Commentable, specific=simTL4J_generics_TypeParametrizable)
gen_simTL4J_generics_ExtendsTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=simTL4J_generics_ExtendsTypeArgument)
gen_simTL4J_generics_QualifiedTypeArgument_generics_TypeArgument = Generalization(general=generics_TypeArgument, specific=simTL4J_generics_QualifiedTypeArgument)
gen_simTL4J_generics_QualifiedTypeArgument_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_generics_QualifiedTypeArgument)
gen_simTL4J_generics_SuperTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=simTL4J_generics_SuperTypeArgument)
gen_simTL4J_generics_TypeParameter_Classifier = Generalization(general=Classifier, specific=simTL4J_generics_TypeParameter)
gen_simTL4J_generics_TypeArgument_ArrayTypeable = Generalization(general=ArrayTypeable, specific=simTL4J_generics_TypeArgument)
gen_simTL4J_generics_TypeArgumentable_Commentable = Generalization(general=Commentable, specific=simTL4J_generics_TypeArgumentable)
gen_simTL4J_generics_CallTypeArgumentable_Commentable = Generalization(general=Commentable, specific=simTL4J_generics_CallTypeArgumentable)
gen_simTL4J_imports_Import_NamespaceAwareElement = Generalization(general=NamespaceAwareElement, specific=simTL4J_imports_Import)
gen_simTL4J_imports_ImportingElement_Commentable = Generalization(general=Commentable, specific=simTL4J_imports_ImportingElement)
gen_simTL4J_imports_StaticImport_Import = Generalization(general=Import, specific=simTL4J_imports_StaticImport)
gen_simTL4J_generics_UnknownTypeArgument_TypeArgument = Generalization(general=TypeArgument, specific=simTL4J_generics_UnknownTypeArgument)
gen_simTL4J_imports_PackageImport_Import = Generalization(general=Import, specific=simTL4J_imports_PackageImport)
gen_simTL4J_imports_StaticClassifierImport_StaticImport = Generalization(general=StaticImport, specific=simTL4J_imports_StaticClassifierImport)
gen_simTL4J_imports_StaticMemberImport_StaticImport = Generalization(general=StaticImport, specific=simTL4J_imports_StaticMemberImport)
gen_simTL4J_instantiations_Initializable_Commentable = Generalization(general=Commentable, specific=simTL4J_instantiations_Initializable)
gen_simTL4J_instantiations_Instantiation_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_instantiations_Instantiation)
gen_simTL4J_instantiations_Instantiation_references_Reference = Generalization(general=references_Reference, specific=simTL4J_instantiations_Instantiation)
gen_simTL4J_instantiations_Instantiation_references_Argumentable = Generalization(general=references_Argumentable, specific=simTL4J_instantiations_Instantiation)
gen_simTL4J_imports_ClassifierImport_Import = Generalization(general=Import, specific=simTL4J_imports_ClassifierImport)
gen_simTL4J_literals_Self_Commentable = Generalization(general=Commentable, specific=simTL4J_literals_Self)
gen_simTL4J_literals_BooleanLiteral_Literal = Generalization(general=Literal, specific=simTL4J_literals_BooleanLiteral)
gen_simTL4J_literals_CharacterLiteral_Literal = Generalization(general=Literal, specific=simTL4J_literals_CharacterLiteral)
gen_simTL4J_literals_FloatLiteral_Literal = Generalization(general=Literal, specific=simTL4J_literals_FloatLiteral)
gen_simTL4J_literals_DecimalFloatLiteral_FloatLiteral = Generalization(general=FloatLiteral, specific=simTL4J_literals_DecimalFloatLiteral)
gen_simTL4J_literals_HexFloatLiteral_FloatLiteral = Generalization(general=FloatLiteral, specific=simTL4J_literals_HexFloatLiteral)
gen_simTL4J_literals_DoubleLiteral_Literal = Generalization(general=Literal, specific=simTL4J_literals_DoubleLiteral)
gen_simTL4J_literals_DecimalDoubleLiteral_DoubleLiteral = Generalization(general=DoubleLiteral, specific=simTL4J_literals_DecimalDoubleLiteral)
gen_simTL4J_instantiations_Instantiation_generics_TypeArgumentable = Generalization(general=generics_TypeArgumentable, specific=simTL4J_instantiations_Instantiation)
gen_simTL4J_literals_HexDoubleLiteral_DoubleLiteral = Generalization(general=DoubleLiteral, specific=simTL4J_literals_HexDoubleLiteral)
gen_simTL4J_instantiations_NewConstructorCall_instantiations_Instantiation = Generalization(general=instantiations_Instantiation, specific=simTL4J_instantiations_NewConstructorCall)
gen_simTL4J_instantiations_NewConstructorCall_generics_CallTypeArgumentable = Generalization(general=generics_CallTypeArgumentable, specific=simTL4J_instantiations_NewConstructorCall)
gen_simTL4J_literals_IntegerLiteral_Literal = Generalization(general=Literal, specific=simTL4J_literals_IntegerLiteral)
gen_simTL4J_instantiations_ExplicitConstructorCall_Instantiation = Generalization(general=Instantiation, specific=simTL4J_instantiations_ExplicitConstructorCall)
gen_simTL4J_literals_Literal_PrimaryExpression = Generalization(general=PrimaryExpression, specific=simTL4J_literals_Literal)
gen_simTL4J_literals_OctalLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=simTL4J_literals_OctalLongLiteral)
gen_simTL4J_literals_NullLiteral_Literal = Generalization(general=Literal, specific=simTL4J_literals_NullLiteral)
gen_simTL4J_literals_Super_Self = Generalization(general=Self, specific=simTL4J_literals_Super)
gen_simTL4J_literals_This_Self = Generalization(general=Self, specific=simTL4J_literals_This)
gen_simTL4J_members_ExceptionThrower_Commentable = Generalization(general=Commentable, specific=simTL4J_members_ExceptionThrower)
gen_simTL4J_members_Member_NamedElement = Generalization(general=NamedElement, specific=simTL4J_members_Member)
gen_simTL4J_members_MemberContainer_Commentable = Generalization(general=Commentable, specific=simTL4J_members_MemberContainer)
gen_simTL4J_members_AdditionalField_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_members_AdditionalField)
gen_simTL4J_members_AdditionalField_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_members_AdditionalField)
gen_simTL4J_members_AdditionalField_instantiations_Initializable = Generalization(general=instantiations_Initializable, specific=simTL4J_members_AdditionalField)
gen_simTL4J_members_Constructor_members_Member = Generalization(general=members_Member, specific=simTL4J_members_Constructor)
gen_simTL4J_literals_DecimalIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=simTL4J_literals_DecimalIntegerLiteral)
gen_simTL4J_literals_HexIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=simTL4J_literals_HexIntegerLiteral)
gen_simTL4J_literals_OctalIntegerLiteral_IntegerLiteral = Generalization(general=IntegerLiteral, specific=simTL4J_literals_OctalIntegerLiteral)
gen_simTL4J_literals_LongLiteral_Literal = Generalization(general=Literal, specific=simTL4J_literals_LongLiteral)
gen_simTL4J_literals_DecimalLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=simTL4J_literals_DecimalLongLiteral)
gen_simTL4J_literals_HexLongLiteral_LongLiteral = Generalization(general=LongLiteral, specific=simTL4J_literals_HexLongLiteral)
gen_simTL4J_members_Method_members_Member = Generalization(general=members_Member, specific=simTL4J_members_Method)
gen_simTL4J_members_Method_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_members_Method)
gen_simTL4J_members_Method_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_members_Method)
gen_simTL4J_members_Method_generics_TypeParametrizable = Generalization(general=generics_TypeParametrizable, specific=simTL4J_members_Method)
gen_simTL4J_members_Method_parameters_Parametrizable = Generalization(general=parameters_Parametrizable, specific=simTL4J_members_Method)
gen_simTL4J_members_Method_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_members_Method)
gen_simTL4J_members_Method_members_ExceptionThrower = Generalization(general=members_ExceptionThrower, specific=simTL4J_members_Method)
gen_simTL4J_members_Method_modifiers_AnnotableAndModifiable = Generalization(general=modifiers_AnnotableAndModifiable, specific=simTL4J_members_Method)
gen_simTL4J_members_InterfaceMethod_Method = Generalization(general=Method_, specific=simTL4J_members_InterfaceMethod)
gen_simTL4J_members_ClassMethod_members_Method = Generalization(general=members_Method, specific=simTL4J_members_ClassMethod)
gen_simTL4J_members_ClassMethod_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=simTL4J_members_ClassMethod)
gen_simTL4J_members_EnumConstant_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_members_EnumConstant)
gen_simTL4J_members_EnumConstant_references_Argumentable = Generalization(general=references_Argumentable, specific=simTL4J_members_EnumConstant)
gen_simTL4J_members_EnumConstant_annotations_Annotable = Generalization(general=annotations_Annotable, specific=simTL4J_members_EnumConstant)
gen_simTL4J_modifiers_Modifier_AnnotationInstanceOrModifier = Generalization(general=AnnotationInstanceOrModifier, specific=simTL4J_modifiers_Modifier)
gen_simTL4J_modifiers_AnnotationInstanceOrModifier_Commentable = Generalization(general=Commentable, specific=simTL4J_modifiers_AnnotationInstanceOrModifier)
gen_simTL4J_members_Constructor_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=simTL4J_members_Constructor)
gen_simTL4J_members_Constructor_parameters_Parametrizable = Generalization(general=parameters_Parametrizable, specific=simTL4J_members_Constructor)
gen_simTL4J_members_Constructor_generics_TypeParametrizable = Generalization(general=generics_TypeParametrizable, specific=simTL4J_members_Constructor)
gen_simTL4J_members_Constructor_members_ExceptionThrower = Generalization(general=members_ExceptionThrower, specific=simTL4J_members_Constructor)
gen_simTL4J_members_Constructor_modifiers_AnnotableAndModifiable = Generalization(general=modifiers_AnnotableAndModifiable, specific=simTL4J_members_Constructor)
gen_simTL4J_members_EmptyMember_Member = Generalization(general=Member, specific=simTL4J_members_EmptyMember)
gen_simTL4J_members_Field_members_Member = Generalization(general=members_Member, specific=simTL4J_members_Field)
gen_simTL4J_members_Field_instantiations_Initializable = Generalization(general=instantiations_Initializable, specific=simTL4J_members_Field)
gen_simTL4J_members_Field_variables_Variable = Generalization(general=variables_Variable, specific=simTL4J_members_Field)
gen_simTL4J_members_Field_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_members_Field)
gen_simTL4J_members_Field_modifiers_AnnotableAndModifiable = Generalization(general=modifiers_AnnotableAndModifiable, specific=simTL4J_members_Field)
gen_simTL4J_modifiers_Modifiable_Commentable = Generalization(general=Commentable, specific=simTL4J_modifiers_Modifiable)
gen_simTL4J_modifiers_Abstract_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Abstract)
gen_simTL4J_modifiers_Final_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Final)
gen_simTL4J_modifiers_Native_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Native)
gen_simTL4J_modifiers_Protected_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Protected)
gen_simTL4J_modifiers_Public_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Public)
gen_simTL4J_modifiers_Private_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Private)
gen_simTL4J_modifiers_Static_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Static)
gen_simTL4J_modifiers_Strictfp_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Strictfp)
gen_simTL4J_modifiers_Synchronized_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Synchronized)
gen_simTL4J_modifiers_Transient_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Transient)
gen_simTL4J_modifiers_Volatile_Modifier = Generalization(general=Modifier, specific=simTL4J_modifiers_Volatile)
gen_simTL4J_operators_Operator_Commentable = Generalization(general=Commentable, specific=simTL4J_operators_Operator)
gen_simTL4J_operators_AdditiveOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_AdditiveOperator)
gen_simTL4J_modifiers_AnnotableAndModifiable_Commentable = Generalization(general=Commentable, specific=simTL4J_modifiers_AnnotableAndModifiable)
gen_simTL4J_operators_UnaryModificationOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_UnaryModificationOperator)
gen_simTL4J_operators_Assignment_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_Assignment)
gen_simTL4J_operators_AssignmentAnd_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentAnd)
gen_simTL4J_operators_AssignmentDivision_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentDivision)
gen_simTL4J_operators_AssignmentExclusiveOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentExclusiveOr)
gen_simTL4J_operators_AssignmentMinus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentMinus)
gen_simTL4J_operators_AssignmentModulo_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentModulo)
gen_simTL4J_operators_AssignmentMultiplication_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentMultiplication)
gen_simTL4J_operators_AssignmentLeftShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentLeftShift)
gen_simTL4J_operators_AssignmentOr_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentOr)
gen_simTL4J_operators_AssignmentPlus_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentPlus)
gen_simTL4J_operators_AssignmentRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentRightShift)
gen_simTL4J_operators_AssignmentUnsignedRightShift_AssignmentOperator = Generalization(general=AssignmentOperator, specific=simTL4J_operators_AssignmentUnsignedRightShift)
gen_simTL4J_operators_Equal_EqualityOperator = Generalization(general=EqualityOperator, specific=simTL4J_operators_Equal)
gen_simTL4J_operators_NotEqual_EqualityOperator = Generalization(general=EqualityOperator, specific=simTL4J_operators_NotEqual)
gen_simTL4J_operators_GreaterThan_RelationOperator = Generalization(general=RelationOperator, specific=simTL4J_operators_GreaterThan)
gen_simTL4J_operators_GreaterThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=simTL4J_operators_GreaterThanOrEqual)
gen_simTL4J_operators_LessThan_RelationOperator = Generalization(general=RelationOperator, specific=simTL4J_operators_LessThan)
gen_simTL4J_operators_AssignmentOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_AssignmentOperator)
gen_simTL4J_operators_EqualityOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_EqualityOperator)
gen_simTL4J_operators_MultiplicativeOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_MultiplicativeOperator)
gen_simTL4J_operators_RelationOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_RelationOperator)
gen_simTL4J_operators_ShiftOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_ShiftOperator)
gen_simTL4J_operators_UnaryOperator_Operator = Generalization(general=Operator, specific=simTL4J_operators_UnaryOperator)
gen_simTL4J_operators_Complement_UnaryOperator = Generalization(general=UnaryOperator, specific=simTL4J_operators_Complement)
gen_simTL4J_operators_MinusMinus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=simTL4J_operators_MinusMinus)
gen_simTL4J_operators_Negate_UnaryOperator = Generalization(general=UnaryOperator, specific=simTL4J_operators_Negate)
gen_simTL4J_operators_PlusPlus_UnaryModificationOperator = Generalization(general=UnaryModificationOperator, specific=simTL4J_operators_PlusPlus)
gen_simTL4J_operators_LeftShift_ShiftOperator = Generalization(general=ShiftOperator, specific=simTL4J_operators_LeftShift)
gen_simTL4J_operators_RightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=simTL4J_operators_RightShift)
gen_simTL4J_operators_UnsignedRightShift_ShiftOperator = Generalization(general=ShiftOperator, specific=simTL4J_operators_UnsignedRightShift)
gen_simTL4J_parameters_Parameter_variables_Variable = Generalization(general=variables_Variable, specific=simTL4J_parameters_Parameter)
gen_simTL4J_parameters_Parameter_modifiers_AnnotableAndModifiable = Generalization(general=modifiers_AnnotableAndModifiable, specific=simTL4J_parameters_Parameter)
gen_simTL4J_parameters_Parametrizable_Commentable = Generalization(general=Commentable, specific=simTL4J_parameters_Parametrizable)
gen_simTL4J_parameters_OrdinaryParameter_Parameter = Generalization(general=Parameter_, specific=simTL4J_parameters_OrdinaryParameter)
gen_simTL4J_parameters_VariableLengthParameter_Parameter = Generalization(general=Parameter_, specific=simTL4J_parameters_VariableLengthParameter)
gen_simTL4J_references_Reference_expressions_PrimaryExpression = Generalization(general=expressions_PrimaryExpression, specific=simTL4J_references_Reference)
gen_simTL4J_references_Reference_generics_TypeArgumentable = Generalization(general=generics_TypeArgumentable, specific=simTL4J_references_Reference)
gen_simTL4J_operators_LessThanOrEqual_RelationOperator = Generalization(general=RelationOperator, specific=simTL4J_operators_LessThanOrEqual)
gen_simTL4J_operators_Addition_operators_AdditiveOperator = Generalization(general=operators_AdditiveOperator, specific=simTL4J_operators_Addition)
gen_simTL4J_operators_Addition_operators_UnaryOperator = Generalization(general=operators_UnaryOperator, specific=simTL4J_operators_Addition)
gen_simTL4J_operators_Subtraction_operators_AdditiveOperator = Generalization(general=operators_AdditiveOperator, specific=simTL4J_operators_Subtraction)
gen_simTL4J_operators_Subtraction_operators_UnaryOperator = Generalization(general=operators_UnaryOperator, specific=simTL4J_operators_Subtraction)
gen_simTL4J_operators_Division_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=simTL4J_operators_Division)
gen_simTL4J_operators_Multiplication_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=simTL4J_operators_Multiplication)
gen_simTL4J_operators_Remainder_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=simTL4J_operators_Remainder)
gen_simTL4J_references_Argumentable_Commentable = Generalization(general=Commentable, specific=simTL4J_references_Argumentable)
gen_simTL4J_references_ReferenceableElement_NamedElement = Generalization(general=NamedElement, specific=simTL4J_references_ReferenceableElement)
gen_simTL4J_references_ElementReference_Reference = Generalization(general=Reference, specific=simTL4J_references_ElementReference)
gen_simTL4J_references_IdentifierReference_ElementReference = Generalization(general=ElementReference, specific=simTL4J_references_IdentifierReference)
gen_simTL4J_references_MethodCall_references_ElementReference = Generalization(general=references_ElementReference, specific=simTL4J_references_MethodCall)
gen_simTL4J_references_MethodCall_references_Argumentable = Generalization(general=references_Argumentable, specific=simTL4J_references_MethodCall)
gen_simTL4J_references_MethodCall_generics_CallTypeArgumentable = Generalization(general=generics_CallTypeArgumentable, specific=simTL4J_references_MethodCall)
gen_simTL4J_references_ReflectiveClassReference_Reference = Generalization(general=Reference, specific=simTL4J_references_ReflectiveClassReference)
gen_simTL4J_references_PrimitiveTypeReference_Reference = Generalization(general=Reference, specific=simTL4J_references_PrimitiveTypeReference)
gen_simTL4J_references_StringReference_Reference = Generalization(general=Reference, specific=simTL4J_references_StringReference)
gen_simTL4J_references_SelfReference_Reference = Generalization(general=Reference, specific=simTL4J_references_SelfReference)
gen_simTL4J_statements_StatementContainer_Commentable = Generalization(general=Commentable, specific=simTL4J_statements_StatementContainer)
gen_simTL4J_statements_Conditional_Commentable = Generalization(general=Commentable, specific=simTL4J_statements_Conditional)
gen_simTL4J_statements_ForLoopInitializer_Commentable = Generalization(general=Commentable, specific=simTL4J_statements_ForLoopInitializer)
gen_simTL4J_statements_Statement_Commentable = Generalization(general=Commentable, specific=simTL4J_statements_Statement)
gen_simTL4J_statements_SwitchCase_StatementListContainer = Generalization(general=StatementListContainer, specific=simTL4J_statements_SwitchCase)
gen_simTL4J_statements_Assert_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_Assert)
gen_simTL4J_statements_Assert_statements_Conditional = Generalization(general=statements_Conditional, specific=simTL4J_statements_Assert)
gen_simTL4J_statements_Break_Jump = Generalization(general=Jump, specific=simTL4J_statements_Break)
gen_simTL4J_statements_Block_members_Member = Generalization(general=members_Member, specific=simTL4J_statements_Block)
gen_simTL4J_statements_Block_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_Block)
gen_simTL4J_statements_Block_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=simTL4J_statements_Block)
gen_simTL4J_statements_Block_modifiers_Modifiable = Generalization(general=modifiers_Modifiable, specific=simTL4J_statements_Block)
gen_simTL4J_statements_StatementListContainer_Commentable = Generalization(general=Commentable, specific=simTL4J_statements_StatementListContainer)
gen_simTL4J_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=simTL4J_statements_EmptyStatement)
gen_simTL4J_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=simTL4J_statements_ExpressionStatement)
gen_simTL4J_statements_ForLoop_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_ForLoop)
gen_simTL4J_statements_ForLoop_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=simTL4J_statements_ForLoop)
gen_simTL4J_statements_ForLoop_statements_Conditional = Generalization(general=statements_Conditional, specific=simTL4J_statements_ForLoop)
gen_simTL4J_statements_ForEachLoop_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_ForEachLoop)
gen_simTL4J_statements_ForEachLoop_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=simTL4J_statements_ForEachLoop)
gen_simTL4J_statements_CatchBlock_StatementListContainer = Generalization(general=StatementListContainer, specific=simTL4J_statements_CatchBlock)
gen_simTL4J_statements_Condition_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_Condition)
gen_simTL4J_statements_Condition_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=simTL4J_statements_Condition)
gen_simTL4J_statements_Condition_statements_Conditional = Generalization(general=statements_Conditional, specific=simTL4J_statements_Condition)
gen_simTL4J_statements_Continue_Jump = Generalization(general=Jump, specific=simTL4J_statements_Continue)
gen_simTL4J_statements_DefaultSwitchCase_SwitchCase = Generalization(general=SwitchCase, specific=simTL4J_statements_DefaultSwitchCase)
gen_simTL4J_statements_DoWhileLoop_WhileLoop = Generalization(general=WhileLoop, specific=simTL4J_statements_DoWhileLoop)
gen_simTL4J_statements_Return_Statement = Generalization(general=Statement, specific=simTL4J_statements_Return)
gen_simTL4J_statements_Switch_Statement = Generalization(general=Statement, specific=simTL4J_statements_Switch)
gen_simTL4J_statements_SynchronizedBlock_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_SynchronizedBlock)
gen_simTL4J_statements_SynchronizedBlock_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=simTL4J_statements_SynchronizedBlock)
gen_simTL4J_statements_Throw_Statement = Generalization(general=Statement, specific=simTL4J_statements_Throw)
gen_simTL4J_statements_TryBlock_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_TryBlock)
gen_simTL4J_statements_TryBlock_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=simTL4J_statements_TryBlock)
gen_simTL4J_statements_WhileLoop_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_WhileLoop)
gen_simTL4J_statements_WhileLoop_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=simTL4J_statements_WhileLoop)
gen_simTL4J_statements_Jump_Statement = Generalization(general=Statement, specific=simTL4J_statements_Jump)
gen_simTL4J_statements_JumpLabel_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_statements_JumpLabel)
gen_simTL4J_statements_JumpLabel_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=simTL4J_statements_JumpLabel)
gen_simTL4J_statements_JumpLabel_commons_NamedElement = Generalization(general=commons_NamedElement, specific=simTL4J_statements_JumpLabel)
gen_simTL4J_statements_LocalVariableStatement_Statement = Generalization(general=Statement, specific=simTL4J_statements_LocalVariableStatement)
gen_simTL4J_statements_NormalSwitchCase_statements_SwitchCase = Generalization(general=statements_SwitchCase, specific=simTL4J_statements_NormalSwitchCase)
gen_simTL4J_statements_NormalSwitchCase_statements_Conditional = Generalization(general=statements_Conditional, specific=simTL4J_statements_NormalSwitchCase)
gen_simTL4J_types_TypedElement_Commentable = Generalization(general=Commentable, specific=simTL4J_types_TypedElement)
gen_simTL4J_types_TypeReference_Commentable = Generalization(general=Commentable, specific=simTL4J_types_TypeReference)
gen_simTL4J_types_ClassifierReference_types_TypeReference = Generalization(general=types_TypeReference, specific=simTL4J_types_ClassifierReference)
gen_simTL4J_types_ClassifierReference_generics_TypeArgumentable = Generalization(general=generics_TypeArgumentable, specific=simTL4J_types_ClassifierReference)
gen_simTL4J_types_NamespaceClassifierReference_types_TypeReference = Generalization(general=types_TypeReference, specific=simTL4J_types_NamespaceClassifierReference)
gen_simTL4J_types_NamespaceClassifierReference_commons_NamespaceAwareElement = Generalization(general=commons_NamespaceAwareElement, specific=simTL4J_types_NamespaceClassifierReference)
gen_simTL4J_types_PrimitiveType_types_Type = Generalization(general=types_Type, specific=simTL4J_types_PrimitiveType)
gen_simTL4J_types_PrimitiveType_types_TypeReference = Generalization(general=types_TypeReference, specific=simTL4J_types_PrimitiveType)
gen_simTL4J_types_Type_Commentable = Generalization(general=Commentable, specific=simTL4J_types_Type)
gen_simTL4J_variables_Variable_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_variables_Variable)
gen_simTL4J_variables_Variable_generics_TypeArgumentable = Generalization(general=generics_TypeArgumentable, specific=simTL4J_variables_Variable)
gen_simTL4J_variables_LocalVariable_variables_Variable = Generalization(general=variables_Variable, specific=simTL4J_variables_LocalVariable)
gen_simTL4J_variables_LocalVariable_instantiations_Initializable = Generalization(general=instantiations_Initializable, specific=simTL4J_variables_LocalVariable)
gen_simTL4J_variables_LocalVariable_statements_ForLoopInitializer = Generalization(general=statements_ForLoopInitializer, specific=simTL4J_variables_LocalVariable)
gen_simTL4J_variables_LocalVariable_modifiers_AnnotableAndModifiable = Generalization(general=modifiers_AnnotableAndModifiable, specific=simTL4J_variables_LocalVariable)
gen_simTL4J_variables_AdditionalLocalVariable_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=simTL4J_variables_AdditionalLocalVariable)
gen_simTL4J_variables_AdditionalLocalVariable_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_variables_AdditionalLocalVariable)
gen_simTL4J_variables_AdditionalLocalVariable_instantiations_Initializable = Generalization(general=instantiations_Initializable, specific=simTL4J_variables_AdditionalLocalVariable)
gen_simTL4J_types_Boolean_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Boolean)
gen_simTL4J_types_Byte_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Byte)
gen_simTL4J_types_Char_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Char)
gen_simTL4J_types_Double_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Double)
gen_simTL4J_types_Float_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Float)
gen_simTL4J_types_Int_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Int)
gen_simTL4J_types_Long_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Long)
gen_simTL4J_types_Short_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Short)
gen_simTL4J_types_Void_PrimitiveType = Generalization(general=PrimitiveType, specific=simTL4J_types_Void)
gen_simTL4J_variables_Variable_commons_NamedElement = Generalization(general=commons_NamedElement, specific=simTL4J_variables_Variable)
gen_simTL4J_variables_Variable_types_TypedElement = Generalization(general=types_TypedElement, specific=simTL4J_variables_Variable)
gen_simTL4J_variables_Variable_arrays_ArrayTypeable = Generalization(general=arrays_ArrayTypeable, specific=simTL4J_variables_Variable)
gen_simTL4J_simTL_TFor_MemberContainer_simTL_TFor = Generalization(general=simTL_TFor, specific=simTL4J_simTL_TFor_MemberContainer)
gen_simTL4J_simTL_TFor_MemberContainer_members_MemberContainer = Generalization(general=members_MemberContainer, specific=simTL4J_simTL_TFor_MemberContainer)
gen_simTL4J_simTL_TFor_MemberContainer_members_Member = Generalization(general=members_Member, specific=simTL4J_simTL_TFor_MemberContainer)
gen_simTL4J_simTL_TFor_StatementListContainer_simTL_TFor = Generalization(general=simTL_TFor, specific=simTL4J_simTL_TFor_StatementListContainer)
gen_simTL4J_simTL_TFor_StatementListContainer_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=simTL4J_simTL_TFor_StatementListContainer)
gen_simTL4J_simTL_TFor_StatementListContainer_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_simTL_TFor_StatementListContainer)
gen_simTL4J_simTL_TIf_MemberContainer_simTL_TIf = Generalization(general=simTL_TIf, specific=simTL4J_simTL_TIf_MemberContainer)
gen_simTL4J_simTL_TIf_MemberContainer_members_MemberContainer = Generalization(general=members_MemberContainer, specific=simTL4J_simTL_TIf_MemberContainer)
gen_simTL4J_simTL_TIf_MemberContainer_members_Member = Generalization(general=members_Member, specific=simTL4J_simTL_TIf_MemberContainer)
gen_simTL4J_simTL_TIf_StatementListContainer_simTL_TIf = Generalization(general=simTL_TIf, specific=simTL4J_simTL_TIf_StatementListContainer)
gen_simTL4J_simTL_TIf_StatementListContainer_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=simTL4J_simTL_TIf_StatementListContainer)
gen_simTL4J_simTL_TIf_StatementListContainer_statements_Statement = Generalization(general=statements_Statement, specific=simTL4J_simTL_TIf_StatementListContainer)
gen_simTL4J_simTL_TPlaceholder_PrimaryExpression_simTL_TPlaceholder = Generalization(general=simTL_TPlaceholder, specific=simTL4J_simTL_TPlaceholder_PrimaryExpression)
gen_simTL4J_simTL_TPlaceholder_PrimaryExpression_expressions_PrimaryExpression = Generalization(general=expressions_PrimaryExpression, specific=simTL4J_simTL_TPlaceholder_PrimaryExpression)
gen_simTL4J_simTL_TUnaryOperator_TAbstractMethodStatement = Generalization(general=TAbstractMethodStatement, specific=simTL4J_simTL_TUnaryOperator)
gen_simTL4J_simTL_TUnaryOperatorNOT_TUnaryOperator = Generalization(general=TUnaryOperator, specific=simTL4J_simTL_TUnaryOperatorNOT)
gen_simTL4J_simTL_TMethodStatementImpl_TAbstractMethodStatement = Generalization(general=TAbstractMethodStatement, specific=simTL4J_simTL_TMethodStatementImpl)

# Domain Model
domain_model = DomainModel(
    name="simTL4J",
    types={simTL4J_annotations_Annotable, Commentable, simTL4J_annotations_AnnotationInstance, references_Reference, modifiers_AnnotationInstanceOrModifier, commons_NamespaceAwareElement, Classifier, AnnotationParameter, simTL4J_annotations_AnnotationParameter, simTL4J_annotations_SingleAnnotationParameter, AnnotationValue, simTL4J_annotations_AnnotationParameterList, AnnotationInstance, simTL4J_annotations_AnnotationAttributeSetting, InterfaceMethod, simTL4J_annotations_AnnotationValue, AnnotationAttributeSetting, simTL4J_arrays_ArrayTypeable, ArrayDimension, simTL4J_annotations_AnnotationAttribute, Expression, types_TypedElement, arrays_ArrayTypeable, simTL4J_arrays_ArrayInstantiationByValues, ArrayInitializer, simTL4J_arrays_ArraySelector, simTL4J_classifiers_Classifier, types_Type, references_ReferenceableElement, simTL4J_arrays_ArrayDimension, simTL4J_arrays_ArrayInitializer, arrays_ArrayInitializationValue, annotations_AnnotationValue, ArrayInitializationValue, simTL4J_arrays_ArrayInitializationValue, simTL4J_arrays_ArrayInstantiationBySize, expressions_Expression, simTL4J_classifiers_Implementor, TypeReference, simTL4J_classifiers_ConcreteClassifier, classifiers_Classifier, generics_TypeParametrizable, members_MemberContainer, members_Member, statements_Statement, modifiers_AnnotableAndModifiable, simTL4J_classifiers_Interface, ConcreteClassifier, simTL4J_classifiers_Enumeration, simTL4J_classifiers_Class, classifiers_ConcreteClassifier, classifiers_Implementor, simTL4J_classifiers_AnonymousClass, simTL4J_commons_Commentable, EnumConstant, simTL4J_classifiers_Annotation, simTL4J_commons_NamedElement, TPlaceholder, simTL4J_commons_NamespaceAwareElement, simTL4J_containers_JavaRoot, commons_NamedElement, imports_ImportingElement, simTL4J_containers_CompilationUnit, JavaRoot, simTL4J_containers_EmptyModel, simTL4J_expressions_ExpressionList, ForLoopInitializer, simTL4J_expressions_Expression, simTL4J_expressions_AssignmentExpression, AssignmentExpressionChild, AssignmentOperator, simTL4J_expressions_AssignmentExpressionChild, simTL4J_expressions_ConditionalExpression, ConditionalExpressionChild, simTL4J_containers_Package, containers_JavaRoot, annotations_Annotable, CompilationUnit, Package, ConditionalAndExpressionChild, simTL4J_expressions_ConditionalAndExpressionChild, simTL4J_expressions_InclusiveOrExpression, InclusiveOrExpressionChild, simTL4J_expressions_InclusiveOrExpressionChild, simTL4J_expressions_ExclusiveOrExpression, ExclusiveOrExpressionChild, simTL4J_expressions_ExclusiveOrExpressionChild, simTL4J_expressions_AndExpression, AndExpressionChild, simTL4J_expressions_AndExpressionChild, simTL4J_expressions_EqualityExpression, EqualityOperator, EqualityExpressionChild, simTL4J_expressions_EqualityExpressionChild, simTL4J_expressions_InstanceOfExpression, expressions_EqualityExpressionChild, InstanceOfExpressionChild, simTL4J_expressions_InstanceOfExpressionChild, simTL4J_expressions_ConditionalExpressionChild, simTL4J_expressions_ConditionalOrExpression, ConditionalOrExpressionChild, simTL4J_expressions_ConditionalOrExpressionChild, simTL4J_expressions_ConditionalAndExpression, ShiftExpressionChild, ShiftOperator, simTL4J_expressions_ShiftExpressionChild, simTL4J_expressions_AdditiveExpression, AdditiveExpressionChild, AdditiveOperator, simTL4J_expressions_AdditiveExpressionChild, simTL4J_expressions_MultiplicativeExpression, MultiplicativeExpressionChild, MultiplicativeOperator, simTL4J_expressions_MultiplicativeExpressionChild, simTL4J_expressions_UnaryExpression, simTL4J_expressions_RelationExpression, RelationExpressionChild, RelationOperator, simTL4J_expressions_RelationExpressionChild, simTL4J_expressions_ShiftExpression, UnaryModificationExpressionChild, UnaryModificationOperator, simTL4J_expressions_PrefixUnaryModificationExpression, UnaryModificationExpression, simTL4J_expressions_SuffixUnaryModificationExpression, simTL4J_expressions_UnaryModificationExpressionChild, simTL4J_expressions_CastExpression, expressions_UnaryModificationExpressionChild, simTL4J_expressions_PrimaryExpression, simTL4J_expressions_NestedExpression, Reference, UnaryOperator, UnaryExpressionChild, simTL4J_expressions_UnaryExpressionChild, simTL4J_expressions_UnaryModificationExpression, simTL4J_generics_TypeParametrizable, TypeParameter, simTL4J_generics_ExtendsTypeArgument, simTL4J_generics_QualifiedTypeArgument, generics_TypeArgument, simTL4J_generics_SuperTypeArgument, simTL4J_generics_TypeParameter, simTL4J_generics_TypeArgument, ArrayTypeable, simTL4J_generics_TypeArgumentable, TypeArgument, simTL4J_generics_CallTypeArgumentable, simTL4J_imports_Import, NamespaceAwareElement, simTL4J_imports_ImportingElement, Import, simTL4J_imports_StaticImport, Static, simTL4J_generics_UnknownTypeArgument, simTL4J_imports_PackageImport, simTL4J_imports_StaticClassifierImport, StaticImport, simTL4J_imports_StaticMemberImport, ReferenceableElement, simTL4J_instantiations_Initializable, simTL4J_instantiations_Instantiation, references_Argumentable, generics_TypeArgumentable, simTL4J_imports_ClassifierImport, simTL4J_literals_Self, simTL4J_literals_BooleanLiteral, Literal, simTL4J_literals_CharacterLiteral, simTL4J_literals_FloatLiteral, simTL4J_literals_DecimalFloatLiteral, FloatLiteral, simTL4J_literals_HexFloatLiteral, simTL4J_literals_DoubleLiteral, simTL4J_literals_DecimalDoubleLiteral, DoubleLiteral, simTL4J_literals_HexDoubleLiteral, simTL4J_instantiations_NewConstructorCall, instantiations_Instantiation, generics_CallTypeArgumentable, simTL4J_literals_IntegerLiteral, AnonymousClass, simTL4J_instantiations_ExplicitConstructorCall, Instantiation, Self, simTL4J_literals_Literal, PrimaryExpression, simTL4J_literals_OctalLongLiteral, simTL4J_literals_NullLiteral, simTL4J_literals_Super, simTL4J_literals_This, simTL4J_members_ExceptionThrower, NamespaceClassifierReference, simTL4J_members_Member, NamedElement, simTL4J_members_MemberContainer, Member, simTL4J_members_AdditionalField, instantiations_Initializable, simTL4J_members_Constructor, statements_StatementListContainer, simTL4J_literals_DecimalIntegerLiteral, IntegerLiteral, simTL4J_literals_HexIntegerLiteral, simTL4J_literals_OctalIntegerLiteral, simTL4J_literals_LongLiteral, simTL4J_literals_DecimalLongLiteral, LongLiteral, simTL4J_literals_HexLongLiteral, simTL4J_members_Method, simTL4J_members_InterfaceMethod, Method_, simTL4J_members_ClassMethod, members_Method, simTL4J_members_EnumConstant, simTL4J_modifiers_Modifier, AnnotationInstanceOrModifier, simTL4J_modifiers_AnnotationInstanceOrModifier, parameters_Parametrizable, members_ExceptionThrower, simTL4J_members_EmptyMember, simTL4J_members_Field, variables_Variable, AdditionalField, simTL4J_modifiers_Modifiable, Modifier, simTL4J_modifiers_Abstract, simTL4J_modifiers_Final, simTL4J_modifiers_Native, simTL4J_modifiers_Protected, simTL4J_modifiers_Public, simTL4J_modifiers_Private, simTL4J_modifiers_Static, simTL4J_modifiers_Strictfp, simTL4J_modifiers_Synchronized, simTL4J_modifiers_Transient, simTL4J_modifiers_Volatile, simTL4J_operators_Operator, simTL4J_operators_AdditiveOperator, Operator, simTL4J_modifiers_AnnotableAndModifiable, simTL4J_operators_UnaryModificationOperator, simTL4J_operators_Assignment, simTL4J_operators_AssignmentAnd, simTL4J_operators_AssignmentDivision, simTL4J_operators_AssignmentExclusiveOr, simTL4J_operators_AssignmentMinus, simTL4J_operators_AssignmentModulo, simTL4J_operators_AssignmentMultiplication, simTL4J_operators_AssignmentLeftShift, simTL4J_operators_AssignmentOr, simTL4J_operators_AssignmentPlus, simTL4J_operators_AssignmentRightShift, simTL4J_operators_AssignmentUnsignedRightShift, simTL4J_operators_Equal, simTL4J_operators_NotEqual, simTL4J_operators_GreaterThan, simTL4J_operators_GreaterThanOrEqual, simTL4J_operators_LessThan, simTL4J_operators_AssignmentOperator, simTL4J_operators_EqualityOperator, simTL4J_operators_MultiplicativeOperator, simTL4J_operators_RelationOperator, simTL4J_operators_ShiftOperator, simTL4J_operators_UnaryOperator, simTL4J_operators_Complement, simTL4J_operators_MinusMinus, simTL4J_operators_Negate, simTL4J_operators_PlusPlus, simTL4J_operators_LeftShift, simTL4J_operators_RightShift, simTL4J_operators_UnsignedRightShift, simTL4J_parameters_Parameter, simTL4J_parameters_Parametrizable, Parameter_, simTL4J_parameters_OrdinaryParameter, simTL4J_parameters_VariableLengthParameter, simTL4J_references_Reference, expressions_PrimaryExpression, simTL4J_operators_LessThanOrEqual, simTL4J_operators_Addition, operators_AdditiveOperator, operators_UnaryOperator, simTL4J_operators_Subtraction, simTL4J_operators_Division, simTL4J_operators_Multiplication, simTL4J_operators_Remainder, simTL4J_references_Argumentable, simTL4J_references_ReferenceableElement, simTL4J_references_ElementReference, simTL4J_references_IdentifierReference, ElementReference, simTL4J_references_MethodCall, references_ElementReference, simTL4J_references_ReflectiveClassReference, simTL4J_references_PrimitiveTypeReference, PrimitiveType, simTL4J_references_StringReference, ArraySelector, simTL4J_references_SelfReference, simTL4J_statements_StatementContainer, Statement, simTL4J_statements_Conditional, simTL4J_statements_ForLoopInitializer, simTL4J_statements_Statement, simTL4J_statements_SwitchCase, StatementListContainer, simTL4J_statements_Assert, statements_Conditional, simTL4J_statements_Break, Jump, simTL4J_statements_Block, modifiers_Modifiable, simTL4J_statements_CatchBlock, simTL4J_statements_StatementListContainer, simTL4J_statements_EmptyStatement, simTL4J_statements_ExpressionStatement, simTL4J_statements_ForLoop, simTL4J_statements_ForEachLoop, OrdinaryParameter, simTL4J_statements_Condition, statements_StatementContainer, simTL4J_statements_Continue, simTL4J_statements_DefaultSwitchCase, SwitchCase, simTL4J_statements_DoWhileLoop, WhileLoop, simTL4J_statements_Return, simTL4J_statements_Switch, simTL4J_statements_SynchronizedBlock, simTL4J_statements_Throw, simTL4J_statements_TryBlock, CatchBlock, Block, simTL4J_statements_WhileLoop, simTL4J_statements_Jump, JumpLabel, simTL4J_statements_JumpLabel, simTL4J_statements_LocalVariableStatement, LocalVariable, simTL4J_statements_NormalSwitchCase, statements_SwitchCase, simTL4J_types_TypedElement, simTL4J_types_TypeReference, simTL4J_types_ClassifierReference, types_TypeReference, simTL4J_types_NamespaceClassifierReference, ClassifierReference, simTL4J_types_PrimitiveType, simTL4J_types_Type, simTL4J_variables_LocalVariable, statements_ForLoopInitializer, AdditionalLocalVariable, simTL4J_variables_AdditionalLocalVariable, simTL4J_simTL_TIf, TAbstractMethodStatement, simTL4J_simTL_TFor, TForVariable, simTL4J_simTL_TForVariable, simTL4J_types_Boolean, simTL4J_types_Byte, simTL4J_types_Char, simTL4J_types_Double, simTL4J_types_Float, simTL4J_types_Int, simTL4J_types_Long, simTL4J_types_Short, simTL4J_types_Void, simTL4J_variables_Variable, TModelImport, simTL4J_simTL_TModelImport, simTL4J_simTL_TMethodCall, simTL4J_simTL_TAbstractMethodStatement, simTL4J_simTL_TFor_MemberContainer, simTL_TFor, simTL4J_simTL_TFor_StatementListContainer, simTL4J_simTL_Template, TemplateHeader, simTL4J_simTL_TemplateHeader, simTL_TIf, simTL4J_simTL_TIf_StatementListContainer, simTL4J_simTL_TPlaceholder, simTL4J_simTL_TPlaceholder_PrimaryExpression, simTL_TPlaceholder, simTL4J_simTL_TUnaryOperator, simTL4J_simTL_TIf_MemberContainer, simTL4J_simTL_TUnaryOperatorNOT, TUnaryOperator, simTL4J_simTL_TMethodStatementImpl, TMethodCall},
    associations={annotation1, parameter2, value4, annotations0, settings5, attribute6, value7, arrayDimensionsBefore11, arrayDimensionsAfter12, defaultValue10, sizes16, arrayInitializer18, position19, initialValues15, implements21, extends22, defaultExtends24, extends27, defaultExtends29, constants32, name_PH33, expressions38, child40, assignmentOperator41, value43, child46, classifiers34, compilationUnits35, subpackages36, children54, children55, children56, children57, equalityOperators58, children59, child61, expressionIf47, expressionElse50, children53, children65, shiftOperators66, children68, additiveOperators69, children71, multiplicativeOperators72, children62, relationOperators63, child77, operator78, child80, expression82, operators74, child75, typeParameters87, extendTypes88, superType90, typeArguments84, callTypeArguments85, imports94, static95, extendTypes92, classifier96, staticMembers98, initialValue99, anonymousClass101, callTarget102, exceptions103, members104, defaultMembers105, anonymousClass109, additionalFields108, annotationsAndModifiers111, modifiers112, parameters113, arguments117, target119, primitiveType121, next114, arraySelectors115, statement124, self122, condition127, errorMessage129, statements125, expression134, init136, updates137, next140, collection142, parameter131, elseStatement132, returnValue147, cases149, variable150, lockProvider153, throwable155, catcheBlocks157, finallyBlock158, target145, variable146, typeReference162, target164, classifierReferences166, condition160, additionalLocalVariables167, condition168, count169, modelImports175, setToBeIterated170, templateHeader172, class173, methodStatement176, methodStatement178, callee180},
    generalizations={gen_simTL4J_annotations_Annotable_Commentable, gen_simTL4J_annotations_AnnotationInstance_references_Reference, gen_simTL4J_annotations_AnnotationInstance_modifiers_AnnotationInstanceOrModifier, gen_simTL4J_annotations_AnnotationInstance_commons_NamespaceAwareElement, gen_simTL4J_annotations_AnnotationParameter_Commentable, gen_simTL4J_annotations_SingleAnnotationParameter_AnnotationParameter, gen_simTL4J_annotations_AnnotationAttributeSetting_Commentable, gen_simTL4J_annotations_AnnotationValue_Commentable, gen_simTL4J_annotations_AnnotationParameterList_AnnotationParameter, gen_simTL4J_arrays_ArrayTypeable_Commentable, gen_simTL4J_annotations_AnnotationAttribute_InterfaceMethod, gen_simTL4J_arrays_ArrayInstantiationBySize_types_TypedElement, gen_simTL4J_arrays_ArrayInstantiationBySize_arrays_ArrayTypeable, gen_simTL4J_arrays_ArrayInstantiationBySize_references_Reference, gen_simTL4J_arrays_ArrayInstantiationByValues_expressions_Expression, gen_simTL4J_arrays_ArrayInstantiationByValues_types_TypedElement, gen_simTL4J_arrays_ArrayInstantiationByValues_arrays_ArrayTypeable, gen_simTL4J_arrays_ArrayInstantiationByValues_references_Reference, gen_simTL4J_arrays_ArraySelector_Commentable, gen_simTL4J_classifiers_Classifier_types_Type, gen_simTL4J_arrays_ArrayDimension_Commentable, gen_simTL4J_arrays_ArrayInitializer_arrays_ArrayInitializationValue, gen_simTL4J_arrays_ArrayInitializer_annotations_AnnotationValue, gen_simTL4J_arrays_ArrayInitializationValue_Commentable, gen_simTL4J_arrays_ArrayInstantiationBySize_expressions_Expression, gen_simTL4J_classifiers_Implementor_Commentable, gen_simTL4J_classifiers_Classifier_references_ReferenceableElement, gen_simTL4J_classifiers_ConcreteClassifier_classifiers_Classifier, gen_simTL4J_classifiers_ConcreteClassifier_generics_TypeParametrizable, gen_simTL4J_classifiers_ConcreteClassifier_members_MemberContainer, gen_simTL4J_classifiers_ConcreteClassifier_members_Member, gen_simTL4J_classifiers_ConcreteClassifier_statements_Statement, gen_simTL4J_classifiers_ConcreteClassifier_modifiers_AnnotableAndModifiable, gen_simTL4J_classifiers_Interface_ConcreteClassifier, gen_simTL4J_classifiers_Enumeration_classifiers_ConcreteClassifier, gen_simTL4J_classifiers_Enumeration_classifiers_Implementor, gen_simTL4J_classifiers_Class_classifiers_ConcreteClassifier, gen_simTL4J_classifiers_Class_classifiers_Implementor, gen_simTL4J_classifiers_AnonymousClass_types_Type, gen_simTL4J_classifiers_AnonymousClass_members_MemberContainer, gen_simTL4J_classifiers_Annotation_ConcreteClassifier, gen_simTL4J_commons_NamedElement_Commentable, gen_simTL4J_commons_NamespaceAwareElement_Commentable, gen_simTL4J_containers_JavaRoot_commons_NamedElement, gen_simTL4J_containers_JavaRoot_commons_NamespaceAwareElement, gen_simTL4J_containers_JavaRoot_imports_ImportingElement, gen_simTL4J_containers_CompilationUnit_JavaRoot, gen_simTL4J_containers_EmptyModel_JavaRoot, gen_simTL4J_expressions_ExpressionList_ForLoopInitializer, gen_simTL4J_expressions_Expression_arrays_ArrayInitializationValue, gen_simTL4J_expressions_Expression_annotations_AnnotationValue, gen_simTL4J_expressions_AssignmentExpression_Expression, gen_simTL4J_expressions_AssignmentExpressionChild_Expression, gen_simTL4J_expressions_ConditionalExpression_AssignmentExpressionChild, gen_simTL4J_containers_Package_containers_JavaRoot, gen_simTL4J_containers_Package_annotations_Annotable, gen_simTL4J_containers_Package_references_ReferenceableElement, gen_simTL4J_expressions_ConditionalAndExpressionChild_ConditionalOrExpressionChild, gen_simTL4J_expressions_InclusiveOrExpression_ConditionalAndExpressionChild, gen_simTL4J_expressions_InclusiveOrExpressionChild_ConditionalAndExpressionChild, gen_simTL4J_expressions_ExclusiveOrExpression_InclusiveOrExpressionChild, gen_simTL4J_expressions_ExclusiveOrExpressionChild_InclusiveOrExpressionChild, gen_simTL4J_expressions_AndExpression_ExclusiveOrExpressionChild, gen_simTL4J_expressions_AndExpressionChild_ExclusiveOrExpressionChild, gen_simTL4J_expressions_EqualityExpression_AndExpressionChild, gen_simTL4J_expressions_EqualityExpressionChild_AndExpressionChild, gen_simTL4J_expressions_InstanceOfExpression_arrays_ArrayTypeable, gen_simTL4J_expressions_InstanceOfExpression_types_TypedElement, gen_simTL4J_expressions_InstanceOfExpression_expressions_EqualityExpressionChild, gen_simTL4J_expressions_InstanceOfExpressionChild_EqualityExpressionChild, gen_simTL4J_expressions_ConditionalExpressionChild_AssignmentExpressionChild, gen_simTL4J_expressions_ConditionalOrExpression_ConditionalExpressionChild, gen_simTL4J_expressions_ConditionalOrExpressionChild_ConditionalExpressionChild, gen_simTL4J_expressions_ConditionalAndExpression_ConditionalOrExpressionChild, gen_simTL4J_expressions_ShiftExpressionChild_RelationExpressionChild, gen_simTL4J_expressions_AdditiveExpression_ShiftExpressionChild, gen_simTL4J_expressions_AdditiveExpressionChild_ShiftExpressionChild, gen_simTL4J_expressions_MultiplicativeExpression_AdditiveExpressionChild, gen_simTL4J_expressions_MultiplicativeExpressionChild_AdditiveExpressionChild, gen_simTL4J_expressions_UnaryExpression_MultiplicativeExpressionChild, gen_simTL4J_expressions_RelationExpression_InstanceOfExpressionChild, gen_simTL4J_expressions_RelationExpressionChild_InstanceOfExpressionChild, gen_simTL4J_expressions_ShiftExpression_RelationExpressionChild, gen_simTL4J_expressions_PrefixUnaryModificationExpression_UnaryModificationExpression, gen_simTL4J_expressions_SuffixUnaryModificationExpression_UnaryModificationExpression, gen_simTL4J_expressions_UnaryModificationExpressionChild_UnaryExpressionChild, gen_simTL4J_expressions_CastExpression_types_TypedElement, gen_simTL4J_expressions_CastExpression_arrays_ArrayTypeable, gen_simTL4J_expressions_CastExpression_expressions_UnaryModificationExpressionChild, gen_simTL4J_expressions_PrimaryExpression_UnaryModificationExpressionChild, gen_simTL4J_expressions_NestedExpression_Reference, gen_simTL4J_expressions_UnaryExpressionChild_MultiplicativeExpressionChild, gen_simTL4J_expressions_UnaryModificationExpression_UnaryExpressionChild, gen_simTL4J_generics_TypeParametrizable_Commentable, gen_simTL4J_generics_ExtendsTypeArgument_TypeArgument, gen_simTL4J_generics_QualifiedTypeArgument_generics_TypeArgument, gen_simTL4J_generics_QualifiedTypeArgument_types_TypedElement, gen_simTL4J_generics_SuperTypeArgument_TypeArgument, gen_simTL4J_generics_TypeParameter_Classifier, gen_simTL4J_generics_TypeArgument_ArrayTypeable, gen_simTL4J_generics_TypeArgumentable_Commentable, gen_simTL4J_generics_CallTypeArgumentable_Commentable, gen_simTL4J_imports_Import_NamespaceAwareElement, gen_simTL4J_imports_ImportingElement_Commentable, gen_simTL4J_imports_StaticImport_Import, gen_simTL4J_generics_UnknownTypeArgument_TypeArgument, gen_simTL4J_imports_PackageImport_Import, gen_simTL4J_imports_StaticClassifierImport_StaticImport, gen_simTL4J_imports_StaticMemberImport_StaticImport, gen_simTL4J_instantiations_Initializable_Commentable, gen_simTL4J_instantiations_Instantiation_types_TypedElement, gen_simTL4J_instantiations_Instantiation_references_Reference, gen_simTL4J_instantiations_Instantiation_references_Argumentable, gen_simTL4J_imports_ClassifierImport_Import, gen_simTL4J_literals_Self_Commentable, gen_simTL4J_literals_BooleanLiteral_Literal, gen_simTL4J_literals_CharacterLiteral_Literal, gen_simTL4J_literals_FloatLiteral_Literal, gen_simTL4J_literals_DecimalFloatLiteral_FloatLiteral, gen_simTL4J_literals_HexFloatLiteral_FloatLiteral, gen_simTL4J_literals_DoubleLiteral_Literal, gen_simTL4J_literals_DecimalDoubleLiteral_DoubleLiteral, gen_simTL4J_instantiations_Instantiation_generics_TypeArgumentable, gen_simTL4J_literals_HexDoubleLiteral_DoubleLiteral, gen_simTL4J_instantiations_NewConstructorCall_instantiations_Instantiation, gen_simTL4J_instantiations_NewConstructorCall_generics_CallTypeArgumentable, gen_simTL4J_literals_IntegerLiteral_Literal, gen_simTL4J_instantiations_ExplicitConstructorCall_Instantiation, gen_simTL4J_literals_Literal_PrimaryExpression, gen_simTL4J_literals_OctalLongLiteral_LongLiteral, gen_simTL4J_literals_NullLiteral_Literal, gen_simTL4J_literals_Super_Self, gen_simTL4J_literals_This_Self, gen_simTL4J_members_ExceptionThrower_Commentable, gen_simTL4J_members_Member_NamedElement, gen_simTL4J_members_MemberContainer_Commentable, gen_simTL4J_members_AdditionalField_references_ReferenceableElement, gen_simTL4J_members_AdditionalField_arrays_ArrayTypeable, gen_simTL4J_members_AdditionalField_instantiations_Initializable, gen_simTL4J_members_Constructor_members_Member, gen_simTL4J_literals_DecimalIntegerLiteral_IntegerLiteral, gen_simTL4J_literals_HexIntegerLiteral_IntegerLiteral, gen_simTL4J_literals_OctalIntegerLiteral_IntegerLiteral, gen_simTL4J_literals_LongLiteral_Literal, gen_simTL4J_literals_DecimalLongLiteral_LongLiteral, gen_simTL4J_literals_HexLongLiteral_LongLiteral, gen_simTL4J_members_Method_members_Member, gen_simTL4J_members_Method_types_TypedElement, gen_simTL4J_members_Method_arrays_ArrayTypeable, gen_simTL4J_members_Method_generics_TypeParametrizable, gen_simTL4J_members_Method_parameters_Parametrizable, gen_simTL4J_members_Method_references_ReferenceableElement, gen_simTL4J_members_Method_members_ExceptionThrower, gen_simTL4J_members_Method_modifiers_AnnotableAndModifiable, gen_simTL4J_members_InterfaceMethod_Method, gen_simTL4J_members_ClassMethod_members_Method, gen_simTL4J_members_ClassMethod_statements_StatementListContainer, gen_simTL4J_members_EnumConstant_references_ReferenceableElement, gen_simTL4J_members_EnumConstant_references_Argumentable, gen_simTL4J_members_EnumConstant_annotations_Annotable, gen_simTL4J_modifiers_Modifier_AnnotationInstanceOrModifier, gen_simTL4J_modifiers_AnnotationInstanceOrModifier_Commentable, gen_simTL4J_members_Constructor_statements_StatementListContainer, gen_simTL4J_members_Constructor_parameters_Parametrizable, gen_simTL4J_members_Constructor_generics_TypeParametrizable, gen_simTL4J_members_Constructor_members_ExceptionThrower, gen_simTL4J_members_Constructor_modifiers_AnnotableAndModifiable, gen_simTL4J_members_EmptyMember_Member, gen_simTL4J_members_Field_members_Member, gen_simTL4J_members_Field_instantiations_Initializable, gen_simTL4J_members_Field_variables_Variable, gen_simTL4J_members_Field_references_ReferenceableElement, gen_simTL4J_members_Field_modifiers_AnnotableAndModifiable, gen_simTL4J_modifiers_Modifiable_Commentable, gen_simTL4J_modifiers_Abstract_Modifier, gen_simTL4J_modifiers_Final_Modifier, gen_simTL4J_modifiers_Native_Modifier, gen_simTL4J_modifiers_Protected_Modifier, gen_simTL4J_modifiers_Public_Modifier, gen_simTL4J_modifiers_Private_Modifier, gen_simTL4J_modifiers_Static_Modifier, gen_simTL4J_modifiers_Strictfp_Modifier, gen_simTL4J_modifiers_Synchronized_Modifier, gen_simTL4J_modifiers_Transient_Modifier, gen_simTL4J_modifiers_Volatile_Modifier, gen_simTL4J_operators_Operator_Commentable, gen_simTL4J_operators_AdditiveOperator_Operator, gen_simTL4J_modifiers_AnnotableAndModifiable_Commentable, gen_simTL4J_operators_UnaryModificationOperator_Operator, gen_simTL4J_operators_Assignment_AssignmentOperator, gen_simTL4J_operators_AssignmentAnd_AssignmentOperator, gen_simTL4J_operators_AssignmentDivision_AssignmentOperator, gen_simTL4J_operators_AssignmentExclusiveOr_AssignmentOperator, gen_simTL4J_operators_AssignmentMinus_AssignmentOperator, gen_simTL4J_operators_AssignmentModulo_AssignmentOperator, gen_simTL4J_operators_AssignmentMultiplication_AssignmentOperator, gen_simTL4J_operators_AssignmentLeftShift_AssignmentOperator, gen_simTL4J_operators_AssignmentOr_AssignmentOperator, gen_simTL4J_operators_AssignmentPlus_AssignmentOperator, gen_simTL4J_operators_AssignmentRightShift_AssignmentOperator, gen_simTL4J_operators_AssignmentUnsignedRightShift_AssignmentOperator, gen_simTL4J_operators_Equal_EqualityOperator, gen_simTL4J_operators_NotEqual_EqualityOperator, gen_simTL4J_operators_GreaterThan_RelationOperator, gen_simTL4J_operators_GreaterThanOrEqual_RelationOperator, gen_simTL4J_operators_LessThan_RelationOperator, gen_simTL4J_operators_AssignmentOperator_Operator, gen_simTL4J_operators_EqualityOperator_Operator, gen_simTL4J_operators_MultiplicativeOperator_Operator, gen_simTL4J_operators_RelationOperator_Operator, gen_simTL4J_operators_ShiftOperator_Operator, gen_simTL4J_operators_UnaryOperator_Operator, gen_simTL4J_operators_Complement_UnaryOperator, gen_simTL4J_operators_MinusMinus_UnaryModificationOperator, gen_simTL4J_operators_Negate_UnaryOperator, gen_simTL4J_operators_PlusPlus_UnaryModificationOperator, gen_simTL4J_operators_LeftShift_ShiftOperator, gen_simTL4J_operators_RightShift_ShiftOperator, gen_simTL4J_operators_UnsignedRightShift_ShiftOperator, gen_simTL4J_parameters_Parameter_variables_Variable, gen_simTL4J_parameters_Parameter_modifiers_AnnotableAndModifiable, gen_simTL4J_parameters_Parametrizable_Commentable, gen_simTL4J_parameters_OrdinaryParameter_Parameter, gen_simTL4J_parameters_VariableLengthParameter_Parameter, gen_simTL4J_references_Reference_expressions_PrimaryExpression, gen_simTL4J_references_Reference_generics_TypeArgumentable, gen_simTL4J_operators_LessThanOrEqual_RelationOperator, gen_simTL4J_operators_Addition_operators_AdditiveOperator, gen_simTL4J_operators_Addition_operators_UnaryOperator, gen_simTL4J_operators_Subtraction_operators_AdditiveOperator, gen_simTL4J_operators_Subtraction_operators_UnaryOperator, gen_simTL4J_operators_Division_MultiplicativeOperator, gen_simTL4J_operators_Multiplication_MultiplicativeOperator, gen_simTL4J_operators_Remainder_MultiplicativeOperator, gen_simTL4J_references_Argumentable_Commentable, gen_simTL4J_references_ReferenceableElement_NamedElement, gen_simTL4J_references_ElementReference_Reference, gen_simTL4J_references_IdentifierReference_ElementReference, gen_simTL4J_references_MethodCall_references_ElementReference, gen_simTL4J_references_MethodCall_references_Argumentable, gen_simTL4J_references_MethodCall_generics_CallTypeArgumentable, gen_simTL4J_references_ReflectiveClassReference_Reference, gen_simTL4J_references_PrimitiveTypeReference_Reference, gen_simTL4J_references_StringReference_Reference, gen_simTL4J_references_SelfReference_Reference, gen_simTL4J_statements_StatementContainer_Commentable, gen_simTL4J_statements_Conditional_Commentable, gen_simTL4J_statements_ForLoopInitializer_Commentable, gen_simTL4J_statements_Statement_Commentable, gen_simTL4J_statements_SwitchCase_StatementListContainer, gen_simTL4J_statements_Assert_statements_Statement, gen_simTL4J_statements_Assert_statements_Conditional, gen_simTL4J_statements_Break_Jump, gen_simTL4J_statements_Block_members_Member, gen_simTL4J_statements_Block_statements_Statement, gen_simTL4J_statements_Block_statements_StatementListContainer, gen_simTL4J_statements_Block_modifiers_Modifiable, gen_simTL4J_statements_StatementListContainer_Commentable, gen_simTL4J_statements_EmptyStatement_Statement, gen_simTL4J_statements_ExpressionStatement_Statement, gen_simTL4J_statements_ForLoop_statements_Statement, gen_simTL4J_statements_ForLoop_statements_StatementContainer, gen_simTL4J_statements_ForLoop_statements_Conditional, gen_simTL4J_statements_ForEachLoop_statements_Statement, gen_simTL4J_statements_ForEachLoop_statements_StatementContainer, gen_simTL4J_statements_CatchBlock_StatementListContainer, gen_simTL4J_statements_Condition_statements_Statement, gen_simTL4J_statements_Condition_statements_StatementContainer, gen_simTL4J_statements_Condition_statements_Conditional, gen_simTL4J_statements_Continue_Jump, gen_simTL4J_statements_DefaultSwitchCase_SwitchCase, gen_simTL4J_statements_DoWhileLoop_WhileLoop, gen_simTL4J_statements_Return_Statement, gen_simTL4J_statements_Switch_Statement, gen_simTL4J_statements_SynchronizedBlock_statements_Statement, gen_simTL4J_statements_SynchronizedBlock_statements_StatementListContainer, gen_simTL4J_statements_Throw_Statement, gen_simTL4J_statements_TryBlock_statements_Statement, gen_simTL4J_statements_TryBlock_statements_StatementListContainer, gen_simTL4J_statements_WhileLoop_statements_Statement, gen_simTL4J_statements_WhileLoop_statements_StatementContainer, gen_simTL4J_statements_Jump_Statement, gen_simTL4J_statements_JumpLabel_statements_Statement, gen_simTL4J_statements_JumpLabel_statements_StatementContainer, gen_simTL4J_statements_JumpLabel_commons_NamedElement, gen_simTL4J_statements_LocalVariableStatement_Statement, gen_simTL4J_statements_NormalSwitchCase_statements_SwitchCase, gen_simTL4J_statements_NormalSwitchCase_statements_Conditional, gen_simTL4J_types_TypedElement_Commentable, gen_simTL4J_types_TypeReference_Commentable, gen_simTL4J_types_ClassifierReference_types_TypeReference, gen_simTL4J_types_ClassifierReference_generics_TypeArgumentable, gen_simTL4J_types_NamespaceClassifierReference_types_TypeReference, gen_simTL4J_types_NamespaceClassifierReference_commons_NamespaceAwareElement, gen_simTL4J_types_PrimitiveType_types_Type, gen_simTL4J_types_PrimitiveType_types_TypeReference, gen_simTL4J_types_Type_Commentable, gen_simTL4J_variables_Variable_references_ReferenceableElement, gen_simTL4J_variables_Variable_generics_TypeArgumentable, gen_simTL4J_variables_LocalVariable_variables_Variable, gen_simTL4J_variables_LocalVariable_instantiations_Initializable, gen_simTL4J_variables_LocalVariable_statements_ForLoopInitializer, gen_simTL4J_variables_LocalVariable_modifiers_AnnotableAndModifiable, gen_simTL4J_variables_AdditionalLocalVariable_references_ReferenceableElement, gen_simTL4J_variables_AdditionalLocalVariable_arrays_ArrayTypeable, gen_simTL4J_variables_AdditionalLocalVariable_instantiations_Initializable, gen_simTL4J_types_Boolean_PrimitiveType, gen_simTL4J_types_Byte_PrimitiveType, gen_simTL4J_types_Char_PrimitiveType, gen_simTL4J_types_Double_PrimitiveType, gen_simTL4J_types_Float_PrimitiveType, gen_simTL4J_types_Int_PrimitiveType, gen_simTL4J_types_Long_PrimitiveType, gen_simTL4J_types_Short_PrimitiveType, gen_simTL4J_types_Void_PrimitiveType, gen_simTL4J_variables_Variable_commons_NamedElement, gen_simTL4J_variables_Variable_types_TypedElement, gen_simTL4J_variables_Variable_arrays_ArrayTypeable, gen_simTL4J_simTL_TFor_MemberContainer_simTL_TFor, gen_simTL4J_simTL_TFor_MemberContainer_members_MemberContainer, gen_simTL4J_simTL_TFor_MemberContainer_members_Member, gen_simTL4J_simTL_TFor_StatementListContainer_simTL_TFor, gen_simTL4J_simTL_TFor_StatementListContainer_statements_StatementListContainer, gen_simTL4J_simTL_TFor_StatementListContainer_statements_Statement, gen_simTL4J_simTL_TIf_MemberContainer_simTL_TIf, gen_simTL4J_simTL_TIf_MemberContainer_members_MemberContainer, gen_simTL4J_simTL_TIf_MemberContainer_members_Member, gen_simTL4J_simTL_TIf_StatementListContainer_simTL_TIf, gen_simTL4J_simTL_TIf_StatementListContainer_statements_StatementListContainer, gen_simTL4J_simTL_TIf_StatementListContainer_statements_Statement, gen_simTL4J_simTL_TPlaceholder_PrimaryExpression_simTL_TPlaceholder, gen_simTL4J_simTL_TPlaceholder_PrimaryExpression_expressions_PrimaryExpression, gen_simTL4J_simTL_TUnaryOperator_TAbstractMethodStatement, gen_simTL4J_simTL_TUnaryOperatorNOT_TUnaryOperator, gen_simTL4J_simTL_TMethodStatementImpl_TAbstractMethodStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)