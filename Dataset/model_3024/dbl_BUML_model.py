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
dbl_Module = Class(name="dbl::Module")
EmbeddableExtensionsContainer = Class(name="EmbeddableExtensionsContainer")
dbl_Classifier = Class(name="dbl::Classifier", is_abstract=True)
dbl_ClassAugment = Class(name="dbl::ClassAugment")
dbl_ExtensionDefinition = Class(name="dbl::ExtensionDefinition")
dbl_Procedure = Class(name="dbl::Procedure")
dbl_Variable = Class(name="dbl::Variable")
dbl_Construct = Class(name="dbl::Construct")
dbl_ExpandExpr = Class(name="dbl::ExpandExpr")
dbl_ExtensibleElement = Class(name="dbl::ExtensibleElement")
NamedElement = Class(name="NamedElement")
Construct = Class(name="Construct")
dbl_Model = Class(name="dbl::Model")
dbl_Import = Class(name="dbl::Import")
dbl_BoolType = Class(name="dbl::BoolType")
dbl_DoubleType = Class(name="dbl::DoubleType")
dbl_StringType = Class(name="dbl::StringType")
TypedElement = Class(name="TypedElement")
LocalScope = Class(name="LocalScope")
dbl_Parameter = Class(name="dbl::Parameter")
dbl_NativeBinding = Class(name="dbl::NativeBinding")
dbl_ClassSimilar = Class(name="dbl::ClassSimilar", is_abstract=True)
ModifierExtensionsContainer = Class(name="ModifierExtensionsContainer")
dbl_EmbeddableExtensionsContainer = Class(name="dbl::EmbeddableExtensionsContainer", is_abstract=True)
dbl_ModifierExtensionsContainer = Class(name="dbl::ModifierExtensionsContainer", is_abstract=True)
dbl_Type = Class(name="dbl::Type", is_abstract=True)
dbl_ArrayDimension = Class(name="dbl::ArrayDimension")
dbl_TypedElement = Class(name="dbl::TypedElement", is_abstract=True)
dbl_PrimitiveType = Class(name="dbl::PrimitiveType", is_abstract=True)
dbl_IdExpr = Class(name="dbl::IdExpr")
dbl_Expression = Class(name="dbl::Expression")
Type = Class(name="Type")
dbl_VoidType = Class(name="dbl::VoidType")
PrimitiveType = Class(name="PrimitiveType")
dbl_IntType = Class(name="dbl::IntType")
dbl_Clazz = Class(name="dbl::Clazz")
dbl_SuperClassSpecification = Class(name="dbl::SuperClassSpecification")
dbl_ClassPart = Class(name="dbl::ClassPart")
dbl_NamedElement = Class(name="dbl::NamedElement")
dbl_Statement = Class(name="dbl::Statement")
ExtensibleElement = Class(name="ExtensibleElement")
dbl_LoopStatement = Class(name="dbl::LoopStatement")
Statement = Class(name="Statement")
dbl_SimpleStatement = Class(name="dbl::SimpleStatement")
dbl_Assignment = Class(name="dbl::Assignment")
dbl_VariableAccess = Class(name="dbl::VariableAccess")
dbl_ProcedureCall = Class(name="dbl::ProcedureCall")
dbl_Return = Class(name="dbl::Return")
Classifier = Class(name="Classifier")
ClassSimilar = Class(name="ClassSimilar")
LanguageConceptClassifier = Class(name="LanguageConceptClassifier")
dbl_Constructor = Class(name="dbl::Constructor")
dbl_AbstractVariable = Class(name="dbl::AbstractVariable", is_abstract=True)
AbstractVariable = Class(name="AbstractVariable")
SimpleStatement = Class(name="SimpleStatement")
dbl_IfStatement = Class(name="dbl::IfStatement")
dbl_LocalScope = Class(name="dbl::LocalScope")
dbl_LocalScopeStatement = Class(name="dbl::LocalScopeStatement")
dbl_ForStatement = Class(name="dbl::ForStatement")
LoopStatement = Class(name="LoopStatement")
dbl_WaitUntil = Class(name="dbl::WaitUntil")
dbl_Terminate = Class(name="dbl::Terminate")
dbl_Yield = Class(name="dbl::Yield")
dbl_Wait = Class(name="dbl::Wait")
dbl_Reactivate = Class(name="dbl::Reactivate")
dbl_ActivateObject = Class(name="dbl::ActivateObject")
dbl_Advance = Class(name="dbl::Advance")
dbl_Print = Class(name="dbl::Print")
dbl_L3Expr = Class(name="dbl::L3Expr")
dbl_L4Expr = Class(name="dbl::L4Expr")
dbl_L5Expr = Class(name="dbl::L5Expr")
dbl_L6Expr = Class(name="dbl::L6Expr")
dbl_L7Expr = Class(name="dbl::L7Expr")
dbl_L8Expr = Class(name="dbl::L8Expr")
dbl_L9Expr = Class(name="dbl::L9Expr")
dbl_BinaryOperator = Class(name="dbl::BinaryOperator", is_abstract=True)
dbl_UnaryOperator = Class(name="dbl::UnaryOperator", is_abstract=True)
dbl_Or = Class(name="dbl::Or")
BinaryOperator = Class(name="BinaryOperator")
dbl_WhileStatement = Class(name="dbl::WhileStatement")
dbl_SwitchStatement = Class(name="dbl::SwitchStatement")
dbl_SwitchCase = Class(name="dbl::SwitchCase")
dbl_BreakStatement = Class(name="dbl::BreakStatement")
dbl_ContinueStatement = Class(name="dbl::ContinueStatement")
dbl_L1Expr = Class(name="dbl::L1Expr")
Expression = Class(name="Expression")
dbl_L2Expr = Class(name="dbl::L2Expr")
L8Expr = Class(name="L8Expr")
dbl_And = Class(name="dbl::And")
L7Expr = Class(name="L7Expr")
dbl_NotEqual = Class(name="dbl::NotEqual")
dbl_Not = Class(name="dbl::Not")
L6Expr = Class(name="L6Expr")
dbl_Equal = Class(name="dbl::Equal")
dbl_Cast = Class(name="dbl::Cast")
dbl_Greater = Class(name="dbl::Greater")
L5Expr = Class(name="L5Expr")
dbl_CreateObject = Class(name="dbl::CreateObject")
L1Expr = Class(name="L1Expr")
dbl_GreaterEqual = Class(name="dbl::GreaterEqual")
dbl_NullLiteral = Class(name="dbl::NullLiteral")
dbl_Less = Class(name="dbl::Less")
dbl_TimeLiteral = Class(name="dbl::TimeLiteral")
dbl_ActiveLiteral = Class(name="dbl::ActiveLiteral")
dbl_LessEqual = Class(name="dbl::LessEqual")
dbl_StringLiteral = Class(name="dbl::StringLiteral")
dbl_InstanceOf = Class(name="dbl::InstanceOf")
dbl_Plus = Class(name="dbl::Plus")
dbl_IntLiteral = Class(name="dbl::IntLiteral")
L4Expr = Class(name="L4Expr")
dbl_Minus = Class(name="dbl::Minus")
dbl_TrueLiteral = Class(name="dbl::TrueLiteral")
dbl_Mul = Class(name="dbl::Mul")
dbl_FalseLiteral = Class(name="dbl::FalseLiteral")
L3Expr = Class(name="L3Expr")
dbl_DoubleLiteral = Class(name="dbl::DoubleLiteral")
dbl_Mod = Class(name="dbl::Mod")
dbl_Div = Class(name="dbl::Div")
dbl_Neg = Class(name="dbl::Neg")
UnaryOperator = Class(name="UnaryOperator")
dbl_ParseExpr = Class(name="dbl::ParseExpr")
dbl_PredefinedId = Class(name="dbl::PredefinedId")
dbl_MeLiteral = Class(name="dbl::MeLiteral")
PredefinedId = Class(name="PredefinedId")
dbl_SuperLiteral = Class(name="dbl::SuperLiteral")
dbl_MetaLiteral = Class(name="dbl::MetaLiteral")
dbl_TypeLiteral = Class(name="dbl::TypeLiteral")
dbl_SizeOfArray = Class(name="dbl::SizeOfArray")
dbl_CallPart = Class(name="dbl::CallPart")
L2Expr = Class(name="L2Expr")
dbl_ElementAccess = Class(name="dbl::ElementAccess", is_abstract=True)
ElementAccess = Class(name="ElementAccess")
dbl_MetaAccess = Class(name="dbl::MetaAccess")
VariableAccess = Class(name="VariableAccess")
dbl_TypeAccess = Class(name="dbl::TypeAccess")
dbl_ClassContentExtension = Class(name="dbl::ClassContentExtension")
dbl_ModuleContentExtension = Class(name="dbl::ModuleContentExtension")
dbl_LanguageConceptClassifier = Class(name="dbl::LanguageConceptClassifier", is_abstract=True)
dbl_TextualSyntaxDef = Class(name="dbl::TextualSyntaxDef")
dbl_Mapping = Class(name="dbl::Mapping")
dbl_TsRule = Class(name="dbl::TsRule")
dbl_LanguageConstructClassifier = Class(name="dbl::LanguageConstructClassifier", is_abstract=True)
LanguageConstructClassifier = Class(name="LanguageConstructClassifier")
dbl_RhsExpression = Class(name="dbl::RhsExpression")
dbl_L3RhsExpr = Class(name="dbl::L3RhsExpr")
RhsExpression = Class(name="RhsExpression")
dbl_L2RhsExpr = Class(name="dbl::L2RhsExpr")
dbl_SequenceExpr = Class(name="dbl::SequenceExpr")
L2RhsExpr = Class(name="L2RhsExpr")
dbl_L1RhsExpr = Class(name="dbl::L1RhsExpr")
dbl_TerminalExpr = Class(name="dbl::TerminalExpr")
L1RhsExpr = Class(name="L1RhsExpr")
dbl_PropertyBindingExpr = Class(name="dbl::PropertyBindingExpr")
dbl_PropertyType = Class(name="dbl::PropertyType", is_abstract=True)
dbl_RhsClassifierExpr = Class(name="dbl::RhsClassifierExpr")
dbl_IdPropertyType = Class(name="dbl::IdPropertyType")
PropertyType = Class(name="PropertyType")
dbl_IntPropertyType = Class(name="dbl::IntPropertyType")
dbl_StringPropertyType = Class(name="dbl::StringPropertyType")
dbl_BooleanPropertyType = Class(name="dbl::BooleanPropertyType")
dbl_StructuredPropertyType = Class(name="dbl::StructuredPropertyType")
dbl_CompositePropertyType = Class(name="dbl::CompositePropertyType")
StructuredPropertyType = Class(name="StructuredPropertyType")
dbl_ExpandStatement = Class(name="dbl::ExpandStatement")
LocalScopeStatement = Class(name="LocalScopeStatement")
dbl_MappingPart = Class(name="dbl::MappingPart", is_abstract=True)
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
dbl_ExpandExpression = Class(name="dbl::ExpandExpression")
dbl_ReferencePropertyType = Class(name="dbl::ReferencePropertyType")
dbl_CodeQuoteExpression = Class(name="dbl::CodeQuoteExpression")
dbl_QuotedCode = Class(name="dbl::QuotedCode")
dbl_QuotedExpression = Class(name="dbl::QuotedExpression")
QuotedCode = Class(name="QuotedCode")
dbl_QuotedStatements = Class(name="dbl::QuotedStatements")
dbl_QuotedClassContent = Class(name="dbl::QuotedClassContent")
dbl_QuotedModuleContent = Class(name="dbl::QuotedModuleContent")
Module = Class(name="Module")
dbl_Pattern = Class(name="dbl::Pattern")
dbl_TestStatement = Class(name="dbl::TestStatement")

# dbl_Module class attributes and methods

# EmbeddableExtensionsContainer class attributes and methods

# dbl_Classifier class attributes and methods

# dbl_ClassAugment class attributes and methods

# dbl_ExtensionDefinition class attributes and methods

# dbl_Procedure class attributes and methods
dbl_Procedure_clazz: Property = Property(name="clazz", type=BooleanType)
dbl_Procedure_abstract: Property = Property(name="abstract", type=BooleanType)
dbl_Procedure.attributes={dbl_Procedure_clazz, dbl_Procedure_abstract}

# dbl_Variable class attributes and methods
dbl_Variable_control: Property = Property(name="control", type=BooleanType)
dbl_Variable_clazz: Property = Property(name="clazz", type=BooleanType)
dbl_Variable.attributes={dbl_Variable_clazz, dbl_Variable_control}

# dbl_Construct class attributes and methods

# dbl_ExpandExpr class attributes and methods

# dbl_ExtensibleElement class attributes and methods
dbl_ExtensibleElement_concreteSyntax: Property = Property(name="concreteSyntax", type=StringType)
dbl_ExtensibleElement_instanceOfExtensionDefinition: Property = Property(name="instanceOfExtensionDefinition", type=BooleanType)
dbl_ExtensibleElement.attributes={dbl_ExtensibleElement_instanceOfExtensionDefinition, dbl_ExtensibleElement_concreteSyntax}

# NamedElement class attributes and methods

# Construct class attributes and methods

# dbl_Model class attributes and methods

# dbl_Import class attributes and methods
dbl_Import_file: Property = Property(name="file", type=StringType)
dbl_Import.attributes={dbl_Import_file}

# dbl_BoolType class attributes and methods

# dbl_DoubleType class attributes and methods

# dbl_StringType class attributes and methods

# TypedElement class attributes and methods

# LocalScope class attributes and methods

# dbl_Parameter class attributes and methods

# dbl_NativeBinding class attributes and methods
dbl_NativeBinding_targetLanguage: Property = Property(name="targetLanguage", type=StringType)
dbl_NativeBinding_targetType: Property = Property(name="targetType", type=StringType)
dbl_NativeBinding.attributes={dbl_NativeBinding_targetType, dbl_NativeBinding_targetLanguage}

# dbl_ClassSimilar class attributes and methods

# ModifierExtensionsContainer class attributes and methods

# dbl_EmbeddableExtensionsContainer class attributes and methods

# dbl_ModifierExtensionsContainer class attributes and methods

# dbl_Type class attributes and methods

# dbl_ArrayDimension class attributes and methods

# dbl_TypedElement class attributes and methods

# dbl_PrimitiveType class attributes and methods

# dbl_IdExpr class attributes and methods

# dbl_Expression class attributes and methods

# Type class attributes and methods

# dbl_VoidType class attributes and methods

# PrimitiveType class attributes and methods

# dbl_IntType class attributes and methods

# dbl_Clazz class attributes and methods
dbl_Clazz_active: Property = Property(name="active", type=BooleanType)
dbl_Clazz.attributes={dbl_Clazz_active}

# dbl_SuperClassSpecification class attributes and methods

# dbl_ClassPart class attributes and methods

# dbl_NamedElement class attributes and methods
dbl_NamedElement_name: Property = Property(name="name", type=StringType)
dbl_NamedElement.attributes={dbl_NamedElement_name}

# dbl_Statement class attributes and methods

# ExtensibleElement class attributes and methods

# dbl_LoopStatement class attributes and methods

# Statement class attributes and methods

# dbl_SimpleStatement class attributes and methods

# dbl_Assignment class attributes and methods

# dbl_VariableAccess class attributes and methods

# dbl_ProcedureCall class attributes and methods

# dbl_Return class attributes and methods

# Classifier class attributes and methods

# ClassSimilar class attributes and methods

# LanguageConceptClassifier class attributes and methods

# dbl_Constructor class attributes and methods

# dbl_AbstractVariable class attributes and methods

# AbstractVariable class attributes and methods

# SimpleStatement class attributes and methods

# dbl_IfStatement class attributes and methods

# dbl_LocalScope class attributes and methods

# dbl_LocalScopeStatement class attributes and methods

# dbl_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# dbl_WaitUntil class attributes and methods

# dbl_Terminate class attributes and methods

# dbl_Yield class attributes and methods

# dbl_Wait class attributes and methods

# dbl_Reactivate class attributes and methods

# dbl_ActivateObject class attributes and methods
dbl_ActivateObject_priority: Property = Property(name="priority", type=IntegerType)
dbl_ActivateObject.attributes={dbl_ActivateObject_priority}

# dbl_Advance class attributes and methods

# dbl_Print class attributes and methods

# dbl_L3Expr class attributes and methods

# dbl_L4Expr class attributes and methods

# dbl_L5Expr class attributes and methods

# dbl_L6Expr class attributes and methods

# dbl_L7Expr class attributes and methods

# dbl_L8Expr class attributes and methods

# dbl_L9Expr class attributes and methods

# dbl_BinaryOperator class attributes and methods

# dbl_UnaryOperator class attributes and methods

# dbl_Or class attributes and methods

# BinaryOperator class attributes and methods

# dbl_WhileStatement class attributes and methods

# dbl_SwitchStatement class attributes and methods

# dbl_SwitchCase class attributes and methods

# dbl_BreakStatement class attributes and methods

# dbl_ContinueStatement class attributes and methods

# dbl_L1Expr class attributes and methods

# Expression class attributes and methods

# dbl_L2Expr class attributes and methods

# L8Expr class attributes and methods

# dbl_And class attributes and methods

# L7Expr class attributes and methods

# dbl_NotEqual class attributes and methods

# dbl_Not class attributes and methods

# L6Expr class attributes and methods

# dbl_Equal class attributes and methods

# dbl_Cast class attributes and methods

# dbl_Greater class attributes and methods

# L5Expr class attributes and methods

# dbl_CreateObject class attributes and methods

# L1Expr class attributes and methods

# dbl_GreaterEqual class attributes and methods

# dbl_NullLiteral class attributes and methods

# dbl_Less class attributes and methods

# dbl_TimeLiteral class attributes and methods

# dbl_ActiveLiteral class attributes and methods

# dbl_LessEqual class attributes and methods

# dbl_StringLiteral class attributes and methods
dbl_StringLiteral_value: Property = Property(name="value", type=StringType)
dbl_StringLiteral.attributes={dbl_StringLiteral_value}

# dbl_InstanceOf class attributes and methods

# dbl_Plus class attributes and methods

# dbl_IntLiteral class attributes and methods
dbl_IntLiteral_value: Property = Property(name="value", type=IntegerType)
dbl_IntLiteral.attributes={dbl_IntLiteral_value}

# L4Expr class attributes and methods

# dbl_Minus class attributes and methods

# dbl_TrueLiteral class attributes and methods

# dbl_Mul class attributes and methods

# dbl_FalseLiteral class attributes and methods

# L3Expr class attributes and methods

# dbl_DoubleLiteral class attributes and methods
dbl_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
dbl_DoubleLiteral.attributes={dbl_DoubleLiteral_value}

# dbl_Mod class attributes and methods

# dbl_Div class attributes and methods

# dbl_Neg class attributes and methods

# UnaryOperator class attributes and methods

# dbl_ParseExpr class attributes and methods

# dbl_PredefinedId class attributes and methods

# dbl_MeLiteral class attributes and methods

# PredefinedId class attributes and methods

# dbl_SuperLiteral class attributes and methods

# dbl_MetaLiteral class attributes and methods

# dbl_TypeLiteral class attributes and methods

# dbl_SizeOfArray class attributes and methods

# dbl_CallPart class attributes and methods

# L2Expr class attributes and methods

# dbl_ElementAccess class attributes and methods

# ElementAccess class attributes and methods

# dbl_MetaAccess class attributes and methods

# VariableAccess class attributes and methods

# dbl_TypeAccess class attributes and methods

# dbl_ClassContentExtension class attributes and methods

# dbl_ModuleContentExtension class attributes and methods

# dbl_LanguageConceptClassifier class attributes and methods

# dbl_TextualSyntaxDef class attributes and methods

# dbl_Mapping class attributes and methods

# dbl_TsRule class attributes and methods

# dbl_LanguageConstructClassifier class attributes and methods

# LanguageConstructClassifier class attributes and methods

# dbl_RhsExpression class attributes and methods

# dbl_L3RhsExpr class attributes and methods

# RhsExpression class attributes and methods

# dbl_L2RhsExpr class attributes and methods

# dbl_SequenceExpr class attributes and methods

# L2RhsExpr class attributes and methods

# dbl_L1RhsExpr class attributes and methods

# dbl_TerminalExpr class attributes and methods
dbl_TerminalExpr_terminal: Property = Property(name="terminal", type=StringType)
dbl_TerminalExpr.attributes={dbl_TerminalExpr_terminal}

# L1RhsExpr class attributes and methods

# dbl_PropertyBindingExpr class attributes and methods

# dbl_PropertyType class attributes and methods

# dbl_RhsClassifierExpr class attributes and methods

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

# dbl_ExpandStatement class attributes and methods

# LocalScopeStatement class attributes and methods

# dbl_MappingPart class attributes and methods

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

# dbl_ExpandExpression class attributes and methods

# dbl_ReferencePropertyType class attributes and methods
dbl_ReferencePropertyType_rawReference: Property = Property(name="rawReference", type=BooleanType)
dbl_ReferencePropertyType.attributes={dbl_ReferencePropertyType_rawReference}

# dbl_CodeQuoteExpression class attributes and methods

# dbl_QuotedCode class attributes and methods

# dbl_QuotedExpression class attributes and methods

# QuotedCode class attributes and methods

# dbl_QuotedStatements class attributes and methods

# dbl_QuotedClassContent class attributes and methods

# dbl_QuotedModuleContent class attributes and methods

# Module class attributes and methods

# dbl_Pattern class attributes and methods
dbl_Pattern_top: Property = Property(name="top", type=BooleanType)
dbl_Pattern.attributes={dbl_Pattern_top}

# dbl_TestStatement class attributes and methods
dbl_TestStatement_value: Property = Property(name="value", type=IntegerType)
dbl_TestStatement.attributes={dbl_TestStatement_value}

# Relationships
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="dbl_Import", type=dbl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Model", type=dbl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules2: BinaryAssociation = BinaryAssociation(
    name="modules2",
    ends={
        Property(name="dbl_Module", type=dbl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Model3", type=dbl_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model4: BinaryAssociation = BinaryAssociation(
    name="model4",
    ends={
        Property(name="dbl_Model6", type=dbl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Import5", type=dbl_Model, multiplicity=Multiplicity(0, 1))
    }
)
classifiers7: BinaryAssociation = BinaryAssociation(
    name="classifiers7",
    ends={
        Property(name="dbl_Classifier", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module8", type=dbl_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classAugments9: BinaryAssociation = BinaryAssociation(
    name="classAugments9",
    ends={
        Property(name="dbl_ClassAugment", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module10", type=dbl_ClassAugment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefs11: BinaryAssociation = BinaryAssociation(
    name="extensionDefs11",
    ends={
        Property(name="dbl_ExtensionDefinition", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module12", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures13: BinaryAssociation = BinaryAssociation(
    name="procedures13",
    ends={
        Property(name="dbl_Procedure", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module14", type=dbl_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expandExpr0: BinaryAssociation = BinaryAssociation(
    name="expandExpr0",
    ends={
        Property(name="dbl_ExpandExpr", type=dbl_Construct, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Construct", type=dbl_ExpandExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters29: BinaryAssociation = BinaryAssociation(
    name="parameters29",
    ends={
        Property(name="dbl_Parameter", type=dbl_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Procedure30", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes31: BinaryAssociation = BinaryAssociation(
    name="attributes31",
    ends={
        Property(name="dbl_Variable32", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables15: BinaryAssociation = BinaryAssociation(
    name="variables15",
    ends={
        Property(name="dbl_Variable", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module16", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions17: BinaryAssociation = BinaryAssociation(
    name="extensions17",
    ends={
        Property(name="dbl_ExtensibleElement", type=dbl_EmbeddableExtensionsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_EmbeddableExtensionsContainer", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modifierExtensions18: BinaryAssociation = BinaryAssociation(
    name="modifierExtensions18",
    ends={
        Property(name="dbl_ExtensibleElement19", type=dbl_ModifierExtensionsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ModifierExtensionsContainer", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayDimensions20: BinaryAssociation = BinaryAssociation(
    name="arrayDimensions20",
    ends={
        Property(name="dbl_ArrayDimension", type=dbl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Type", type=dbl_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveType21: BinaryAssociation = BinaryAssociation(
    name="primitiveType21",
    ends={
        Property(name="dbl_PrimitiveType", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement", type=dbl_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArrayDimensions22: BinaryAssociation = BinaryAssociation(
    name="typeArrayDimensions22",
    ends={
        Property(name="dbl_ArrayDimension24", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement23", type=dbl_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierType25: BinaryAssociation = BinaryAssociation(
    name="classifierType25",
    ends={
        Property(name="dbl_IdExpr", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement26", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size27: BinaryAssociation = BinaryAssociation(
    name="size27",
    ends={
        Property(name="dbl_Expression", type=dbl_ArrayDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ArrayDimension28", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finalBlock40: BinaryAssociation = BinaryAssociation(
    name="finalBlock40",
    ends={
        Property(name="dbl_ClassPart42", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar41", type=dbl_ClassPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionsBlock43: BinaryAssociation = BinaryAssociation(
    name="actionsBlock43",
    ends={
        Property(name="dbl_ClassPart45", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar44", type=dbl_ClassPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reportBlock46: BinaryAssociation = BinaryAssociation(
    name="reportBlock46",
    ends={
        Property(name="dbl_ClassPart48", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar47", type=dbl_ClassPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clearBlock49: BinaryAssociation = BinaryAssociation(
    name="clearBlock49",
    ends={
        Property(name="dbl_ClassPart51", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar50", type=dbl_ClassPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clazz52: BinaryAssociation = BinaryAssociation(
    name="clazz52",
    ends={
        Property(name="dbl_Clazz", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SuperClassSpecification53", type=dbl_Clazz, multiplicity=Multiplicity(1, 1))
    }
)
methods33: BinaryAssociation = BinaryAssociation(
    name="methods33",
    ends={
        Property(name="dbl_Procedure35", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar34", type=dbl_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClasses36: BinaryAssociation = BinaryAssociation(
    name="superClasses36",
    ends={
        Property(name="dbl_SuperClassSpecification", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar37", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialBlock38: BinaryAssociation = BinaryAssociation(
    name="initialBlock38",
    ends={
        Property(name="dbl_ClassPart", type=dbl_ClassSimilar, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassSimilar39", type=dbl_ClassPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue67: BinaryAssociation = BinaryAssociation(
    name="initialValue67",
    ends={
        Property(name="dbl_Expression69", type=dbl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Variable68", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable70: BinaryAssociation = BinaryAssociation(
    name="variable70",
    ends={
        Property(name="dbl_VariableAccess", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="dbl_Expression73", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment72", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callIdExpr74: BinaryAssociation = BinaryAssociation(
    name="callIdExpr74",
    ends={
        Property(name="dbl_IdExpr75", type=dbl_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ProcedureCall", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constructorArguments54: BinaryAssociation = BinaryAssociation(
    name="constructorArguments54",
    ends={
        Property(name="dbl_Expression56", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SuperClassSpecification55", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructor57: BinaryAssociation = BinaryAssociation(
    name="constructor57",
    ends={
        Property(name="dbl_Constructor", type=dbl_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Clazz58", type=dbl_Constructor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings59: BinaryAssociation = BinaryAssociation(
    name="bindings59",
    ends={
        Property(name="dbl_NativeBinding", type=dbl_Clazz, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Clazz60", type=dbl_NativeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters61: BinaryAssociation = BinaryAssociation(
    name="parameters61",
    ends={
        Property(name="dbl_Parameter63", type=dbl_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Constructor62", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
augmentedClass64: BinaryAssociation = BinaryAssociation(
    name="augmentedClass64",
    ends={
        Property(name="dbl_Clazz66", type=dbl_ClassAugment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ClassAugment65", type=dbl_Clazz, multiplicity=Multiplicity(1, 1))
    }
)
condition88: BinaryAssociation = BinaryAssociation(
    name="condition88",
    ends={
        Property(name="dbl_Expression89", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueCase90: BinaryAssociation = BinaryAssociation(
    name="trueCase90",
    ends={
        Property(name="dbl_Statement", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement91", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseCase92: BinaryAssociation = BinaryAssociation(
    name="falseCase92",
    ends={
        Property(name="dbl_Statement94", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement93", type=dbl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements95: BinaryAssociation = BinaryAssociation(
    name="statements95",
    ends={
        Property(name="dbl_Statement96", type=dbl_LocalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_LocalScope", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
termination97: BinaryAssociation = BinaryAssociation(
    name="termination97",
    ends={
        Property(name="dbl_Expression98", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
increment99: BinaryAssociation = BinaryAssociation(
    name="increment99",
    ends={
        Property(name="dbl_Assignment101", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement100", type=dbl_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body102: BinaryAssociation = BinaryAssociation(
    name="body102",
    ends={
        Property(name="dbl_Statement104", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement103", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value76: BinaryAssociation = BinaryAssociation(
    name="value76",
    ends={
        Property(name="dbl_Expression77", type=dbl_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Return", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition78: BinaryAssociation = BinaryAssociation(
    name="condition78",
    ends={
        Property(name="dbl_Expression79", type=dbl_WaitUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WaitUntil", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess80: BinaryAssociation = BinaryAssociation(
    name="objectAccess80",
    ends={
        Property(name="dbl_Expression81", type=dbl_Reactivate, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Reactivate", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess82: BinaryAssociation = BinaryAssociation(
    name="objectAccess82",
    ends={
        Property(name="dbl_Expression83", type=dbl_ActivateObject, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ActivateObject", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
time84: BinaryAssociation = BinaryAssociation(
    name="time84",
    ends={
        Property(name="dbl_Expression85", type=dbl_Advance, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Advance", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputs86: BinaryAssociation = BinaryAssociation(
    name="outputs86",
    ends={
        Property(name="dbl_Expression87", type=dbl_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Print", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op1123: BinaryAssociation = BinaryAssociation(
    name="op1123",
    ends={
        Property(name="dbl_Expression124", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op2125: BinaryAssociation = BinaryAssociation(
    name="op2125",
    ends={
        Property(name="dbl_Expression127", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator126", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op128: BinaryAssociation = BinaryAssociation(
    name="op128",
    ends={
        Property(name="dbl_Expression129", type=dbl_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_UnaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition105: BinaryAssociation = BinaryAssociation(
    name="condition105",
    ends={
        Property(name="dbl_Expression106", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body107: BinaryAssociation = BinaryAssociation(
    name="body107",
    ends={
        Property(name="dbl_Statement109", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement108", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable110: BinaryAssociation = BinaryAssociation(
    name="variable110",
    ends={
        Property(name="dbl_VariableAccess111", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases112: BinaryAssociation = BinaryAssociation(
    name="cases112",
    ends={
        Property(name="dbl_SwitchCase", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement113", type=dbl_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultCase114: BinaryAssociation = BinaryAssociation(
    name="defaultCase114",
    ends={
        Property(name="dbl_SwitchCase116", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement115", type=dbl_SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value117: BinaryAssociation = BinaryAssociation(
    name="value117",
    ends={
        Property(name="dbl_Expression119", type=dbl_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchCase118", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body120: BinaryAssociation = BinaryAssociation(
    name="body120",
    ends={
        Property(name="dbl_Statement122", type=dbl_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchCase121", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr130: BinaryAssociation = BinaryAssociation(
    name="expr130",
    ends={
        Property(name="dbl_Expression132", type=dbl_ExpandExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandExpr131", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
astPart133: BinaryAssociation = BinaryAssociation(
    name="astPart133",
    ends={
        Property(name="dbl_Construct134", type=dbl_ParseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ParseExpr", type=dbl_Construct, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentIdExpr136: BinaryAssociation = BinaryAssociation(
    name="parentIdExpr136",
    ends={
        Property(name="dbl_IdExpr137", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr135", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedElement138: BinaryAssociation = BinaryAssociation(
    name="referencedElement138",
    ends={
        Property(name="dbl_NamedElement", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr139", type=dbl_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
predefinedId140: BinaryAssociation = BinaryAssociation(
    name="predefinedId140",
    ends={
        Property(name="dbl_PredefinedId", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr141", type=dbl_PredefinedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayIndex142: BinaryAssociation = BinaryAssociation(
    name="arrayIndex142",
    ends={
        Property(name="dbl_Expression144", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr143", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callPart145: BinaryAssociation = BinaryAssociation(
    name="callPart145",
    ends={
        Property(name="dbl_CallPart", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr146", type=dbl_CallPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callArguments147: BinaryAssociation = BinaryAssociation(
    name="callArguments147",
    ends={
        Property(name="dbl_Expression149", type=dbl_CallPart, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CallPart148", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idExpr150: BinaryAssociation = BinaryAssociation(
    name="idExpr150",
    ends={
        Property(name="dbl_IdExpr151", type=dbl_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ElementAccess", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedConcept152: BinaryAssociation = BinaryAssociation(
    name="extendedConcept152",
    ends={
        Property(name="dbl_LanguageConceptClassifier", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition153", type=dbl_LanguageConceptClassifier, multiplicity=Multiplicity(1, 1))
    }
)
abstractSyntaxDef154: BinaryAssociation = BinaryAssociation(
    name="abstractSyntaxDef154",
    ends={
        Property(name="dbl_Classifier156", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition155", type=dbl_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
textualSyntaxDef157: BinaryAssociation = BinaryAssociation(
    name="textualSyntaxDef157",
    ends={
        Property(name="dbl_TextualSyntaxDef", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition158", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappingDef159: BinaryAssociation = BinaryAssociation(
    name="mappingDef159",
    ends={
        Property(name="dbl_Mapping", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition160", type=dbl_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startRule161: BinaryAssociation = BinaryAssociation(
    name="startRule161",
    ends={
        Property(name="dbl_TsRule", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TextualSyntaxDef162", type=dbl_TsRule, multiplicity=Multiplicity(1, 1))
    }
)
rules163: BinaryAssociation = BinaryAssociation(
    name="rules163",
    ends={
        Property(name="dbl_TsRule165", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TextualSyntaxDef164", type=dbl_TsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rhs166: BinaryAssociation = BinaryAssociation(
    name="rhs166",
    ends={
        Property(name="dbl_RhsExpression", type=dbl_TsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TsRule167", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
propertyType170: BinaryAssociation = BinaryAssociation(
    name="propertyType170",
    ends={
        Property(name="dbl_PropertyType", type=dbl_PropertyBindingExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_PropertyBindingExpr", type=dbl_PropertyType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier171: BinaryAssociation = BinaryAssociation(
    name="classifier171",
    ends={
        Property(name="dbl_LanguageConstructClassifier", type=dbl_RhsClassifierExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_RhsClassifierExpr", type=dbl_LanguageConstructClassifier, multiplicity=Multiplicity(1, 1))
    }
)
type172: BinaryAssociation = BinaryAssociation(
    name="type172",
    ends={
        Property(name="dbl_LanguageConstructClassifier173", type=dbl_StructuredPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_StructuredPropertyType", type=dbl_LanguageConstructClassifier, multiplicity=Multiplicity(1, 1))
    }
)
sequence168: BinaryAssociation = BinaryAssociation(
    name="sequence168",
    ends={
        Property(name="dbl_RhsExpression169", type=dbl_SequenceExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SequenceExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaObject198: BinaryAssociation = BinaryAssociation(
    name="metaObject198",
    ends={
        Property(name="dbl_Expression199", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parts174: BinaryAssociation = BinaryAssociation(
    name="parts174",
    ends={
        Property(name="dbl_MappingPart", type=dbl_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Mapping175", type=dbl_MappingPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaObject176: BinaryAssociation = BinaryAssociation(
    name="metaObject176",
    ends={
        Property(name="dbl_Expression178", type=dbl_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Mapping177", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr179: BinaryAssociation = BinaryAssociation(
    name="expr179",
    ends={
        Property(name="dbl_Expression180", type=dbl_MetaExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MetaExpr", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body181: BinaryAssociation = BinaryAssociation(
    name="body181",
    ends={
        Property(name="dbl_Statement182", type=dbl_TargetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TargetStatement", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parts183: BinaryAssociation = BinaryAssociation(
    name="parts183",
    ends={
        Property(name="dbl_MappingPart184", type=dbl_MappingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MappingStatement", type=dbl_MappingPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs185: BinaryAssociation = BinaryAssociation(
    name="exprs185",
    ends={
        Property(name="dbl_Expression187", type=dbl_MappingStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MappingStatement186", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context188: BinaryAssociation = BinaryAssociation(
    name="context188",
    ends={
        Property(name="dbl_Expression189", type=dbl_SetGenContextStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SetGenContextStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable190: BinaryAssociation = BinaryAssociation(
    name="variable190",
    ends={
        Property(name="dbl_Expression191", type=dbl_SaveGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SaveGenStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable192: BinaryAssociation = BinaryAssociation(
    name="variable192",
    ends={
        Property(name="dbl_Expression193", type=dbl_ResumeGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ResumeGenStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr194: BinaryAssociation = BinaryAssociation(
    name="expr194",
    ends={
        Property(name="dbl_Expression195", type=dbl_DynamicMappingPart, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_DynamicMappingPart", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject196: BinaryAssociation = BinaryAssociation(
    name="metaObject196",
    ends={
        Property(name="dbl_Expression197", type=dbl_ExpandExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location200: BinaryAssociation = BinaryAssociation(
    name="location200",
    ends={
        Property(name="dbl_Expression202", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement201", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quotedCode203: BinaryAssociation = BinaryAssociation(
    name="quotedCode203",
    ends={
        Property(name="dbl_QuotedCode", type=dbl_CodeQuoteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CodeQuoteExpression", type=dbl_QuotedCode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression204: BinaryAssociation = BinaryAssociation(
    name="expression204",
    ends={
        Property(name="dbl_Expression205", type=dbl_QuotedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements206: BinaryAssociation = BinaryAssociation(
    name="statements206",
    ends={
        Property(name="dbl_Statement207", type=dbl_QuotedStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedStatements", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context208: BinaryAssociation = BinaryAssociation(
    name="context208",
    ends={
        Property(name="dbl_Parameter209", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern", type=dbl_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body210: BinaryAssociation = BinaryAssociation(
    name="body210",
    ends={
        Property(name="dbl_Statement212", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern211", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_dbl_Module_NamedElement = Generalization(general=NamedElement, specific=dbl_Module)
gen_dbl_Module_EmbeddableExtensionsContainer = Generalization(general=EmbeddableExtensionsContainer, specific=dbl_Module)
gen_dbl_Module_Construct = Generalization(general=Construct, specific=dbl_Module)
gen_dbl_ExtensibleElement_NamedElement = Generalization(general=NamedElement, specific=dbl_ExtensibleElement)
gen_dbl_ExtensibleElement_Construct = Generalization(general=Construct, specific=dbl_ExtensibleElement)
gen_dbl_BoolType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_BoolType)
gen_dbl_DoubleType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_DoubleType)
gen_dbl_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_StringType)
gen_dbl_Procedure_NamedElement = Generalization(general=NamedElement, specific=dbl_Procedure)
gen_dbl_Procedure_TypedElement = Generalization(general=TypedElement, specific=dbl_Procedure)
gen_dbl_Procedure_LocalScope = Generalization(general=LocalScope, specific=dbl_Procedure)
gen_dbl_Classifier_NamedElement = Generalization(general=NamedElement, specific=dbl_Classifier)
gen_dbl_Classifier_Type = Generalization(general=Type, specific=dbl_Classifier)
gen_dbl_ClassSimilar_EmbeddableExtensionsContainer = Generalization(general=EmbeddableExtensionsContainer, specific=dbl_ClassSimilar)
gen_dbl_ClassSimilar_ModifierExtensionsContainer = Generalization(general=ModifierExtensionsContainer, specific=dbl_ClassSimilar)
gen_dbl_PrimitiveType_Type = Generalization(general=Type, specific=dbl_PrimitiveType)
gen_dbl_VoidType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_VoidType)
gen_dbl_IntType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_IntType)
gen_dbl_ClassPart_LocalScope = Generalization(general=LocalScope, specific=dbl_ClassPart)
gen_dbl_Parameter_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Parameter)
gen_dbl_Statement_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_Statement)
gen_dbl_LoopStatement_Statement = Generalization(general=Statement, specific=dbl_LoopStatement)
gen_dbl_SimpleStatement_Statement = Generalization(general=Statement, specific=dbl_SimpleStatement)
gen_dbl_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Assignment)
gen_dbl_ProcedureCall_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ProcedureCall)
gen_dbl_Return_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Return)
gen_dbl_Clazz_Classifier = Generalization(general=Classifier, specific=dbl_Clazz)
gen_dbl_Clazz_ClassSimilar = Generalization(general=ClassSimilar, specific=dbl_Clazz)
gen_dbl_Clazz_LanguageConceptClassifier = Generalization(general=LanguageConceptClassifier, specific=dbl_Clazz)
gen_dbl_Clazz_Construct = Generalization(general=Construct, specific=dbl_Clazz)
gen_dbl_ClassAugment_ClassSimilar = Generalization(general=ClassSimilar, specific=dbl_ClassAugment)
gen_dbl_AbstractVariable_NamedElement = Generalization(general=NamedElement, specific=dbl_AbstractVariable)
gen_dbl_AbstractVariable_TypedElement = Generalization(general=TypedElement, specific=dbl_AbstractVariable)
gen_dbl_Variable_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Variable)
gen_dbl_Variable_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Variable)
gen_dbl_Variable_ModifierExtensionsContainer = Generalization(general=ModifierExtensionsContainer, specific=dbl_Variable)
gen_dbl_IfStatement_Statement = Generalization(general=Statement, specific=dbl_IfStatement)
gen_dbl_LocalScopeStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_LocalScopeStatement)
gen_dbl_LocalScopeStatement_LocalScope = Generalization(general=LocalScope, specific=dbl_LocalScopeStatement)
gen_dbl_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=dbl_ForStatement)
gen_dbl_ForStatement_LocalScope = Generalization(general=LocalScope, specific=dbl_ForStatement)
gen_dbl_WaitUntil_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_WaitUntil)
gen_dbl_Terminate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Terminate)
gen_dbl_Yield_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Yield)
gen_dbl_Wait_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Wait)
gen_dbl_Reactivate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Reactivate)
gen_dbl_ActivateObject_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ActivateObject)
gen_dbl_Advance_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Advance)
gen_dbl_Print_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Print)
gen_dbl_L2Expr_Expression = Generalization(general=Expression, specific=dbl_L2Expr)
gen_dbl_L3Expr_Expression = Generalization(general=Expression, specific=dbl_L3Expr)
gen_dbl_L4Expr_Expression = Generalization(general=Expression, specific=dbl_L4Expr)
gen_dbl_L5Expr_Expression = Generalization(general=Expression, specific=dbl_L5Expr)
gen_dbl_L6Expr_Expression = Generalization(general=Expression, specific=dbl_L6Expr)
gen_dbl_L7Expr_Expression = Generalization(general=Expression, specific=dbl_L7Expr)
gen_dbl_L8Expr_Expression = Generalization(general=Expression, specific=dbl_L8Expr)
gen_dbl_L9Expr_Expression = Generalization(general=Expression, specific=dbl_L9Expr)
gen_dbl_BinaryOperator_Expression = Generalization(general=Expression, specific=dbl_BinaryOperator)
gen_dbl_UnaryOperator_Expression = Generalization(general=Expression, specific=dbl_UnaryOperator)
gen_dbl_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Or)
gen_dbl_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=dbl_WhileStatement)
gen_dbl_SwitchStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SwitchStatement)
gen_dbl_BreakStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_BreakStatement)
gen_dbl_ContinueStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ContinueStatement)
gen_dbl_Expression_TypedElement = Generalization(general=TypedElement, specific=dbl_Expression)
gen_dbl_Expression_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_Expression)
gen_dbl_L1Expr_Expression = Generalization(general=Expression, specific=dbl_L1Expr)
gen_dbl_Or_L8Expr = Generalization(general=L8Expr, specific=dbl_Or)
gen_dbl_And_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_And)
gen_dbl_And_L7Expr = Generalization(general=L7Expr, specific=dbl_And)
gen_dbl_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_NotEqual)
gen_dbl_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Not)
gen_dbl_NotEqual_L6Expr = Generalization(general=L6Expr, specific=dbl_NotEqual)
gen_dbl_Not_L2Expr = Generalization(general=L2Expr, specific=dbl_Not)
gen_dbl_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Equal)
gen_dbl_Cast_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Cast)
gen_dbl_Equal_L6Expr = Generalization(general=L6Expr, specific=dbl_Equal)
gen_dbl_Cast_TypedElement = Generalization(general=TypedElement, specific=dbl_Cast)
gen_dbl_Cast_L2Expr = Generalization(general=L2Expr, specific=dbl_Cast)
gen_dbl_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Greater)
gen_dbl_Greater_L5Expr = Generalization(general=L5Expr, specific=dbl_Greater)
gen_dbl_CreateObject_L1Expr = Generalization(general=L1Expr, specific=dbl_CreateObject)
gen_dbl_CreateObject_TypedElement = Generalization(general=TypedElement, specific=dbl_CreateObject)
gen_dbl_GreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_GreaterEqual)
gen_dbl_GreaterEqual_L5Expr = Generalization(general=L5Expr, specific=dbl_GreaterEqual)
gen_dbl_NullLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_NullLiteral)
gen_dbl_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Less)
gen_dbl_TimeLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_TimeLiteral)
gen_dbl_Less_L5Expr = Generalization(general=L5Expr, specific=dbl_Less)
gen_dbl_ActiveLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_ActiveLiteral)
gen_dbl_LessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_LessEqual)
gen_dbl_LessEqual_L5Expr = Generalization(general=L5Expr, specific=dbl_LessEqual)
gen_dbl_StringLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_StringLiteral)
gen_dbl_InstanceOf_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_InstanceOf)
gen_dbl_InstanceOf_L5Expr = Generalization(general=L5Expr, specific=dbl_InstanceOf)
gen_dbl_Plus_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Plus)
gen_dbl_IntLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_IntLiteral)
gen_dbl_Plus_L4Expr = Generalization(general=L4Expr, specific=dbl_Plus)
gen_dbl_Minus_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Minus)
gen_dbl_Minus_L4Expr = Generalization(general=L4Expr, specific=dbl_Minus)
gen_dbl_TrueLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_TrueLiteral)
gen_dbl_Mul_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Mul)
gen_dbl_FalseLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_FalseLiteral)
gen_dbl_Mul_L3Expr = Generalization(general=L3Expr, specific=dbl_Mul)
gen_dbl_DoubleLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_DoubleLiteral)
gen_dbl_Mod_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Mod)
gen_dbl_Mod_L3Expr = Generalization(general=L3Expr, specific=dbl_Mod)
gen_dbl_Div_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Div)
gen_dbl_Div_L3Expr = Generalization(general=L3Expr, specific=dbl_Div)
gen_dbl_ExpandExpr_Expression = Generalization(general=Expression, specific=dbl_ExpandExpr)
gen_dbl_ParseExpr_Expression = Generalization(general=Expression, specific=dbl_ParseExpr)
gen_dbl_MeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MeLiteral)
gen_dbl_SuperLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SuperLiteral)
gen_dbl_MetaLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MetaLiteral)
gen_dbl_TypeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_TypeLiteral)
gen_dbl_SizeOfArray_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SizeOfArray)
gen_dbl_IdExpr_L1Expr = Generalization(general=L1Expr, specific=dbl_IdExpr)
gen_dbl_Neg_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Neg)
gen_dbl_Neg_L2Expr = Generalization(general=L2Expr, specific=dbl_Neg)
gen_dbl_ElementAccess_Expression = Generalization(general=Expression, specific=dbl_ElementAccess)
gen_dbl_VariableAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_VariableAccess)
gen_dbl_MetaAccess_VariableAccess = Generalization(general=VariableAccess, specific=dbl_MetaAccess)
gen_dbl_TypeAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_TypeAccess)
gen_dbl_ClassContentExtension_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ClassContentExtension)
gen_dbl_ModuleContentExtension_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ModuleContentExtension)
gen_dbl_ExtensionDefinition_LanguageConceptClassifier = Generalization(general=LanguageConceptClassifier, specific=dbl_ExtensionDefinition)
gen_dbl_ExtensionDefinition_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ExtensionDefinition)
gen_dbl_TextualSyntaxDef_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_TextualSyntaxDef)
gen_dbl_LanguageConstructClassifier_NamedElement = Generalization(general=NamedElement, specific=dbl_LanguageConstructClassifier)
gen_dbl_LanguageConstructClassifier_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_LanguageConstructClassifier)
gen_dbl_LanguageConceptClassifier_LanguageConstructClassifier = Generalization(general=LanguageConstructClassifier, specific=dbl_LanguageConceptClassifier)
gen_dbl_TsRule_NamedElement = Generalization(general=NamedElement, specific=dbl_TsRule)
gen_dbl_TsRule_LanguageConstructClassifier = Generalization(general=LanguageConstructClassifier, specific=dbl_TsRule)
gen_dbl_L3RhsExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_L3RhsExpr)
gen_dbl_L2RhsExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_L2RhsExpr)
gen_dbl_SequenceExpr_L2RhsExpr = Generalization(general=L2RhsExpr, specific=dbl_SequenceExpr)
gen_dbl_L1RhsExpr_RhsExpression = Generalization(general=RhsExpression, specific=dbl_L1RhsExpr)
gen_dbl_TerminalExpr_L1RhsExpr = Generalization(general=L1RhsExpr, specific=dbl_TerminalExpr)
gen_dbl_PropertyBindingExpr_NamedElement = Generalization(general=NamedElement, specific=dbl_PropertyBindingExpr)
gen_dbl_PropertyBindingExpr_L1RhsExpr = Generalization(general=L1RhsExpr, specific=dbl_PropertyBindingExpr)
gen_dbl_RhsClassifierExpr_L1RhsExpr = Generalization(general=L1RhsExpr, specific=dbl_RhsClassifierExpr)
gen_dbl_IdPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_IdPropertyType)
gen_dbl_IntPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_IntPropertyType)
gen_dbl_StringPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_StringPropertyType)
gen_dbl_BooleanPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_BooleanPropertyType)
gen_dbl_StructuredPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_StructuredPropertyType)
gen_dbl_CompositePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=dbl_CompositePropertyType)
gen_dbl_ExpandStatement_Statement = Generalization(general=Statement, specific=dbl_ExpandStatement)
gen_dbl_Mapping_LocalScopeStatement = Generalization(general=LocalScopeStatement, specific=dbl_Mapping)
gen_dbl_MetaExpr_Expression = Generalization(general=Expression, specific=dbl_MetaExpr)
gen_dbl_TargetStatement_Statement = Generalization(general=Statement, specific=dbl_TargetStatement)
gen_dbl_MappingStatement_Statement = Generalization(general=Statement, specific=dbl_MappingStatement)
gen_dbl_SetGenContextStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SetGenContextStatement)
gen_dbl_ResetGenContextStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ResetGenContextStatement)
gen_dbl_SaveGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SaveGenStatement)
gen_dbl_ResumeGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ResumeGenStatement)
gen_dbl_FixedMappingPart_MappingPart = Generalization(general=MappingPart, specific=dbl_FixedMappingPart)
gen_dbl_DynamicMappingPart_MappingPart = Generalization(general=MappingPart, specific=dbl_DynamicMappingPart)
gen_dbl_ExpandExpression_Expression = Generalization(general=Expression, specific=dbl_ExpandExpression)
gen_dbl_ReferencePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=dbl_ReferencePropertyType)
gen_dbl_CodeQuoteExpression_Expression = Generalization(general=Expression, specific=dbl_CodeQuoteExpression)
gen_dbl_QuotedExpression_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedExpression)
gen_dbl_QuotedStatements_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedStatements)
gen_dbl_QuotedClassContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedClassContent)
gen_dbl_QuotedClassContent_ClassSimilar = Generalization(general=ClassSimilar, specific=dbl_QuotedClassContent)
gen_dbl_QuotedModuleContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedModuleContent)
gen_dbl_QuotedModuleContent_Module = Generalization(general=Module, specific=dbl_QuotedModuleContent)
gen_dbl_Pattern_NamedElement = Generalization(general=NamedElement, specific=dbl_Pattern)
gen_dbl_TestStatement_Statement = Generalization(general=Statement, specific=dbl_TestStatement)

# Domain Model
domain_model = DomainModel(
    name="dbl",
    types={dbl_Module, EmbeddableExtensionsContainer, dbl_Classifier, dbl_ClassAugment, dbl_ExtensionDefinition, dbl_Procedure, dbl_Variable, dbl_Construct, dbl_ExpandExpr, dbl_ExtensibleElement, NamedElement, Construct, dbl_Model, dbl_Import, dbl_BoolType, dbl_DoubleType, dbl_StringType, TypedElement, LocalScope, dbl_Parameter, dbl_NativeBinding, dbl_ClassSimilar, ModifierExtensionsContainer, dbl_EmbeddableExtensionsContainer, dbl_ModifierExtensionsContainer, dbl_Type, dbl_ArrayDimension, dbl_TypedElement, dbl_PrimitiveType, dbl_IdExpr, dbl_Expression, Type, dbl_VoidType, PrimitiveType, dbl_IntType, dbl_Clazz, dbl_SuperClassSpecification, dbl_ClassPart, dbl_NamedElement, dbl_Statement, ExtensibleElement, dbl_LoopStatement, Statement, dbl_SimpleStatement, dbl_Assignment, dbl_VariableAccess, dbl_ProcedureCall, dbl_Return, Classifier, ClassSimilar, LanguageConceptClassifier, dbl_Constructor, dbl_AbstractVariable, AbstractVariable, SimpleStatement, dbl_IfStatement, dbl_LocalScope, dbl_LocalScopeStatement, dbl_ForStatement, LoopStatement, dbl_WaitUntil, dbl_Terminate, dbl_Yield, dbl_Wait, dbl_Reactivate, dbl_ActivateObject, dbl_Advance, dbl_Print, dbl_L3Expr, dbl_L4Expr, dbl_L5Expr, dbl_L6Expr, dbl_L7Expr, dbl_L8Expr, dbl_L9Expr, dbl_BinaryOperator, dbl_UnaryOperator, dbl_Or, BinaryOperator, dbl_WhileStatement, dbl_SwitchStatement, dbl_SwitchCase, dbl_BreakStatement, dbl_ContinueStatement, dbl_L1Expr, Expression, dbl_L2Expr, L8Expr, dbl_And, L7Expr, dbl_NotEqual, dbl_Not, L6Expr, dbl_Equal, dbl_Cast, dbl_Greater, L5Expr, dbl_CreateObject, L1Expr, dbl_GreaterEqual, dbl_NullLiteral, dbl_Less, dbl_TimeLiteral, dbl_ActiveLiteral, dbl_LessEqual, dbl_StringLiteral, dbl_InstanceOf, dbl_Plus, dbl_IntLiteral, L4Expr, dbl_Minus, dbl_TrueLiteral, dbl_Mul, dbl_FalseLiteral, L3Expr, dbl_DoubleLiteral, dbl_Mod, dbl_Div, dbl_Neg, UnaryOperator, dbl_ParseExpr, dbl_PredefinedId, dbl_MeLiteral, PredefinedId, dbl_SuperLiteral, dbl_MetaLiteral, dbl_TypeLiteral, dbl_SizeOfArray, dbl_CallPart, L2Expr, dbl_ElementAccess, ElementAccess, dbl_MetaAccess, VariableAccess, dbl_TypeAccess, dbl_ClassContentExtension, dbl_ModuleContentExtension, dbl_LanguageConceptClassifier, dbl_TextualSyntaxDef, dbl_Mapping, dbl_TsRule, dbl_LanguageConstructClassifier, LanguageConstructClassifier, dbl_RhsExpression, dbl_L3RhsExpr, RhsExpression, dbl_L2RhsExpr, dbl_SequenceExpr, L2RhsExpr, dbl_L1RhsExpr, dbl_TerminalExpr, L1RhsExpr, dbl_PropertyBindingExpr, dbl_PropertyType, dbl_RhsClassifierExpr, dbl_IdPropertyType, PropertyType, dbl_IntPropertyType, dbl_StringPropertyType, dbl_BooleanPropertyType, dbl_StructuredPropertyType, dbl_CompositePropertyType, StructuredPropertyType, dbl_ExpandStatement, LocalScopeStatement, dbl_MappingPart, dbl_MetaExpr, dbl_TargetStatement, dbl_MappingStatement, dbl_SetGenContextStatement, dbl_ResetGenContextStatement, dbl_SaveGenStatement, dbl_ResumeGenStatement, dbl_FixedMappingPart, MappingPart, dbl_DynamicMappingPart, dbl_ExpandExpression, dbl_ReferencePropertyType, dbl_CodeQuoteExpression, dbl_QuotedCode, dbl_QuotedExpression, QuotedCode, dbl_QuotedStatements, dbl_QuotedClassContent, dbl_QuotedModuleContent, Module, dbl_Pattern, dbl_TestStatement},
    associations={imports1, modules2, model4, classifiers7, classAugments9, extensionDefs11, procedures13, expandExpr0, parameters29, attributes31, variables15, extensions17, modifierExtensions18, arrayDimensions20, primitiveType21, typeArrayDimensions22, classifierType25, size27, finalBlock40, actionsBlock43, reportBlock46, clearBlock49, clazz52, methods33, superClasses36, initialBlock38, initialValue67, variable70, value71, callIdExpr74, constructorArguments54, constructor57, bindings59, parameters61, augmentedClass64, condition88, trueCase90, falseCase92, statements95, termination97, increment99, body102, value76, condition78, objectAccess80, objectAccess82, time84, outputs86, op1123, op2125, op128, condition105, body107, variable110, cases112, defaultCase114, value117, body120, expr130, astPart133, parentIdExpr136, referencedElement138, predefinedId140, arrayIndex142, callPart145, callArguments147, idExpr150, extendedConcept152, abstractSyntaxDef154, textualSyntaxDef157, mappingDef159, startRule161, rules163, rhs166, propertyType170, classifier171, type172, sequence168, metaObject198, parts174, metaObject176, expr179, body181, parts183, exprs185, context188, variable190, variable192, expr194, metaObject196, location200, quotedCode203, expression204, statements206, context208, body210},
    generalizations={gen_dbl_Module_NamedElement, gen_dbl_Module_EmbeddableExtensionsContainer, gen_dbl_Module_Construct, gen_dbl_ExtensibleElement_NamedElement, gen_dbl_ExtensibleElement_Construct, gen_dbl_BoolType_PrimitiveType, gen_dbl_DoubleType_PrimitiveType, gen_dbl_StringType_PrimitiveType, gen_dbl_Procedure_NamedElement, gen_dbl_Procedure_TypedElement, gen_dbl_Procedure_LocalScope, gen_dbl_Classifier_NamedElement, gen_dbl_Classifier_Type, gen_dbl_ClassSimilar_EmbeddableExtensionsContainer, gen_dbl_ClassSimilar_ModifierExtensionsContainer, gen_dbl_PrimitiveType_Type, gen_dbl_VoidType_PrimitiveType, gen_dbl_IntType_PrimitiveType, gen_dbl_ClassPart_LocalScope, gen_dbl_Parameter_AbstractVariable, gen_dbl_Statement_ExtensibleElement, gen_dbl_LoopStatement_Statement, gen_dbl_SimpleStatement_Statement, gen_dbl_Assignment_SimpleStatement, gen_dbl_ProcedureCall_SimpleStatement, gen_dbl_Return_SimpleStatement, gen_dbl_Clazz_Classifier, gen_dbl_Clazz_ClassSimilar, gen_dbl_Clazz_LanguageConceptClassifier, gen_dbl_Clazz_Construct, gen_dbl_ClassAugment_ClassSimilar, gen_dbl_AbstractVariable_NamedElement, gen_dbl_AbstractVariable_TypedElement, gen_dbl_Variable_AbstractVariable, gen_dbl_Variable_SimpleStatement, gen_dbl_Variable_ModifierExtensionsContainer, gen_dbl_IfStatement_Statement, gen_dbl_LocalScopeStatement_SimpleStatement, gen_dbl_LocalScopeStatement_LocalScope, gen_dbl_ForStatement_LoopStatement, gen_dbl_ForStatement_LocalScope, gen_dbl_WaitUntil_SimpleStatement, gen_dbl_Terminate_SimpleStatement, gen_dbl_Yield_SimpleStatement, gen_dbl_Wait_SimpleStatement, gen_dbl_Reactivate_SimpleStatement, gen_dbl_ActivateObject_SimpleStatement, gen_dbl_Advance_SimpleStatement, gen_dbl_Print_SimpleStatement, gen_dbl_L2Expr_Expression, gen_dbl_L3Expr_Expression, gen_dbl_L4Expr_Expression, gen_dbl_L5Expr_Expression, gen_dbl_L6Expr_Expression, gen_dbl_L7Expr_Expression, gen_dbl_L8Expr_Expression, gen_dbl_L9Expr_Expression, gen_dbl_BinaryOperator_Expression, gen_dbl_UnaryOperator_Expression, gen_dbl_Or_BinaryOperator, gen_dbl_WhileStatement_LoopStatement, gen_dbl_SwitchStatement_SimpleStatement, gen_dbl_BreakStatement_SimpleStatement, gen_dbl_ContinueStatement_SimpleStatement, gen_dbl_Expression_TypedElement, gen_dbl_Expression_ExtensibleElement, gen_dbl_L1Expr_Expression, gen_dbl_Or_L8Expr, gen_dbl_And_BinaryOperator, gen_dbl_And_L7Expr, gen_dbl_NotEqual_BinaryOperator, gen_dbl_Not_UnaryOperator, gen_dbl_NotEqual_L6Expr, gen_dbl_Not_L2Expr, gen_dbl_Equal_BinaryOperator, gen_dbl_Cast_UnaryOperator, gen_dbl_Equal_L6Expr, gen_dbl_Cast_TypedElement, gen_dbl_Cast_L2Expr, gen_dbl_Greater_BinaryOperator, gen_dbl_Greater_L5Expr, gen_dbl_CreateObject_L1Expr, gen_dbl_CreateObject_TypedElement, gen_dbl_GreaterEqual_BinaryOperator, gen_dbl_GreaterEqual_L5Expr, gen_dbl_NullLiteral_L1Expr, gen_dbl_Less_BinaryOperator, gen_dbl_TimeLiteral_L1Expr, gen_dbl_Less_L5Expr, gen_dbl_ActiveLiteral_L1Expr, gen_dbl_LessEqual_BinaryOperator, gen_dbl_LessEqual_L5Expr, gen_dbl_StringLiteral_L1Expr, gen_dbl_InstanceOf_BinaryOperator, gen_dbl_InstanceOf_L5Expr, gen_dbl_Plus_BinaryOperator, gen_dbl_IntLiteral_L1Expr, gen_dbl_Plus_L4Expr, gen_dbl_Minus_BinaryOperator, gen_dbl_Minus_L4Expr, gen_dbl_TrueLiteral_L1Expr, gen_dbl_Mul_BinaryOperator, gen_dbl_FalseLiteral_L1Expr, gen_dbl_Mul_L3Expr, gen_dbl_DoubleLiteral_L1Expr, gen_dbl_Mod_BinaryOperator, gen_dbl_Mod_L3Expr, gen_dbl_Div_BinaryOperator, gen_dbl_Div_L3Expr, gen_dbl_ExpandExpr_Expression, gen_dbl_ParseExpr_Expression, gen_dbl_MeLiteral_PredefinedId, gen_dbl_SuperLiteral_PredefinedId, gen_dbl_MetaLiteral_PredefinedId, gen_dbl_TypeLiteral_PredefinedId, gen_dbl_SizeOfArray_PredefinedId, gen_dbl_IdExpr_L1Expr, gen_dbl_Neg_UnaryOperator, gen_dbl_Neg_L2Expr, gen_dbl_ElementAccess_Expression, gen_dbl_VariableAccess_ElementAccess, gen_dbl_MetaAccess_VariableAccess, gen_dbl_TypeAccess_ElementAccess, gen_dbl_ClassContentExtension_ExtensibleElement, gen_dbl_ModuleContentExtension_ExtensibleElement, gen_dbl_ExtensionDefinition_LanguageConceptClassifier, gen_dbl_ExtensionDefinition_ExtensibleElement, gen_dbl_TextualSyntaxDef_ExtensibleElement, gen_dbl_LanguageConstructClassifier_NamedElement, gen_dbl_LanguageConstructClassifier_ExtensibleElement, gen_dbl_LanguageConceptClassifier_LanguageConstructClassifier, gen_dbl_TsRule_NamedElement, gen_dbl_TsRule_LanguageConstructClassifier, gen_dbl_L3RhsExpr_RhsExpression, gen_dbl_L2RhsExpr_RhsExpression, gen_dbl_SequenceExpr_L2RhsExpr, gen_dbl_L1RhsExpr_RhsExpression, gen_dbl_TerminalExpr_L1RhsExpr, gen_dbl_PropertyBindingExpr_NamedElement, gen_dbl_PropertyBindingExpr_L1RhsExpr, gen_dbl_RhsClassifierExpr_L1RhsExpr, gen_dbl_IdPropertyType_PropertyType, gen_dbl_IntPropertyType_PropertyType, gen_dbl_StringPropertyType_PropertyType, gen_dbl_BooleanPropertyType_PropertyType, gen_dbl_StructuredPropertyType_PropertyType, gen_dbl_CompositePropertyType_StructuredPropertyType, gen_dbl_ExpandStatement_Statement, gen_dbl_Mapping_LocalScopeStatement, gen_dbl_MetaExpr_Expression, gen_dbl_TargetStatement_Statement, gen_dbl_MappingStatement_Statement, gen_dbl_SetGenContextStatement_SimpleStatement, gen_dbl_ResetGenContextStatement_SimpleStatement, gen_dbl_SaveGenStatement_SimpleStatement, gen_dbl_ResumeGenStatement_SimpleStatement, gen_dbl_FixedMappingPart_MappingPart, gen_dbl_DynamicMappingPart_MappingPart, gen_dbl_ExpandExpression_Expression, gen_dbl_ReferencePropertyType_StructuredPropertyType, gen_dbl_CodeQuoteExpression_Expression, gen_dbl_QuotedExpression_QuotedCode, gen_dbl_QuotedStatements_QuotedCode, gen_dbl_QuotedClassContent_QuotedCode, gen_dbl_QuotedClassContent_ClassSimilar, gen_dbl_QuotedModuleContent_QuotedCode, gen_dbl_QuotedModuleContent_Module, gen_dbl_Pattern_NamedElement, gen_dbl_TestStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)