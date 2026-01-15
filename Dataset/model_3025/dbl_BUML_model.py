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
dbl_Construct = Class(name="dbl::Construct")
dbl_ExpandExpr = Class(name="dbl::ExpandExpr")
dbl_Model = Class(name="dbl::Model")
dbl_Import = Class(name="dbl::Import")
dbl_Module = Class(name="dbl::Module")
ConstructiveExtensionAtContentExtensionPoint = Class(name="ConstructiveExtensionAtContentExtensionPoint")
dbl_Class = Class(name="dbl::Class")
dbl_ExtensionDefinition = Class(name="dbl::ExtensionDefinition")
dbl_ExtensionSemanticsDefinition = Class(name="dbl::ExtensionSemanticsDefinition")
dbl_ExtensibleElement = Class(name="dbl::ExtensibleElement")
NamedElement = Class(name="NamedElement")
Construct = Class(name="Construct")
dbl_PrimitiveType = Class(name="dbl::PrimitiveType", is_abstract=True)
dbl_IdExpr = Class(name="dbl::IdExpr")
dbl_Expression = Class(name="dbl::Expression")
Type = Class(name="Type")
dbl_VoidType = Class(name="dbl::VoidType")
PrimitiveType = Class(name="PrimitiveType")
dbl_IntType = Class(name="dbl::IntType")
dbl_BoolType = Class(name="dbl::BoolType")
dbl_DoubleType = Class(name="dbl::DoubleType")
dbl_StringType = Class(name="dbl::StringType")
TypedElement = Class(name="TypedElement")
LocalScope = Class(name="LocalScope")
dbl_Parameter = Class(name="dbl::Parameter")
dbl_NativeBinding = Class(name="dbl::NativeBinding")
dbl_Function = Class(name="dbl::Function")
dbl_Variable = Class(name="dbl::Variable")
dbl_ConstructiveExtension = Class(name="dbl::ConstructiveExtension")
ExtensibleElement = Class(name="ExtensibleElement")
dbl_ConstructiveExtensionAtContentExtensionPoint = Class(name="dbl::ConstructiveExtensionAtContentExtensionPoint", is_abstract=True)
dbl_ModuleContent = Class(name="dbl::ModuleContent")
ConstructiveExtension = Class(name="ConstructiveExtension")
dbl_ClassContent = Class(name="dbl::ClassContent")
dbl_Type = Class(name="dbl::Type", is_abstract=True)
dbl_ArrayDimension = Class(name="dbl::ArrayDimension")
dbl_TypedElement = Class(name="dbl::TypedElement", is_abstract=True)
dbl_LocalScope = Class(name="dbl::LocalScope")
dbl_AbstractVariable = Class(name="dbl::AbstractVariable", is_abstract=True)
AbstractVariable = Class(name="AbstractVariable")
SimpleStatement = Class(name="SimpleStatement")
dbl_NamedElement = Class(name="dbl::NamedElement")
dbl_Statement = Class(name="dbl::Statement")
dbl_LoopStatement = Class(name="dbl::LoopStatement")
Statement = Class(name="Statement")
dbl_SimpleStatement = Class(name="dbl::SimpleStatement")
dbl_SuperClassSpecification = Class(name="dbl::SuperClassSpecification")
LanguageConceptClassifier = Class(name="LanguageConceptClassifier")
dbl_Constructor = Class(name="dbl::Constructor")
dbl_Terminate = Class(name="dbl::Terminate")
dbl_Yield = Class(name="dbl::Yield")
dbl_Wait = Class(name="dbl::Wait")
dbl_Reactivate = Class(name="dbl::Reactivate")
dbl_ActivateObject = Class(name="dbl::ActivateObject")
dbl_Advance = Class(name="dbl::Advance")
dbl_Print = Class(name="dbl::Print")
dbl_IfStatement = Class(name="dbl::IfStatement")
dbl_Assignment = Class(name="dbl::Assignment")
dbl_VariableAccess = Class(name="dbl::VariableAccess")
dbl_FunctionCall = Class(name="dbl::FunctionCall")
dbl_Return = Class(name="dbl::Return")
dbl_WaitUntil = Class(name="dbl::WaitUntil")
dbl_SwitchStatement = Class(name="dbl::SwitchStatement")
dbl_LocalScopeStatement = Class(name="dbl::LocalScopeStatement")
dbl_ForStatement = Class(name="dbl::ForStatement")
LoopStatement = Class(name="LoopStatement")
dbl_WhileStatement = Class(name="dbl::WhileStatement")
dbl_L2Expr = Class(name="dbl::L2Expr")
dbl_L3Expr = Class(name="dbl::L3Expr")
dbl_L4Expr = Class(name="dbl::L4Expr")
dbl_L5Expr = Class(name="dbl::L5Expr")
dbl_L6Expr = Class(name="dbl::L6Expr")
dbl_L7Expr = Class(name="dbl::L7Expr")
dbl_L8Expr = Class(name="dbl::L8Expr")
dbl_L9Expr = Class(name="dbl::L9Expr")
dbl_BinaryOperator = Class(name="dbl::BinaryOperator", is_abstract=True)
dbl_SwitchCase = Class(name="dbl::SwitchCase")
dbl_BreakStatement = Class(name="dbl::BreakStatement")
dbl_ContinueStatement = Class(name="dbl::ContinueStatement")
dbl_L1Expr = Class(name="dbl::L1Expr")
Expression = Class(name="Expression")
dbl_Or = Class(name="dbl::Or")
BinaryOperator = Class(name="BinaryOperator")
L8Expr = Class(name="L8Expr")
dbl_And = Class(name="dbl::And")
L7Expr = Class(name="L7Expr")
dbl_NotEqual = Class(name="dbl::NotEqual")
L6Expr = Class(name="L6Expr")
dbl_Equal = Class(name="dbl::Equal")
dbl_Greater = Class(name="dbl::Greater")
L5Expr = Class(name="L5Expr")
dbl_GreaterEqual = Class(name="dbl::GreaterEqual")
dbl_Less = Class(name="dbl::Less")
dbl_LessEqual = Class(name="dbl::LessEqual")
dbl_InstanceOf = Class(name="dbl::InstanceOf")
dbl_Plus = Class(name="dbl::Plus")
L4Expr = Class(name="L4Expr")
dbl_Minus = Class(name="dbl::Minus")
dbl_Mul = Class(name="dbl::Mul")
L3Expr = Class(name="L3Expr")
dbl_Mod = Class(name="dbl::Mod")
dbl_UnaryOperator = Class(name="dbl::UnaryOperator", is_abstract=True)
dbl_UniqueIdExpr = Class(name="dbl::UniqueIdExpr")
dbl_ParseExpr = Class(name="dbl::ParseExpr")
dbl_PredefinedId = Class(name="dbl::PredefinedId")
dbl_MeLiteral = Class(name="dbl::MeLiteral")
PredefinedId = Class(name="PredefinedId")
dbl_SuperLiteral = Class(name="dbl::SuperLiteral")
dbl_MetaLiteral = Class(name="dbl::MetaLiteral")
dbl_TypeLiteral = Class(name="dbl::TypeLiteral")
dbl_SizeOfArray = Class(name="dbl::SizeOfArray")
dbl_CallPart = Class(name="dbl::CallPart")
dbl_ElementAccess = Class(name="dbl::ElementAccess", is_abstract=True)
dbl_Div = Class(name="dbl::Div")
dbl_Neg = Class(name="dbl::Neg")
UnaryOperator = Class(name="UnaryOperator")
L2Expr = Class(name="L2Expr")
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
ElementAccess = Class(name="ElementAccess")
dbl_MetaAccess = Class(name="dbl::MetaAccess")
VariableAccess = Class(name="VariableAccess")
dbl_TypeAccess = Class(name="dbl::TypeAccess")
dbl_LanguageConceptClassifier = Class(name="dbl::LanguageConceptClassifier", is_abstract=True)
dbl_TextualSyntaxDef = Class(name="dbl::TextualSyntaxDef")
dbl_IdPropertyType = Class(name="dbl::IdPropertyType")
PropertyType = Class(name="PropertyType")
dbl_IntPropertyType = Class(name="dbl::IntPropertyType")
dbl_StringPropertyType = Class(name="dbl::StringPropertyType")
dbl_BooleanPropertyType = Class(name="dbl::BooleanPropertyType")
dbl_StructuredPropertyType = Class(name="dbl::StructuredPropertyType")
dbl_CompositePropertyType = Class(name="dbl::CompositePropertyType")
StructuredPropertyType = Class(name="StructuredPropertyType")
dbl_ReferencePropertyType = Class(name="dbl::ReferencePropertyType")
dbl_MetaExpr = Class(name="dbl::MetaExpr")
dbl_PropertyBindingExpr = Class(name="dbl::PropertyBindingExpr")
dbl_PropertyType = Class(name="dbl::PropertyType", is_abstract=True)
dbl_RhsClassifierExpr = Class(name="dbl::RhsClassifierExpr")
dbl_ExpandVariablePart = Class(name="dbl::ExpandVariablePart")
dbl_SetExpansionContextStatement = Class(name="dbl::SetExpansionContextStatement")
dbl_SaveGenStatement = Class(name="dbl::SaveGenStatement")
dbl_ResumeGenStatement = Class(name="dbl::ResumeGenStatement")
dbl_ExpandExpression = Class(name="dbl::ExpandExpression")
dbl_ExpandStatement = Class(name="dbl::ExpandStatement")
dbl_TargetStatement = Class(name="dbl::TargetStatement")
dbl_ExpansionStatement = Class(name="dbl::ExpansionStatement")
dbl_ExpansionPart = Class(name="dbl::ExpansionPart", is_abstract=True)
dbl_ExpandTextPart = Class(name="dbl::ExpandTextPart")
ExpansionPart = Class(name="ExpansionPart")
dbl_Pattern = Class(name="dbl::Pattern")
dbl_TestStatement = Class(name="dbl::TestStatement")
dbl_CodeQuoteExpression = Class(name="dbl::CodeQuoteExpression")
dbl_QuotedCode = Class(name="dbl::QuotedCode")
dbl_QuotedExpression = Class(name="dbl::QuotedExpression")
QuotedCode = Class(name="QuotedCode")
dbl_QuotedStatements = Class(name="dbl::QuotedStatements")
dbl_QuotedClassContent = Class(name="dbl::QuotedClassContent")
Class_ = Class(name="Class")
dbl_QuotedModuleContent = Class(name="dbl::QuotedModuleContent")
Module = Class(name="Module")

# dbl_Construct class attributes and methods

# dbl_ExpandExpr class attributes and methods

# dbl_Model class attributes and methods

# dbl_Import class attributes and methods
dbl_Import_file: Property = Property(name="file", type=StringType)
dbl_Import.attributes={dbl_Import_file}

# dbl_Module class attributes and methods

# ConstructiveExtensionAtContentExtensionPoint class attributes and methods

# dbl_Class class attributes and methods
dbl_Class_active: Property = Property(name="active", type=BooleanType)
dbl_Class.attributes={dbl_Class_active}

# dbl_ExtensionDefinition class attributes and methods

# dbl_ExtensionSemanticsDefinition class attributes and methods

# dbl_ExtensibleElement class attributes and methods
dbl_ExtensibleElement_concreteSyntax: Property = Property(name="concreteSyntax", type=StringType)
dbl_ExtensibleElement_instanceOfExtensionDefinition: Property = Property(name="instanceOfExtensionDefinition", type=BooleanType)
dbl_ExtensibleElement.attributes={dbl_ExtensibleElement_instanceOfExtensionDefinition, dbl_ExtensibleElement_concreteSyntax}

# NamedElement class attributes and methods

# Construct class attributes and methods

# dbl_PrimitiveType class attributes and methods

# dbl_IdExpr class attributes and methods

# dbl_Expression class attributes and methods

# Type class attributes and methods

# dbl_VoidType class attributes and methods

# PrimitiveType class attributes and methods

# dbl_IntType class attributes and methods

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

# dbl_Function class attributes and methods
dbl_Function_class: Property = Property(name="class", type=BooleanType)
dbl_Function_abstract: Property = Property(name="abstract", type=BooleanType)
dbl_Function.attributes={dbl_Function_abstract, dbl_Function_class}

# dbl_Variable class attributes and methods
dbl_Variable_control: Property = Property(name="control", type=BooleanType)
dbl_Variable_class: Property = Property(name="class", type=BooleanType)
dbl_Variable.attributes={dbl_Variable_class, dbl_Variable_control}

# dbl_ConstructiveExtension class attributes and methods

# ExtensibleElement class attributes and methods

# dbl_ConstructiveExtensionAtContentExtensionPoint class attributes and methods

# dbl_ModuleContent class attributes and methods

# ConstructiveExtension class attributes and methods

# dbl_ClassContent class attributes and methods

# dbl_Type class attributes and methods

# dbl_ArrayDimension class attributes and methods

# dbl_TypedElement class attributes and methods

# dbl_LocalScope class attributes and methods

# dbl_AbstractVariable class attributes and methods

# AbstractVariable class attributes and methods

# SimpleStatement class attributes and methods

# dbl_NamedElement class attributes and methods
dbl_NamedElement_name: Property = Property(name="name", type=StringType)
dbl_NamedElement.attributes={dbl_NamedElement_name}

# dbl_Statement class attributes and methods

# dbl_LoopStatement class attributes and methods

# Statement class attributes and methods

# dbl_SimpleStatement class attributes and methods

# dbl_SuperClassSpecification class attributes and methods

# LanguageConceptClassifier class attributes and methods

# dbl_Constructor class attributes and methods

# dbl_Terminate class attributes and methods

# dbl_Yield class attributes and methods

# dbl_Wait class attributes and methods

# dbl_Reactivate class attributes and methods

# dbl_ActivateObject class attributes and methods
dbl_ActivateObject_priority: Property = Property(name="priority", type=IntegerType)
dbl_ActivateObject.attributes={dbl_ActivateObject_priority}

# dbl_Advance class attributes and methods

# dbl_Print class attributes and methods

# dbl_IfStatement class attributes and methods

# dbl_Assignment class attributes and methods

# dbl_VariableAccess class attributes and methods

# dbl_FunctionCall class attributes and methods

# dbl_Return class attributes and methods

# dbl_WaitUntil class attributes and methods

# dbl_SwitchStatement class attributes and methods

# dbl_LocalScopeStatement class attributes and methods

# dbl_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# dbl_WhileStatement class attributes and methods

# dbl_L2Expr class attributes and methods

# dbl_L3Expr class attributes and methods

# dbl_L4Expr class attributes and methods

# dbl_L5Expr class attributes and methods

# dbl_L6Expr class attributes and methods

# dbl_L7Expr class attributes and methods

# dbl_L8Expr class attributes and methods

# dbl_L9Expr class attributes and methods

# dbl_BinaryOperator class attributes and methods

# dbl_SwitchCase class attributes and methods

# dbl_BreakStatement class attributes and methods

# dbl_ContinueStatement class attributes and methods

# dbl_L1Expr class attributes and methods

# Expression class attributes and methods

# dbl_Or class attributes and methods

# BinaryOperator class attributes and methods

# L8Expr class attributes and methods

# dbl_And class attributes and methods

# L7Expr class attributes and methods

# dbl_NotEqual class attributes and methods

# L6Expr class attributes and methods

# dbl_Equal class attributes and methods

# dbl_Greater class attributes and methods

# L5Expr class attributes and methods

# dbl_GreaterEqual class attributes and methods

# dbl_Less class attributes and methods

# dbl_LessEqual class attributes and methods

# dbl_InstanceOf class attributes and methods

# dbl_Plus class attributes and methods

# L4Expr class attributes and methods

# dbl_Minus class attributes and methods

# dbl_Mul class attributes and methods

# L3Expr class attributes and methods

# dbl_Mod class attributes and methods

# dbl_UnaryOperator class attributes and methods

# dbl_UniqueIdExpr class attributes and methods
dbl_UniqueIdExpr_identifier: Property = Property(name="identifier", type=StringType)
dbl_UniqueIdExpr.attributes={dbl_UniqueIdExpr_identifier}

# dbl_ParseExpr class attributes and methods

# dbl_PredefinedId class attributes and methods

# dbl_MeLiteral class attributes and methods

# PredefinedId class attributes and methods

# dbl_SuperLiteral class attributes and methods

# dbl_MetaLiteral class attributes and methods

# dbl_TypeLiteral class attributes and methods

# dbl_SizeOfArray class attributes and methods

# dbl_CallPart class attributes and methods

# dbl_ElementAccess class attributes and methods

# dbl_Div class attributes and methods

# dbl_Neg class attributes and methods

# UnaryOperator class attributes and methods

# L2Expr class attributes and methods

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

# ElementAccess class attributes and methods

# dbl_MetaAccess class attributes and methods

# VariableAccess class attributes and methods

# dbl_TypeAccess class attributes and methods

# dbl_LanguageConceptClassifier class attributes and methods

# dbl_TextualSyntaxDef class attributes and methods

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

# dbl_MetaExpr class attributes and methods

# dbl_PropertyBindingExpr class attributes and methods

# dbl_PropertyType class attributes and methods

# dbl_RhsClassifierExpr class attributes and methods

# dbl_ExpandVariablePart class attributes and methods

# dbl_SetExpansionContextStatement class attributes and methods
dbl_SetExpansionContextStatement_addAfterContext: Property = Property(name="addAfterContext", type=BooleanType)
dbl_SetExpansionContextStatement.attributes={dbl_SetExpansionContextStatement_addAfterContext}

# dbl_SaveGenStatement class attributes and methods

# dbl_ResumeGenStatement class attributes and methods

# dbl_ExpandExpression class attributes and methods

# dbl_ExpandStatement class attributes and methods

# dbl_TargetStatement class attributes and methods

# dbl_ExpansionStatement class attributes and methods

# dbl_ExpansionPart class attributes and methods

# dbl_ExpandTextPart class attributes and methods
dbl_ExpandTextPart_text: Property = Property(name="text", type=StringType)
dbl_ExpandTextPart.attributes={dbl_ExpandTextPart_text}

# ExpansionPart class attributes and methods

# dbl_Pattern class attributes and methods
dbl_Pattern_top: Property = Property(name="top", type=BooleanType)
dbl_Pattern.attributes={dbl_Pattern_top}

# dbl_TestStatement class attributes and methods
dbl_TestStatement_value: Property = Property(name="value", type=IntegerType)
dbl_TestStatement.attributes={dbl_TestStatement_value}

# dbl_CodeQuoteExpression class attributes and methods

# dbl_QuotedCode class attributes and methods

# dbl_QuotedExpression class attributes and methods

# QuotedCode class attributes and methods

# dbl_QuotedStatements class attributes and methods

# dbl_QuotedClassContent class attributes and methods

# Class class attributes and methods

# dbl_QuotedModuleContent class attributes and methods

# Module class attributes and methods

# Relationships
expandExpr0: BinaryAssociation = BinaryAssociation(
    name="expandExpr0",
    ends={
        Property(name="dbl_ExpandExpr", type=dbl_Construct, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Construct", type=dbl_ExpandExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
placeHolder819: BinaryAssociation = BinaryAssociation(
    name="placeHolder819",
    ends={
        Property(name="dbl_ExtensibleElement20", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement18", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
placeHolder922: BinaryAssociation = BinaryAssociation(
    name="placeHolder922",
    ends={
        Property(name="dbl_ExtensibleElement23", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement21", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
placeHolder1025: BinaryAssociation = BinaryAssociation(
    name="placeHolder1025",
    ends={
        Property(name="dbl_ExtensibleElement26", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement24", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
imports27: BinaryAssociation = BinaryAssociation(
    name="imports27",
    ends={
        Property(name="dbl_Import", type=dbl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Model", type=dbl_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules28: BinaryAssociation = BinaryAssociation(
    name="modules28",
    ends={
        Property(name="dbl_Module", type=dbl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Model29", type=dbl_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model30: BinaryAssociation = BinaryAssociation(
    name="model30",
    ends={
        Property(name="dbl_Model32", type=dbl_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Import31", type=dbl_Model, multiplicity=Multiplicity(0, 1))
    }
)
classes33: BinaryAssociation = BinaryAssociation(
    name="classes33",
    ends={
        Property(name="dbl_Class", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module34", type=dbl_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionDefinitions35: BinaryAssociation = BinaryAssociation(
    name="extensionDefinitions35",
    ends={
        Property(name="dbl_ExtensionDefinition", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module36", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionSemanticsDefinitions37: BinaryAssociation = BinaryAssociation(
    name="extensionSemanticsDefinitions37",
    ends={
        Property(name="dbl_ExtensionSemanticsDefinition", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module38", type=dbl_ExtensionSemanticsDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
placeHolder12: BinaryAssociation = BinaryAssociation(
    name="placeHolder12",
    ends={
        Property(name="dbl_ExtensibleElement", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement1", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
placeHolder24: BinaryAssociation = BinaryAssociation(
    name="placeHolder24",
    ends={
        Property(name="dbl_ExtensibleElement5", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement3", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
placeHolder37: BinaryAssociation = BinaryAssociation(
    name="placeHolder37",
    ends={
        Property(name="dbl_ExtensibleElement8", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement6", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
placeHolder410: BinaryAssociation = BinaryAssociation(
    name="placeHolder410",
    ends={
        Property(name="dbl_ExtensibleElement11", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement9", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
placeHolder513: BinaryAssociation = BinaryAssociation(
    name="placeHolder513",
    ends={
        Property(name="dbl_ExtensibleElement14", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement12", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
placeHolder616: BinaryAssociation = BinaryAssociation(
    name="placeHolder616",
    ends={
        Property(name="dbl_ExtensibleElement17", type=dbl_ExtensibleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensibleElement15", type=dbl_ExtensibleElement, multiplicity=Multiplicity(0, 1))
    }
)
primitiveType45: BinaryAssociation = BinaryAssociation(
    name="primitiveType45",
    ends={
        Property(name="dbl_PrimitiveType", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement", type=dbl_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArrayDimensions46: BinaryAssociation = BinaryAssociation(
    name="typeArrayDimensions46",
    ends={
        Property(name="dbl_ArrayDimension48", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement47", type=dbl_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierType49: BinaryAssociation = BinaryAssociation(
    name="classifierType49",
    ends={
        Property(name="dbl_IdExpr", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement50", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size51: BinaryAssociation = BinaryAssociation(
    name="size51",
    ends={
        Property(name="dbl_Expression", type=dbl_ArrayDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ArrayDimension52", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters53: BinaryAssociation = BinaryAssociation(
    name="parameters53",
    ends={
        Property(name="dbl_Parameter", type=dbl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Function54", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions39: BinaryAssociation = BinaryAssociation(
    name="functions39",
    ends={
        Property(name="dbl_Function", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module40", type=dbl_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables41: BinaryAssociation = BinaryAssociation(
    name="variables41",
    ends={
        Property(name="dbl_Variable", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module42", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentExtensions43: BinaryAssociation = BinaryAssociation(
    name="contentExtensions43",
    ends={
        Property(name="dbl_ConstructiveExtension", type=dbl_ConstructiveExtensionAtContentExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ConstructiveExtensionAtContentExtensionPoint", type=dbl_ConstructiveExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayDimensions44: BinaryAssociation = BinaryAssociation(
    name="arrayDimensions44",
    ends={
        Property(name="dbl_ArrayDimension", type=dbl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Type", type=dbl_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors65: BinaryAssociation = BinaryAssociation(
    name="constructors65",
    ends={
        Property(name="owningClass", type=dbl_Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Constructor", type=dbl_Class, multiplicity=Multiplicity(1, 1))
    }
)
attributes66: BinaryAssociation = BinaryAssociation(
    name="attributes66",
    ends={
        Property(name="dbl_Variable68", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class67", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods69: BinaryAssociation = BinaryAssociation(
    name="methods69",
    ends={
        Property(name="dbl_Function71", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class70", type=dbl_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsBlock72: BinaryAssociation = BinaryAssociation(
    name="actionsBlock72",
    ends={
        Property(name="dbl_LocalScope", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class73", type=dbl_LocalScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters74: BinaryAssociation = BinaryAssociation(
    name="parameters74",
    ends={
        Property(name="dbl_Parameter75", type=dbl_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Constructor", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningClass76: BinaryAssociation = BinaryAssociation(
    name="owningClass76",
    ends={
        Property(name="Class", type=dbl_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="constructors", type=dbl_Class, multiplicity=Multiplicity(1, 1))
    }
)
initialValue77: BinaryAssociation = BinaryAssociation(
    name="initialValue77",
    ends={
        Property(name="dbl_Expression79", type=dbl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Variable78", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class55: BinaryAssociation = BinaryAssociation(
    name="class55",
    ends={
        Property(name="dbl_Class56", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SuperClassSpecification", type=dbl_Class, multiplicity=Multiplicity(1, 1))
    }
)
constructorArguments57: BinaryAssociation = BinaryAssociation(
    name="constructorArguments57",
    ends={
        Property(name="dbl_Expression59", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SuperClassSpecification58", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings60: BinaryAssociation = BinaryAssociation(
    name="bindings60",
    ends={
        Property(name="dbl_NativeBinding", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class61", type=dbl_NativeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClasses62: BinaryAssociation = BinaryAssociation(
    name="superClasses62",
    ends={
        Property(name="dbl_SuperClassSpecification64", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class63", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectAccess90: BinaryAssociation = BinaryAssociation(
    name="objectAccess90",
    ends={
        Property(name="dbl_Expression91", type=dbl_Reactivate, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Reactivate", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess92: BinaryAssociation = BinaryAssociation(
    name="objectAccess92",
    ends={
        Property(name="dbl_Expression93", type=dbl_ActivateObject, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ActivateObject", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
time94: BinaryAssociation = BinaryAssociation(
    name="time94",
    ends={
        Property(name="dbl_Expression95", type=dbl_Advance, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Advance", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputs96: BinaryAssociation = BinaryAssociation(
    name="outputs96",
    ends={
        Property(name="dbl_Expression97", type=dbl_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Print", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition98: BinaryAssociation = BinaryAssociation(
    name="condition98",
    ends={
        Property(name="dbl_Expression99", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueCase100: BinaryAssociation = BinaryAssociation(
    name="trueCase100",
    ends={
        Property(name="dbl_Statement", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement101", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseCase102: BinaryAssociation = BinaryAssociation(
    name="falseCase102",
    ends={
        Property(name="dbl_Statement104", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement103", type=dbl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements105: BinaryAssociation = BinaryAssociation(
    name="statements105",
    ends={
        Property(name="dbl_Statement107", type=dbl_LocalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_LocalScope106", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable80: BinaryAssociation = BinaryAssociation(
    name="variable80",
    ends={
        Property(name="dbl_VariableAccess", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value81: BinaryAssociation = BinaryAssociation(
    name="value81",
    ends={
        Property(name="dbl_Expression83", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment82", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callIdExpr84: BinaryAssociation = BinaryAssociation(
    name="callIdExpr84",
    ends={
        Property(name="dbl_IdExpr85", type=dbl_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_FunctionCall", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value86: BinaryAssociation = BinaryAssociation(
    name="value86",
    ends={
        Property(name="dbl_Expression87", type=dbl_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Return", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition88: BinaryAssociation = BinaryAssociation(
    name="condition88",
    ends={
        Property(name="dbl_Expression89", type=dbl_WaitUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WaitUntil", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
termination108: BinaryAssociation = BinaryAssociation(
    name="termination108",
    ends={
        Property(name="dbl_Expression109", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
increment110: BinaryAssociation = BinaryAssociation(
    name="increment110",
    ends={
        Property(name="dbl_Assignment112", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement111", type=dbl_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body113: BinaryAssociation = BinaryAssociation(
    name="body113",
    ends={
        Property(name="dbl_Statement115", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement114", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition116: BinaryAssociation = BinaryAssociation(
    name="condition116",
    ends={
        Property(name="dbl_Expression117", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body118: BinaryAssociation = BinaryAssociation(
    name="body118",
    ends={
        Property(name="dbl_Statement120", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement119", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op1134: BinaryAssociation = BinaryAssociation(
    name="op1134",
    ends={
        Property(name="dbl_Expression135", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op2136: BinaryAssociation = BinaryAssociation(
    name="op2136",
    ends={
        Property(name="dbl_Expression138", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator137", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable121: BinaryAssociation = BinaryAssociation(
    name="variable121",
    ends={
        Property(name="dbl_VariableAccess122", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases123: BinaryAssociation = BinaryAssociation(
    name="cases123",
    ends={
        Property(name="dbl_SwitchCase", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement124", type=dbl_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultCase125: BinaryAssociation = BinaryAssociation(
    name="defaultCase125",
    ends={
        Property(name="dbl_SwitchCase127", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement126", type=dbl_SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value128: BinaryAssociation = BinaryAssociation(
    name="value128",
    ends={
        Property(name="dbl_Expression130", type=dbl_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchCase129", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body131: BinaryAssociation = BinaryAssociation(
    name="body131",
    ends={
        Property(name="dbl_Statement133", type=dbl_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchCase132", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op139: BinaryAssociation = BinaryAssociation(
    name="op139",
    ends={
        Property(name="dbl_Expression140", type=dbl_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_UnaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr141: BinaryAssociation = BinaryAssociation(
    name="expr141",
    ends={
        Property(name="dbl_Expression143", type=dbl_ExpandExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandExpr142", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
astPart144: BinaryAssociation = BinaryAssociation(
    name="astPart144",
    ends={
        Property(name="dbl_Construct145", type=dbl_ParseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ParseExpr", type=dbl_Construct, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentIdExpr147: BinaryAssociation = BinaryAssociation(
    name="parentIdExpr147",
    ends={
        Property(name="dbl_IdExpr148", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr146", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedElement149: BinaryAssociation = BinaryAssociation(
    name="referencedElement149",
    ends={
        Property(name="dbl_NamedElement", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr150", type=dbl_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
predefinedId151: BinaryAssociation = BinaryAssociation(
    name="predefinedId151",
    ends={
        Property(name="dbl_PredefinedId", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr152", type=dbl_PredefinedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayIndex153: BinaryAssociation = BinaryAssociation(
    name="arrayIndex153",
    ends={
        Property(name="dbl_Expression155", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr154", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callPart156: BinaryAssociation = BinaryAssociation(
    name="callPart156",
    ends={
        Property(name="dbl_CallPart", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr157", type=dbl_CallPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callArguments158: BinaryAssociation = BinaryAssociation(
    name="callArguments158",
    ends={
        Property(name="dbl_Expression160", type=dbl_CallPart, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CallPart159", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
syntaxDefinition170: BinaryAssociation = BinaryAssociation(
    name="syntaxDefinition170",
    ends={
        Property(name="dbl_ExtensionDefinition172", type=dbl_ExtensionSemanticsDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionSemanticsDefinition171", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1))
    }
)
startRule173: BinaryAssociation = BinaryAssociation(
    name="startRule173",
    ends={
        Property(name="dbl_TsRule", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TextualSyntaxDef174", type=dbl_TsRule, multiplicity=Multiplicity(1, 1))
    }
)
rules175: BinaryAssociation = BinaryAssociation(
    name="rules175",
    ends={
        Property(name="dbl_TsRule177", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TextualSyntaxDef176", type=dbl_TsRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rhs178: BinaryAssociation = BinaryAssociation(
    name="rhs178",
    ends={
        Property(name="dbl_RhsExpression", type=dbl_TsRule, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TsRule179", type=dbl_RhsExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequence180: BinaryAssociation = BinaryAssociation(
    name="sequence180",
    ends={
        Property(name="dbl_RhsExpression181", type=dbl_SequenceExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SequenceExpr", type=dbl_RhsExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idExpr161: BinaryAssociation = BinaryAssociation(
    name="idExpr161",
    ends={
        Property(name="dbl_IdExpr162", type=dbl_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ElementAccess", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedConcept163: BinaryAssociation = BinaryAssociation(
    name="extendedConcept163",
    ends={
        Property(name="dbl_LanguageConceptClassifier", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition164", type=dbl_LanguageConceptClassifier, multiplicity=Multiplicity(1, 1))
    }
)
abstractSyntaxDef165: BinaryAssociation = BinaryAssociation(
    name="abstractSyntaxDef165",
    ends={
        Property(name="dbl_Class167", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition166", type=dbl_Class, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
textualSyntaxDef168: BinaryAssociation = BinaryAssociation(
    name="textualSyntaxDef168",
    ends={
        Property(name="dbl_TextualSyntaxDef", type=dbl_ExtensionDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionDefinition169", type=dbl_TextualSyntaxDef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type184: BinaryAssociation = BinaryAssociation(
    name="type184",
    ends={
        Property(name="dbl_LanguageConstructClassifier185", type=dbl_StructuredPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_StructuredPropertyType", type=dbl_LanguageConstructClassifier, multiplicity=Multiplicity(1, 1))
    }
)
expr186: BinaryAssociation = BinaryAssociation(
    name="expr186",
    ends={
        Property(name="dbl_Expression187", type=dbl_MetaExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MetaExpr", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
propertyType182: BinaryAssociation = BinaryAssociation(
    name="propertyType182",
    ends={
        Property(name="dbl_PropertyType", type=dbl_PropertyBindingExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_PropertyBindingExpr", type=dbl_PropertyType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classifier183: BinaryAssociation = BinaryAssociation(
    name="classifier183",
    ends={
        Property(name="dbl_LanguageConstructClassifier", type=dbl_RhsClassifierExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_RhsClassifierExpr", type=dbl_LanguageConstructClassifier, multiplicity=Multiplicity(1, 1))
    }
)
expr194: BinaryAssociation = BinaryAssociation(
    name="expr194",
    ends={
        Property(name="dbl_Expression195", type=dbl_ExpandVariablePart, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandVariablePart", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context196: BinaryAssociation = BinaryAssociation(
    name="context196",
    ends={
        Property(name="dbl_Expression197", type=dbl_SetExpansionContextStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SetExpansionContextStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable198: BinaryAssociation = BinaryAssociation(
    name="variable198",
    ends={
        Property(name="dbl_Expression199", type=dbl_SaveGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SaveGenStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable200: BinaryAssociation = BinaryAssociation(
    name="variable200",
    ends={
        Property(name="dbl_Expression201", type=dbl_ResumeGenStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ResumeGenStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject202: BinaryAssociation = BinaryAssociation(
    name="metaObject202",
    ends={
        Property(name="dbl_Expression203", type=dbl_ExpandExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject204: BinaryAssociation = BinaryAssociation(
    name="metaObject204",
    ends={
        Property(name="dbl_Expression205", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location206: BinaryAssociation = BinaryAssociation(
    name="location206",
    ends={
        Property(name="dbl_Expression208", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement207", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body188: BinaryAssociation = BinaryAssociation(
    name="body188",
    ends={
        Property(name="dbl_Statement189", type=dbl_TargetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TargetStatement", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parts190: BinaryAssociation = BinaryAssociation(
    name="parts190",
    ends={
        Property(name="dbl_ExpansionPart", type=dbl_ExpansionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpansionStatement", type=dbl_ExpansionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs191: BinaryAssociation = BinaryAssociation(
    name="exprs191",
    ends={
        Property(name="dbl_Expression193", type=dbl_ExpansionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpansionStatement192", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context214: BinaryAssociation = BinaryAssociation(
    name="context214",
    ends={
        Property(name="dbl_Parameter215", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern", type=dbl_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body216: BinaryAssociation = BinaryAssociation(
    name="body216",
    ends={
        Property(name="dbl_Statement218", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern217", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
quotedCode209: BinaryAssociation = BinaryAssociation(
    name="quotedCode209",
    ends={
        Property(name="dbl_QuotedCode", type=dbl_CodeQuoteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CodeQuoteExpression", type=dbl_QuotedCode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression210: BinaryAssociation = BinaryAssociation(
    name="expression210",
    ends={
        Property(name="dbl_Expression211", type=dbl_QuotedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements212: BinaryAssociation = BinaryAssociation(
    name="statements212",
    ends={
        Property(name="dbl_Statement213", type=dbl_QuotedStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedStatements", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dbl_Module_NamedElement = Generalization(general=NamedElement, specific=dbl_Module)
gen_dbl_Module_ConstructiveExtensionAtContentExtensionPoint = Generalization(general=ConstructiveExtensionAtContentExtensionPoint, specific=dbl_Module)
gen_dbl_Module_Construct = Generalization(general=Construct, specific=dbl_Module)
gen_dbl_ExtensibleElement_NamedElement = Generalization(general=NamedElement, specific=dbl_ExtensibleElement)
gen_dbl_ExtensibleElement_Construct = Generalization(general=Construct, specific=dbl_ExtensibleElement)
gen_dbl_PrimitiveType_Type = Generalization(general=Type, specific=dbl_PrimitiveType)
gen_dbl_VoidType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_VoidType)
gen_dbl_IntType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_IntType)
gen_dbl_BoolType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_BoolType)
gen_dbl_DoubleType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_DoubleType)
gen_dbl_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_StringType)
gen_dbl_Function_NamedElement = Generalization(general=NamedElement, specific=dbl_Function)
gen_dbl_Function_TypedElement = Generalization(general=TypedElement, specific=dbl_Function)
gen_dbl_Function_LocalScope = Generalization(general=LocalScope, specific=dbl_Function)
gen_dbl_ConstructiveExtension_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ConstructiveExtension)
gen_dbl_ModuleContent_ConstructiveExtension = Generalization(general=ConstructiveExtension, specific=dbl_ModuleContent)
gen_dbl_ClassContent_ConstructiveExtension = Generalization(general=ConstructiveExtension, specific=dbl_ClassContent)
gen_dbl_Constructor_LocalScope = Generalization(general=LocalScope, specific=dbl_Constructor)
gen_dbl_AbstractVariable_NamedElement = Generalization(general=NamedElement, specific=dbl_AbstractVariable)
gen_dbl_AbstractVariable_TypedElement = Generalization(general=TypedElement, specific=dbl_AbstractVariable)
gen_dbl_Variable_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Variable)
gen_dbl_Variable_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Variable)
gen_dbl_Parameter_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Parameter)
gen_dbl_Statement_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_Statement)
gen_dbl_LoopStatement_Statement = Generalization(general=Statement, specific=dbl_LoopStatement)
gen_dbl_SimpleStatement_Statement = Generalization(general=Statement, specific=dbl_SimpleStatement)
gen_dbl_Class_NamedElement = Generalization(general=NamedElement, specific=dbl_Class)
gen_dbl_Class_Type = Generalization(general=Type, specific=dbl_Class)
gen_dbl_Class_ConstructiveExtensionAtContentExtensionPoint = Generalization(general=ConstructiveExtensionAtContentExtensionPoint, specific=dbl_Class)
gen_dbl_Class_LanguageConceptClassifier = Generalization(general=LanguageConceptClassifier, specific=dbl_Class)
gen_dbl_Class_Construct = Generalization(general=Construct, specific=dbl_Class)
gen_dbl_Terminate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Terminate)
gen_dbl_Yield_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Yield)
gen_dbl_Wait_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Wait)
gen_dbl_Reactivate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Reactivate)
gen_dbl_ActivateObject_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ActivateObject)
gen_dbl_Advance_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Advance)
gen_dbl_Print_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Print)
gen_dbl_IfStatement_Statement = Generalization(general=Statement, specific=dbl_IfStatement)
gen_dbl_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Assignment)
gen_dbl_FunctionCall_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_FunctionCall)
gen_dbl_Return_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Return)
gen_dbl_WaitUntil_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_WaitUntil)
gen_dbl_SwitchStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SwitchStatement)
gen_dbl_LocalScopeStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_LocalScopeStatement)
gen_dbl_LocalScopeStatement_LocalScope = Generalization(general=LocalScope, specific=dbl_LocalScopeStatement)
gen_dbl_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=dbl_ForStatement)
gen_dbl_ForStatement_LocalScope = Generalization(general=LocalScope, specific=dbl_ForStatement)
gen_dbl_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=dbl_WhileStatement)
gen_dbl_L1Expr_Expression = Generalization(general=Expression, specific=dbl_L1Expr)
gen_dbl_L2Expr_Expression = Generalization(general=Expression, specific=dbl_L2Expr)
gen_dbl_L3Expr_Expression = Generalization(general=Expression, specific=dbl_L3Expr)
gen_dbl_L4Expr_Expression = Generalization(general=Expression, specific=dbl_L4Expr)
gen_dbl_L5Expr_Expression = Generalization(general=Expression, specific=dbl_L5Expr)
gen_dbl_L6Expr_Expression = Generalization(general=Expression, specific=dbl_L6Expr)
gen_dbl_L7Expr_Expression = Generalization(general=Expression, specific=dbl_L7Expr)
gen_dbl_L8Expr_Expression = Generalization(general=Expression, specific=dbl_L8Expr)
gen_dbl_L9Expr_Expression = Generalization(general=Expression, specific=dbl_L9Expr)
gen_dbl_BinaryOperator_Expression = Generalization(general=Expression, specific=dbl_BinaryOperator)
gen_dbl_BreakStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_BreakStatement)
gen_dbl_ContinueStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ContinueStatement)
gen_dbl_Expression_TypedElement = Generalization(general=TypedElement, specific=dbl_Expression)
gen_dbl_Expression_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_Expression)
gen_dbl_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Or)
gen_dbl_Or_L8Expr = Generalization(general=L8Expr, specific=dbl_Or)
gen_dbl_And_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_And)
gen_dbl_And_L7Expr = Generalization(general=L7Expr, specific=dbl_And)
gen_dbl_NotEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_NotEqual)
gen_dbl_NotEqual_L6Expr = Generalization(general=L6Expr, specific=dbl_NotEqual)
gen_dbl_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Equal)
gen_dbl_Equal_L6Expr = Generalization(general=L6Expr, specific=dbl_Equal)
gen_dbl_Greater_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Greater)
gen_dbl_Greater_L5Expr = Generalization(general=L5Expr, specific=dbl_Greater)
gen_dbl_GreaterEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_GreaterEqual)
gen_dbl_GreaterEqual_L5Expr = Generalization(general=L5Expr, specific=dbl_GreaterEqual)
gen_dbl_Less_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Less)
gen_dbl_Less_L5Expr = Generalization(general=L5Expr, specific=dbl_Less)
gen_dbl_LessEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_LessEqual)
gen_dbl_LessEqual_L5Expr = Generalization(general=L5Expr, specific=dbl_LessEqual)
gen_dbl_InstanceOf_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_InstanceOf)
gen_dbl_InstanceOf_L5Expr = Generalization(general=L5Expr, specific=dbl_InstanceOf)
gen_dbl_Plus_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Plus)
gen_dbl_Plus_L4Expr = Generalization(general=L4Expr, specific=dbl_Plus)
gen_dbl_Minus_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Minus)
gen_dbl_Minus_L4Expr = Generalization(general=L4Expr, specific=dbl_Minus)
gen_dbl_Mul_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Mul)
gen_dbl_Mul_L3Expr = Generalization(general=L3Expr, specific=dbl_Mul)
gen_dbl_Mod_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Mod)
gen_dbl_Mod_L3Expr = Generalization(general=L3Expr, specific=dbl_Mod)
gen_dbl_UnaryOperator_Expression = Generalization(general=Expression, specific=dbl_UnaryOperator)
gen_dbl_UniqueIdExpr_Expression = Generalization(general=Expression, specific=dbl_UniqueIdExpr)
gen_dbl_ExpandExpr_Expression = Generalization(general=Expression, specific=dbl_ExpandExpr)
gen_dbl_ParseExpr_Expression = Generalization(general=Expression, specific=dbl_ParseExpr)
gen_dbl_MeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MeLiteral)
gen_dbl_SuperLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SuperLiteral)
gen_dbl_MetaLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MetaLiteral)
gen_dbl_TypeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_TypeLiteral)
gen_dbl_SizeOfArray_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SizeOfArray)
gen_dbl_IdExpr_L1Expr = Generalization(general=L1Expr, specific=dbl_IdExpr)
gen_dbl_ElementAccess_Expression = Generalization(general=Expression, specific=dbl_ElementAccess)
gen_dbl_Div_BinaryOperator = Generalization(general=BinaryOperator, specific=dbl_Div)
gen_dbl_Div_L3Expr = Generalization(general=L3Expr, specific=dbl_Div)
gen_dbl_Neg_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Neg)
gen_dbl_Neg_L2Expr = Generalization(general=L2Expr, specific=dbl_Neg)
gen_dbl_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Not)
gen_dbl_Not_L2Expr = Generalization(general=L2Expr, specific=dbl_Not)
gen_dbl_Cast_UnaryOperator = Generalization(general=UnaryOperator, specific=dbl_Cast)
gen_dbl_Cast_TypedElement = Generalization(general=TypedElement, specific=dbl_Cast)
gen_dbl_Cast_L2Expr = Generalization(general=L2Expr, specific=dbl_Cast)
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
gen_dbl_ExtensionSemanticsDefinition_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ExtensionSemanticsDefinition)
gen_dbl_ExtensionSemanticsDefinition_LocalScope = Generalization(general=LocalScope, specific=dbl_ExtensionSemanticsDefinition)
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
gen_dbl_VariableAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_VariableAccess)
gen_dbl_MetaAccess_VariableAccess = Generalization(general=VariableAccess, specific=dbl_MetaAccess)
gen_dbl_TypeAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_TypeAccess)
gen_dbl_ExtensionDefinition_LanguageConceptClassifier = Generalization(general=LanguageConceptClassifier, specific=dbl_ExtensionDefinition)
gen_dbl_ExtensionDefinition_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ExtensionDefinition)
gen_dbl_IdPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_IdPropertyType)
gen_dbl_IntPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_IntPropertyType)
gen_dbl_StringPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_StringPropertyType)
gen_dbl_BooleanPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_BooleanPropertyType)
gen_dbl_StructuredPropertyType_PropertyType = Generalization(general=PropertyType, specific=dbl_StructuredPropertyType)
gen_dbl_CompositePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=dbl_CompositePropertyType)
gen_dbl_ReferencePropertyType_StructuredPropertyType = Generalization(general=StructuredPropertyType, specific=dbl_ReferencePropertyType)
gen_dbl_MetaExpr_Expression = Generalization(general=Expression, specific=dbl_MetaExpr)
gen_dbl_PropertyBindingExpr_NamedElement = Generalization(general=NamedElement, specific=dbl_PropertyBindingExpr)
gen_dbl_PropertyBindingExpr_L1RhsExpr = Generalization(general=L1RhsExpr, specific=dbl_PropertyBindingExpr)
gen_dbl_RhsClassifierExpr_L1RhsExpr = Generalization(general=L1RhsExpr, specific=dbl_RhsClassifierExpr)
gen_dbl_ExpandVariablePart_ExpansionPart = Generalization(general=ExpansionPart, specific=dbl_ExpandVariablePart)
gen_dbl_SetExpansionContextStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SetExpansionContextStatement)
gen_dbl_SaveGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SaveGenStatement)
gen_dbl_ResumeGenStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ResumeGenStatement)
gen_dbl_ExpandExpression_Expression = Generalization(general=Expression, specific=dbl_ExpandExpression)
gen_dbl_ExpandStatement_Statement = Generalization(general=Statement, specific=dbl_ExpandStatement)
gen_dbl_TargetStatement_Statement = Generalization(general=Statement, specific=dbl_TargetStatement)
gen_dbl_ExpansionStatement_Statement = Generalization(general=Statement, specific=dbl_ExpansionStatement)
gen_dbl_ExpandTextPart_ExpansionPart = Generalization(general=ExpansionPart, specific=dbl_ExpandTextPart)
gen_dbl_Pattern_NamedElement = Generalization(general=NamedElement, specific=dbl_Pattern)
gen_dbl_TestStatement_Statement = Generalization(general=Statement, specific=dbl_TestStatement)
gen_dbl_CodeQuoteExpression_Expression = Generalization(general=Expression, specific=dbl_CodeQuoteExpression)
gen_dbl_QuotedExpression_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedExpression)
gen_dbl_QuotedStatements_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedStatements)
gen_dbl_QuotedClassContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedClassContent)
gen_dbl_QuotedClassContent_Class = Generalization(general=Class_, specific=dbl_QuotedClassContent)
gen_dbl_QuotedModuleContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedModuleContent)
gen_dbl_QuotedModuleContent_Module = Generalization(general=Module, specific=dbl_QuotedModuleContent)

# Domain Model
domain_model = DomainModel(
    name="dbl",
    types={dbl_Construct, dbl_ExpandExpr, dbl_Model, dbl_Import, dbl_Module, ConstructiveExtensionAtContentExtensionPoint, dbl_Class, dbl_ExtensionDefinition, dbl_ExtensionSemanticsDefinition, dbl_ExtensibleElement, NamedElement, Construct, dbl_PrimitiveType, dbl_IdExpr, dbl_Expression, Type, dbl_VoidType, PrimitiveType, dbl_IntType, dbl_BoolType, dbl_DoubleType, dbl_StringType, TypedElement, LocalScope, dbl_Parameter, dbl_NativeBinding, dbl_Function, dbl_Variable, dbl_ConstructiveExtension, ExtensibleElement, dbl_ConstructiveExtensionAtContentExtensionPoint, dbl_ModuleContent, ConstructiveExtension, dbl_ClassContent, dbl_Type, dbl_ArrayDimension, dbl_TypedElement, dbl_LocalScope, dbl_AbstractVariable, AbstractVariable, SimpleStatement, dbl_NamedElement, dbl_Statement, dbl_LoopStatement, Statement, dbl_SimpleStatement, dbl_SuperClassSpecification, LanguageConceptClassifier, dbl_Constructor, dbl_Terminate, dbl_Yield, dbl_Wait, dbl_Reactivate, dbl_ActivateObject, dbl_Advance, dbl_Print, dbl_IfStatement, dbl_Assignment, dbl_VariableAccess, dbl_FunctionCall, dbl_Return, dbl_WaitUntil, dbl_SwitchStatement, dbl_LocalScopeStatement, dbl_ForStatement, LoopStatement, dbl_WhileStatement, dbl_L2Expr, dbl_L3Expr, dbl_L4Expr, dbl_L5Expr, dbl_L6Expr, dbl_L7Expr, dbl_L8Expr, dbl_L9Expr, dbl_BinaryOperator, dbl_SwitchCase, dbl_BreakStatement, dbl_ContinueStatement, dbl_L1Expr, Expression, dbl_Or, BinaryOperator, L8Expr, dbl_And, L7Expr, dbl_NotEqual, L6Expr, dbl_Equal, dbl_Greater, L5Expr, dbl_GreaterEqual, dbl_Less, dbl_LessEqual, dbl_InstanceOf, dbl_Plus, L4Expr, dbl_Minus, dbl_Mul, L3Expr, dbl_Mod, dbl_UnaryOperator, dbl_UniqueIdExpr, dbl_ParseExpr, dbl_PredefinedId, dbl_MeLiteral, PredefinedId, dbl_SuperLiteral, dbl_MetaLiteral, dbl_TypeLiteral, dbl_SizeOfArray, dbl_CallPart, dbl_ElementAccess, dbl_Div, dbl_Neg, UnaryOperator, L2Expr, dbl_Not, dbl_Cast, dbl_CreateObject, L1Expr, dbl_NullLiteral, dbl_TimeLiteral, dbl_ActiveLiteral, dbl_StringLiteral, dbl_IntLiteral, dbl_TrueLiteral, dbl_FalseLiteral, dbl_DoubleLiteral, dbl_TsRule, dbl_LanguageConstructClassifier, LanguageConstructClassifier, dbl_RhsExpression, dbl_L3RhsExpr, RhsExpression, dbl_L2RhsExpr, dbl_SequenceExpr, L2RhsExpr, dbl_L1RhsExpr, dbl_TerminalExpr, L1RhsExpr, ElementAccess, dbl_MetaAccess, VariableAccess, dbl_TypeAccess, dbl_LanguageConceptClassifier, dbl_TextualSyntaxDef, dbl_IdPropertyType, PropertyType, dbl_IntPropertyType, dbl_StringPropertyType, dbl_BooleanPropertyType, dbl_StructuredPropertyType, dbl_CompositePropertyType, StructuredPropertyType, dbl_ReferencePropertyType, dbl_MetaExpr, dbl_PropertyBindingExpr, dbl_PropertyType, dbl_RhsClassifierExpr, dbl_ExpandVariablePart, dbl_SetExpansionContextStatement, dbl_SaveGenStatement, dbl_ResumeGenStatement, dbl_ExpandExpression, dbl_ExpandStatement, dbl_TargetStatement, dbl_ExpansionStatement, dbl_ExpansionPart, dbl_ExpandTextPart, ExpansionPart, dbl_Pattern, dbl_TestStatement, dbl_CodeQuoteExpression, dbl_QuotedCode, dbl_QuotedExpression, QuotedCode, dbl_QuotedStatements, dbl_QuotedClassContent, Class_, dbl_QuotedModuleContent, Module},
    associations={expandExpr0, placeHolder819, placeHolder922, placeHolder1025, imports27, modules28, model30, classes33, extensionDefinitions35, extensionSemanticsDefinitions37, placeHolder12, placeHolder24, placeHolder37, placeHolder410, placeHolder513, placeHolder616, primitiveType45, typeArrayDimensions46, classifierType49, size51, parameters53, functions39, variables41, contentExtensions43, arrayDimensions44, constructors65, attributes66, methods69, actionsBlock72, parameters74, owningClass76, initialValue77, class55, constructorArguments57, bindings60, superClasses62, objectAccess90, objectAccess92, time94, outputs96, condition98, trueCase100, falseCase102, statements105, variable80, value81, callIdExpr84, value86, condition88, termination108, increment110, body113, condition116, body118, op1134, op2136, variable121, cases123, defaultCase125, value128, body131, op139, expr141, astPart144, parentIdExpr147, referencedElement149, predefinedId151, arrayIndex153, callPart156, callArguments158, syntaxDefinition170, startRule173, rules175, rhs178, sequence180, idExpr161, extendedConcept163, abstractSyntaxDef165, textualSyntaxDef168, type184, expr186, propertyType182, classifier183, expr194, context196, variable198, variable200, metaObject202, metaObject204, location206, body188, parts190, exprs191, context214, body216, quotedCode209, expression210, statements212},
    generalizations={gen_dbl_Module_NamedElement, gen_dbl_Module_ConstructiveExtensionAtContentExtensionPoint, gen_dbl_Module_Construct, gen_dbl_ExtensibleElement_NamedElement, gen_dbl_ExtensibleElement_Construct, gen_dbl_PrimitiveType_Type, gen_dbl_VoidType_PrimitiveType, gen_dbl_IntType_PrimitiveType, gen_dbl_BoolType_PrimitiveType, gen_dbl_DoubleType_PrimitiveType, gen_dbl_StringType_PrimitiveType, gen_dbl_Function_NamedElement, gen_dbl_Function_TypedElement, gen_dbl_Function_LocalScope, gen_dbl_ConstructiveExtension_ExtensibleElement, gen_dbl_ModuleContent_ConstructiveExtension, gen_dbl_ClassContent_ConstructiveExtension, gen_dbl_Constructor_LocalScope, gen_dbl_AbstractVariable_NamedElement, gen_dbl_AbstractVariable_TypedElement, gen_dbl_Variable_AbstractVariable, gen_dbl_Variable_SimpleStatement, gen_dbl_Parameter_AbstractVariable, gen_dbl_Statement_ExtensibleElement, gen_dbl_LoopStatement_Statement, gen_dbl_SimpleStatement_Statement, gen_dbl_Class_NamedElement, gen_dbl_Class_Type, gen_dbl_Class_ConstructiveExtensionAtContentExtensionPoint, gen_dbl_Class_LanguageConceptClassifier, gen_dbl_Class_Construct, gen_dbl_Terminate_SimpleStatement, gen_dbl_Yield_SimpleStatement, gen_dbl_Wait_SimpleStatement, gen_dbl_Reactivate_SimpleStatement, gen_dbl_ActivateObject_SimpleStatement, gen_dbl_Advance_SimpleStatement, gen_dbl_Print_SimpleStatement, gen_dbl_IfStatement_Statement, gen_dbl_Assignment_SimpleStatement, gen_dbl_FunctionCall_SimpleStatement, gen_dbl_Return_SimpleStatement, gen_dbl_WaitUntil_SimpleStatement, gen_dbl_SwitchStatement_SimpleStatement, gen_dbl_LocalScopeStatement_SimpleStatement, gen_dbl_LocalScopeStatement_LocalScope, gen_dbl_ForStatement_LoopStatement, gen_dbl_ForStatement_LocalScope, gen_dbl_WhileStatement_LoopStatement, gen_dbl_L1Expr_Expression, gen_dbl_L2Expr_Expression, gen_dbl_L3Expr_Expression, gen_dbl_L4Expr_Expression, gen_dbl_L5Expr_Expression, gen_dbl_L6Expr_Expression, gen_dbl_L7Expr_Expression, gen_dbl_L8Expr_Expression, gen_dbl_L9Expr_Expression, gen_dbl_BinaryOperator_Expression, gen_dbl_BreakStatement_SimpleStatement, gen_dbl_ContinueStatement_SimpleStatement, gen_dbl_Expression_TypedElement, gen_dbl_Expression_ExtensibleElement, gen_dbl_Or_BinaryOperator, gen_dbl_Or_L8Expr, gen_dbl_And_BinaryOperator, gen_dbl_And_L7Expr, gen_dbl_NotEqual_BinaryOperator, gen_dbl_NotEqual_L6Expr, gen_dbl_Equal_BinaryOperator, gen_dbl_Equal_L6Expr, gen_dbl_Greater_BinaryOperator, gen_dbl_Greater_L5Expr, gen_dbl_GreaterEqual_BinaryOperator, gen_dbl_GreaterEqual_L5Expr, gen_dbl_Less_BinaryOperator, gen_dbl_Less_L5Expr, gen_dbl_LessEqual_BinaryOperator, gen_dbl_LessEqual_L5Expr, gen_dbl_InstanceOf_BinaryOperator, gen_dbl_InstanceOf_L5Expr, gen_dbl_Plus_BinaryOperator, gen_dbl_Plus_L4Expr, gen_dbl_Minus_BinaryOperator, gen_dbl_Minus_L4Expr, gen_dbl_Mul_BinaryOperator, gen_dbl_Mul_L3Expr, gen_dbl_Mod_BinaryOperator, gen_dbl_Mod_L3Expr, gen_dbl_UnaryOperator_Expression, gen_dbl_UniqueIdExpr_Expression, gen_dbl_ExpandExpr_Expression, gen_dbl_ParseExpr_Expression, gen_dbl_MeLiteral_PredefinedId, gen_dbl_SuperLiteral_PredefinedId, gen_dbl_MetaLiteral_PredefinedId, gen_dbl_TypeLiteral_PredefinedId, gen_dbl_SizeOfArray_PredefinedId, gen_dbl_IdExpr_L1Expr, gen_dbl_ElementAccess_Expression, gen_dbl_Div_BinaryOperator, gen_dbl_Div_L3Expr, gen_dbl_Neg_UnaryOperator, gen_dbl_Neg_L2Expr, gen_dbl_Not_UnaryOperator, gen_dbl_Not_L2Expr, gen_dbl_Cast_UnaryOperator, gen_dbl_Cast_TypedElement, gen_dbl_Cast_L2Expr, gen_dbl_CreateObject_L1Expr, gen_dbl_CreateObject_TypedElement, gen_dbl_NullLiteral_L1Expr, gen_dbl_TimeLiteral_L1Expr, gen_dbl_ActiveLiteral_L1Expr, gen_dbl_StringLiteral_L1Expr, gen_dbl_IntLiteral_L1Expr, gen_dbl_TrueLiteral_L1Expr, gen_dbl_FalseLiteral_L1Expr, gen_dbl_DoubleLiteral_L1Expr, gen_dbl_ExtensionSemanticsDefinition_ExtensibleElement, gen_dbl_ExtensionSemanticsDefinition_LocalScope, gen_dbl_TextualSyntaxDef_ExtensibleElement, gen_dbl_LanguageConstructClassifier_NamedElement, gen_dbl_LanguageConstructClassifier_ExtensibleElement, gen_dbl_LanguageConceptClassifier_LanguageConstructClassifier, gen_dbl_TsRule_NamedElement, gen_dbl_TsRule_LanguageConstructClassifier, gen_dbl_L3RhsExpr_RhsExpression, gen_dbl_L2RhsExpr_RhsExpression, gen_dbl_SequenceExpr_L2RhsExpr, gen_dbl_L1RhsExpr_RhsExpression, gen_dbl_TerminalExpr_L1RhsExpr, gen_dbl_VariableAccess_ElementAccess, gen_dbl_MetaAccess_VariableAccess, gen_dbl_TypeAccess_ElementAccess, gen_dbl_ExtensionDefinition_LanguageConceptClassifier, gen_dbl_ExtensionDefinition_ExtensibleElement, gen_dbl_IdPropertyType_PropertyType, gen_dbl_IntPropertyType_PropertyType, gen_dbl_StringPropertyType_PropertyType, gen_dbl_BooleanPropertyType_PropertyType, gen_dbl_StructuredPropertyType_PropertyType, gen_dbl_CompositePropertyType_StructuredPropertyType, gen_dbl_ReferencePropertyType_StructuredPropertyType, gen_dbl_MetaExpr_Expression, gen_dbl_PropertyBindingExpr_NamedElement, gen_dbl_PropertyBindingExpr_L1RhsExpr, gen_dbl_RhsClassifierExpr_L1RhsExpr, gen_dbl_ExpandVariablePart_ExpansionPart, gen_dbl_SetExpansionContextStatement_SimpleStatement, gen_dbl_SaveGenStatement_SimpleStatement, gen_dbl_ResumeGenStatement_SimpleStatement, gen_dbl_ExpandExpression_Expression, gen_dbl_ExpandStatement_Statement, gen_dbl_TargetStatement_Statement, gen_dbl_ExpansionStatement_Statement, gen_dbl_ExpandTextPart_ExpansionPart, gen_dbl_Pattern_NamedElement, gen_dbl_TestStatement_Statement, gen_dbl_CodeQuoteExpression_Expression, gen_dbl_QuotedExpression_QuotedCode, gen_dbl_QuotedStatements_QuotedCode, gen_dbl_QuotedClassContent_QuotedCode, gen_dbl_QuotedClassContent_Class, gen_dbl_QuotedModuleContent_QuotedCode, gen_dbl_QuotedModuleContent_Module},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)