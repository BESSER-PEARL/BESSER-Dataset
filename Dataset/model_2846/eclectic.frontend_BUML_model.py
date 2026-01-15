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
MappingCardinality: Enumeration = Enumeration(
    name="MappingCardinality",
    literals={
            EnumerationLiteral(name="OneToOne"),
			EnumerationLiteral(name="NToOne"),
			EnumerationLiteral(name="OneToN")
    }
)

BinaryOp: Enumeration = Enumeration(
    name="BinaryOp",
    literals={
            EnumerationLiteral(name="DIV"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="ADD"),
			EnumerationLiteral(name="SUB"),
			EnumerationLiteral(name="MUL")
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
frontend_script_ScriptedTransformation = Class(name="frontend::script::ScriptedTransformation")
TransformationDefinition = Class(name="TransformationDefinition")
Statement = Class(name="Statement")
frontend_koan_KoanTransformation = Class(name="frontend::koan::KoanTransformation")
TraceInterface = Class(name="TraceInterface")
KoanRule = Class(name="KoanRule")
frontend_koan_KoanRule = Class(name="frontend::koan::KoanRule")
core_LocatedElement = Class(name="core::LocatedElement")
core_NamedElement = Class(name="core::NamedElement")
Matcher = Class(name="Matcher")
frontend_koan_Matcher = Class(name="frontend::koan::Matcher", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
frontend_koan_ForAllMatcher = Class(name="frontend::koan::ForAllMatcher")
koan_Matcher = Class(name="koan::Matcher")
frontend_DummyRootMetaclass = Class(name="frontend::DummyRootMetaclass")
frontend_attribution_AttributionTransformation = Class(name="frontend::attribution::AttributionTransformation")
AttributeDcl = Class(name="AttributeDcl")
AttributionRule = Class(name="AttributionRule")
frontend_attribution_AttributeDcl = Class(name="frontend::attribution::AttributeDcl", is_abstract=True)
core_TypedWithClass = Class(name="core::TypedWithClass")
frontend_attribution_InheritedAttributeDcl = Class(name="frontend::attribution::InheritedAttributeDcl")
core_Variable = Class(name="core::Variable")
ClassUse = Class(name="ClassUse")
frontend_attribution_RuleSelf = Class(name="frontend::attribution::RuleSelf")
Variable = Class(name="Variable")
frontend_attribution_AttributeInit = Class(name="frontend::attribution::AttributeInit")
frontend_attribution_AttributeUse = Class(name="frontend::attribution::AttributeUse")
frontend_attribution_SynthesizedAttributeDcl = Class(name="frontend::attribution::SynthesizedAttributeDcl")
frontend_attribution_AttributionRule = Class(name="frontend::attribution::AttributionRule")
RuleSelf = Class(name="RuleSelf")
Expression = Class(name="Expression")
MethodParameter = Class(name="MethodParameter")
MethodSelf = Class(name="MethodSelf")
frontend_imperative_MethodSelf = Class(name="frontend::imperative::MethodSelf")
frontend_imperative_MethodParameter = Class(name="frontend::imperative::MethodParameter")
frontend_chain_ChainTransformation = Class(name="frontend::chain::ChainTransformation")
frontend_imperative_ImperativeTransformation = Class(name="frontend::imperative::ImperativeTransformation")
MethodDefinition = Class(name="MethodDefinition")
frontend_chain_GeneratedModel = Class(name="frontend::chain::GeneratedModel")
frontend_imperative_MethodDefinition = Class(name="frontend::imperative::MethodDefinition")
core_RepresentModel = Class(name="core::RepresentModel")
frontend_chain_TransformationExecution = Class(name="frontend::chain::TransformationExecution")
AvailableTransformation = Class(name="AvailableTransformation")
RepresentModel = Class(name="RepresentModel")
frontend_chain_AvailableTransformation = Class(name="frontend::chain::AvailableTransformation", is_abstract=True)
frontend_chain_ExternalTransformation = Class(name="frontend::chain::ExternalTransformation")
chain_AvailableTransformation = Class(name="chain::AvailableTransformation")
frontend_chain_CompositeTransformation = Class(name="frontend::chain::CompositeTransformation")
core_TransformationDefinition = Class(name="core::TransformationDefinition")
CompositeTransformation = Class(name="CompositeTransformation")
ExternalTransformation = Class(name="ExternalTransformation")
GeneratedModel = Class(name="GeneratedModel")
TransformationExecution = Class(name="TransformationExecution")
POutputVariable = Class(name="POutputVariable")
frontend_patterns_POutputVariable = Class(name="frontend::patterns::POutputVariable")
frontend_patterns_PObject = Class(name="frontend::patterns::PObject")
PFeature = Class(name="PFeature")
frontend_patterns_PFeature = Class(name="frontend::patterns::PFeature", is_abstract=True)
frontend_patterns_PatternSpecification = Class(name="frontend::patterns::PatternSpecification")
Pattern = Class(name="Pattern")
frontend_patterns_Pattern = Class(name="frontend::patterns::Pattern")
PObject = Class(name="PObject")
frontend_patterns_CollectionReference = Class(name="frontend::patterns::CollectionReference")
PReference = Class(name="PReference")
frontend_mappings_MappingTransformation = Class(name="frontend::mappings::MappingTransformation")
Delegate = Class(name="Delegate")
Context = Class(name="Context")
frontend_mappings_MappingVariable = Class(name="frontend::mappings::MappingVariable")
frontend_mappings_MatchedElement = Class(name="frontend::mappings::MatchedElement")
core_ClassUse = Class(name="core::ClassUse")
mappings_MappingVariable = Class(name="mappings::MappingVariable")
frontend_mappings_Delegate = Class(name="frontend::mappings::Delegate")
frontend_patterns_PAttribute = Class(name="frontend::patterns::PAttribute")
UseDeclaration = Class(name="UseDeclaration")
frontend_patterns_PReference = Class(name="frontend::patterns::PReference")
Tag = Class(name="Tag")
frontend_mappings_Context = Class(name="frontend::mappings::Context")
MappingElement = Class(name="MappingElement")
C2CModifier = Class(name="C2CModifier")
MatchedElement = Class(name="MatchedElement")
frontend_mappings_MappingElement = Class(name="frontend::mappings::MappingElement", is_abstract=True)
frontend_mappings_ClassMapping = Class(name="frontend::mappings::ClassMapping", is_abstract=True)
frontend_mappings_Feature2Feature = Class(name="frontend::mappings::Feature2Feature", is_abstract=True)
FeatureRef = Class(name="FeatureRef")
Converter = Class(name="Converter")
frontend_mappings_AttributeMapping = Class(name="frontend::mappings::AttributeMapping")
Feature2Feature = Class(name="Feature2Feature")
Section = Class(name="Section")
frontend_mappings_Section = Class(name="frontend::mappings::Section")
frontend_mappings_AttributeIsInteger = Class(name="frontend::mappings::AttributeIsInteger")
frontend_mappings_Converter = Class(name="frontend::mappings::Converter")
frontend_mappings_Tag = Class(name="frontend::mappings::Tag")
NamedElement = Class(name="NamedElement")
frontend_mappings_Class2Class = Class(name="frontend::mappings::Class2Class")
ClassMapping = Class(name="ClassMapping")
ClassRef = Class(name="ClassRef")
Attribute2Attribute = Class(name="Attribute2Attribute")
frontend_mappings_C2CModifier = Class(name="frontend::mappings::C2CModifier", is_abstract=True)
frontend_mappings_RelatedBy = Class(name="frontend::mappings::RelatedBy")
AttributeRef = Class(name="AttributeRef")
AttributeRightPart = Class(name="AttributeRightPart")
frontend_mappings_AttributeRightPart = Class(name="frontend::mappings::AttributeRightPart", is_abstract=True)
frontend_mappings_AttributeIsString = Class(name="frontend::mappings::AttributeIsString")
frontend_mappings_AttributeIsBoolean = Class(name="frontend::mappings::AttributeIsBoolean")
frontend_mappings_AttributeIsDouble = Class(name="frontend::mappings::AttributeIsDouble")
frontend_mappings_AttributeIsResolveLink = Class(name="frontend::mappings::AttributeIsResolveLink")
ResolveLink = Class(name="ResolveLink")
frontend_mappings_Join = Class(name="frontend::mappings::Join")
frontend_mappings_Attribute2Attribute = Class(name="frontend::mappings::Attribute2Attribute")
mappings_Feature2Feature = Class(name="mappings::Feature2Feature")
mappings_AttributeRightPart = Class(name="mappings::AttributeRightPart")
Class2Class = Class(name="Class2Class")
AttributeModifier = Class(name="AttributeModifier")
frontend_mappings_Reference2Reference = Class(name="frontend::mappings::Reference2Reference")
ReferenceRef = Class(name="ReferenceRef")
frontend_mappings_Modifier = Class(name="frontend::mappings::Modifier", is_abstract=True)
frontend_mappings_AttributeModifier = Class(name="frontend::mappings::AttributeModifier", is_abstract=True)
Modifier = Class(name="Modifier")
frontend_mappings_LinkedBy = Class(name="frontend::mappings::LinkedBy")
frontend_mappings_EqualityFilter = Class(name="frontend::mappings::EqualityFilter")
frontend_mappings_Operator = Class(name="frontend::mappings::Operator", is_abstract=True)
frontend_mappings_Split = Class(name="frontend::mappings::Split")
Operator = Class(name="Operator")
frontend_mappings_FeatureRef = Class(name="frontend::mappings::FeatureRef")
mappings_MetamodelElementRef = Class(name="mappings::MetamodelElementRef")
frontend_mappings_AttributeRef = Class(name="frontend::mappings::AttributeRef")
frontend_mappings_ReferenceRef = Class(name="frontend::mappings::ReferenceRef")
frontend_qool_QoolTransformation = Class(name="frontend::qool::QoolTransformation")
QoolQueue = Class(name="QoolQueue")
Segment = Class(name="Segment")
frontend_mappings_ConvertModifier = Class(name="frontend::mappings::ConvertModifier")
frontend_mappings_DefaultValue = Class(name="frontend::mappings::DefaultValue", is_abstract=True)
frontend_mappings_IntDefaultValue = Class(name="frontend::mappings::IntDefaultValue")
DefaultValue = Class(name="DefaultValue")
frontend_mappings_MetamodelElementRef = Class(name="frontend::mappings::MetamodelElementRef", is_abstract=True)
frontend_mappings_ClassRef = Class(name="frontend::mappings::ClassRef")
MetamodelElementRef = Class(name="MetamodelElementRef")
frontend_qool_ModelElementQueue = Class(name="frontend::qool::ModelElementQueue")
frontend_qool_Segment = Class(name="frontend::qool::Segment")
frontend_qool_IteratorStatement = Class(name="frontend::qool::IteratorStatement")
core_Statement = Class(name="core::Statement")
frontend_qool_ForAllStatement = Class(name="frontend::qool::ForAllStatement")
IteratorStatement = Class(name="IteratorStatement")
frontend_qool_ForEachStatement = Class(name="frontend::qool::ForEachStatement")
frontend_qool_EmitStatement = Class(name="frontend::qool::EmitStatement")
frontend_qool_QoolQueue = Class(name="frontend::qool::QoolQueue", is_abstract=True)
QueueOptimization = Class(name="QueueOptimization")
frontend_qool_QueueOptimization = Class(name="frontend::qool::QueueOptimization", is_abstract=True)
frontend_qool_AccessByFeatureOptimization = Class(name="frontend::qool::AccessByFeatureOptimization")
frontend_qool_LocalQueue = Class(name="frontend::qool::LocalQueue")
TypeExpression = Class(name="TypeExpression")
frontend_qool_MatchPredicate = Class(name="frontend::qool::MatchPredicate", is_abstract=True)
frontend_qool_KindOfPredicate = Class(name="frontend::qool::KindOfPredicate")
frontend_qool_PropertyEqualsPredicate = Class(name="frontend::qool::PropertyEqualsPredicate")
frontend_qool_InvokeTransformation = Class(name="frontend::qool::InvokeTransformation", is_abstract=True)
InvocationParameter = Class(name="InvocationParameter")
NamedInvocationParameter = Class(name="NamedInvocationParameter")
frontend_qool_MatchExpression = Class(name="frontend::qool::MatchExpression")
MatchPredicate = Class(name="MatchPredicate")
frontend_facilities_Copier = Class(name="frontend::facilities::Copier")
facilities_CopierCallbackDefinition = Class(name="facilities::CopierCallbackDefinition")
frontend_facilities_CopierCallbackDefinition = Class(name="frontend::facilities::CopierCallbackDefinition")
frontend_tao_TaoTransformation = Class(name="frontend::tao::TaoTransformation")
Template = Class(name="Template")
frontend_tao_TemplateParameter = Class(name="frontend::tao::TemplateParameter")
frontend_tao_ObjectInstantiation = Class(name="frontend::tao::ObjectInstantiation")
frontend_qool_InvokeExternal = Class(name="frontend::qool::InvokeExternal")
InvokeTransformation = Class(name="InvokeTransformation")
frontend_qool_InvokeInternal = Class(name="frontend::qool::InvokeInternal")
frontend_qool_InvocationParameter = Class(name="frontend::qool::InvocationParameter")
TransformationDefinitionParameter = Class(name="TransformationDefinitionParameter")
frontend_qool_NamedInvocationParameter = Class(name="frontend::qool::NamedInvocationParameter")
frontend_tao_AttributeAssigment = Class(name="frontend::tao::AttributeAssigment")
SourceExpression = Class(name="SourceExpression")
frontend_tao_SourceExpression = Class(name="frontend::tao::SourceExpression", is_abstract=True)
frontend_tao_WithOptionalVariableExpression = Class(name="frontend::tao::WithOptionalVariableExpression")
ObjectSourceVariable = Class(name="ObjectSourceVariable")
frontend_tao_ObjectSourceVariable = Class(name="frontend::tao::ObjectSourceVariable")
frontend_tao_ReferenceAssignment = Class(name="frontend::tao::ReferenceAssignment", is_abstract=True)
tao_Assignment = Class(name="tao::Assignment")
frontend_tao_ObjectSyntax = Class(name="frontend::tao::ObjectSyntax")
ReferenceAssignment = Class(name="ReferenceAssignment")
frontend_tao_Invocation = Class(name="frontend::tao::Invocation")
Assignment = Class(name="Assignment")
frontend_tao_TemplateRootObject = Class(name="frontend::tao::TemplateRootObject")
ObjectInstantiation = Class(name="ObjectInstantiation")
frontend_tao_Template = Class(name="frontend::tao::Template")
TemplateParameter = Class(name="TemplateParameter")
TemplateRootObject = Class(name="TemplateRootObject")
frontend_tao_Assignment = Class(name="frontend::tao::Assignment", is_abstract=True)
frontend_core_ImplicitlyAnnotableElement = Class(name="frontend::core::ImplicitlyAnnotableElement")
SingleAnnotation = Class(name="SingleAnnotation")
frontend_core_Annotation = Class(name="frontend::core::Annotation", is_abstract=True)
AnnotableElement = Class(name="AnnotableElement")
frontend_core_OptimizationsAnnotation = Class(name="frontend::core::OptimizationsAnnotation")
frontend_core_MetamodelModelAnnotation = Class(name="frontend::core::MetamodelModelAnnotation")
frontend_core_SingleAnnotation = Class(name="frontend::core::SingleAnnotation", is_abstract=True)
frontend_core_PotencyAnnotation = Class(name="frontend::core::PotencyAnnotation")
frontend_core_GenericAnnotation = Class(name="frontend::core::GenericAnnotation")
AnnotationParameter = Class(name="AnnotationParameter")
frontend_core_AnnotationParameter = Class(name="frontend::core::AnnotationParameter", is_abstract=True)
frontend_core_RepresentModel = Class(name="frontend::core::RepresentModel", is_abstract=True)
frontend_core_TransformationDefinition = Class(name="frontend::core::TransformationDefinition", is_abstract=True)
ModuleDefinition = Class(name="ModuleDefinition")
frontend_core_LocatedElement = Class(name="frontend::core::LocatedElement", is_abstract=True)
frontend_core_NamedElement = Class(name="frontend::core::NamedElement", is_abstract=True)
frontend_core_DefinitionParameter = Class(name="frontend::core::DefinitionParameter", is_abstract=True)
frontend_core_ModuleParameter = Class(name="frontend::core::ModuleParameter")
DefinitionParameter = Class(name="DefinitionParameter")
frontend_core_ModuleDefinition = Class(name="frontend::core::ModuleDefinition", is_abstract=True)
core_AnnotableElement = Class(name="core::AnnotableElement")
frontend_core_AnnotableElement = Class(name="frontend::core::AnnotableElement", is_abstract=True)
Annotation = Class(name="Annotation")
RequireDeclaration = Class(name="RequireDeclaration")
frontend_core_EclecticTransformationDefinition = Class(name="frontend::core::EclecticTransformationDefinition")
frontend_core_TransformationDefinitionParameter = Class(name="frontend::core::TransformationDefinitionParameter")
core_DefinitionParameter = Class(name="core::DefinitionParameter")
frontend_core_ImportedModel = Class(name="frontend::core::ImportedModel")
frontend_core_UseDeclaration = Class(name="frontend::core::UseDeclaration")
frontend_core_RequireDeclaration = Class(name="frontend::core::RequireDeclaration")
ImportedModel = Class(name="ImportedModel")
InlineModel = Class(name="InlineModel")
frontend_core_Variable = Class(name="frontend::core::Variable", is_abstract=True)
frontend_core_Statement = Class(name="frontend::core::Statement", is_abstract=True)
frontend_core_Expression = Class(name="frontend::core::Expression", is_abstract=True)
frontend_core_DefineVariable = Class(name="frontend::core::DefineVariable")
frontend_core_PropertyWrite = Class(name="frontend::core::PropertyWrite")
RequireParameter = Class(name="RequireParameter")
frontend_core_RequireParameter = Class(name="frontend::core::RequireParameter", is_abstract=True)
frontend_core_RequireModelParameter = Class(name="frontend::core::RequireModelParameter")
core_Expression = Class(name="core::Expression")
frontend_core_VariableReference = Class(name="frontend::core::VariableReference")
frontend_core_MethodCall = Class(name="frontend::core::MethodCall")
frontend_core_ModelReference = Class(name="frontend::core::ModelReference")
KeywordParameter = Class(name="KeywordParameter")
frontend_core_KeywordParameter = Class(name="frontend::core::KeywordParameter")
frontend_core_BinaryExpr = Class(name="frontend::core::BinaryExpr")
frontend_core_KeywordMethodCall = Class(name="frontend::core::KeywordMethodCall")
ClosureParameter = Class(name="ClosureParameter")
frontend_core_ClosureParameter = Class(name="frontend::core::ClosureParameter")
frontend_core_ResolveLink = Class(name="frontend::core::ResolveLink")
frontend_core_ClosureDeclaration = Class(name="frontend::core::ClosureDeclaration")
frontend_core_IfExpr = Class(name="frontend::core::IfExpr")
IfBranch = Class(name="IfBranch")
frontend_core_IfBranch = Class(name="frontend::core::IfBranch")
frontend_core_NumLiteral = Class(name="frontend::core::NumLiteral")
frontend_core_DoubleLiteral = Class(name="frontend::core::DoubleLiteral")
frontend_core_StringLiteral = Class(name="frontend::core::StringLiteral")
frontend_core_BooleanLiteral = Class(name="frontend::core::BooleanLiteral")
TraceDefinition = Class(name="TraceDefinition")
frontend_core_TypedWithClass = Class(name="frontend::core::TypedWithClass", is_abstract=True)
frontend_core_TraceInterface = Class(name="frontend::core::TraceInterface")
frontend_core_TracedModelParameter = Class(name="frontend::core::TracedModelParameter")
frontend_core_TraceDefinition = Class(name="frontend::core::TraceDefinition")
TraceElement = Class(name="TraceElement")
frontend_core_TypeExpression = Class(name="frontend::core::TypeExpression", is_abstract=True)
frontend_core_TraceElement = Class(name="frontend::core::TraceElement")
frontend_core_ClassUse = Class(name="frontend::core::ClassUse")
core_TypeExpression = Class(name="core::TypeExpression")
core_ImplicitlyAnnotableElement = Class(name="core::ImplicitlyAnnotableElement")
frontend_core_InlineModel = Class(name="frontend::core::InlineModel")
core_ModuleDefinition = Class(name="core::ModuleDefinition")
InlineClass = Class(name="InlineClass")
frontend_core_TraceUse = Class(name="frontend::core::TraceUse")
frontend_core_InlineFeature = Class(name="frontend::core::InlineFeature")
frontend_core_InlineAttribute = Class(name="frontend::core::InlineAttribute")
frontend_core_InlineReference = Class(name="frontend::core::InlineReference")
frontend_core_MatchTrace = Class(name="frontend::core::MatchTrace")
TraceCompareExpression = Class(name="TraceCompareExpression")
frontend_core_TraceCompareExpression = Class(name="frontend::core::TraceCompareExpression")
frontend_core_PutTrace = Class(name="frontend::core::PutTrace")
frontend_core_InlineClass = Class(name="frontend::core::InlineClass")
InlineFeature = Class(name="InlineFeature")
PutTraceParameter = Class(name="PutTraceParameter")
frontend_core_PutTraceParameter = Class(name="frontend::core::PutTraceParameter")

# frontend_script_ScriptedTransformation class attributes and methods

# TransformationDefinition class attributes and methods

# Statement class attributes and methods

# frontend_koan_KoanTransformation class attributes and methods

# TraceInterface class attributes and methods

# KoanRule class attributes and methods

# frontend_koan_KoanRule class attributes and methods

# core_LocatedElement class attributes and methods

# core_NamedElement class attributes and methods

# Matcher class attributes and methods

# frontend_koan_Matcher class attributes and methods

# LocatedElement class attributes and methods

# frontend_koan_ForAllMatcher class attributes and methods

# koan_Matcher class attributes and methods

# frontend_DummyRootMetaclass class attributes and methods

# frontend_attribution_AttributionTransformation class attributes and methods

# AttributeDcl class attributes and methods

# AttributionRule class attributes and methods

# frontend_attribution_AttributeDcl class attributes and methods

# core_TypedWithClass class attributes and methods

# frontend_attribution_InheritedAttributeDcl class attributes and methods

# core_Variable class attributes and methods

# ClassUse class attributes and methods

# frontend_attribution_RuleSelf class attributes and methods

# Variable class attributes and methods

# frontend_attribution_AttributeInit class attributes and methods

# frontend_attribution_AttributeUse class attributes and methods

# frontend_attribution_SynthesizedAttributeDcl class attributes and methods

# frontend_attribution_AttributionRule class attributes and methods

# RuleSelf class attributes and methods

# Expression class attributes and methods

# MethodParameter class attributes and methods

# MethodSelf class attributes and methods

# frontend_imperative_MethodSelf class attributes and methods

# frontend_imperative_MethodParameter class attributes and methods

# frontend_chain_ChainTransformation class attributes and methods

# frontend_imperative_ImperativeTransformation class attributes and methods

# MethodDefinition class attributes and methods

# frontend_chain_GeneratedModel class attributes and methods

# frontend_imperative_MethodDefinition class attributes and methods
frontend_imperative_MethodDefinition_name: Property = Property(name="name", type=StringType)
frontend_imperative_MethodDefinition.attributes={frontend_imperative_MethodDefinition_name}

# core_RepresentModel class attributes and methods

# frontend_chain_TransformationExecution class attributes and methods

# AvailableTransformation class attributes and methods

# RepresentModel class attributes and methods

# frontend_chain_AvailableTransformation class attributes and methods

# frontend_chain_ExternalTransformation class attributes and methods

# chain_AvailableTransformation class attributes and methods

# frontend_chain_CompositeTransformation class attributes and methods

# core_TransformationDefinition class attributes and methods

# CompositeTransformation class attributes and methods

# ExternalTransformation class attributes and methods

# GeneratedModel class attributes and methods

# TransformationExecution class attributes and methods

# POutputVariable class attributes and methods

# frontend_patterns_POutputVariable class attributes and methods

# frontend_patterns_PObject class attributes and methods

# PFeature class attributes and methods

# frontend_patterns_PFeature class attributes and methods
frontend_patterns_PFeature_name: Property = Property(name="name", type=StringType)
frontend_patterns_PFeature.attributes={frontend_patterns_PFeature_name}

# frontend_patterns_PatternSpecification class attributes and methods

# Pattern class attributes and methods

# frontend_patterns_Pattern class attributes and methods
frontend_patterns_Pattern_name: Property = Property(name="name", type=StringType)
frontend_patterns_Pattern.attributes={frontend_patterns_Pattern_name}

# PObject class attributes and methods

# frontend_patterns_CollectionReference class attributes and methods

# PReference class attributes and methods

# frontend_mappings_MappingTransformation class attributes and methods

# Delegate class attributes and methods

# Context class attributes and methods

# frontend_mappings_MappingVariable class attributes and methods

# frontend_mappings_MatchedElement class attributes and methods

# core_ClassUse class attributes and methods

# mappings_MappingVariable class attributes and methods

# frontend_mappings_Delegate class attributes and methods
frontend_mappings_Delegate_linkName: Property = Property(name="linkName", type=StringType)
frontend_mappings_Delegate_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_Delegate_isExternal: Property = Property(name="isExternal", type=StringType)
frontend_mappings_Delegate.attributes={frontend_mappings_Delegate_isExternal, frontend_mappings_Delegate_featureName, frontend_mappings_Delegate_linkName}

# frontend_patterns_PAttribute class attributes and methods

# UseDeclaration class attributes and methods

# frontend_patterns_PReference class attributes and methods

# Tag class attributes and methods

# frontend_mappings_Context class attributes and methods

# MappingElement class attributes and methods

# C2CModifier class attributes and methods

# MatchedElement class attributes and methods

# frontend_mappings_MappingElement class attributes and methods

# frontend_mappings_ClassMapping class attributes and methods

# frontend_mappings_Feature2Feature class attributes and methods

# FeatureRef class attributes and methods

# Converter class attributes and methods

# frontend_mappings_AttributeMapping class attributes and methods

# Feature2Feature class attributes and methods

# Section class attributes and methods

# frontend_mappings_Section class attributes and methods
frontend_mappings_Section_sectionType: Property = Property(name="sectionType", type=StringType)
frontend_mappings_Section.attributes={frontend_mappings_Section_sectionType}

# frontend_mappings_AttributeIsInteger class attributes and methods
frontend_mappings_AttributeIsInteger_intValue: Property = Property(name="intValue", type=IntegerType)
frontend_mappings_AttributeIsInteger.attributes={frontend_mappings_AttributeIsInteger_intValue}

# frontend_mappings_Converter class attributes and methods
frontend_mappings_Converter_isExternal: Property = Property(name="isExternal", type=StringType)
frontend_mappings_Converter_converterName: Property = Property(name="converterName", type=StringType)
frontend_mappings_Converter.attributes={frontend_mappings_Converter_isExternal, frontend_mappings_Converter_converterName}

# frontend_mappings_Tag class attributes and methods

# NamedElement class attributes and methods

# frontend_mappings_Class2Class class attributes and methods
frontend_mappings_Class2Class_cardinality: Property = Property(name="cardinality", type=StringType)
frontend_mappings_Class2Class.attributes={frontend_mappings_Class2Class_cardinality}

# ClassMapping class attributes and methods

# ClassRef class attributes and methods

# Attribute2Attribute class attributes and methods

# frontend_mappings_C2CModifier class attributes and methods

# frontend_mappings_RelatedBy class attributes and methods

# AttributeRef class attributes and methods

# AttributeRightPart class attributes and methods

# frontend_mappings_AttributeRightPart class attributes and methods

# frontend_mappings_AttributeIsString class attributes and methods
frontend_mappings_AttributeIsString_strValue: Property = Property(name="strValue", type=StringType)
frontend_mappings_AttributeIsString.attributes={frontend_mappings_AttributeIsString_strValue}

# frontend_mappings_AttributeIsBoolean class attributes and methods
frontend_mappings_AttributeIsBoolean_boolValue: Property = Property(name="boolValue", type=StringType)
frontend_mappings_AttributeIsBoolean.attributes={frontend_mappings_AttributeIsBoolean_boolValue}

# frontend_mappings_AttributeIsDouble class attributes and methods
frontend_mappings_AttributeIsDouble_doubleValue: Property = Property(name="doubleValue", type=StringType)
frontend_mappings_AttributeIsDouble.attributes={frontend_mappings_AttributeIsDouble_doubleValue}

# frontend_mappings_AttributeIsResolveLink class attributes and methods

# ResolveLink class attributes and methods

# frontend_mappings_Join class attributes and methods

# frontend_mappings_Attribute2Attribute class attributes and methods
frontend_mappings_Attribute2Attribute_cardinality: Property = Property(name="cardinality", type=StringType)
frontend_mappings_Attribute2Attribute.attributes={frontend_mappings_Attribute2Attribute_cardinality}

# mappings_Feature2Feature class attributes and methods

# mappings_AttributeRightPart class attributes and methods

# Class2Class class attributes and methods

# AttributeModifier class attributes and methods

# frontend_mappings_Reference2Reference class attributes and methods
frontend_mappings_Reference2Reference_cardinality: Property = Property(name="cardinality", type=StringType)
frontend_mappings_Reference2Reference_resolverName: Property = Property(name="resolverName", type=StringType)
frontend_mappings_Reference2Reference.attributes={frontend_mappings_Reference2Reference_resolverName, frontend_mappings_Reference2Reference_cardinality}

# ReferenceRef class attributes and methods

# frontend_mappings_Modifier class attributes and methods

# frontend_mappings_AttributeModifier class attributes and methods

# Modifier class attributes and methods

# frontend_mappings_LinkedBy class attributes and methods

# frontend_mappings_EqualityFilter class attributes and methods
frontend_mappings_EqualityFilter_filter: Property = Property(name="filter", type=StringType)
frontend_mappings_EqualityFilter.attributes={frontend_mappings_EqualityFilter_filter}

# frontend_mappings_Operator class attributes and methods

# frontend_mappings_Split class attributes and methods

# Operator class attributes and methods

# frontend_mappings_FeatureRef class attributes and methods
frontend_mappings_FeatureRef_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_FeatureRef_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_mappings_FeatureRef.attributes={frontend_mappings_FeatureRef_multivalued, frontend_mappings_FeatureRef_featureName}

# mappings_MetamodelElementRef class attributes and methods

# frontend_mappings_AttributeRef class attributes and methods
frontend_mappings_AttributeRef_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_AttributeRef_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_mappings_AttributeRef.attributes={frontend_mappings_AttributeRef_multivalued, frontend_mappings_AttributeRef_featureName}

# frontend_mappings_ReferenceRef class attributes and methods
frontend_mappings_ReferenceRef_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_ReferenceRef_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_mappings_ReferenceRef.attributes={frontend_mappings_ReferenceRef_featureName, frontend_mappings_ReferenceRef_multivalued}

# frontend_qool_QoolTransformation class attributes and methods

# QoolQueue class attributes and methods

# Segment class attributes and methods

# frontend_mappings_ConvertModifier class attributes and methods
frontend_mappings_ConvertModifier_converter: Property = Property(name="converter", type=StringType)
frontend_mappings_ConvertModifier.attributes={frontend_mappings_ConvertModifier_converter}

# frontend_mappings_DefaultValue class attributes and methods

# frontend_mappings_IntDefaultValue class attributes and methods
frontend_mappings_IntDefaultValue_defaultValue: Property = Property(name="defaultValue", type=StringType)
frontend_mappings_IntDefaultValue.attributes={frontend_mappings_IntDefaultValue_defaultValue}

# DefaultValue class attributes and methods

# frontend_mappings_MetamodelElementRef class attributes and methods

# frontend_mappings_ClassRef class attributes and methods

# MetamodelElementRef class attributes and methods

# frontend_qool_ModelElementQueue class attributes and methods

# frontend_qool_Segment class attributes and methods

# frontend_qool_IteratorStatement class attributes and methods

# core_Statement class attributes and methods

# frontend_qool_ForAllStatement class attributes and methods

# IteratorStatement class attributes and methods

# frontend_qool_ForEachStatement class attributes and methods

# frontend_qool_EmitStatement class attributes and methods

# frontend_qool_QoolQueue class attributes and methods

# QueueOptimization class attributes and methods

# frontend_qool_QueueOptimization class attributes and methods

# frontend_qool_AccessByFeatureOptimization class attributes and methods
frontend_qool_AccessByFeatureOptimization_featureName: Property = Property(name="featureName", type=StringType)
frontend_qool_AccessByFeatureOptimization_force: Property = Property(name="force", type=BooleanType)
frontend_qool_AccessByFeatureOptimization.attributes={frontend_qool_AccessByFeatureOptimization_force, frontend_qool_AccessByFeatureOptimization_featureName}

# frontend_qool_LocalQueue class attributes and methods

# TypeExpression class attributes and methods

# frontend_qool_MatchPredicate class attributes and methods

# frontend_qool_KindOfPredicate class attributes and methods

# frontend_qool_PropertyEqualsPredicate class attributes and methods
frontend_qool_PropertyEqualsPredicate_propertyName: Property = Property(name="propertyName", type=StringType)
frontend_qool_PropertyEqualsPredicate.attributes={frontend_qool_PropertyEqualsPredicate_propertyName}

# frontend_qool_InvokeTransformation class attributes and methods
frontend_qool_InvokeTransformation_transformationName: Property = Property(name="transformationName", type=StringType)
frontend_qool_InvokeTransformation_entryPointName: Property = Property(name="entryPointName", type=StringType)
frontend_qool_InvokeTransformation.attributes={frontend_qool_InvokeTransformation_transformationName, frontend_qool_InvokeTransformation_entryPointName}

# InvocationParameter class attributes and methods

# NamedInvocationParameter class attributes and methods

# frontend_qool_MatchExpression class attributes and methods

# MatchPredicate class attributes and methods

# frontend_facilities_Copier class attributes and methods

# facilities_CopierCallbackDefinition class attributes and methods

# frontend_facilities_CopierCallbackDefinition class attributes and methods
frontend_facilities_CopierCallbackDefinition_stop: Property = Property(name="stop", type=BooleanType)
frontend_facilities_CopierCallbackDefinition.attributes={frontend_facilities_CopierCallbackDefinition_stop}

# frontend_tao_TaoTransformation class attributes and methods

# Template class attributes and methods

# frontend_tao_TemplateParameter class attributes and methods

# frontend_tao_ObjectInstantiation class attributes and methods

# frontend_qool_InvokeExternal class attributes and methods
frontend_qool_InvokeExternal_queueName: Property = Property(name="queueName", type=StringType)
frontend_qool_InvokeExternal_traceAttributeName: Property = Property(name="traceAttributeName", type=StringType)
frontend_qool_InvokeExternal.attributes={frontend_qool_InvokeExternal_queueName, frontend_qool_InvokeExternal_traceAttributeName}

# InvokeTransformation class attributes and methods

# frontend_qool_InvokeInternal class attributes and methods

# frontend_qool_InvocationParameter class attributes and methods
frontend_qool_InvocationParameter_calleeModelName: Property = Property(name="calleeModelName", type=StringType)
frontend_qool_InvocationParameter.attributes={frontend_qool_InvocationParameter_calleeModelName}

# TransformationDefinitionParameter class attributes and methods

# frontend_qool_NamedInvocationParameter class attributes and methods
frontend_qool_NamedInvocationParameter_formalName: Property = Property(name="formalName", type=StringType)
frontend_qool_NamedInvocationParameter.attributes={frontend_qool_NamedInvocationParameter_formalName}

# frontend_tao_AttributeAssigment class attributes and methods
frontend_tao_AttributeAssigment_targetFeature: Property = Property(name="targetFeature", type=StringType)
frontend_tao_AttributeAssigment.attributes={frontend_tao_AttributeAssigment_targetFeature}

# SourceExpression class attributes and methods

# frontend_tao_SourceExpression class attributes and methods

# frontend_tao_WithOptionalVariableExpression class attributes and methods

# ObjectSourceVariable class attributes and methods

# frontend_tao_ObjectSourceVariable class attributes and methods

# frontend_tao_ReferenceAssignment class attributes and methods
frontend_tao_ReferenceAssignment_targetFeature: Property = Property(name="targetFeature", type=StringType)
frontend_tao_ReferenceAssignment_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_tao_ReferenceAssignment.attributes={frontend_tao_ReferenceAssignment_targetFeature, frontend_tao_ReferenceAssignment_multivalued}

# tao_Assignment class attributes and methods

# frontend_tao_ObjectSyntax class attributes and methods

# ReferenceAssignment class attributes and methods

# frontend_tao_Invocation class attributes and methods

# Assignment class attributes and methods

# frontend_tao_TemplateRootObject class attributes and methods

# ObjectInstantiation class attributes and methods

# frontend_tao_Template class attributes and methods

# TemplateParameter class attributes and methods

# TemplateRootObject class attributes and methods

# frontend_tao_Assignment class attributes and methods

# frontend_core_ImplicitlyAnnotableElement class attributes and methods

# SingleAnnotation class attributes and methods

# frontend_core_Annotation class attributes and methods

# AnnotableElement class attributes and methods

# frontend_core_OptimizationsAnnotation class attributes and methods
frontend_core_OptimizationsAnnotation_enabled: Property = Property(name="enabled", type=BooleanType)
frontend_core_OptimizationsAnnotation.attributes={frontend_core_OptimizationsAnnotation_enabled}

# frontend_core_MetamodelModelAnnotation class attributes and methods
frontend_core_MetamodelModelAnnotation_metamodel: Property = Property(name="metamodel", type=StringType)
frontend_core_MetamodelModelAnnotation.attributes={frontend_core_MetamodelModelAnnotation_metamodel}

# frontend_core_SingleAnnotation class attributes and methods

# frontend_core_PotencyAnnotation class attributes and methods
frontend_core_PotencyAnnotation_value: Property = Property(name="value", type=StringType)
frontend_core_PotencyAnnotation.attributes={frontend_core_PotencyAnnotation_value}

# frontend_core_GenericAnnotation class attributes and methods
frontend_core_GenericAnnotation_name: Property = Property(name="name", type=StringType)
frontend_core_GenericAnnotation.attributes={frontend_core_GenericAnnotation_name}

# AnnotationParameter class attributes and methods

# frontend_core_AnnotationParameter class attributes and methods

# frontend_core_RepresentModel class attributes and methods

# frontend_core_TransformationDefinition class attributes and methods

# ModuleDefinition class attributes and methods

# frontend_core_LocatedElement class attributes and methods
frontend_core_LocatedElement_row: Property = Property(name="row", type=IntegerType)
frontend_core_LocatedElement_column: Property = Property(name="column", type=IntegerType)
frontend_core_LocatedElement_file: Property = Property(name="file", type=StringType)
frontend_core_LocatedElement.attributes={frontend_core_LocatedElement_column, frontend_core_LocatedElement_file, frontend_core_LocatedElement_row}

# frontend_core_NamedElement class attributes and methods
frontend_core_NamedElement_name: Property = Property(name="name", type=StringType)
frontend_core_NamedElement.attributes={frontend_core_NamedElement_name}

# frontend_core_DefinitionParameter class attributes and methods

# frontend_core_ModuleParameter class attributes and methods

# DefinitionParameter class attributes and methods

# frontend_core_ModuleDefinition class attributes and methods

# core_AnnotableElement class attributes and methods

# frontend_core_AnnotableElement class attributes and methods

# Annotation class attributes and methods

# RequireDeclaration class attributes and methods

# frontend_core_EclecticTransformationDefinition class attributes and methods

# frontend_core_TransformationDefinitionParameter class attributes and methods

# core_DefinitionParameter class attributes and methods

# frontend_core_ImportedModel class attributes and methods

# frontend_core_UseDeclaration class attributes and methods
frontend_core_UseDeclaration_module: Property = Property(name="module", type=StringType)
frontend_core_UseDeclaration_as: Property = Property(name="as", type=StringType)
frontend_core_UseDeclaration.attributes={frontend_core_UseDeclaration_module, frontend_core_UseDeclaration_as}

# frontend_core_RequireDeclaration class attributes and methods
frontend_core_RequireDeclaration_name: Property = Property(name="name", type=StringType)
frontend_core_RequireDeclaration_default: Property = Property(name="default", type=StringType)
frontend_core_RequireDeclaration.attributes={frontend_core_RequireDeclaration_default, frontend_core_RequireDeclaration_name}

# ImportedModel class attributes and methods

# InlineModel class attributes and methods

# frontend_core_Variable class attributes and methods
frontend_core_Variable_name: Property = Property(name="name", type=StringType)
frontend_core_Variable.attributes={frontend_core_Variable_name}

# frontend_core_Statement class attributes and methods

# frontend_core_Expression class attributes and methods

# frontend_core_DefineVariable class attributes and methods

# frontend_core_PropertyWrite class attributes and methods
frontend_core_PropertyWrite_property: Property = Property(name="property", type=StringType)
frontend_core_PropertyWrite.attributes={frontend_core_PropertyWrite_property}

# RequireParameter class attributes and methods

# frontend_core_RequireParameter class attributes and methods
frontend_core_RequireParameter_formalParameterName: Property = Property(name="formalParameterName", type=StringType)
frontend_core_RequireParameter.attributes={frontend_core_RequireParameter_formalParameterName}

# frontend_core_RequireModelParameter class attributes and methods

# core_Expression class attributes and methods

# frontend_core_VariableReference class attributes and methods

# frontend_core_MethodCall class attributes and methods
frontend_core_MethodCall_methodName: Property = Property(name="methodName", type=StringType)
frontend_core_MethodCall_withParameters: Property = Property(name="withParameters", type=BooleanType)
frontend_core_MethodCall.attributes={frontend_core_MethodCall_withParameters, frontend_core_MethodCall_methodName}

# frontend_core_ModelReference class attributes and methods

# KeywordParameter class attributes and methods

# frontend_core_KeywordParameter class attributes and methods
frontend_core_KeywordParameter_keyword: Property = Property(name="keyword", type=StringType)
frontend_core_KeywordParameter.attributes={frontend_core_KeywordParameter_keyword}

# frontend_core_BinaryExpr class attributes and methods
frontend_core_BinaryExpr_binaryOp: Property = Property(name="binaryOp", type=StringType)
frontend_core_BinaryExpr.attributes={frontend_core_BinaryExpr_binaryOp}

# frontend_core_KeywordMethodCall class attributes and methods

# ClosureParameter class attributes and methods

# frontend_core_ClosureParameter class attributes and methods

# frontend_core_ResolveLink class attributes and methods
frontend_core_ResolveLink_isExternal: Property = Property(name="isExternal", type=StringType)
frontend_core_ResolveLink_linkName: Property = Property(name="linkName", type=StringType)
frontend_core_ResolveLink_featureName: Property = Property(name="featureName", type=StringType)
frontend_core_ResolveLink.attributes={frontend_core_ResolveLink_isExternal, frontend_core_ResolveLink_featureName, frontend_core_ResolveLink_linkName}

# frontend_core_ClosureDeclaration class attributes and methods

# frontend_core_IfExpr class attributes and methods

# IfBranch class attributes and methods

# frontend_core_IfBranch class attributes and methods

# frontend_core_NumLiteral class attributes and methods
frontend_core_NumLiteral_value: Property = Property(name="value", type=IntegerType)
frontend_core_NumLiteral.attributes={frontend_core_NumLiteral_value}

# frontend_core_DoubleLiteral class attributes and methods
frontend_core_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
frontend_core_DoubleLiteral.attributes={frontend_core_DoubleLiteral_value}

# frontend_core_StringLiteral class attributes and methods
frontend_core_StringLiteral_value: Property = Property(name="value", type=StringType)
frontend_core_StringLiteral.attributes={frontend_core_StringLiteral_value}

# frontend_core_BooleanLiteral class attributes and methods
frontend_core_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
frontend_core_BooleanLiteral.attributes={frontend_core_BooleanLiteral_value}

# TraceDefinition class attributes and methods

# frontend_core_TypedWithClass class attributes and methods

# frontend_core_TraceInterface class attributes and methods

# frontend_core_TracedModelParameter class attributes and methods

# frontend_core_TraceDefinition class attributes and methods

# TraceElement class attributes and methods

# frontend_core_TypeExpression class attributes and methods

# frontend_core_TraceElement class attributes and methods

# frontend_core_ClassUse class attributes and methods
frontend_core_ClassUse_className: Property = Property(name="className", type=StringType)
frontend_core_ClassUse_strictType: Property = Property(name="strictType", type=BooleanType)
frontend_core_ClassUse.attributes={frontend_core_ClassUse_strictType, frontend_core_ClassUse_className}

# core_TypeExpression class attributes and methods

# core_ImplicitlyAnnotableElement class attributes and methods

# frontend_core_InlineModel class attributes and methods

# core_ModuleDefinition class attributes and methods

# InlineClass class attributes and methods

# frontend_core_TraceUse class attributes and methods

# frontend_core_InlineFeature class attributes and methods
frontend_core_InlineFeature_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_core_InlineFeature.attributes={frontend_core_InlineFeature_multivalued}

# frontend_core_InlineAttribute class attributes and methods

# frontend_core_InlineReference class attributes and methods

# frontend_core_MatchTrace class attributes and methods
frontend_core_MatchTrace_cardinality: Property = Property(name="cardinality", type=StringType)
frontend_core_MatchTrace.attributes={frontend_core_MatchTrace_cardinality}

# TraceCompareExpression class attributes and methods

# frontend_core_TraceCompareExpression class attributes and methods
frontend_core_TraceCompareExpression_multivaluedTag: Property = Property(name="multivaluedTag", type=BooleanType)
frontend_core_TraceCompareExpression.attributes={frontend_core_TraceCompareExpression_multivaluedTag}

# frontend_core_PutTrace class attributes and methods

# frontend_core_InlineClass class attributes and methods

# InlineFeature class attributes and methods

# PutTraceParameter class attributes and methods

# frontend_core_PutTraceParameter class attributes and methods

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="Statement", type=frontend_script_ScriptedTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_script_ScriptedTransformation", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceInterface1: BinaryAssociation = BinaryAssociation(
    name="traceInterface1",
    ends={
        Property(name="TraceInterface", type=frontend_koan_KoanTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_koan_KoanTransformation", type=TraceInterface, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rules2: BinaryAssociation = BinaryAssociation(
    name="rules2",
    ends={
        Property(name="KoanRule", type=frontend_koan_KoanTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_koan_KoanTransformation3", type=KoanRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matcher4: BinaryAssociation = BinaryAssociation(
    name="matcher4",
    ends={
        Property(name="Matcher", type=frontend_koan_KoanRule, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_koan_KoanRule", type=Matcher, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements5: BinaryAssociation = BinaryAssociation(
    name="statements5",
    ends={
        Property(name="Statement7", type=frontend_koan_KoanRule, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_koan_KoanRule6", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child8: BinaryAssociation = BinaryAssociation(
    name="child8",
    ends={
        Property(name="Matcher9", type=frontend_koan_Matcher, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_koan_Matcher", type=Matcher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes11: BinaryAssociation = BinaryAssociation(
    name="attributes11",
    ends={
        Property(name="AttributeDcl", type=frontend_attribution_AttributionTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributionTransformation", type=AttributeDcl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules12: BinaryAssociation = BinaryAssociation(
    name="rules12",
    ends={
        Property(name="AttributionRule", type=frontend_attribution_AttributionTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributionTransformation13", type=AttributionRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="ClassUse", type=frontend_koan_ForAllMatcher, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_koan_ForAllMatcher", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition18: BinaryAssociation = BinaryAssociation(
    name="condition18",
    ends={
        Property(name="frontend_attribution_AttributionRule19", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Expression", type=frontend_attribution_AttributionRule, multiplicity=Multiplicity(1, 1))
    }
)
statements20: BinaryAssociation = BinaryAssociation(
    name="statements20",
    ends={
        Property(name="Statement22", type=frontend_attribution_AttributionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributionRule21", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute23: BinaryAssociation = BinaryAssociation(
    name="attribute23",
    ends={
        Property(name="AttributeDcl24", type=frontend_attribution_AttributeInit, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributeInit", type=AttributeDcl, multiplicity=Multiplicity(1, 1))
    }
)
receptor25: BinaryAssociation = BinaryAssociation(
    name="receptor25",
    ends={
        Property(name="Expression27", type=frontend_attribution_AttributeInit, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributeInit26", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="Expression30", type=frontend_attribution_AttributeInit, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributeInit29", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr31: BinaryAssociation = BinaryAssociation(
    name="expr31",
    ends={
        Property(name="Expression32", type=frontend_attribution_AttributeUse, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributeUse", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="ClassUse15", type=frontend_attribution_AttributionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributionRule", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
self16: BinaryAssociation = BinaryAssociation(
    name="self16",
    ends={
        Property(name="RuleSelf", type=frontend_attribution_AttributionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributionRule17", type=RuleSelf, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
formalParameters37: BinaryAssociation = BinaryAssociation(
    name="formalParameters37",
    ends={
        Property(name="MethodParameter", type=frontend_imperative_MethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_imperative_MethodDefinition", type=MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self38: BinaryAssociation = BinaryAssociation(
    name="self38",
    ends={
        Property(name="MethodSelf", type=frontend_imperative_MethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_imperative_MethodDefinition39", type=MethodSelf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type40: BinaryAssociation = BinaryAssociation(
    name="type40",
    ends={
        Property(name="ClassUse42", type=frontend_imperative_MethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_imperative_MethodDefinition41", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements43: BinaryAssociation = BinaryAssociation(
    name="statements43",
    ends={
        Property(name="Statement45", type=frontend_imperative_MethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_imperative_MethodDefinition44", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute33: BinaryAssociation = BinaryAssociation(
    name="attribute33",
    ends={
        Property(name="AttributeDcl35", type=frontend_attribution_AttributeUse, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributeUse34", type=AttributeDcl, multiplicity=Multiplicity(1, 1))
    }
)
methods36: BinaryAssociation = BinaryAssociation(
    name="methods36",
    ends={
        Property(name="MethodDefinition", type=frontend_imperative_ImperativeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_imperative_ImperativeTransformation", type=MethodDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation53: BinaryAssociation = BinaryAssociation(
    name="transformation53",
    ends={
        Property(name="AvailableTransformation", type=frontend_chain_TransformationExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_TransformationExecution", type=AvailableTransformation, multiplicity=Multiplicity(1, 1))
    }
)
inputModels54: BinaryAssociation = BinaryAssociation(
    name="inputModels54",
    ends={
        Property(name="RepresentModel", type=frontend_chain_TransformationExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_TransformationExecution55", type=RepresentModel, multiplicity=Multiplicity(0, 9999))
    }
)
outputModels56: BinaryAssociation = BinaryAssociation(
    name="outputModels56",
    ends={
        Property(name="RepresentModel58", type=frontend_chain_TransformationExecution, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_TransformationExecution57", type=RepresentModel, multiplicity=Multiplicity(0, 9999))
    }
)
composites46: BinaryAssociation = BinaryAssociation(
    name="composites46",
    ends={
        Property(name="CompositeTransformation", type=frontend_chain_ChainTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_ChainTransformation", type=CompositeTransformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externals47: BinaryAssociation = BinaryAssociation(
    name="externals47",
    ends={
        Property(name="ExternalTransformation", type=frontend_chain_ChainTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_ChainTransformation48", type=ExternalTransformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generatedModels49: BinaryAssociation = BinaryAssociation(
    name="generatedModels49",
    ends={
        Property(name="GeneratedModel", type=frontend_chain_ChainTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_ChainTransformation50", type=GeneratedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects62: BinaryAssociation = BinaryAssociation(
    name="objects62",
    ends={
        Property(name="PObject", type=frontend_patterns_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_Pattern", type=PObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executions51: BinaryAssociation = BinaryAssociation(
    name="executions51",
    ends={
        Property(name="TransformationExecution", type=frontend_chain_ChainTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_ChainTransformation52", type=TransformationExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputVariables63: BinaryAssociation = BinaryAssociation(
    name="outputVariables63",
    ends={
        Property(name="POutputVariable", type=frontend_patterns_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_Pattern64", type=POutputVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object65: BinaryAssociation = BinaryAssociation(
    name="object65",
    ends={
        Property(name="PObject66", type=frontend_patterns_POutputVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_POutputVariable", type=PObject, multiplicity=Multiplicity(1, 1))
    }
)
type67: BinaryAssociation = BinaryAssociation(
    name="type67",
    ends={
        Property(name="ClassUse68", type=frontend_patterns_PObject, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_PObject", type=ClassUse, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
features69: BinaryAssociation = BinaryAssociation(
    name="features69",
    ends={
        Property(name="PFeature", type=frontend_patterns_PObject, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_PObject70", type=PFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executions59: BinaryAssociation = BinaryAssociation(
    name="executions59",
    ends={
        Property(name="TransformationExecution60", type=frontend_chain_CompositeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_CompositeTransformation", type=TransformationExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
patterns61: BinaryAssociation = BinaryAssociation(
    name="patterns61",
    ends={
        Property(name="Pattern", type=frontend_patterns_PatternSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_PatternSpecification", type=Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value75: BinaryAssociation = BinaryAssociation(
    name="value75",
    ends={
        Property(name="PObject76", type=frontend_patterns_PReference, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_PReference", type=PObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegates77: BinaryAssociation = BinaryAssociation(
    name="delegates77",
    ends={
        Property(name="Delegate", type=frontend_mappings_MappingTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_MappingTransformation", type=Delegate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contexts78: BinaryAssociation = BinaryAssociation(
    name="contexts78",
    ends={
        Property(name="Context", type=frontend_mappings_MappingTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_MappingTransformation79", type=Context, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="Expression72", type=frontend_patterns_PAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_PAttribute", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable73: BinaryAssociation = BinaryAssociation(
    name="variable73",
    ends={
        Property(name="Variable", type=frontend_patterns_PAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_PAttribute74", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
module81: BinaryAssociation = BinaryAssociation(
    name="module81",
    ends={
        Property(name="UseDeclaration", type=frontend_mappings_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Delegate82", type=UseDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
tags83: BinaryAssociation = BinaryAssociation(
    name="tags83",
    ends={
        Property(name="Tag", type=frontend_mappings_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Delegate84", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left85: BinaryAssociation = BinaryAssociation(
    name="left85",
    ends={
        Property(name="MatchedElement86", type=frontend_mappings_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Context", type=MatchedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right87: BinaryAssociation = BinaryAssociation(
    name="right87",
    ends={
        Property(name="MatchedElement89", type=frontend_mappings_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Context88", type=MatchedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings90: BinaryAssociation = BinaryAssociation(
    name="mappings90",
    ends={
        Property(name="MappingElement", type=frontend_mappings_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Context91", type=MappingElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="MatchedElement", type=frontend_mappings_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Delegate", type=MatchedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings99: BinaryAssociation = BinaryAssociation(
    name="mappings99",
    ends={
        Property(name="MappingElement100", type=frontend_mappings_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Section", type=MappingElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftFeature101: BinaryAssociation = BinaryAssociation(
    name="leftFeature101",
    ends={
        Property(name="FeatureRef", type=frontend_mappings_Feature2Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Feature2Feature", type=FeatureRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
converter102: BinaryAssociation = BinaryAssociation(
    name="converter102",
    ends={
        Property(name="Converter", type=frontend_mappings_Feature2Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Feature2Feature103", type=Converter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modifiers92: BinaryAssociation = BinaryAssociation(
    name="modifiers92",
    ends={
        Property(name="C2CModifier", type=frontend_mappings_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Context93", type=C2CModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections94: BinaryAssociation = BinaryAssociation(
    name="sections94",
    ends={
        Property(name="Section", type=frontend_mappings_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Context95", type=Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags96: BinaryAssociation = BinaryAssociation(
    name="tags96",
    ends={
        Property(name="Tag98", type=frontend_mappings_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Context97", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module108: BinaryAssociation = BinaryAssociation(
    name="module108",
    ends={
        Property(name="UseDeclaration109", type=frontend_mappings_Converter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Converter", type=UseDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
modifiers110: BinaryAssociation = BinaryAssociation(
    name="modifiers110",
    ends={
        Property(name="C2CModifier111", type=frontend_mappings_Class2Class, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Class2Class", type=C2CModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left112: BinaryAssociation = BinaryAssociation(
    name="left112",
    ends={
        Property(name="ClassRef", type=frontend_mappings_Class2Class, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Class2Class113", type=ClassRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
right114: BinaryAssociation = BinaryAssociation(
    name="right114",
    ends={
        Property(name="ClassRef116", type=frontend_mappings_Class2Class, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Class2Class115", type=ClassRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
scopedAttributes117: BinaryAssociation = BinaryAssociation(
    name="scopedAttributes117",
    ends={
        Property(name="mappings", type=frontend_mappings_Class2Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute2Attribute", type=Attribute2Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute118: BinaryAssociation = BinaryAssociation(
    name="attribute118",
    ends={
        Property(name="AttributeRef119", type=frontend_mappings_RelatedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_RelatedBy", type=AttributeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left104: BinaryAssociation = BinaryAssociation(
    name="left104",
    ends={
        Property(name="AttributeRef", type=frontend_mappings_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_AttributeMapping", type=AttributeRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightPart105: BinaryAssociation = BinaryAssociation(
    name="rightPart105",
    ends={
        Property(name="AttributeRightPart", type=frontend_mappings_AttributeMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_AttributeMapping106", type=AttributeRightPart, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resolveLink107: BinaryAssociation = BinaryAssociation(
    name="resolveLink107",
    ends={
        Property(name="ResolveLink", type=frontend_mappings_AttributeIsResolveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_AttributeIsResolveLink", type=ResolveLink, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings128: BinaryAssociation = BinaryAssociation(
    name="mappings128",
    ends={
        Property(name="ClassMapping129", type=frontend_mappings_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Join", type=ClassMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context130: BinaryAssociation = BinaryAssociation(
    name="context130",
    ends={
        Property(name="mappings131", type=frontend_mappings_Attribute2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Class2Class", type=Class2Class, multiplicity=Multiplicity(0, 1))
    }
)
right132: BinaryAssociation = BinaryAssociation(
    name="right132",
    ends={
        Property(name="AttributeRef133", type=frontend_mappings_Attribute2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Attribute2Attribute", type=AttributeRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modifiers134: BinaryAssociation = BinaryAssociation(
    name="modifiers134",
    ends={
        Property(name="AttributeModifier", type=frontend_mappings_Attribute2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Attribute2Attribute135", type=AttributeModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left136: BinaryAssociation = BinaryAssociation(
    name="left136",
    ends={
        Property(name="ReferenceRef", type=frontend_mappings_Reference2Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Reference2Reference", type=ReferenceRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right137: BinaryAssociation = BinaryAssociation(
    name="right137",
    ends={
        Property(name="ReferenceRef139", type=frontend_mappings_Reference2Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Reference2Reference138", type=ReferenceRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute120: BinaryAssociation = BinaryAssociation(
    name="attribute120",
    ends={
        Property(name="AttributeRef121", type=frontend_mappings_LinkedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_LinkedBy", type=AttributeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
linkedElement122: BinaryAssociation = BinaryAssociation(
    name="linkedElement122",
    ends={
        Property(name="MatchedElement124", type=frontend_mappings_LinkedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_LinkedBy123", type=MatchedElement, multiplicity=Multiplicity(1, 1))
    }
)
attribute125: BinaryAssociation = BinaryAssociation(
    name="attribute125",
    ends={
        Property(name="AttributeRef126", type=frontend_mappings_EqualityFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_EqualityFilter", type=AttributeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mappings127: BinaryAssociation = BinaryAssociation(
    name="mappings127",
    ends={
        Property(name="ClassMapping", type=frontend_mappings_Split, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Split", type=ClassMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredElement142: BinaryAssociation = BinaryAssociation(
    name="referredElement142",
    ends={
        Property(name="MatchedElement143", type=frontend_mappings_FeatureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_FeatureRef", type=MatchedElement, multiplicity=Multiplicity(1, 1))
    }
)
referredElement144: BinaryAssociation = BinaryAssociation(
    name="referredElement144",
    ends={
        Property(name="MatchedElement145", type=frontend_mappings_AttributeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_AttributeRef", type=MatchedElement, multiplicity=Multiplicity(1, 1))
    }
)
referredElement146: BinaryAssociation = BinaryAssociation(
    name="referredElement146",
    ends={
        Property(name="MatchedElement147", type=frontend_mappings_ReferenceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_ReferenceRef", type=MatchedElement, multiplicity=Multiplicity(1, 1))
    }
)
queues148: BinaryAssociation = BinaryAssociation(
    name="queues148",
    ends={
        Property(name="QoolQueue", type=frontend_qool_QoolTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_QoolTransformation", type=QoolQueue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segments149: BinaryAssociation = BinaryAssociation(
    name="segments149",
    ends={
        Property(name="Segment", type=frontend_qool_QoolTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_QoolTransformation150", type=Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
klass140: BinaryAssociation = BinaryAssociation(
    name="klass140",
    ends={
        Property(name="ClassUse141", type=frontend_mappings_ClassRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_ClassRef", type=ClassUse, multiplicity=Multiplicity(1, 1))
    }
)
class_153: BinaryAssociation = BinaryAssociation(
    name="class_153",
    ends={
        Property(name="ClassUse154", type=frontend_qool_ModelElementQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_ModelElementQueue", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
additionals155: BinaryAssociation = BinaryAssociation(
    name="additionals155",
    ends={
        Property(name="ClassUse157", type=frontend_qool_ModelElementQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_ModelElementQueue156", type=ClassUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements158: BinaryAssociation = BinaryAssociation(
    name="statements158",
    ends={
        Property(name="Statement159", type=frontend_qool_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_Segment", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition160: BinaryAssociation = BinaryAssociation(
    name="condition160",
    ends={
        Property(name="Expression161", type=frontend_qool_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_IteratorStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements162: BinaryAssociation = BinaryAssociation(
    name="statements162",
    ends={
        Property(name="Statement164", type=frontend_qool_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_IteratorStatement163", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queue165: BinaryAssociation = BinaryAssociation(
    name="queue165",
    ends={
        Property(name="QoolQueue166", type=frontend_qool_ForAllStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_ForAllStatement", type=QoolQueue, multiplicity=Multiplicity(1, 1))
    }
)
collection167: BinaryAssociation = BinaryAssociation(
    name="collection167",
    ends={
        Property(name="Expression168", type=frontend_qool_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_ForEachStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queue169: BinaryAssociation = BinaryAssociation(
    name="queue169",
    ends={
        Property(name="QoolQueue170", type=frontend_qool_EmitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_EmitStatement", type=QoolQueue, multiplicity=Multiplicity(1, 1))
    }
)
value171: BinaryAssociation = BinaryAssociation(
    name="value171",
    ends={
        Property(name="Expression173", type=frontend_qool_EmitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_EmitStatement172", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
optimizations151: BinaryAssociation = BinaryAssociation(
    name="optimizations151",
    ends={
        Property(name="QueueOptimization", type=frontend_qool_QoolQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_QoolQueue", type=QueueOptimization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_152: BinaryAssociation = BinaryAssociation(
    name="type_152",
    ends={
        Property(name="TypeExpression", type=frontend_qool_LocalQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_LocalQueue", type=TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicates176: BinaryAssociation = BinaryAssociation(
    name="predicates176",
    ends={
        Property(name="frontend_qool_MatchExpression177", type=MatchPredicate, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="MatchPredicate", type=frontend_qool_MatchExpression, multiplicity=Multiplicity(1, 1))
    }
)
class_178: BinaryAssociation = BinaryAssociation(
    name="class_178",
    ends={
        Property(name="ClassUse179", type=frontend_qool_KindOfPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_KindOfPredicate", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value180: BinaryAssociation = BinaryAssociation(
    name="value180",
    ends={
        Property(name="Expression181", type=frontend_qool_PropertyEqualsPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_PropertyEqualsPredicate", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceModels182: BinaryAssociation = BinaryAssociation(
    name="sourceModels182",
    ends={
        Property(name="InvocationParameter", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation", type=InvocationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetModels183: BinaryAssociation = BinaryAssociation(
    name="targetModels183",
    ends={
        Property(name="InvocationParameter185", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation184", type=InvocationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters186: BinaryAssociation = BinaryAssociation(
    name="parameters186",
    ends={
        Property(name="NamedInvocationParameter", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation187", type=NamedInvocationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputViewFilter188: BinaryAssociation = BinaryAssociation(
    name="inputViewFilter188",
    ends={
        Property(name="Variable190", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation189", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
queue174: BinaryAssociation = BinaryAssociation(
    name="queue174",
    ends={
        Property(name="QoolQueue175", type=frontend_qool_MatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_MatchExpression", type=QoolQueue, multiplicity=Multiplicity(1, 1))
    }
)
actualParameter197: BinaryAssociation = BinaryAssociation(
    name="actualParameter197",
    ends={
        Property(name="Expression198", type=frontend_qool_NamedInvocationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_NamedInvocationParameter", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objects199: BinaryAssociation = BinaryAssociation(
    name="objects199",
    ends={
        Property(name="Expression200", type=frontend_facilities_Copier, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_Copier", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callbacks201: BinaryAssociation = BinaryAssociation(
    name="callbacks201",
    ends={
        Property(name="facilities_CopierCallbackDefinition", type=frontend_facilities_Copier, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_Copier202", type=facilities_CopierCallbackDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copyInModel203: BinaryAssociation = BinaryAssociation(
    name="copyInModel203",
    ends={
        Property(name="TransformationDefinitionParameter205", type=frontend_facilities_Copier, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_Copier204", type=TransformationDefinitionParameter, multiplicity=Multiplicity(1, 1))
    }
)
trigger206: BinaryAssociation = BinaryAssociation(
    name="trigger206",
    ends={
        Property(name="Expression207", type=frontend_facilities_CopierCallbackDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_CopierCallbackDefinition", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action208: BinaryAssociation = BinaryAssociation(
    name="action208",
    ends={
        Property(name="Expression210", type=frontend_facilities_CopierCallbackDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_CopierCallbackDefinition209", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
templates211: BinaryAssociation = BinaryAssociation(
    name="templates211",
    ends={
        Property(name="Template", type=frontend_tao_TaoTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_TaoTransformation", type=Template, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type212: BinaryAssociation = BinaryAssociation(
    name="type212",
    ends={
        Property(name="ClassUse213", type=frontend_tao_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_TemplateParameter", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
entryPointParameters191: BinaryAssociation = BinaryAssociation(
    name="entryPointParameters191",
    ends={
        Property(name="Expression193", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation192", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputResolutionSourceElement194: BinaryAssociation = BinaryAssociation(
    name="outputResolutionSourceElement194",
    ends={
        Property(name="Expression195", type=frontend_qool_InvokeExternal, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeExternal", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model196: BinaryAssociation = BinaryAssociation(
    name="model196",
    ends={
        Property(name="TransformationDefinitionParameter", type=frontend_qool_InvocationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvocationParameter", type=TransformationDefinitionParameter, multiplicity=Multiplicity(1, 1))
    }
)
expr221: BinaryAssociation = BinaryAssociation(
    name="expr221",
    ends={
        Property(name="SourceExpression", type=frontend_tao_AttributeAssigment, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_AttributeAssigment", type=SourceExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable222: BinaryAssociation = BinaryAssociation(
    name="variable222",
    ends={
        Property(name="ObjectSourceVariable", type=frontend_tao_WithOptionalVariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_WithOptionalVariableExpression", type=ObjectSourceVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr223: BinaryAssociation = BinaryAssociation(
    name="expr223",
    ends={
        Property(name="Expression225", type=frontend_tao_WithOptionalVariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_WithOptionalVariableExpression224", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr226: BinaryAssociation = BinaryAssociation(
    name="expr226",
    ends={
        Property(name="SourceExpression227", type=frontend_tao_ReferenceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ReferenceAssignment", type=SourceExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object228: BinaryAssociation = BinaryAssociation(
    name="object228",
    ends={
        Property(name="ObjectInstantiation", type=frontend_tao_ObjectSyntax, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ObjectSyntax", type=ObjectInstantiation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
template229: BinaryAssociation = BinaryAssociation(
    name="template229",
    ends={
        Property(name="Template230", type=frontend_tao_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_Invocation", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
type214: BinaryAssociation = BinaryAssociation(
    name="type214",
    ends={
        Property(name="ClassUse215", type=frontend_tao_ObjectInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ObjectInstantiation", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assigments216: BinaryAssociation = BinaryAssociation(
    name="assigments216",
    ends={
        Property(name="Assignment", type=frontend_tao_ObjectInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ObjectInstantiation217", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters218: BinaryAssociation = BinaryAssociation(
    name="parameters218",
    ends={
        Property(name="TemplateParameter", type=frontend_tao_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_Template", type=TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roots219: BinaryAssociation = BinaryAssociation(
    name="roots219",
    ends={
        Property(name="TemplateRootObject", type=frontend_tao_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_Template220", type=TemplateRootObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedWith231: BinaryAssociation = BinaryAssociation(
    name="annotatedWith231",
    ends={
        Property(name="core", type=frontend_core_AnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Annotation", type=Annotation, multiplicity=Multiplicity(0, 9999))
    }
)
annotations232: BinaryAssociation = BinaryAssociation(
    name="annotations232",
    ends={
        Property(name="SingleAnnotation", type=frontend_core_ImplicitlyAnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ImplicitlyAnnotableElement", type=SingleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement233: BinaryAssociation = BinaryAssociation(
    name="annotatedElement233",
    ends={
        Property(name="core234", type=frontend_core_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="AnnotableElement", type=AnnotableElement, multiplicity=Multiplicity(0, 1))
    }
)
parameters235: BinaryAssociation = BinaryAssociation(
    name="parameters235",
    ends={
        Property(name="AnnotationParameter", type=frontend_core_GenericAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_GenericAnnotation", type=AnnotationParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inModels236: BinaryAssociation = BinaryAssociation(
    name="inModels236",
    ends={
        Property(name="TransformationDefinitionParameter237", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition", type=TransformationDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requires251: BinaryAssociation = BinaryAssociation(
    name="requires251",
    ends={
        Property(name="RequireDeclaration", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition252", type=RequireDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformations253: BinaryAssociation = BinaryAssociation(
    name="transformations253",
    ends={
        Property(name="TransformationDefinition", type=frontend_core_EclecticTransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_EclecticTransformationDefinition", type=TransformationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outModels238: BinaryAssociation = BinaryAssociation(
    name="outModels238",
    ends={
        Property(name="TransformationDefinitionParameter240", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition239", type=TransformationDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedModels241: BinaryAssociation = BinaryAssociation(
    name="importedModels241",
    ends={
        Property(name="ImportedModel", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition242", type=ImportedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineModels243: BinaryAssociation = BinaryAssociation(
    name="inlineModels243",
    ends={
        Property(name="InlineModel", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition244", type=InlineModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations245: BinaryAssociation = BinaryAssociation(
    name="annotations245",
    ends={
        Property(name="Annotation247", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition246", type=Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses248: BinaryAssociation = BinaryAssociation(
    name="uses248",
    ends={
        Property(name="UseDeclaration250", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition249", type=UseDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model255: BinaryAssociation = BinaryAssociation(
    name="model255",
    ends={
        Property(name="frontend_core_RequireModelParameter", type=RepresentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentModel256", type=frontend_core_RequireModelParameter, multiplicity=Multiplicity(1, 1))
    }
)
expression257: BinaryAssociation = BinaryAssociation(
    name="expression257",
    ends={
        Property(name="Expression258", type=frontend_core_DefineVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_DefineVariable", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters254: BinaryAssociation = BinaryAssociation(
    name="parameters254",
    ends={
        Property(name="RequireParameter", type=frontend_core_RequireDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_RequireDeclaration", type=RequireParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable264: BinaryAssociation = BinaryAssociation(
    name="variable264",
    ends={
        Property(name="Variable265", type=frontend_core_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_VariableReference", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
receptor266: BinaryAssociation = BinaryAssociation(
    name="receptor266",
    ends={
        Property(name="Expression267", type=frontend_core_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_MethodCall", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters268: BinaryAssociation = BinaryAssociation(
    name="parameters268",
    ends={
        Property(name="Expression270", type=frontend_core_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_MethodCall269", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receptor259: BinaryAssociation = BinaryAssociation(
    name="receptor259",
    ends={
        Property(name="Variable260", type=frontend_core_PropertyWrite, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PropertyWrite", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression261: BinaryAssociation = BinaryAssociation(
    name="expression261",
    ends={
        Property(name="Expression263", type=frontend_core_PropertyWrite, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PropertyWrite262", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters273: BinaryAssociation = BinaryAssociation(
    name="parameters273",
    ends={
        Property(name="KeywordParameter", type=frontend_core_KeywordMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_KeywordMethodCall274", type=KeywordParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value275: BinaryAssociation = BinaryAssociation(
    name="value275",
    ends={
        Property(name="Expression276", type=frontend_core_KeywordParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_KeywordParameter", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left277: BinaryAssociation = BinaryAssociation(
    name="left277",
    ends={
        Property(name="Expression278", type=frontend_core_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_BinaryExpr", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right279: BinaryAssociation = BinaryAssociation(
    name="right279",
    ends={
        Property(name="Expression281", type=frontend_core_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_BinaryExpr280", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receptor271: BinaryAssociation = BinaryAssociation(
    name="receptor271",
    ends={
        Property(name="Expression272", type=frontend_core_KeywordMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_KeywordMethodCall", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements282: BinaryAssociation = BinaryAssociation(
    name="statements282",
    ends={
        Property(name="Statement283", type=frontend_core_ClosureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ClosureDeclaration", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameters284: BinaryAssociation = BinaryAssociation(
    name="formalParameters284",
    ends={
        Property(name="ClosureParameter", type=frontend_core_ClosureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ClosureDeclaration285", type=ClosureParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr286: BinaryAssociation = BinaryAssociation(
    name="expr286",
    ends={
        Property(name="Expression287", type=frontend_core_ResolveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ResolveLink", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
module288: BinaryAssociation = BinaryAssociation(
    name="module288",
    ends={
        Property(name="UseDeclaration290", type=frontend_core_ResolveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ResolveLink289", type=UseDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
then291: BinaryAssociation = BinaryAssociation(
    name="then291",
    ends={
        Property(name="IfBranch", type=frontend_core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfExpr", type=IfBranch, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsifs292: BinaryAssociation = BinaryAssociation(
    name="elsifs292",
    ends={
        Property(name="IfBranch294", type=frontend_core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfExpr293", type=IfBranch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else295: BinaryAssociation = BinaryAssociation(
    name="else295",
    ends={
        Property(name="IfBranch297", type=frontend_core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfExpr296", type=IfBranch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition298: BinaryAssociation = BinaryAssociation(
    name="condition298",
    ends={
        Property(name="Expression299", type=frontend_core_IfBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfBranch", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements300: BinaryAssociation = BinaryAssociation(
    name="statements300",
    ends={
        Property(name="Statement302", type=frontend_core_IfBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfBranch301", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trace305: BinaryAssociation = BinaryAssociation(
    name="trace305",
    ends={
        Property(name="TraceDefinition", type=frontend_core_TraceUse, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceUse", type=TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
type_306: BinaryAssociation = BinaryAssociation(
    name="type_306",
    ends={
        Property(name="ClassUse307", type=frontend_core_TypedWithClass, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TypedWithClass", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions308: BinaryAssociation = BinaryAssociation(
    name="definitions308",
    ends={
        Property(name="TraceDefinition309", type=frontend_core_TraceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceInterface", type=TraceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements310: BinaryAssociation = BinaryAssociation(
    name="elements310",
    ends={
        Property(name="TraceElement", type=frontend_core_TraceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceDefinition", type=TraceElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type311: BinaryAssociation = BinaryAssociation(
    name="type311",
    ends={
        Property(name="TypeExpression312", type=frontend_core_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceElement", type=TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model303: BinaryAssociation = BinaryAssociation(
    name="model303",
    ends={
        Property(name="RepresentModel304", type=frontend_core_ClassUse, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ClassUse", type=RepresentModel, multiplicity=Multiplicity(1, 1))
    }
)
classes313: BinaryAssociation = BinaryAssociation(
    name="classes313",
    ends={
        Property(name="InlineClass", type=frontend_core_InlineModel, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_InlineModel", type=InlineClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features314: BinaryAssociation = BinaryAssociation(
    name="features314",
    ends={
        Property(name="frontend_core_InlineClass", type=InlineFeature, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="InlineFeature", type=frontend_core_InlineClass, multiplicity=Multiplicity(1, 1))
    }
)
type315: BinaryAssociation = BinaryAssociation(
    name="type315",
    ends={
        Property(name="TypeExpression316", type=frontend_core_InlineFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_InlineFeature", type=TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trace317: BinaryAssociation = BinaryAssociation(
    name="trace317",
    ends={
        Property(name="TraceDefinition318", type=frontend_core_MatchTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_MatchTrace", type=TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
traceExpr319: BinaryAssociation = BinaryAssociation(
    name="traceExpr319",
    ends={
        Property(name="TraceCompareExpression", type=frontend_core_MatchTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_MatchTrace320", type=TraceCompareExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
traceVar321: BinaryAssociation = BinaryAssociation(
    name="traceVar321",
    ends={
        Property(name="TraceElement322", type=frontend_core_TraceCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceCompareExpression", type=TraceElement, multiplicity=Multiplicity(1, 1))
    }
)
expr323: BinaryAssociation = BinaryAssociation(
    name="expr323",
    ends={
        Property(name="Expression325", type=frontend_core_TraceCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceCompareExpression324", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trace326: BinaryAssociation = BinaryAssociation(
    name="trace326",
    ends={
        Property(name="TraceDefinition327", type=frontend_core_PutTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTrace", type=TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parameters328: BinaryAssociation = BinaryAssociation(
    name="parameters328",
    ends={
        Property(name="PutTraceParameter", type=frontend_core_PutTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTrace329", type=PutTraceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value330: BinaryAssociation = BinaryAssociation(
    name="value330",
    ends={
        Property(name="Expression331", type=frontend_core_PutTraceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTraceParameter", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
traceVar332: BinaryAssociation = BinaryAssociation(
    name="traceVar332",
    ends={
        Property(name="TraceElement334", type=frontend_core_PutTraceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTraceParameter333", type=TraceElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_frontend_script_ScriptedTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_script_ScriptedTransformation)
gen_frontend_koan_KoanTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_koan_KoanTransformation)
gen_frontend_koan_KoanRule_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_koan_KoanRule)
gen_frontend_koan_KoanRule_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_koan_KoanRule)
gen_frontend_koan_Matcher_LocatedElement = Generalization(general=LocatedElement, specific=frontend_koan_Matcher)
gen_frontend_attribution_AttributionTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_attribution_AttributionTransformation)
gen_frontend_attribution_AttributeDcl_core_Variable = Generalization(general=core_Variable, specific=frontend_attribution_AttributeDcl)
gen_frontend_attribution_AttributeDcl_core_TypedWithClass = Generalization(general=core_TypedWithClass, specific=frontend_attribution_AttributeDcl)
gen_frontend_attribution_AttributeDcl_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_attribution_AttributeDcl)
gen_frontend_attribution_InheritedAttributeDcl_AttributeDcl = Generalization(general=AttributeDcl, specific=frontend_attribution_InheritedAttributeDcl)
gen_frontend_koan_ForAllMatcher_koan_Matcher = Generalization(general=koan_Matcher, specific=frontend_koan_ForAllMatcher)
gen_frontend_koan_ForAllMatcher_core_Variable = Generalization(general=core_Variable, specific=frontend_koan_ForAllMatcher)
gen_frontend_attribution_RuleSelf_Variable = Generalization(general=Variable, specific=frontend_attribution_RuleSelf)
gen_frontend_attribution_AttributeInit_Statement = Generalization(general=Statement, specific=frontend_attribution_AttributeInit)
gen_frontend_attribution_AttributeUse_Expression = Generalization(general=Expression, specific=frontend_attribution_AttributeUse)
gen_frontend_attribution_SynthesizedAttributeDcl_AttributeDcl = Generalization(general=AttributeDcl, specific=frontend_attribution_SynthesizedAttributeDcl)
gen_frontend_attribution_AttributionRule_LocatedElement = Generalization(general=LocatedElement, specific=frontend_attribution_AttributionRule)
gen_frontend_imperative_MethodDefinition_LocatedElement = Generalization(general=LocatedElement, specific=frontend_imperative_MethodDefinition)
gen_frontend_imperative_MethodSelf_Variable = Generalization(general=Variable, specific=frontend_imperative_MethodSelf)
gen_frontend_imperative_MethodParameter_Variable = Generalization(general=Variable, specific=frontend_imperative_MethodParameter)
gen_frontend_chain_ChainTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_chain_ChainTransformation)
gen_frontend_imperative_ImperativeTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_imperative_ImperativeTransformation)
gen_frontend_chain_GeneratedModel_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_chain_GeneratedModel)
gen_frontend_chain_GeneratedModel_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_chain_GeneratedModel)
gen_frontend_chain_TransformationExecution_LocatedElement = Generalization(general=LocatedElement, specific=frontend_chain_TransformationExecution)
gen_frontend_chain_ExternalTransformation_chain_AvailableTransformation = Generalization(general=chain_AvailableTransformation, specific=frontend_chain_ExternalTransformation)
gen_frontend_chain_ExternalTransformation_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_chain_ExternalTransformation)
gen_frontend_chain_CompositeTransformation_chain_AvailableTransformation = Generalization(general=chain_AvailableTransformation, specific=frontend_chain_CompositeTransformation)
gen_frontend_chain_CompositeTransformation_core_TransformationDefinition = Generalization(general=core_TransformationDefinition, specific=frontend_chain_CompositeTransformation)
gen_frontend_patterns_PObject_core_Variable = Generalization(general=core_Variable, specific=frontend_patterns_PObject)
gen_frontend_patterns_PObject_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_patterns_PObject)
gen_frontend_patterns_PFeature_LocatedElement = Generalization(general=LocatedElement, specific=frontend_patterns_PFeature)
gen_frontend_patterns_PatternSpecification_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_patterns_PatternSpecification)
gen_frontend_patterns_Pattern_LocatedElement = Generalization(general=LocatedElement, specific=frontend_patterns_Pattern)
gen_frontend_patterns_CollectionReference_PReference = Generalization(general=PReference, specific=frontend_patterns_CollectionReference)
gen_frontend_mappings_MappingTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_mappings_MappingTransformation)
gen_frontend_mappings_MappingVariable_Variable = Generalization(general=Variable, specific=frontend_mappings_MappingVariable)
gen_frontend_mappings_MatchedElement_core_ClassUse = Generalization(general=core_ClassUse, specific=frontend_mappings_MatchedElement)
gen_frontend_mappings_MatchedElement_mappings_MappingVariable = Generalization(general=mappings_MappingVariable, specific=frontend_mappings_MatchedElement)
gen_frontend_mappings_Delegate_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Delegate)
gen_frontend_patterns_PAttribute_PFeature = Generalization(general=PFeature, specific=frontend_patterns_PAttribute)
gen_frontend_patterns_PReference_PFeature = Generalization(general=PFeature, specific=frontend_patterns_PReference)
gen_frontend_mappings_Context_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Context)
gen_frontend_mappings_MappingElement_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_MappingElement)
gen_frontend_mappings_ClassMapping_MappingElement = Generalization(general=MappingElement, specific=frontend_mappings_ClassMapping)
gen_frontend_mappings_Feature2Feature_MappingElement = Generalization(general=MappingElement, specific=frontend_mappings_Feature2Feature)
gen_frontend_mappings_AttributeMapping_Feature2Feature = Generalization(general=Feature2Feature, specific=frontend_mappings_AttributeMapping)
gen_frontend_mappings_Section_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Section)
gen_frontend_mappings_AttributeIsInteger_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsInteger)
gen_frontend_mappings_Tag_NamedElement = Generalization(general=NamedElement, specific=frontend_mappings_Tag)
gen_frontend_mappings_Class2Class_ClassMapping = Generalization(general=ClassMapping, specific=frontend_mappings_Class2Class)
gen_frontend_mappings_C2CModifier_MappingElement = Generalization(general=MappingElement, specific=frontend_mappings_C2CModifier)
gen_frontend_mappings_RelatedBy_C2CModifier = Generalization(general=C2CModifier, specific=frontend_mappings_RelatedBy)
gen_frontend_mappings_AttributeIsString_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsString)
gen_frontend_mappings_AttributeIsBoolean_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsBoolean)
gen_frontend_mappings_AttributeIsDouble_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsDouble)
gen_frontend_mappings_AttributeIsResolveLink_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsResolveLink)
gen_frontend_mappings_Join_Operator = Generalization(general=Operator, specific=frontend_mappings_Join)
gen_frontend_mappings_Attribute2Attribute_mappings_Feature2Feature = Generalization(general=mappings_Feature2Feature, specific=frontend_mappings_Attribute2Attribute)
gen_frontend_mappings_Attribute2Attribute_mappings_AttributeRightPart = Generalization(general=mappings_AttributeRightPart, specific=frontend_mappings_Attribute2Attribute)
gen_frontend_mappings_Reference2Reference_Feature2Feature = Generalization(general=Feature2Feature, specific=frontend_mappings_Reference2Reference)
gen_frontend_mappings_AttributeModifier_Modifier = Generalization(general=Modifier, specific=frontend_mappings_AttributeModifier)
gen_frontend_mappings_LinkedBy_C2CModifier = Generalization(general=C2CModifier, specific=frontend_mappings_LinkedBy)
gen_frontend_mappings_EqualityFilter_C2CModifier = Generalization(general=C2CModifier, specific=frontend_mappings_EqualityFilter)
gen_frontend_mappings_Operator_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Operator)
gen_frontend_mappings_Split_Operator = Generalization(general=Operator, specific=frontend_mappings_Split)
gen_frontend_mappings_FeatureRef_mappings_MetamodelElementRef = Generalization(general=mappings_MetamodelElementRef, specific=frontend_mappings_FeatureRef)
gen_frontend_mappings_FeatureRef_mappings_Feature2Feature = Generalization(general=mappings_Feature2Feature, specific=frontend_mappings_FeatureRef)
gen_frontend_mappings_AttributeRef_MetamodelElementRef = Generalization(general=MetamodelElementRef, specific=frontend_mappings_AttributeRef)
gen_frontend_mappings_ReferenceRef_MetamodelElementRef = Generalization(general=MetamodelElementRef, specific=frontend_mappings_ReferenceRef)
gen_frontend_qool_QoolTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_qool_QoolTransformation)
gen_frontend_mappings_ConvertModifier_AttributeModifier = Generalization(general=AttributeModifier, specific=frontend_mappings_ConvertModifier)
gen_frontend_mappings_DefaultValue_AttributeModifier = Generalization(general=AttributeModifier, specific=frontend_mappings_DefaultValue)
gen_frontend_mappings_IntDefaultValue_DefaultValue = Generalization(general=DefaultValue, specific=frontend_mappings_IntDefaultValue)
gen_frontend_mappings_ClassRef_MetamodelElementRef = Generalization(general=MetamodelElementRef, specific=frontend_mappings_ClassRef)
gen_frontend_qool_ModelElementQueue_QoolQueue = Generalization(general=QoolQueue, specific=frontend_qool_ModelElementQueue)
gen_frontend_qool_Segment_NamedElement = Generalization(general=NamedElement, specific=frontend_qool_Segment)
gen_frontend_qool_IteratorStatement_core_Statement = Generalization(general=core_Statement, specific=frontend_qool_IteratorStatement)
gen_frontend_qool_IteratorStatement_core_Variable = Generalization(general=core_Variable, specific=frontend_qool_IteratorStatement)
gen_frontend_qool_ForAllStatement_IteratorStatement = Generalization(general=IteratorStatement, specific=frontend_qool_ForAllStatement)
gen_frontend_qool_ForEachStatement_IteratorStatement = Generalization(general=IteratorStatement, specific=frontend_qool_ForEachStatement)
gen_frontend_qool_EmitStatement_Statement = Generalization(general=Statement, specific=frontend_qool_EmitStatement)
gen_frontend_qool_QoolQueue_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_qool_QoolQueue)
gen_frontend_qool_QoolQueue_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_qool_QoolQueue)
gen_frontend_qool_AccessByFeatureOptimization_QueueOptimization = Generalization(general=QueueOptimization, specific=frontend_qool_AccessByFeatureOptimization)
gen_frontend_qool_LocalQueue_QoolQueue = Generalization(general=QoolQueue, specific=frontend_qool_LocalQueue)
gen_frontend_qool_KindOfPredicate_MatchPredicate = Generalization(general=MatchPredicate, specific=frontend_qool_KindOfPredicate)
gen_frontend_qool_PropertyEqualsPredicate_MatchPredicate = Generalization(general=MatchPredicate, specific=frontend_qool_PropertyEqualsPredicate)
gen_frontend_qool_InvokeTransformation_Expression = Generalization(general=Expression, specific=frontend_qool_InvokeTransformation)
gen_frontend_qool_MatchExpression_Expression = Generalization(general=Expression, specific=frontend_qool_MatchExpression)
gen_frontend_facilities_Copier_Expression = Generalization(general=Expression, specific=frontend_facilities_Copier)
gen_frontend_tao_TaoTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_tao_TaoTransformation)
gen_frontend_tao_TemplateParameter_Variable = Generalization(general=Variable, specific=frontend_tao_TemplateParameter)
gen_frontend_tao_ObjectInstantiation_core_Variable = Generalization(general=core_Variable, specific=frontend_tao_ObjectInstantiation)
gen_frontend_tao_ObjectInstantiation_core_Statement = Generalization(general=core_Statement, specific=frontend_tao_ObjectInstantiation)
gen_frontend_qool_InvokeExternal_InvokeTransformation = Generalization(general=InvokeTransformation, specific=frontend_qool_InvokeExternal)
gen_frontend_qool_InvokeInternal_InvokeTransformation = Generalization(general=InvokeTransformation, specific=frontend_qool_InvokeInternal)
gen_frontend_tao_AttributeAssigment_Assignment = Generalization(general=Assignment, specific=frontend_tao_AttributeAssigment)
gen_frontend_tao_SourceExpression_LocatedElement = Generalization(general=LocatedElement, specific=frontend_tao_SourceExpression)
gen_frontend_tao_WithOptionalVariableExpression_SourceExpression = Generalization(general=SourceExpression, specific=frontend_tao_WithOptionalVariableExpression)
gen_frontend_tao_ObjectSourceVariable_Variable = Generalization(general=Variable, specific=frontend_tao_ObjectSourceVariable)
gen_frontend_tao_ReferenceAssignment_tao_Assignment = Generalization(general=tao_Assignment, specific=frontend_tao_ReferenceAssignment)
gen_frontend_tao_ReferenceAssignment_core_Variable = Generalization(general=core_Variable, specific=frontend_tao_ReferenceAssignment)
gen_frontend_tao_ObjectSyntax_ReferenceAssignment = Generalization(general=ReferenceAssignment, specific=frontend_tao_ObjectSyntax)
gen_frontend_tao_Invocation_ReferenceAssignment = Generalization(general=ReferenceAssignment, specific=frontend_tao_Invocation)
gen_frontend_tao_TemplateRootObject_ObjectInstantiation = Generalization(general=ObjectInstantiation, specific=frontend_tao_TemplateRootObject)
gen_frontend_tao_Template_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_tao_Template)
gen_frontend_tao_Template_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_tao_Template)
gen_frontend_tao_Assignment_Statement = Generalization(general=Statement, specific=frontend_tao_Assignment)
gen_frontend_core_OptimizationsAnnotation_Annotation = Generalization(general=Annotation, specific=frontend_core_OptimizationsAnnotation)
gen_frontend_core_MetamodelModelAnnotation_Annotation = Generalization(general=Annotation, specific=frontend_core_MetamodelModelAnnotation)
gen_frontend_core_SingleAnnotation_Annotation = Generalization(general=Annotation, specific=frontend_core_SingleAnnotation)
gen_frontend_core_PotencyAnnotation_SingleAnnotation = Generalization(general=SingleAnnotation, specific=frontend_core_PotencyAnnotation)
gen_frontend_core_RepresentModel_AnnotableElement = Generalization(general=AnnotableElement, specific=frontend_core_RepresentModel)
gen_frontend_core_TransformationDefinition_ModuleDefinition = Generalization(general=ModuleDefinition, specific=frontend_core_TransformationDefinition)
gen_frontend_core_DefinitionParameter_NamedElement = Generalization(general=NamedElement, specific=frontend_core_DefinitionParameter)
gen_frontend_core_ModuleParameter_DefinitionParameter = Generalization(general=DefinitionParameter, specific=frontend_core_ModuleParameter)
gen_frontend_core_ModuleDefinition_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_core_ModuleDefinition)
gen_frontend_core_ModuleDefinition_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_core_ModuleDefinition)
gen_frontend_core_ModuleDefinition_core_AnnotableElement = Generalization(general=core_AnnotableElement, specific=frontend_core_ModuleDefinition)
gen_frontend_core_EclecticTransformationDefinition_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_core_EclecticTransformationDefinition)
gen_frontend_core_TransformationDefinitionParameter_core_DefinitionParameter = Generalization(general=core_DefinitionParameter, specific=frontend_core_TransformationDefinitionParameter)
gen_frontend_core_TransformationDefinitionParameter_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_TransformationDefinitionParameter)
gen_frontend_core_ImportedModel_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_ImportedModel)
gen_frontend_core_ImportedModel_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_core_ImportedModel)
gen_frontend_core_UseDeclaration_RepresentModel = Generalization(general=RepresentModel, specific=frontend_core_UseDeclaration)
gen_frontend_core_RequireDeclaration_RepresentModel = Generalization(general=RepresentModel, specific=frontend_core_RequireDeclaration)
gen_frontend_core_Statement_LocatedElement = Generalization(general=LocatedElement, specific=frontend_core_Statement)
gen_frontend_core_Expression_Statement = Generalization(general=Statement, specific=frontend_core_Expression)
gen_frontend_core_DefineVariable_core_Statement = Generalization(general=core_Statement, specific=frontend_core_DefineVariable)
gen_frontend_core_DefineVariable_core_Variable = Generalization(general=core_Variable, specific=frontend_core_DefineVariable)
gen_frontend_core_PropertyWrite_Expression = Generalization(general=Expression, specific=frontend_core_PropertyWrite)
gen_frontend_core_RequireModelParameter_RequireParameter = Generalization(general=RequireParameter, specific=frontend_core_RequireModelParameter)
gen_frontend_core_ModelReference_core_Expression = Generalization(general=core_Expression, specific=frontend_core_ModelReference)
gen_frontend_core_VariableReference_Expression = Generalization(general=Expression, specific=frontend_core_VariableReference)
gen_frontend_core_MethodCall_Expression = Generalization(general=Expression, specific=frontend_core_MethodCall)
gen_frontend_core_ModelReference_core_ClassUse = Generalization(general=core_ClassUse, specific=frontend_core_ModelReference)
gen_frontend_core_BinaryExpr_Expression = Generalization(general=Expression, specific=frontend_core_BinaryExpr)
gen_frontend_core_KeywordMethodCall_Expression = Generalization(general=Expression, specific=frontend_core_KeywordMethodCall)
gen_frontend_core_ClosureParameter_Variable = Generalization(general=Variable, specific=frontend_core_ClosureParameter)
gen_frontend_core_ResolveLink_Expression = Generalization(general=Expression, specific=frontend_core_ResolveLink)
gen_frontend_core_ClosureDeclaration_Expression = Generalization(general=Expression, specific=frontend_core_ClosureDeclaration)
gen_frontend_core_IfExpr_Expression = Generalization(general=Expression, specific=frontend_core_IfExpr)
gen_frontend_core_NumLiteral_Expression = Generalization(general=Expression, specific=frontend_core_NumLiteral)
gen_frontend_core_DoubleLiteral_Expression = Generalization(general=Expression, specific=frontend_core_DoubleLiteral)
gen_frontend_core_StringLiteral_Expression = Generalization(general=Expression, specific=frontend_core_StringLiteral)
gen_frontend_core_BooleanLiteral_Expression = Generalization(general=Expression, specific=frontend_core_BooleanLiteral)
gen_frontend_core_TraceInterface_ModuleDefinition = Generalization(general=ModuleDefinition, specific=frontend_core_TraceInterface)
gen_frontend_core_TracedModelParameter_core_DefinitionParameter = Generalization(general=core_DefinitionParameter, specific=frontend_core_TracedModelParameter)
gen_frontend_core_TracedModelParameter_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_TracedModelParameter)
gen_frontend_core_TraceDefinition_NamedElement = Generalization(general=NamedElement, specific=frontend_core_TraceDefinition)
gen_frontend_core_TraceElement_NamedElement = Generalization(general=NamedElement, specific=frontend_core_TraceElement)
gen_frontend_core_ClassUse_core_TypeExpression = Generalization(general=core_TypeExpression, specific=frontend_core_ClassUse)
gen_frontend_core_ClassUse_core_ImplicitlyAnnotableElement = Generalization(general=core_ImplicitlyAnnotableElement, specific=frontend_core_ClassUse)
gen_frontend_core_InlineModel_core_ModuleDefinition = Generalization(general=core_ModuleDefinition, specific=frontend_core_InlineModel)
gen_frontend_core_InlineModel_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_InlineModel)
gen_frontend_core_TraceUse_TypeExpression = Generalization(general=TypeExpression, specific=frontend_core_TraceUse)
gen_frontend_core_InlineFeature_NamedElement = Generalization(general=NamedElement, specific=frontend_core_InlineFeature)
gen_frontend_core_InlineAttribute_InlineFeature = Generalization(general=InlineFeature, specific=frontend_core_InlineAttribute)
gen_frontend_core_InlineReference_InlineFeature = Generalization(general=InlineFeature, specific=frontend_core_InlineReference)
gen_frontend_core_MatchTrace_Expression = Generalization(general=Expression, specific=frontend_core_MatchTrace)
gen_frontend_core_PutTrace_Expression = Generalization(general=Expression, specific=frontend_core_PutTrace)
gen_frontend_core_InlineClass_NamedElement = Generalization(general=NamedElement, specific=frontend_core_InlineClass)

# Domain Model
domain_model = DomainModel(
    name="frontend",
    types={frontend_script_ScriptedTransformation, TransformationDefinition, Statement, frontend_koan_KoanTransformation, TraceInterface, KoanRule, frontend_koan_KoanRule, core_LocatedElement, core_NamedElement, Matcher, frontend_koan_Matcher, LocatedElement, frontend_koan_ForAllMatcher, koan_Matcher, frontend_DummyRootMetaclass, frontend_attribution_AttributionTransformation, AttributeDcl, AttributionRule, frontend_attribution_AttributeDcl, core_TypedWithClass, frontend_attribution_InheritedAttributeDcl, core_Variable, ClassUse, frontend_attribution_RuleSelf, Variable, frontend_attribution_AttributeInit, frontend_attribution_AttributeUse, frontend_attribution_SynthesizedAttributeDcl, frontend_attribution_AttributionRule, RuleSelf, Expression, MethodParameter, MethodSelf, frontend_imperative_MethodSelf, frontend_imperative_MethodParameter, frontend_chain_ChainTransformation, frontend_imperative_ImperativeTransformation, MethodDefinition, frontend_chain_GeneratedModel, frontend_imperative_MethodDefinition, core_RepresentModel, frontend_chain_TransformationExecution, AvailableTransformation, RepresentModel, frontend_chain_AvailableTransformation, frontend_chain_ExternalTransformation, chain_AvailableTransformation, frontend_chain_CompositeTransformation, core_TransformationDefinition, CompositeTransformation, ExternalTransformation, GeneratedModel, TransformationExecution, POutputVariable, frontend_patterns_POutputVariable, frontend_patterns_PObject, PFeature, frontend_patterns_PFeature, frontend_patterns_PatternSpecification, Pattern, frontend_patterns_Pattern, PObject, frontend_patterns_CollectionReference, PReference, frontend_mappings_MappingTransformation, Delegate, Context, frontend_mappings_MappingVariable, frontend_mappings_MatchedElement, core_ClassUse, mappings_MappingVariable, frontend_mappings_Delegate, frontend_patterns_PAttribute, UseDeclaration, frontend_patterns_PReference, Tag, frontend_mappings_Context, MappingElement, C2CModifier, MatchedElement, frontend_mappings_MappingElement, frontend_mappings_ClassMapping, frontend_mappings_Feature2Feature, FeatureRef, Converter, frontend_mappings_AttributeMapping, Feature2Feature, Section, frontend_mappings_Section, frontend_mappings_AttributeIsInteger, frontend_mappings_Converter, frontend_mappings_Tag, NamedElement, frontend_mappings_Class2Class, ClassMapping, ClassRef, Attribute2Attribute, frontend_mappings_C2CModifier, frontend_mappings_RelatedBy, AttributeRef, AttributeRightPart, frontend_mappings_AttributeRightPart, frontend_mappings_AttributeIsString, frontend_mappings_AttributeIsBoolean, frontend_mappings_AttributeIsDouble, frontend_mappings_AttributeIsResolveLink, ResolveLink, frontend_mappings_Join, frontend_mappings_Attribute2Attribute, mappings_Feature2Feature, mappings_AttributeRightPart, Class2Class, AttributeModifier, frontend_mappings_Reference2Reference, ReferenceRef, frontend_mappings_Modifier, frontend_mappings_AttributeModifier, Modifier, frontend_mappings_LinkedBy, frontend_mappings_EqualityFilter, frontend_mappings_Operator, frontend_mappings_Split, Operator, frontend_mappings_FeatureRef, mappings_MetamodelElementRef, frontend_mappings_AttributeRef, frontend_mappings_ReferenceRef, frontend_qool_QoolTransformation, QoolQueue, Segment, frontend_mappings_ConvertModifier, frontend_mappings_DefaultValue, frontend_mappings_IntDefaultValue, DefaultValue, frontend_mappings_MetamodelElementRef, frontend_mappings_ClassRef, MetamodelElementRef, frontend_qool_ModelElementQueue, frontend_qool_Segment, frontend_qool_IteratorStatement, core_Statement, frontend_qool_ForAllStatement, IteratorStatement, frontend_qool_ForEachStatement, frontend_qool_EmitStatement, frontend_qool_QoolQueue, QueueOptimization, frontend_qool_QueueOptimization, frontend_qool_AccessByFeatureOptimization, frontend_qool_LocalQueue, TypeExpression, frontend_qool_MatchPredicate, frontend_qool_KindOfPredicate, frontend_qool_PropertyEqualsPredicate, frontend_qool_InvokeTransformation, InvocationParameter, NamedInvocationParameter, frontend_qool_MatchExpression, MatchPredicate, frontend_facilities_Copier, facilities_CopierCallbackDefinition, frontend_facilities_CopierCallbackDefinition, frontend_tao_TaoTransformation, Template, frontend_tao_TemplateParameter, frontend_tao_ObjectInstantiation, frontend_qool_InvokeExternal, InvokeTransformation, frontend_qool_InvokeInternal, frontend_qool_InvocationParameter, TransformationDefinitionParameter, frontend_qool_NamedInvocationParameter, frontend_tao_AttributeAssigment, SourceExpression, frontend_tao_SourceExpression, frontend_tao_WithOptionalVariableExpression, ObjectSourceVariable, frontend_tao_ObjectSourceVariable, frontend_tao_ReferenceAssignment, tao_Assignment, frontend_tao_ObjectSyntax, ReferenceAssignment, frontend_tao_Invocation, Assignment, frontend_tao_TemplateRootObject, ObjectInstantiation, frontend_tao_Template, TemplateParameter, TemplateRootObject, frontend_tao_Assignment, frontend_core_ImplicitlyAnnotableElement, SingleAnnotation, frontend_core_Annotation, AnnotableElement, frontend_core_OptimizationsAnnotation, frontend_core_MetamodelModelAnnotation, frontend_core_SingleAnnotation, frontend_core_PotencyAnnotation, frontend_core_GenericAnnotation, AnnotationParameter, frontend_core_AnnotationParameter, frontend_core_RepresentModel, frontend_core_TransformationDefinition, ModuleDefinition, frontend_core_LocatedElement, frontend_core_NamedElement, frontend_core_DefinitionParameter, frontend_core_ModuleParameter, DefinitionParameter, frontend_core_ModuleDefinition, core_AnnotableElement, frontend_core_AnnotableElement, Annotation, RequireDeclaration, frontend_core_EclecticTransformationDefinition, frontend_core_TransformationDefinitionParameter, core_DefinitionParameter, frontend_core_ImportedModel, frontend_core_UseDeclaration, frontend_core_RequireDeclaration, ImportedModel, InlineModel, frontend_core_Variable, frontend_core_Statement, frontend_core_Expression, frontend_core_DefineVariable, frontend_core_PropertyWrite, RequireParameter, frontend_core_RequireParameter, frontend_core_RequireModelParameter, core_Expression, frontend_core_VariableReference, frontend_core_MethodCall, frontend_core_ModelReference, KeywordParameter, frontend_core_KeywordParameter, frontend_core_BinaryExpr, frontend_core_KeywordMethodCall, ClosureParameter, frontend_core_ClosureParameter, frontend_core_ResolveLink, frontend_core_ClosureDeclaration, frontend_core_IfExpr, IfBranch, frontend_core_IfBranch, frontend_core_NumLiteral, frontend_core_DoubleLiteral, frontend_core_StringLiteral, frontend_core_BooleanLiteral, TraceDefinition, frontend_core_TypedWithClass, frontend_core_TraceInterface, frontend_core_TracedModelParameter, frontend_core_TraceDefinition, TraceElement, frontend_core_TypeExpression, frontend_core_TraceElement, frontend_core_ClassUse, core_TypeExpression, core_ImplicitlyAnnotableElement, frontend_core_InlineModel, core_ModuleDefinition, InlineClass, frontend_core_TraceUse, frontend_core_InlineFeature, frontend_core_InlineAttribute, frontend_core_InlineReference, frontend_core_MatchTrace, TraceCompareExpression, frontend_core_TraceCompareExpression, frontend_core_PutTrace, frontend_core_InlineClass, InlineFeature, PutTraceParameter, frontend_core_PutTraceParameter, MappingCardinality, BinaryOp, ResolveTraceCardinality},
    associations={statements0, traceInterface1, rules2, matcher4, statements5, child8, attributes11, rules12, type10, condition18, statements20, attribute23, receptor25, right28, expr31, type14, self16, formalParameters37, self38, type40, statements43, attribute33, methods36, transformation53, inputModels54, outputModels56, composites46, externals47, generatedModels49, objects62, executions51, outputVariables63, object65, type67, features69, executions59, patterns61, value75, delegates77, contexts78, value71, variable73, module81, tags83, left85, right87, mappings90, left80, mappings99, leftFeature101, converter102, modifiers92, sections94, tags96, module108, modifiers110, left112, right114, scopedAttributes117, attribute118, left104, rightPart105, resolveLink107, mappings128, context130, right132, modifiers134, left136, right137, attribute120, linkedElement122, attribute125, mappings127, referredElement142, referredElement144, referredElement146, queues148, segments149, klass140, class_153, additionals155, statements158, condition160, statements162, queue165, collection167, queue169, value171, optimizations151, type_152, predicates176, class_178, value180, sourceModels182, targetModels183, parameters186, inputViewFilter188, queue174, actualParameter197, objects199, callbacks201, copyInModel203, trigger206, action208, templates211, type212, entryPointParameters191, outputResolutionSourceElement194, model196, expr221, variable222, expr223, expr226, object228, template229, type214, assigments216, parameters218, roots219, annotatedWith231, annotations232, annotatedElement233, parameters235, inModels236, requires251, transformations253, outModels238, importedModels241, inlineModels243, annotations245, uses248, model255, expression257, parameters254, variable264, receptor266, parameters268, receptor259, expression261, parameters273, value275, left277, right279, receptor271, statements282, formalParameters284, expr286, module288, then291, elsifs292, else295, condition298, statements300, trace305, type_306, definitions308, elements310, type311, model303, classes313, features314, type315, trace317, traceExpr319, traceVar321, expr323, trace326, parameters328, value330, traceVar332},
    generalizations={gen_frontend_script_ScriptedTransformation_TransformationDefinition, gen_frontend_koan_KoanTransformation_TransformationDefinition, gen_frontend_koan_KoanRule_core_LocatedElement, gen_frontend_koan_KoanRule_core_NamedElement, gen_frontend_koan_Matcher_LocatedElement, gen_frontend_attribution_AttributionTransformation_TransformationDefinition, gen_frontend_attribution_AttributeDcl_core_Variable, gen_frontend_attribution_AttributeDcl_core_TypedWithClass, gen_frontend_attribution_AttributeDcl_core_LocatedElement, gen_frontend_attribution_InheritedAttributeDcl_AttributeDcl, gen_frontend_koan_ForAllMatcher_koan_Matcher, gen_frontend_koan_ForAllMatcher_core_Variable, gen_frontend_attribution_RuleSelf_Variable, gen_frontend_attribution_AttributeInit_Statement, gen_frontend_attribution_AttributeUse_Expression, gen_frontend_attribution_SynthesizedAttributeDcl_AttributeDcl, gen_frontend_attribution_AttributionRule_LocatedElement, gen_frontend_imperative_MethodDefinition_LocatedElement, gen_frontend_imperative_MethodSelf_Variable, gen_frontend_imperative_MethodParameter_Variable, gen_frontend_chain_ChainTransformation_TransformationDefinition, gen_frontend_imperative_ImperativeTransformation_TransformationDefinition, gen_frontend_chain_GeneratedModel_core_RepresentModel, gen_frontend_chain_GeneratedModel_core_NamedElement, gen_frontend_chain_TransformationExecution_LocatedElement, gen_frontend_chain_ExternalTransformation_chain_AvailableTransformation, gen_frontend_chain_ExternalTransformation_core_NamedElement, gen_frontend_chain_CompositeTransformation_chain_AvailableTransformation, gen_frontend_chain_CompositeTransformation_core_TransformationDefinition, gen_frontend_patterns_PObject_core_Variable, gen_frontend_patterns_PObject_core_LocatedElement, gen_frontend_patterns_PFeature_LocatedElement, gen_frontend_patterns_PatternSpecification_TransformationDefinition, gen_frontend_patterns_Pattern_LocatedElement, gen_frontend_patterns_CollectionReference_PReference, gen_frontend_mappings_MappingTransformation_TransformationDefinition, gen_frontend_mappings_MappingVariable_Variable, gen_frontend_mappings_MatchedElement_core_ClassUse, gen_frontend_mappings_MatchedElement_mappings_MappingVariable, gen_frontend_mappings_Delegate_LocatedElement, gen_frontend_patterns_PAttribute_PFeature, gen_frontend_patterns_PReference_PFeature, gen_frontend_mappings_Context_LocatedElement, gen_frontend_mappings_MappingElement_LocatedElement, gen_frontend_mappings_ClassMapping_MappingElement, gen_frontend_mappings_Feature2Feature_MappingElement, gen_frontend_mappings_AttributeMapping_Feature2Feature, gen_frontend_mappings_Section_LocatedElement, gen_frontend_mappings_AttributeIsInteger_AttributeRightPart, gen_frontend_mappings_Tag_NamedElement, gen_frontend_mappings_Class2Class_ClassMapping, gen_frontend_mappings_C2CModifier_MappingElement, gen_frontend_mappings_RelatedBy_C2CModifier, gen_frontend_mappings_AttributeIsString_AttributeRightPart, gen_frontend_mappings_AttributeIsBoolean_AttributeRightPart, gen_frontend_mappings_AttributeIsDouble_AttributeRightPart, gen_frontend_mappings_AttributeIsResolveLink_AttributeRightPart, gen_frontend_mappings_Join_Operator, gen_frontend_mappings_Attribute2Attribute_mappings_Feature2Feature, gen_frontend_mappings_Attribute2Attribute_mappings_AttributeRightPart, gen_frontend_mappings_Reference2Reference_Feature2Feature, gen_frontend_mappings_AttributeModifier_Modifier, gen_frontend_mappings_LinkedBy_C2CModifier, gen_frontend_mappings_EqualityFilter_C2CModifier, gen_frontend_mappings_Operator_LocatedElement, gen_frontend_mappings_Split_Operator, gen_frontend_mappings_FeatureRef_mappings_MetamodelElementRef, gen_frontend_mappings_FeatureRef_mappings_Feature2Feature, gen_frontend_mappings_AttributeRef_MetamodelElementRef, gen_frontend_mappings_ReferenceRef_MetamodelElementRef, gen_frontend_qool_QoolTransformation_TransformationDefinition, gen_frontend_mappings_ConvertModifier_AttributeModifier, gen_frontend_mappings_DefaultValue_AttributeModifier, gen_frontend_mappings_IntDefaultValue_DefaultValue, gen_frontend_mappings_ClassRef_MetamodelElementRef, gen_frontend_qool_ModelElementQueue_QoolQueue, gen_frontend_qool_Segment_NamedElement, gen_frontend_qool_IteratorStatement_core_Statement, gen_frontend_qool_IteratorStatement_core_Variable, gen_frontend_qool_ForAllStatement_IteratorStatement, gen_frontend_qool_ForEachStatement_IteratorStatement, gen_frontend_qool_EmitStatement_Statement, gen_frontend_qool_QoolQueue_core_LocatedElement, gen_frontend_qool_QoolQueue_core_NamedElement, gen_frontend_qool_AccessByFeatureOptimization_QueueOptimization, gen_frontend_qool_LocalQueue_QoolQueue, gen_frontend_qool_KindOfPredicate_MatchPredicate, gen_frontend_qool_PropertyEqualsPredicate_MatchPredicate, gen_frontend_qool_InvokeTransformation_Expression, gen_frontend_qool_MatchExpression_Expression, gen_frontend_facilities_Copier_Expression, gen_frontend_tao_TaoTransformation_TransformationDefinition, gen_frontend_tao_TemplateParameter_Variable, gen_frontend_tao_ObjectInstantiation_core_Variable, gen_frontend_tao_ObjectInstantiation_core_Statement, gen_frontend_qool_InvokeExternal_InvokeTransformation, gen_frontend_qool_InvokeInternal_InvokeTransformation, gen_frontend_tao_AttributeAssigment_Assignment, gen_frontend_tao_SourceExpression_LocatedElement, gen_frontend_tao_WithOptionalVariableExpression_SourceExpression, gen_frontend_tao_ObjectSourceVariable_Variable, gen_frontend_tao_ReferenceAssignment_tao_Assignment, gen_frontend_tao_ReferenceAssignment_core_Variable, gen_frontend_tao_ObjectSyntax_ReferenceAssignment, gen_frontend_tao_Invocation_ReferenceAssignment, gen_frontend_tao_TemplateRootObject_ObjectInstantiation, gen_frontend_tao_Template_core_NamedElement, gen_frontend_tao_Template_core_LocatedElement, gen_frontend_tao_Assignment_Statement, gen_frontend_core_OptimizationsAnnotation_Annotation, gen_frontend_core_MetamodelModelAnnotation_Annotation, gen_frontend_core_SingleAnnotation_Annotation, gen_frontend_core_PotencyAnnotation_SingleAnnotation, gen_frontend_core_RepresentModel_AnnotableElement, gen_frontend_core_TransformationDefinition_ModuleDefinition, gen_frontend_core_DefinitionParameter_NamedElement, gen_frontend_core_ModuleParameter_DefinitionParameter, gen_frontend_core_ModuleDefinition_core_LocatedElement, gen_frontend_core_ModuleDefinition_core_NamedElement, gen_frontend_core_ModuleDefinition_core_AnnotableElement, gen_frontend_core_EclecticTransformationDefinition_TransformationDefinition, gen_frontend_core_TransformationDefinitionParameter_core_DefinitionParameter, gen_frontend_core_TransformationDefinitionParameter_core_RepresentModel, gen_frontend_core_ImportedModel_core_RepresentModel, gen_frontend_core_ImportedModel_core_NamedElement, gen_frontend_core_UseDeclaration_RepresentModel, gen_frontend_core_RequireDeclaration_RepresentModel, gen_frontend_core_Statement_LocatedElement, gen_frontend_core_Expression_Statement, gen_frontend_core_DefineVariable_core_Statement, gen_frontend_core_DefineVariable_core_Variable, gen_frontend_core_PropertyWrite_Expression, gen_frontend_core_RequireModelParameter_RequireParameter, gen_frontend_core_ModelReference_core_Expression, gen_frontend_core_VariableReference_Expression, gen_frontend_core_MethodCall_Expression, gen_frontend_core_ModelReference_core_ClassUse, gen_frontend_core_BinaryExpr_Expression, gen_frontend_core_KeywordMethodCall_Expression, gen_frontend_core_ClosureParameter_Variable, gen_frontend_core_ResolveLink_Expression, gen_frontend_core_ClosureDeclaration_Expression, gen_frontend_core_IfExpr_Expression, gen_frontend_core_NumLiteral_Expression, gen_frontend_core_DoubleLiteral_Expression, gen_frontend_core_StringLiteral_Expression, gen_frontend_core_BooleanLiteral_Expression, gen_frontend_core_TraceInterface_ModuleDefinition, gen_frontend_core_TracedModelParameter_core_DefinitionParameter, gen_frontend_core_TracedModelParameter_core_RepresentModel, gen_frontend_core_TraceDefinition_NamedElement, gen_frontend_core_TraceElement_NamedElement, gen_frontend_core_ClassUse_core_TypeExpression, gen_frontend_core_ClassUse_core_ImplicitlyAnnotableElement, gen_frontend_core_InlineModel_core_ModuleDefinition, gen_frontend_core_InlineModel_core_RepresentModel, gen_frontend_core_TraceUse_TypeExpression, gen_frontend_core_InlineFeature_NamedElement, gen_frontend_core_InlineAttribute_InlineFeature, gen_frontend_core_InlineReference_InlineFeature, gen_frontend_core_MatchTrace_Expression, gen_frontend_core_PutTrace_Expression, gen_frontend_core_InlineClass_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)