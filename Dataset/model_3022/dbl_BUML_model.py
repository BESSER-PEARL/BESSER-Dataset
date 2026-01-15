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
dbl_Model = Class(name="dbl::Model")
dbl_Import = Class(name="dbl::Import")
dbl_Module = Class(name="dbl::Module")
NamedElement = Class(name="NamedElement")
EmbeddableExtensionsContainer = Class(name="EmbeddableExtensionsContainer")
dbl_Classifier = Class(name="dbl::Classifier", is_abstract=True)
dbl_ClassAugment = Class(name="dbl::ClassAugment")
dbl_ExtensionDefinition = Class(name="dbl::ExtensionDefinition")
dbl_Annotation = Class(name="dbl::Annotation")
dbl_Procedure = Class(name="dbl::Procedure")
dbl_Variable = Class(name="dbl::Variable")
dbl_Construct = Class(name="dbl::Construct")
NamedExtension = Class(name="NamedExtension")
dbl_ModifierExtensionsContainer = Class(name="dbl::ModifierExtensionsContainer", is_abstract=True)
dbl_Type = Class(name="dbl::Type", is_abstract=True)
dbl_TypedElement = Class(name="dbl::TypedElement", is_abstract=True)
dbl_PrimitiveType = Class(name="dbl::PrimitiveType", is_abstract=True)
dbl_IdExpr = Class(name="dbl::IdExpr")
Type = Class(name="Type")
dbl_VoidType = Class(name="dbl::VoidType")
PrimitiveType = Class(name="PrimitiveType")
dbl_IntType = Class(name="dbl::IntType")
dbl_BoolType = Class(name="dbl::BoolType")
dbl_DoubleType = Class(name="dbl::DoubleType")
dbl_StringType = Class(name="dbl::StringType")
TypedElement = Class(name="TypedElement")
CodeBlock = Class(name="CodeBlock")
AnnotatableElement = Class(name="AnnotatableElement")
dbl_Parameter = Class(name="dbl::Parameter")
dbl_SimpleAnnotation = Class(name="dbl::SimpleAnnotation")
dbl_AnnotationApplication = Class(name="dbl::AnnotationApplication")
dbl_KeyValuePair = Class(name="dbl::KeyValuePair")
dbl_VariableAccess = Class(name="dbl::VariableAccess")
dbl_IdResolution = Class(name="dbl::IdResolution")
dbl_EmbeddableExtensionsContainer = Class(name="dbl::EmbeddableExtensionsContainer", is_abstract=True)
dbl_Extension = Class(name="dbl::Extension")
ReferableRhsType = Class(name="ReferableRhsType")
dbl_NativeBinding = Class(name="dbl::NativeBinding")
dbl_ClassSimilar = Class(name="dbl::ClassSimilar", is_abstract=True)
ModifierExtensionsContainer = Class(name="ModifierExtensionsContainer")
dbl_Clazz = Class(name="dbl::Clazz")
dbl_Interface = Class(name="dbl::Interface")
dbl_StartCodeBlock = Class(name="dbl::StartCodeBlock")
dbl_Expression = Class(name="dbl::Expression")
dbl_AnnotatableElement = Class(name="dbl::AnnotatableElement", is_abstract=True)
Classifier = Class(name="Classifier")
ClassSimilar = Class(name="ClassSimilar")
dbl_Constructor = Class(name="dbl::Constructor")
dbl_AbstractVariable = Class(name="dbl::AbstractVariable", is_abstract=True)
AbstractVariable = Class(name="AbstractVariable")
Statement = Class(name="Statement")
dbl_NamedElement = Class(name="dbl::NamedElement")
ExpandableElement = Class(name="ExpandableElement")
dbl_Statement = Class(name="dbl::Statement")
dbl_CompositeStatement = Class(name="dbl::CompositeStatement")
dbl_SimpleStatement = Class(name="dbl::SimpleStatement")
dbl_ExpressionStatement = Class(name="dbl::ExpressionStatement")
SimpleStatement = Class(name="SimpleStatement")
dbl_StatementExpression = Class(name="dbl::StatementExpression")
dbl_Assignment = Class(name="dbl::Assignment")
dbl_CodeBlock = Class(name="dbl::CodeBlock")
Construct = Class(name="Construct")
dbl_DeprecatedProcedureCallStatement = Class(name="dbl::DeprecatedProcedureCallStatement")
ExpressionStatement = Class(name="ExpressionStatement")
dbl_ProcedureCall = Class(name="dbl::ProcedureCall")
StatementExpression = Class(name="StatementExpression")
dbl_Return = Class(name="dbl::Return")
dbl_WaitUntil = Class(name="dbl::WaitUntil")
dbl_Terminate = Class(name="dbl::Terminate")
dbl_Wait = Class(name="dbl::Wait")
dbl_Reactivate = Class(name="dbl::Reactivate")
dbl_ActivateObject = Class(name="dbl::ActivateObject")
dbl_Advance = Class(name="dbl::Advance")
dbl_Print = Class(name="dbl::Print")
dbl_SetStatement = Class(name="dbl::SetStatement", is_abstract=True)
dbl_RemoveFromSet = Class(name="dbl::RemoveFromSet")
SetStatement = Class(name="SetStatement")
dbl_AddToSet = Class(name="dbl::AddToSet")
dbl_EmptySet = Class(name="dbl::EmptySet")
dbl_IfStatement = Class(name="dbl::IfStatement")
CompositeStatement = Class(name="CompositeStatement")
dbl_WhileStatement = Class(name="dbl::WhileStatement")
dbl_BreakStatement = Class(name="dbl::BreakStatement")
dbl_ContinueStatement = Class(name="dbl::ContinueStatement")
dbl_ForEachStatement = Class(name="dbl::ForEachStatement")
dbl_L1Expr = Class(name="dbl::L1Expr")
Expression = Class(name="Expression")
dbl_BinaryOperator = Class(name="dbl::BinaryOperator", is_abstract=True)
dbl_UnaryOperator = Class(name="dbl::UnaryOperator", is_abstract=True)
dbl_And = Class(name="dbl::And")
BinaryOperator = Class(name="BinaryOperator")
dbl_Or = Class(name="dbl::Or")
dbl_Greater = Class(name="dbl::Greater")
dbl_GreaterEqual = Class(name="dbl::GreaterEqual")
dbl_Less = Class(name="dbl::Less")
dbl_LessEqual = Class(name="dbl::LessEqual")
dbl_NotEqual = Class(name="dbl::NotEqual")
dbl_Equal = Class(name="dbl::Equal")
dbl_InstanceOf = Class(name="dbl::InstanceOf")
dbl_Plus = Class(name="dbl::Plus")
dbl_Minus = Class(name="dbl::Minus")
dbl_Mul = Class(name="dbl::Mul")
dbl_Mod = Class(name="dbl::Mod")
dbl_Div = Class(name="dbl::Div")
dbl_Not = Class(name="dbl::Not")
dbl_Cast = Class(name="dbl::Cast")
dbl_CreateObject = Class(name="dbl::CreateObject")
L1Expr = Class(name="L1Expr")
dbl_NullLiteral = Class(name="dbl::NullLiteral")
dbl_TimeLiteral = Class(name="dbl::TimeLiteral")
dbl_ActiveLiteral = Class(name="dbl::ActiveLiteral")
dbl_StringLiteral = Class(name="dbl::StringLiteral")
dbl_IntLiteral = Class(name="dbl::IntLiteral")
dbl_TrueLiteral = Class(name="dbl::TrueLiteral")
dbl_FalseLiteral = Class(name="dbl::FalseLiteral")
dbl_DoubleLiteral = Class(name="dbl::DoubleLiteral")
dbl_EvalExpr = Class(name="dbl::EvalExpr")
dbl_Neg = Class(name="dbl::Neg")
UnaryOperator = Class(name="UnaryOperator")
dbl_MeLiteral = Class(name="dbl::MeLiteral")
PredefinedId = Class(name="PredefinedId")
dbl_SuperLiteral = Class(name="dbl::SuperLiteral")
dbl_MetaLiteral = Class(name="dbl::MetaLiteral")
dbl_TypeLiteral = Class(name="dbl::TypeLiteral")
dbl_SetOp = Class(name="dbl::SetOp", is_abstract=True)
dbl_SizeOfSet = Class(name="dbl::SizeOfSet")
SetOp = Class(name="SetOp")
dbl_FirstInSet = Class(name="dbl::FirstInSet")
dbl_LastInSet = Class(name="dbl::LastInSet")
dbl_Contains = Class(name="dbl::Contains")
dbl_IndexOf = Class(name="dbl::IndexOf")
dbl_ObjectAt = Class(name="dbl::ObjectAt")
dbl_BeforeInSet = Class(name="dbl::BeforeInSet")
dbl_AfterInSet = Class(name="dbl::AfterInSet")
dbl_DepIdentifiableElement = Class(name="dbl::DepIdentifiableElement", is_abstract=True)
dbl_PredefinedId = Class(name="dbl::PredefinedId")
dbl_ArgumentExpression = Class(name="dbl::ArgumentExpression")
dbl_ElementAccess = Class(name="dbl::ElementAccess", is_abstract=True)
ElementAccess = Class(name="ElementAccess")
dbl_MetaAccess = Class(name="dbl::MetaAccess")
VariableAccess = Class(name="VariableAccess")
dbl_TypeAccess = Class(name="dbl::TypeAccess")
dbl_NamedExtension = Class(name="dbl::NamedExtension")
Extension = Class(name="Extension")
dbl_ClassContentExtension = Class(name="dbl::ClassContentExtension")
dbl_TextualSyntaxDef = Class(name="dbl::TextualSyntaxDef")
dbl_Mapping = Class(name="dbl::Mapping")
dbl_ExtensionRule = Class(name="dbl::ExtensionRule")
dbl_TsRule = Class(name="dbl::TsRule")
dbl_ReferableRhsType = Class(name="dbl::ReferableRhsType", is_abstract=True)
dbl_RhsExpression = Class(name="dbl::RhsExpression", is_abstract=True)
dbl_RuleExpr = Class(name="dbl::RuleExpr")
dbl_ModuleContentExtension = Class(name="dbl::ModuleContentExtension")
dbl_OptionalExpr = Class(name="dbl::OptionalExpr")
dbl_RuntimeExpr = Class(name="dbl::RuntimeExpr")
dbl_AtLeastOneExpr = Class(name="dbl::AtLeastOneExpr")
dbl_ArbitraryExpr = Class(name="dbl::ArbitraryExpr")
dbl_AlternativeExpr = Class(name="dbl::AlternativeExpr")
dbl_TerminalExpr = Class(name="dbl::TerminalExpr")
dbl_PropertyBindingExpr = Class(name="dbl::PropertyBindingExpr")
dbl_SequenceExpr = Class(name="dbl::SequenceExpr")
RhsExpression = Class(name="RhsExpression")
dbl_IdPropertyType = Class(name="dbl::IdPropertyType")
PropertyType = Class(name="PropertyType")
dbl_IntPropertyType = Class(name="dbl::IntPropertyType")
dbl_StringPropertyType = Class(name="dbl::StringPropertyType")
dbl_BooleanPropertyType = Class(name="dbl::BooleanPropertyType")
dbl_StructuredPropertyType = Class(name="dbl::StructuredPropertyType")
dbl_CompositePropertyType = Class(name="dbl::CompositePropertyType")
StructuredPropertyType = Class(name="StructuredPropertyType")
dbl_ReferencePropertyType = Class(name="dbl::ReferencePropertyType")
dbl_Pattern = Class(name="dbl::Pattern")
dbl_MappingPart = Class(name="dbl::MappingPart", is_abstract=True)
dbl_PropertyType = Class(name="dbl::PropertyType", is_abstract=True)
dbl_MetaExpr = Class(name="dbl::MetaExpr")
dbl_TargetStatement = Class(name="dbl::TargetStatement")
dbl_MappingStatement = Class(name="dbl::MappingStatement")
dbl_SetGenContextStatement = Class(name="dbl::SetGenContextStatement")
dbl_ResetGenContextStatement = Class(name="dbl::ResetGenContextStatement")
dbl_SaveGenStatement = Class(name="dbl::SaveGenStatement")
dbl_ResumeGenStatement = Class(name="dbl::ResumeGenStatement")
dbl_FixedMappingPart = Class(name="dbl::FixedMappingPart")
MappingPart = Class(name="MappingPart")
dbl_DynamicMappingPart = Class(name="dbl::DynamicMappingPart")
dbl_ExpandStatement = Class(name="dbl::ExpandStatement")
dbl_ExpandSection = Class(name="dbl::ExpandSection")
dbl_CodeQuoteExpression = Class(name="dbl::CodeQuoteExpression")
dbl_QuotedCode = Class(name="dbl::QuotedCode")
dbl_QuotedExpression = Class(name="dbl::QuotedExpression")
QuotedCode = Class(name="QuotedCode")
dbl_QuotedStatements = Class(name="dbl::QuotedStatements")
dbl_QuotedClassContent = Class(name="dbl::QuotedClassContent")
dbl_ExpandExpression = Class(name="dbl::ExpandExpression")
dbl_TestStatement = Class(name="dbl::TestStatement")
dbl_PotentiallyHiddenIdElements = Class(name="dbl::PotentiallyHiddenIdElements")
dbl_FindContainer = Class(name="dbl::FindContainer")
dbl_ConsiderIdElements = Class(name="dbl::ConsiderIdElements")
dbl_IncludePattern = Class(name="dbl::IncludePattern")
dbl_QuotedModuleContent = Class(name="dbl::QuotedModuleContent")
Module = Class(name="Module")
dbl_ExpandableElement = Class(name="dbl::ExpandableElement")

# dbl_Model class attributes and methods

# dbl_Import class attributes and methods
dbl_Import_file: Property = Property(name="file", type=StringType)
dbl_Import.attributes={dbl_Import_file}

# dbl_Module class attributes and methods

# NamedElement class attributes and methods

# EmbeddableExtensionsContainer class attributes and methods

# dbl_Classifier class attributes and methods

# dbl_ClassAugment class attributes and methods

# dbl_ExtensionDefinition class attributes and methods

# dbl_Annotation class attributes and methods

# dbl_Procedure class attributes and methods
dbl_Procedure_clazz: Property = Property(name="clazz", type=BooleanType)
dbl_Procedure.attributes={dbl_Procedure_clazz}

# dbl_Variable class attributes and methods
dbl_Variable_control: Property = Property(name="control", type=BooleanType)
dbl_Variable_clazz: Property = Property(name="clazz", type=BooleanType)
dbl_Variable.attributes={dbl_Variable_control, dbl_Variable_clazz}

# dbl_Construct class attributes and methods
dbl_Construct_concreteSyntax: Property = Property(name="concreteSyntax", type=StringType)
dbl_Construct.attributes={dbl_Construct_concreteSyntax}

# NamedExtension class attributes and methods

# dbl_ModifierExtensionsContainer class attributes and methods

# dbl_Type class attributes and methods

# dbl_TypedElement class attributes and methods
dbl_TypedElement_isList: Property = Property(name="isList", type=BooleanType)
dbl_TypedElement.attributes={dbl_TypedElement_isList}

# dbl_PrimitiveType class attributes and methods

# dbl_IdExpr class attributes and methods

# Type class attributes and methods

# dbl_VoidType class attributes and methods

# PrimitiveType class attributes and methods

# dbl_IntType class attributes and methods

# dbl_BoolType class attributes and methods

# dbl_DoubleType class attributes and methods

# dbl_StringType class attributes and methods

# TypedElement class attributes and methods

# CodeBlock class attributes and methods

# AnnotatableElement class attributes and methods

# dbl_Parameter class attributes and methods

# dbl_SimpleAnnotation class attributes and methods
dbl_SimpleAnnotation_value: Property = Property(name="value", type=StringType)
dbl_SimpleAnnotation.attributes={dbl_SimpleAnnotation_value}

# dbl_AnnotationApplication class attributes and methods

# dbl_KeyValuePair class attributes and methods

# dbl_VariableAccess class attributes and methods

# dbl_IdResolution class attributes and methods
dbl_IdResolution_metaModelPlatformURI: Property = Property(name="metaModelPlatformURI", type=StringType)
dbl_IdResolution.attributes={dbl_IdResolution_metaModelPlatformURI}

# dbl_EmbeddableExtensionsContainer class attributes and methods

# dbl_Extension class attributes and methods

# ReferableRhsType class attributes and methods

# dbl_NativeBinding class attributes and methods
dbl_NativeBinding_targetLanguage: Property = Property(name="targetLanguage", type=StringType)
dbl_NativeBinding_targetType: Property = Property(name="targetType", type=StringType)
dbl_NativeBinding.attributes={dbl_NativeBinding_targetType, dbl_NativeBinding_targetLanguage}

# dbl_ClassSimilar class attributes and methods

# ModifierExtensionsContainer class attributes and methods

# dbl_Clazz class attributes and methods
dbl_Clazz_active: Property = Property(name="active", type=BooleanType)
dbl_Clazz.attributes={dbl_Clazz_active}

# dbl_Interface class attributes and methods

# dbl_StartCodeBlock class attributes and methods

# dbl_Expression class attributes and methods

# dbl_AnnotatableElement class attributes and methods

# Classifier class attributes and methods

# ClassSimilar class attributes and methods

# dbl_Constructor class attributes and methods

# dbl_AbstractVariable class attributes and methods

# AbstractVariable class attributes and methods

# Statement class attributes and methods

# dbl_NamedElement class attributes and methods
dbl_NamedElement_name: Property = Property(name="name", type=StringType)
dbl_NamedElement.attributes={dbl_NamedElement_name}

# ExpandableElement class attributes and methods

# dbl_Statement class attributes and methods

# dbl_CompositeStatement class attributes and methods

# dbl_SimpleStatement class attributes and methods

# dbl_ExpressionStatement class attributes and methods

# SimpleStatement class attributes and methods

# dbl_StatementExpression class attributes and methods

# dbl_Assignment class attributes and methods

# dbl_CodeBlock class attributes and methods

# Construct class attributes and methods

# dbl_DeprecatedProcedureCallStatement class attributes and methods

# ExpressionStatement class attributes and methods

# dbl_ProcedureCall class attributes and methods

# StatementExpression class attributes and methods

# dbl_Return class attributes and methods

# dbl_WaitUntil class attributes and methods

# dbl_Terminate class attributes and methods

# dbl_Wait class attributes and methods

# dbl_Reactivate class attributes and methods

# dbl_ActivateObject class attributes and methods
dbl_ActivateObject_priority: Property = Property(name="priority", type=IntegerType)
dbl_ActivateObject.attributes={dbl_ActivateObject_priority}

# dbl_Advance class attributes and methods

# dbl_Print class attributes and methods

# dbl_SetStatement class attributes and methods

# dbl_RemoveFromSet class attributes and methods

# SetStatement class attributes and methods

# dbl_AddToSet class attributes and methods

# dbl_EmptySet class attributes and methods

# dbl_IfStatement class attributes and methods

# CompositeStatement class attributes and methods

# dbl_WhileStatement class attributes and methods

# dbl_BreakStatement class attributes and methods

# dbl_ContinueStatement class attributes and methods

# dbl_ForEachStatement class attributes and methods

# dbl_L1Expr class attributes and methods

# Expression class attributes and methods

# dbl_BinaryOperator class attributes and methods

# dbl_UnaryOperator class attributes and methods

# dbl_And class attributes and methods

# BinaryOperator class attributes and methods

# dbl_Or class attributes and methods

# dbl_Greater class attributes and methods

# dbl_GreaterEqual class attributes and methods

# dbl_Less class attributes and methods

# dbl_LessEqual class attributes and methods

# dbl_NotEqual class attributes and methods

# dbl_Equal class attributes and methods

# dbl_InstanceOf class attributes and methods

# dbl_Plus class attributes and methods

# dbl_Minus class attributes and methods

# dbl_Mul class attributes and methods

# dbl_Mod class attributes and methods

# dbl_Div class attributes and methods

# dbl_Not class attributes and methods

# dbl_Cast class attributes and methods

# dbl_CreateObject class attributes and methods

# L1Expr class attributes and methods

# dbl_NullLiteral class attributes and methods

# dbl_TimeLiteral class attributes and methods

# dbl_ActiveLiteral class attributes and methods

# dbl_StringLiteral class attributes and methods
dbl_StringLiteral_value: Property = Property(name="value", type=StringType)
dbl_StringLiteral.attributes={dbl_StringLiteral_value}

# dbl_IntLiteral class attributes and methods
dbl_IntLiteral_value: Property = Property(name="value", type=IntegerType)
dbl_IntLiteral.attributes={dbl_IntLiteral_value}

# dbl_TrueLiteral class attributes and methods

# dbl_FalseLiteral class attributes and methods

# dbl_DoubleLiteral class attributes and methods
dbl_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
dbl_DoubleLiteral.attributes={dbl_DoubleLiteral_value}

# dbl_EvalExpr class attributes and methods

# dbl_Neg class attributes and methods

# UnaryOperator class attributes and methods

# dbl_MeLiteral class attributes and methods

# PredefinedId class attributes and methods

# dbl_SuperLiteral class attributes and methods

# dbl_MetaLiteral class attributes and methods

# dbl_TypeLiteral class attributes and methods

# dbl_SetOp class attributes and methods

# dbl_SizeOfSet class attributes and methods

# SetOp class attributes and methods

# dbl_FirstInSet class attributes and methods

# dbl_LastInSet class attributes and methods

# dbl_Contains class attributes and methods

# dbl_IndexOf class attributes and methods

# dbl_ObjectAt class attributes and methods

# dbl_BeforeInSet class attributes and methods

# dbl_AfterInSet class attributes and methods

# dbl_DepIdentifiableElement class attributes and methods

# dbl_PredefinedId class attributes and methods

# dbl_ArgumentExpression class attributes and methods

# dbl_ElementAccess class attributes and methods

# ElementAccess class attributes and methods

# dbl_MetaAccess class attributes and methods

# VariableAccess class attributes and methods

# dbl_TypeAccess class attributes and methods

# dbl_NamedExtension class attributes and methods

# Extension class attributes and methods

# dbl_ClassContentExtension class attributes and methods

# dbl_TextualSyntaxDef class attributes and methods

# dbl_Mapping class attributes and methods

# dbl_ExtensionRule class attributes and methods

# dbl_TsRule class attributes and methods
dbl_TsRule_metaClassName: Property = Property(name="metaClassName", type=StringType)
dbl_TsRule.attributes={dbl_TsRule_metaClassName}

# dbl_ReferableRhsType class attributes and methods

# dbl_RhsExpression class attributes and methods
dbl_RhsExpression_m_getSubExpressions: Method = Method(name="getSubExpressions", parameters={}, type=StringType)
dbl_RhsExpression.methods={dbl_RhsExpression_m_getSubExpressions}

# dbl_RuleExpr class attributes and methods

# dbl_ModuleContentExtension class attributes and methods

# dbl_OptionalExpr class attributes and methods

# dbl_RuntimeExpr class attributes and methods

# dbl_AtLeastOneExpr class attributes and methods

# dbl_ArbitraryExpr class attributes and methods

# dbl_AlternativeExpr class attributes and methods

# dbl_TerminalExpr class attributes and methods
dbl_TerminalExpr_terminal: Property = Property(name="terminal", type=StringType)
dbl_TerminalExpr.attributes={dbl_TerminalExpr_terminal}

# dbl_PropertyBindingExpr class attributes and methods
dbl_PropertyBindingExpr_operator: Property = Property(name="operator", type=StringType)
dbl_PropertyBindingExpr.attributes={dbl_PropertyBindingExpr_operator}

# dbl_SequenceExpr class attributes and methods

# RhsExpression class attributes and methods

# dbl_IdPropertyType class attributes and methods

# PropertyType class attributes and methods

# dbl_IntPropertyType class attributes and methods

# dbl_StringPropertyType class attributes and methods

# dbl_BooleanPropertyType class attributes and methods
dbl_BooleanPropertyType_terminal: Property = Property(name="terminal", type=StringType)
dbl_BooleanPropertyType.attributes={dbl_BooleanPropertyType_terminal}

# dbl_StructuredPropertyType class attributes and methods

# dbl_CompositePropertyType class attributes and methods
dbl_CompositePropertyType_list: Property = Property(name="list", type=BooleanType)
dbl_CompositePropertyType.attributes={dbl_CompositePropertyType_list}

# StructuredPropertyType class attributes and methods

# dbl_ReferencePropertyType class attributes and methods
dbl_ReferencePropertyType_rawReference: Property = Property(name="rawReference", type=BooleanType)
dbl_ReferencePropertyType.attributes={dbl_ReferencePropertyType_rawReference}

# dbl_Pattern class attributes and methods
dbl_Pattern_top: Property = Property(name="top", type=BooleanType)
dbl_Pattern.attributes={dbl_Pattern_top}

# dbl_MappingPart class attributes and methods

# dbl_PropertyType class attributes and methods

# dbl_MetaExpr class attributes and methods

# dbl_TargetStatement class attributes and methods

# dbl_MappingStatement class attributes and methods

# dbl_SetGenContextStatement class attributes and methods
dbl_SetGenContextStatement_addAfterContext: Property = Property(name="addAfterContext", type=BooleanType)
dbl_SetGenContextStatement.attributes={dbl_SetGenContextStatement_addAfterContext}

# dbl_ResetGenContextStatement class attributes and methods

# dbl_SaveGenStatement class attributes and methods

# dbl_ResumeGenStatement class attributes and methods

# dbl_FixedMappingPart class attributes and methods
dbl_FixedMappingPart_code: Property = Property(name="code", type=StringType)
dbl_FixedMappingPart.attributes={dbl_FixedMappingPart_code}

# MappingPart class attributes and methods

# dbl_DynamicMappingPart class attributes and methods

# dbl_ExpandStatement class attributes and methods

# dbl_ExpandSection class attributes and methods

# dbl_CodeQuoteExpression class attributes and methods

# dbl_QuotedCode class attributes and methods

# dbl_QuotedExpression class attributes and methods

# QuotedCode class attributes and methods

# dbl_QuotedStatements class attributes and methods

# dbl_QuotedClassContent class attributes and methods

# dbl_ExpandExpression class attributes and methods

# dbl_TestStatement class attributes and methods
dbl_TestStatement_value: Property = Property(name="value", type=StringType)
dbl_TestStatement.attributes={dbl_TestStatement_value}

# dbl_PotentiallyHiddenIdElements class attributes and methods

# dbl_FindContainer class attributes and methods

# dbl_ConsiderIdElements class attributes and methods

# dbl_IncludePattern class attributes and methods

# dbl_QuotedModuleContent class attributes and methods

# Module class attributes and methods

# dbl_ExpandableElement class attributes and methods

# Relationships
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="dbl_Import", type=dbl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Model", type=dbl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules1: BinaryAssociation = BinaryAssociation(
    name="modules1",
    ends={
        Property(name="dbl_Module", type=dbl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Model2", type=dbl_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model3: BinaryAssociation = BinaryAssociation(
    name="model3",
    ends={
        Property(name="dbl_Model5", type=dbl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Import4", type=dbl_Model, multiplicity=Multiplicity(0, 1))
    }
)
classifiers6: BinaryAssociation = BinaryAssociation(
    name="classifiers6",
    ends={
        Property(name="dbl_Classifier", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module7", type=dbl_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classAugments8: BinaryAssociation = BinaryAssociation(
    name="classAugments8",
    ends={
        Property(name="dbl_ClassAugment", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module9", type=dbl_ClassAugment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefs10: BinaryAssociation = BinaryAssociation(
    name="extensionDefs10",
    ends={
        Property(name="dbl_ExtensionDefinition", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module11", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationDefs12: BinaryAssociation = BinaryAssociation(
    name="annotationDefs12",
    ends={
        Property(name="dbl_Annotation", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module13", type=dbl_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures14: BinaryAssociation = BinaryAssociation(
    name="procedures14",
    ends={
        Property(name="dbl_Procedure", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module15", type=dbl_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables16: BinaryAssociation = BinaryAssociation(
    name="variables16",
    ends={
        Property(name="dbl_Variable", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module17", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions20: BinaryAssociation = BinaryAssociation(
    name="extensions20",
    ends={
        Property(name="dbl_EmbeddableExtensionsContainer", type=dbl_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="dbl_Extension", type=dbl_EmbeddableExtensionsContainer, multiplicity=Multiplicity(1, 1))
    }
)
modifierExtensions21: BinaryAssociation = BinaryAssociation(
    name="modifierExtensions21",
    ends={
        Property(name="dbl_Extension22", type=dbl_ModifierExtensionsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ModifierExtensionsContainer", type=dbl_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveType23: BinaryAssociation = BinaryAssociation(
    name="primitiveType23",
    ends={
        Property(name="dbl_PrimitiveType", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement", type=dbl_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifierTypeExpr24: BinaryAssociation = BinaryAssociation(
    name="classifierTypeExpr24",
    ends={
        Property(name="dbl_IdExpr", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement25", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters26: BinaryAssociation = BinaryAssociation(
    name="parameters26",
    ends={
        Property(name="dbl_Parameter", type=dbl_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Procedure27", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys28: BinaryAssociation = BinaryAssociation(
    name="keys28",
    ends={
        Property(name="dbl_Variable30", type=dbl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Annotation29", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationDef31: BinaryAssociation = BinaryAssociation(
    name="annotationDef31",
    ends={
        Property(name="dbl_Annotation32", type=dbl_AnnotationApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AnnotationApplication", type=dbl_Annotation, multiplicity=Multiplicity(1, 1))
    }
)
keyValuePairs33: BinaryAssociation = BinaryAssociation(
    name="keyValuePairs33",
    ends={
        Property(name="dbl_KeyValuePair", type=dbl_AnnotationApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AnnotationApplication34", type=dbl_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key35: BinaryAssociation = BinaryAssociation(
    name="key35",
    ends={
        Property(name="dbl_VariableAccess", type=dbl_KeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_KeyValuePair36", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
idRes18: BinaryAssociation = BinaryAssociation(
    name="idRes18",
    ends={
        Property(name="dbl_IdResolution", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module19", type=dbl_IdResolution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationApplications39: BinaryAssociation = BinaryAssociation(
    name="annotationApplications39",
    ends={
        Property(name="dbl_AnnotationApplication40", type=dbl_AnnotatableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AnnotatableElement", type=dbl_AnnotationApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleAnnotations41: BinaryAssociation = BinaryAssociation(
    name="simpleAnnotations41",
    ends={
        Property(name="dbl_SimpleAnnotation", type=dbl_AnnotatableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AnnotatableElement42", type=dbl_SimpleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings43: BinaryAssociation = BinaryAssociation(
    name="bindings43",
    ends={
        Property(name="dbl_NativeBinding", type=dbl_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Classifier44", type=dbl_NativeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes45: BinaryAssociation = BinaryAssociation(
    name="attributes45",
    ends={
        Property(name="dbl_Variable46", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods47: BinaryAssociation = BinaryAssociation(
    name="methods47",
    ends={
        Property(name="dbl_Procedure49", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar48", type=dbl_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass50: BinaryAssociation = BinaryAssociation(
    name="superClass50",
    ends={
        Property(name="dbl_Clazz", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar51", type=dbl_Clazz, multiplicity=Multiplicity(0, 1))
    }
)
implementedInterfaces52: BinaryAssociation = BinaryAssociation(
    name="implementedInterfaces52",
    ends={
        Property(name="dbl_Interface", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar53", type=dbl_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
initialBlock54: BinaryAssociation = BinaryAssociation(
    name="initialBlock54",
    ends={
        Property(name="dbl_StartCodeBlock", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar55", type=dbl_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalBlock56: BinaryAssociation = BinaryAssociation(
    name="finalBlock56",
    ends={
        Property(name="dbl_StartCodeBlock58", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar57", type=dbl_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionsBlock59: BinaryAssociation = BinaryAssociation(
    name="actionsBlock59",
    ends={
        Property(name="dbl_StartCodeBlock61", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar60", type=dbl_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reportBlock62: BinaryAssociation = BinaryAssociation(
    name="reportBlock62",
    ends={
        Property(name="dbl_StartCodeBlock64", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar63", type=dbl_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clearBlock65: BinaryAssociation = BinaryAssociation(
    name="clearBlock65",
    ends={
        Property(name="dbl_StartCodeBlock67", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar66", type=dbl_StartCodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value37: BinaryAssociation = BinaryAssociation(
    name="value37",
    ends={
        Property(name="dbl_Expression", type=dbl_KeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_KeyValuePair38", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constructor68: BinaryAssociation = BinaryAssociation(
    name="constructor68",
    ends={
        Property(name="dbl_Constructor", type=dbl_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Clazz69", type=dbl_Constructor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters73: BinaryAssociation = BinaryAssociation(
    name="parameters73",
    ends={
        Property(name="dbl_Parameter75", type=dbl_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Constructor74", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
augmentedClass76: BinaryAssociation = BinaryAssociation(
    name="augmentedClass76",
    ends={
        Property(name="dbl_Clazz78", type=dbl_ClassAugment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassAugment77", type=dbl_Clazz, multiplicity=Multiplicity(1, 1))
    }
)
methods79: BinaryAssociation = BinaryAssociation(
    name="methods79",
    ends={
        Property(name="dbl_Procedure81", type=dbl_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Interface80", type=dbl_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces83: BinaryAssociation = BinaryAssociation(
    name="superInterfaces83",
    ends={
        Property(name="dbl_Interface84", type=dbl_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Interface82", type=dbl_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
initialValue85: BinaryAssociation = BinaryAssociation(
    name="initialValue85",
    ends={
        Property(name="dbl_Expression87", type=dbl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Variable86", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseConstructorArguments70: BinaryAssociation = BinaryAssociation(
    name="baseConstructorArguments70",
    ends={
        Property(name="dbl_Expression72", type=dbl_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Clazz71", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements88: BinaryAssociation = BinaryAssociation(
    name="statements88",
    ends={
        Property(name="dbl_Statement", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CodeBlock", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression89: BinaryAssociation = BinaryAssociation(
    name="expression89",
    ends={
        Property(name="dbl_StatementExpression", type=dbl_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpressionStatement", type=dbl_StatementExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value92: BinaryAssociation = BinaryAssociation(
    name="value92",
    ends={
        Property(name="dbl_Expression94", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment93", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
procedureCall95: BinaryAssociation = BinaryAssociation(
    name="procedureCall95",
    ends={
        Property(name="dbl_Expression96", type=dbl_DeprecatedProcedureCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_DeprecatedProcedureCallStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
procedureAccess97: BinaryAssociation = BinaryAssociation(
    name="procedureAccess97",
    ends={
        Property(name="dbl_Expression98", type=dbl_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ProcedureCall", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value99: BinaryAssociation = BinaryAssociation(
    name="value99",
    ends={
        Property(name="dbl_Expression100", type=dbl_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Return", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition101: BinaryAssociation = BinaryAssociation(
    name="condition101",
    ends={
        Property(name="dbl_Expression102", type=dbl_WaitUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WaitUntil", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess103: BinaryAssociation = BinaryAssociation(
    name="objectAccess103",
    ends={
        Property(name="dbl_Expression104", type=dbl_Reactivate, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Reactivate", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess105: BinaryAssociation = BinaryAssociation(
    name="objectAccess105",
    ends={
        Property(name="dbl_Expression106", type=dbl_ActivateObject, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ActivateObject", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
time107: BinaryAssociation = BinaryAssociation(
    name="time107",
    ends={
        Property(name="dbl_Expression108", type=dbl_Advance, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Advance", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputs109: BinaryAssociation = BinaryAssociation(
    name="outputs109",
    ends={
        Property(name="dbl_Expression110", type=dbl_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Print", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object111: BinaryAssociation = BinaryAssociation(
    name="object111",
    ends={
        Property(name="dbl_Expression112", type=dbl_SetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SetStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
set113: BinaryAssociation = BinaryAssociation(
    name="set113",
    ends={
        Property(name="dbl_Expression115", type=dbl_SetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SetStatement114", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
atIndex116: BinaryAssociation = BinaryAssociation(
    name="atIndex116",
    ends={
        Property(name="dbl_Expression117", type=dbl_AddToSet, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AddToSet", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable90: BinaryAssociation = BinaryAssociation(
    name="variable90",
    ends={
        Property(name="dbl_VariableAccess91", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elifCondition123: BinaryAssociation = BinaryAssociation(
    name="elifCondition123",
    ends={
        Property(name="dbl_Expression125", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement124", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elifCaseBlock126: BinaryAssociation = BinaryAssociation(
    name="elifCaseBlock126",
    ends={
        Property(name="dbl_CodeBlock128", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement127", type=dbl_CodeBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseCaseBlock129: BinaryAssociation = BinaryAssociation(
    name="elseCaseBlock129",
    ends={
        Property(name="dbl_CodeBlock131", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement130", type=dbl_CodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition132: BinaryAssociation = BinaryAssociation(
    name="condition132",
    ends={
        Property(name="dbl_Expression133", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whileBlock134: BinaryAssociation = BinaryAssociation(
    name="whileBlock134",
    ends={
        Property(name="dbl_CodeBlock136", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement135", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteratorVariableDefinition137: BinaryAssociation = BinaryAssociation(
    name="iteratorVariableDefinition137",
    ends={
        Property(name="dbl_Variable138", type=dbl_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForEachStatement", type=dbl_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iteratorVariableReference139: BinaryAssociation = BinaryAssociation(
    name="iteratorVariableReference139",
    ends={
        Property(name="dbl_VariableAccess141", type=dbl_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForEachStatement140", type=dbl_VariableAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterableExpression142: BinaryAssociation = BinaryAssociation(
    name="iterableExpression142",
    ends={
        Property(name="dbl_Expression144", type=dbl_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForEachStatement143", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
forBlock145: BinaryAssociation = BinaryAssociation(
    name="forBlock145",
    ends={
        Property(name="dbl_CodeBlock147", type=dbl_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForEachStatement146", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op1148: BinaryAssociation = BinaryAssociation(
    name="op1148",
    ends={
        Property(name="dbl_Expression149", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition118: BinaryAssociation = BinaryAssociation(
    name="condition118",
    ends={
        Property(name="dbl_Expression119", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifCaseBlock120: BinaryAssociation = BinaryAssociation(
    name="ifCaseBlock120",
    ends={
        Property(name="dbl_CodeBlock122", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement121", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op153: BinaryAssociation = BinaryAssociation(
    name="op153",
    ends={
        Property(name="dbl_Expression154", type=dbl_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_UnaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op2150: BinaryAssociation = BinaryAssociation(
    name="op2150",
    ends={
        Property(name="dbl_Expression152", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator151", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
set157: BinaryAssociation = BinaryAssociation(
    name="set157",
    ends={
        Property(name="dbl_Expression158", type=dbl_SetOp, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SetOp", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr155: BinaryAssociation = BinaryAssociation(
    name="expr155",
    ends={
        Property(name="dbl_Expression156", type=dbl_EvalExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_EvalExpr", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedElement162: BinaryAssociation = BinaryAssociation(
    name="referencedElement162",
    ends={
        Property(name="dbl_NamedElement", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr163", type=dbl_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
predefinedId164: BinaryAssociation = BinaryAssociation(
    name="predefinedId164",
    ends={
        Property(name="dbl_PredefinedId", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr165", type=dbl_PredefinedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments166: BinaryAssociation = BinaryAssociation(
    name="arguments166",
    ends={
        Property(name="dbl_ArgumentExpression", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr167", type=dbl_ArgumentExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments168: BinaryAssociation = BinaryAssociation(
    name="arguments168",
    ends={
        Property(name="dbl_Expression170", type=dbl_ArgumentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ArgumentExpression169", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idExpr171: BinaryAssociation = BinaryAssociation(
    name="idExpr171",
    ends={
        Property(name="dbl_IdExpr172", type=dbl_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ElementAccess", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentIdExpr160: BinaryAssociation = BinaryAssociation(
    name="parentIdExpr160",
    ends={
        Property(name="dbl_IdExpr161", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr159", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abstractSyntaxDef173: BinaryAssociation = BinaryAssociation(
    name="abstractSyntaxDef173",
    ends={
        Property(name="dbl_Classifier175", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition174", type=dbl_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textualSyntaxDef176: BinaryAssociation = BinaryAssociation(
    name="textualSyntaxDef176",
    ends={
        Property(name="dbl_TextualSyntaxDef", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition177", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappingDef178: BinaryAssociation = BinaryAssociation(
    name="mappingDef178",
    ends={
        Property(name="dbl_Mapping", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition179", type=dbl_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionRule180: BinaryAssociation = BinaryAssociation(
    name="extensionRule180",
    ends={
        Property(name="dbl_ExtensionRule", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TextualSyntaxDef181", type=dbl_ExtensionRule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
newRules182: BinaryAssociation = BinaryAssociation(
    name="newRules182",
    ends={
        Property(name="dbl_TsRule", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TextualSyntaxDef183", type=dbl_TsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rhs184: BinaryAssociation = BinaryAssociation(
    name="rhs184",
    ends={
        Property(name="dbl_RhsExpression", type=dbl_TsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TsRule185", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instantiableMetaClass186: BinaryAssociation = BinaryAssociation(
    name="instantiableMetaClass186",
    ends={
        Property(name="dbl_Classifier188", type=dbl_ExtensionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionRule187", type=dbl_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
firstNewRule189: BinaryAssociation = BinaryAssociation(
    name="firstNewRule189",
    ends={
        Property(name="dbl_RuleExpr", type=dbl_ExtensionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionRule190", type=dbl_RuleExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequence191: BinaryAssociation = BinaryAssociation(
    name="sequence191",
    ends={
        Property(name="dbl_RhsExpression192", type=dbl_SequenceExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SequenceExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression193: BinaryAssociation = BinaryAssociation(
    name="expression193",
    ends={
        Property(name="dbl_RhsExpression194", type=dbl_OptionalExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_OptionalExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression195: BinaryAssociation = BinaryAssociation(
    name="expression195",
    ends={
        Property(name="dbl_RhsExpression196", type=dbl_RuntimeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_RuntimeExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression197: BinaryAssociation = BinaryAssociation(
    name="expression197",
    ends={
        Property(name="dbl_RhsExpression198", type=dbl_AtLeastOneExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AtLeastOneExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression199: BinaryAssociation = BinaryAssociation(
    name="expression199",
    ends={
        Property(name="dbl_RhsExpression200", type=dbl_ArbitraryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ArbitraryExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left201: BinaryAssociation = BinaryAssociation(
    name="left201",
    ends={
        Property(name="dbl_RhsExpression202", type=dbl_AlternativeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AlternativeExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right203: BinaryAssociation = BinaryAssociation(
    name="right203",
    ends={
        Property(name="dbl_RhsExpression205", type=dbl_AlternativeExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AlternativeExpr204", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule207: BinaryAssociation = BinaryAssociation(
    name="rule207",
    ends={
        Property(name="dbl_TsRule209", type=dbl_RuleExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_RuleExpr208", type=dbl_TsRule, multiplicity=Multiplicity(1, 1))
    }
)
type210: BinaryAssociation = BinaryAssociation(
    name="type210",
    ends={
        Property(name="dbl_ReferableRhsType", type=dbl_StructuredPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_StructuredPropertyType", type=dbl_ReferableRhsType, multiplicity=Multiplicity(1, 1))
    }
)
idResolutionPattern211: BinaryAssociation = BinaryAssociation(
    name="idResolutionPattern211",
    ends={
        Property(name="dbl_Pattern", type=dbl_ReferencePropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ReferencePropertyType", type=dbl_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
parts212: BinaryAssociation = BinaryAssociation(
    name="parts212",
    ends={
        Property(name="dbl_MappingPart", type=dbl_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Mapping213", type=dbl_MappingPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyType206: BinaryAssociation = BinaryAssociation(
    name="propertyType206",
    ends={
        Property(name="dbl_PropertyType", type=dbl_PropertyBindingExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_PropertyBindingExpr", type=dbl_PropertyType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr217: BinaryAssociation = BinaryAssociation(
    name="expr217",
    ends={
        Property(name="dbl_Expression218", type=dbl_MetaExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MetaExpr", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
codeBlock219: BinaryAssociation = BinaryAssociation(
    name="codeBlock219",
    ends={
        Property(name="dbl_CodeBlock220", type=dbl_TargetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TargetStatement", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parts221: BinaryAssociation = BinaryAssociation(
    name="parts221",
    ends={
        Property(name="dbl_MappingPart222", type=dbl_MappingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MappingStatement", type=dbl_MappingPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs223: BinaryAssociation = BinaryAssociation(
    name="exprs223",
    ends={
        Property(name="dbl_Expression225", type=dbl_MappingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MappingStatement224", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context226: BinaryAssociation = BinaryAssociation(
    name="context226",
    ends={
        Property(name="dbl_Expression227", type=dbl_SetGenContextStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SetGenContextStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable228: BinaryAssociation = BinaryAssociation(
    name="variable228",
    ends={
        Property(name="dbl_Expression229", type=dbl_SaveGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SaveGenStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable230: BinaryAssociation = BinaryAssociation(
    name="variable230",
    ends={
        Property(name="dbl_Expression231", type=dbl_ResumeGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ResumeGenStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject214: BinaryAssociation = BinaryAssociation(
    name="metaObject214",
    ends={
        Property(name="dbl_Expression216", type=dbl_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Mapping215", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject234: BinaryAssociation = BinaryAssociation(
    name="metaObject234",
    ends={
        Property(name="dbl_Expression235", type=dbl_ExpandExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject236: BinaryAssociation = BinaryAssociation(
    name="metaObject236",
    ends={
        Property(name="dbl_Expression237", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location238: BinaryAssociation = BinaryAssociation(
    name="location238",
    ends={
        Property(name="dbl_Expression240", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement239", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codeBlock241: BinaryAssociation = BinaryAssociation(
    name="codeBlock241",
    ends={
        Property(name="dbl_CodeBlock242", type=dbl_ExpandSection, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandSection", type=dbl_CodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quotedCode243: BinaryAssociation = BinaryAssociation(
    name="quotedCode243",
    ends={
        Property(name="dbl_QuotedCode", type=dbl_CodeQuoteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CodeQuoteExpression", type=dbl_QuotedCode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression244: BinaryAssociation = BinaryAssociation(
    name="expression244",
    ends={
        Property(name="dbl_Expression245", type=dbl_QuotedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements246: BinaryAssociation = BinaryAssociation(
    name="statements246",
    ends={
        Property(name="dbl_Statement247", type=dbl_QuotedStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedStatements", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr232: BinaryAssociation = BinaryAssociation(
    name="expr232",
    ends={
        Property(name="dbl_Expression233", type=dbl_DynamicMappingPart, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_DynamicMappingPart", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
patterns250: BinaryAssociation = BinaryAssociation(
    name="patterns250",
    ends={
        Property(name="dbl_Pattern252", type=dbl_IdResolution, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdResolution251", type=dbl_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context253: BinaryAssociation = BinaryAssociation(
    name="context253",
    ends={
        Property(name="dbl_Parameter255", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern254", type=dbl_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
codeBlock256: BinaryAssociation = BinaryAssociation(
    name="codeBlock256",
    ends={
        Property(name="dbl_CodeBlock258", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern257", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
codeBlock259: BinaryAssociation = BinaryAssociation(
    name="codeBlock259",
    ends={
        Property(name="dbl_CodeBlock260", type=dbl_PotentiallyHiddenIdElements, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_PotentiallyHiddenIdElements", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableBinding261: BinaryAssociation = BinaryAssociation(
    name="variableBinding261",
    ends={
        Property(name="dbl_Parameter262", type=dbl_FindContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_FindContainer", type=dbl_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
containerBlock263: BinaryAssociation = BinaryAssociation(
    name="containerBlock263",
    ends={
        Property(name="dbl_CodeBlock265", type=dbl_FindContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_FindContainer264", type=dbl_CodeBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock266: BinaryAssociation = BinaryAssociation(
    name="elseBlock266",
    ends={
        Property(name="dbl_CodeBlock268", type=dbl_FindContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_FindContainer267", type=dbl_CodeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementsQuery269: BinaryAssociation = BinaryAssociation(
    name="elementsQuery269",
    ends={
        Property(name="dbl_Expression270", type=dbl_ConsiderIdElements, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ConsiderIdElements", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern271: BinaryAssociation = BinaryAssociation(
    name="pattern271",
    ends={
        Property(name="dbl_Pattern272", type=dbl_IncludePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IncludePattern", type=dbl_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
context273: BinaryAssociation = BinaryAssociation(
    name="context273",
    ends={
        Property(name="dbl_Expression275", type=dbl_IncludePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IncludePattern274", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expandExpression248: BinaryAssociation = BinaryAssociation(
    name="expandExpression248",
    ends={
        Property(name="dbl_ExpandExpression249", type=dbl_ExpandableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandableElement", type=dbl_ExpandExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dbl_Module_NamedElement = Generalization(general=NamedElement, specific=dbl_Module)
gen_dbl_Module_EmbeddableExtensionsContainer = Generalization(general=EmbeddableExtensionsContainer, specific=dbl_Module)
gen_dbl_Construct_NamedExtension = Generalization(general=NamedExtension, specific=dbl_Construct)
gen_dbl_PrimitiveType_Type = Generalization(general=Type, specific=dbl_PrimitiveType)
gen_dbl_VoidType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_VoidType)
gen_dbl_IntType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_IntType)
gen_dbl_BoolType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_BoolType)
gen_dbl_DoubleType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_DoubleType)
gen_dbl_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_StringType)
gen_dbl_Procedure_NamedElement = Generalization(general=NamedElement, specific=dbl_Procedure)
gen_dbl_Procedure_TypedElement = Generalization(general=TypedElement, specific=dbl_Procedure)
gen_dbl_Procedure_CodeBlock = Generalization(general=CodeBlock, specific=dbl_Procedure)
gen_dbl_Procedure_AnnotatableElement = Generalization(general=AnnotatableElement, specific=dbl_Procedure)
gen_dbl_SimpleAnnotation_NamedElement = Generalization(general=NamedElement, specific=dbl_SimpleAnnotation)
gen_dbl_Annotation_NamedElement = Generalization(general=NamedElement, specific=dbl_Annotation)
gen_dbl_Classifier_Type = Generalization(general=Type, specific=dbl_Classifier)
gen_dbl_Classifier_NamedElement = Generalization(general=NamedElement, specific=dbl_Classifier)
gen_dbl_Classifier_ReferableRhsType = Generalization(general=ReferableRhsType, specific=dbl_Classifier)
gen_dbl_ClassSimilar_EmbeddableExtensionsContainer = Generalization(general=EmbeddableExtensionsContainer, specific=dbl_ClassSimilar)
gen_dbl_ClassSimilar_ModifierExtensionsContainer = Generalization(general=ModifierExtensionsContainer, specific=dbl_ClassSimilar)
gen_dbl_StartCodeBlock_CodeBlock = Generalization(general=CodeBlock, specific=dbl_StartCodeBlock)
gen_dbl_Clazz_Classifier = Generalization(general=Classifier, specific=dbl_Clazz)
gen_dbl_Clazz_ClassSimilar = Generalization(general=ClassSimilar, specific=dbl_Clazz)
gen_dbl_ClassAugment_ClassSimilar = Generalization(general=ClassSimilar, specific=dbl_ClassAugment)
gen_dbl_Interface_Classifier = Generalization(general=Classifier, specific=dbl_Interface)
gen_dbl_AbstractVariable_NamedElement = Generalization(general=NamedElement, specific=dbl_AbstractVariable)
gen_dbl_AbstractVariable_TypedElement = Generalization(general=TypedElement, specific=dbl_AbstractVariable)
gen_dbl_Variable_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Variable)
gen_dbl_Variable_Statement = Generalization(general=Statement, specific=dbl_Variable)
gen_dbl_Variable_ModifierExtensionsContainer = Generalization(general=ModifierExtensionsContainer, specific=dbl_Variable)
gen_dbl_Parameter_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Parameter)
gen_dbl_NamedElement_ExpandableElement = Generalization(general=ExpandableElement, specific=dbl_NamedElement)
gen_dbl_Statement_Construct = Generalization(general=Construct, specific=dbl_Statement)
gen_dbl_CompositeStatement_Statement = Generalization(general=Statement, specific=dbl_CompositeStatement)
gen_dbl_SimpleStatement_Statement = Generalization(general=Statement, specific=dbl_SimpleStatement)
gen_dbl_ExpressionStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ExpressionStatement)
gen_dbl_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Assignment)
gen_dbl_CodeBlock_Construct = Generalization(general=Construct, specific=dbl_CodeBlock)
gen_dbl_DeprecatedProcedureCallStatement_ExpressionStatement = Generalization(general=ExpressionStatement, specific=dbl_DeprecatedProcedureCallStatement)
gen_dbl_ProcedureCall_StatementExpression = Generalization(general=StatementExpression, specific=dbl_ProcedureCall)
gen_dbl_Return_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Return)
gen_dbl_WaitUntil_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_WaitUntil)
gen_dbl_Terminate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Terminate)
gen_dbl_Wait_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Wait)
gen_dbl_Reactivate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Reactivate)
gen_dbl_ActivateObject_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ActivateObject)
gen_dbl_Advance_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Advance)
gen_dbl_Print_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Print)
gen_dbl_SetStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SetStatement)
gen_dbl_RemoveFromSet_SetStatement = Generalization(general=SetStatement, specific=dbl_RemoveFromSet)
gen_dbl_AddToSet_SetStatement = Generalization(general=SetStatement, specific=dbl_AddToSet)
gen_dbl_EmptySet_SetStatement = Generalization(general=SetStatement, specific=dbl_EmptySet)
gen_dbl_IfStatement_CompositeStatement = Generalization(general=CompositeStatement, specific=dbl_IfStatement)
gen_dbl_WhileStatement_CompositeStatement = Generalization(general=CompositeStatement, specific=dbl_WhileStatement)
gen_dbl_BreakStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_BreakStatement)
gen_dbl_ContinueStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ContinueStatement)
gen_dbl_ForEachStatement_CompositeStatement = Generalization(general=CompositeStatement, specific=dbl_ForEachStatement)
gen_dbl_Expression_Construct = Generalization(general=Construct, specific=dbl_Expression)
gen_dbl_L1Expr_Expression = Generalization(general=Expression, specific=dbl_L1Expr)
gen_dbl_BinaryOperator_Expression = Generalization(general=Expression, specific=dbl_BinaryOperator)
gen_dbl_UnaryOperator_Expression = Generalization(general=Expression, specific=dbl_UnaryOperator)
gen_dbl_And_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_And)
gen_dbl_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Or)
gen_dbl_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Greater)
gen_dbl_GreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_GreaterEqual)
gen_dbl_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Less)
gen_dbl_LessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_LessEqual)
gen_dbl_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_NotEqual)
gen_dbl_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Equal)
gen_dbl_InstanceOf_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_InstanceOf)
gen_dbl_Plus_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Plus)
gen_dbl_Minus_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Minus)
gen_dbl_Mul_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Mul)
gen_dbl_Mod_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Mod)
gen_dbl_Div_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Div)
gen_dbl_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Not)
gen_dbl_Cast_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Cast)
gen_dbl_Cast_TypedElement = Generalization(general=TypedElement, specific=dbl_Cast)
gen_dbl_CreateObject_L1Expr = Generalization(general=L1Expr, specific=dbl_CreateObject)
gen_dbl_CreateObject_TypedElement = Generalization(general=TypedElement, specific=dbl_CreateObject)
gen_dbl_NullLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_NullLiteral)
gen_dbl_TimeLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_TimeLiteral)
gen_dbl_ActiveLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_ActiveLiteral)
gen_dbl_StringLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_StringLiteral)
gen_dbl_IntLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_IntLiteral)
gen_dbl_TrueLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_TrueLiteral)
gen_dbl_FalseLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_FalseLiteral)
gen_dbl_DoubleLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_DoubleLiteral)
gen_dbl_EvalExpr_Expression = Generalization(general=Expression, specific=dbl_EvalExpr)
gen_dbl_Neg_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Neg)
gen_dbl_MeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MeLiteral)
gen_dbl_SuperLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SuperLiteral)
gen_dbl_MetaLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MetaLiteral)
gen_dbl_TypeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_TypeLiteral)
gen_dbl_SetOp_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SetOp)
gen_dbl_SizeOfSet_SetOp = Generalization(general=SetOp, specific=dbl_SizeOfSet)
gen_dbl_FirstInSet_SetOp = Generalization(general=SetOp, specific=dbl_FirstInSet)
gen_dbl_LastInSet_SetOp = Generalization(general=SetOp, specific=dbl_LastInSet)
gen_dbl_Contains_SetOp = Generalization(general=SetOp, specific=dbl_Contains)
gen_dbl_IndexOf_SetOp = Generalization(general=SetOp, specific=dbl_IndexOf)
gen_dbl_ObjectAt_SetOp = Generalization(general=SetOp, specific=dbl_ObjectAt)
gen_dbl_BeforeInSet_SetOp = Generalization(general=SetOp, specific=dbl_BeforeInSet)
gen_dbl_AfterInSet_SetOp = Generalization(general=SetOp, specific=dbl_AfterInSet)
gen_dbl_IdExpr_L1Expr = Generalization(general=L1Expr, specific=dbl_IdExpr)
gen_dbl_ElementAccess_Expression = Generalization(general=Expression, specific=dbl_ElementAccess)
gen_dbl_VariableAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_VariableAccess)
gen_dbl_VariableAccess_ExpandableElement = Generalization(general=ExpandableElement, specific=dbl_VariableAccess)
gen_dbl_MetaAccess_VariableAccess = Generalization(general=VariableAccess, specific=dbl_MetaAccess)
gen_dbl_TypeAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_TypeAccess)
gen_dbl_TypeAccess_ExpandableElement = Generalization(general=ExpandableElement, specific=dbl_TypeAccess)
gen_dbl_NamedExtension_Extension = Generalization(general=Extension, specific=dbl_NamedExtension)
gen_dbl_NamedExtension_NamedElement = Generalization(general=NamedElement, specific=dbl_NamedExtension)
gen_dbl_ClassContentExtension_NamedExtension = Generalization(general=NamedExtension, specific=dbl_ClassContentExtension)
gen_dbl_ReferableRhsType_NamedElement = Generalization(general=NamedElement, specific=dbl_ReferableRhsType)
gen_dbl_TsRule_NamedElement = Generalization(general=NamedElement, specific=dbl_TsRule)
gen_dbl_TsRule_ReferableRhsType = Generalization(general=ReferableRhsType, specific=dbl_TsRule)
gen_dbl_ExtensionRule_NamedElement = Generalization(general=NamedElement, specific=dbl_ExtensionRule)
gen_dbl_ModuleContentExtension_NamedExtension = Generalization(general=NamedExtension, specific=dbl_ModuleContentExtension)
gen_dbl_ExtensionDefinition_NamedElement = Generalization(general=NamedElement, specific=dbl_ExtensionDefinition)
gen_dbl_SequenceExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_SequenceExpr)
gen_dbl_OptionalExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_OptionalExpr)
gen_dbl_RuntimeExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_RuntimeExpr)
gen_dbl_AtLeastOneExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_AtLeastOneExpr)
gen_dbl_ArbitraryExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_ArbitraryExpr)
gen_dbl_AlternativeExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_AlternativeExpr)
gen_dbl_TerminalExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_TerminalExpr)
gen_dbl_PropertyBindingExpr_NamedElement = Generalization(general=NamedElement, specific=dbl_PropertyBindingExpr)
gen_dbl_PropertyBindingExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_PropertyBindingExpr)
gen_dbl_RuleExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_RuleExpr)
gen_dbl_IdPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_IdPropertyType)
gen_dbl_IntPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_IntPropertyType)
gen_dbl_StringPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_StringPropertyType)
gen_dbl_BooleanPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_BooleanPropertyType)
gen_dbl_StructuredPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_StructuredPropertyType)
gen_dbl_CompositePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=dbl_CompositePropertyType)
gen_dbl_ReferencePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=dbl_ReferencePropertyType)
gen_dbl_Mapping_CodeBlock = Generalization(general=CodeBlock, specific=dbl_Mapping)
gen_dbl_MetaExpr_Expression = Generalization(general=Expression, specific=dbl_MetaExpr)
gen_dbl_TargetStatement_Statement = Generalization(general=Statement, specific=dbl_TargetStatement)
gen_dbl_MappingStatement_Statement = Generalization(general=Statement, specific=dbl_MappingStatement)
gen_dbl_SetGenContextStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SetGenContextStatement)
gen_dbl_ResetGenContextStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ResetGenContextStatement)
gen_dbl_SaveGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SaveGenStatement)
gen_dbl_ResumeGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ResumeGenStatement)
gen_dbl_FixedMappingPart_MappingPart = Generalization(general=MappingPart, specific=dbl_FixedMappingPart)
gen_dbl_DynamicMappingPart_MappingPart = Generalization(general=MappingPart, specific=dbl_DynamicMappingPart)
gen_dbl_ExpandExpression_StatementExpression = Generalization(general=StatementExpression, specific=dbl_ExpandExpression)
gen_dbl_ExpandExpression_Expression = Generalization(general=Expression, specific=dbl_ExpandExpression)
gen_dbl_ExpandStatement_Statement = Generalization(general=Statement, specific=dbl_ExpandStatement)
gen_dbl_ExpandSection_CompositeStatement = Generalization(general=CompositeStatement, specific=dbl_ExpandSection)
gen_dbl_CodeQuoteExpression_Expression = Generalization(general=Expression, specific=dbl_CodeQuoteExpression)
gen_dbl_QuotedExpression_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedExpression)
gen_dbl_QuotedStatements_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedStatements)
gen_dbl_QuotedClassContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedClassContent)
gen_dbl_QuotedClassContent_ClassSimilar = Generalization(general=ClassSimilar, specific=dbl_QuotedClassContent)
gen_dbl_TestStatement_Statement = Generalization(general=Statement, specific=dbl_TestStatement)
gen_dbl_Pattern_NamedElement = Generalization(general=NamedElement, specific=dbl_Pattern)
gen_dbl_PotentiallyHiddenIdElements_Statement = Generalization(general=Statement, specific=dbl_PotentiallyHiddenIdElements)
gen_dbl_FindContainer_Statement = Generalization(general=Statement, specific=dbl_FindContainer)
gen_dbl_ConsiderIdElements_Statement = Generalization(general=Statement, specific=dbl_ConsiderIdElements)
gen_dbl_IncludePattern_Statement = Generalization(general=Statement, specific=dbl_IncludePattern)
gen_dbl_QuotedModuleContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedModuleContent)
gen_dbl_QuotedModuleContent_Module = Generalization(general=Module, specific=dbl_QuotedModuleContent)

# Domain Model
domain_model = DomainModel(
    name="dbl",
    types={dbl_Model, dbl_Import, dbl_Module, NamedElement, EmbeddableExtensionsContainer, dbl_Classifier, dbl_ClassAugment, dbl_ExtensionDefinition, dbl_Annotation, dbl_Procedure, dbl_Variable, dbl_Construct, NamedExtension, dbl_ModifierExtensionsContainer, dbl_Type, dbl_TypedElement, dbl_PrimitiveType, dbl_IdExpr, Type, dbl_VoidType, PrimitiveType, dbl_IntType, dbl_BoolType, dbl_DoubleType, dbl_StringType, TypedElement, CodeBlock, AnnotatableElement, dbl_Parameter, dbl_SimpleAnnotation, dbl_AnnotationApplication, dbl_KeyValuePair, dbl_VariableAccess, dbl_IdResolution, dbl_EmbeddableExtensionsContainer, dbl_Extension, ReferableRhsType, dbl_NativeBinding, dbl_ClassSimilar, ModifierExtensionsContainer, dbl_Clazz, dbl_Interface, dbl_StartCodeBlock, dbl_Expression, dbl_AnnotatableElement, Classifier, ClassSimilar, dbl_Constructor, dbl_AbstractVariable, AbstractVariable, Statement, dbl_NamedElement, ExpandableElement, dbl_Statement, dbl_CompositeStatement, dbl_SimpleStatement, dbl_ExpressionStatement, SimpleStatement, dbl_StatementExpression, dbl_Assignment, dbl_CodeBlock, Construct, dbl_DeprecatedProcedureCallStatement, ExpressionStatement, dbl_ProcedureCall, StatementExpression, dbl_Return, dbl_WaitUntil, dbl_Terminate, dbl_Wait, dbl_Reactivate, dbl_ActivateObject, dbl_Advance, dbl_Print, dbl_SetStatement, dbl_RemoveFromSet, SetStatement, dbl_AddToSet, dbl_EmptySet, dbl_IfStatement, CompositeStatement, dbl_WhileStatement, dbl_BreakStatement, dbl_ContinueStatement, dbl_ForEachStatement, dbl_L1Expr, Expression, dbl_BinaryOperator, dbl_UnaryOperator, dbl_And, BinaryOperator, dbl_Or, dbl_Greater, dbl_GreaterEqual, dbl_Less, dbl_LessEqual, dbl_NotEqual, dbl_Equal, dbl_InstanceOf, dbl_Plus, dbl_Minus, dbl_Mul, dbl_Mod, dbl_Div, dbl_Not, dbl_Cast, dbl_CreateObject, L1Expr, dbl_NullLiteral, dbl_TimeLiteral, dbl_ActiveLiteral, dbl_StringLiteral, dbl_IntLiteral, dbl_TrueLiteral, dbl_FalseLiteral, dbl_DoubleLiteral, dbl_EvalExpr, dbl_Neg, UnaryOperator, dbl_MeLiteral, PredefinedId, dbl_SuperLiteral, dbl_MetaLiteral, dbl_TypeLiteral, dbl_SetOp, dbl_SizeOfSet, SetOp, dbl_FirstInSet, dbl_LastInSet, dbl_Contains, dbl_IndexOf, dbl_ObjectAt, dbl_BeforeInSet, dbl_AfterInSet, dbl_DepIdentifiableElement, dbl_PredefinedId, dbl_ArgumentExpression, dbl_ElementAccess, ElementAccess, dbl_MetaAccess, VariableAccess, dbl_TypeAccess, dbl_NamedExtension, Extension, dbl_ClassContentExtension, dbl_TextualSyntaxDef, dbl_Mapping, dbl_ExtensionRule, dbl_TsRule, dbl_ReferableRhsType, dbl_RhsExpression, dbl_RuleExpr, dbl_ModuleContentExtension, dbl_OptionalExpr, dbl_RuntimeExpr, dbl_AtLeastOneExpr, dbl_ArbitraryExpr, dbl_AlternativeExpr, dbl_TerminalExpr, dbl_PropertyBindingExpr, dbl_SequenceExpr, RhsExpression, dbl_IdPropertyType, PropertyType, dbl_IntPropertyType, dbl_StringPropertyType, dbl_BooleanPropertyType, dbl_StructuredPropertyType, dbl_CompositePropertyType, StructuredPropertyType, dbl_ReferencePropertyType, dbl_Pattern, dbl_MappingPart, dbl_PropertyType, dbl_MetaExpr, dbl_TargetStatement, dbl_MappingStatement, dbl_SetGenContextStatement, dbl_ResetGenContextStatement, dbl_SaveGenStatement, dbl_ResumeGenStatement, dbl_FixedMappingPart, MappingPart, dbl_DynamicMappingPart, dbl_ExpandStatement, dbl_ExpandSection, dbl_CodeQuoteExpression, dbl_QuotedCode, dbl_QuotedExpression, QuotedCode, dbl_QuotedStatements, dbl_QuotedClassContent, dbl_ExpandExpression, dbl_TestStatement, dbl_PotentiallyHiddenIdElements, dbl_FindContainer, dbl_ConsiderIdElements, dbl_IncludePattern, dbl_QuotedModuleContent, Module, dbl_ExpandableElement, BindingExprOpKind},
    associations={imports0, modules1, model3, classifiers6, classAugments8, extensionDefs10, annotationDefs12, procedures14, variables16, extensions20, modifierExtensions21, primitiveType23, classifierTypeExpr24, parameters26, keys28, annotationDef31, keyValuePairs33, key35, idRes18, annotationApplications39, simpleAnnotations41, bindings43, attributes45, methods47, superClass50, implementedInterfaces52, initialBlock54, finalBlock56, actionsBlock59, reportBlock62, clearBlock65, value37, constructor68, parameters73, augmentedClass76, methods79, superInterfaces83, initialValue85, baseConstructorArguments70, statements88, expression89, value92, procedureCall95, procedureAccess97, value99, condition101, objectAccess103, objectAccess105, time107, outputs109, object111, set113, atIndex116, variable90, elifCondition123, elifCaseBlock126, elseCaseBlock129, condition132, whileBlock134, iteratorVariableDefinition137, iteratorVariableReference139, iterableExpression142, forBlock145, op1148, condition118, ifCaseBlock120, op153, op2150, set157, expr155, referencedElement162, predefinedId164, arguments166, arguments168, idExpr171, parentIdExpr160, abstractSyntaxDef173, textualSyntaxDef176, mappingDef178, extensionRule180, newRules182, rhs184, instantiableMetaClass186, firstNewRule189, sequence191, expression193, expression195, expression197, expression199, left201, right203, rule207, type210, idResolutionPattern211, parts212, propertyType206, expr217, codeBlock219, parts221, exprs223, context226, variable228, variable230, metaObject214, metaObject234, metaObject236, location238, codeBlock241, quotedCode243, expression244, statements246, expr232, patterns250, context253, codeBlock256, codeBlock259, variableBinding261, containerBlock263, elseBlock266, elementsQuery269, pattern271, context273, expandExpression248},
    generalizations={gen_dbl_Module_NamedElement, gen_dbl_Module_EmbeddableExtensionsContainer, gen_dbl_Construct_NamedExtension, gen_dbl_PrimitiveType_Type, gen_dbl_VoidType_PrimitiveType, gen_dbl_IntType_PrimitiveType, gen_dbl_BoolType_PrimitiveType, gen_dbl_DoubleType_PrimitiveType, gen_dbl_StringType_PrimitiveType, gen_dbl_Procedure_NamedElement, gen_dbl_Procedure_TypedElement, gen_dbl_Procedure_CodeBlock, gen_dbl_Procedure_AnnotatableElement, gen_dbl_SimpleAnnotation_NamedElement, gen_dbl_Annotation_NamedElement, gen_dbl_Classifier_Type, gen_dbl_Classifier_NamedElement, gen_dbl_Classifier_ReferableRhsType, gen_dbl_ClassSimilar_EmbeddableExtensionsContainer, gen_dbl_ClassSimilar_ModifierExtensionsContainer, gen_dbl_StartCodeBlock_CodeBlock, gen_dbl_Clazz_Classifier, gen_dbl_Clazz_ClassSimilar, gen_dbl_ClassAugment_ClassSimilar, gen_dbl_Interface_Classifier, gen_dbl_AbstractVariable_NamedElement, gen_dbl_AbstractVariable_TypedElement, gen_dbl_Variable_AbstractVariable, gen_dbl_Variable_Statement, gen_dbl_Variable_ModifierExtensionsContainer, gen_dbl_Parameter_AbstractVariable, gen_dbl_NamedElement_ExpandableElement, gen_dbl_Statement_Construct, gen_dbl_CompositeStatement_Statement, gen_dbl_SimpleStatement_Statement, gen_dbl_ExpressionStatement_SimpleStatement, gen_dbl_Assignment_SimpleStatement, gen_dbl_CodeBlock_Construct, gen_dbl_DeprecatedProcedureCallStatement_ExpressionStatement, gen_dbl_ProcedureCall_StatementExpression, gen_dbl_Return_SimpleStatement, gen_dbl_WaitUntil_SimpleStatement, gen_dbl_Terminate_SimpleStatement, gen_dbl_Wait_SimpleStatement, gen_dbl_Reactivate_SimpleStatement, gen_dbl_ActivateObject_SimpleStatement, gen_dbl_Advance_SimpleStatement, gen_dbl_Print_SimpleStatement, gen_dbl_SetStatement_SimpleStatement, gen_dbl_RemoveFromSet_SetStatement, gen_dbl_AddToSet_SetStatement, gen_dbl_EmptySet_SetStatement, gen_dbl_IfStatement_CompositeStatement, gen_dbl_WhileStatement_CompositeStatement, gen_dbl_BreakStatement_SimpleStatement, gen_dbl_ContinueStatement_SimpleStatement, gen_dbl_ForEachStatement_CompositeStatement, gen_dbl_Expression_Construct, gen_dbl_L1Expr_Expression, gen_dbl_BinaryOperator_Expression, gen_dbl_UnaryOperator_Expression, gen_dbl_And_BinaryOperator, gen_dbl_Or_BinaryOperator, gen_dbl_Greater_BinaryOperator, gen_dbl_GreaterEqual_BinaryOperator, gen_dbl_Less_BinaryOperator, gen_dbl_LessEqual_BinaryOperator, gen_dbl_NotEqual_BinaryOperator, gen_dbl_Equal_BinaryOperator, gen_dbl_InstanceOf_BinaryOperator, gen_dbl_Plus_BinaryOperator, gen_dbl_Minus_BinaryOperator, gen_dbl_Mul_BinaryOperator, gen_dbl_Mod_BinaryOperator, gen_dbl_Div_BinaryOperator, gen_dbl_Not_UnaryOperator, gen_dbl_Cast_UnaryOperator, gen_dbl_Cast_TypedElement, gen_dbl_CreateObject_L1Expr, gen_dbl_CreateObject_TypedElement, gen_dbl_NullLiteral_L1Expr, gen_dbl_TimeLiteral_L1Expr, gen_dbl_ActiveLiteral_L1Expr, gen_dbl_StringLiteral_L1Expr, gen_dbl_IntLiteral_L1Expr, gen_dbl_TrueLiteral_L1Expr, gen_dbl_FalseLiteral_L1Expr, gen_dbl_DoubleLiteral_L1Expr, gen_dbl_EvalExpr_Expression, gen_dbl_Neg_UnaryOperator, gen_dbl_MeLiteral_PredefinedId, gen_dbl_SuperLiteral_PredefinedId, gen_dbl_MetaLiteral_PredefinedId, gen_dbl_TypeLiteral_PredefinedId, gen_dbl_SetOp_PredefinedId, gen_dbl_SizeOfSet_SetOp, gen_dbl_FirstInSet_SetOp, gen_dbl_LastInSet_SetOp, gen_dbl_Contains_SetOp, gen_dbl_IndexOf_SetOp, gen_dbl_ObjectAt_SetOp, gen_dbl_BeforeInSet_SetOp, gen_dbl_AfterInSet_SetOp, gen_dbl_IdExpr_L1Expr, gen_dbl_ElementAccess_Expression, gen_dbl_VariableAccess_ElementAccess, gen_dbl_VariableAccess_ExpandableElement, gen_dbl_MetaAccess_VariableAccess, gen_dbl_TypeAccess_ElementAccess, gen_dbl_TypeAccess_ExpandableElement, gen_dbl_NamedExtension_Extension, gen_dbl_NamedExtension_NamedElement, gen_dbl_ClassContentExtension_NamedExtension, gen_dbl_ReferableRhsType_NamedElement, gen_dbl_TsRule_NamedElement, gen_dbl_TsRule_ReferableRhsType, gen_dbl_ExtensionRule_NamedElement, gen_dbl_ModuleContentExtension_NamedExtension, gen_dbl_ExtensionDefinition_NamedElement, gen_dbl_SequenceExpr_RhsExpression, gen_dbl_OptionalExpr_RhsExpression, gen_dbl_RuntimeExpr_RhsExpression, gen_dbl_AtLeastOneExpr_RhsExpression, gen_dbl_ArbitraryExpr_RhsExpression, gen_dbl_AlternativeExpr_RhsExpression, gen_dbl_TerminalExpr_RhsExpression, gen_dbl_PropertyBindingExpr_NamedElement, gen_dbl_PropertyBindingExpr_RhsExpression, gen_dbl_RuleExpr_RhsExpression, gen_dbl_IdPropertyType_PropertyType, gen_dbl_IntPropertyType_PropertyType, gen_dbl_StringPropertyType_PropertyType, gen_dbl_BooleanPropertyType_PropertyType, gen_dbl_StructuredPropertyType_PropertyType, gen_dbl_CompositePropertyType_StructuredPropertyType, gen_dbl_ReferencePropertyType_StructuredPropertyType, gen_dbl_Mapping_CodeBlock, gen_dbl_MetaExpr_Expression, gen_dbl_TargetStatement_Statement, gen_dbl_MappingStatement_Statement, gen_dbl_SetGenContextStatement_SimpleStatement, gen_dbl_ResetGenContextStatement_SimpleStatement, gen_dbl_SaveGenStatement_SimpleStatement, gen_dbl_ResumeGenStatement_SimpleStatement, gen_dbl_FixedMappingPart_MappingPart, gen_dbl_DynamicMappingPart_MappingPart, gen_dbl_ExpandExpression_StatementExpression, gen_dbl_ExpandExpression_Expression, gen_dbl_ExpandStatement_Statement, gen_dbl_ExpandSection_CompositeStatement, gen_dbl_CodeQuoteExpression_Expression, gen_dbl_QuotedExpression_QuotedCode, gen_dbl_QuotedStatements_QuotedCode, gen_dbl_QuotedClassContent_QuotedCode, gen_dbl_QuotedClassContent_ClassSimilar, gen_dbl_TestStatement_Statement, gen_dbl_Pattern_NamedElement, gen_dbl_PotentiallyHiddenIdElements_Statement, gen_dbl_FindContainer_Statement, gen_dbl_ConsiderIdElements_Statement, gen_dbl_IncludePattern_Statement, gen_dbl_QuotedModuleContent_QuotedCode, gen_dbl_QuotedModuleContent_Module},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)