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
BinaryOp: Enumeration = Enumeration(
    name="BinaryOp",
    literals={
            EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUB"),
			EnumerationLiteral(name="MUL"),
			EnumerationLiteral(name="DIV")
    }
)

ResolveTraceCardinality: Enumeration = Enumeration(
    name="ResolveTraceCardinality",
    literals={
            EnumerationLiteral(name="ONE_ONE"),
			EnumerationLiteral(name="ZERO_OR_ONE"),
			EnumerationLiteral(name="MANY")
    }
)

# Classes
core_LocatedElement = Class(name="core::LocatedElement", is_abstract=True)
core_GenericAnnotation = Class(name="core::GenericAnnotation")
core_AnnotationParameter = Class(name="core::AnnotationParameter", is_abstract=True)
core_RepresentModel = Class(name="core::RepresentModel", is_abstract=True)
core_TransformationDefinition = Class(name="core::TransformationDefinition", is_abstract=True)
ModuleDefinition = Class(name="ModuleDefinition")
core_TransformationDefinitionParameter = Class(name="core::TransformationDefinitionParameter")
core_ImportedModel = Class(name="core::ImportedModel")
core_NamedElement = Class(name="core::NamedElement", is_abstract=True)
core_DefinitionParameter = Class(name="core::DefinitionParameter", is_abstract=True)
NamedElement = Class(name="NamedElement")
core_ModuleParameter = Class(name="core::ModuleParameter")
DefinitionParameter = Class(name="DefinitionParameter")
core_ModuleDefinition = Class(name="core::ModuleDefinition", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
AnnotableElement = Class(name="AnnotableElement")
core_AnnotableElement = Class(name="core::AnnotableElement", is_abstract=True)
core_Annotation = Class(name="core::Annotation", is_abstract=True)
core_ImplicitlyAnnotableElement = Class(name="core::ImplicitlyAnnotableElement")
core_SingleAnnotation = Class(name="core::SingleAnnotation", is_abstract=True)
core_OptimizationsAnnotation = Class(name="core::OptimizationsAnnotation")
Annotation = Class(name="Annotation")
core_MetamodelModelAnnotation = Class(name="core::MetamodelModelAnnotation")
core_PotencyAnnotation = Class(name="core::PotencyAnnotation")
SingleAnnotation = Class(name="SingleAnnotation")
RepresentModel = Class(name="RepresentModel")
core_InlineModel = Class(name="core::InlineModel")
core_UseDeclaration = Class(name="core::UseDeclaration")
core_RequireDeclaration = Class(name="core::RequireDeclaration")
core_EclecticTransformationDefinition = Class(name="core::EclecticTransformationDefinition")
TransformationDefinition = Class(name="TransformationDefinition")
core_Variable = Class(name="core::Variable", is_abstract=True)
core_Statement = Class(name="core::Statement", is_abstract=True)
core_Expression = Class(name="core::Expression", is_abstract=True)
Statement = Class(name="Statement")
core_DefineVariable = Class(name="core::DefineVariable")
Variable = Class(name="Variable")
core_RequireParameter = Class(name="core::RequireParameter", is_abstract=True)
core_RequireModelParameter = Class(name="core::RequireModelParameter")
RequireParameter = Class(name="RequireParameter")
core_MethodCall = Class(name="core::MethodCall")
core_PropertyWrite = Class(name="core::PropertyWrite")
Expression = Class(name="Expression")
core_ModelReference = Class(name="core::ModelReference")
ClassUse = Class(name="ClassUse")
core_VariableReference = Class(name="core::VariableReference")
core_BinaryExpr = Class(name="core::BinaryExpr")
core_KeywordMethodCall = Class(name="core::KeywordMethodCall")
core_KeywordParameter = Class(name="core::KeywordParameter")
core_IfExpr = Class(name="core::IfExpr")
core_IfBranch = Class(name="core::IfBranch")
core_ClosureDeclaration = Class(name="core::ClosureDeclaration")
core_ClosureParameter = Class(name="core::ClosureParameter")
core_ResolveLink = Class(name="core::ResolveLink")
core_StringLiteral = Class(name="core::StringLiteral")
core_BooleanLiteral = Class(name="core::BooleanLiteral")
core_TypeExpression = Class(name="core::TypeExpression", is_abstract=True)
core_ClassUse = Class(name="core::ClassUse")
TypeExpression = Class(name="TypeExpression")
ImplicitlyAnnotableElement = Class(name="ImplicitlyAnnotableElement")
core_TraceUse = Class(name="core::TraceUse")
core_TraceDefinition = Class(name="core::TraceDefinition")
core_NumLiteral = Class(name="core::NumLiteral")
core_DoubleLiteral = Class(name="core::DoubleLiteral")
core_InlineClass = Class(name="core::InlineClass")
core_InlineFeature = Class(name="core::InlineFeature")
core_InlineAttribute = Class(name="core::InlineAttribute")
InlineFeature = Class(name="InlineFeature")
core_InlineReference = Class(name="core::InlineReference")
core_TypedWithClass = Class(name="core::TypedWithClass", is_abstract=True)
core_MatchTrace = Class(name="core::MatchTrace")
core_TraceInterface = Class(name="core::TraceInterface")
core_TracedModelParameter = Class(name="core::TracedModelParameter")
core_TraceCompareExpression = Class(name="core::TraceCompareExpression")
core_TraceElement = Class(name="core::TraceElement")
core_PutTrace = Class(name="core::PutTrace")
core_PutTraceParameter = Class(name="core::PutTraceParameter")

# core_LocatedElement class attributes and methods
core_LocatedElement_row: Property = Property(name="row", type=IntegerType)
core_LocatedElement_column: Property = Property(name="column", type=IntegerType)
core_LocatedElement_file: Property = Property(name="file", type=StringType)
core_LocatedElement.attributes={core_LocatedElement_file, core_LocatedElement_row, core_LocatedElement_column}

# core_GenericAnnotation class attributes and methods
core_GenericAnnotation_name: Property = Property(name="name", type=StringType)
core_GenericAnnotation.attributes={core_GenericAnnotation_name}

# core_AnnotationParameter class attributes and methods

# core_RepresentModel class attributes and methods

# core_TransformationDefinition class attributes and methods

# ModuleDefinition class attributes and methods

# core_TransformationDefinitionParameter class attributes and methods

# core_ImportedModel class attributes and methods

# core_NamedElement class attributes and methods
core_NamedElement_name: Property = Property(name="name", type=StringType)
core_NamedElement.attributes={core_NamedElement_name}

# core_DefinitionParameter class attributes and methods

# NamedElement class attributes and methods

# core_ModuleParameter class attributes and methods

# DefinitionParameter class attributes and methods

# core_ModuleDefinition class attributes and methods

# LocatedElement class attributes and methods

# AnnotableElement class attributes and methods

# core_AnnotableElement class attributes and methods

# core_Annotation class attributes and methods

# core_ImplicitlyAnnotableElement class attributes and methods

# core_SingleAnnotation class attributes and methods

# core_OptimizationsAnnotation class attributes and methods
core_OptimizationsAnnotation_enabled: Property = Property(name="enabled", type=BooleanType)
core_OptimizationsAnnotation.attributes={core_OptimizationsAnnotation_enabled}

# Annotation class attributes and methods

# core_MetamodelModelAnnotation class attributes and methods
core_MetamodelModelAnnotation_metamodel: Property = Property(name="metamodel", type=StringType)
core_MetamodelModelAnnotation.attributes={core_MetamodelModelAnnotation_metamodel}

# core_PotencyAnnotation class attributes and methods
core_PotencyAnnotation_value: Property = Property(name="value", type=StringType)
core_PotencyAnnotation.attributes={core_PotencyAnnotation_value}

# SingleAnnotation class attributes and methods

# RepresentModel class attributes and methods

# core_InlineModel class attributes and methods

# core_UseDeclaration class attributes and methods
core_UseDeclaration_module: Property = Property(name="module", type=StringType)
core_UseDeclaration_as: Property = Property(name="as", type=StringType)
core_UseDeclaration.attributes={core_UseDeclaration_module, core_UseDeclaration_as}

# core_RequireDeclaration class attributes and methods
core_RequireDeclaration_name: Property = Property(name="name", type=StringType)
core_RequireDeclaration_default: Property = Property(name="default", type=StringType)
core_RequireDeclaration.attributes={core_RequireDeclaration_default, core_RequireDeclaration_name}

# core_EclecticTransformationDefinition class attributes and methods

# TransformationDefinition class attributes and methods

# core_Variable class attributes and methods
core_Variable_name: Property = Property(name="name", type=StringType)
core_Variable.attributes={core_Variable_name}

# core_Statement class attributes and methods

# core_Expression class attributes and methods

# Statement class attributes and methods

# core_DefineVariable class attributes and methods

# Variable class attributes and methods

# core_RequireParameter class attributes and methods
core_RequireParameter_formalParameterName: Property = Property(name="formalParameterName", type=StringType)
core_RequireParameter.attributes={core_RequireParameter_formalParameterName}

# core_RequireModelParameter class attributes and methods

# RequireParameter class attributes and methods

# core_MethodCall class attributes and methods
core_MethodCall_methodName: Property = Property(name="methodName", type=StringType)
core_MethodCall_withParameters: Property = Property(name="withParameters", type=BooleanType)
core_MethodCall.attributes={core_MethodCall_withParameters, core_MethodCall_methodName}

# core_PropertyWrite class attributes and methods
core_PropertyWrite_property: Property = Property(name="property", type=StringType)
core_PropertyWrite.attributes={core_PropertyWrite_property}

# Expression class attributes and methods

# core_ModelReference class attributes and methods

# ClassUse class attributes and methods

# core_VariableReference class attributes and methods

# core_BinaryExpr class attributes and methods
core_BinaryExpr_binaryOp: Property = Property(name="binaryOp", type=StringType)
core_BinaryExpr.attributes={core_BinaryExpr_binaryOp}

# core_KeywordMethodCall class attributes and methods

# core_KeywordParameter class attributes and methods
core_KeywordParameter_keyword: Property = Property(name="keyword", type=StringType)
core_KeywordParameter.attributes={core_KeywordParameter_keyword}

# core_IfExpr class attributes and methods

# core_IfBranch class attributes and methods

# core_ClosureDeclaration class attributes and methods

# core_ClosureParameter class attributes and methods

# core_ResolveLink class attributes and methods
core_ResolveLink_isExternal: Property = Property(name="isExternal", type=StringType)
core_ResolveLink_linkName: Property = Property(name="linkName", type=StringType)
core_ResolveLink_featureName: Property = Property(name="featureName", type=StringType)
core_ResolveLink.attributes={core_ResolveLink_featureName, core_ResolveLink_isExternal, core_ResolveLink_linkName}

# core_StringLiteral class attributes and methods
core_StringLiteral_value: Property = Property(name="value", type=StringType)
core_StringLiteral.attributes={core_StringLiteral_value}

# core_BooleanLiteral class attributes and methods
core_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
core_BooleanLiteral.attributes={core_BooleanLiteral_value}

# core_TypeExpression class attributes and methods

# core_ClassUse class attributes and methods
core_ClassUse_className: Property = Property(name="className", type=StringType)
core_ClassUse_strictType: Property = Property(name="strictType", type=BooleanType)
core_ClassUse.attributes={core_ClassUse_strictType, core_ClassUse_className}

# TypeExpression class attributes and methods

# ImplicitlyAnnotableElement class attributes and methods

# core_TraceUse class attributes and methods

# core_TraceDefinition class attributes and methods

# core_NumLiteral class attributes and methods
core_NumLiteral_value: Property = Property(name="value", type=IntegerType)
core_NumLiteral.attributes={core_NumLiteral_value}

# core_DoubleLiteral class attributes and methods
core_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
core_DoubleLiteral.attributes={core_DoubleLiteral_value}

# core_InlineClass class attributes and methods

# core_InlineFeature class attributes and methods
core_InlineFeature_multivalued: Property = Property(name="multivalued", type=BooleanType)
core_InlineFeature.attributes={core_InlineFeature_multivalued}

# core_InlineAttribute class attributes and methods

# InlineFeature class attributes and methods

# core_InlineReference class attributes and methods

# core_TypedWithClass class attributes and methods

# core_MatchTrace class attributes and methods
core_MatchTrace_cardinality: Property = Property(name="cardinality", type=StringType)
core_MatchTrace.attributes={core_MatchTrace_cardinality}

# core_TraceInterface class attributes and methods

# core_TracedModelParameter class attributes and methods

# core_TraceCompareExpression class attributes and methods
core_TraceCompareExpression_multivaluedTag: Property = Property(name="multivaluedTag", type=BooleanType)
core_TraceCompareExpression.attributes={core_TraceCompareExpression_multivaluedTag}

# core_TraceElement class attributes and methods

# core_PutTrace class attributes and methods

# core_PutTraceParameter class attributes and methods

# Relationships
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="core_AnnotationParameter", type=core_GenericAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="core_GenericAnnotation", type=core_AnnotationParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inModels4: BinaryAssociation = BinaryAssociation(
    name="inModels4",
    ends={
        Property(name="core_TransformationDefinitionParameter", type=core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TransformationDefinition", type=core_TransformationDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outModels5: BinaryAssociation = BinaryAssociation(
    name="outModels5",
    ends={
        Property(name="core_TransformationDefinitionParameter7", type=core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TransformationDefinition6", type=core_TransformationDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedWith0: BinaryAssociation = BinaryAssociation(
    name="annotatedWith0",
    ends={
        Property(name="Annotation", type=core_AnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedElement", type=core_Annotation, multiplicity=Multiplicity(0, 9999))
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="core_SingleAnnotation", type=core_ImplicitlyAnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ImplicitlyAnnotableElement", type=core_SingleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement2: BinaryAssociation = BinaryAssociation(
    name="annotatedElement2",
    ends={
        Property(name="AnnotableElement", type=core_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedWith", type=core_AnnotableElement, multiplicity=Multiplicity(0, 1))
    }
)
transformations18: BinaryAssociation = BinaryAssociation(
    name="transformations18",
    ends={
        Property(name="core_TransformationDefinition19", type=core_EclecticTransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_EclecticTransformationDefinition", type=core_TransformationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedModels8: BinaryAssociation = BinaryAssociation(
    name="importedModels8",
    ends={
        Property(name="core_ImportedModel", type=core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TransformationDefinition9", type=core_ImportedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineModels10: BinaryAssociation = BinaryAssociation(
    name="inlineModels10",
    ends={
        Property(name="core_InlineModel", type=core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TransformationDefinition11", type=core_InlineModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations12: BinaryAssociation = BinaryAssociation(
    name="annotations12",
    ends={
        Property(name="core_Annotation", type=core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TransformationDefinition13", type=core_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses14: BinaryAssociation = BinaryAssociation(
    name="uses14",
    ends={
        Property(name="core_UseDeclaration", type=core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TransformationDefinition15", type=core_UseDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requires16: BinaryAssociation = BinaryAssociation(
    name="requires16",
    ends={
        Property(name="core_RequireDeclaration", type=core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TransformationDefinition17", type=core_RequireDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression23: BinaryAssociation = BinaryAssociation(
    name="expression23",
    ends={
        Property(name="core_Expression", type=core_DefineVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="core_DefineVariable", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters20: BinaryAssociation = BinaryAssociation(
    name="parameters20",
    ends={
        Property(name="core_RequireParameter", type=core_RequireDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_RequireDeclaration21", type=core_RequireParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model22: BinaryAssociation = BinaryAssociation(
    name="model22",
    ends={
        Property(name="core_RepresentModel", type=core_RequireModelParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="core_RequireModelParameter", type=core_RepresentModel, multiplicity=Multiplicity(1, 1))
    }
)
receptor30: BinaryAssociation = BinaryAssociation(
    name="receptor30",
    ends={
        Property(name="core_Expression31", type=core_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="core_MethodCall", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters32: BinaryAssociation = BinaryAssociation(
    name="parameters32",
    ends={
        Property(name="core_Expression34", type=core_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="core_MethodCall33", type=core_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receptor24: BinaryAssociation = BinaryAssociation(
    name="receptor24",
    ends={
        Property(name="core_Variable", type=core_PropertyWrite, multiplicity=Multiplicity(1, 1)),
        Property(name="core_PropertyWrite", type=core_Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression25: BinaryAssociation = BinaryAssociation(
    name="expression25",
    ends={
        Property(name="core_Expression27", type=core_PropertyWrite, multiplicity=Multiplicity(1, 1)),
        Property(name="core_PropertyWrite26", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable28: BinaryAssociation = BinaryAssociation(
    name="variable28",
    ends={
        Property(name="core_Variable29", type=core_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="core_VariableReference", type=core_Variable, multiplicity=Multiplicity(1, 1))
    }
)
value39: BinaryAssociation = BinaryAssociation(
    name="value39",
    ends={
        Property(name="core_KeywordParameter40", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="core_Expression41", type=core_KeywordParameter, multiplicity=Multiplicity(1, 1))
    }
)
left42: BinaryAssociation = BinaryAssociation(
    name="left42",
    ends={
        Property(name="core_Expression43", type=core_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="core_BinaryExpr", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receptor35: BinaryAssociation = BinaryAssociation(
    name="receptor35",
    ends={
        Property(name="core_Expression36", type=core_KeywordMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="core_KeywordMethodCall", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters37: BinaryAssociation = BinaryAssociation(
    name="parameters37",
    ends={
        Property(name="core_KeywordParameter", type=core_KeywordMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="core_KeywordMethodCall38", type=core_KeywordParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module52: BinaryAssociation = BinaryAssociation(
    name="module52",
    ends={
        Property(name="core_UseDeclaration54", type=core_ResolveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ResolveLink53", type=core_UseDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
then55: BinaryAssociation = BinaryAssociation(
    name="then55",
    ends={
        Property(name="core_IfBranch", type=core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="core_IfExpr", type=core_IfBranch, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsifs56: BinaryAssociation = BinaryAssociation(
    name="elsifs56",
    ends={
        Property(name="core_IfBranch58", type=core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="core_IfExpr57", type=core_IfBranch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else59: BinaryAssociation = BinaryAssociation(
    name="else59",
    ends={
        Property(name="core_IfBranch61", type=core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="core_IfExpr60", type=core_IfBranch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right44: BinaryAssociation = BinaryAssociation(
    name="right44",
    ends={
        Property(name="core_Expression46", type=core_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="core_BinaryExpr45", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition62: BinaryAssociation = BinaryAssociation(
    name="condition62",
    ends={
        Property(name="core_Expression64", type=core_IfBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="core_IfBranch63", type=core_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements47: BinaryAssociation = BinaryAssociation(
    name="statements47",
    ends={
        Property(name="core_Statement", type=core_ClosureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ClosureDeclaration", type=core_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameters48: BinaryAssociation = BinaryAssociation(
    name="formalParameters48",
    ends={
        Property(name="core_ClosureParameter", type=core_ClosureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ClosureDeclaration49", type=core_ClosureParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr50: BinaryAssociation = BinaryAssociation(
    name="expr50",
    ends={
        Property(name="core_Expression51", type=core_ResolveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ResolveLink", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model68: BinaryAssociation = BinaryAssociation(
    name="model68",
    ends={
        Property(name="core_RepresentModel69", type=core_ClassUse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_ClassUse", type=core_RepresentModel, multiplicity=Multiplicity(1, 1))
    }
)
trace70: BinaryAssociation = BinaryAssociation(
    name="trace70",
    ends={
        Property(name="core_TraceDefinition", type=core_TraceUse, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TraceUse", type=core_TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
statements65: BinaryAssociation = BinaryAssociation(
    name="statements65",
    ends={
        Property(name="core_Statement67", type=core_IfBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="core_IfBranch66", type=core_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes79: BinaryAssociation = BinaryAssociation(
    name="classes79",
    ends={
        Property(name="core_InlineClass", type=core_InlineModel, multiplicity=Multiplicity(1, 1)),
        Property(name="core_InlineModel80", type=core_InlineClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features81: BinaryAssociation = BinaryAssociation(
    name="features81",
    ends={
        Property(name="core_InlineFeature", type=core_InlineClass, multiplicity=Multiplicity(1, 1)),
        Property(name="core_InlineClass82", type=core_InlineFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type83: BinaryAssociation = BinaryAssociation(
    name="type83",
    ends={
        Property(name="core_TypeExpression85", type=core_InlineFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="core_InlineFeature84", type=core_TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type_71: BinaryAssociation = BinaryAssociation(
    name="type_71",
    ends={
        Property(name="core_ClassUse72", type=core_TypedWithClass, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TypedWithClass", type=core_ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trace86: BinaryAssociation = BinaryAssociation(
    name="trace86",
    ends={
        Property(name="core_TraceDefinition87", type=core_MatchTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="core_MatchTrace", type=core_TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
definitions73: BinaryAssociation = BinaryAssociation(
    name="definitions73",
    ends={
        Property(name="core_TraceDefinition74", type=core_TraceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TraceInterface", type=core_TraceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceExpr88: BinaryAssociation = BinaryAssociation(
    name="traceExpr88",
    ends={
        Property(name="core_TraceCompareExpression", type=core_MatchTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="core_MatchTrace89", type=core_TraceCompareExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elements75: BinaryAssociation = BinaryAssociation(
    name="elements75",
    ends={
        Property(name="core_TraceElement", type=core_TraceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TraceDefinition76", type=core_TraceElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type77: BinaryAssociation = BinaryAssociation(
    name="type77",
    ends={
        Property(name="core_TypeExpression", type=core_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TraceElement78", type=core_TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
traceVar103: BinaryAssociation = BinaryAssociation(
    name="traceVar103",
    ends={
        Property(name="core_PutTraceParameter104", type=core_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TraceElement105", type=core_PutTraceParameter, multiplicity=Multiplicity(1, 1))
    }
)
traceVar90: BinaryAssociation = BinaryAssociation(
    name="traceVar90",
    ends={
        Property(name="core_TraceElement92", type=core_TraceCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TraceCompareExpression91", type=core_TraceElement, multiplicity=Multiplicity(1, 1))
    }
)
expr93: BinaryAssociation = BinaryAssociation(
    name="expr93",
    ends={
        Property(name="core_Expression95", type=core_TraceCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="core_TraceCompareExpression94", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trace96: BinaryAssociation = BinaryAssociation(
    name="trace96",
    ends={
        Property(name="core_TraceDefinition97", type=core_PutTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="core_PutTrace", type=core_TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parameters98: BinaryAssociation = BinaryAssociation(
    name="parameters98",
    ends={
        Property(name="core_PutTraceParameter", type=core_PutTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="core_PutTrace99", type=core_PutTraceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value100: BinaryAssociation = BinaryAssociation(
    name="value100",
    ends={
        Property(name="core_Expression102", type=core_PutTraceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="core_PutTraceParameter101", type=core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_core_RepresentModel_AnnotableElement = Generalization(general=AnnotableElement, specific=core_RepresentModel)
gen_core_TransformationDefinition_ModuleDefinition = Generalization(general=ModuleDefinition, specific=core_TransformationDefinition)
gen_core_DefinitionParameter_NamedElement = Generalization(general=NamedElement, specific=core_DefinitionParameter)
gen_core_ModuleParameter_DefinitionParameter = Generalization(general=DefinitionParameter, specific=core_ModuleParameter)
gen_core_ModuleDefinition_LocatedElement = Generalization(general=LocatedElement, specific=core_ModuleDefinition)
gen_core_ModuleDefinition_NamedElement = Generalization(general=NamedElement, specific=core_ModuleDefinition)
gen_core_ModuleDefinition_AnnotableElement = Generalization(general=AnnotableElement, specific=core_ModuleDefinition)
gen_core_OptimizationsAnnotation_Annotation = Generalization(general=Annotation, specific=core_OptimizationsAnnotation)
gen_core_MetamodelModelAnnotation_Annotation = Generalization(general=Annotation, specific=core_MetamodelModelAnnotation)
gen_core_SingleAnnotation_Annotation = Generalization(general=Annotation, specific=core_SingleAnnotation)
gen_core_PotencyAnnotation_SingleAnnotation = Generalization(general=SingleAnnotation, specific=core_PotencyAnnotation)
gen_core_TransformationDefinitionParameter_DefinitionParameter = Generalization(general=DefinitionParameter, specific=core_TransformationDefinitionParameter)
gen_core_TransformationDefinitionParameter_RepresentModel = Generalization(general=RepresentModel, specific=core_TransformationDefinitionParameter)
gen_core_ImportedModel_RepresentModel = Generalization(general=RepresentModel, specific=core_ImportedModel)
gen_core_ImportedModel_NamedElement = Generalization(general=NamedElement, specific=core_ImportedModel)
gen_core_EclecticTransformationDefinition_TransformationDefinition = Generalization(general=TransformationDefinition, specific=core_EclecticTransformationDefinition)
gen_core_Statement_LocatedElement = Generalization(general=LocatedElement, specific=core_Statement)
gen_core_Expression_Statement = Generalization(general=Statement, specific=core_Expression)
gen_core_DefineVariable_Statement = Generalization(general=Statement, specific=core_DefineVariable)
gen_core_DefineVariable_Variable = Generalization(general=Variable, specific=core_DefineVariable)
gen_core_UseDeclaration_RepresentModel = Generalization(general=RepresentModel, specific=core_UseDeclaration)
gen_core_RequireDeclaration_RepresentModel = Generalization(general=RepresentModel, specific=core_RequireDeclaration)
gen_core_RequireModelParameter_RequireParameter = Generalization(general=RequireParameter, specific=core_RequireModelParameter)
gen_core_MethodCall_Expression = Generalization(general=Expression, specific=core_MethodCall)
gen_core_PropertyWrite_Expression = Generalization(general=Expression, specific=core_PropertyWrite)
gen_core_ModelReference_ClassUse = Generalization(general=ClassUse, specific=core_ModelReference)
gen_core_ModelReference_Expression = Generalization(general=Expression, specific=core_ModelReference)
gen_core_VariableReference_Expression = Generalization(general=Expression, specific=core_VariableReference)
gen_core_BinaryExpr_Expression = Generalization(general=Expression, specific=core_BinaryExpr)
gen_core_KeywordMethodCall_Expression = Generalization(general=Expression, specific=core_KeywordMethodCall)
gen_core_IfExpr_Expression = Generalization(general=Expression, specific=core_IfExpr)
gen_core_ClosureDeclaration_Expression = Generalization(general=Expression, specific=core_ClosureDeclaration)
gen_core_ClosureParameter_Variable = Generalization(general=Variable, specific=core_ClosureParameter)
gen_core_ResolveLink_Expression = Generalization(general=Expression, specific=core_ResolveLink)
gen_core_StringLiteral_Expression = Generalization(general=Expression, specific=core_StringLiteral)
gen_core_BooleanLiteral_Expression = Generalization(general=Expression, specific=core_BooleanLiteral)
gen_core_ClassUse_TypeExpression = Generalization(general=TypeExpression, specific=core_ClassUse)
gen_core_ClassUse_ImplicitlyAnnotableElement = Generalization(general=ImplicitlyAnnotableElement, specific=core_ClassUse)
gen_core_TraceUse_TypeExpression = Generalization(general=TypeExpression, specific=core_TraceUse)
gen_core_NumLiteral_Expression = Generalization(general=Expression, specific=core_NumLiteral)
gen_core_DoubleLiteral_Expression = Generalization(general=Expression, specific=core_DoubleLiteral)
gen_core_InlineModel_ModuleDefinition = Generalization(general=ModuleDefinition, specific=core_InlineModel)
gen_core_InlineModel_RepresentModel = Generalization(general=RepresentModel, specific=core_InlineModel)
gen_core_InlineClass_NamedElement = Generalization(general=NamedElement, specific=core_InlineClass)
gen_core_InlineFeature_NamedElement = Generalization(general=NamedElement, specific=core_InlineFeature)
gen_core_InlineAttribute_InlineFeature = Generalization(general=InlineFeature, specific=core_InlineAttribute)
gen_core_InlineReference_InlineFeature = Generalization(general=InlineFeature, specific=core_InlineReference)
gen_core_MatchTrace_Expression = Generalization(general=Expression, specific=core_MatchTrace)
gen_core_TraceInterface_ModuleDefinition = Generalization(general=ModuleDefinition, specific=core_TraceInterface)
gen_core_TracedModelParameter_DefinitionParameter = Generalization(general=DefinitionParameter, specific=core_TracedModelParameter)
gen_core_TracedModelParameter_RepresentModel = Generalization(general=RepresentModel, specific=core_TracedModelParameter)
gen_core_TraceDefinition_NamedElement = Generalization(general=NamedElement, specific=core_TraceDefinition)
gen_core_TraceElement_NamedElement = Generalization(general=NamedElement, specific=core_TraceElement)
gen_core_PutTrace_Expression = Generalization(general=Expression, specific=core_PutTrace)

# Domain Model
domain_model = DomainModel(
    name="core",
    types={core_LocatedElement, core_GenericAnnotation, core_AnnotationParameter, core_RepresentModel, core_TransformationDefinition, ModuleDefinition, core_TransformationDefinitionParameter, core_ImportedModel, core_NamedElement, core_DefinitionParameter, NamedElement, core_ModuleParameter, DefinitionParameter, core_ModuleDefinition, LocatedElement, AnnotableElement, core_AnnotableElement, core_Annotation, core_ImplicitlyAnnotableElement, core_SingleAnnotation, core_OptimizationsAnnotation, Annotation, core_MetamodelModelAnnotation, core_PotencyAnnotation, SingleAnnotation, RepresentModel, core_InlineModel, core_UseDeclaration, core_RequireDeclaration, core_EclecticTransformationDefinition, TransformationDefinition, core_Variable, core_Statement, core_Expression, Statement, core_DefineVariable, Variable, core_RequireParameter, core_RequireModelParameter, RequireParameter, core_MethodCall, core_PropertyWrite, Expression, core_ModelReference, ClassUse, core_VariableReference, core_BinaryExpr, core_KeywordMethodCall, core_KeywordParameter, core_IfExpr, core_IfBranch, core_ClosureDeclaration, core_ClosureParameter, core_ResolveLink, core_StringLiteral, core_BooleanLiteral, core_TypeExpression, core_ClassUse, TypeExpression, ImplicitlyAnnotableElement, core_TraceUse, core_TraceDefinition, core_NumLiteral, core_DoubleLiteral, core_InlineClass, core_InlineFeature, core_InlineAttribute, InlineFeature, core_InlineReference, core_TypedWithClass, core_MatchTrace, core_TraceInterface, core_TracedModelParameter, core_TraceCompareExpression, core_TraceElement, core_PutTrace, core_PutTraceParameter, BinaryOp, ResolveTraceCardinality},
    associations={parameters3, inModels4, outModels5, annotatedWith0, annotations1, annotatedElement2, transformations18, importedModels8, inlineModels10, annotations12, uses14, requires16, expression23, parameters20, model22, receptor30, parameters32, receptor24, expression25, variable28, value39, left42, receptor35, parameters37, module52, then55, elsifs56, else59, right44, condition62, statements47, formalParameters48, expr50, model68, trace70, statements65, classes79, features81, type83, type_71, trace86, definitions73, traceExpr88, elements75, type77, traceVar103, traceVar90, expr93, trace96, parameters98, value100},
    generalizations={gen_core_RepresentModel_AnnotableElement, gen_core_TransformationDefinition_ModuleDefinition, gen_core_DefinitionParameter_NamedElement, gen_core_ModuleParameter_DefinitionParameter, gen_core_ModuleDefinition_LocatedElement, gen_core_ModuleDefinition_NamedElement, gen_core_ModuleDefinition_AnnotableElement, gen_core_OptimizationsAnnotation_Annotation, gen_core_MetamodelModelAnnotation_Annotation, gen_core_SingleAnnotation_Annotation, gen_core_PotencyAnnotation_SingleAnnotation, gen_core_TransformationDefinitionParameter_DefinitionParameter, gen_core_TransformationDefinitionParameter_RepresentModel, gen_core_ImportedModel_RepresentModel, gen_core_ImportedModel_NamedElement, gen_core_EclecticTransformationDefinition_TransformationDefinition, gen_core_Statement_LocatedElement, gen_core_Expression_Statement, gen_core_DefineVariable_Statement, gen_core_DefineVariable_Variable, gen_core_UseDeclaration_RepresentModel, gen_core_RequireDeclaration_RepresentModel, gen_core_RequireModelParameter_RequireParameter, gen_core_MethodCall_Expression, gen_core_PropertyWrite_Expression, gen_core_ModelReference_ClassUse, gen_core_ModelReference_Expression, gen_core_VariableReference_Expression, gen_core_BinaryExpr_Expression, gen_core_KeywordMethodCall_Expression, gen_core_IfExpr_Expression, gen_core_ClosureDeclaration_Expression, gen_core_ClosureParameter_Variable, gen_core_ResolveLink_Expression, gen_core_StringLiteral_Expression, gen_core_BooleanLiteral_Expression, gen_core_ClassUse_TypeExpression, gen_core_ClassUse_ImplicitlyAnnotableElement, gen_core_TraceUse_TypeExpression, gen_core_NumLiteral_Expression, gen_core_DoubleLiteral_Expression, gen_core_InlineModel_ModuleDefinition, gen_core_InlineModel_RepresentModel, gen_core_InlineClass_NamedElement, gen_core_InlineFeature_NamedElement, gen_core_InlineAttribute_InlineFeature, gen_core_InlineReference_InlineFeature, gen_core_MatchTrace_Expression, gen_core_TraceInterface_ModuleDefinition, gen_core_TracedModelParameter_DefinitionParameter, gen_core_TracedModelParameter_RepresentModel, gen_core_TraceDefinition_NamedElement, gen_core_TraceElement_NamedElement, gen_core_PutTrace_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)