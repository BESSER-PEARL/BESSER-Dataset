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

# Enumerations
LogicOperator: Enumeration = Enumeration(
    name="LogicOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="IF_THEN")
    }
)

CollectionKind: Enumeration = Enumeration(
    name="CollectionKind",
    literals={
            EnumerationLiteral(name="EXACT"),
			EnumerationLiteral(name="SEQUENCE"),
			EnumerationLiteral(name="ANY"),
			EnumerationLiteral(name="IMMEDIATE")
    }
)

Inheritance: Enumeration = Enumeration(
    name="Inheritance",
    literals={
            EnumerationLiteral(name="ABSTRACT"),
			EnumerationLiteral(name="FINAL"),
			EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="ANY")
    }
)

Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PACKAGE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="ANY")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="EQUAL_TO"),
			EnumerationLiteral(name="NOT_EQUAL_TO"),
			EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="GREATER_THAN_OR_EQUAL_TO"),
			EnumerationLiteral(name="LESS_THAN_OR_EQUAL_TO"),
			EnumerationLiteral(name="ANY")
    }
)

ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="ADDITION"),
			EnumerationLiteral(name="SUBTRACTION"),
			EnumerationLiteral(name="MULTIPLICATION"),
			EnumerationLiteral(name="DIVISION"),
			EnumerationLiteral(name="MODULUS"),
			EnumerationLiteral(name="UNDEFINED")
    }
)

AssignmentOperator: Enumeration = Enumeration(
    name="AssignmentOperator",
    literals={
            EnumerationLiteral(name="PLUS_ASSIGN"),
			EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="ANY")
    }
)

UnaryAssignmentOperator: Enumeration = Enumeration(
    name="UnaryAssignmentOperator",
    literals={
            EnumerationLiteral(name="DECREMENT"),
			EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="ANY")
    }
)

EquationOperator: Enumeration = Enumeration(
    name="EquationOperator",
    literals={
            EnumerationLiteral(name="PLUS")
    }
)

# Classes
ccsl_Rule = Class(name="ccsl::Rule", is_abstract=True)
Root = Class(name="Root")
ccsl_CompositeRule = Class(name="ccsl::CompositeRule")
Rule = Class(name="Rule")
Element = Class(name="Element")
Context = Class(name="Context")
ccsl_Root = Class(name="ccsl::Root", is_abstract=True)
ccsl_FaultTypeDescription = Class(name="ccsl::FaultTypeDescription")
InjectionAction = Class(name="InjectionAction")
InjectionStrategy = Class(name="InjectionStrategy")
ccsl_elements_Element = Class(name="ccsl::elements::Element")
ccsl_AtomicRule = Class(name="ccsl::AtomicRule")
ccsl_namedElements_NamedElement = Class(name="ccsl::namedElements::NamedElement")
ccsl_namedElements_Package = Class(name="ccsl::namedElements::Package")
namedElements_NamedElement = Class(name="namedElements::NamedElement")
import_ImportableElement = Class(name="import::ImportableElement")
complexType_DeclaredType = Class(name="complexType::DeclaredType")
ccsl_variable_Variable = Class(name="ccsl::variable::Variable")
NamedElement = Class(name="NamedElement")
datatype_DataType = Class(name="datatype::DataType")
annotation_AnnotableElement = Class(name="annotation::AnnotableElement")
ccsl_variable_LocalVariable = Class(name="ccsl::variable::LocalVariable")
InitializableVariable = Class(name="InitializableVariable")
ccsl_variable_InitializableVariable = Class(name="ccsl::variable::InitializableVariable")
Variable = Class(name="Variable")
statements_Statement = Class(name="statements::Statement")
ccsl_variable_FieldVariable = Class(name="ccsl::variable::FieldVariable")
variable_InitializableVariable = Class(name="variable::InitializableVariable")
ccsl_complexType_JInterface = Class(name="ccsl::complexType::JInterface")
complexType_ComplexType = Class(name="complexType::ComplexType")
ccsl_complexType_AnonymousClass = Class(name="ccsl::complexType::AnonymousClass")
ComplexType = Class(name="ComplexType")
datatype_ObjectType = Class(name="datatype::ObjectType")
ccsl_complexType_DeclaredType = Class(name="ccsl::complexType::DeclaredType")
ccsl_variable_ParameterVariable = Class(name="ccsl::variable::ParameterVariable")
variable_Variable = Class(name="variable::Variable")
complexType_JInterface = Class(name="complexType::JInterface")
import_ImportStatement = Class(name="import::ImportStatement")
ccsl_complexType_ComplexType = Class(name="ccsl::complexType::ComplexType")
variable_FieldVariable = Class(name="variable::FieldVariable")
method_Method = Class(name="method::Method")
ccsl_complexType_AnnotationType = Class(name="ccsl::complexType::AnnotationType")
DeclaredType = Class(name="DeclaredType")
ccsl_method_Constructor = Class(name="ccsl::method::Constructor")
SimpleMethod = Class(name="SimpleMethod")
ccsl_method_SimpleMethod = Class(name="ccsl::method::SimpleMethod")
elements_Element = Class(name="elements::Element")
variable_ParameterVariable = Class(name="variable::ParameterVariable")
ccsl_complexType_JClass = Class(name="ccsl::complexType::JClass")
ccsl_method_Method = Class(name="ccsl::method::Method")
method_SimpleMethod = Class(name="method::SimpleMethod")
method_Constructor = Class(name="method::Constructor")
complexType_JClass = Class(name="complexType::JClass")
ccsl_statements_Statement = Class(name="ccsl::statements::Statement")
ccsl_statements_NamedElementAccess = Class(name="ccsl::statements::NamedElementAccess")
Statement = Class(name="Statement")
ccsl_statements_VariableAccess = Class(name="ccsl::statements::VariableAccess")
Access = Class(name="Access")
ccsl_statements_DataTypeAccess = Class(name="ccsl::statements::DataTypeAccess")
ccsl_statements_ControlFlow = Class(name="ccsl::statements::ControlFlow")
ccsl_statements_Block = Class(name="ccsl::statements::Block")
ccsl_statements_VarDeclaration = Class(name="ccsl::statements::VarDeclaration")
ccsl_statements_InstanceCreation = Class(name="ccsl::statements::InstanceCreation")
ccsl_statements_Access = Class(name="ccsl::statements::Access")
ccsl_statements_ArrayCreation = Class(name="ccsl::statements::ArrayCreation")
ccsl_statements_SynchronizedBlock = Class(name="ccsl::statements::SynchronizedBlock")
ccsl_statements_EmptyStatement = Class(name="ccsl::statements::EmptyStatement")
ccsl_statements_InstanceOf = Class(name="ccsl::statements::InstanceOf")
ccsl_statements_ReturnStatement = Class(name="ccsl::statements::ReturnStatement")
ccsl_statements_ThisStatement = Class(name="ccsl::statements::ThisStatement")
ccsl_statements_BreakStatement = Class(name="ccsl::statements::BreakStatement")
ccsl_statements_ContinueStatement = Class(name="ccsl::statements::ContinueStatement")
ccsl_expressions_OperatorExpression = Class(name="ccsl::expressions::OperatorExpression")
ccsl_expressions_ParenthesizedExpression = Class(name="ccsl::expressions::ParenthesizedExpression")
ccsl_expressions_StringConcatenation = Class(name="ccsl::expressions::StringConcatenation")
OperatorExpression = Class(name="OperatorExpression")
ccsl_expressions_InfixExpression = Class(name="ccsl::expressions::InfixExpression")
ccsl_expressions_BooleanExpression = Class(name="ccsl::expressions::BooleanExpression")
ccsl_expressions_ArithmeticExpression = Class(name="ccsl::expressions::ArithmeticExpression")
ccsl_statements_ThrowStatement = Class(name="ccsl::statements::ThrowStatement")
ccsl_literalValues_LiteralValue = Class(name="ccsl::literalValues::LiteralValue")
ccsl_literalValues_NullLiteral = Class(name="ccsl::literalValues::NullLiteral")
LiteralValue = Class(name="LiteralValue")
ccsl_literalValues_CharacterLiteral = Class(name="ccsl::literalValues::CharacterLiteral")
ccsl_literalValues_StringLiteral = Class(name="ccsl::literalValues::StringLiteral")
ccsl_literalValues_NumberLiteral = Class(name="ccsl::literalValues::NumberLiteral")
ccsl_literalValues_BooleanLiteral = Class(name="ccsl::literalValues::BooleanLiteral")
ccsl_controlFlow_SwitchStatement = Class(name="ccsl::controlFlow::SwitchStatement")
ControlFlow = Class(name="ControlFlow")
controlFlow_SwitchCaseBlock = Class(name="controlFlow::SwitchCaseBlock")
ccsl_controlFlow_SwitchCaseBlock = Class(name="ccsl::controlFlow::SwitchCaseBlock")
Block = Class(name="Block")
ccsl_controlFlow_IfStatement = Class(name="ccsl::controlFlow::IfStatement")
ccsl_controlFlow_LoopStatement = Class(name="ccsl::controlFlow::LoopStatement")
ccsl_tryCatch_TryStatement = Class(name="ccsl::tryCatch::TryStatement")
tryCatch_CatchClause = Class(name="tryCatch::CatchClause")
statements_Block = Class(name="statements::Block")
ccsl_tryCatch_CatchClause = Class(name="ccsl::tryCatch::CatchClause")
ccsl_assignment_AbstractAssignment = Class(name="ccsl::assignment::AbstractAssignment")
ccsl_assignment_Assignment = Class(name="ccsl::assignment::Assignment")
AbstractAssignment = Class(name="AbstractAssignment")
ccsl_assignment_UnaryAssignment = Class(name="ccsl::assignment::UnaryAssignment")
ccsl_assignment_PrefixUnaryAssignment = Class(name="ccsl::assignment::PrefixUnaryAssignment")
UnaryAssignment = Class(name="UnaryAssignment")
ccsl_assignment_PostfixUnaryAssignment = Class(name="ccsl::assignment::PostfixUnaryAssignment")
ccsl_invocation_MethodInvocation = Class(name="ccsl::invocation::MethodInvocation")
SimpleMethodInvocation = Class(name="SimpleMethodInvocation")
ccsl_invocation_ConstructorInvocation = Class(name="ccsl::invocation::ConstructorInvocation")
Invocation = Class(name="Invocation")
ccsl_invocation_SimpleMethodInvocation = Class(name="ccsl::invocation::SimpleMethodInvocation")
ccsl_import_ImportableElement = Class(name="ccsl::import::ImportableElement")
ccsl_import_ImportStatement = Class(name="ccsl::import::ImportStatement")
ccsl_annotation_Annotation = Class(name="ccsl::annotation::Annotation")
complexType_AnnotationType = Class(name="complexType::AnnotationType")
ccsl_annotation_AnnotableElement = Class(name="ccsl::annotation::AnnotableElement")
annotation_Annotation = Class(name="annotation::Annotation")
ccsl_invocation_SuperMethodInvocation = Class(name="ccsl::invocation::SuperMethodInvocation")
ccsl_invocation_Invocation = Class(name="ccsl::invocation::Invocation")
ccsl_datatype_StringPrimitiveType = Class(name="ccsl::datatype::StringPrimitiveType")
PrimitiveType = Class(name="PrimitiveType")
ccsl_datatype_BooleanPrimitiveType = Class(name="ccsl::datatype::BooleanPrimitiveType")
ccsl_datatype_ShortPrimitiveType = Class(name="ccsl::datatype::ShortPrimitiveType")
ccsl_datatype_ObjectType = Class(name="ccsl::datatype::ObjectType")
ccsl_datatype_ParameterizedType = Class(name="ccsl::datatype::ParameterizedType")
ObjectType = Class(name="ObjectType")
ccsl_datatype_GenericType = Class(name="ccsl::datatype::GenericType")
ccsl_datatype_IntPrimitiveType = Class(name="ccsl::datatype::IntPrimitiveType")
ccsl_datatype_ArrayType = Class(name="ccsl::datatype::ArrayType")
ccsl_datatype_VoidType = Class(name="ccsl::datatype::VoidType")
ccsl_context_Context = Class(name="ccsl::context::Context")
filters_Filter = Class(name="filters::Filter")
ccsl_faultTypeDescription_InjectionAction = Class(name="ccsl::faultTypeDescription::InjectionAction", is_abstract=True)
ccsl_datatype_DataType = Class(name="ccsl::datatype::DataType")
ccsl_datatype_PrimitiveType = Class(name="ccsl::datatype::PrimitiveType")
DataType = Class(name="DataType")
ccsl_faultTypeDescription_InjectionStrategy = Class(name="ccsl::faultTypeDescription::InjectionStrategy", is_abstract=True)
ccsl_action_DeleteAction = Class(name="ccsl::action::DeleteAction")
ccsl_action_MoveScopeUpAction = Class(name="ccsl::action::MoveScopeUpAction")
ccsl_action_DeleteInfixOperatorAction = Class(name="ccsl::action::DeleteInfixOperatorAction")
ccsl_action_ChangeLiteralValueAction = Class(name="ccsl::action::ChangeLiteralValueAction")
ccsl_action_DeleteRandomStatementAction = Class(name="ccsl::action::DeleteRandomStatementAction")
ccsl_action_ReplaceVariableAccessAction = Class(name="ccsl::action::ReplaceVariableAccessAction")
ccsl_action_ReplaceArithmeticOperatorAction = Class(name="ccsl::action::ReplaceArithmeticOperatorAction")
action_ArithmeticOperatorMap = Class(name="action::ArithmeticOperatorMap")
ccsl_action_ArithmeticOperatorMap = Class(name="ccsl::action::ArithmeticOperatorMap")
ccsl_strategy_AllStrategy = Class(name="ccsl::strategy::AllStrategy")
ccsl_functions_CcslFunction = Class(name="ccsl::functions::CcslFunction", is_abstract=True)
ccsl_booleanFunctions_CcslBooleanFunction = Class(name="ccsl::booleanFunctions::CcslBooleanFunction", is_abstract=True)
CcslFunction = Class(name="CcslFunction")
ccsl_filters_Filter = Class(name="ccsl::filters::Filter", is_abstract=True)
CcslBooleanFunction = Class(name="CcslBooleanFunction")
ccsl_filters_AtomicFilter = Class(name="ccsl::filters::AtomicFilter")
Filter = Class(name="Filter")
ccsl_filters_CompositeFilter = Class(name="ccsl::filters::CompositeFilter")
ccsl_filters_PropertyFilter = Class(name="ccsl::filters::PropertyFilter")
AtomicFilter = Class(name="AtomicFilter")
ccsl_filters_TemplateFilter = Class(name="ccsl::filters::TemplateFilter")
ccsl_filters_SameNameFilter = Class(name="ccsl::filters::SameNameFilter")
ccsl_filters_CountFilter = Class(name="ccsl::filters::CountFilter")
ccsl_filters_RegexMatch = Class(name="ccsl::filters::RegexMatch")
ccsl_filters_ImplicityOperandFilter = Class(name="ccsl::filters::ImplicityOperandFilter")
TemplateFilter = Class(name="TemplateFilter")
expressions_OperatorExpression = Class(name="expressions::OperatorExpression")
ccsl_filters_ImplicityContainerFilter = Class(name="ccsl::filters::ImplicityContainerFilter")
ccsl_filters_IsKindOfFilter = Class(name="ccsl::filters::IsKindOfFilter")
ccsl_filters_SuperMethodClosureFilter = Class(name="ccsl::filters::SuperMethodClosureFilter")
ccsl_filters_IsTypeOfFilter = Class(name="ccsl::filters::IsTypeOfFilter")
ccsl_filters_ChildClosureComplexTypeFilter = Class(name="ccsl::filters::ChildClosureComplexTypeFilter")
ccsl_filters_IsStringFilter = Class(name="ccsl::filters::IsStringFilter")
ccsl_filters_EquationFilter = Class(name="ccsl::filters::EquationFilter")
numberFunctions_CcslNumberFunction = Class(name="numberFunctions::CcslNumberFunction")
ccsl_filters_FromClosureFilter = Class(name="ccsl::filters::FromClosureFilter")
statements_Access = Class(name="statements::Access")
ccsl_filters_SuperClassClosureFilter = Class(name="ccsl::filters::SuperClassClosureFilter")
ccsl_filters_BlockLastStatementFilter = Class(name="ccsl::filters::BlockLastStatementFilter")
ccsl_filters_HasSameReferenceFilter = Class(name="ccsl::filters::HasSameReferenceFilter")
ccsl_numberFunctions_CcslNumberFunction = Class(name="ccsl::numberFunctions::CcslNumberFunction", is_abstract=True)
ccsl_numberFunctions_CcslIntegerLiteral = Class(name="ccsl::numberFunctions::CcslIntegerLiteral")
CcslNumberFunction = Class(name="CcslNumberFunction")
ccsl_numberFunctions_GetIndexOf = Class(name="ccsl::numberFunctions::GetIndexOf")

# ccsl_Rule class attributes and methods
ccsl_Rule_negated: Property = Property(name="negated", type=StringType)
ccsl_Rule.attributes={ccsl_Rule_negated}

# Root class attributes and methods

# ccsl_CompositeRule class attributes and methods
ccsl_CompositeRule_operator: Property = Property(name="operator", type=StringType)
ccsl_CompositeRule.attributes={ccsl_CompositeRule_operator}

# Rule class attributes and methods

# Element class attributes and methods

# Context class attributes and methods

# ccsl_Root class attributes and methods

# ccsl_FaultTypeDescription class attributes and methods
ccsl_FaultTypeDescription_name: Property = Property(name="name", type=StringType)
ccsl_FaultTypeDescription.attributes={ccsl_FaultTypeDescription_name}

# InjectionAction class attributes and methods

# InjectionStrategy class attributes and methods

# ccsl_elements_Element class attributes and methods
ccsl_elements_Element_uniqueName: Property = Property(name="uniqueName", type=StringType)
ccsl_elements_Element.attributes={ccsl_elements_Element_uniqueName}

# ccsl_AtomicRule class attributes and methods

# ccsl_namedElements_NamedElement class attributes and methods
ccsl_namedElements_NamedElement_name: Property = Property(name="name", type=StringType)
ccsl_namedElements_NamedElement_avaliableInSourceCode: Property = Property(name="avaliableInSourceCode", type=StringType)
ccsl_namedElements_NamedElement.attributes={ccsl_namedElements_NamedElement_name, ccsl_namedElements_NamedElement_avaliableInSourceCode}

# ccsl_namedElements_Package class attributes and methods

# namedElements_NamedElement class attributes and methods

# import_ImportableElement class attributes and methods

# complexType_DeclaredType class attributes and methods

# ccsl_variable_Variable class attributes and methods
ccsl_variable_Variable_final: Property = Property(name="final", type=StringType)
ccsl_variable_Variable.attributes={ccsl_variable_Variable_final}

# NamedElement class attributes and methods

# datatype_DataType class attributes and methods

# annotation_AnnotableElement class attributes and methods

# ccsl_variable_LocalVariable class attributes and methods

# InitializableVariable class attributes and methods

# ccsl_variable_InitializableVariable class attributes and methods

# Variable class attributes and methods

# statements_Statement class attributes and methods

# ccsl_variable_FieldVariable class attributes and methods
ccsl_variable_FieldVariable_static: Property = Property(name="static", type=StringType)
ccsl_variable_FieldVariable_visibility: Property = Property(name="visibility", type=StringType)
ccsl_variable_FieldVariable.attributes={ccsl_variable_FieldVariable_static, ccsl_variable_FieldVariable_visibility}

# variable_InitializableVariable class attributes and methods

# ccsl_complexType_JInterface class attributes and methods

# complexType_ComplexType class attributes and methods

# ccsl_complexType_AnonymousClass class attributes and methods

# ComplexType class attributes and methods

# datatype_ObjectType class attributes and methods

# ccsl_complexType_DeclaredType class attributes and methods
ccsl_complexType_DeclaredType_visibility: Property = Property(name="visibility", type=StringType)
ccsl_complexType_DeclaredType_static: Property = Property(name="static", type=StringType)
ccsl_complexType_DeclaredType.attributes={ccsl_complexType_DeclaredType_static, ccsl_complexType_DeclaredType_visibility}

# ccsl_variable_ParameterVariable class attributes and methods

# variable_Variable class attributes and methods

# complexType_JInterface class attributes and methods

# import_ImportStatement class attributes and methods

# ccsl_complexType_ComplexType class attributes and methods

# variable_FieldVariable class attributes and methods

# method_Method class attributes and methods

# ccsl_complexType_AnnotationType class attributes and methods

# DeclaredType class attributes and methods

# ccsl_method_Constructor class attributes and methods
ccsl_method_Constructor_avaliableInSourceCode: Property = Property(name="avaliableInSourceCode", type=StringType)
ccsl_method_Constructor.attributes={ccsl_method_Constructor_avaliableInSourceCode}

# SimpleMethod class attributes and methods

# ccsl_method_SimpleMethod class attributes and methods
ccsl_method_SimpleMethod_visibility: Property = Property(name="visibility", type=StringType)
ccsl_method_SimpleMethod_paramsKind: Property = Property(name="paramsKind", type=StringType)
ccsl_method_SimpleMethod.attributes={ccsl_method_SimpleMethod_paramsKind, ccsl_method_SimpleMethod_visibility}

# elements_Element class attributes and methods

# variable_ParameterVariable class attributes and methods

# ccsl_complexType_JClass class attributes and methods
ccsl_complexType_JClass_inheritance: Property = Property(name="inheritance", type=StringType)
ccsl_complexType_JClass.attributes={ccsl_complexType_JClass_inheritance}

# ccsl_method_Method class attributes and methods
ccsl_method_Method_abstract: Property = Property(name="abstract", type=StringType)
ccsl_method_Method_final: Property = Property(name="final", type=StringType)
ccsl_method_Method_static: Property = Property(name="static", type=StringType)
ccsl_method_Method_inheritance: Property = Property(name="inheritance", type=StringType)
ccsl_method_Method.attributes={ccsl_method_Method_final, ccsl_method_Method_static, ccsl_method_Method_inheritance, ccsl_method_Method_abstract}

# method_SimpleMethod class attributes and methods

# method_Constructor class attributes and methods

# complexType_JClass class attributes and methods

# ccsl_statements_Statement class attributes and methods

# ccsl_statements_NamedElementAccess class attributes and methods

# Statement class attributes and methods

# ccsl_statements_VariableAccess class attributes and methods

# Access class attributes and methods

# ccsl_statements_DataTypeAccess class attributes and methods

# ccsl_statements_ControlFlow class attributes and methods

# ccsl_statements_Block class attributes and methods
ccsl_statements_Block_statementsKind: Property = Property(name="statementsKind", type=StringType)
ccsl_statements_Block.attributes={ccsl_statements_Block_statementsKind}

# ccsl_statements_VarDeclaration class attributes and methods

# ccsl_statements_InstanceCreation class attributes and methods
ccsl_statements_InstanceCreation_argsKind: Property = Property(name="argsKind", type=StringType)
ccsl_statements_InstanceCreation.attributes={ccsl_statements_InstanceCreation_argsKind}

# ccsl_statements_Access class attributes and methods

# ccsl_statements_ArrayCreation class attributes and methods

# ccsl_statements_SynchronizedBlock class attributes and methods

# ccsl_statements_EmptyStatement class attributes and methods

# ccsl_statements_InstanceOf class attributes and methods

# ccsl_statements_ReturnStatement class attributes and methods

# ccsl_statements_ThisStatement class attributes and methods

# ccsl_statements_BreakStatement class attributes and methods

# ccsl_statements_ContinueStatement class attributes and methods

# ccsl_expressions_OperatorExpression class attributes and methods

# ccsl_expressions_ParenthesizedExpression class attributes and methods

# ccsl_expressions_StringConcatenation class attributes and methods

# OperatorExpression class attributes and methods

# ccsl_expressions_InfixExpression class attributes and methods

# ccsl_expressions_BooleanExpression class attributes and methods
ccsl_expressions_BooleanExpression_booleanOperator: Property = Property(name="booleanOperator", type=StringType)
ccsl_expressions_BooleanExpression.attributes={ccsl_expressions_BooleanExpression_booleanOperator}

# ccsl_expressions_ArithmeticExpression class attributes and methods
ccsl_expressions_ArithmeticExpression_arithmeticOperator: Property = Property(name="arithmeticOperator", type=StringType)
ccsl_expressions_ArithmeticExpression.attributes={ccsl_expressions_ArithmeticExpression_arithmeticOperator}

# ccsl_statements_ThrowStatement class attributes and methods

# ccsl_literalValues_LiteralValue class attributes and methods
ccsl_literalValues_LiteralValue_value: Property = Property(name="value", type=StringType)
ccsl_literalValues_LiteralValue.attributes={ccsl_literalValues_LiteralValue_value}

# ccsl_literalValues_NullLiteral class attributes and methods

# LiteralValue class attributes and methods

# ccsl_literalValues_CharacterLiteral class attributes and methods

# ccsl_literalValues_StringLiteral class attributes and methods

# ccsl_literalValues_NumberLiteral class attributes and methods

# ccsl_literalValues_BooleanLiteral class attributes and methods

# ccsl_controlFlow_SwitchStatement class attributes and methods

# ControlFlow class attributes and methods

# controlFlow_SwitchCaseBlock class attributes and methods

# ccsl_controlFlow_SwitchCaseBlock class attributes and methods
ccsl_controlFlow_SwitchCaseBlock_default: Property = Property(name="default", type=StringType)
ccsl_controlFlow_SwitchCaseBlock.attributes={ccsl_controlFlow_SwitchCaseBlock_default}

# Block class attributes and methods

# ccsl_controlFlow_IfStatement class attributes and methods

# ccsl_controlFlow_LoopStatement class attributes and methods

# ccsl_tryCatch_TryStatement class attributes and methods

# tryCatch_CatchClause class attributes and methods

# statements_Block class attributes and methods

# ccsl_tryCatch_CatchClause class attributes and methods

# ccsl_assignment_AbstractAssignment class attributes and methods

# ccsl_assignment_Assignment class attributes and methods
ccsl_assignment_Assignment_operator: Property = Property(name="operator", type=StringType)
ccsl_assignment_Assignment.attributes={ccsl_assignment_Assignment_operator}

# AbstractAssignment class attributes and methods

# ccsl_assignment_UnaryAssignment class attributes and methods
ccsl_assignment_UnaryAssignment_operator: Property = Property(name="operator", type=StringType)
ccsl_assignment_UnaryAssignment.attributes={ccsl_assignment_UnaryAssignment_operator}

# ccsl_assignment_PrefixUnaryAssignment class attributes and methods

# UnaryAssignment class attributes and methods

# ccsl_assignment_PostfixUnaryAssignment class attributes and methods

# ccsl_invocation_MethodInvocation class attributes and methods

# SimpleMethodInvocation class attributes and methods

# ccsl_invocation_ConstructorInvocation class attributes and methods

# Invocation class attributes and methods

# ccsl_invocation_SimpleMethodInvocation class attributes and methods

# ccsl_import_ImportableElement class attributes and methods

# ccsl_import_ImportStatement class attributes and methods

# ccsl_annotation_Annotation class attributes and methods

# complexType_AnnotationType class attributes and methods

# ccsl_annotation_AnnotableElement class attributes and methods
ccsl_annotation_AnnotableElement_annotationsKind: Property = Property(name="annotationsKind", type=StringType)
ccsl_annotation_AnnotableElement.attributes={ccsl_annotation_AnnotableElement_annotationsKind}

# annotation_Annotation class attributes and methods

# ccsl_invocation_SuperMethodInvocation class attributes and methods

# ccsl_invocation_Invocation class attributes and methods
ccsl_invocation_Invocation_argsKind: Property = Property(name="argsKind", type=StringType)
ccsl_invocation_Invocation.attributes={ccsl_invocation_Invocation_argsKind}

# ccsl_datatype_StringPrimitiveType class attributes and methods

# PrimitiveType class attributes and methods

# ccsl_datatype_BooleanPrimitiveType class attributes and methods

# ccsl_datatype_ShortPrimitiveType class attributes and methods

# ccsl_datatype_ObjectType class attributes and methods

# ccsl_datatype_ParameterizedType class attributes and methods

# ObjectType class attributes and methods

# ccsl_datatype_GenericType class attributes and methods

# ccsl_datatype_IntPrimitiveType class attributes and methods

# ccsl_datatype_ArrayType class attributes and methods
ccsl_datatype_ArrayType_dimensions: Property = Property(name="dimensions", type=StringType)
ccsl_datatype_ArrayType.attributes={ccsl_datatype_ArrayType_dimensions}

# ccsl_datatype_VoidType class attributes and methods

# ccsl_context_Context class attributes and methods

# filters_Filter class attributes and methods

# ccsl_faultTypeDescription_InjectionAction class attributes and methods

# ccsl_datatype_DataType class attributes and methods

# ccsl_datatype_PrimitiveType class attributes and methods

# DataType class attributes and methods

# ccsl_faultTypeDescription_InjectionStrategy class attributes and methods

# ccsl_action_DeleteAction class attributes and methods

# ccsl_action_MoveScopeUpAction class attributes and methods

# ccsl_action_DeleteInfixOperatorAction class attributes and methods

# ccsl_action_ChangeLiteralValueAction class attributes and methods

# ccsl_action_DeleteRandomStatementAction class attributes and methods

# ccsl_action_ReplaceVariableAccessAction class attributes and methods

# ccsl_action_ReplaceArithmeticOperatorAction class attributes and methods

# action_ArithmeticOperatorMap class attributes and methods

# ccsl_action_ArithmeticOperatorMap class attributes and methods
ccsl_action_ArithmeticOperatorMap_oldArithmeticOperator: Property = Property(name="oldArithmeticOperator", type=StringType)
ccsl_action_ArithmeticOperatorMap_newArithmeticOperator: Property = Property(name="newArithmeticOperator", type=StringType)
ccsl_action_ArithmeticOperatorMap.attributes={ccsl_action_ArithmeticOperatorMap_newArithmeticOperator, ccsl_action_ArithmeticOperatorMap_oldArithmeticOperator}

# ccsl_strategy_AllStrategy class attributes and methods

# ccsl_functions_CcslFunction class attributes and methods

# ccsl_booleanFunctions_CcslBooleanFunction class attributes and methods

# CcslFunction class attributes and methods

# ccsl_filters_Filter class attributes and methods
ccsl_filters_Filter_negated: Property = Property(name="negated", type=StringType)
ccsl_filters_Filter.attributes={ccsl_filters_Filter_negated}

# CcslBooleanFunction class attributes and methods

# ccsl_filters_AtomicFilter class attributes and methods

# Filter class attributes and methods

# ccsl_filters_CompositeFilter class attributes and methods
ccsl_filters_CompositeFilter_operator: Property = Property(name="operator", type=StringType)
ccsl_filters_CompositeFilter.attributes={ccsl_filters_CompositeFilter_operator}

# ccsl_filters_PropertyFilter class attributes and methods

# AtomicFilter class attributes and methods

# ccsl_filters_TemplateFilter class attributes and methods

# ccsl_filters_SameNameFilter class attributes and methods
ccsl_filters_SameNameFilter_ignoreCase: Property = Property(name="ignoreCase", type=StringType)
ccsl_filters_SameNameFilter.attributes={ccsl_filters_SameNameFilter_ignoreCase}

# ccsl_filters_CountFilter class attributes and methods
ccsl_filters_CountFilter_min: Property = Property(name="min", type=StringType)
ccsl_filters_CountFilter_max: Property = Property(name="max", type=StringType)
ccsl_filters_CountFilter.attributes={ccsl_filters_CountFilter_max, ccsl_filters_CountFilter_min}

# ccsl_filters_RegexMatch class attributes and methods
ccsl_filters_RegexMatch_regex: Property = Property(name="regex", type=StringType)
ccsl_filters_RegexMatch.attributes={ccsl_filters_RegexMatch_regex}

# ccsl_filters_ImplicityOperandFilter class attributes and methods

# TemplateFilter class attributes and methods

# expressions_OperatorExpression class attributes and methods

# ccsl_filters_ImplicityContainerFilter class attributes and methods

# ccsl_filters_IsKindOfFilter class attributes and methods

# ccsl_filters_SuperMethodClosureFilter class attributes and methods

# ccsl_filters_IsTypeOfFilter class attributes and methods

# ccsl_filters_ChildClosureComplexTypeFilter class attributes and methods

# ccsl_filters_IsStringFilter class attributes and methods

# ccsl_filters_EquationFilter class attributes and methods
ccsl_filters_EquationFilter_operator: Property = Property(name="operator", type=StringType)
ccsl_filters_EquationFilter.attributes={ccsl_filters_EquationFilter_operator}

# numberFunctions_CcslNumberFunction class attributes and methods

# ccsl_filters_FromClosureFilter class attributes and methods

# statements_Access class attributes and methods

# ccsl_filters_SuperClassClosureFilter class attributes and methods
ccsl_filters_SuperClassClosureFilter_includesSubClass: Property = Property(name="includesSubClass", type=StringType)
ccsl_filters_SuperClassClosureFilter.attributes={ccsl_filters_SuperClassClosureFilter_includesSubClass}

# ccsl_filters_BlockLastStatementFilter class attributes and methods

# ccsl_filters_HasSameReferenceFilter class attributes and methods

# ccsl_numberFunctions_CcslNumberFunction class attributes and methods

# ccsl_numberFunctions_CcslIntegerLiteral class attributes and methods
ccsl_numberFunctions_CcslIntegerLiteral_value: Property = Property(name="value", type=StringType)
ccsl_numberFunctions_CcslIntegerLiteral.attributes={ccsl_numberFunctions_CcslIntegerLiteral_value}

# CcslNumberFunction class attributes and methods

# ccsl_numberFunctions_GetIndexOf class attributes and methods

# Relationships
subject1: BinaryAssociation = BinaryAssociation(
    name="subject1",
    ends={
        Property(name="Element", type=ccsl_AtomicRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_AtomicRule", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
context2: BinaryAssociation = BinaryAssociation(
    name="context2",
    ends={
        Property(name="Context", type=ccsl_AtomicRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_AtomicRule3", type=Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule4: BinaryAssociation = BinaryAssociation(
    name="rule4",
    ends={
        Property(name="ccsl_AtomicRule5", type=ccsl_FaultTypeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_FaultTypeDescription", type=ccsl_AtomicRule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actions6: BinaryAssociation = BinaryAssociation(
    name="actions6",
    ends={
        Property(name="InjectionAction", type=ccsl_FaultTypeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_FaultTypeDescription7", type=InjectionAction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
strategy8: BinaryAssociation = BinaryAssociation(
    name="strategy8",
    ends={
        Property(name="InjectionStrategy", type=ccsl_FaultTypeDescription, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_FaultTypeDescription9", type=InjectionStrategy, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="ccsl_Rule", type=ccsl_CompositeRule, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_CompositeRule", type=ccsl_Rule, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
declaredTypes10: BinaryAssociation = BinaryAssociation(
    name="declaredTypes10",
    ends={
        Property(name="complexType_DeclaredType", type=ccsl_namedElements_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_namedElements_Package", type=complexType_DeclaredType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue12: BinaryAssociation = BinaryAssociation(
    name="initialValue12",
    ends={
        Property(name="statements_Statement", type=ccsl_variable_InitializableVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_variable_InitializableVariable", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="datatype_ObjectType", type=ccsl_complexType_AnonymousClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_AnonymousClass", type=datatype_ObjectType, multiplicity=Multiplicity(0, 1))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="datatype_DataType", type=ccsl_variable_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_variable_Variable", type=datatype_DataType, multiplicity=Multiplicity(0, 1))
    }
)
superInterfaces17: BinaryAssociation = BinaryAssociation(
    name="superInterfaces17",
    ends={
        Property(name="complexType_JInterface", type=ccsl_complexType_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_DeclaredType", type=complexType_JInterface, multiplicity=Multiplicity(0, 9999))
    }
)
imports18: BinaryAssociation = BinaryAssociation(
    name="imports18",
    ends={
        Property(name="import_ImportStatement", type=ccsl_complexType_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_DeclaredType19", type=import_ImportStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedTypes20: BinaryAssociation = BinaryAssociation(
    name="nestedTypes20",
    ends={
        Property(name="complexType_DeclaredType22", type=ccsl_complexType_DeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_DeclaredType21", type=complexType_DeclaredType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields23: BinaryAssociation = BinaryAssociation(
    name="fields23",
    ends={
        Property(name="variable_FieldVariable", type=ccsl_complexType_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_ComplexType", type=variable_FieldVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods24: BinaryAssociation = BinaryAssociation(
    name="methods24",
    ends={
        Property(name="method_Method", type=ccsl_complexType_ComplexType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_ComplexType25", type=method_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params26: BinaryAssociation = BinaryAssociation(
    name="params26",
    ends={
        Property(name="variable_ParameterVariable", type=ccsl_method_SimpleMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_method_SimpleMethod", type=variable_ParameterVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType27: BinaryAssociation = BinaryAssociation(
    name="returnType27",
    ends={
        Property(name="datatype_DataType28", type=ccsl_method_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_method_Method", type=datatype_DataType, multiplicity=Multiplicity(0, 1))
    }
)
constructors14: BinaryAssociation = BinaryAssociation(
    name="constructors14",
    ends={
        Property(name="method_Constructor", type=ccsl_complexType_JClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_JClass", type=method_Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass15: BinaryAssociation = BinaryAssociation(
    name="superClass15",
    ends={
        Property(name="complexType_JClass", type=ccsl_complexType_JClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_complexType_JClass16", type=complexType_JClass, multiplicity=Multiplicity(0, 1))
    }
)
from29: BinaryAssociation = BinaryAssociation(
    name="from29",
    ends={
        Property(name="statements_Statement30", type=ccsl_statements_NamedElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_NamedElementAccess", type=statements_Statement, multiplicity=Multiplicity(0, 1))
    }
)
condition31: BinaryAssociation = BinaryAssociation(
    name="condition31",
    ends={
        Property(name="statements_Statement32", type=ccsl_statements_ControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_ControlFlow", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements33: BinaryAssociation = BinaryAssociation(
    name="statements33",
    ends={
        Property(name="statements_Statement34", type=ccsl_statements_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_Block", type=statements_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable35: BinaryAssociation = BinaryAssociation(
    name="variable35",
    ends={
        Property(name="variable_Variable", type=ccsl_statements_VarDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_VarDeclaration", type=variable_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type36: BinaryAssociation = BinaryAssociation(
    name="type36",
    ends={
        Property(name="datatype_ObjectType37", type=ccsl_statements_InstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_InstanceCreation", type=datatype_ObjectType, multiplicity=Multiplicity(0, 1))
    }
)
constructor38: BinaryAssociation = BinaryAssociation(
    name="constructor38",
    ends={
        Property(name="method_Constructor40", type=ccsl_statements_InstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_InstanceCreation39", type=method_Constructor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args41: BinaryAssociation = BinaryAssociation(
    name="args41",
    ends={
        Property(name="statements_Statement43", type=ccsl_statements_InstanceCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_InstanceCreation42", type=statements_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementAccessed44: BinaryAssociation = BinaryAssociation(
    name="elementAccessed44",
    ends={
        Property(name="Element45", type=ccsl_statements_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_Access", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
from46: BinaryAssociation = BinaryAssociation(
    name="from46",
    ends={
        Property(name="statements_Statement48", type=ccsl_statements_Access, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_Access47", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="datatype_ObjectType50", type=ccsl_statements_ArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_ArrayCreation", type=datatype_ObjectType, multiplicity=Multiplicity(0, 1))
    }
)
bodyStatements51: BinaryAssociation = BinaryAssociation(
    name="bodyStatements51",
    ends={
        Property(name="statements_Statement52", type=ccsl_statements_SynchronizedBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_SynchronizedBlock", type=statements_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftOperand58: BinaryAssociation = BinaryAssociation(
    name="leftOperand58",
    ends={
        Property(name="statements_Statement59", type=ccsl_statements_InstanceOf, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_InstanceOf", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand60: BinaryAssociation = BinaryAssociation(
    name="rightOperand60",
    ends={
        Property(name="statements_Statement62", type=ccsl_statements_InstanceOf, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_InstanceOf61", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement63: BinaryAssociation = BinaryAssociation(
    name="statement63",
    ends={
        Property(name="statements_Statement64", type=ccsl_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_ReturnStatement", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operands65: BinaryAssociation = BinaryAssociation(
    name="operands65",
    ends={
        Property(name="statements_Statement66", type=ccsl_expressions_OperatorExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_expressions_OperatorExpression", type=statements_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression67: BinaryAssociation = BinaryAssociation(
    name="expression67",
    ends={
        Property(name="statements_Statement68", type=ccsl_expressions_ParenthesizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_expressions_ParenthesizedExpression", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key53: BinaryAssociation = BinaryAssociation(
    name="key53",
    ends={
        Property(name="statements_Statement55", type=ccsl_statements_SynchronizedBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_SynchronizedBlock54", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression56: BinaryAssociation = BinaryAssociation(
    name="expression56",
    ends={
        Property(name="statements_Statement57", type=ccsl_statements_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_statements_ThrowStatement", type=statements_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases69: BinaryAssociation = BinaryAssociation(
    name="cases69",
    ends={
        Property(name="controlFlow_SwitchCaseBlock", type=ccsl_controlFlow_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_controlFlow_SwitchStatement", type=controlFlow_SwitchCaseBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenStatement70: BinaryAssociation = BinaryAssociation(
    name="thenStatement70",
    ends={
        Property(name="statements_Statement71", type=ccsl_controlFlow_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_controlFlow_IfStatement", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement72: BinaryAssociation = BinaryAssociation(
    name="elseStatement72",
    ends={
        Property(name="statements_Statement74", type=ccsl_controlFlow_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_controlFlow_IfStatement73", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body75: BinaryAssociation = BinaryAssociation(
    name="body75",
    ends={
        Property(name="statements_Statement76", type=ccsl_controlFlow_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_controlFlow_LoopStatement", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses77: BinaryAssociation = BinaryAssociation(
    name="catchClauses77",
    ends={
        Property(name="tryCatch_CatchClause", type=ccsl_tryCatch_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_tryCatch_TryStatement", type=tryCatch_CatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyBlock78: BinaryAssociation = BinaryAssociation(
    name="finallyBlock78",
    ends={
        Property(name="statements_Block", type=ccsl_tryCatch_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_tryCatch_TryStatement79", type=statements_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
handledExceptions85: BinaryAssociation = BinaryAssociation(
    name="handledExceptions85",
    ends={
        Property(name="complexType_JClass87", type=ccsl_tryCatch_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_tryCatch_CatchClause86", type=complexType_JClass, multiplicity=Multiplicity(0, 9999))
    }
)
leftHandSide88: BinaryAssociation = BinaryAssociation(
    name="leftHandSide88",
    ends={
        Property(name="statements_Statement89", type=ccsl_assignment_AbstractAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_assignment_AbstractAssignment", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightHandSide90: BinaryAssociation = BinaryAssociation(
    name="rightHandSide90",
    ends={
        Property(name="statements_Statement91", type=ccsl_assignment_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_assignment_Assignment", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from92: BinaryAssociation = BinaryAssociation(
    name="from92",
    ends={
        Property(name="statements_Statement93", type=ccsl_invocation_MethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_invocation_MethodInvocation", type=statements_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body80: BinaryAssociation = BinaryAssociation(
    name="body80",
    ends={
        Property(name="statements_Block81", type=ccsl_tryCatch_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_tryCatch_CatchClause", type=statements_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable82: BinaryAssociation = BinaryAssociation(
    name="variable82",
    ends={
        Property(name="variable_ParameterVariable84", type=ccsl_tryCatch_CatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_tryCatch_CatchClause83", type=variable_ParameterVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args94: BinaryAssociation = BinaryAssociation(
    name="args94",
    ends={
        Property(name="statements_Statement95", type=ccsl_invocation_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_invocation_Invocation", type=statements_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructor96: BinaryAssociation = BinaryAssociation(
    name="constructor96",
    ends={
        Property(name="method_Constructor97", type=ccsl_invocation_ConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_invocation_ConstructorInvocation", type=method_Constructor, multiplicity=Multiplicity(0, 1))
    }
)
method98: BinaryAssociation = BinaryAssociation(
    name="method98",
    ends={
        Property(name="method_Method99", type=ccsl_invocation_SimpleMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_invocation_SimpleMethodInvocation", type=method_Method, multiplicity=Multiplicity(0, 1))
    }
)
importedElement100: BinaryAssociation = BinaryAssociation(
    name="importedElement100",
    ends={
        Property(name="import_ImportableElement", type=ccsl_import_ImportStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_import_ImportStatement", type=import_ImportableElement, multiplicity=Multiplicity(0, 1))
    }
)
type101: BinaryAssociation = BinaryAssociation(
    name="type101",
    ends={
        Property(name="complexType_AnnotationType", type=ccsl_annotation_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_annotation_Annotation", type=complexType_AnnotationType, multiplicity=Multiplicity(0, 1))
    }
)
annotations102: BinaryAssociation = BinaryAssociation(
    name="annotations102",
    ends={
        Property(name="annotation_Annotation", type=ccsl_annotation_AnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_annotation_AnnotableElement", type=annotation_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments103: BinaryAssociation = BinaryAssociation(
    name="typeArguments103",
    ends={
        Property(name="datatype_ObjectType104", type=ccsl_datatype_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_datatype_ParameterizedType", type=datatype_ObjectType, multiplicity=Multiplicity(0, 9999))
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="complexType_DeclaredType107", type=ccsl_datatype_ParameterizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_datatype_ParameterizedType106", type=complexType_DeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
type108: BinaryAssociation = BinaryAssociation(
    name="type108",
    ends={
        Property(name="datatype_DataType109", type=ccsl_datatype_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_datatype_ArrayType", type=datatype_DataType, multiplicity=Multiplicity(0, 1))
    }
)
contextElements110: BinaryAssociation = BinaryAssociation(
    name="contextElements110",
    ends={
        Property(name="Element111", type=ccsl_context_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_context_Context", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
filters112: BinaryAssociation = BinaryAssociation(
    name="filters112",
    ends={
        Property(name="filters_Filter", type=ccsl_context_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_context_Context113", type=filters_Filter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target114: BinaryAssociation = BinaryAssociation(
    name="target114",
    ends={
        Property(name="Element115", type=ccsl_faultTypeDescription_InjectionAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_faultTypeDescription_InjectionAction", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
replaceMap116: BinaryAssociation = BinaryAssociation(
    name="replaceMap116",
    ends={
        Property(name="action_ArithmeticOperatorMap", type=ccsl_action_ReplaceArithmeticOperatorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_action_ReplaceArithmeticOperatorAction", type=action_ArithmeticOperatorMap, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targets117: BinaryAssociation = BinaryAssociation(
    name="targets117",
    ends={
        Property(name="Element118", type=ccsl_filters_AtomicFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_AtomicFilter", type=Element, multiplicity=Multiplicity(1, 9999))
    }
)
filters119: BinaryAssociation = BinaryAssociation(
    name="filters119",
    ends={
        Property(name="filters_Filter120", type=ccsl_filters_CompositeFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_CompositeFilter", type=filters_Filter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targetTemplate121: BinaryAssociation = BinaryAssociation(
    name="targetTemplate121",
    ends={
        Property(name="Element122", type=ccsl_filters_TemplateFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_TemplateFilter", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
context123: BinaryAssociation = BinaryAssociation(
    name="context123",
    ends={
        Property(name="Context125", type=ccsl_filters_TemplateFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_TemplateFilter124", type=Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements126: BinaryAssociation = BinaryAssociation(
    name="elements126",
    ends={
        Property(name="namedElements_NamedElement", type=ccsl_filters_SameNameFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_SameNameFilter", type=namedElements_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
context127: BinaryAssociation = BinaryAssociation(
    name="context127",
    ends={
        Property(name="Context128", type=ccsl_filters_CountFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_CountFilter", type=Context, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
container129: BinaryAssociation = BinaryAssociation(
    name="container129",
    ends={
        Property(name="Element131", type=ccsl_filters_CountFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_CountFilter130", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
field132: BinaryAssociation = BinaryAssociation(
    name="field132",
    ends={
        Property(name="Element134", type=ccsl_filters_CountFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_CountFilter133", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
implicityOperand135: BinaryAssociation = BinaryAssociation(
    name="implicityOperand135",
    ends={
        Property(name="Element136", type=ccsl_filters_ImplicityOperandFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ImplicityOperandFilter", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
operatorExpression137: BinaryAssociation = BinaryAssociation(
    name="operatorExpression137",
    ends={
        Property(name="expressions_OperatorExpression", type=ccsl_filters_ImplicityOperandFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ImplicityOperandFilter138", type=expressions_OperatorExpression, multiplicity=Multiplicity(1, 1))
    }
)
implicityContainer139: BinaryAssociation = BinaryAssociation(
    name="implicityContainer139",
    ends={
        Property(name="Element140", type=ccsl_filters_ImplicityContainerFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ImplicityContainerFilter", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
implicityField141: BinaryAssociation = BinaryAssociation(
    name="implicityField141",
    ends={
        Property(name="Element143", type=ccsl_filters_ImplicityContainerFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ImplicityContainerFilter142", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
context144: BinaryAssociation = BinaryAssociation(
    name="context144",
    ends={
        Property(name="Context146", type=ccsl_filters_ImplicityContainerFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ImplicityContainerFilter145", type=Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context147: BinaryAssociation = BinaryAssociation(
    name="context147",
    ends={
        Property(name="Context148", type=ccsl_filters_IsKindOfFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_IsKindOfFilter", type=Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type149: BinaryAssociation = BinaryAssociation(
    name="type149",
    ends={
        Property(name="datatype_DataType151", type=ccsl_filters_IsKindOfFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_IsKindOfFilter150", type=datatype_DataType, multiplicity=Multiplicity(1, 1))
    }
)
context152: BinaryAssociation = BinaryAssociation(
    name="context152",
    ends={
        Property(name="Context153", type=ccsl_filters_SuperMethodClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_SuperMethodClosureFilter", type=Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
superMethod154: BinaryAssociation = BinaryAssociation(
    name="superMethod154",
    ends={
        Property(name="method_Method156", type=ccsl_filters_SuperMethodClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_SuperMethodClosureFilter155", type=method_Method, multiplicity=Multiplicity(1, 1))
    }
)
context157: BinaryAssociation = BinaryAssociation(
    name="context157",
    ends={
        Property(name="Context158", type=ccsl_filters_IsTypeOfFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_IsTypeOfFilter", type=Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type159: BinaryAssociation = BinaryAssociation(
    name="type159",
    ends={
        Property(name="datatype_DataType161", type=ccsl_filters_IsTypeOfFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_IsTypeOfFilter160", type=datatype_DataType, multiplicity=Multiplicity(1, 1))
    }
)
superComplexType162: BinaryAssociation = BinaryAssociation(
    name="superComplexType162",
    ends={
        Property(name="complexType_ComplexType", type=ccsl_filters_ChildClosureComplexTypeFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ChildClosureComplexTypeFilter", type=complexType_ComplexType, multiplicity=Multiplicity(1, 1))
    }
)
childComplexType163: BinaryAssociation = BinaryAssociation(
    name="childComplexType163",
    ends={
        Property(name="complexType_ComplexType165", type=ccsl_filters_ChildClosureComplexTypeFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ChildClosureComplexTypeFilter164", type=complexType_ComplexType, multiplicity=Multiplicity(1, 1))
    }
)
context166: BinaryAssociation = BinaryAssociation(
    name="context166",
    ends={
        Property(name="Context168", type=ccsl_filters_ChildClosureComplexTypeFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_ChildClosureComplexTypeFilter167", type=Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide169: BinaryAssociation = BinaryAssociation(
    name="leftHandSide169",
    ends={
        Property(name="numberFunctions_CcslNumberFunction", type=ccsl_filters_EquationFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_EquationFilter", type=numberFunctions_CcslNumberFunction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rightHandSide170: BinaryAssociation = BinaryAssociation(
    name="rightHandSide170",
    ends={
        Property(name="numberFunctions_CcslNumberFunction172", type=ccsl_filters_EquationFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_EquationFilter171", type=numberFunctions_CcslNumberFunction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
access173: BinaryAssociation = BinaryAssociation(
    name="access173",
    ends={
        Property(name="statements_Access", type=ccsl_filters_FromClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_FromClosureFilter", type=statements_Access, multiplicity=Multiplicity(1, 1))
    }
)
from174: BinaryAssociation = BinaryAssociation(
    name="from174",
    ends={
        Property(name="statements_Statement176", type=ccsl_filters_FromClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_FromClosureFilter175", type=statements_Statement, multiplicity=Multiplicity(1, 1))
    }
)
context177: BinaryAssociation = BinaryAssociation(
    name="context177",
    ends={
        Property(name="Context179", type=ccsl_filters_FromClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_FromClosureFilter178", type=Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superClass180: BinaryAssociation = BinaryAssociation(
    name="superClass180",
    ends={
        Property(name="complexType_JClass181", type=ccsl_filters_SuperClassClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_SuperClassClosureFilter", type=complexType_JClass, multiplicity=Multiplicity(0, 1))
    }
)
subClass182: BinaryAssociation = BinaryAssociation(
    name="subClass182",
    ends={
        Property(name="complexType_JClass184", type=ccsl_filters_SuperClassClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_SuperClassClosureFilter183", type=complexType_JClass, multiplicity=Multiplicity(0, 1))
    }
)
context185: BinaryAssociation = BinaryAssociation(
    name="context185",
    ends={
        Property(name="Context187", type=ccsl_filters_SuperClassClosureFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_SuperClassClosureFilter186", type=Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastStatement188: BinaryAssociation = BinaryAssociation(
    name="lastStatement188",
    ends={
        Property(name="statements_Statement189", type=ccsl_filters_BlockLastStatementFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_BlockLastStatementFilter", type=statements_Statement, multiplicity=Multiplicity(0, 1))
    }
)
context190: BinaryAssociation = BinaryAssociation(
    name="context190",
    ends={
        Property(name="Context192", type=ccsl_filters_BlockLastStatementFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_filters_BlockLastStatementFilter191", type=Context, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container193: BinaryAssociation = BinaryAssociation(
    name="container193",
    ends={
        Property(name="Element194", type=ccsl_numberFunctions_GetIndexOf, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_numberFunctions_GetIndexOf", type=Element, multiplicity=Multiplicity(1, 1))
    }
)
field195: BinaryAssociation = BinaryAssociation(
    name="field195",
    ends={
        Property(name="Element197", type=ccsl_numberFunctions_GetIndexOf, multiplicity=Multiplicity(1, 1)),
        Property(name="ccsl_numberFunctions_GetIndexOf196", type=Element, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ccsl_Rule_Root = Generalization(general=Root, specific=ccsl_Rule)
gen_ccsl_CompositeRule_Rule = Generalization(general=Rule, specific=ccsl_CompositeRule)
gen_ccsl_FaultTypeDescription_Root = Generalization(general=Root, specific=ccsl_FaultTypeDescription)
gen_ccsl_AtomicRule_Rule = Generalization(general=Rule, specific=ccsl_AtomicRule)
gen_ccsl_namedElements_NamedElement_Element = Generalization(general=Element, specific=ccsl_namedElements_NamedElement)
gen_ccsl_namedElements_Package_namedElements_NamedElement = Generalization(general=namedElements_NamedElement, specific=ccsl_namedElements_Package)
gen_ccsl_namedElements_Package_import_ImportableElement = Generalization(general=import_ImportableElement, specific=ccsl_namedElements_Package)
gen_ccsl_variable_Variable_NamedElement = Generalization(general=NamedElement, specific=ccsl_variable_Variable)
gen_ccsl_variable_ParameterVariable_annotation_AnnotableElement = Generalization(general=annotation_AnnotableElement, specific=ccsl_variable_ParameterVariable)
gen_ccsl_variable_LocalVariable_InitializableVariable = Generalization(general=InitializableVariable, specific=ccsl_variable_LocalVariable)
gen_ccsl_variable_InitializableVariable_Variable = Generalization(general=Variable, specific=ccsl_variable_InitializableVariable)
gen_ccsl_variable_FieldVariable_variable_InitializableVariable = Generalization(general=variable_InitializableVariable, specific=ccsl_variable_FieldVariable)
gen_ccsl_variable_FieldVariable_annotation_AnnotableElement = Generalization(general=annotation_AnnotableElement, specific=ccsl_variable_FieldVariable)
gen_ccsl_complexType_JInterface_complexType_DeclaredType = Generalization(general=complexType_DeclaredType, specific=ccsl_complexType_JInterface)
gen_ccsl_complexType_JInterface_complexType_ComplexType = Generalization(general=complexType_ComplexType, specific=ccsl_complexType_JInterface)
gen_ccsl_complexType_JInterface_annotation_AnnotableElement = Generalization(general=annotation_AnnotableElement, specific=ccsl_complexType_JInterface)
gen_ccsl_complexType_AnonymousClass_ComplexType = Generalization(general=ComplexType, specific=ccsl_complexType_AnonymousClass)
gen_ccsl_complexType_DeclaredType_namedElements_NamedElement = Generalization(general=namedElements_NamedElement, specific=ccsl_complexType_DeclaredType)
gen_ccsl_complexType_DeclaredType_datatype_ObjectType = Generalization(general=datatype_ObjectType, specific=ccsl_complexType_DeclaredType)
gen_ccsl_complexType_DeclaredType_import_ImportableElement = Generalization(general=import_ImportableElement, specific=ccsl_complexType_DeclaredType)
gen_ccsl_variable_ParameterVariable_variable_Variable = Generalization(general=variable_Variable, specific=ccsl_variable_ParameterVariable)
gen_ccsl_complexType_ComplexType_Element = Generalization(general=Element, specific=ccsl_complexType_ComplexType)
gen_ccsl_complexType_AnnotationType_DeclaredType = Generalization(general=DeclaredType, specific=ccsl_complexType_AnnotationType)
gen_ccsl_method_Constructor_SimpleMethod = Generalization(general=SimpleMethod, specific=ccsl_method_Constructor)
gen_ccsl_method_SimpleMethod_elements_Element = Generalization(general=elements_Element, specific=ccsl_method_SimpleMethod)
gen_ccsl_method_SimpleMethod_annotation_AnnotableElement = Generalization(general=annotation_AnnotableElement, specific=ccsl_method_SimpleMethod)
gen_ccsl_complexType_JClass_complexType_DeclaredType = Generalization(general=complexType_DeclaredType, specific=ccsl_complexType_JClass)
gen_ccsl_method_Method_namedElements_NamedElement = Generalization(general=namedElements_NamedElement, specific=ccsl_method_Method)
gen_ccsl_method_Method_method_SimpleMethod = Generalization(general=method_SimpleMethod, specific=ccsl_method_Method)
gen_ccsl_complexType_JClass_complexType_ComplexType = Generalization(general=complexType_ComplexType, specific=ccsl_complexType_JClass)
gen_ccsl_complexType_JClass_annotation_AnnotableElement = Generalization(general=annotation_AnnotableElement, specific=ccsl_complexType_JClass)
gen_ccsl_statements_Statement_Element = Generalization(general=Element, specific=ccsl_statements_Statement)
gen_ccsl_statements_NamedElementAccess_Statement = Generalization(general=Statement, specific=ccsl_statements_NamedElementAccess)
gen_ccsl_statements_VariableAccess_Access = Generalization(general=Access, specific=ccsl_statements_VariableAccess)
gen_ccsl_statements_DataTypeAccess_Access = Generalization(general=Access, specific=ccsl_statements_DataTypeAccess)
gen_ccsl_statements_ControlFlow_Statement = Generalization(general=Statement, specific=ccsl_statements_ControlFlow)
gen_ccsl_statements_Block_Statement = Generalization(general=Statement, specific=ccsl_statements_Block)
gen_ccsl_statements_VarDeclaration_Statement = Generalization(general=Statement, specific=ccsl_statements_VarDeclaration)
gen_ccsl_statements_InstanceCreation_Statement = Generalization(general=Statement, specific=ccsl_statements_InstanceCreation)
gen_ccsl_statements_Access_Statement = Generalization(general=Statement, specific=ccsl_statements_Access)
gen_ccsl_statements_ArrayCreation_Statement = Generalization(general=Statement, specific=ccsl_statements_ArrayCreation)
gen_ccsl_statements_SynchronizedBlock_Statement = Generalization(general=Statement, specific=ccsl_statements_SynchronizedBlock)
gen_ccsl_statements_EmptyStatement_Statement = Generalization(general=Statement, specific=ccsl_statements_EmptyStatement)
gen_ccsl_statements_InstanceOf_Statement = Generalization(general=Statement, specific=ccsl_statements_InstanceOf)
gen_ccsl_statements_ReturnStatement_Statement = Generalization(general=Statement, specific=ccsl_statements_ReturnStatement)
gen_ccsl_statements_ThisStatement_Statement = Generalization(general=Statement, specific=ccsl_statements_ThisStatement)
gen_ccsl_statements_BreakStatement_Statement = Generalization(general=Statement, specific=ccsl_statements_BreakStatement)
gen_ccsl_statements_ContinueStatement_Statement = Generalization(general=Statement, specific=ccsl_statements_ContinueStatement)
gen_ccsl_expressions_OperatorExpression_Statement = Generalization(general=Statement, specific=ccsl_expressions_OperatorExpression)
gen_ccsl_expressions_ParenthesizedExpression_Statement = Generalization(general=Statement, specific=ccsl_expressions_ParenthesizedExpression)
gen_ccsl_expressions_StringConcatenation_OperatorExpression = Generalization(general=OperatorExpression, specific=ccsl_expressions_StringConcatenation)
gen_ccsl_expressions_InfixExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=ccsl_expressions_InfixExpression)
gen_ccsl_expressions_BooleanExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=ccsl_expressions_BooleanExpression)
gen_ccsl_expressions_ArithmeticExpression_OperatorExpression = Generalization(general=OperatorExpression, specific=ccsl_expressions_ArithmeticExpression)
gen_ccsl_literalValues_LiteralValue_Statement = Generalization(general=Statement, specific=ccsl_literalValues_LiteralValue)
gen_ccsl_literalValues_NullLiteral_LiteralValue = Generalization(general=LiteralValue, specific=ccsl_literalValues_NullLiteral)
gen_ccsl_literalValues_CharacterLiteral_LiteralValue = Generalization(general=LiteralValue, specific=ccsl_literalValues_CharacterLiteral)
gen_ccsl_literalValues_StringLiteral_LiteralValue = Generalization(general=LiteralValue, specific=ccsl_literalValues_StringLiteral)
gen_ccsl_literalValues_NumberLiteral_LiteralValue = Generalization(general=LiteralValue, specific=ccsl_literalValues_NumberLiteral)
gen_ccsl_literalValues_BooleanLiteral_LiteralValue = Generalization(general=LiteralValue, specific=ccsl_literalValues_BooleanLiteral)
gen_ccsl_controlFlow_SwitchStatement_ControlFlow = Generalization(general=ControlFlow, specific=ccsl_controlFlow_SwitchStatement)
gen_ccsl_controlFlow_SwitchCaseBlock_Block = Generalization(general=Block, specific=ccsl_controlFlow_SwitchCaseBlock)
gen_ccsl_controlFlow_IfStatement_ControlFlow = Generalization(general=ControlFlow, specific=ccsl_controlFlow_IfStatement)
gen_ccsl_controlFlow_LoopStatement_ControlFlow = Generalization(general=ControlFlow, specific=ccsl_controlFlow_LoopStatement)
gen_ccsl_tryCatch_TryStatement_Statement = Generalization(general=Statement, specific=ccsl_tryCatch_TryStatement)
gen_ccsl_tryCatch_CatchClause_Statement = Generalization(general=Statement, specific=ccsl_tryCatch_CatchClause)
gen_ccsl_assignment_AbstractAssignment_Statement = Generalization(general=Statement, specific=ccsl_assignment_AbstractAssignment)
gen_ccsl_assignment_Assignment_AbstractAssignment = Generalization(general=AbstractAssignment, specific=ccsl_assignment_Assignment)
gen_ccsl_assignment_UnaryAssignment_AbstractAssignment = Generalization(general=AbstractAssignment, specific=ccsl_assignment_UnaryAssignment)
gen_ccsl_assignment_PrefixUnaryAssignment_UnaryAssignment = Generalization(general=UnaryAssignment, specific=ccsl_assignment_PrefixUnaryAssignment)
gen_ccsl_assignment_PostfixUnaryAssignment_UnaryAssignment = Generalization(general=UnaryAssignment, specific=ccsl_assignment_PostfixUnaryAssignment)
gen_ccsl_invocation_MethodInvocation_SimpleMethodInvocation = Generalization(general=SimpleMethodInvocation, specific=ccsl_invocation_MethodInvocation)
gen_ccsl_invocation_ConstructorInvocation_Invocation = Generalization(general=Invocation, specific=ccsl_invocation_ConstructorInvocation)
gen_ccsl_invocation_SimpleMethodInvocation_Invocation = Generalization(general=Invocation, specific=ccsl_invocation_SimpleMethodInvocation)
gen_ccsl_import_ImportableElement_Element = Generalization(general=Element, specific=ccsl_import_ImportableElement)
gen_ccsl_import_ImportStatement_Statement = Generalization(general=Statement, specific=ccsl_import_ImportStatement)
gen_ccsl_annotation_Annotation_Statement = Generalization(general=Statement, specific=ccsl_annotation_Annotation)
gen_ccsl_annotation_AnnotableElement_Element = Generalization(general=Element, specific=ccsl_annotation_AnnotableElement)
gen_ccsl_invocation_SuperMethodInvocation_SimpleMethodInvocation = Generalization(general=SimpleMethodInvocation, specific=ccsl_invocation_SuperMethodInvocation)
gen_ccsl_invocation_Invocation_Statement = Generalization(general=Statement, specific=ccsl_invocation_Invocation)
gen_ccsl_datatype_StringPrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=ccsl_datatype_StringPrimitiveType)
gen_ccsl_datatype_BooleanPrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=ccsl_datatype_BooleanPrimitiveType)
gen_ccsl_datatype_ShortPrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=ccsl_datatype_ShortPrimitiveType)
gen_ccsl_datatype_ObjectType_DataType = Generalization(general=DataType, specific=ccsl_datatype_ObjectType)
gen_ccsl_datatype_ParameterizedType_ObjectType = Generalization(general=ObjectType, specific=ccsl_datatype_ParameterizedType)
gen_ccsl_datatype_GenericType_ComplexType = Generalization(general=ComplexType, specific=ccsl_datatype_GenericType)
gen_ccsl_datatype_IntPrimitiveType_PrimitiveType = Generalization(general=PrimitiveType, specific=ccsl_datatype_IntPrimitiveType)
gen_ccsl_datatype_ArrayType_ObjectType = Generalization(general=ObjectType, specific=ccsl_datatype_ArrayType)
gen_ccsl_datatype_VoidType_PrimitiveType = Generalization(general=PrimitiveType, specific=ccsl_datatype_VoidType)
gen_ccsl_datatype_DataType_Element = Generalization(general=Element, specific=ccsl_datatype_DataType)
gen_ccsl_datatype_PrimitiveType_DataType = Generalization(general=DataType, specific=ccsl_datatype_PrimitiveType)
gen_ccsl_action_DeleteAction_InjectionAction = Generalization(general=InjectionAction, specific=ccsl_action_DeleteAction)
gen_ccsl_action_MoveScopeUpAction_InjectionAction = Generalization(general=InjectionAction, specific=ccsl_action_MoveScopeUpAction)
gen_ccsl_action_DeleteInfixOperatorAction_InjectionAction = Generalization(general=InjectionAction, specific=ccsl_action_DeleteInfixOperatorAction)
gen_ccsl_action_ChangeLiteralValueAction_InjectionAction = Generalization(general=InjectionAction, specific=ccsl_action_ChangeLiteralValueAction)
gen_ccsl_action_DeleteRandomStatementAction_InjectionAction = Generalization(general=InjectionAction, specific=ccsl_action_DeleteRandomStatementAction)
gen_ccsl_action_ReplaceVariableAccessAction_InjectionAction = Generalization(general=InjectionAction, specific=ccsl_action_ReplaceVariableAccessAction)
gen_ccsl_action_ReplaceArithmeticOperatorAction_InjectionAction = Generalization(general=InjectionAction, specific=ccsl_action_ReplaceArithmeticOperatorAction)
gen_ccsl_strategy_AllStrategy_InjectionStrategy = Generalization(general=InjectionStrategy, specific=ccsl_strategy_AllStrategy)
gen_ccsl_booleanFunctions_CcslBooleanFunction_CcslFunction = Generalization(general=CcslFunction, specific=ccsl_booleanFunctions_CcslBooleanFunction)
gen_ccsl_filters_Filter_CcslBooleanFunction = Generalization(general=CcslBooleanFunction, specific=ccsl_filters_Filter)
gen_ccsl_filters_AtomicFilter_Filter = Generalization(general=Filter, specific=ccsl_filters_AtomicFilter)
gen_ccsl_filters_CompositeFilter_Filter = Generalization(general=Filter, specific=ccsl_filters_CompositeFilter)
gen_ccsl_filters_PropertyFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_PropertyFilter)
gen_ccsl_filters_TemplateFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_TemplateFilter)
gen_ccsl_filters_SameNameFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_SameNameFilter)
gen_ccsl_filters_CountFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_CountFilter)
gen_ccsl_filters_RegexMatch_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_RegexMatch)
gen_ccsl_filters_ImplicityOperandFilter_TemplateFilter = Generalization(general=TemplateFilter, specific=ccsl_filters_ImplicityOperandFilter)
gen_ccsl_filters_ImplicityContainerFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_ImplicityContainerFilter)
gen_ccsl_filters_IsKindOfFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_IsKindOfFilter)
gen_ccsl_filters_SuperMethodClosureFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_SuperMethodClosureFilter)
gen_ccsl_filters_IsTypeOfFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_IsTypeOfFilter)
gen_ccsl_filters_ChildClosureComplexTypeFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_ChildClosureComplexTypeFilter)
gen_ccsl_filters_IsStringFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_IsStringFilter)
gen_ccsl_filters_FromClosureFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_FromClosureFilter)
gen_ccsl_filters_SuperClassClosureFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_SuperClassClosureFilter)
gen_ccsl_filters_BlockLastStatementFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_BlockLastStatementFilter)
gen_ccsl_filters_HasSameReferenceFilter_AtomicFilter = Generalization(general=AtomicFilter, specific=ccsl_filters_HasSameReferenceFilter)
gen_ccsl_numberFunctions_CcslNumberFunction_CcslFunction = Generalization(general=CcslFunction, specific=ccsl_numberFunctions_CcslNumberFunction)
gen_ccsl_numberFunctions_CcslIntegerLiteral_CcslNumberFunction = Generalization(general=CcslNumberFunction, specific=ccsl_numberFunctions_CcslIntegerLiteral)
gen_ccsl_numberFunctions_GetIndexOf_CcslNumberFunction = Generalization(general=CcslNumberFunction, specific=ccsl_numberFunctions_GetIndexOf)

# Domain Model
domain_model = DomainModel(
    name="ccsl",
    types={ccsl_Rule, Root, ccsl_CompositeRule, Rule, Element, Context, ccsl_Root, ccsl_FaultTypeDescription, InjectionAction, InjectionStrategy, ccsl_elements_Element, ccsl_AtomicRule, ccsl_namedElements_NamedElement, ccsl_namedElements_Package, namedElements_NamedElement, import_ImportableElement, complexType_DeclaredType, ccsl_variable_Variable, NamedElement, datatype_DataType, annotation_AnnotableElement, ccsl_variable_LocalVariable, InitializableVariable, ccsl_variable_InitializableVariable, Variable, statements_Statement, ccsl_variable_FieldVariable, variable_InitializableVariable, ccsl_complexType_JInterface, complexType_ComplexType, ccsl_complexType_AnonymousClass, ComplexType, datatype_ObjectType, ccsl_complexType_DeclaredType, ccsl_variable_ParameterVariable, variable_Variable, complexType_JInterface, import_ImportStatement, ccsl_complexType_ComplexType, variable_FieldVariable, method_Method, ccsl_complexType_AnnotationType, DeclaredType, ccsl_method_Constructor, SimpleMethod, ccsl_method_SimpleMethod, elements_Element, variable_ParameterVariable, ccsl_complexType_JClass, ccsl_method_Method, method_SimpleMethod, method_Constructor, complexType_JClass, ccsl_statements_Statement, ccsl_statements_NamedElementAccess, Statement, ccsl_statements_VariableAccess, Access, ccsl_statements_DataTypeAccess, ccsl_statements_ControlFlow, ccsl_statements_Block, ccsl_statements_VarDeclaration, ccsl_statements_InstanceCreation, ccsl_statements_Access, ccsl_statements_ArrayCreation, ccsl_statements_SynchronizedBlock, ccsl_statements_EmptyStatement, ccsl_statements_InstanceOf, ccsl_statements_ReturnStatement, ccsl_statements_ThisStatement, ccsl_statements_BreakStatement, ccsl_statements_ContinueStatement, ccsl_expressions_OperatorExpression, ccsl_expressions_ParenthesizedExpression, ccsl_expressions_StringConcatenation, OperatorExpression, ccsl_expressions_InfixExpression, ccsl_expressions_BooleanExpression, ccsl_expressions_ArithmeticExpression, ccsl_statements_ThrowStatement, ccsl_literalValues_LiteralValue, ccsl_literalValues_NullLiteral, LiteralValue, ccsl_literalValues_CharacterLiteral, ccsl_literalValues_StringLiteral, ccsl_literalValues_NumberLiteral, ccsl_literalValues_BooleanLiteral, ccsl_controlFlow_SwitchStatement, ControlFlow, controlFlow_SwitchCaseBlock, ccsl_controlFlow_SwitchCaseBlock, Block, ccsl_controlFlow_IfStatement, ccsl_controlFlow_LoopStatement, ccsl_tryCatch_TryStatement, tryCatch_CatchClause, statements_Block, ccsl_tryCatch_CatchClause, ccsl_assignment_AbstractAssignment, ccsl_assignment_Assignment, AbstractAssignment, ccsl_assignment_UnaryAssignment, ccsl_assignment_PrefixUnaryAssignment, UnaryAssignment, ccsl_assignment_PostfixUnaryAssignment, ccsl_invocation_MethodInvocation, SimpleMethodInvocation, ccsl_invocation_ConstructorInvocation, Invocation, ccsl_invocation_SimpleMethodInvocation, ccsl_import_ImportableElement, ccsl_import_ImportStatement, ccsl_annotation_Annotation, complexType_AnnotationType, ccsl_annotation_AnnotableElement, annotation_Annotation, ccsl_invocation_SuperMethodInvocation, ccsl_invocation_Invocation, ccsl_datatype_StringPrimitiveType, PrimitiveType, ccsl_datatype_BooleanPrimitiveType, ccsl_datatype_ShortPrimitiveType, ccsl_datatype_ObjectType, ccsl_datatype_ParameterizedType, ObjectType, ccsl_datatype_GenericType, ccsl_datatype_IntPrimitiveType, ccsl_datatype_ArrayType, ccsl_datatype_VoidType, ccsl_context_Context, filters_Filter, ccsl_faultTypeDescription_InjectionAction, ccsl_datatype_DataType, ccsl_datatype_PrimitiveType, DataType, ccsl_faultTypeDescription_InjectionStrategy, ccsl_action_DeleteAction, ccsl_action_MoveScopeUpAction, ccsl_action_DeleteInfixOperatorAction, ccsl_action_ChangeLiteralValueAction, ccsl_action_DeleteRandomStatementAction, ccsl_action_ReplaceVariableAccessAction, ccsl_action_ReplaceArithmeticOperatorAction, action_ArithmeticOperatorMap, ccsl_action_ArithmeticOperatorMap, ccsl_strategy_AllStrategy, ccsl_functions_CcslFunction, ccsl_booleanFunctions_CcslBooleanFunction, CcslFunction, ccsl_filters_Filter, CcslBooleanFunction, ccsl_filters_AtomicFilter, Filter, ccsl_filters_CompositeFilter, ccsl_filters_PropertyFilter, AtomicFilter, ccsl_filters_TemplateFilter, ccsl_filters_SameNameFilter, ccsl_filters_CountFilter, ccsl_filters_RegexMatch, ccsl_filters_ImplicityOperandFilter, TemplateFilter, expressions_OperatorExpression, ccsl_filters_ImplicityContainerFilter, ccsl_filters_IsKindOfFilter, ccsl_filters_SuperMethodClosureFilter, ccsl_filters_IsTypeOfFilter, ccsl_filters_ChildClosureComplexTypeFilter, ccsl_filters_IsStringFilter, ccsl_filters_EquationFilter, numberFunctions_CcslNumberFunction, ccsl_filters_FromClosureFilter, statements_Access, ccsl_filters_SuperClassClosureFilter, ccsl_filters_BlockLastStatementFilter, ccsl_filters_HasSameReferenceFilter, ccsl_numberFunctions_CcslNumberFunction, ccsl_numberFunctions_CcslIntegerLiteral, CcslNumberFunction, ccsl_numberFunctions_GetIndexOf, LogicOperator, CollectionKind, Inheritance, Visibility, BooleanOperator, ArithmeticOperator, AssignmentOperator, UnaryAssignmentOperator, EquationOperator},
    associations={subject1, context2, rule4, actions6, strategy8, rules0, declaredTypes10, initialValue12, type13, type11, superInterfaces17, imports18, nestedTypes20, fields23, methods24, params26, returnType27, constructors14, superClass15, from29, condition31, statements33, variable35, type36, constructor38, args41, elementAccessed44, from46, type49, bodyStatements51, leftOperand58, rightOperand60, statement63, operands65, expression67, key53, expression56, cases69, thenStatement70, elseStatement72, body75, catchClauses77, finallyBlock78, handledExceptions85, leftHandSide88, rightHandSide90, from92, body80, variable82, args94, constructor96, method98, importedElement100, type101, annotations102, typeArguments103, type105, type108, contextElements110, filters112, target114, replaceMap116, targets117, filters119, targetTemplate121, context123, elements126, context127, container129, field132, implicityOperand135, operatorExpression137, implicityContainer139, implicityField141, context144, context147, type149, context152, superMethod154, context157, type159, superComplexType162, childComplexType163, context166, leftHandSide169, rightHandSide170, access173, from174, context177, superClass180, subClass182, context185, lastStatement188, context190, container193, field195},
    generalizations={gen_ccsl_Rule_Root, gen_ccsl_CompositeRule_Rule, gen_ccsl_FaultTypeDescription_Root, gen_ccsl_AtomicRule_Rule, gen_ccsl_namedElements_NamedElement_Element, gen_ccsl_namedElements_Package_namedElements_NamedElement, gen_ccsl_namedElements_Package_import_ImportableElement, gen_ccsl_variable_Variable_NamedElement, gen_ccsl_variable_ParameterVariable_annotation_AnnotableElement, gen_ccsl_variable_LocalVariable_InitializableVariable, gen_ccsl_variable_InitializableVariable_Variable, gen_ccsl_variable_FieldVariable_variable_InitializableVariable, gen_ccsl_variable_FieldVariable_annotation_AnnotableElement, gen_ccsl_complexType_JInterface_complexType_DeclaredType, gen_ccsl_complexType_JInterface_complexType_ComplexType, gen_ccsl_complexType_JInterface_annotation_AnnotableElement, gen_ccsl_complexType_AnonymousClass_ComplexType, gen_ccsl_complexType_DeclaredType_namedElements_NamedElement, gen_ccsl_complexType_DeclaredType_datatype_ObjectType, gen_ccsl_complexType_DeclaredType_import_ImportableElement, gen_ccsl_variable_ParameterVariable_variable_Variable, gen_ccsl_complexType_ComplexType_Element, gen_ccsl_complexType_AnnotationType_DeclaredType, gen_ccsl_method_Constructor_SimpleMethod, gen_ccsl_method_SimpleMethod_elements_Element, gen_ccsl_method_SimpleMethod_annotation_AnnotableElement, gen_ccsl_complexType_JClass_complexType_DeclaredType, gen_ccsl_method_Method_namedElements_NamedElement, gen_ccsl_method_Method_method_SimpleMethod, gen_ccsl_complexType_JClass_complexType_ComplexType, gen_ccsl_complexType_JClass_annotation_AnnotableElement, gen_ccsl_statements_Statement_Element, gen_ccsl_statements_NamedElementAccess_Statement, gen_ccsl_statements_VariableAccess_Access, gen_ccsl_statements_DataTypeAccess_Access, gen_ccsl_statements_ControlFlow_Statement, gen_ccsl_statements_Block_Statement, gen_ccsl_statements_VarDeclaration_Statement, gen_ccsl_statements_InstanceCreation_Statement, gen_ccsl_statements_Access_Statement, gen_ccsl_statements_ArrayCreation_Statement, gen_ccsl_statements_SynchronizedBlock_Statement, gen_ccsl_statements_EmptyStatement_Statement, gen_ccsl_statements_InstanceOf_Statement, gen_ccsl_statements_ReturnStatement_Statement, gen_ccsl_statements_ThisStatement_Statement, gen_ccsl_statements_BreakStatement_Statement, gen_ccsl_statements_ContinueStatement_Statement, gen_ccsl_expressions_OperatorExpression_Statement, gen_ccsl_expressions_ParenthesizedExpression_Statement, gen_ccsl_expressions_StringConcatenation_OperatorExpression, gen_ccsl_expressions_InfixExpression_OperatorExpression, gen_ccsl_expressions_BooleanExpression_OperatorExpression, gen_ccsl_expressions_ArithmeticExpression_OperatorExpression, gen_ccsl_literalValues_LiteralValue_Statement, gen_ccsl_literalValues_NullLiteral_LiteralValue, gen_ccsl_literalValues_CharacterLiteral_LiteralValue, gen_ccsl_literalValues_StringLiteral_LiteralValue, gen_ccsl_literalValues_NumberLiteral_LiteralValue, gen_ccsl_literalValues_BooleanLiteral_LiteralValue, gen_ccsl_controlFlow_SwitchStatement_ControlFlow, gen_ccsl_controlFlow_SwitchCaseBlock_Block, gen_ccsl_controlFlow_IfStatement_ControlFlow, gen_ccsl_controlFlow_LoopStatement_ControlFlow, gen_ccsl_tryCatch_TryStatement_Statement, gen_ccsl_tryCatch_CatchClause_Statement, gen_ccsl_assignment_AbstractAssignment_Statement, gen_ccsl_assignment_Assignment_AbstractAssignment, gen_ccsl_assignment_UnaryAssignment_AbstractAssignment, gen_ccsl_assignment_PrefixUnaryAssignment_UnaryAssignment, gen_ccsl_assignment_PostfixUnaryAssignment_UnaryAssignment, gen_ccsl_invocation_MethodInvocation_SimpleMethodInvocation, gen_ccsl_invocation_ConstructorInvocation_Invocation, gen_ccsl_invocation_SimpleMethodInvocation_Invocation, gen_ccsl_import_ImportableElement_Element, gen_ccsl_import_ImportStatement_Statement, gen_ccsl_annotation_Annotation_Statement, gen_ccsl_annotation_AnnotableElement_Element, gen_ccsl_invocation_SuperMethodInvocation_SimpleMethodInvocation, gen_ccsl_invocation_Invocation_Statement, gen_ccsl_datatype_StringPrimitiveType_PrimitiveType, gen_ccsl_datatype_BooleanPrimitiveType_PrimitiveType, gen_ccsl_datatype_ShortPrimitiveType_PrimitiveType, gen_ccsl_datatype_ObjectType_DataType, gen_ccsl_datatype_ParameterizedType_ObjectType, gen_ccsl_datatype_GenericType_ComplexType, gen_ccsl_datatype_IntPrimitiveType_PrimitiveType, gen_ccsl_datatype_ArrayType_ObjectType, gen_ccsl_datatype_VoidType_PrimitiveType, gen_ccsl_datatype_DataType_Element, gen_ccsl_datatype_PrimitiveType_DataType, gen_ccsl_action_DeleteAction_InjectionAction, gen_ccsl_action_MoveScopeUpAction_InjectionAction, gen_ccsl_action_DeleteInfixOperatorAction_InjectionAction, gen_ccsl_action_ChangeLiteralValueAction_InjectionAction, gen_ccsl_action_DeleteRandomStatementAction_InjectionAction, gen_ccsl_action_ReplaceVariableAccessAction_InjectionAction, gen_ccsl_action_ReplaceArithmeticOperatorAction_InjectionAction, gen_ccsl_strategy_AllStrategy_InjectionStrategy, gen_ccsl_booleanFunctions_CcslBooleanFunction_CcslFunction, gen_ccsl_filters_Filter_CcslBooleanFunction, gen_ccsl_filters_AtomicFilter_Filter, gen_ccsl_filters_CompositeFilter_Filter, gen_ccsl_filters_PropertyFilter_AtomicFilter, gen_ccsl_filters_TemplateFilter_AtomicFilter, gen_ccsl_filters_SameNameFilter_AtomicFilter, gen_ccsl_filters_CountFilter_AtomicFilter, gen_ccsl_filters_RegexMatch_AtomicFilter, gen_ccsl_filters_ImplicityOperandFilter_TemplateFilter, gen_ccsl_filters_ImplicityContainerFilter_AtomicFilter, gen_ccsl_filters_IsKindOfFilter_AtomicFilter, gen_ccsl_filters_SuperMethodClosureFilter_AtomicFilter, gen_ccsl_filters_IsTypeOfFilter_AtomicFilter, gen_ccsl_filters_ChildClosureComplexTypeFilter_AtomicFilter, gen_ccsl_filters_IsStringFilter_AtomicFilter, gen_ccsl_filters_FromClosureFilter_AtomicFilter, gen_ccsl_filters_SuperClassClosureFilter_AtomicFilter, gen_ccsl_filters_BlockLastStatementFilter_AtomicFilter, gen_ccsl_filters_HasSameReferenceFilter_AtomicFilter, gen_ccsl_numberFunctions_CcslNumberFunction_CcslFunction, gen_ccsl_numberFunctions_CcslIntegerLiteral_CcslNumberFunction, gen_ccsl_numberFunctions_GetIndexOf_CcslNumberFunction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)