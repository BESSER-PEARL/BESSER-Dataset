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
BindingExprOpKind: Enumeration = Enumeration(
    name="BindingExprOpKind",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="BOOL")
    }
)

# Classes
odemcustom_Construct = Class(name="odemcustom::Construct")
NamedExtension = Class(name="NamedExtension")
odemcustom_Model = Class(name="odemcustom::Model")
odemcustom_Import = Class(name="odemcustom::Import")
odemcustom_Module = Class(name="odemcustom::Module")
odemcustom_ExtensionDefinition = Class(name="odemcustom::ExtensionDefinition")
odemcustom_Annotation = Class(name="odemcustom::Annotation")
odemcustom_Procedure = Class(name="odemcustom::Procedure")
odemcustom_Variable = Class(name="odemcustom::Variable")
odemcustom_IdResolution = Class(name="odemcustom::IdResolution")
odemcustom_EmbeddableExtensionsContainer = Class(name="odemcustom::EmbeddableExtensionsContainer", is_abstract=True)
NamedElement = Class(name="NamedElement")
EmbeddableExtensionsContainer = Class(name="EmbeddableExtensionsContainer")
odemcustom_Classifier = Class(name="odemcustom::Classifier", is_abstract=True)
odemcustom_ClassAugment = Class(name="odemcustom::ClassAugment")
odemcustom_IdExpr = Class(name="odemcustom::IdExpr")
Type = Class(name="Type")
odemcustom_VoidType = Class(name="odemcustom::VoidType")
PrimitiveType = Class(name="PrimitiveType")
odemcustom_IntType = Class(name="odemcustom::IntType")
odemcustom_BoolType = Class(name="odemcustom::BoolType")
odemcustom_DoubleType = Class(name="odemcustom::DoubleType")
odemcustom_StringType = Class(name="odemcustom::StringType")
TypedElement = Class(name="TypedElement")
CodeBlock = Class(name="CodeBlock")
AnnotatableElement = Class(name="AnnotatableElement")
odemcustom_Extension = Class(name="odemcustom::Extension")
odemcustom_ModifierExtensionsContainer = Class(name="odemcustom::ModifierExtensionsContainer", is_abstract=True)
odemcustom_Type = Class(name="odemcustom::Type", is_abstract=True)
odemcustom_TypedElement = Class(name="odemcustom::TypedElement", is_abstract=True)
odemcustom_PrimitiveType = Class(name="odemcustom::PrimitiveType", is_abstract=True)
odemcustom_AnnotationApplication = Class(name="odemcustom::AnnotationApplication")
odemcustom_KeyValuePair = Class(name="odemcustom::KeyValuePair")
odemcustom_VariableAccess = Class(name="odemcustom::VariableAccess")
odemcustom_Expression = Class(name="odemcustom::Expression")
odemcustom_AnnotatableElement = Class(name="odemcustom::AnnotatableElement", is_abstract=True)
odemcustom_Parameter = Class(name="odemcustom::Parameter")
odemcustom_SimpleAnnotation = Class(name="odemcustom::SimpleAnnotation")
odemcustom_ClassSimilar = Class(name="odemcustom::ClassSimilar", is_abstract=True)
ModifierExtensionsContainer = Class(name="ModifierExtensionsContainer")
odemcustom_Clazz = Class(name="odemcustom::Clazz")
odemcustom_Interface = Class(name="odemcustom::Interface")
odemcustom_StartCodeBlock = Class(name="odemcustom::StartCodeBlock")
ReferableRhsType = Class(name="ReferableRhsType")
odemcustom_NativeBinding = Class(name="odemcustom::NativeBinding")
Classifier = Class(name="Classifier")
ClassSimilar = Class(name="ClassSimilar")
odemcustom_Constructor = Class(name="odemcustom::Constructor")
odemcustom_NamedElement = Class(name="odemcustom::NamedElement")
ExpandableElement = Class(name="ExpandableElement")
odemcustom_CodeBlock = Class(name="odemcustom::CodeBlock")
Construct = Class(name="Construct")
odemcustom_Statement = Class(name="odemcustom::Statement")
odemcustom_AbstractVariable = Class(name="odemcustom::AbstractVariable", is_abstract=True)
AbstractVariable = Class(name="AbstractVariable")
Statement = Class(name="Statement")
odemcustom_ExpressionStatement = Class(name="odemcustom::ExpressionStatement")
SimpleStatement = Class(name="SimpleStatement")
odemcustom_StatementExpression = Class(name="odemcustom::StatementExpression")
odemcustom_Assignment = Class(name="odemcustom::Assignment")
odemcustom_CompositeStatement = Class(name="odemcustom::CompositeStatement")
odemcustom_SimpleStatement = Class(name="odemcustom::SimpleStatement")
ExpressionStatement = Class(name="ExpressionStatement")
odemcustom_ProcedureCall = Class(name="odemcustom::ProcedureCall")
StatementExpression = Class(name="StatementExpression")
odemcustom_DeprecatedProcedureCallStatement = Class(name="odemcustom::DeprecatedProcedureCallStatement")
odemcustom_Terminate = Class(name="odemcustom::Terminate")
odemcustom_Wait = Class(name="odemcustom::Wait")
odemcustom_Reactivate = Class(name="odemcustom::Reactivate")
odemcustom_ActivateObject = Class(name="odemcustom::ActivateObject")
odemcustom_Advance = Class(name="odemcustom::Advance")
odemcustom_Print = Class(name="odemcustom::Print")
odemcustom_SetStatement = Class(name="odemcustom::SetStatement", is_abstract=True)
odemcustom_RemoveFromSet = Class(name="odemcustom::RemoveFromSet")
SetStatement = Class(name="SetStatement")
odemcustom_AddToSet = Class(name="odemcustom::AddToSet")
odemcustom_Return = Class(name="odemcustom::Return")
odemcustom_WaitUntil = Class(name="odemcustom::WaitUntil")
odemcustom_WhileStatement = Class(name="odemcustom::WhileStatement")
odemcustom_BreakStatement = Class(name="odemcustom::BreakStatement")
odemcustom_ContinueStatement = Class(name="odemcustom::ContinueStatement")
odemcustom_ForEachStatement = Class(name="odemcustom::ForEachStatement")
odemcustom_L1Expr = Class(name="odemcustom::L1Expr")
Expression = Class(name="Expression")
odemcustom_BinaryOperator = Class(name="odemcustom::BinaryOperator", is_abstract=True)
odemcustom_UnaryOperator = Class(name="odemcustom::UnaryOperator", is_abstract=True)
odemcustom_EmptySet = Class(name="odemcustom::EmptySet")
odemcustom_IfStatement = Class(name="odemcustom::IfStatement")
CompositeStatement = Class(name="CompositeStatement")
odemcustom_GreaterEqual = Class(name="odemcustom::GreaterEqual")
odemcustom_Less = Class(name="odemcustom::Less")
odemcustom_LessEqual = Class(name="odemcustom::LessEqual")
odemcustom_NotEqual = Class(name="odemcustom::NotEqual")
odemcustom_Equal = Class(name="odemcustom::Equal")
odemcustom_InstanceOf = Class(name="odemcustom::InstanceOf")
odemcustom_Not = Class(name="odemcustom::Not")
odemcustom_CreateObject = Class(name="odemcustom::CreateObject")
odemcustom_Cast = Class(name="odemcustom::Cast")
odemcustom_NullLiteral = Class(name="odemcustom::NullLiteral")
odemcustom_TimeLiteral = Class(name="odemcustom::TimeLiteral")
odemcustom_ActiveLiteral = Class(name="odemcustom::ActiveLiteral")
odemcustom_EvalExpr = Class(name="odemcustom::EvalExpr")
odemcustom_MeLiteral = Class(name="odemcustom::MeLiteral")
PredefinedId = Class(name="PredefinedId")
odemcustom_SuperLiteral = Class(name="odemcustom::SuperLiteral")
odemcustom_MetaLiteral = Class(name="odemcustom::MetaLiteral")
odemcustom_TypeLiteral = Class(name="odemcustom::TypeLiteral")
odemcustom_SetOp = Class(name="odemcustom::SetOp", is_abstract=True)
odemcustom_SizeOfSet = Class(name="odemcustom::SizeOfSet")
SetOp = Class(name="SetOp")
odemcustom_FirstInSet = Class(name="odemcustom::FirstInSet")
odemcustom_LastInSet = Class(name="odemcustom::LastInSet")
odemcustom_Plus = Class(name="odemcustom::Plus")
BinaryOperator = Class(name="BinaryOperator")
odemcustom_Minus = Class(name="odemcustom::Minus")
odemcustom_Mul = Class(name="odemcustom::Mul")
odemcustom_Mod = Class(name="odemcustom::Mod")
odemcustom_Div = Class(name="odemcustom::Div")
odemcustom_Neg = Class(name="odemcustom::Neg")
UnaryOperator = Class(name="UnaryOperator")
odemcustom_And = Class(name="odemcustom::And")
odemcustom_Or = Class(name="odemcustom::Or")
odemcustom_Greater = Class(name="odemcustom::Greater")
odemcustom_DoubleLiteral = Class(name="odemcustom::DoubleLiteral")
odemcustom_DepIdentifiableElement = Class(name="odemcustom::DepIdentifiableElement", is_abstract=True)
odemcustom_PredefinedId = Class(name="odemcustom::PredefinedId")
odemcustom_ArgumentExpression = Class(name="odemcustom::ArgumentExpression")
odemcustom_ElementAccess = Class(name="odemcustom::ElementAccess", is_abstract=True)
ElementAccess = Class(name="ElementAccess")
odemcustom_MetaAccess = Class(name="odemcustom::MetaAccess")
VariableAccess = Class(name="VariableAccess")
odemcustom_TypeAccess = Class(name="odemcustom::TypeAccess")
odemcustom_NamedExtension = Class(name="odemcustom::NamedExtension")
Extension = Class(name="Extension")
odemcustom_ClassContentExtension = Class(name="odemcustom::ClassContentExtension")
odemcustom_Contains = Class(name="odemcustom::Contains")
odemcustom_IndexOf = Class(name="odemcustom::IndexOf")
odemcustom_ObjectAt = Class(name="odemcustom::ObjectAt")
odemcustom_BeforeInSet = Class(name="odemcustom::BeforeInSet")
odemcustom_AfterInSet = Class(name="odemcustom::AfterInSet")
odemcustom_StringLiteral = Class(name="odemcustom::StringLiteral")
odemcustom_IntLiteral = Class(name="odemcustom::IntLiteral")
odemcustom_TrueLiteral = Class(name="odemcustom::TrueLiteral")
odemcustom_FalseLiteral = Class(name="odemcustom::FalseLiteral")
odemcustom_ReferableRhsType = Class(name="odemcustom::ReferableRhsType", is_abstract=True)
odemcustom_RhsExpression = Class(name="odemcustom::RhsExpression", is_abstract=True)
odemcustom_RuleExpr = Class(name="odemcustom::RuleExpr")
odemcustom_SequenceExpr = Class(name="odemcustom::SequenceExpr")
RhsExpression = Class(name="RhsExpression")
odemcustom_OptionalExpr = Class(name="odemcustom::OptionalExpr")
odemcustom_RuntimeExpr = Class(name="odemcustom::RuntimeExpr")
odemcustom_AtLeastOneExpr = Class(name="odemcustom::AtLeastOneExpr")
odemcustom_ArbitraryExpr = Class(name="odemcustom::ArbitraryExpr")
odemcustom_ModuleContentExtension = Class(name="odemcustom::ModuleContentExtension")
odemcustom_TextualSyntaxDef = Class(name="odemcustom::TextualSyntaxDef")
odemcustom_Mapping = Class(name="odemcustom::Mapping")
odemcustom_ExtensionRule = Class(name="odemcustom::ExtensionRule")
odemcustom_TsRule = Class(name="odemcustom::TsRule")
odemcustom_PropertyType = Class(name="odemcustom::PropertyType", is_abstract=True)
odemcustom_IdPropertyType = Class(name="odemcustom::IdPropertyType")
PropertyType = Class(name="PropertyType")
odemcustom_IntPropertyType = Class(name="odemcustom::IntPropertyType")
odemcustom_StringPropertyType = Class(name="odemcustom::StringPropertyType")
odemcustom_BooleanPropertyType = Class(name="odemcustom::BooleanPropertyType")
odemcustom_StructuredPropertyType = Class(name="odemcustom::StructuredPropertyType")
odemcustom_CompositePropertyType = Class(name="odemcustom::CompositePropertyType")
StructuredPropertyType = Class(name="StructuredPropertyType")
odemcustom_ReferencePropertyType = Class(name="odemcustom::ReferencePropertyType")
odemcustom_Pattern = Class(name="odemcustom::Pattern")
odemcustom_MappingPart = Class(name="odemcustom::MappingPart", is_abstract=True)
odemcustom_AlternativeExpr = Class(name="odemcustom::AlternativeExpr")
odemcustom_TerminalExpr = Class(name="odemcustom::TerminalExpr")
odemcustom_PropertyBindingExpr = Class(name="odemcustom::PropertyBindingExpr")
odemcustom_MappingStatement = Class(name="odemcustom::MappingStatement")
odemcustom_SetGenContextStatement = Class(name="odemcustom::SetGenContextStatement")
odemcustom_ResetGenContextStatement = Class(name="odemcustom::ResetGenContextStatement")
odemcustom_SaveGenStatement = Class(name="odemcustom::SaveGenStatement")
odemcustom_ResumeGenStatement = Class(name="odemcustom::ResumeGenStatement")
odemcustom_FixedMappingPart = Class(name="odemcustom::FixedMappingPart")
MappingPart = Class(name="MappingPart")
odemcustom_DynamicMappingPart = Class(name="odemcustom::DynamicMappingPart")
odemcustom_ExpandExpression = Class(name="odemcustom::ExpandExpression")
odemcustom_MetaExpr = Class(name="odemcustom::MetaExpr")
odemcustom_TargetStatement = Class(name="odemcustom::TargetStatement")
odemcustom_CodeQuoteExpression = Class(name="odemcustom::CodeQuoteExpression")
odemcustom_QuotedCode = Class(name="odemcustom::QuotedCode")
odemcustom_QuotedExpression = Class(name="odemcustom::QuotedExpression")
QuotedCode = Class(name="QuotedCode")
odemcustom_QuotedStatements = Class(name="odemcustom::QuotedStatements")
odemcustom_QuotedClassContent = Class(name="odemcustom::QuotedClassContent")
odemcustom_QuotedModuleContent = Class(name="odemcustom::QuotedModuleContent")
Module = Class(name="Module")
odemcustom_ExpandableElement = Class(name="odemcustom::ExpandableElement")
odemcustom_TestStatement = Class(name="odemcustom::TestStatement")
odemcustom_ExpandStatement = Class(name="odemcustom::ExpandStatement")
odemcustom_ExpandSection = Class(name="odemcustom::ExpandSection")
odemcustom_ConsiderIdElements = Class(name="odemcustom::ConsiderIdElements")
odemcustom_IncludePattern = Class(name="odemcustom::IncludePattern")
odemcustom_PotentiallyHiddenIdElements = Class(name="odemcustom::PotentiallyHiddenIdElements")
odemcustom_FindContainer = Class(name="odemcustom::FindContainer")

# odemcustom_Construct class attributes and methods
odemcustom_Construct_concreteSyntax: Property = Property(name="concreteSyntax", type=StringType)
odemcustom_Construct.attributes={odemcustom_Construct_concreteSyntax}

# NamedExtension class attributes and methods

# odemcustom_Model class attributes and methods

# odemcustom_Import class attributes and methods
odemcustom_Import_file: Property = Property(name="file", type=StringType)
odemcustom_Import.attributes={odemcustom_Import_file}

# odemcustom_Module class attributes and methods

# odemcustom_ExtensionDefinition class attributes and methods

# odemcustom_Annotation class attributes and methods

# odemcustom_Procedure class attributes and methods
odemcustom_Procedure_clazz: Property = Property(name="clazz", type=BooleanType)
odemcustom_Procedure.attributes={odemcustom_Procedure_clazz}

# odemcustom_Variable class attributes and methods
odemcustom_Variable_control: Property = Property(name="control", type=BooleanType)
odemcustom_Variable_clazz: Property = Property(name="clazz", type=BooleanType)
odemcustom_Variable.attributes={odemcustom_Variable_clazz, odemcustom_Variable_control}

# odemcustom_IdResolution class attributes and methods
odemcustom_IdResolution_metaModelPlatformURI: Property = Property(name="metaModelPlatformURI", type=StringType)
odemcustom_IdResolution.attributes={odemcustom_IdResolution_metaModelPlatformURI}

# odemcustom_EmbeddableExtensionsContainer class attributes and methods

# NamedElement class attributes and methods

# EmbeddableExtensionsContainer class attributes and methods

# odemcustom_Classifier class attributes and methods

# odemcustom_ClassAugment class attributes and methods

# odemcustom_IdExpr class attributes and methods

# Type class attributes and methods

# odemcustom_VoidType class attributes and methods

# PrimitiveType class attributes and methods

# odemcustom_IntType class attributes and methods

# odemcustom_BoolType class attributes and methods

# odemcustom_DoubleType class attributes and methods

# odemcustom_StringType class attributes and methods

# TypedElement class attributes and methods

# CodeBlock class attributes and methods

# AnnotatableElement class attributes and methods

# odemcustom_Extension class attributes and methods

# odemcustom_ModifierExtensionsContainer class attributes and methods

# odemcustom_Type class attributes and methods

# odemcustom_TypedElement class attributes and methods
odemcustom_TypedElement_isList: Property = Property(name="isList", type=BooleanType)
odemcustom_TypedElement.attributes={odemcustom_TypedElement_isList}

# odemcustom_PrimitiveType class attributes and methods

# odemcustom_AnnotationApplication class attributes and methods

# odemcustom_KeyValuePair class attributes and methods

# odemcustom_VariableAccess class attributes and methods

# odemcustom_Expression class attributes and methods

# odemcustom_AnnotatableElement class attributes and methods

# odemcustom_Parameter class attributes and methods

# odemcustom_SimpleAnnotation class attributes and methods
odemcustom_SimpleAnnotation_value: Property = Property(name="value", type=StringType)
odemcustom_SimpleAnnotation.attributes={odemcustom_SimpleAnnotation_value}

# odemcustom_ClassSimilar class attributes and methods

# ModifierExtensionsContainer class attributes and methods

# odemcustom_Clazz class attributes and methods
odemcustom_Clazz_active: Property = Property(name="active", type=BooleanType)
odemcustom_Clazz.attributes={odemcustom_Clazz_active}

# odemcustom_Interface class attributes and methods

# odemcustom_StartCodeBlock class attributes and methods

# ReferableRhsType class attributes and methods

# odemcustom_NativeBinding class attributes and methods
odemcustom_NativeBinding_targetLanguage: Property = Property(name="targetLanguage", type=StringType)
odemcustom_NativeBinding_targetType: Property = Property(name="targetType", type=StringType)
odemcustom_NativeBinding.attributes={odemcustom_NativeBinding_targetLanguage, odemcustom_NativeBinding_targetType}

# Classifier class attributes and methods

# ClassSimilar class attributes and methods

# odemcustom_Constructor class attributes and methods

# odemcustom_NamedElement class attributes and methods
odemcustom_NamedElement_name: Property = Property(name="name", type=StringType)
odemcustom_NamedElement.attributes={odemcustom_NamedElement_name}

# ExpandableElement class attributes and methods

# odemcustom_CodeBlock class attributes and methods

# Construct class attributes and methods

# odemcustom_Statement class attributes and methods

# odemcustom_AbstractVariable class attributes and methods

# AbstractVariable class attributes and methods

# Statement class attributes and methods

# odemcustom_ExpressionStatement class attributes and methods

# SimpleStatement class attributes and methods

# odemcustom_StatementExpression class attributes and methods

# odemcustom_Assignment class attributes and methods

# odemcustom_CompositeStatement class attributes and methods

# odemcustom_SimpleStatement class attributes and methods

# ExpressionStatement class attributes and methods

# odemcustom_ProcedureCall class attributes and methods

# StatementExpression class attributes and methods

# odemcustom_DeprecatedProcedureCallStatement class attributes and methods

# odemcustom_Terminate class attributes and methods

# odemcustom_Wait class attributes and methods

# odemcustom_Reactivate class attributes and methods

# odemcustom_ActivateObject class attributes and methods
odemcustom_ActivateObject_priority: Property = Property(name="priority", type=IntegerType)
odemcustom_ActivateObject.attributes={odemcustom_ActivateObject_priority}

# odemcustom_Advance class attributes and methods

# odemcustom_Print class attributes and methods

# odemcustom_SetStatement class attributes and methods

# odemcustom_RemoveFromSet class attributes and methods

# SetStatement class attributes and methods

# odemcustom_AddToSet class attributes and methods

# odemcustom_Return class attributes and methods

# odemcustom_WaitUntil class attributes and methods

# odemcustom_WhileStatement class attributes and methods

# odemcustom_BreakStatement class attributes and methods

# odemcustom_ContinueStatement class attributes and methods

# odemcustom_ForEachStatement class attributes and methods

# odemcustom_L1Expr class attributes and methods

# Expression class attributes and methods

# odemcustom_BinaryOperator class attributes and methods

# odemcustom_UnaryOperator class attributes and methods

# odemcustom_EmptySet class attributes and methods

# odemcustom_IfStatement class attributes and methods

# CompositeStatement class attributes and methods

# odemcustom_GreaterEqual class attributes and methods

# odemcustom_Less class attributes and methods

# odemcustom_LessEqual class attributes and methods

# odemcustom_NotEqual class attributes and methods

# odemcustom_Equal class attributes and methods

# odemcustom_InstanceOf class attributes and methods

# odemcustom_Not class attributes and methods

# odemcustom_CreateObject class attributes and methods

# odemcustom_Cast class attributes and methods

# odemcustom_NullLiteral class attributes and methods

# odemcustom_TimeLiteral class attributes and methods

# odemcustom_ActiveLiteral class attributes and methods

# odemcustom_EvalExpr class attributes and methods

# odemcustom_MeLiteral class attributes and methods

# PredefinedId class attributes and methods

# odemcustom_SuperLiteral class attributes and methods

# odemcustom_MetaLiteral class attributes and methods

# odemcustom_TypeLiteral class attributes and methods

# odemcustom_SetOp class attributes and methods

# odemcustom_SizeOfSet class attributes and methods

# SetOp class attributes and methods

# odemcustom_FirstInSet class attributes and methods

# odemcustom_LastInSet class attributes and methods

# odemcustom_Plus class attributes and methods

# BinaryOperator class attributes and methods

# odemcustom_Minus class attributes and methods

# odemcustom_Mul class attributes and methods

# odemcustom_Mod class attributes and methods

# odemcustom_Div class attributes and methods

# odemcustom_Neg class attributes and methods

# UnaryOperator class attributes and methods

# odemcustom_And class attributes and methods

# odemcustom_Or class attributes and methods

# odemcustom_Greater class attributes and methods

# odemcustom_DoubleLiteral class attributes and methods
odemcustom_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
odemcustom_DoubleLiteral.attributes={odemcustom_DoubleLiteral_value}

# odemcustom_DepIdentifiableElement class attributes and methods

# odemcustom_PredefinedId class attributes and methods

# odemcustom_ArgumentExpression class attributes and methods

# odemcustom_ElementAccess class attributes and methods

# ElementAccess class attributes and methods

# odemcustom_MetaAccess class attributes and methods

# VariableAccess class attributes and methods

# odemcustom_TypeAccess class attributes and methods

# odemcustom_NamedExtension class attributes and methods

# Extension class attributes and methods

# odemcustom_ClassContentExtension class attributes and methods

# odemcustom_Contains class attributes and methods

# odemcustom_IndexOf class attributes and methods

# odemcustom_ObjectAt class attributes and methods

# odemcustom_BeforeInSet class attributes and methods

# odemcustom_AfterInSet class attributes and methods

# odemcustom_StringLiteral class attributes and methods
odemcustom_StringLiteral_value: Property = Property(name="value", type=StringType)
odemcustom_StringLiteral.attributes={odemcustom_StringLiteral_value}

# odemcustom_IntLiteral class attributes and methods
odemcustom_IntLiteral_value: Property = Property(name="value", type=IntegerType)
odemcustom_IntLiteral.attributes={odemcustom_IntLiteral_value}

# odemcustom_TrueLiteral class attributes and methods

# odemcustom_FalseLiteral class attributes and methods

# odemcustom_ReferableRhsType class attributes and methods

# odemcustom_RhsExpression class attributes and methods
odemcustom_RhsExpression_m_getSubExpressions: Method = Method(name="getSubExpressions", parameters={}, type=StringType)
odemcustom_RhsExpression.methods={odemcustom_RhsExpression_m_getSubExpressions}

# odemcustom_RuleExpr class attributes and methods

# odemcustom_SequenceExpr class attributes and methods

# RhsExpression class attributes and methods

# odemcustom_OptionalExpr class attributes and methods

# odemcustom_RuntimeExpr class attributes and methods

# odemcustom_AtLeastOneExpr class attributes and methods

# odemcustom_ArbitraryExpr class attributes and methods

# odemcustom_ModuleContentExtension class attributes and methods

# odemcustom_TextualSyntaxDef class attributes and methods

# odemcustom_Mapping class attributes and methods

# odemcustom_ExtensionRule class attributes and methods

# odemcustom_TsRule class attributes and methods
odemcustom_TsRule_metaClassName: Property = Property(name="metaClassName", type=StringType)
odemcustom_TsRule.attributes={odemcustom_TsRule_metaClassName}

# odemcustom_PropertyType class attributes and methods

# odemcustom_IdPropertyType class attributes and methods

# PropertyType class attributes and methods

# odemcustom_IntPropertyType class attributes and methods

# odemcustom_StringPropertyType class attributes and methods

# odemcustom_BooleanPropertyType class attributes and methods
odemcustom_BooleanPropertyType_terminal: Property = Property(name="terminal", type=StringType)
odemcustom_BooleanPropertyType.attributes={odemcustom_BooleanPropertyType_terminal}

# odemcustom_StructuredPropertyType class attributes and methods

# odemcustom_CompositePropertyType class attributes and methods
odemcustom_CompositePropertyType_list: Property = Property(name="list", type=BooleanType)
odemcustom_CompositePropertyType.attributes={odemcustom_CompositePropertyType_list}

# StructuredPropertyType class attributes and methods

# odemcustom_ReferencePropertyType class attributes and methods
odemcustom_ReferencePropertyType_rawReference: Property = Property(name="rawReference", type=BooleanType)
odemcustom_ReferencePropertyType.attributes={odemcustom_ReferencePropertyType_rawReference}

# odemcustom_Pattern class attributes and methods
odemcustom_Pattern_top: Property = Property(name="top", type=BooleanType)
odemcustom_Pattern.attributes={odemcustom_Pattern_top}

# odemcustom_MappingPart class attributes and methods

# odemcustom_AlternativeExpr class attributes and methods

# odemcustom_TerminalExpr class attributes and methods
odemcustom_TerminalExpr_terminal: Property = Property(name="terminal", type=StringType)
odemcustom_TerminalExpr.attributes={odemcustom_TerminalExpr_terminal}

# odemcustom_PropertyBindingExpr class attributes and methods
odemcustom_PropertyBindingExpr_operator: Property = Property(name="operator", type=StringType)
odemcustom_PropertyBindingExpr.attributes={odemcustom_PropertyBindingExpr_operator}

# odemcustom_MappingStatement class attributes and methods

# odemcustom_SetGenContextStatement class attributes and methods
odemcustom_SetGenContextStatement_addAfterContext: Property = Property(name="addAfterContext", type=BooleanType)
odemcustom_SetGenContextStatement.attributes={odemcustom_SetGenContextStatement_addAfterContext}

# odemcustom_ResetGenContextStatement class attributes and methods

# odemcustom_SaveGenStatement class attributes and methods

# odemcustom_ResumeGenStatement class attributes and methods

# odemcustom_FixedMappingPart class attributes and methods
odemcustom_FixedMappingPart_code: Property = Property(name="code", type=StringType)
odemcustom_FixedMappingPart.attributes={odemcustom_FixedMappingPart_code}

# MappingPart class attributes and methods

# odemcustom_DynamicMappingPart class attributes and methods

# odemcustom_ExpandExpression class attributes and methods

# odemcustom_MetaExpr class attributes and methods

# odemcustom_TargetStatement class attributes and methods

# odemcustom_CodeQuoteExpression class attributes and methods

# odemcustom_QuotedCode class attributes and methods

# odemcustom_QuotedExpression class attributes and methods

# QuotedCode class attributes and methods

# odemcustom_QuotedStatements class attributes and methods

# odemcustom_QuotedClassContent class attributes and methods

# odemcustom_QuotedModuleContent class attributes and methods

# Module class attributes and methods

# odemcustom_ExpandableElement class attributes and methods

# odemcustom_TestStatement class attributes and methods
odemcustom_TestStatement_value: Property = Property(name="value", type=StringType)
odemcustom_TestStatement.attributes={odemcustom_TestStatement_value}

# odemcustom_ExpandStatement class attributes and methods

# odemcustom_ExpandSection class attributes and methods

# odemcustom_ConsiderIdElements class attributes and methods

# odemcustom_IncludePattern class attributes and methods

# odemcustom_PotentiallyHiddenIdElements class attributes and methods

# odemcustom_FindContainer class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="odemcustom_Import", type=odemcustom_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Model", type=odemcustom_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules1: BinaryAssociation = BinaryAssociation(
    name="modules1",
    ends={
        Property(name="odemcustom_Module", type=odemcustom_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Model2", type=odemcustom_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classAugments8: BinaryAssociation = BinaryAssociation(
    name="classAugments8",
    ends={
        Property(name="odemcustom_ClassAugment", type=odemcustom_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Module9", type=odemcustom_ClassAugment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefs10: BinaryAssociation = BinaryAssociation(
    name="extensionDefs10",
    ends={
        Property(name="odemcustom_ExtensionDefinition", type=odemcustom_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Module11", type=odemcustom_ExtensionDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationDefs12: BinaryAssociation = BinaryAssociation(
    name="annotationDefs12",
    ends={
        Property(name="odemcustom_Annotation", type=odemcustom_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Module13", type=odemcustom_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures14: BinaryAssociation = BinaryAssociation(
    name="procedures14",
    ends={
        Property(name="odemcustom_Procedure", type=odemcustom_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Module15", type=odemcustom_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables16: BinaryAssociation = BinaryAssociation(
    name="variables16",
    ends={
        Property(name="odemcustom_Variable", type=odemcustom_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Module17", type=odemcustom_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idRes18: BinaryAssociation = BinaryAssociation(
    name="idRes18",
    ends={
        Property(name="odemcustom_IdResolution", type=odemcustom_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Module19", type=odemcustom_IdResolution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model3: BinaryAssociation = BinaryAssociation(
    name="model3",
    ends={
        Property(name="odemcustom_Model5", type=odemcustom_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Import4", type=odemcustom_Model, multiplicity=Multiplicity(0, 1))
    }
)
classifiers6: BinaryAssociation = BinaryAssociation(
    name="classifiers6",
    ends={
        Property(name="odemcustom_Classifier", type=odemcustom_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Module7", type=odemcustom_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierTypeExpr24: BinaryAssociation = BinaryAssociation(
    name="classifierTypeExpr24",
    ends={
        Property(name="odemcustom_IdExpr", type=odemcustom_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_TypedElement25", type=odemcustom_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensions20: BinaryAssociation = BinaryAssociation(
    name="extensions20",
    ends={
        Property(name="odemcustom_Extension", type=odemcustom_EmbeddableExtensionsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_EmbeddableExtensionsContainer", type=odemcustom_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifierExtensions21: BinaryAssociation = BinaryAssociation(
    name="modifierExtensions21",
    ends={
        Property(name="odemcustom_Extension22", type=odemcustom_ModifierExtensionsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ModifierExtensionsContainer", type=odemcustom_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveType23: BinaryAssociation = BinaryAssociation(
    name="primitiveType23",
    ends={
        Property(name="odemcustom_PrimitiveType", type=odemcustom_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_TypedElement", type=odemcustom_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationDef31: BinaryAssociation = BinaryAssociation(
    name="annotationDef31",
    ends={
        Property(name="odemcustom_Annotation32", type=odemcustom_AnnotationApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AnnotationApplication", type=odemcustom_Annotation, multiplicity=Multiplicity(1, 1))
    }
)
keyValuePairs33: BinaryAssociation = BinaryAssociation(
    name="keyValuePairs33",
    ends={
        Property(name="odemcustom_KeyValuePair", type=odemcustom_AnnotationApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AnnotationApplication34", type=odemcustom_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key35: BinaryAssociation = BinaryAssociation(
    name="key35",
    ends={
        Property(name="odemcustom_VariableAccess", type=odemcustom_KeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_KeyValuePair36", type=odemcustom_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="odemcustom_Expression", type=odemcustom_KeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_KeyValuePair38", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotationApplications39: BinaryAssociation = BinaryAssociation(
    name="annotationApplications39",
    ends={
        Property(name="odemcustom_AnnotationApplication40", type=odemcustom_AnnotatableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AnnotatableElement", type=odemcustom_AnnotationApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleAnnotations41: BinaryAssociation = BinaryAssociation(
    name="simpleAnnotations41",
    ends={
        Property(name="odemcustom_SimpleAnnotation", type=odemcustom_AnnotatableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AnnotatableElement42", type=odemcustom_SimpleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters26: BinaryAssociation = BinaryAssociation(
    name="parameters26",
    ends={
        Property(name="odemcustom_Parameter", type=odemcustom_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Procedure27", type=odemcustom_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys28: BinaryAssociation = BinaryAssociation(
    name="keys28",
    ends={
        Property(name="odemcustom_Variable30", type=odemcustom_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Annotation29", type=odemcustom_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes45: BinaryAssociation = BinaryAssociation(
    name="attributes45",
    ends={
        Property(name="odemcustom_Variable46", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar", type=odemcustom_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods47: BinaryAssociation = BinaryAssociation(
    name="methods47",
    ends={
        Property(name="odemcustom_Procedure49", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar48", type=odemcustom_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass50: BinaryAssociation = BinaryAssociation(
    name="superClass50",
    ends={
        Property(name="odemcustom_Clazz", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar51", type=odemcustom_Clazz, multiplicity=Multiplicity(0, 1))
    }
)
implementedInterfaces52: BinaryAssociation = BinaryAssociation(
    name="implementedInterfaces52",
    ends={
        Property(name="odemcustom_Interface", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar53", type=odemcustom_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
initialBlock54: BinaryAssociation = BinaryAssociation(
    name="initialBlock54",
    ends={
        Property(name="odemcustom_StartCodeBlock", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar55", type=odemcustom_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalBlock56: BinaryAssociation = BinaryAssociation(
    name="finalBlock56",
    ends={
        Property(name="odemcustom_StartCodeBlock58", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar57", type=odemcustom_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings43: BinaryAssociation = BinaryAssociation(
    name="bindings43",
    ends={
        Property(name="odemcustom_NativeBinding", type=odemcustom_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Classifier44", type=odemcustom_NativeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructor68: BinaryAssociation = BinaryAssociation(
    name="constructor68",
    ends={
        Property(name="odemcustom_Constructor", type=odemcustom_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Clazz69", type=odemcustom_Constructor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseConstructorArguments70: BinaryAssociation = BinaryAssociation(
    name="baseConstructorArguments70",
    ends={
        Property(name="odemcustom_Expression72", type=odemcustom_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Clazz71", type=odemcustom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters73: BinaryAssociation = BinaryAssociation(
    name="parameters73",
    ends={
        Property(name="odemcustom_Parameter75", type=odemcustom_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Constructor74", type=odemcustom_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
augmentedClass76: BinaryAssociation = BinaryAssociation(
    name="augmentedClass76",
    ends={
        Property(name="odemcustom_Clazz78", type=odemcustom_ClassAugment, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassAugment77", type=odemcustom_Clazz, multiplicity=Multiplicity(1, 1))
    }
)
actionsBlock59: BinaryAssociation = BinaryAssociation(
    name="actionsBlock59",
    ends={
        Property(name="odemcustom_StartCodeBlock61", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar60", type=odemcustom_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reportBlock62: BinaryAssociation = BinaryAssociation(
    name="reportBlock62",
    ends={
        Property(name="odemcustom_StartCodeBlock64", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar63", type=odemcustom_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clearBlock65: BinaryAssociation = BinaryAssociation(
    name="clearBlock65",
    ends={
        Property(name="odemcustom_StartCodeBlock67", type=odemcustom_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ClassSimilar66", type=odemcustom_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue85: BinaryAssociation = BinaryAssociation(
    name="initialValue85",
    ends={
        Property(name="odemcustom_Expression87", type=odemcustom_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Variable86", type=odemcustom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methods79: BinaryAssociation = BinaryAssociation(
    name="methods79",
    ends={
        Property(name="odemcustom_Procedure81", type=odemcustom_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Interface80", type=odemcustom_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces83: BinaryAssociation = BinaryAssociation(
    name="superInterfaces83",
    ends={
        Property(name="odemcustom_Interface84", type=odemcustom_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Interface82", type=odemcustom_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
expression89: BinaryAssociation = BinaryAssociation(
    name="expression89",
    ends={
        Property(name="odemcustom_StatementExpression", type=odemcustom_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExpressionStatement", type=odemcustom_StatementExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable90: BinaryAssociation = BinaryAssociation(
    name="variable90",
    ends={
        Property(name="odemcustom_VariableAccess91", type=odemcustom_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Assignment", type=odemcustom_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements88: BinaryAssociation = BinaryAssociation(
    name="statements88",
    ends={
        Property(name="odemcustom_Statement", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_CodeBlock", type=odemcustom_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedureCall95: BinaryAssociation = BinaryAssociation(
    name="procedureCall95",
    ends={
        Property(name="odemcustom_Expression96", type=odemcustom_DeprecatedProcedureCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_DeprecatedProcedureCallStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
procedureAccess97: BinaryAssociation = BinaryAssociation(
    name="procedureAccess97",
    ends={
        Property(name="odemcustom_Expression98", type=odemcustom_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ProcedureCall", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value92: BinaryAssociation = BinaryAssociation(
    name="value92",
    ends={
        Property(name="odemcustom_Expression94", type=odemcustom_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Assignment93", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition101: BinaryAssociation = BinaryAssociation(
    name="condition101",
    ends={
        Property(name="odemcustom_Expression102", type=odemcustom_WaitUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_WaitUntil", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess103: BinaryAssociation = BinaryAssociation(
    name="objectAccess103",
    ends={
        Property(name="odemcustom_Expression104", type=odemcustom_Reactivate, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Reactivate", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess105: BinaryAssociation = BinaryAssociation(
    name="objectAccess105",
    ends={
        Property(name="odemcustom_Expression106", type=odemcustom_ActivateObject, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ActivateObject", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
time107: BinaryAssociation = BinaryAssociation(
    name="time107",
    ends={
        Property(name="odemcustom_Expression108", type=odemcustom_Advance, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Advance", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputs109: BinaryAssociation = BinaryAssociation(
    name="outputs109",
    ends={
        Property(name="odemcustom_Expression110", type=odemcustom_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Print", type=odemcustom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object111: BinaryAssociation = BinaryAssociation(
    name="object111",
    ends={
        Property(name="odemcustom_Expression112", type=odemcustom_SetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_SetStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
set113: BinaryAssociation = BinaryAssociation(
    name="set113",
    ends={
        Property(name="odemcustom_Expression115", type=odemcustom_SetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_SetStatement114", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
atIndex116: BinaryAssociation = BinaryAssociation(
    name="atIndex116",
    ends={
        Property(name="odemcustom_Expression117", type=odemcustom_AddToSet, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AddToSet", type=odemcustom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value99: BinaryAssociation = BinaryAssociation(
    name="value99",
    ends={
        Property(name="odemcustom_Expression100", type=odemcustom_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Return", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition132: BinaryAssociation = BinaryAssociation(
    name="condition132",
    ends={
        Property(name="odemcustom_Expression133", type=odemcustom_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_WhileStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whileBlock134: BinaryAssociation = BinaryAssociation(
    name="whileBlock134",
    ends={
        Property(name="odemcustom_CodeBlock136", type=odemcustom_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_WhileStatement135", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteratorVariableDefinition137: BinaryAssociation = BinaryAssociation(
    name="iteratorVariableDefinition137",
    ends={
        Property(name="odemcustom_Variable138", type=odemcustom_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ForEachStatement", type=odemcustom_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iteratorVariableReference139: BinaryAssociation = BinaryAssociation(
    name="iteratorVariableReference139",
    ends={
        Property(name="odemcustom_VariableAccess141", type=odemcustom_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ForEachStatement140", type=odemcustom_VariableAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterableExpression142: BinaryAssociation = BinaryAssociation(
    name="iterableExpression142",
    ends={
        Property(name="odemcustom_Expression144", type=odemcustom_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ForEachStatement143", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
forBlock145: BinaryAssociation = BinaryAssociation(
    name="forBlock145",
    ends={
        Property(name="odemcustom_CodeBlock147", type=odemcustom_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ForEachStatement146", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op1148: BinaryAssociation = BinaryAssociation(
    name="op1148",
    ends={
        Property(name="odemcustom_Expression149", type=odemcustom_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_BinaryOperator", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op2150: BinaryAssociation = BinaryAssociation(
    name="op2150",
    ends={
        Property(name="odemcustom_Expression152", type=odemcustom_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_BinaryOperator151", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition118: BinaryAssociation = BinaryAssociation(
    name="condition118",
    ends={
        Property(name="odemcustom_Expression119", type=odemcustom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IfStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifCaseBlock120: BinaryAssociation = BinaryAssociation(
    name="ifCaseBlock120",
    ends={
        Property(name="odemcustom_CodeBlock122", type=odemcustom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IfStatement121", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elifCondition123: BinaryAssociation = BinaryAssociation(
    name="elifCondition123",
    ends={
        Property(name="odemcustom_Expression125", type=odemcustom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IfStatement124", type=odemcustom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elifCaseBlock126: BinaryAssociation = BinaryAssociation(
    name="elifCaseBlock126",
    ends={
        Property(name="odemcustom_CodeBlock128", type=odemcustom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IfStatement127", type=odemcustom_CodeBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseCaseBlock129: BinaryAssociation = BinaryAssociation(
    name="elseCaseBlock129",
    ends={
        Property(name="odemcustom_CodeBlock131", type=odemcustom_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IfStatement130", type=odemcustom_CodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr155: BinaryAssociation = BinaryAssociation(
    name="expr155",
    ends={
        Property(name="odemcustom_Expression156", type=odemcustom_EvalExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_EvalExpr", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
set157: BinaryAssociation = BinaryAssociation(
    name="set157",
    ends={
        Property(name="odemcustom_Expression158", type=odemcustom_SetOp, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_SetOp", type=odemcustom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op153: BinaryAssociation = BinaryAssociation(
    name="op153",
    ends={
        Property(name="odemcustom_Expression154", type=odemcustom_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_UnaryOperator", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentIdExpr160: BinaryAssociation = BinaryAssociation(
    name="parentIdExpr160",
    ends={
        Property(name="odemcustom_IdExpr161", type=odemcustom_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IdExpr159", type=odemcustom_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedElement162: BinaryAssociation = BinaryAssociation(
    name="referencedElement162",
    ends={
        Property(name="odemcustom_NamedElement", type=odemcustom_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IdExpr163", type=odemcustom_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
predefinedId164: BinaryAssociation = BinaryAssociation(
    name="predefinedId164",
    ends={
        Property(name="odemcustom_PredefinedId", type=odemcustom_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IdExpr165", type=odemcustom_PredefinedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments166: BinaryAssociation = BinaryAssociation(
    name="arguments166",
    ends={
        Property(name="odemcustom_ArgumentExpression", type=odemcustom_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IdExpr167", type=odemcustom_ArgumentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments168: BinaryAssociation = BinaryAssociation(
    name="arguments168",
    ends={
        Property(name="odemcustom_Expression170", type=odemcustom_ArgumentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ArgumentExpression169", type=odemcustom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idExpr171: BinaryAssociation = BinaryAssociation(
    name="idExpr171",
    ends={
        Property(name="odemcustom_IdExpr172", type=odemcustom_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ElementAccess", type=odemcustom_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newRules182: BinaryAssociation = BinaryAssociation(
    name="newRules182",
    ends={
        Property(name="odemcustom_TsRule", type=odemcustom_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_TextualSyntaxDef183", type=odemcustom_TsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rhs184: BinaryAssociation = BinaryAssociation(
    name="rhs184",
    ends={
        Property(name="odemcustom_RhsExpression", type=odemcustom_TsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_TsRule185", type=odemcustom_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instantiableMetaClass186: BinaryAssociation = BinaryAssociation(
    name="instantiableMetaClass186",
    ends={
        Property(name="odemcustom_Classifier188", type=odemcustom_ExtensionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExtensionRule187", type=odemcustom_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
firstNewRule189: BinaryAssociation = BinaryAssociation(
    name="firstNewRule189",
    ends={
        Property(name="odemcustom_RuleExpr", type=odemcustom_ExtensionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExtensionRule190", type=odemcustom_RuleExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequence191: BinaryAssociation = BinaryAssociation(
    name="sequence191",
    ends={
        Property(name="odemcustom_RhsExpression192", type=odemcustom_SequenceExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_SequenceExpr", type=odemcustom_RhsExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression193: BinaryAssociation = BinaryAssociation(
    name="expression193",
    ends={
        Property(name="odemcustom_RhsExpression194", type=odemcustom_OptionalExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_OptionalExpr", type=odemcustom_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression195: BinaryAssociation = BinaryAssociation(
    name="expression195",
    ends={
        Property(name="odemcustom_RhsExpression196", type=odemcustom_RuntimeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_RuntimeExpr", type=odemcustom_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression197: BinaryAssociation = BinaryAssociation(
    name="expression197",
    ends={
        Property(name="odemcustom_RhsExpression198", type=odemcustom_AtLeastOneExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AtLeastOneExpr", type=odemcustom_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
abstractSyntaxDef173: BinaryAssociation = BinaryAssociation(
    name="abstractSyntaxDef173",
    ends={
        Property(name="odemcustom_Classifier175", type=odemcustom_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExtensionDefinition174", type=odemcustom_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textualSyntaxDef176: BinaryAssociation = BinaryAssociation(
    name="textualSyntaxDef176",
    ends={
        Property(name="odemcustom_TextualSyntaxDef", type=odemcustom_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExtensionDefinition177", type=odemcustom_TextualSyntaxDef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappingDef178: BinaryAssociation = BinaryAssociation(
    name="mappingDef178",
    ends={
        Property(name="odemcustom_Mapping", type=odemcustom_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExtensionDefinition179", type=odemcustom_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionRule180: BinaryAssociation = BinaryAssociation(
    name="extensionRule180",
    ends={
        Property(name="odemcustom_ExtensionRule", type=odemcustom_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_TextualSyntaxDef181", type=odemcustom_ExtensionRule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
propertyType206: BinaryAssociation = BinaryAssociation(
    name="propertyType206",
    ends={
        Property(name="odemcustom_PropertyType", type=odemcustom_PropertyBindingExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_PropertyBindingExpr", type=odemcustom_PropertyType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule207: BinaryAssociation = BinaryAssociation(
    name="rule207",
    ends={
        Property(name="odemcustom_TsRule209", type=odemcustom_RuleExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_RuleExpr208", type=odemcustom_TsRule, multiplicity=Multiplicity(1, 1))
    }
)
type210: BinaryAssociation = BinaryAssociation(
    name="type210",
    ends={
        Property(name="odemcustom_ReferableRhsType", type=odemcustom_StructuredPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_StructuredPropertyType", type=odemcustom_ReferableRhsType, multiplicity=Multiplicity(1, 1))
    }
)
idResolutionPattern211: BinaryAssociation = BinaryAssociation(
    name="idResolutionPattern211",
    ends={
        Property(name="odemcustom_Pattern", type=odemcustom_ReferencePropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ReferencePropertyType", type=odemcustom_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
parts212: BinaryAssociation = BinaryAssociation(
    name="parts212",
    ends={
        Property(name="odemcustom_MappingPart", type=odemcustom_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Mapping213", type=odemcustom_MappingPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression199: BinaryAssociation = BinaryAssociation(
    name="expression199",
    ends={
        Property(name="odemcustom_RhsExpression200", type=odemcustom_ArbitraryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ArbitraryExpr", type=odemcustom_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left201: BinaryAssociation = BinaryAssociation(
    name="left201",
    ends={
        Property(name="odemcustom_RhsExpression202", type=odemcustom_AlternativeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AlternativeExpr", type=odemcustom_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right203: BinaryAssociation = BinaryAssociation(
    name="right203",
    ends={
        Property(name="odemcustom_RhsExpression205", type=odemcustom_AlternativeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_AlternativeExpr204", type=odemcustom_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parts221: BinaryAssociation = BinaryAssociation(
    name="parts221",
    ends={
        Property(name="odemcustom_MappingPart222", type=odemcustom_MappingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_MappingStatement", type=odemcustom_MappingPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs223: BinaryAssociation = BinaryAssociation(
    name="exprs223",
    ends={
        Property(name="odemcustom_Expression225", type=odemcustom_MappingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_MappingStatement224", type=odemcustom_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context226: BinaryAssociation = BinaryAssociation(
    name="context226",
    ends={
        Property(name="odemcustom_Expression227", type=odemcustom_SetGenContextStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_SetGenContextStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable228: BinaryAssociation = BinaryAssociation(
    name="variable228",
    ends={
        Property(name="odemcustom_Expression229", type=odemcustom_SaveGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_SaveGenStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable230: BinaryAssociation = BinaryAssociation(
    name="variable230",
    ends={
        Property(name="odemcustom_Expression231", type=odemcustom_ResumeGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ResumeGenStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr232: BinaryAssociation = BinaryAssociation(
    name="expr232",
    ends={
        Property(name="odemcustom_Expression233", type=odemcustom_DynamicMappingPart, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_DynamicMappingPart", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject234: BinaryAssociation = BinaryAssociation(
    name="metaObject234",
    ends={
        Property(name="odemcustom_Expression235", type=odemcustom_ExpandExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExpandExpression", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject214: BinaryAssociation = BinaryAssociation(
    name="metaObject214",
    ends={
        Property(name="odemcustom_Expression216", type=odemcustom_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Mapping215", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr217: BinaryAssociation = BinaryAssociation(
    name="expr217",
    ends={
        Property(name="odemcustom_Expression218", type=odemcustom_MetaExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_MetaExpr", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
codeBlock219: BinaryAssociation = BinaryAssociation(
    name="codeBlock219",
    ends={
        Property(name="odemcustom_CodeBlock220", type=odemcustom_TargetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_TargetStatement", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
quotedCode243: BinaryAssociation = BinaryAssociation(
    name="quotedCode243",
    ends={
        Property(name="odemcustom_QuotedCode", type=odemcustom_CodeQuoteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_CodeQuoteExpression", type=odemcustom_QuotedCode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression244: BinaryAssociation = BinaryAssociation(
    name="expression244",
    ends={
        Property(name="odemcustom_Expression245", type=odemcustom_QuotedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_QuotedExpression", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements246: BinaryAssociation = BinaryAssociation(
    name="statements246",
    ends={
        Property(name="odemcustom_Statement247", type=odemcustom_QuotedStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_QuotedStatements", type=odemcustom_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expandExpression248: BinaryAssociation = BinaryAssociation(
    name="expandExpression248",
    ends={
        Property(name="odemcustom_ExpandExpression249", type=odemcustom_ExpandableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExpandableElement", type=odemcustom_ExpandExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
patterns250: BinaryAssociation = BinaryAssociation(
    name="patterns250",
    ends={
        Property(name="odemcustom_Pattern252", type=odemcustom_IdResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IdResolution251", type=odemcustom_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context253: BinaryAssociation = BinaryAssociation(
    name="context253",
    ends={
        Property(name="odemcustom_Parameter255", type=odemcustom_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Pattern254", type=odemcustom_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
codeBlock256: BinaryAssociation = BinaryAssociation(
    name="codeBlock256",
    ends={
        Property(name="odemcustom_CodeBlock258", type=odemcustom_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_Pattern257", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject236: BinaryAssociation = BinaryAssociation(
    name="metaObject236",
    ends={
        Property(name="odemcustom_Expression237", type=odemcustom_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExpandStatement", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location238: BinaryAssociation = BinaryAssociation(
    name="location238",
    ends={
        Property(name="odemcustom_Expression240", type=odemcustom_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExpandStatement239", type=odemcustom_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codeBlock241: BinaryAssociation = BinaryAssociation(
    name="codeBlock241",
    ends={
        Property(name="odemcustom_CodeBlock242", type=odemcustom_ExpandSection, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ExpandSection", type=odemcustom_CodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock266: BinaryAssociation = BinaryAssociation(
    name="elseBlock266",
    ends={
        Property(name="odemcustom_CodeBlock268", type=odemcustom_FindContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_FindContainer267", type=odemcustom_CodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementsQuery269: BinaryAssociation = BinaryAssociation(
    name="elementsQuery269",
    ends={
        Property(name="odemcustom_Expression270", type=odemcustom_ConsiderIdElements, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_ConsiderIdElements", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern271: BinaryAssociation = BinaryAssociation(
    name="pattern271",
    ends={
        Property(name="odemcustom_Pattern272", type=odemcustom_IncludePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IncludePattern", type=odemcustom_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
context273: BinaryAssociation = BinaryAssociation(
    name="context273",
    ends={
        Property(name="odemcustom_Expression275", type=odemcustom_IncludePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_IncludePattern274", type=odemcustom_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
codeBlock259: BinaryAssociation = BinaryAssociation(
    name="codeBlock259",
    ends={
        Property(name="odemcustom_CodeBlock260", type=odemcustom_PotentiallyHiddenIdElements, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_PotentiallyHiddenIdElements", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableBinding261: BinaryAssociation = BinaryAssociation(
    name="variableBinding261",
    ends={
        Property(name="odemcustom_Parameter262", type=odemcustom_FindContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_FindContainer", type=odemcustom_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerBlock263: BinaryAssociation = BinaryAssociation(
    name="containerBlock263",
    ends={
        Property(name="odemcustom_CodeBlock265", type=odemcustom_FindContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="odemcustom_FindContainer264", type=odemcustom_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_odemcustom_Construct_NamedExtension = Generalization(general=NamedExtension, specific=odemcustom_Construct)
gen_odemcustom_Module_NamedElement = Generalization(general=NamedElement, specific=odemcustom_Module)
gen_odemcustom_Module_EmbeddableExtensionsContainer = Generalization(general=EmbeddableExtensionsContainer, specific=odemcustom_Module)
gen_odemcustom_PrimitiveType_Type = Generalization(general=Type, specific=odemcustom_PrimitiveType)
gen_odemcustom_VoidType_PrimitiveType = Generalization(general=PrimitiveType, specific=odemcustom_VoidType)
gen_odemcustom_IntType_PrimitiveType = Generalization(general=PrimitiveType, specific=odemcustom_IntType)
gen_odemcustom_BoolType_PrimitiveType = Generalization(general=PrimitiveType, specific=odemcustom_BoolType)
gen_odemcustom_DoubleType_PrimitiveType = Generalization(general=PrimitiveType, specific=odemcustom_DoubleType)
gen_odemcustom_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=odemcustom_StringType)
gen_odemcustom_Procedure_NamedElement = Generalization(general=NamedElement, specific=odemcustom_Procedure)
gen_odemcustom_Procedure_TypedElement = Generalization(general=TypedElement, specific=odemcustom_Procedure)
gen_odemcustom_Procedure_CodeBlock = Generalization(general=CodeBlock, specific=odemcustom_Procedure)
gen_odemcustom_Procedure_AnnotatableElement = Generalization(general=AnnotatableElement, specific=odemcustom_Procedure)
gen_odemcustom_SimpleAnnotation_NamedElement = Generalization(general=NamedElement, specific=odemcustom_SimpleAnnotation)
gen_odemcustom_Annotation_NamedElement = Generalization(general=NamedElement, specific=odemcustom_Annotation)
gen_odemcustom_ClassSimilar_EmbeddableExtensionsContainer = Generalization(general=EmbeddableExtensionsContainer, specific=odemcustom_ClassSimilar)
gen_odemcustom_ClassSimilar_ModifierExtensionsContainer = Generalization(general=ModifierExtensionsContainer, specific=odemcustom_ClassSimilar)
gen_odemcustom_Classifier_Type = Generalization(general=Type, specific=odemcustom_Classifier)
gen_odemcustom_Classifier_NamedElement = Generalization(general=NamedElement, specific=odemcustom_Classifier)
gen_odemcustom_Classifier_ReferableRhsType = Generalization(general=ReferableRhsType, specific=odemcustom_Classifier)
gen_odemcustom_Clazz_Classifier = Generalization(general=Classifier, specific=odemcustom_Clazz)
gen_odemcustom_Clazz_ClassSimilar = Generalization(general=ClassSimilar, specific=odemcustom_Clazz)
gen_odemcustom_ClassAugment_ClassSimilar = Generalization(general=ClassSimilar, specific=odemcustom_ClassAugment)
gen_odemcustom_Interface_Classifier = Generalization(general=Classifier, specific=odemcustom_Interface)
gen_odemcustom_StartCodeBlock_CodeBlock = Generalization(general=CodeBlock, specific=odemcustom_StartCodeBlock)
gen_odemcustom_Parameter_AbstractVariable = Generalization(general=AbstractVariable, specific=odemcustom_Parameter)
gen_odemcustom_NamedElement_ExpandableElement = Generalization(general=ExpandableElement, specific=odemcustom_NamedElement)
gen_odemcustom_CodeBlock_Construct = Generalization(general=Construct, specific=odemcustom_CodeBlock)
gen_odemcustom_AbstractVariable_NamedElement = Generalization(general=NamedElement, specific=odemcustom_AbstractVariable)
gen_odemcustom_AbstractVariable_TypedElement = Generalization(general=TypedElement, specific=odemcustom_AbstractVariable)
gen_odemcustom_Variable_AbstractVariable = Generalization(general=AbstractVariable, specific=odemcustom_Variable)
gen_odemcustom_Variable_Statement = Generalization(general=Statement, specific=odemcustom_Variable)
gen_odemcustom_Variable_ModifierExtensionsContainer = Generalization(general=ModifierExtensionsContainer, specific=odemcustom_Variable)
gen_odemcustom_SimpleStatement_Statement = Generalization(general=Statement, specific=odemcustom_SimpleStatement)
gen_odemcustom_ExpressionStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_ExpressionStatement)
gen_odemcustom_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_Assignment)
gen_odemcustom_Statement_Construct = Generalization(general=Construct, specific=odemcustom_Statement)
gen_odemcustom_CompositeStatement_Statement = Generalization(general=Statement, specific=odemcustom_CompositeStatement)
gen_odemcustom_DeprecatedProcedureCallStatement_ExpressionStatement = Generalization(general=ExpressionStatement, specific=odemcustom_DeprecatedProcedureCallStatement)
gen_odemcustom_ProcedureCall_StatementExpression = Generalization(general=StatementExpression, specific=odemcustom_ProcedureCall)
gen_odemcustom_Terminate_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_Terminate)
gen_odemcustom_Wait_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_Wait)
gen_odemcustom_Reactivate_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_Reactivate)
gen_odemcustom_ActivateObject_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_ActivateObject)
gen_odemcustom_Advance_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_Advance)
gen_odemcustom_Print_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_Print)
gen_odemcustom_SetStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_SetStatement)
gen_odemcustom_RemoveFromSet_SetStatement = Generalization(general=SetStatement, specific=odemcustom_RemoveFromSet)
gen_odemcustom_AddToSet_SetStatement = Generalization(general=SetStatement, specific=odemcustom_AddToSet)
gen_odemcustom_Return_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_Return)
gen_odemcustom_WaitUntil_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_WaitUntil)
gen_odemcustom_WhileStatement_CompositeStatement = Generalization(general=CompositeStatement, specific=odemcustom_WhileStatement)
gen_odemcustom_BreakStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_BreakStatement)
gen_odemcustom_ContinueStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_ContinueStatement)
gen_odemcustom_ForEachStatement_CompositeStatement = Generalization(general=CompositeStatement, specific=odemcustom_ForEachStatement)
gen_odemcustom_Expression_Construct = Generalization(general=Construct, specific=odemcustom_Expression)
gen_odemcustom_L1Expr_Expression = Generalization(general=Expression, specific=odemcustom_L1Expr)
gen_odemcustom_BinaryOperator_Expression = Generalization(general=Expression, specific=odemcustom_BinaryOperator)
gen_odemcustom_UnaryOperator_Expression = Generalization(general=Expression, specific=odemcustom_UnaryOperator)
gen_odemcustom_EmptySet_SetStatement = Generalization(general=SetStatement, specific=odemcustom_EmptySet)
gen_odemcustom_IfStatement_CompositeStatement = Generalization(general=CompositeStatement, specific=odemcustom_IfStatement)
gen_odemcustom_GreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_GreaterEqual)
gen_odemcustom_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Less)
gen_odemcustom_LessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_LessEqual)
gen_odemcustom_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_NotEqual)
gen_odemcustom_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Equal)
gen_odemcustom_InstanceOf_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_InstanceOf)
gen_odemcustom_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=odemcustom_Not)
gen_odemcustom_CreateObject_Expression = Generalization(general=Expression, specific=odemcustom_CreateObject)
gen_odemcustom_CreateObject_TypedElement = Generalization(general=TypedElement, specific=odemcustom_CreateObject)
gen_odemcustom_Cast_UnaryOperator = Generalization(general=UnaryOperator, specific=odemcustom_Cast)
gen_odemcustom_Cast_TypedElement = Generalization(general=TypedElement, specific=odemcustom_Cast)
gen_odemcustom_NullLiteral_Expression = Generalization(general=Expression, specific=odemcustom_NullLiteral)
gen_odemcustom_TimeLiteral_Expression = Generalization(general=Expression, specific=odemcustom_TimeLiteral)
gen_odemcustom_ActiveLiteral_Expression = Generalization(general=Expression, specific=odemcustom_ActiveLiteral)
gen_odemcustom_EvalExpr_Expression = Generalization(general=Expression, specific=odemcustom_EvalExpr)
gen_odemcustom_MeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=odemcustom_MeLiteral)
gen_odemcustom_SuperLiteral_PredefinedId = Generalization(general=PredefinedId, specific=odemcustom_SuperLiteral)
gen_odemcustom_MetaLiteral_PredefinedId = Generalization(general=PredefinedId, specific=odemcustom_MetaLiteral)
gen_odemcustom_TypeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=odemcustom_TypeLiteral)
gen_odemcustom_SetOp_PredefinedId = Generalization(general=PredefinedId, specific=odemcustom_SetOp)
gen_odemcustom_SizeOfSet_SetOp = Generalization(general=SetOp, specific=odemcustom_SizeOfSet)
gen_odemcustom_FirstInSet_SetOp = Generalization(general=SetOp, specific=odemcustom_FirstInSet)
gen_odemcustom_Plus_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Plus)
gen_odemcustom_Minus_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Minus)
gen_odemcustom_Mul_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Mul)
gen_odemcustom_Mod_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Mod)
gen_odemcustom_Div_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Div)
gen_odemcustom_Neg_UnaryOperator = Generalization(general=UnaryOperator, specific=odemcustom_Neg)
gen_odemcustom_And_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_And)
gen_odemcustom_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Or)
gen_odemcustom_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=odemcustom_Greater)
gen_odemcustom_FalseLiteral_Expression = Generalization(general=Expression, specific=odemcustom_FalseLiteral)
gen_odemcustom_DoubleLiteral_Expression = Generalization(general=Expression, specific=odemcustom_DoubleLiteral)
gen_odemcustom_IdExpr_Expression = Generalization(general=Expression, specific=odemcustom_IdExpr)
gen_odemcustom_ElementAccess_Expression = Generalization(general=Expression, specific=odemcustom_ElementAccess)
gen_odemcustom_VariableAccess_ElementAccess = Generalization(general=ElementAccess, specific=odemcustom_VariableAccess)
gen_odemcustom_VariableAccess_ExpandableElement = Generalization(general=ExpandableElement, specific=odemcustom_VariableAccess)
gen_odemcustom_MetaAccess_VariableAccess = Generalization(general=VariableAccess, specific=odemcustom_MetaAccess)
gen_odemcustom_TypeAccess_ElementAccess = Generalization(general=ElementAccess, specific=odemcustom_TypeAccess)
gen_odemcustom_TypeAccess_ExpandableElement = Generalization(general=ExpandableElement, specific=odemcustom_TypeAccess)
gen_odemcustom_NamedExtension_Extension = Generalization(general=Extension, specific=odemcustom_NamedExtension)
gen_odemcustom_NamedExtension_NamedElement = Generalization(general=NamedElement, specific=odemcustom_NamedExtension)
gen_odemcustom_ClassContentExtension_NamedExtension = Generalization(general=NamedExtension, specific=odemcustom_ClassContentExtension)
gen_odemcustom_LastInSet_SetOp = Generalization(general=SetOp, specific=odemcustom_LastInSet)
gen_odemcustom_Contains_SetOp = Generalization(general=SetOp, specific=odemcustom_Contains)
gen_odemcustom_IndexOf_SetOp = Generalization(general=SetOp, specific=odemcustom_IndexOf)
gen_odemcustom_ObjectAt_SetOp = Generalization(general=SetOp, specific=odemcustom_ObjectAt)
gen_odemcustom_BeforeInSet_SetOp = Generalization(general=SetOp, specific=odemcustom_BeforeInSet)
gen_odemcustom_AfterInSet_SetOp = Generalization(general=SetOp, specific=odemcustom_AfterInSet)
gen_odemcustom_StringLiteral_Expression = Generalization(general=Expression, specific=odemcustom_StringLiteral)
gen_odemcustom_IntLiteral_Expression = Generalization(general=Expression, specific=odemcustom_IntLiteral)
gen_odemcustom_TrueLiteral_Expression = Generalization(general=Expression, specific=odemcustom_TrueLiteral)
gen_odemcustom_ReferableRhsType_NamedElement = Generalization(general=NamedElement, specific=odemcustom_ReferableRhsType)
gen_odemcustom_TsRule_NamedElement = Generalization(general=NamedElement, specific=odemcustom_TsRule)
gen_odemcustom_TsRule_ReferableRhsType = Generalization(general=ReferableRhsType, specific=odemcustom_TsRule)
gen_odemcustom_ExtensionRule_NamedElement = Generalization(general=NamedElement, specific=odemcustom_ExtensionRule)
gen_odemcustom_SequenceExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_SequenceExpr)
gen_odemcustom_OptionalExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_OptionalExpr)
gen_odemcustom_RuntimeExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_RuntimeExpr)
gen_odemcustom_AtLeastOneExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_AtLeastOneExpr)
gen_odemcustom_ArbitraryExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_ArbitraryExpr)
gen_odemcustom_ModuleContentExtension_NamedExtension = Generalization(general=NamedExtension, specific=odemcustom_ModuleContentExtension)
gen_odemcustom_ExtensionDefinition_NamedElement = Generalization(general=NamedElement, specific=odemcustom_ExtensionDefinition)
gen_odemcustom_RuleExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_RuleExpr)
gen_odemcustom_IdPropertyType_PropertyType = Generalization(general=PropertyType, specific=odemcustom_IdPropertyType)
gen_odemcustom_IntPropertyType_PropertyType = Generalization(general=PropertyType, specific=odemcustom_IntPropertyType)
gen_odemcustom_StringPropertyType_PropertyType = Generalization(general=PropertyType, specific=odemcustom_StringPropertyType)
gen_odemcustom_BooleanPropertyType_PropertyType = Generalization(general=PropertyType, specific=odemcustom_BooleanPropertyType)
gen_odemcustom_StructuredPropertyType_PropertyType = Generalization(general=PropertyType, specific=odemcustom_StructuredPropertyType)
gen_odemcustom_CompositePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=odemcustom_CompositePropertyType)
gen_odemcustom_ReferencePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=odemcustom_ReferencePropertyType)
gen_odemcustom_Mapping_CodeBlock = Generalization(general=CodeBlock, specific=odemcustom_Mapping)
gen_odemcustom_AlternativeExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_AlternativeExpr)
gen_odemcustom_TerminalExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_TerminalExpr)
gen_odemcustom_PropertyBindingExpr_NamedElement = Generalization(general=NamedElement, specific=odemcustom_PropertyBindingExpr)
gen_odemcustom_PropertyBindingExpr_RhsExpression = Generalization(general=RhsExpression, specific=odemcustom_PropertyBindingExpr)
gen_odemcustom_MappingStatement_Statement = Generalization(general=Statement, specific=odemcustom_MappingStatement)
gen_odemcustom_SetGenContextStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_SetGenContextStatement)
gen_odemcustom_ResetGenContextStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_ResetGenContextStatement)
gen_odemcustom_SaveGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_SaveGenStatement)
gen_odemcustom_ResumeGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=odemcustom_ResumeGenStatement)
gen_odemcustom_FixedMappingPart_MappingPart = Generalization(general=MappingPart, specific=odemcustom_FixedMappingPart)
gen_odemcustom_DynamicMappingPart_MappingPart = Generalization(general=MappingPart, specific=odemcustom_DynamicMappingPart)
gen_odemcustom_ExpandExpression_StatementExpression = Generalization(general=StatementExpression, specific=odemcustom_ExpandExpression)
gen_odemcustom_ExpandExpression_Expression = Generalization(general=Expression, specific=odemcustom_ExpandExpression)
gen_odemcustom_MetaExpr_Expression = Generalization(general=Expression, specific=odemcustom_MetaExpr)
gen_odemcustom_TargetStatement_Statement = Generalization(general=Statement, specific=odemcustom_TargetStatement)
gen_odemcustom_CodeQuoteExpression_Expression = Generalization(general=Expression, specific=odemcustom_CodeQuoteExpression)
gen_odemcustom_QuotedExpression_QuotedCode = Generalization(general=QuotedCode, specific=odemcustom_QuotedExpression)
gen_odemcustom_QuotedStatements_QuotedCode = Generalization(general=QuotedCode, specific=odemcustom_QuotedStatements)
gen_odemcustom_QuotedClassContent_QuotedCode = Generalization(general=QuotedCode, specific=odemcustom_QuotedClassContent)
gen_odemcustom_QuotedClassContent_ClassSimilar = Generalization(general=ClassSimilar, specific=odemcustom_QuotedClassContent)
gen_odemcustom_QuotedModuleContent_QuotedCode = Generalization(general=QuotedCode, specific=odemcustom_QuotedModuleContent)
gen_odemcustom_QuotedModuleContent_Module = Generalization(general=Module, specific=odemcustom_QuotedModuleContent)
gen_odemcustom_TestStatement_Statement = Generalization(general=Statement, specific=odemcustom_TestStatement)
gen_odemcustom_Pattern_NamedElement = Generalization(general=NamedElement, specific=odemcustom_Pattern)
gen_odemcustom_ExpandStatement_Statement = Generalization(general=Statement, specific=odemcustom_ExpandStatement)
gen_odemcustom_ExpandSection_CompositeStatement = Generalization(general=CompositeStatement, specific=odemcustom_ExpandSection)
gen_odemcustom_ConsiderIdElements_Statement = Generalization(general=Statement, specific=odemcustom_ConsiderIdElements)
gen_odemcustom_IncludePattern_Statement = Generalization(general=Statement, specific=odemcustom_IncludePattern)
gen_odemcustom_PotentiallyHiddenIdElements_Statement = Generalization(general=Statement, specific=odemcustom_PotentiallyHiddenIdElements)
gen_odemcustom_FindContainer_Statement = Generalization(general=Statement, specific=odemcustom_FindContainer)

# Domain Model
domain_model = DomainModel(
    name="odemcustom",
    types={odemcustom_Construct, NamedExtension, odemcustom_Model, odemcustom_Import, odemcustom_Module, odemcustom_ExtensionDefinition, odemcustom_Annotation, odemcustom_Procedure, odemcustom_Variable, odemcustom_IdResolution, odemcustom_EmbeddableExtensionsContainer, NamedElement, EmbeddableExtensionsContainer, odemcustom_Classifier, odemcustom_ClassAugment, odemcustom_IdExpr, Type, odemcustom_VoidType, PrimitiveType, odemcustom_IntType, odemcustom_BoolType, odemcustom_DoubleType, odemcustom_StringType, TypedElement, CodeBlock, AnnotatableElement, odemcustom_Extension, odemcustom_ModifierExtensionsContainer, odemcustom_Type, odemcustom_TypedElement, odemcustom_PrimitiveType, odemcustom_AnnotationApplication, odemcustom_KeyValuePair, odemcustom_VariableAccess, odemcustom_Expression, odemcustom_AnnotatableElement, odemcustom_Parameter, odemcustom_SimpleAnnotation, odemcustom_ClassSimilar, ModifierExtensionsContainer, odemcustom_Clazz, odemcustom_Interface, odemcustom_StartCodeBlock, ReferableRhsType, odemcustom_NativeBinding, Classifier, ClassSimilar, odemcustom_Constructor, odemcustom_NamedElement, ExpandableElement, odemcustom_CodeBlock, Construct, odemcustom_Statement, odemcustom_AbstractVariable, AbstractVariable, Statement, odemcustom_ExpressionStatement, SimpleStatement, odemcustom_StatementExpression, odemcustom_Assignment, odemcustom_CompositeStatement, odemcustom_SimpleStatement, ExpressionStatement, odemcustom_ProcedureCall, StatementExpression, odemcustom_DeprecatedProcedureCallStatement, odemcustom_Terminate, odemcustom_Wait, odemcustom_Reactivate, odemcustom_ActivateObject, odemcustom_Advance, odemcustom_Print, odemcustom_SetStatement, odemcustom_RemoveFromSet, SetStatement, odemcustom_AddToSet, odemcustom_Return, odemcustom_WaitUntil, odemcustom_WhileStatement, odemcustom_BreakStatement, odemcustom_ContinueStatement, odemcustom_ForEachStatement, odemcustom_L1Expr, Expression, odemcustom_BinaryOperator, odemcustom_UnaryOperator, odemcustom_EmptySet, odemcustom_IfStatement, CompositeStatement, odemcustom_GreaterEqual, odemcustom_Less, odemcustom_LessEqual, odemcustom_NotEqual, odemcustom_Equal, odemcustom_InstanceOf, odemcustom_Not, odemcustom_CreateObject, odemcustom_Cast, odemcustom_NullLiteral, odemcustom_TimeLiteral, odemcustom_ActiveLiteral, odemcustom_EvalExpr, odemcustom_MeLiteral, PredefinedId, odemcustom_SuperLiteral, odemcustom_MetaLiteral, odemcustom_TypeLiteral, odemcustom_SetOp, odemcustom_SizeOfSet, SetOp, odemcustom_FirstInSet, odemcustom_LastInSet, odemcustom_Plus, BinaryOperator, odemcustom_Minus, odemcustom_Mul, odemcustom_Mod, odemcustom_Div, odemcustom_Neg, UnaryOperator, odemcustom_And, odemcustom_Or, odemcustom_Greater, odemcustom_DoubleLiteral, odemcustom_DepIdentifiableElement, odemcustom_PredefinedId, odemcustom_ArgumentExpression, odemcustom_ElementAccess, ElementAccess, odemcustom_MetaAccess, VariableAccess, odemcustom_TypeAccess, odemcustom_NamedExtension, Extension, odemcustom_ClassContentExtension, odemcustom_Contains, odemcustom_IndexOf, odemcustom_ObjectAt, odemcustom_BeforeInSet, odemcustom_AfterInSet, odemcustom_StringLiteral, odemcustom_IntLiteral, odemcustom_TrueLiteral, odemcustom_FalseLiteral, odemcustom_ReferableRhsType, odemcustom_RhsExpression, odemcustom_RuleExpr, odemcustom_SequenceExpr, RhsExpression, odemcustom_OptionalExpr, odemcustom_RuntimeExpr, odemcustom_AtLeastOneExpr, odemcustom_ArbitraryExpr, odemcustom_ModuleContentExtension, odemcustom_TextualSyntaxDef, odemcustom_Mapping, odemcustom_ExtensionRule, odemcustom_TsRule, odemcustom_PropertyType, odemcustom_IdPropertyType, PropertyType, odemcustom_IntPropertyType, odemcustom_StringPropertyType, odemcustom_BooleanPropertyType, odemcustom_StructuredPropertyType, odemcustom_CompositePropertyType, StructuredPropertyType, odemcustom_ReferencePropertyType, odemcustom_Pattern, odemcustom_MappingPart, odemcustom_AlternativeExpr, odemcustom_TerminalExpr, odemcustom_PropertyBindingExpr, odemcustom_MappingStatement, odemcustom_SetGenContextStatement, odemcustom_ResetGenContextStatement, odemcustom_SaveGenStatement, odemcustom_ResumeGenStatement, odemcustom_FixedMappingPart, MappingPart, odemcustom_DynamicMappingPart, odemcustom_ExpandExpression, odemcustom_MetaExpr, odemcustom_TargetStatement, odemcustom_CodeQuoteExpression, odemcustom_QuotedCode, odemcustom_QuotedExpression, QuotedCode, odemcustom_QuotedStatements, odemcustom_QuotedClassContent, odemcustom_QuotedModuleContent, Module, odemcustom_ExpandableElement, odemcustom_TestStatement, odemcustom_ExpandStatement, odemcustom_ExpandSection, odemcustom_ConsiderIdElements, odemcustom_IncludePattern, odemcustom_PotentiallyHiddenIdElements, odemcustom_FindContainer, BindingExprOpKind},
    associations={imports0, modules1, classAugments8, extensionDefs10, annotationDefs12, procedures14, variables16, idRes18, model3, classifiers6, classifierTypeExpr24, extensions20, modifierExtensions21, primitiveType23, annotationDef31, keyValuePairs33, key35, value37, annotationApplications39, simpleAnnotations41, parameters26, keys28, attributes45, methods47, superClass50, implementedInterfaces52, initialBlock54, finalBlock56, bindings43, constructor68, baseConstructorArguments70, parameters73, augmentedClass76, actionsBlock59, reportBlock62, clearBlock65, initialValue85, methods79, superInterfaces83, expression89, variable90, statements88, procedureCall95, procedureAccess97, value92, condition101, objectAccess103, objectAccess105, time107, outputs109, object111, set113, atIndex116, value99, condition132, whileBlock134, iteratorVariableDefinition137, iteratorVariableReference139, iterableExpression142, forBlock145, op1148, op2150, condition118, ifCaseBlock120, elifCondition123, elifCaseBlock126, elseCaseBlock129, expr155, set157, op153, parentIdExpr160, referencedElement162, predefinedId164, arguments166, arguments168, idExpr171, newRules182, rhs184, instantiableMetaClass186, firstNewRule189, sequence191, expression193, expression195, expression197, abstractSyntaxDef173, textualSyntaxDef176, mappingDef178, extensionRule180, propertyType206, rule207, type210, idResolutionPattern211, parts212, expression199, left201, right203, parts221, exprs223, context226, variable228, variable230, expr232, metaObject234, metaObject214, expr217, codeBlock219, quotedCode243, expression244, statements246, expandExpression248, patterns250, context253, codeBlock256, metaObject236, location238, codeBlock241, elseBlock266, elementsQuery269, pattern271, context273, codeBlock259, variableBinding261, containerBlock263},
    generalizations={gen_odemcustom_Construct_NamedExtension, gen_odemcustom_Module_NamedElement, gen_odemcustom_Module_EmbeddableExtensionsContainer, gen_odemcustom_PrimitiveType_Type, gen_odemcustom_VoidType_PrimitiveType, gen_odemcustom_IntType_PrimitiveType, gen_odemcustom_BoolType_PrimitiveType, gen_odemcustom_DoubleType_PrimitiveType, gen_odemcustom_StringType_PrimitiveType, gen_odemcustom_Procedure_NamedElement, gen_odemcustom_Procedure_TypedElement, gen_odemcustom_Procedure_CodeBlock, gen_odemcustom_Procedure_AnnotatableElement, gen_odemcustom_SimpleAnnotation_NamedElement, gen_odemcustom_Annotation_NamedElement, gen_odemcustom_ClassSimilar_EmbeddableExtensionsContainer, gen_odemcustom_ClassSimilar_ModifierExtensionsContainer, gen_odemcustom_Classifier_Type, gen_odemcustom_Classifier_NamedElement, gen_odemcustom_Classifier_ReferableRhsType, gen_odemcustom_Clazz_Classifier, gen_odemcustom_Clazz_ClassSimilar, gen_odemcustom_ClassAugment_ClassSimilar, gen_odemcustom_Interface_Classifier, gen_odemcustom_StartCodeBlock_CodeBlock, gen_odemcustom_Parameter_AbstractVariable, gen_odemcustom_NamedElement_ExpandableElement, gen_odemcustom_CodeBlock_Construct, gen_odemcustom_AbstractVariable_NamedElement, gen_odemcustom_AbstractVariable_TypedElement, gen_odemcustom_Variable_AbstractVariable, gen_odemcustom_Variable_Statement, gen_odemcustom_Variable_ModifierExtensionsContainer, gen_odemcustom_SimpleStatement_Statement, gen_odemcustom_ExpressionStatement_SimpleStatement, gen_odemcustom_Assignment_SimpleStatement, gen_odemcustom_Statement_Construct, gen_odemcustom_CompositeStatement_Statement, gen_odemcustom_DeprecatedProcedureCallStatement_ExpressionStatement, gen_odemcustom_ProcedureCall_StatementExpression, gen_odemcustom_Terminate_SimpleStatement, gen_odemcustom_Wait_SimpleStatement, gen_odemcustom_Reactivate_SimpleStatement, gen_odemcustom_ActivateObject_SimpleStatement, gen_odemcustom_Advance_SimpleStatement, gen_odemcustom_Print_SimpleStatement, gen_odemcustom_SetStatement_SimpleStatement, gen_odemcustom_RemoveFromSet_SetStatement, gen_odemcustom_AddToSet_SetStatement, gen_odemcustom_Return_SimpleStatement, gen_odemcustom_WaitUntil_SimpleStatement, gen_odemcustom_WhileStatement_CompositeStatement, gen_odemcustom_BreakStatement_SimpleStatement, gen_odemcustom_ContinueStatement_SimpleStatement, gen_odemcustom_ForEachStatement_CompositeStatement, gen_odemcustom_Expression_Construct, gen_odemcustom_L1Expr_Expression, gen_odemcustom_BinaryOperator_Expression, gen_odemcustom_UnaryOperator_Expression, gen_odemcustom_EmptySet_SetStatement, gen_odemcustom_IfStatement_CompositeStatement, gen_odemcustom_GreaterEqual_BinaryOperator, gen_odemcustom_Less_BinaryOperator, gen_odemcustom_LessEqual_BinaryOperator, gen_odemcustom_NotEqual_BinaryOperator, gen_odemcustom_Equal_BinaryOperator, gen_odemcustom_InstanceOf_BinaryOperator, gen_odemcustom_Not_UnaryOperator, gen_odemcustom_CreateObject_Expression, gen_odemcustom_CreateObject_TypedElement, gen_odemcustom_Cast_UnaryOperator, gen_odemcustom_Cast_TypedElement, gen_odemcustom_NullLiteral_Expression, gen_odemcustom_TimeLiteral_Expression, gen_odemcustom_ActiveLiteral_Expression, gen_odemcustom_EvalExpr_Expression, gen_odemcustom_MeLiteral_PredefinedId, gen_odemcustom_SuperLiteral_PredefinedId, gen_odemcustom_MetaLiteral_PredefinedId, gen_odemcustom_TypeLiteral_PredefinedId, gen_odemcustom_SetOp_PredefinedId, gen_odemcustom_SizeOfSet_SetOp, gen_odemcustom_FirstInSet_SetOp, gen_odemcustom_Plus_BinaryOperator, gen_odemcustom_Minus_BinaryOperator, gen_odemcustom_Mul_BinaryOperator, gen_odemcustom_Mod_BinaryOperator, gen_odemcustom_Div_BinaryOperator, gen_odemcustom_Neg_UnaryOperator, gen_odemcustom_And_BinaryOperator, gen_odemcustom_Or_BinaryOperator, gen_odemcustom_Greater_BinaryOperator, gen_odemcustom_FalseLiteral_Expression, gen_odemcustom_DoubleLiteral_Expression, gen_odemcustom_IdExpr_Expression, gen_odemcustom_ElementAccess_Expression, gen_odemcustom_VariableAccess_ElementAccess, gen_odemcustom_VariableAccess_ExpandableElement, gen_odemcustom_MetaAccess_VariableAccess, gen_odemcustom_TypeAccess_ElementAccess, gen_odemcustom_TypeAccess_ExpandableElement, gen_odemcustom_NamedExtension_Extension, gen_odemcustom_NamedExtension_NamedElement, gen_odemcustom_ClassContentExtension_NamedExtension, gen_odemcustom_LastInSet_SetOp, gen_odemcustom_Contains_SetOp, gen_odemcustom_IndexOf_SetOp, gen_odemcustom_ObjectAt_SetOp, gen_odemcustom_BeforeInSet_SetOp, gen_odemcustom_AfterInSet_SetOp, gen_odemcustom_StringLiteral_Expression, gen_odemcustom_IntLiteral_Expression, gen_odemcustom_TrueLiteral_Expression, gen_odemcustom_ReferableRhsType_NamedElement, gen_odemcustom_TsRule_NamedElement, gen_odemcustom_TsRule_ReferableRhsType, gen_odemcustom_ExtensionRule_NamedElement, gen_odemcustom_SequenceExpr_RhsExpression, gen_odemcustom_OptionalExpr_RhsExpression, gen_odemcustom_RuntimeExpr_RhsExpression, gen_odemcustom_AtLeastOneExpr_RhsExpression, gen_odemcustom_ArbitraryExpr_RhsExpression, gen_odemcustom_ModuleContentExtension_NamedExtension, gen_odemcustom_ExtensionDefinition_NamedElement, gen_odemcustom_RuleExpr_RhsExpression, gen_odemcustom_IdPropertyType_PropertyType, gen_odemcustom_IntPropertyType_PropertyType, gen_odemcustom_StringPropertyType_PropertyType, gen_odemcustom_BooleanPropertyType_PropertyType, gen_odemcustom_StructuredPropertyType_PropertyType, gen_odemcustom_CompositePropertyType_StructuredPropertyType, gen_odemcustom_ReferencePropertyType_StructuredPropertyType, gen_odemcustom_Mapping_CodeBlock, gen_odemcustom_AlternativeExpr_RhsExpression, gen_odemcustom_TerminalExpr_RhsExpression, gen_odemcustom_PropertyBindingExpr_NamedElement, gen_odemcustom_PropertyBindingExpr_RhsExpression, gen_odemcustom_MappingStatement_Statement, gen_odemcustom_SetGenContextStatement_SimpleStatement, gen_odemcustom_ResetGenContextStatement_SimpleStatement, gen_odemcustom_SaveGenStatement_SimpleStatement, gen_odemcustom_ResumeGenStatement_SimpleStatement, gen_odemcustom_FixedMappingPart_MappingPart, gen_odemcustom_DynamicMappingPart_MappingPart, gen_odemcustom_ExpandExpression_StatementExpression, gen_odemcustom_ExpandExpression_Expression, gen_odemcustom_MetaExpr_Expression, gen_odemcustom_TargetStatement_Statement, gen_odemcustom_CodeQuoteExpression_Expression, gen_odemcustom_QuotedExpression_QuotedCode, gen_odemcustom_QuotedStatements_QuotedCode, gen_odemcustom_QuotedClassContent_QuotedCode, gen_odemcustom_QuotedClassContent_ClassSimilar, gen_odemcustom_QuotedModuleContent_QuotedCode, gen_odemcustom_QuotedModuleContent_Module, gen_odemcustom_TestStatement_Statement, gen_odemcustom_Pattern_NamedElement, gen_odemcustom_ExpandStatement_Statement, gen_odemcustom_ExpandSection_CompositeStatement, gen_odemcustom_ConsiderIdElements_Statement, gen_odemcustom_IncludePattern_Statement, gen_odemcustom_PotentiallyHiddenIdElements_Statement, gen_odemcustom_FindContainer_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)