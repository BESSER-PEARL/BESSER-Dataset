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
dbl_AnnotateableElement = Class(name="dbl_AnnotateableElement")
dbl_ConstructiveExtension = Class(name="dbl_ConstructiveExtension")
ExtensibleElement = Class(name="ExtensibleElement")
dbl_ConstructiveExtensionAtContentExtensionPoint = Class(name="dbl_ConstructiveExtensionAtContentExtensionPoint", is_abstract=True)
dbl_Construct = Class(name="dbl_Construct")
dbl_ExpandExpr = Class(name="dbl_ExpandExpr")
dbl_ExtensibleElement = Class(name="dbl_ExtensibleElement")
NamedElement = Class(name="NamedElement")
Construct = Class(name="Construct")
dbl_Model = Class(name="dbl_Model")
dbl_Import = Class(name="dbl_Import")
dbl_Module = Class(name="dbl_Module")
ConstructiveExtensionAtContentExtensionPoint = Class(name="ConstructiveExtensionAtContentExtensionPoint")
dbl_Class = Class(name="dbl_Class")
dbl_Extension = Class(name="dbl_Extension")
dbl_ExtensionSemantics = Class(name="dbl_ExtensionSemantics")
dbl_Function = Class(name="dbl_Function")
dbl_Variable = Class(name="dbl_Variable")
dbl_Annotation = Class(name="dbl_Annotation")
dbl_AnnotationItem = Class(name="dbl_AnnotationItem")
dbl_SuperClassSpecification = Class(name="dbl_SuperClassSpecification")
Concept = Class(name="Concept")
dbl_ModuleContentExtension = Class(name="dbl_ModuleContentExtension")
ConstructiveExtension = Class(name="ConstructiveExtension")
dbl_ClassContentExtension = Class(name="dbl_ClassContentExtension")
dbl_Type = Class(name="dbl_Type", is_abstract=True)
dbl_ArrayDimension = Class(name="dbl_ArrayDimension")
dbl_TypedElement = Class(name="dbl_TypedElement", is_abstract=True)
dbl_PrimitiveType = Class(name="dbl_PrimitiveType", is_abstract=True)
dbl_IdExpr = Class(name="dbl_IdExpr")
dbl_Expression = Class(name="dbl_Expression")
Type = Class(name="Type")
dbl_VoidType = Class(name="dbl_VoidType")
PrimitiveType = Class(name="PrimitiveType")
dbl_IntType = Class(name="dbl_IntType")
dbl_BoolType = Class(name="dbl_BoolType")
dbl_DoubleType = Class(name="dbl_DoubleType")
dbl_StringType = Class(name="dbl_StringType")
TypedElement = Class(name="TypedElement")
LocalScope = Class(name="LocalScope")
dbl_Parameter = Class(name="dbl_Parameter")
dbl_NativeBinding = Class(name="dbl_NativeBinding")
dbl_NamedElement = Class(name="dbl_NamedElement")
dbl_Statement = Class(name="dbl_Statement")
dbl_LoopStatement = Class(name="dbl_LoopStatement")
Statement = Class(name="Statement")
dbl_SimpleStatement = Class(name="dbl_SimpleStatement")
dbl_Assignment = Class(name="dbl_Assignment")
AnnotateableElement = Class(name="AnnotateableElement")
dbl_Constructor = Class(name="dbl_Constructor")
dbl_LocalScope = Class(name="dbl_LocalScope")
dbl_AbstractVariable = Class(name="dbl_AbstractVariable", is_abstract=True)
AbstractVariable = Class(name="AbstractVariable")
SimpleStatement = Class(name="SimpleStatement")
dbl_VariableAccess = Class(name="dbl_VariableAccess")
dbl_FunctionCall = Class(name="dbl_FunctionCall")
dbl_Return = Class(name="dbl_Return")
dbl_WaitUntil = Class(name="dbl_WaitUntil")
dbl_Terminate = Class(name="dbl_Terminate")
dbl_Yield = Class(name="dbl_Yield")
dbl_Wait = Class(name="dbl_Wait")
dbl_Reactivate = Class(name="dbl_Reactivate")
dbl_ActivateObject = Class(name="dbl_ActivateObject")
dbl_Advance = Class(name="dbl_Advance")
dbl_Print = Class(name="dbl_Print")
dbl_IfStatement = Class(name="dbl_IfStatement")
dbl_L7Expr = Class(name="dbl_L7Expr")
dbl_L8Expr = Class(name="dbl_L8Expr")
dbl_L9Expr = Class(name="dbl_L9Expr")
dbl_BinaryOperator = Class(name="dbl_BinaryOperator", is_abstract=True)
dbl_LocalScopeStatement = Class(name="dbl_LocalScopeStatement")
dbl_ForStatement = Class(name="dbl_ForStatement")
LoopStatement = Class(name="LoopStatement")
dbl_WhileStatement = Class(name="dbl_WhileStatement")
dbl_SwitchStatement = Class(name="dbl_SwitchStatement")
dbl_SwitchCase = Class(name="dbl_SwitchCase")
dbl_BreakStatement = Class(name="dbl_BreakStatement")
dbl_ContinueStatement = Class(name="dbl_ContinueStatement")
dbl_L1Expr = Class(name="dbl_L1Expr")
Expression = Class(name="Expression")
dbl_L2Expr = Class(name="dbl_L2Expr")
dbl_L3Expr = Class(name="dbl_L3Expr")
dbl_L4Expr = Class(name="dbl_L4Expr")
dbl_L5Expr = Class(name="dbl_L5Expr")
dbl_L6Expr = Class(name="dbl_L6Expr")
dbl_StringLiteral = Class(name="dbl_StringLiteral")
dbl_IntLiteral = Class(name="dbl_IntLiteral")
dbl_TrueLiteral = Class(name="dbl_TrueLiteral")
dbl_FalseLiteral = Class(name="dbl_FalseLiteral")
dbl_DoubleLiteral = Class(name="dbl_DoubleLiteral")
dbl_UnaryOperator = Class(name="dbl_UnaryOperator", is_abstract=True)
dbl_Or = Class(name="dbl_Or")
BinaryOperator = Class(name="BinaryOperator")
L8Expr = Class(name="L8Expr")
dbl_And = Class(name="dbl_And")
L7Expr = Class(name="L7Expr")
dbl_NotEqual = Class(name="dbl_NotEqual")
L6Expr = Class(name="L6Expr")
dbl_Equal = Class(name="dbl_Equal")
dbl_Greater = Class(name="dbl_Greater")
L5Expr = Class(name="L5Expr")
dbl_GreaterEqual = Class(name="dbl_GreaterEqual")
dbl_Less = Class(name="dbl_Less")
dbl_LessEqual = Class(name="dbl_LessEqual")
dbl_InstanceOf = Class(name="dbl_InstanceOf")
dbl_Plus = Class(name="dbl_Plus")
L4Expr = Class(name="L4Expr")
dbl_Minus = Class(name="dbl_Minus")
dbl_Mul = Class(name="dbl_Mul")
L3Expr = Class(name="L3Expr")
dbl_Mod = Class(name="dbl_Mod")
dbl_Div = Class(name="dbl_Div")
dbl_Neg = Class(name="dbl_Neg")
UnaryOperator = Class(name="UnaryOperator")
L2Expr = Class(name="L2Expr")
dbl_Not = Class(name="dbl_Not")
dbl_Cast = Class(name="dbl_Cast")
dbl_CreateObject = Class(name="dbl_CreateObject")
L1Expr = Class(name="L1Expr")
dbl_NullLiteral = Class(name="dbl_NullLiteral")
dbl_TimeLiteral = Class(name="dbl_TimeLiteral")
dbl_ActiveLiteral = Class(name="dbl_ActiveLiteral")
ElementAccess = Class(name="ElementAccess")
dbl_MetaAccess = Class(name="dbl_MetaAccess")
VariableAccess = Class(name="VariableAccess")
dbl_TypeAccess = Class(name="dbl_TypeAccess")
dbl_Concept = Class(name="dbl_Concept")
dbl_ParseExpr = Class(name="dbl_ParseExpr")
dbl_PredefinedId = Class(name="dbl_PredefinedId")
dbl_MeLiteral = Class(name="dbl_MeLiteral")
PredefinedId = Class(name="PredefinedId")
dbl_SuperLiteral = Class(name="dbl_SuperLiteral")
dbl_MetaLiteral = Class(name="dbl_MetaLiteral")
dbl_TypeLiteral = Class(name="dbl_TypeLiteral")
dbl_SizeOfArray = Class(name="dbl_SizeOfArray")
dbl_AnnotationLiteral = Class(name="dbl_AnnotationLiteral")
Annotation = Class(name="Annotation")
dbl_CallPart = Class(name="dbl_CallPart")
dbl_ElementAccess = Class(name="dbl_ElementAccess", is_abstract=True)
dbl_PlainSymbolReference = Class(name="dbl_PlainSymbolReference")
L1SyntaxExpression = Class(name="L1SyntaxExpression")
dbl_SyntaxDefinition = Class(name="dbl_SyntaxDefinition")
dbl_MetaSymbol = Class(name="dbl_MetaSymbol")
dbl_SyntaxSymbolClassifier = Class(name="dbl_SyntaxSymbolClassifier")
dbl_ComplexSymbol = Class(name="dbl_ComplexSymbol")
SyntaxSymbolClassifier = Class(name="SyntaxSymbolClassifier")
ComplexSymbol = Class(name="ComplexSymbol")
dbl_SyntaxExpression = Class(name="dbl_SyntaxExpression")
dbl_L3SyntaxExpression = Class(name="dbl_L3SyntaxExpression")
SyntaxExpression = Class(name="SyntaxExpression")
dbl_L2SyntaxExpression = Class(name="dbl_L2SyntaxExpression")
dbl_SymbolSequence = Class(name="dbl_SymbolSequence")
L2SyntaxExpression = Class(name="L2SyntaxExpression")
dbl_L1SyntaxExpression = Class(name="dbl_L1SyntaxExpression")
dbl_StructuralSymbolReference = Class(name="dbl_StructuralSymbolReference")
PlainSymbolReference = Class(name="PlainSymbolReference")
dbl_ExpandExpression = Class(name="dbl_ExpandExpression")
dbl_ExpandStatement = Class(name="dbl_ExpandStatement")
dbl_ElementarySymbol = Class(name="dbl_ElementarySymbol", is_abstract=True)
dbl_IdSymbol = Class(name="dbl_IdSymbol")
ElementarySymbol = Class(name="ElementarySymbol")
dbl_IntSymbol = Class(name="dbl_IntSymbol")
dbl_StringSymbol = Class(name="dbl_StringSymbol")
dbl_Keyword = Class(name="dbl_Keyword")
dbl_MetaExpr = Class(name="dbl_MetaExpr")
dbl_TargetStatement = Class(name="dbl_TargetStatement")
dbl_CreateIdStatement = Class(name="dbl_CreateIdStatement")
Variable = Class(name="Variable")
dbl_ExpansionStatement = Class(name="dbl_ExpansionStatement")
dbl_ExpansionPart = Class(name="dbl_ExpansionPart", is_abstract=True)
dbl_ExpandTextPart = Class(name="dbl_ExpandTextPart")
ExpansionPart = Class(name="ExpansionPart")
dbl_ExpandVariablePart = Class(name="dbl_ExpandVariablePart")
dbl_CodeQuoteExpression = Class(name="dbl_CodeQuoteExpression")
dbl_QuotedCode = Class(name="dbl_QuotedCode")
dbl_QuotedExpression = Class(name="dbl_QuotedExpression")
QuotedCode = Class(name="QuotedCode")
dbl_QuotedStatements = Class(name="dbl_QuotedStatements")
dbl_QuotedClassContent = Class(name="dbl_QuotedClassContent")
Class_ = Class(name="Class")
dbl_QuotedModuleContent = Class(name="dbl_QuotedModuleContent")
Module = Class(name="Module")
dbl_Pattern = Class(name="dbl_Pattern")
dbl_TestStatement = Class(name="dbl_TestStatement")

# dbl_AnnotateableElement class attributes and methods

# dbl_ConstructiveExtension class attributes and methods

# ExtensibleElement class attributes and methods

# dbl_ConstructiveExtensionAtContentExtensionPoint class attributes and methods

# dbl_Construct class attributes and methods

# dbl_ExpandExpr class attributes and methods

# dbl_ExtensibleElement class attributes and methods
dbl_ExtensibleElement_concreteSyntax: Property = Property(name="concreteSyntax", type=StringType)
dbl_ExtensibleElement_instanceOfExtensionDefinition: Property = Property(name="instanceOfExtensionDefinition", type=BooleanType)
dbl_ExtensibleElement.attributes={dbl_ExtensibleElement_concreteSyntax, dbl_ExtensibleElement_instanceOfExtensionDefinition}

# NamedElement class attributes and methods

# Construct class attributes and methods

# dbl_Model class attributes and methods

# dbl_Import class attributes and methods
dbl_Import_file: Property = Property(name="file", type=StringType)
dbl_Import.attributes={dbl_Import_file}

# dbl_Module class attributes and methods

# ConstructiveExtensionAtContentExtensionPoint class attributes and methods

# dbl_Class class attributes and methods
dbl_Class_active: Property = Property(name="active", type=BooleanType)
dbl_Class.attributes={dbl_Class_active}

# dbl_Extension class attributes and methods

# dbl_ExtensionSemantics class attributes and methods

# dbl_Function class attributes and methods
dbl_Function_class_: Property = Property(name="class_", type=BooleanType)
dbl_Function_abstract: Property = Property(name="abstract", type=BooleanType)
dbl_Function.attributes={dbl_Function_abstract, dbl_Function_class_}

# dbl_Variable class attributes and methods
dbl_Variable_control: Property = Property(name="control", type=BooleanType)
dbl_Variable_class_: Property = Property(name="class_", type=BooleanType)
dbl_Variable.attributes={dbl_Variable_class_, dbl_Variable_control}

# dbl_Annotation class attributes and methods

# dbl_AnnotationItem class attributes and methods
dbl_AnnotationItem_key: Property = Property(name="key", type=StringType)
dbl_AnnotationItem_value: Property = Property(name="value", type=StringType)
dbl_AnnotationItem.attributes={dbl_AnnotationItem_key, dbl_AnnotationItem_value}

# dbl_SuperClassSpecification class attributes and methods

# Concept class attributes and methods

# dbl_ModuleContentExtension class attributes and methods

# ConstructiveExtension class attributes and methods

# dbl_ClassContentExtension class attributes and methods

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

# dbl_BoolType class attributes and methods

# dbl_DoubleType class attributes and methods

# dbl_StringType class attributes and methods

# TypedElement class attributes and methods

# LocalScope class attributes and methods

# dbl_Parameter class attributes and methods

# dbl_NativeBinding class attributes and methods
dbl_NativeBinding_targetType: Property = Property(name="targetType", type=StringType)
dbl_NativeBinding_targetLanguage: Property = Property(name="targetLanguage", type=StringType)
dbl_NativeBinding.attributes={dbl_NativeBinding_targetType, dbl_NativeBinding_targetLanguage}

# dbl_NamedElement class attributes and methods
dbl_NamedElement_name: Property = Property(name="name", type=StringType)
dbl_NamedElement.attributes={dbl_NamedElement_name}

# dbl_Statement class attributes and methods

# dbl_LoopStatement class attributes and methods

# Statement class attributes and methods

# dbl_SimpleStatement class attributes and methods

# dbl_Assignment class attributes and methods

# AnnotateableElement class attributes and methods

# dbl_Constructor class attributes and methods

# dbl_LocalScope class attributes and methods

# dbl_AbstractVariable class attributes and methods

# AbstractVariable class attributes and methods

# SimpleStatement class attributes and methods

# dbl_VariableAccess class attributes and methods

# dbl_FunctionCall class attributes and methods

# dbl_Return class attributes and methods

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

# dbl_IfStatement class attributes and methods

# dbl_L7Expr class attributes and methods

# dbl_L8Expr class attributes and methods

# dbl_L9Expr class attributes and methods

# dbl_BinaryOperator class attributes and methods

# dbl_LocalScopeStatement class attributes and methods

# dbl_ForStatement class attributes and methods

# LoopStatement class attributes and methods

# dbl_WhileStatement class attributes and methods

# dbl_SwitchStatement class attributes and methods

# dbl_SwitchCase class attributes and methods

# dbl_BreakStatement class attributes and methods

# dbl_ContinueStatement class attributes and methods

# dbl_L1Expr class attributes and methods

# Expression class attributes and methods

# dbl_L2Expr class attributes and methods

# dbl_L3Expr class attributes and methods

# dbl_L4Expr class attributes and methods

# dbl_L5Expr class attributes and methods

# dbl_L6Expr class attributes and methods

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

# dbl_UnaryOperator class attributes and methods

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

# ElementAccess class attributes and methods

# dbl_MetaAccess class attributes and methods

# VariableAccess class attributes and methods

# dbl_TypeAccess class attributes and methods

# dbl_Concept class attributes and methods

# dbl_ParseExpr class attributes and methods

# dbl_PredefinedId class attributes and methods

# dbl_MeLiteral class attributes and methods

# PredefinedId class attributes and methods

# dbl_SuperLiteral class attributes and methods

# dbl_MetaLiteral class attributes and methods

# dbl_TypeLiteral class attributes and methods

# dbl_SizeOfArray class attributes and methods

# dbl_AnnotationLiteral class attributes and methods

# Annotation class attributes and methods

# dbl_CallPart class attributes and methods

# dbl_ElementAccess class attributes and methods

# dbl_PlainSymbolReference class attributes and methods

# L1SyntaxExpression class attributes and methods

# dbl_SyntaxDefinition class attributes and methods

# dbl_MetaSymbol class attributes and methods

# dbl_SyntaxSymbolClassifier class attributes and methods

# dbl_ComplexSymbol class attributes and methods

# SyntaxSymbolClassifier class attributes and methods

# ComplexSymbol class attributes and methods

# dbl_SyntaxExpression class attributes and methods

# dbl_L3SyntaxExpression class attributes and methods

# SyntaxExpression class attributes and methods

# dbl_L2SyntaxExpression class attributes and methods

# dbl_SymbolSequence class attributes and methods

# L2SyntaxExpression class attributes and methods

# dbl_L1SyntaxExpression class attributes and methods

# dbl_StructuralSymbolReference class attributes and methods
dbl_StructuralSymbolReference_localScopedReference: Property = Property(name="localScopedReference", type=BooleanType)
dbl_StructuralSymbolReference_globalScopedReference: Property = Property(name="globalScopedReference", type=BooleanType)
dbl_StructuralSymbolReference_list: Property = Property(name="list", type=BooleanType)
dbl_StructuralSymbolReference_composite: Property = Property(name="composite", type=BooleanType)
dbl_StructuralSymbolReference.attributes={dbl_StructuralSymbolReference_list, dbl_StructuralSymbolReference_localScopedReference, dbl_StructuralSymbolReference_composite, dbl_StructuralSymbolReference_globalScopedReference}

# PlainSymbolReference class attributes and methods

# dbl_ExpandExpression class attributes and methods

# dbl_ExpandStatement class attributes and methods

# dbl_ElementarySymbol class attributes and methods

# dbl_IdSymbol class attributes and methods

# ElementarySymbol class attributes and methods

# dbl_IntSymbol class attributes and methods

# dbl_StringSymbol class attributes and methods

# dbl_Keyword class attributes and methods
dbl_Keyword_keyword: Property = Property(name="keyword", type=StringType)
dbl_Keyword.attributes={dbl_Keyword_keyword}

# dbl_MetaExpr class attributes and methods

# dbl_TargetStatement class attributes and methods

# dbl_CreateIdStatement class attributes and methods

# Variable class attributes and methods

# dbl_ExpansionStatement class attributes and methods
dbl_ExpansionStatement_classContext: Property = Property(name="classContext", type=BooleanType)
dbl_ExpansionStatement_functionContext: Property = Property(name="functionContext", type=BooleanType)
dbl_ExpansionStatement_variableContext: Property = Property(name="variableContext", type=BooleanType)
dbl_ExpansionStatement.attributes={dbl_ExpansionStatement_variableContext, dbl_ExpansionStatement_classContext, dbl_ExpansionStatement_functionContext}

# dbl_ExpansionPart class attributes and methods

# dbl_ExpandTextPart class attributes and methods
dbl_ExpandTextPart_text: Property = Property(name="text", type=StringType)
dbl_ExpandTextPart.attributes={dbl_ExpandTextPart_text}

# ExpansionPart class attributes and methods

# dbl_ExpandVariablePart class attributes and methods

# dbl_CodeQuoteExpression class attributes and methods

# dbl_QuotedCode class attributes and methods

# dbl_QuotedExpression class attributes and methods

# QuotedCode class attributes and methods

# dbl_QuotedStatements class attributes and methods

# dbl_QuotedClassContent class attributes and methods

# Class class attributes and methods

# dbl_QuotedModuleContent class attributes and methods

# Module class attributes and methods

# dbl_Pattern class attributes and methods
dbl_Pattern_top: Property = Property(name="top", type=BooleanType)
dbl_Pattern.attributes={dbl_Pattern_top}

# dbl_TestStatement class attributes and methods
dbl_TestStatement_value: Property = Property(name="value", type=IntegerType)
dbl_TestStatement.attributes={dbl_TestStatement_value}

# Relationships
items17: BinaryAssociation = BinaryAssociation(
    name="items17",
    ends={
        Property(name="dbl_AnnotationItem", type=dbl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Annotation", type=dbl_AnnotationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations18: BinaryAssociation = BinaryAssociation(
    name="annotations18",
    ends={
        Property(name="dbl_Annotation19", type=dbl_AnnotateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_AnnotateableElement", type=dbl_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expandExpr0: BinaryAssociation = BinaryAssociation(
    name="expandExpr0",
    ends={
        Property(name="dbl_ExpandExpr", type=dbl_Construct, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Construct", type=dbl_ExpandExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
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
classes7: BinaryAssociation = BinaryAssociation(
    name="classes7",
    ends={
        Property(name="dbl_Class", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module8", type=dbl_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions9: BinaryAssociation = BinaryAssociation(
    name="extensions9",
    ends={
        Property(name="dbl_Extension", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module10", type=dbl_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensionSemantics11: BinaryAssociation = BinaryAssociation(
    name="extensionSemantics11",
    ends={
        Property(name="dbl_ExtensionSemantics", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module12", type=dbl_ExtensionSemantics, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions13: BinaryAssociation = BinaryAssociation(
    name="functions13",
    ends={
        Property(name="dbl_Function", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module14", type=dbl_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables15: BinaryAssociation = BinaryAssociation(
    name="variables15",
    ends={
        Property(name="dbl_Variable", type=dbl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Module16", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_32: BinaryAssociation = BinaryAssociation(
    name="class_32",
    ends={
        Property(name="dbl_Class33", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SuperClassSpecification", type=dbl_Class, multiplicity=Multiplicity(1, 1))
    }
)
constructorArguments34: BinaryAssociation = BinaryAssociation(
    name="constructorArguments34",
    ends={
        Property(name="dbl_Expression36", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SuperClassSpecification35", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contentExtensions20: BinaryAssociation = BinaryAssociation(
    name="contentExtensions20",
    ends={
        Property(name="dbl_ConstructiveExtension", type=dbl_ConstructiveExtensionAtContentExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ConstructiveExtensionAtContentExtensionPoint", type=dbl_ConstructiveExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayDimensions21: BinaryAssociation = BinaryAssociation(
    name="arrayDimensions21",
    ends={
        Property(name="dbl_ArrayDimension", type=dbl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Type", type=dbl_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveType22: BinaryAssociation = BinaryAssociation(
    name="primitiveType22",
    ends={
        Property(name="dbl_PrimitiveType", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement", type=dbl_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArrayDimensions23: BinaryAssociation = BinaryAssociation(
    name="typeArrayDimensions23",
    ends={
        Property(name="dbl_ArrayDimension25", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement24", type=dbl_ArrayDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierType26: BinaryAssociation = BinaryAssociation(
    name="classifierType26",
    ends={
        Property(name="dbl_IdExpr", type=dbl_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TypedElement27", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size28: BinaryAssociation = BinaryAssociation(
    name="size28",
    ends={
        Property(name="dbl_Expression", type=dbl_ArrayDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ArrayDimension29", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="dbl_Parameter", type=dbl_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Function31", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings37: BinaryAssociation = BinaryAssociation(
    name="bindings37",
    ends={
        Property(name="dbl_NativeBinding", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class38", type=dbl_NativeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClasses39: BinaryAssociation = BinaryAssociation(
    name="superClasses39",
    ends={
        Property(name="dbl_SuperClassSpecification41", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class40", type=dbl_SuperClassSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructors42: BinaryAssociation = BinaryAssociation(
    name="constructors42",
    ends={
        Property(name="Constructor", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClass", type=dbl_Constructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes43: BinaryAssociation = BinaryAssociation(
    name="attributes43",
    ends={
        Property(name="dbl_Variable45", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class44", type=dbl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods46: BinaryAssociation = BinaryAssociation(
    name="methods46",
    ends={
        Property(name="dbl_Function48", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class47", type=dbl_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsBlock49: BinaryAssociation = BinaryAssociation(
    name="actionsBlock49",
    ends={
        Property(name="dbl_LocalScope", type=dbl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Class50", type=dbl_LocalScope, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters51: BinaryAssociation = BinaryAssociation(
    name="parameters51",
    ends={
        Property(name="dbl_Parameter52", type=dbl_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Constructor", type=dbl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningClass53: BinaryAssociation = BinaryAssociation(
    name="owningClass53",
    ends={
        Property(name="Class", type=dbl_Constructor, multiplicity=Multiplicity(1, 1)),
        Property(name="constructors", type=dbl_Class, multiplicity=Multiplicity(1, 1))
    }
)
initialValue54: BinaryAssociation = BinaryAssociation(
    name="initialValue54",
    ends={
        Property(name="dbl_Expression56", type=dbl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Variable55", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition75: BinaryAssociation = BinaryAssociation(
    name="condition75",
    ends={
        Property(name="dbl_Expression76", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trueCase77: BinaryAssociation = BinaryAssociation(
    name="trueCase77",
    ends={
        Property(name="dbl_Statement", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement78", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
falseCase79: BinaryAssociation = BinaryAssociation(
    name="falseCase79",
    ends={
        Property(name="dbl_Statement81", type=dbl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IfStatement80", type=dbl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements82: BinaryAssociation = BinaryAssociation(
    name="statements82",
    ends={
        Property(name="dbl_Statement84", type=dbl_LocalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_LocalScope83", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable57: BinaryAssociation = BinaryAssociation(
    name="variable57",
    ends={
        Property(name="dbl_VariableAccess", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="dbl_Expression60", type=dbl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Assignment59", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callIdExpr61: BinaryAssociation = BinaryAssociation(
    name="callIdExpr61",
    ends={
        Property(name="dbl_IdExpr62", type=dbl_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_FunctionCall", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value63: BinaryAssociation = BinaryAssociation(
    name="value63",
    ends={
        Property(name="dbl_Expression64", type=dbl_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Return", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition65: BinaryAssociation = BinaryAssociation(
    name="condition65",
    ends={
        Property(name="dbl_Expression66", type=dbl_WaitUntil, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WaitUntil", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess67: BinaryAssociation = BinaryAssociation(
    name="objectAccess67",
    ends={
        Property(name="dbl_Expression68", type=dbl_Reactivate, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Reactivate", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objectAccess69: BinaryAssociation = BinaryAssociation(
    name="objectAccess69",
    ends={
        Property(name="dbl_Expression70", type=dbl_ActivateObject, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ActivateObject", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
time71: BinaryAssociation = BinaryAssociation(
    name="time71",
    ends={
        Property(name="dbl_Expression72", type=dbl_Advance, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Advance", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outputs73: BinaryAssociation = BinaryAssociation(
    name="outputs73",
    ends={
        Property(name="dbl_Expression74", type=dbl_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Print", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op1111: BinaryAssociation = BinaryAssociation(
    name="op1111",
    ends={
        Property(name="dbl_Expression112", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op2113: BinaryAssociation = BinaryAssociation(
    name="op2113",
    ends={
        Property(name="dbl_Expression115", type=dbl_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_BinaryOperator114", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
termination85: BinaryAssociation = BinaryAssociation(
    name="termination85",
    ends={
        Property(name="dbl_Expression86", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
increment87: BinaryAssociation = BinaryAssociation(
    name="increment87",
    ends={
        Property(name="dbl_Assignment89", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement88", type=dbl_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body90: BinaryAssociation = BinaryAssociation(
    name="body90",
    ends={
        Property(name="dbl_Statement92", type=dbl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ForStatement91", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition93: BinaryAssociation = BinaryAssociation(
    name="condition93",
    ends={
        Property(name="dbl_Expression94", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body95: BinaryAssociation = BinaryAssociation(
    name="body95",
    ends={
        Property(name="dbl_Statement97", type=dbl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_WhileStatement96", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable98: BinaryAssociation = BinaryAssociation(
    name="variable98",
    ends={
        Property(name="dbl_VariableAccess99", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement", type=dbl_VariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases100: BinaryAssociation = BinaryAssociation(
    name="cases100",
    ends={
        Property(name="dbl_SwitchCase", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement101", type=dbl_SwitchCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultCase102: BinaryAssociation = BinaryAssociation(
    name="defaultCase102",
    ends={
        Property(name="dbl_SwitchCase104", type=dbl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchStatement103", type=dbl_SwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value105: BinaryAssociation = BinaryAssociation(
    name="value105",
    ends={
        Property(name="dbl_Expression107", type=dbl_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchCase106", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body108: BinaryAssociation = BinaryAssociation(
    name="body108",
    ends={
        Property(name="dbl_Statement110", type=dbl_SwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SwitchCase109", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op116: BinaryAssociation = BinaryAssociation(
    name="op116",
    ends={
        Property(name="dbl_Expression117", type=dbl_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_UnaryOperator", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
idExpr138: BinaryAssociation = BinaryAssociation(
    name="idExpr138",
    ends={
        Property(name="dbl_IdExpr139", type=dbl_ElementAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ElementAccess", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extensionPoint140: BinaryAssociation = BinaryAssociation(
    name="extensionPoint140",
    ends={
        Property(name="dbl_Concept", type=dbl_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Extension141", type=dbl_Concept, multiplicity=Multiplicity(1, 1))
    }
)
expr118: BinaryAssociation = BinaryAssociation(
    name="expr118",
    ends={
        Property(name="dbl_Expression120", type=dbl_ExpandExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandExpr119", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
astPart121: BinaryAssociation = BinaryAssociation(
    name="astPart121",
    ends={
        Property(name="dbl_Construct122", type=dbl_ParseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ParseExpr", type=dbl_Construct, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentIdExpr124: BinaryAssociation = BinaryAssociation(
    name="parentIdExpr124",
    ends={
        Property(name="dbl_IdExpr125", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr123", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedElement126: BinaryAssociation = BinaryAssociation(
    name="referencedElement126",
    ends={
        Property(name="dbl_NamedElement", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr127", type=dbl_NamedElement, multiplicity=Multiplicity(0, 1))
    }
)
predefinedId128: BinaryAssociation = BinaryAssociation(
    name="predefinedId128",
    ends={
        Property(name="dbl_PredefinedId", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr129", type=dbl_PredefinedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayIndex130: BinaryAssociation = BinaryAssociation(
    name="arrayIndex130",
    ends={
        Property(name="dbl_Expression132", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr131", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callPart133: BinaryAssociation = BinaryAssociation(
    name="callPart133",
    ends={
        Property(name="dbl_CallPart", type=dbl_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_IdExpr134", type=dbl_CallPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
callArguments135: BinaryAssociation = BinaryAssociation(
    name="callArguments135",
    ends={
        Property(name="dbl_Expression137", type=dbl_CallPart, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CallPart136", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier156: BinaryAssociation = BinaryAssociation(
    name="classifier156",
    ends={
        Property(name="dbl_SyntaxSymbolClassifier", type=dbl_PlainSymbolReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_PlainSymbolReference", type=dbl_SyntaxSymbolClassifier, multiplicity=Multiplicity(1, 1))
    }
)
syntaxDefinition142: BinaryAssociation = BinaryAssociation(
    name="syntaxDefinition142",
    ends={
        Property(name="dbl_SyntaxDefinition", type=dbl_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Extension143", type=dbl_SyntaxDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
syntaxDefinition144: BinaryAssociation = BinaryAssociation(
    name="syntaxDefinition144",
    ends={
        Property(name="dbl_Extension146", type=dbl_ExtensionSemantics, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExtensionSemantics145", type=dbl_Extension, multiplicity=Multiplicity(1, 1))
    }
)
startSymbol147: BinaryAssociation = BinaryAssociation(
    name="startSymbol147",
    ends={
        Property(name="dbl_MetaSymbol", type=dbl_SyntaxDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SyntaxDefinition148", type=dbl_MetaSymbol, multiplicity=Multiplicity(1, 1))
    }
)
symbols149: BinaryAssociation = BinaryAssociation(
    name="symbols149",
    ends={
        Property(name="dbl_MetaSymbol151", type=dbl_SyntaxDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SyntaxDefinition150", type=dbl_MetaSymbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
possibleSyntax152: BinaryAssociation = BinaryAssociation(
    name="possibleSyntax152",
    ends={
        Property(name="dbl_SyntaxExpression", type=dbl_MetaSymbol, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MetaSymbol153", type=dbl_SyntaxExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequence154: BinaryAssociation = BinaryAssociation(
    name="sequence154",
    ends={
        Property(name="dbl_SyntaxExpression155", type=dbl_SymbolSequence, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_SymbolSequence", type=dbl_SyntaxExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr174: BinaryAssociation = BinaryAssociation(
    name="expr174",
    ends={
        Property(name="dbl_Expression175", type=dbl_ExpandVariablePart, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandVariablePart", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
metaObject176: BinaryAssociation = BinaryAssociation(
    name="metaObject176",
    ends={
        Property(name="dbl_Expression177", type=dbl_ExpandExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedClassifier157: BinaryAssociation = BinaryAssociation(
    name="ownedClassifier157",
    ends={
        Property(name="dbl_SyntaxSymbolClassifier159", type=dbl_PlainSymbolReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_PlainSymbolReference158", type=dbl_SyntaxSymbolClassifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedClassifier160: BinaryAssociation = BinaryAssociation(
    name="referencedClassifier160",
    ends={
        Property(name="dbl_SyntaxSymbolClassifier162", type=dbl_PlainSymbolReference, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_PlainSymbolReference161", type=dbl_SyntaxSymbolClassifier, multiplicity=Multiplicity(0, 1))
    }
)
expr163: BinaryAssociation = BinaryAssociation(
    name="expr163",
    ends={
        Property(name="dbl_Expression164", type=dbl_MetaExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_MetaExpr", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body165: BinaryAssociation = BinaryAssociation(
    name="body165",
    ends={
        Property(name="dbl_Statement166", type=dbl_TargetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_TargetStatement", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
differingContext167: BinaryAssociation = BinaryAssociation(
    name="differingContext167",
    ends={
        Property(name="dbl_IdExpr168", type=dbl_ExpansionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpansionStatement", type=dbl_IdExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parts169: BinaryAssociation = BinaryAssociation(
    name="parts169",
    ends={
        Property(name="dbl_ExpansionPart", type=dbl_ExpansionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpansionStatement170", type=dbl_ExpansionPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprs171: BinaryAssociation = BinaryAssociation(
    name="exprs171",
    ends={
        Property(name="dbl_Expression173", type=dbl_ExpansionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpansionStatement172", type=dbl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaObject178: BinaryAssociation = BinaryAssociation(
    name="metaObject178",
    ends={
        Property(name="dbl_Expression179", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location180: BinaryAssociation = BinaryAssociation(
    name="location180",
    ends={
        Property(name="dbl_Expression182", type=dbl_ExpandStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_ExpandStatement181", type=dbl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
quotedCode183: BinaryAssociation = BinaryAssociation(
    name="quotedCode183",
    ends={
        Property(name="dbl_QuotedCode", type=dbl_CodeQuoteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_CodeQuoteExpression", type=dbl_QuotedCode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression184: BinaryAssociation = BinaryAssociation(
    name="expression184",
    ends={
        Property(name="dbl_Expression185", type=dbl_QuotedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedExpression", type=dbl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements186: BinaryAssociation = BinaryAssociation(
    name="statements186",
    ends={
        Property(name="dbl_Statement187", type=dbl_QuotedStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_QuotedStatements", type=dbl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context188: BinaryAssociation = BinaryAssociation(
    name="context188",
    ends={
        Property(name="dbl_Parameter189", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern", type=dbl_Parameter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body190: BinaryAssociation = BinaryAssociation(
    name="body190",
    ends={
        Property(name="dbl_Statement192", type=dbl_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="dbl_Pattern191", type=dbl_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_dbl_ConstructiveExtension_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ConstructiveExtension)
gen_dbl_ExtensibleElement_NamedElement = Generalization(general=NamedElement, specific=dbl_ExtensibleElement)
gen_dbl_ExtensibleElement_Construct = Generalization(general=Construct, specific=dbl_ExtensibleElement)
gen_dbl_Module_NamedElement = Generalization(general=NamedElement, specific=dbl_Module)
gen_dbl_Module_ConstructiveExtensionAtContentExtensionPoint = Generalization(general=ConstructiveExtensionAtContentExtensionPoint, specific=dbl_Module)
gen_dbl_Module_Construct = Generalization(general=Construct, specific=dbl_Module)
gen_dbl_Annotation_NamedElement = Generalization(general=NamedElement, specific=dbl_Annotation)
gen_dbl_Class_NamedElement = Generalization(general=NamedElement, specific=dbl_Class)
gen_dbl_Class_Type = Generalization(general=Type, specific=dbl_Class)
gen_dbl_Class_ConstructiveExtensionAtContentExtensionPoint = Generalization(general=ConstructiveExtensionAtContentExtensionPoint, specific=dbl_Class)
gen_dbl_Class_Concept = Generalization(general=Concept, specific=dbl_Class)
gen_dbl_ModuleContentExtension_ConstructiveExtension = Generalization(general=ConstructiveExtension, specific=dbl_ModuleContentExtension)
gen_dbl_ClassContentExtension_ConstructiveExtension = Generalization(general=ConstructiveExtension, specific=dbl_ClassContentExtension)
gen_dbl_PrimitiveType_Type = Generalization(general=Type, specific=dbl_PrimitiveType)
gen_dbl_VoidType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_VoidType)
gen_dbl_IntType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_IntType)
gen_dbl_BoolType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_BoolType)
gen_dbl_DoubleType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_DoubleType)
gen_dbl_StringType_PrimitiveType = Generalization(general=PrimitiveType, specific=dbl_StringType)
gen_dbl_Function_NamedElement = Generalization(general=NamedElement, specific=dbl_Function)
gen_dbl_Function_TypedElement = Generalization(general=TypedElement, specific=dbl_Function)
gen_dbl_Function_LocalScope = Generalization(general=LocalScope, specific=dbl_Function)
gen_dbl_Parameter_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Parameter)
gen_dbl_Statement_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_Statement)
gen_dbl_Statement_AnnotateableElement = Generalization(general=AnnotateableElement, specific=dbl_Statement)
gen_dbl_LoopStatement_Statement = Generalization(general=Statement, specific=dbl_LoopStatement)
gen_dbl_SimpleStatement_Statement = Generalization(general=Statement, specific=dbl_SimpleStatement)
gen_dbl_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Assignment)
gen_dbl_Class_Construct = Generalization(general=Construct, specific=dbl_Class)
gen_dbl_Class_AnnotateableElement = Generalization(general=AnnotateableElement, specific=dbl_Class)
gen_dbl_Constructor_LocalScope = Generalization(general=LocalScope, specific=dbl_Constructor)
gen_dbl_AbstractVariable_NamedElement = Generalization(general=NamedElement, specific=dbl_AbstractVariable)
gen_dbl_AbstractVariable_TypedElement = Generalization(general=TypedElement, specific=dbl_AbstractVariable)
gen_dbl_AbstractVariable_AnnotateableElement = Generalization(general=AnnotateableElement, specific=dbl_AbstractVariable)
gen_dbl_Variable_AbstractVariable = Generalization(general=AbstractVariable, specific=dbl_Variable)
gen_dbl_Variable_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Variable)
gen_dbl_FunctionCall_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_FunctionCall)
gen_dbl_Return_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Return)
gen_dbl_WaitUntil_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_WaitUntil)
gen_dbl_Terminate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Terminate)
gen_dbl_Yield_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Yield)
gen_dbl_Wait_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Wait)
gen_dbl_Reactivate_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Reactivate)
gen_dbl_ActivateObject_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ActivateObject)
gen_dbl_Advance_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Advance)
gen_dbl_Print_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_Print)
gen_dbl_IfStatement_Statement = Generalization(general=Statement, specific=dbl_IfStatement)
gen_dbl_L7Expr_Expression = Generalization(general=Expression, specific=dbl_L7Expr)
gen_dbl_L8Expr_Expression = Generalization(general=Expression, specific=dbl_L8Expr)
gen_dbl_L9Expr_Expression = Generalization(general=Expression, specific=dbl_L9Expr)
gen_dbl_BinaryOperator_Expression = Generalization(general=Expression, specific=dbl_BinaryOperator)
gen_dbl_LocalScopeStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_LocalScopeStatement)
gen_dbl_LocalScopeStatement_LocalScope = Generalization(general=LocalScope, specific=dbl_LocalScopeStatement)
gen_dbl_ForStatement_LoopStatement = Generalization(general=LoopStatement, specific=dbl_ForStatement)
gen_dbl_ForStatement_LocalScope = Generalization(general=LocalScope, specific=dbl_ForStatement)
gen_dbl_WhileStatement_LoopStatement = Generalization(general=LoopStatement, specific=dbl_WhileStatement)
gen_dbl_SwitchStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_SwitchStatement)
gen_dbl_BreakStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_BreakStatement)
gen_dbl_ContinueStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ContinueStatement)
gen_dbl_Expression_TypedElement = Generalization(general=TypedElement, specific=dbl_Expression)
gen_dbl_Expression_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_Expression)
gen_dbl_L1Expr_Expression = Generalization(general=Expression, specific=dbl_L1Expr)
gen_dbl_L2Expr_Expression = Generalization(general=Expression, specific=dbl_L2Expr)
gen_dbl_L3Expr_Expression = Generalization(general=Expression, specific=dbl_L3Expr)
gen_dbl_L4Expr_Expression = Generalization(general=Expression, specific=dbl_L4Expr)
gen_dbl_L5Expr_Expression = Generalization(general=Expression, specific=dbl_L5Expr)
gen_dbl_L6Expr_Expression = Generalization(general=Expression, specific=dbl_L6Expr)
gen_dbl_StringLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_StringLiteral)
gen_dbl_IntLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_IntLiteral)
gen_dbl_TrueLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_TrueLiteral)
gen_dbl_FalseLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_FalseLiteral)
gen_dbl_DoubleLiteral_L1Expr = Generalization(general=L1Expr, specific=dbl_DoubleLiteral)
gen_dbl_UnaryOperator_Expression = Generalization(general=Expression, specific=dbl_UnaryOperator)
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
gen_dbl_VariableAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_VariableAccess)
gen_dbl_MetaAccess_VariableAccess = Generalization(general=VariableAccess, specific=dbl_MetaAccess)
gen_dbl_TypeAccess_ElementAccess = Generalization(general=ElementAccess, specific=dbl_TypeAccess)
gen_dbl_Extension_Concept = Generalization(general=Concept, specific=dbl_Extension)
gen_dbl_Extension_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_Extension)
gen_dbl_ExpandExpr_Expression = Generalization(general=Expression, specific=dbl_ExpandExpr)
gen_dbl_ParseExpr_Expression = Generalization(general=Expression, specific=dbl_ParseExpr)
gen_dbl_MeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MeLiteral)
gen_dbl_SuperLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SuperLiteral)
gen_dbl_MetaLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_MetaLiteral)
gen_dbl_TypeLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_TypeLiteral)
gen_dbl_SizeOfArray_PredefinedId = Generalization(general=PredefinedId, specific=dbl_SizeOfArray)
gen_dbl_AnnotationLiteral_PredefinedId = Generalization(general=PredefinedId, specific=dbl_AnnotationLiteral)
gen_dbl_AnnotationLiteral_Annotation = Generalization(general=Annotation, specific=dbl_AnnotationLiteral)
gen_dbl_IdExpr_L1Expr = Generalization(general=L1Expr, specific=dbl_IdExpr)
gen_dbl_ElementAccess_Expression = Generalization(general=Expression, specific=dbl_ElementAccess)
gen_dbl_PlainSymbolReference_L1SyntaxExpression = Generalization(general=L1SyntaxExpression, specific=dbl_PlainSymbolReference)
gen_dbl_ExtensionSemantics_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_ExtensionSemantics)
gen_dbl_ExtensionSemantics_LocalScope = Generalization(general=LocalScope, specific=dbl_ExtensionSemantics)
gen_dbl_SyntaxDefinition_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_SyntaxDefinition)
gen_dbl_SyntaxSymbolClassifier_NamedElement = Generalization(general=NamedElement, specific=dbl_SyntaxSymbolClassifier)
gen_dbl_SyntaxSymbolClassifier_ExtensibleElement = Generalization(general=ExtensibleElement, specific=dbl_SyntaxSymbolClassifier)
gen_dbl_ComplexSymbol_SyntaxSymbolClassifier = Generalization(general=SyntaxSymbolClassifier, specific=dbl_ComplexSymbol)
gen_dbl_Concept_ComplexSymbol = Generalization(general=ComplexSymbol, specific=dbl_Concept)
gen_dbl_MetaSymbol_NamedElement = Generalization(general=NamedElement, specific=dbl_MetaSymbol)
gen_dbl_MetaSymbol_ComplexSymbol = Generalization(general=ComplexSymbol, specific=dbl_MetaSymbol)
gen_dbl_L3SyntaxExpression_SyntaxExpression = Generalization(general=SyntaxExpression, specific=dbl_L3SyntaxExpression)
gen_dbl_L2SyntaxExpression_SyntaxExpression = Generalization(general=SyntaxExpression, specific=dbl_L2SyntaxExpression)
gen_dbl_SymbolSequence_L2SyntaxExpression = Generalization(general=L2SyntaxExpression, specific=dbl_SymbolSequence)
gen_dbl_L1SyntaxExpression_SyntaxExpression = Generalization(general=SyntaxExpression, specific=dbl_L1SyntaxExpression)
gen_dbl_StructuralSymbolReference_NamedElement = Generalization(general=NamedElement, specific=dbl_StructuralSymbolReference)
gen_dbl_StructuralSymbolReference_PlainSymbolReference = Generalization(general=PlainSymbolReference, specific=dbl_StructuralSymbolReference)
gen_dbl_ExpandExpression_Expression = Generalization(general=Expression, specific=dbl_ExpandExpression)
gen_dbl_ExpandStatement_Statement = Generalization(general=Statement, specific=dbl_ExpandStatement)
gen_dbl_ElementarySymbol_SyntaxSymbolClassifier = Generalization(general=SyntaxSymbolClassifier, specific=dbl_ElementarySymbol)
gen_dbl_IdSymbol_ElementarySymbol = Generalization(general=ElementarySymbol, specific=dbl_IdSymbol)
gen_dbl_IntSymbol_ElementarySymbol = Generalization(general=ElementarySymbol, specific=dbl_IntSymbol)
gen_dbl_StringSymbol_ElementarySymbol = Generalization(general=ElementarySymbol, specific=dbl_StringSymbol)
gen_dbl_Keyword_ElementarySymbol = Generalization(general=ElementarySymbol, specific=dbl_Keyword)
gen_dbl_MetaExpr_Expression = Generalization(general=Expression, specific=dbl_MetaExpr)
gen_dbl_TargetStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_TargetStatement)
gen_dbl_CreateIdStatement_Variable = Generalization(general=Variable, specific=dbl_CreateIdStatement)
gen_dbl_ExpansionStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=dbl_ExpansionStatement)
gen_dbl_ExpandTextPart_ExpansionPart = Generalization(general=ExpansionPart, specific=dbl_ExpandTextPart)
gen_dbl_ExpandVariablePart_ExpansionPart = Generalization(general=ExpansionPart, specific=dbl_ExpandVariablePart)
gen_dbl_CodeQuoteExpression_Expression = Generalization(general=Expression, specific=dbl_CodeQuoteExpression)
gen_dbl_QuotedExpression_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedExpression)
gen_dbl_QuotedStatements_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedStatements)
gen_dbl_QuotedClassContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedClassContent)
gen_dbl_QuotedClassContent_Class = Generalization(general=Class_, specific=dbl_QuotedClassContent)
gen_dbl_QuotedModuleContent_QuotedCode = Generalization(general=QuotedCode, specific=dbl_QuotedModuleContent)
gen_dbl_QuotedModuleContent_Module = Generalization(general=Module, specific=dbl_QuotedModuleContent)
gen_dbl_Pattern_NamedElement = Generalization(general=NamedElement, specific=dbl_Pattern)
gen_dbl_TestStatement_Statement = Generalization(general=Statement, specific=dbl_TestStatement)

# Domain Model
domain_model = DomainModel(
    name="dbl",
    types={dbl_AnnotateableElement, dbl_ConstructiveExtension, ExtensibleElement, dbl_ConstructiveExtensionAtContentExtensionPoint, dbl_Construct, dbl_ExpandExpr, dbl_ExtensibleElement, NamedElement, Construct, dbl_Model, dbl_Import, dbl_Module, ConstructiveExtensionAtContentExtensionPoint, dbl_Class, dbl_Extension, dbl_ExtensionSemantics, dbl_Function, dbl_Variable, dbl_Annotation, dbl_AnnotationItem, dbl_SuperClassSpecification, Concept, dbl_ModuleContentExtension, ConstructiveExtension, dbl_ClassContentExtension, dbl_Type, dbl_ArrayDimension, dbl_TypedElement, dbl_PrimitiveType, dbl_IdExpr, dbl_Expression, Type, dbl_VoidType, PrimitiveType, dbl_IntType, dbl_BoolType, dbl_DoubleType, dbl_StringType, TypedElement, LocalScope, dbl_Parameter, dbl_NativeBinding, dbl_NamedElement, dbl_Statement, dbl_LoopStatement, Statement, dbl_SimpleStatement, dbl_Assignment, AnnotateableElement, dbl_Constructor, dbl_LocalScope, dbl_AbstractVariable, AbstractVariable, SimpleStatement, dbl_VariableAccess, dbl_FunctionCall, dbl_Return, dbl_WaitUntil, dbl_Terminate, dbl_Yield, dbl_Wait, dbl_Reactivate, dbl_ActivateObject, dbl_Advance, dbl_Print, dbl_IfStatement, dbl_L7Expr, dbl_L8Expr, dbl_L9Expr, dbl_BinaryOperator, dbl_LocalScopeStatement, dbl_ForStatement, LoopStatement, dbl_WhileStatement, dbl_SwitchStatement, dbl_SwitchCase, dbl_BreakStatement, dbl_ContinueStatement, dbl_L1Expr, Expression, dbl_L2Expr, dbl_L3Expr, dbl_L4Expr, dbl_L5Expr, dbl_L6Expr, dbl_StringLiteral, dbl_IntLiteral, dbl_TrueLiteral, dbl_FalseLiteral, dbl_DoubleLiteral, dbl_UnaryOperator, dbl_Or, BinaryOperator, L8Expr, dbl_And, L7Expr, dbl_NotEqual, L6Expr, dbl_Equal, dbl_Greater, L5Expr, dbl_GreaterEqual, dbl_Less, dbl_LessEqual, dbl_InstanceOf, dbl_Plus, L4Expr, dbl_Minus, dbl_Mul, L3Expr, dbl_Mod, dbl_Div, dbl_Neg, UnaryOperator, L2Expr, dbl_Not, dbl_Cast, dbl_CreateObject, L1Expr, dbl_NullLiteral, dbl_TimeLiteral, dbl_ActiveLiteral, ElementAccess, dbl_MetaAccess, VariableAccess, dbl_TypeAccess, dbl_Concept, dbl_ParseExpr, dbl_PredefinedId, dbl_MeLiteral, PredefinedId, dbl_SuperLiteral, dbl_MetaLiteral, dbl_TypeLiteral, dbl_SizeOfArray, dbl_AnnotationLiteral, Annotation, dbl_CallPart, dbl_ElementAccess, dbl_PlainSymbolReference, L1SyntaxExpression, dbl_SyntaxDefinition, dbl_MetaSymbol, dbl_SyntaxSymbolClassifier, dbl_ComplexSymbol, SyntaxSymbolClassifier, ComplexSymbol, dbl_SyntaxExpression, dbl_L3SyntaxExpression, SyntaxExpression, dbl_L2SyntaxExpression, dbl_SymbolSequence, L2SyntaxExpression, dbl_L1SyntaxExpression, dbl_StructuralSymbolReference, PlainSymbolReference, dbl_ExpandExpression, dbl_ExpandStatement, dbl_ElementarySymbol, dbl_IdSymbol, ElementarySymbol, dbl_IntSymbol, dbl_StringSymbol, dbl_Keyword, dbl_MetaExpr, dbl_TargetStatement, dbl_CreateIdStatement, Variable, dbl_ExpansionStatement, dbl_ExpansionPart, dbl_ExpandTextPart, ExpansionPart, dbl_ExpandVariablePart, dbl_CodeQuoteExpression, dbl_QuotedCode, dbl_QuotedExpression, QuotedCode, dbl_QuotedStatements, dbl_QuotedClassContent, Class_, dbl_QuotedModuleContent, Module, dbl_Pattern, dbl_TestStatement},
    associations={items17, annotations18, expandExpr0, imports1, modules2, model4, classes7, extensions9, extensionSemantics11, functions13, variables15, class_32, constructorArguments34, contentExtensions20, arrayDimensions21, primitiveType22, typeArrayDimensions23, classifierType26, size28, parameters30, bindings37, superClasses39, constructors42, attributes43, methods46, actionsBlock49, parameters51, owningClass53, initialValue54, condition75, trueCase77, falseCase79, statements82, variable57, value58, callIdExpr61, value63, condition65, objectAccess67, objectAccess69, time71, outputs73, op1111, op2113, termination85, increment87, body90, condition93, body95, variable98, cases100, defaultCase102, value105, body108, op116, idExpr138, extensionPoint140, expr118, astPart121, parentIdExpr124, referencedElement126, predefinedId128, arrayIndex130, callPart133, callArguments135, classifier156, syntaxDefinition142, syntaxDefinition144, startSymbol147, symbols149, possibleSyntax152, sequence154, expr174, metaObject176, ownedClassifier157, referencedClassifier160, expr163, body165, differingContext167, parts169, exprs171, metaObject178, location180, quotedCode183, expression184, statements186, context188, body190},
    generalizations={gen_dbl_ConstructiveExtension_ExtensibleElement, gen_dbl_ExtensibleElement_NamedElement, gen_dbl_ExtensibleElement_Construct, gen_dbl_Module_NamedElement, gen_dbl_Module_ConstructiveExtensionAtContentExtensionPoint, gen_dbl_Module_Construct, gen_dbl_Annotation_NamedElement, gen_dbl_Class_NamedElement, gen_dbl_Class_Type, gen_dbl_Class_ConstructiveExtensionAtContentExtensionPoint, gen_dbl_Class_Concept, gen_dbl_ModuleContentExtension_ConstructiveExtension, gen_dbl_ClassContentExtension_ConstructiveExtension, gen_dbl_PrimitiveType_Type, gen_dbl_VoidType_PrimitiveType, gen_dbl_IntType_PrimitiveType, gen_dbl_BoolType_PrimitiveType, gen_dbl_DoubleType_PrimitiveType, gen_dbl_StringType_PrimitiveType, gen_dbl_Function_NamedElement, gen_dbl_Function_TypedElement, gen_dbl_Function_LocalScope, gen_dbl_Parameter_AbstractVariable, gen_dbl_Statement_ExtensibleElement, gen_dbl_Statement_AnnotateableElement, gen_dbl_LoopStatement_Statement, gen_dbl_SimpleStatement_Statement, gen_dbl_Assignment_SimpleStatement, gen_dbl_Class_Construct, gen_dbl_Class_AnnotateableElement, gen_dbl_Constructor_LocalScope, gen_dbl_AbstractVariable_NamedElement, gen_dbl_AbstractVariable_TypedElement, gen_dbl_AbstractVariable_AnnotateableElement, gen_dbl_Variable_AbstractVariable, gen_dbl_Variable_SimpleStatement, gen_dbl_FunctionCall_SimpleStatement, gen_dbl_Return_SimpleStatement, gen_dbl_WaitUntil_SimpleStatement, gen_dbl_Terminate_SimpleStatement, gen_dbl_Yield_SimpleStatement, gen_dbl_Wait_SimpleStatement, gen_dbl_Reactivate_SimpleStatement, gen_dbl_ActivateObject_SimpleStatement, gen_dbl_Advance_SimpleStatement, gen_dbl_Print_SimpleStatement, gen_dbl_IfStatement_Statement, gen_dbl_L7Expr_Expression, gen_dbl_L8Expr_Expression, gen_dbl_L9Expr_Expression, gen_dbl_BinaryOperator_Expression, gen_dbl_LocalScopeStatement_SimpleStatement, gen_dbl_LocalScopeStatement_LocalScope, gen_dbl_ForStatement_LoopStatement, gen_dbl_ForStatement_LocalScope, gen_dbl_WhileStatement_LoopStatement, gen_dbl_SwitchStatement_SimpleStatement, gen_dbl_BreakStatement_SimpleStatement, gen_dbl_ContinueStatement_SimpleStatement, gen_dbl_Expression_TypedElement, gen_dbl_Expression_ExtensibleElement, gen_dbl_L1Expr_Expression, gen_dbl_L2Expr_Expression, gen_dbl_L3Expr_Expression, gen_dbl_L4Expr_Expression, gen_dbl_L5Expr_Expression, gen_dbl_L6Expr_Expression, gen_dbl_StringLiteral_L1Expr, gen_dbl_IntLiteral_L1Expr, gen_dbl_TrueLiteral_L1Expr, gen_dbl_FalseLiteral_L1Expr, gen_dbl_DoubleLiteral_L1Expr, gen_dbl_UnaryOperator_Expression, gen_dbl_Or_BinaryOperator, gen_dbl_Or_L8Expr, gen_dbl_And_BinaryOperator, gen_dbl_And_L7Expr, gen_dbl_NotEqual_BinaryOperator, gen_dbl_NotEqual_L6Expr, gen_dbl_Equal_BinaryOperator, gen_dbl_Equal_L6Expr, gen_dbl_Greater_BinaryOperator, gen_dbl_Greater_L5Expr, gen_dbl_GreaterEqual_BinaryOperator, gen_dbl_GreaterEqual_L5Expr, gen_dbl_Less_BinaryOperator, gen_dbl_Less_L5Expr, gen_dbl_LessEqual_BinaryOperator, gen_dbl_LessEqual_L5Expr, gen_dbl_InstanceOf_BinaryOperator, gen_dbl_InstanceOf_L5Expr, gen_dbl_Plus_BinaryOperator, gen_dbl_Plus_L4Expr, gen_dbl_Minus_BinaryOperator, gen_dbl_Minus_L4Expr, gen_dbl_Mul_BinaryOperator, gen_dbl_Mul_L3Expr, gen_dbl_Mod_BinaryOperator, gen_dbl_Mod_L3Expr, gen_dbl_Div_BinaryOperator, gen_dbl_Div_L3Expr, gen_dbl_Neg_UnaryOperator, gen_dbl_Neg_L2Expr, gen_dbl_Not_UnaryOperator, gen_dbl_Not_L2Expr, gen_dbl_Cast_UnaryOperator, gen_dbl_Cast_TypedElement, gen_dbl_Cast_L2Expr, gen_dbl_CreateObject_L1Expr, gen_dbl_CreateObject_TypedElement, gen_dbl_NullLiteral_L1Expr, gen_dbl_TimeLiteral_L1Expr, gen_dbl_ActiveLiteral_L1Expr, gen_dbl_VariableAccess_ElementAccess, gen_dbl_MetaAccess_VariableAccess, gen_dbl_TypeAccess_ElementAccess, gen_dbl_Extension_Concept, gen_dbl_Extension_ExtensibleElement, gen_dbl_ExpandExpr_Expression, gen_dbl_ParseExpr_Expression, gen_dbl_MeLiteral_PredefinedId, gen_dbl_SuperLiteral_PredefinedId, gen_dbl_MetaLiteral_PredefinedId, gen_dbl_TypeLiteral_PredefinedId, gen_dbl_SizeOfArray_PredefinedId, gen_dbl_AnnotationLiteral_PredefinedId, gen_dbl_AnnotationLiteral_Annotation, gen_dbl_IdExpr_L1Expr, gen_dbl_ElementAccess_Expression, gen_dbl_PlainSymbolReference_L1SyntaxExpression, gen_dbl_ExtensionSemantics_ExtensibleElement, gen_dbl_ExtensionSemantics_LocalScope, gen_dbl_SyntaxDefinition_ExtensibleElement, gen_dbl_SyntaxSymbolClassifier_NamedElement, gen_dbl_SyntaxSymbolClassifier_ExtensibleElement, gen_dbl_ComplexSymbol_SyntaxSymbolClassifier, gen_dbl_Concept_ComplexSymbol, gen_dbl_MetaSymbol_NamedElement, gen_dbl_MetaSymbol_ComplexSymbol, gen_dbl_L3SyntaxExpression_SyntaxExpression, gen_dbl_L2SyntaxExpression_SyntaxExpression, gen_dbl_SymbolSequence_L2SyntaxExpression, gen_dbl_L1SyntaxExpression_SyntaxExpression, gen_dbl_StructuralSymbolReference_NamedElement, gen_dbl_StructuralSymbolReference_PlainSymbolReference, gen_dbl_ExpandExpression_Expression, gen_dbl_ExpandStatement_Statement, gen_dbl_ElementarySymbol_SyntaxSymbolClassifier, gen_dbl_IdSymbol_ElementarySymbol, gen_dbl_IntSymbol_ElementarySymbol, gen_dbl_StringSymbol_ElementarySymbol, gen_dbl_Keyword_ElementarySymbol, gen_dbl_MetaExpr_Expression, gen_dbl_TargetStatement_SimpleStatement, gen_dbl_CreateIdStatement_Variable, gen_dbl_ExpansionStatement_SimpleStatement, gen_dbl_ExpandTextPart_ExpansionPart, gen_dbl_ExpandVariablePart_ExpansionPart, gen_dbl_CodeQuoteExpression_Expression, gen_dbl_QuotedExpression_QuotedCode, gen_dbl_QuotedStatements_QuotedCode, gen_dbl_QuotedClassContent_QuotedCode, gen_dbl_QuotedClassContent_Class, gen_dbl_QuotedModuleContent_QuotedCode, gen_dbl_QuotedModuleContent_Module, gen_dbl_Pattern_NamedElement, gen_dbl_TestStatement_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)