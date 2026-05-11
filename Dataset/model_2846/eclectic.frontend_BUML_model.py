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
frontend_DummyRootMetaclass = Class(name="frontend_DummyRootMetaclass")
frontend_script_ScriptedTransformation = Class(name="frontend_script_ScriptedTransformation")
TransformationDefinition = Class(name="TransformationDefinition")
Statement = Class(name="Statement")
frontend_koan_KoanTransformation = Class(name="frontend_koan_KoanTransformation")
TraceInterface = Class(name="TraceInterface")
KoanRule = Class(name="KoanRule")
frontend_koan_KoanRule = Class(name="frontend_koan_KoanRule")
core_LocatedElement = Class(name="core_LocatedElement")
core_NamedElement = Class(name="core_NamedElement")
Matcher = Class(name="Matcher")
frontend_koan_Matcher = Class(name="frontend_koan_Matcher", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
frontend_koan_ForAllMatcher = Class(name="frontend_koan_ForAllMatcher")
koan_Matcher = Class(name="koan_Matcher")
core_Variable = Class(name="core_Variable")
ClassUse = Class(name="ClassUse")
frontend_attribution_AttributionTransformation = Class(name="frontend_attribution_AttributionTransformation")
AttributeDcl = Class(name="AttributeDcl")
AttributionRule = Class(name="AttributionRule")
frontend_attribution_AttributeDcl = Class(name="frontend_attribution_AttributeDcl", is_abstract=True)
core_TypedWithClass = Class(name="core_TypedWithClass")
CompositeTransformation = Class(name="CompositeTransformation")
frontend_attribution_InheritedAttributeDcl = Class(name="frontend_attribution_InheritedAttributeDcl")
frontend_attribution_SynthesizedAttributeDcl = Class(name="frontend_attribution_SynthesizedAttributeDcl")
frontend_attribution_AttributionRule = Class(name="frontend_attribution_AttributionRule")
RuleSelf = Class(name="RuleSelf")
Expression = Class(name="Expression")
frontend_attribution_RuleSelf = Class(name="frontend_attribution_RuleSelf")
Variable = Class(name="Variable")
frontend_attribution_AttributeInit = Class(name="frontend_attribution_AttributeInit")
frontend_attribution_AttributeUse = Class(name="frontend_attribution_AttributeUse")
frontend_imperative_ImperativeTransformation = Class(name="frontend_imperative_ImperativeTransformation")
MethodDefinition = Class(name="MethodDefinition")
frontend_imperative_MethodDefinition = Class(name="frontend_imperative_MethodDefinition")
MethodParameter = Class(name="MethodParameter")
MethodSelf = Class(name="MethodSelf")
frontend_imperative_MethodSelf = Class(name="frontend_imperative_MethodSelf")
frontend_imperative_MethodParameter = Class(name="frontend_imperative_MethodParameter")
frontend_chain_ChainTransformation = Class(name="frontend_chain_ChainTransformation")
ExternalTransformation = Class(name="ExternalTransformation")
GeneratedModel = Class(name="GeneratedModel")
TransformationExecution = Class(name="TransformationExecution")
frontend_chain_GeneratedModel = Class(name="frontend_chain_GeneratedModel")
core_RepresentModel = Class(name="core_RepresentModel")
frontend_chain_TransformationExecution = Class(name="frontend_chain_TransformationExecution")
AvailableTransformation = Class(name="AvailableTransformation")
RepresentModel = Class(name="RepresentModel")
frontend_chain_AvailableTransformation = Class(name="frontend_chain_AvailableTransformation", is_abstract=True)
frontend_chain_ExternalTransformation = Class(name="frontend_chain_ExternalTransformation")
chain_AvailableTransformation = Class(name="chain_AvailableTransformation")
frontend_chain_CompositeTransformation = Class(name="frontend_chain_CompositeTransformation")
core_TransformationDefinition = Class(name="core_TransformationDefinition")
frontend_patterns_PatternSpecification = Class(name="frontend_patterns_PatternSpecification")
Pattern = Class(name="Pattern")
frontend_patterns_Pattern = Class(name="frontend_patterns_Pattern")
PObject = Class(name="PObject")
POutputVariable = Class(name="POutputVariable")
frontend_patterns_POutputVariable = Class(name="frontend_patterns_POutputVariable")
frontend_patterns_PObject = Class(name="frontend_patterns_PObject")
PFeature = Class(name="PFeature")
frontend_patterns_PFeature = Class(name="frontend_patterns_PFeature", is_abstract=True)
frontend_patterns_PAttribute = Class(name="frontend_patterns_PAttribute")
frontend_patterns_PReference = Class(name="frontend_patterns_PReference")
frontend_patterns_CollectionReference = Class(name="frontend_patterns_CollectionReference")
PReference = Class(name="PReference")
frontend_mappings_MappingTransformation = Class(name="frontend_mappings_MappingTransformation")
Delegate = Class(name="Delegate")
Context = Class(name="Context")
frontend_mappings_MappingVariable = Class(name="frontend_mappings_MappingVariable")
frontend_mappings_MatchedElement = Class(name="frontend_mappings_MatchedElement")
core_ClassUse = Class(name="core_ClassUse")
mappings_MappingVariable = Class(name="mappings_MappingVariable")
frontend_mappings_Delegate = Class(name="frontend_mappings_Delegate")
MatchedElement = Class(name="MatchedElement")
UseDeclaration = Class(name="UseDeclaration")
Tag = Class(name="Tag")
frontend_mappings_Context = Class(name="frontend_mappings_Context")
MappingElement = Class(name="MappingElement")
C2CModifier = Class(name="C2CModifier")
Section = Class(name="Section")
frontend_mappings_Section = Class(name="frontend_mappings_Section")
frontend_mappings_MappingElement = Class(name="frontend_mappings_MappingElement", is_abstract=True)
frontend_mappings_ClassMapping = Class(name="frontend_mappings_ClassMapping", is_abstract=True)
frontend_mappings_Feature2Feature = Class(name="frontend_mappings_Feature2Feature", is_abstract=True)
FeatureRef = Class(name="FeatureRef")
Converter = Class(name="Converter")
frontend_mappings_AttributeMapping = Class(name="frontend_mappings_AttributeMapping")
Feature2Feature = Class(name="Feature2Feature")
AttributeRef = Class(name="AttributeRef")
AttributeRightPart = Class(name="AttributeRightPart")
frontend_mappings_AttributeRightPart = Class(name="frontend_mappings_AttributeRightPart", is_abstract=True)
frontend_mappings_AttributeIsString = Class(name="frontend_mappings_AttributeIsString")
frontend_mappings_AttributeIsBoolean = Class(name="frontend_mappings_AttributeIsBoolean")
frontend_mappings_AttributeIsDouble = Class(name="frontend_mappings_AttributeIsDouble")
frontend_mappings_AttributeIsResolveLink = Class(name="frontend_mappings_AttributeIsResolveLink")
ResolveLink = Class(name="ResolveLink")
frontend_mappings_AttributeIsInteger = Class(name="frontend_mappings_AttributeIsInteger")
frontend_mappings_Converter = Class(name="frontend_mappings_Converter")
frontend_mappings_Tag = Class(name="frontend_mappings_Tag")
NamedElement = Class(name="NamedElement")
frontend_mappings_Class2Class = Class(name="frontend_mappings_Class2Class")
ClassMapping = Class(name="ClassMapping")
ClassRef = Class(name="ClassRef")
Attribute2Attribute = Class(name="Attribute2Attribute")
frontend_mappings_C2CModifier = Class(name="frontend_mappings_C2CModifier", is_abstract=True)
frontend_mappings_RelatedBy = Class(name="frontend_mappings_RelatedBy")
frontend_mappings_LinkedBy = Class(name="frontend_mappings_LinkedBy")
frontend_mappings_EqualityFilter = Class(name="frontend_mappings_EqualityFilter")
frontend_mappings_Operator = Class(name="frontend_mappings_Operator", is_abstract=True)
frontend_mappings_Split = Class(name="frontend_mappings_Split")
Operator = Class(name="Operator")
frontend_mappings_Join = Class(name="frontend_mappings_Join")
frontend_mappings_Attribute2Attribute = Class(name="frontend_mappings_Attribute2Attribute")
mappings_Feature2Feature = Class(name="mappings_Feature2Feature")
mappings_AttributeRightPart = Class(name="mappings_AttributeRightPart")
Class2Class = Class(name="Class2Class")
AttributeModifier = Class(name="AttributeModifier")
frontend_mappings_Reference2Reference = Class(name="frontend_mappings_Reference2Reference")
ReferenceRef = Class(name="ReferenceRef")
frontend_mappings_Modifier = Class(name="frontend_mappings_Modifier", is_abstract=True)
frontend_mappings_AttributeModifier = Class(name="frontend_mappings_AttributeModifier", is_abstract=True)
Modifier = Class(name="Modifier")
frontend_mappings_ConvertModifier = Class(name="frontend_mappings_ConvertModifier")
frontend_mappings_DefaultValue = Class(name="frontend_mappings_DefaultValue", is_abstract=True)
frontend_mappings_IntDefaultValue = Class(name="frontend_mappings_IntDefaultValue")
DefaultValue = Class(name="DefaultValue")
frontend_mappings_MetamodelElementRef = Class(name="frontend_mappings_MetamodelElementRef", is_abstract=True)
frontend_mappings_ClassRef = Class(name="frontend_mappings_ClassRef")
MetamodelElementRef = Class(name="MetamodelElementRef")
frontend_mappings_FeatureRef = Class(name="frontend_mappings_FeatureRef")
mappings_MetamodelElementRef = Class(name="mappings_MetamodelElementRef")
frontend_mappings_AttributeRef = Class(name="frontend_mappings_AttributeRef")
frontend_mappings_ReferenceRef = Class(name="frontend_mappings_ReferenceRef")
frontend_qool_QoolTransformation = Class(name="frontend_qool_QoolTransformation")
QoolQueue = Class(name="QoolQueue")
Segment = Class(name="Segment")
frontend_qool_QoolQueue = Class(name="frontend_qool_QoolQueue", is_abstract=True)
QueueOptimization = Class(name="QueueOptimization")
frontend_qool_QueueOptimization = Class(name="frontend_qool_QueueOptimization", is_abstract=True)
frontend_qool_AccessByFeatureOptimization = Class(name="frontend_qool_AccessByFeatureOptimization")
frontend_qool_LocalQueue = Class(name="frontend_qool_LocalQueue")
TypeExpression = Class(name="TypeExpression")
frontend_qool_ModelElementQueue = Class(name="frontend_qool_ModelElementQueue")
frontend_qool_Segment = Class(name="frontend_qool_Segment")
frontend_qool_IteratorStatement = Class(name="frontend_qool_IteratorStatement")
core_Statement = Class(name="core_Statement")
frontend_qool_ForAllStatement = Class(name="frontend_qool_ForAllStatement")
IteratorStatement = Class(name="IteratorStatement")
frontend_qool_ForEachStatement = Class(name="frontend_qool_ForEachStatement")
frontend_qool_EmitStatement = Class(name="frontend_qool_EmitStatement")
frontend_qool_MatchExpression = Class(name="frontend_qool_MatchExpression")
MatchPredicate = Class(name="MatchPredicate")
frontend_qool_MatchPredicate = Class(name="frontend_qool_MatchPredicate", is_abstract=True)
frontend_qool_KindOfPredicate = Class(name="frontend_qool_KindOfPredicate")
frontend_qool_InvokeTransformation = Class(name="frontend_qool_InvokeTransformation", is_abstract=True)
InvocationParameter = Class(name="InvocationParameter")
NamedInvocationParameter = Class(name="NamedInvocationParameter")
frontend_qool_InvokeExternal = Class(name="frontend_qool_InvokeExternal")
InvokeTransformation = Class(name="InvokeTransformation")
frontend_qool_InvokeInternal = Class(name="frontend_qool_InvokeInternal")
frontend_qool_InvocationParameter = Class(name="frontend_qool_InvocationParameter")
TransformationDefinitionParameter = Class(name="TransformationDefinitionParameter")
frontend_qool_NamedInvocationParameter = Class(name="frontend_qool_NamedInvocationParameter")
frontend_facilities_Copier = Class(name="frontend_facilities_Copier")
frontend_qool_PropertyEqualsPredicate = Class(name="frontend_qool_PropertyEqualsPredicate")
frontend_facilities_CopierCallbackDefinition = Class(name="frontend_facilities_CopierCallbackDefinition")
frontend_tao_TaoTransformation = Class(name="frontend_tao_TaoTransformation")
Template = Class(name="Template")
frontend_tao_TemplateParameter = Class(name="frontend_tao_TemplateParameter")
frontend_tao_ObjectInstantiation = Class(name="frontend_tao_ObjectInstantiation")
Assignment = Class(name="Assignment")
frontend_tao_TemplateRootObject = Class(name="frontend_tao_TemplateRootObject")
ObjectInstantiation = Class(name="ObjectInstantiation")
frontend_tao_Template = Class(name="frontend_tao_Template")
TemplateParameter = Class(name="TemplateParameter")
TemplateRootObject = Class(name="TemplateRootObject")
frontend_tao_Assignment = Class(name="frontend_tao_Assignment", is_abstract=True)
frontend_tao_AttributeAssigment = Class(name="frontend_tao_AttributeAssigment")
SourceExpression = Class(name="SourceExpression")
frontend_tao_SourceExpression = Class(name="frontend_tao_SourceExpression", is_abstract=True)
frontend_tao_WithOptionalVariableExpression = Class(name="frontend_tao_WithOptionalVariableExpression")
ObjectSourceVariable = Class(name="ObjectSourceVariable")
facilities_CopierCallbackDefinition = Class(name="facilities_CopierCallbackDefinition")
frontend_tao_ObjectSourceVariable = Class(name="frontend_tao_ObjectSourceVariable")
frontend_tao_ReferenceAssignment = Class(name="frontend_tao_ReferenceAssignment", is_abstract=True)
tao_Assignment = Class(name="tao_Assignment")
frontend_tao_ObjectSyntax = Class(name="frontend_tao_ObjectSyntax")
ReferenceAssignment = Class(name="ReferenceAssignment")
frontend_tao_Invocation = Class(name="frontend_tao_Invocation")
frontend_core_LocatedElement = Class(name="frontend_core_LocatedElement", is_abstract=True)
frontend_core_NamedElement = Class(name="frontend_core_NamedElement", is_abstract=True)
frontend_core_DefinitionParameter = Class(name="frontend_core_DefinitionParameter", is_abstract=True)
frontend_core_ModuleParameter = Class(name="frontend_core_ModuleParameter")
DefinitionParameter = Class(name="DefinitionParameter")
frontend_core_ModuleDefinition = Class(name="frontend_core_ModuleDefinition", is_abstract=True)
core_AnnotableElement = Class(name="core_AnnotableElement")
frontend_core_AnnotableElement = Class(name="frontend_core_AnnotableElement", is_abstract=True)
Annotation = Class(name="Annotation")
frontend_core_ImplicitlyAnnotableElement = Class(name="frontend_core_ImplicitlyAnnotableElement")
SingleAnnotation = Class(name="SingleAnnotation")
frontend_core_Annotation = Class(name="frontend_core_Annotation", is_abstract=True)
AnnotableElement = Class(name="AnnotableElement")
frontend_core_OptimizationsAnnotation = Class(name="frontend_core_OptimizationsAnnotation")
frontend_core_MetamodelModelAnnotation = Class(name="frontend_core_MetamodelModelAnnotation")
frontend_core_SingleAnnotation = Class(name="frontend_core_SingleAnnotation", is_abstract=True)
frontend_core_PotencyAnnotation = Class(name="frontend_core_PotencyAnnotation")
frontend_core_GenericAnnotation = Class(name="frontend_core_GenericAnnotation")
AnnotationParameter = Class(name="AnnotationParameter")
frontend_core_AnnotationParameter = Class(name="frontend_core_AnnotationParameter", is_abstract=True)
frontend_core_RepresentModel = Class(name="frontend_core_RepresentModel", is_abstract=True)
frontend_core_TransformationDefinition = Class(name="frontend_core_TransformationDefinition", is_abstract=True)
ModuleDefinition = Class(name="ModuleDefinition")
ImportedModel = Class(name="ImportedModel")
InlineModel = Class(name="InlineModel")
RequireDeclaration = Class(name="RequireDeclaration")
frontend_core_EclecticTransformationDefinition = Class(name="frontend_core_EclecticTransformationDefinition")
frontend_core_ImportedModel = Class(name="frontend_core_ImportedModel")
frontend_core_UseDeclaration = Class(name="frontend_core_UseDeclaration")
frontend_core_RequireDeclaration = Class(name="frontend_core_RequireDeclaration")
RequireParameter = Class(name="RequireParameter")
frontend_core_RequireParameter = Class(name="frontend_core_RequireParameter", is_abstract=True)
frontend_core_RequireModelParameter = Class(name="frontend_core_RequireModelParameter")
frontend_core_Variable = Class(name="frontend_core_Variable", is_abstract=True)
frontend_core_Statement = Class(name="frontend_core_Statement", is_abstract=True)
frontend_core_Expression = Class(name="frontend_core_Expression", is_abstract=True)
frontend_core_DefineVariable = Class(name="frontend_core_DefineVariable")
frontend_core_PropertyWrite = Class(name="frontend_core_PropertyWrite")
frontend_core_TransformationDefinitionParameter = Class(name="frontend_core_TransformationDefinitionParameter")
core_DefinitionParameter = Class(name="core_DefinitionParameter")
frontend_core_ModelReference = Class(name="frontend_core_ModelReference")
core_Expression = Class(name="core_Expression")
frontend_core_VariableReference = Class(name="frontend_core_VariableReference")
frontend_core_MethodCall = Class(name="frontend_core_MethodCall")
frontend_core_KeywordMethodCall = Class(name="frontend_core_KeywordMethodCall")
KeywordParameter = Class(name="KeywordParameter")
frontend_core_KeywordParameter = Class(name="frontend_core_KeywordParameter")
frontend_core_BinaryExpr = Class(name="frontend_core_BinaryExpr")
frontend_core_ClosureDeclaration = Class(name="frontend_core_ClosureDeclaration")
ClosureParameter = Class(name="ClosureParameter")
frontend_core_ClosureParameter = Class(name="frontend_core_ClosureParameter")
frontend_core_ResolveLink = Class(name="frontend_core_ResolveLink")
frontend_core_IfExpr = Class(name="frontend_core_IfExpr")
IfBranch = Class(name="IfBranch")
frontend_core_IfBranch = Class(name="frontend_core_IfBranch")
frontend_core_NumLiteral = Class(name="frontend_core_NumLiteral")
frontend_core_BooleanLiteral = Class(name="frontend_core_BooleanLiteral")
frontend_core_TypeExpression = Class(name="frontend_core_TypeExpression", is_abstract=True)
frontend_core_ClassUse = Class(name="frontend_core_ClassUse")
core_TypeExpression = Class(name="core_TypeExpression")
core_ImplicitlyAnnotableElement = Class(name="core_ImplicitlyAnnotableElement")
frontend_core_TraceUse = Class(name="frontend_core_TraceUse")
TraceDefinition = Class(name="TraceDefinition")
frontend_core_TypedWithClass = Class(name="frontend_core_TypedWithClass", is_abstract=True)
frontend_core_TraceInterface = Class(name="frontend_core_TraceInterface")
frontend_core_TracedModelParameter = Class(name="frontend_core_TracedModelParameter")
frontend_core_TraceDefinition = Class(name="frontend_core_TraceDefinition")
TraceElement = Class(name="TraceElement")
frontend_core_TraceElement = Class(name="frontend_core_TraceElement")
frontend_core_InlineModel = Class(name="frontend_core_InlineModel")
core_ModuleDefinition = Class(name="core_ModuleDefinition")
InlineClass = Class(name="InlineClass")
frontend_core_InlineClass = Class(name="frontend_core_InlineClass")
InlineFeature = Class(name="InlineFeature")
frontend_core_InlineFeature = Class(name="frontend_core_InlineFeature")
frontend_core_InlineAttribute = Class(name="frontend_core_InlineAttribute")
frontend_core_InlineReference = Class(name="frontend_core_InlineReference")
frontend_core_MatchTrace = Class(name="frontend_core_MatchTrace")
frontend_core_DoubleLiteral = Class(name="frontend_core_DoubleLiteral")
frontend_core_StringLiteral = Class(name="frontend_core_StringLiteral")
frontend_core_TraceCompareExpression = Class(name="frontend_core_TraceCompareExpression")
frontend_core_PutTrace = Class(name="frontend_core_PutTrace")
PutTraceParameter = Class(name="PutTraceParameter")
frontend_core_PutTraceParameter = Class(name="frontend_core_PutTraceParameter")
TraceCompareExpression = Class(name="TraceCompareExpression")

# frontend_DummyRootMetaclass class attributes and methods

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

# core_Variable class attributes and methods

# ClassUse class attributes and methods

# frontend_attribution_AttributionTransformation class attributes and methods

# AttributeDcl class attributes and methods

# AttributionRule class attributes and methods

# frontend_attribution_AttributeDcl class attributes and methods

# core_TypedWithClass class attributes and methods

# CompositeTransformation class attributes and methods

# frontend_attribution_InheritedAttributeDcl class attributes and methods

# frontend_attribution_SynthesizedAttributeDcl class attributes and methods

# frontend_attribution_AttributionRule class attributes and methods

# RuleSelf class attributes and methods

# Expression class attributes and methods

# frontend_attribution_RuleSelf class attributes and methods

# Variable class attributes and methods

# frontend_attribution_AttributeInit class attributes and methods

# frontend_attribution_AttributeUse class attributes and methods

# frontend_imperative_ImperativeTransformation class attributes and methods

# MethodDefinition class attributes and methods

# frontend_imperative_MethodDefinition class attributes and methods
frontend_imperative_MethodDefinition_name: Property = Property(name="name", type=StringType)
frontend_imperative_MethodDefinition.attributes={frontend_imperative_MethodDefinition_name}

# MethodParameter class attributes and methods

# MethodSelf class attributes and methods

# frontend_imperative_MethodSelf class attributes and methods

# frontend_imperative_MethodParameter class attributes and methods

# frontend_chain_ChainTransformation class attributes and methods

# ExternalTransformation class attributes and methods

# GeneratedModel class attributes and methods

# TransformationExecution class attributes and methods

# frontend_chain_GeneratedModel class attributes and methods

# core_RepresentModel class attributes and methods

# frontend_chain_TransformationExecution class attributes and methods

# AvailableTransformation class attributes and methods

# RepresentModel class attributes and methods

# frontend_chain_AvailableTransformation class attributes and methods

# frontend_chain_ExternalTransformation class attributes and methods

# chain_AvailableTransformation class attributes and methods

# frontend_chain_CompositeTransformation class attributes and methods

# core_TransformationDefinition class attributes and methods

# frontend_patterns_PatternSpecification class attributes and methods

# Pattern class attributes and methods

# frontend_patterns_Pattern class attributes and methods
frontend_patterns_Pattern_name: Property = Property(name="name", type=StringType)
frontend_patterns_Pattern.attributes={frontend_patterns_Pattern_name}

# PObject class attributes and methods

# POutputVariable class attributes and methods

# frontend_patterns_POutputVariable class attributes and methods

# frontend_patterns_PObject class attributes and methods

# PFeature class attributes and methods

# frontend_patterns_PFeature class attributes and methods
frontend_patterns_PFeature_name: Property = Property(name="name", type=StringType)
frontend_patterns_PFeature.attributes={frontend_patterns_PFeature_name}

# frontend_patterns_PAttribute class attributes and methods

# frontend_patterns_PReference class attributes and methods

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
frontend_mappings_Delegate_isExternal: Property = Property(name="isExternal", type=StringType)
frontend_mappings_Delegate_linkName: Property = Property(name="linkName", type=StringType)
frontend_mappings_Delegate_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_Delegate.attributes={frontend_mappings_Delegate_featureName, frontend_mappings_Delegate_isExternal, frontend_mappings_Delegate_linkName}

# MatchedElement class attributes and methods

# UseDeclaration class attributes and methods

# Tag class attributes and methods

# frontend_mappings_Context class attributes and methods

# MappingElement class attributes and methods

# C2CModifier class attributes and methods

# Section class attributes and methods

# frontend_mappings_Section class attributes and methods
frontend_mappings_Section_sectionType: Property = Property(name="sectionType", type=StringType)
frontend_mappings_Section.attributes={frontend_mappings_Section_sectionType}

# frontend_mappings_MappingElement class attributes and methods

# frontend_mappings_ClassMapping class attributes and methods

# frontend_mappings_Feature2Feature class attributes and methods

# FeatureRef class attributes and methods

# Converter class attributes and methods

# frontend_mappings_AttributeMapping class attributes and methods

# Feature2Feature class attributes and methods

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

# frontend_mappings_LinkedBy class attributes and methods

# frontend_mappings_EqualityFilter class attributes and methods
frontend_mappings_EqualityFilter_filter: Property = Property(name="filter", type=StringType)
frontend_mappings_EqualityFilter.attributes={frontend_mappings_EqualityFilter_filter}

# frontend_mappings_Operator class attributes and methods

# frontend_mappings_Split class attributes and methods

# Operator class attributes and methods

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
frontend_mappings_Reference2Reference.attributes={frontend_mappings_Reference2Reference_cardinality, frontend_mappings_Reference2Reference_resolverName}

# ReferenceRef class attributes and methods

# frontend_mappings_Modifier class attributes and methods

# frontend_mappings_AttributeModifier class attributes and methods

# Modifier class attributes and methods

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

# frontend_mappings_FeatureRef class attributes and methods
frontend_mappings_FeatureRef_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_FeatureRef_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_mappings_FeatureRef.attributes={frontend_mappings_FeatureRef_multivalued, frontend_mappings_FeatureRef_featureName}

# mappings_MetamodelElementRef class attributes and methods

# frontend_mappings_AttributeRef class attributes and methods
frontend_mappings_AttributeRef_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_AttributeRef_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_mappings_AttributeRef.attributes={frontend_mappings_AttributeRef_featureName, frontend_mappings_AttributeRef_multivalued}

# frontend_mappings_ReferenceRef class attributes and methods
frontend_mappings_ReferenceRef_featureName: Property = Property(name="featureName", type=StringType)
frontend_mappings_ReferenceRef_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_mappings_ReferenceRef.attributes={frontend_mappings_ReferenceRef_featureName, frontend_mappings_ReferenceRef_multivalued}

# frontend_qool_QoolTransformation class attributes and methods

# QoolQueue class attributes and methods

# Segment class attributes and methods

# frontend_qool_QoolQueue class attributes and methods

# QueueOptimization class attributes and methods

# frontend_qool_QueueOptimization class attributes and methods

# frontend_qool_AccessByFeatureOptimization class attributes and methods
frontend_qool_AccessByFeatureOptimization_featureName: Property = Property(name="featureName", type=StringType)
frontend_qool_AccessByFeatureOptimization_force: Property = Property(name="force", type=BooleanType)
frontend_qool_AccessByFeatureOptimization.attributes={frontend_qool_AccessByFeatureOptimization_force, frontend_qool_AccessByFeatureOptimization_featureName}

# frontend_qool_LocalQueue class attributes and methods

# TypeExpression class attributes and methods

# frontend_qool_ModelElementQueue class attributes and methods

# frontend_qool_Segment class attributes and methods

# frontend_qool_IteratorStatement class attributes and methods

# core_Statement class attributes and methods

# frontend_qool_ForAllStatement class attributes and methods

# IteratorStatement class attributes and methods

# frontend_qool_ForEachStatement class attributes and methods

# frontend_qool_EmitStatement class attributes and methods

# frontend_qool_MatchExpression class attributes and methods

# MatchPredicate class attributes and methods

# frontend_qool_MatchPredicate class attributes and methods

# frontend_qool_KindOfPredicate class attributes and methods

# frontend_qool_InvokeTransformation class attributes and methods
frontend_qool_InvokeTransformation_transformationName: Property = Property(name="transformationName", type=StringType)
frontend_qool_InvokeTransformation_entryPointName: Property = Property(name="entryPointName", type=StringType)
frontend_qool_InvokeTransformation.attributes={frontend_qool_InvokeTransformation_transformationName, frontend_qool_InvokeTransformation_entryPointName}

# InvocationParameter class attributes and methods

# NamedInvocationParameter class attributes and methods

# frontend_qool_InvokeExternal class attributes and methods
frontend_qool_InvokeExternal_queueName: Property = Property(name="queueName", type=StringType)
frontend_qool_InvokeExternal_traceAttributeName: Property = Property(name="traceAttributeName", type=StringType)
frontend_qool_InvokeExternal.attributes={frontend_qool_InvokeExternal_traceAttributeName, frontend_qool_InvokeExternal_queueName}

# InvokeTransformation class attributes and methods

# frontend_qool_InvokeInternal class attributes and methods

# frontend_qool_InvocationParameter class attributes and methods
frontend_qool_InvocationParameter_calleeModelName: Property = Property(name="calleeModelName", type=StringType)
frontend_qool_InvocationParameter.attributes={frontend_qool_InvocationParameter_calleeModelName}

# TransformationDefinitionParameter class attributes and methods

# frontend_qool_NamedInvocationParameter class attributes and methods
frontend_qool_NamedInvocationParameter_formalName: Property = Property(name="formalName", type=StringType)
frontend_qool_NamedInvocationParameter.attributes={frontend_qool_NamedInvocationParameter_formalName}

# frontend_facilities_Copier class attributes and methods

# frontend_qool_PropertyEqualsPredicate class attributes and methods
frontend_qool_PropertyEqualsPredicate_propertyName: Property = Property(name="propertyName", type=StringType)
frontend_qool_PropertyEqualsPredicate.attributes={frontend_qool_PropertyEqualsPredicate_propertyName}

# frontend_facilities_CopierCallbackDefinition class attributes and methods
frontend_facilities_CopierCallbackDefinition_stop: Property = Property(name="stop", type=BooleanType)
frontend_facilities_CopierCallbackDefinition.attributes={frontend_facilities_CopierCallbackDefinition_stop}

# frontend_tao_TaoTransformation class attributes and methods

# Template class attributes and methods

# frontend_tao_TemplateParameter class attributes and methods

# frontend_tao_ObjectInstantiation class attributes and methods

# Assignment class attributes and methods

# frontend_tao_TemplateRootObject class attributes and methods

# ObjectInstantiation class attributes and methods

# frontend_tao_Template class attributes and methods

# TemplateParameter class attributes and methods

# TemplateRootObject class attributes and methods

# frontend_tao_Assignment class attributes and methods

# frontend_tao_AttributeAssigment class attributes and methods
frontend_tao_AttributeAssigment_targetFeature: Property = Property(name="targetFeature", type=StringType)
frontend_tao_AttributeAssigment.attributes={frontend_tao_AttributeAssigment_targetFeature}

# SourceExpression class attributes and methods

# frontend_tao_SourceExpression class attributes and methods

# frontend_tao_WithOptionalVariableExpression class attributes and methods

# ObjectSourceVariable class attributes and methods

# facilities_CopierCallbackDefinition class attributes and methods

# frontend_tao_ObjectSourceVariable class attributes and methods

# frontend_tao_ReferenceAssignment class attributes and methods
frontend_tao_ReferenceAssignment_targetFeature: Property = Property(name="targetFeature", type=StringType)
frontend_tao_ReferenceAssignment_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_tao_ReferenceAssignment.attributes={frontend_tao_ReferenceAssignment_multivalued, frontend_tao_ReferenceAssignment_targetFeature}

# tao_Assignment class attributes and methods

# frontend_tao_ObjectSyntax class attributes and methods

# ReferenceAssignment class attributes and methods

# frontend_tao_Invocation class attributes and methods

# frontend_core_LocatedElement class attributes and methods
frontend_core_LocatedElement_row: Property = Property(name="row", type=IntegerType)
frontend_core_LocatedElement_column: Property = Property(name="column", type=IntegerType)
frontend_core_LocatedElement_file: Property = Property(name="file", type=StringType)
frontend_core_LocatedElement.attributes={frontend_core_LocatedElement_row, frontend_core_LocatedElement_column, frontend_core_LocatedElement_file}

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

# ImportedModel class attributes and methods

# InlineModel class attributes and methods

# RequireDeclaration class attributes and methods

# frontend_core_EclecticTransformationDefinition class attributes and methods

# frontend_core_ImportedModel class attributes and methods

# frontend_core_UseDeclaration class attributes and methods
frontend_core_UseDeclaration_module: Property = Property(name="module", type=StringType)
frontend_core_UseDeclaration_as_: Property = Property(name="as_", type=StringType)
frontend_core_UseDeclaration.attributes={frontend_core_UseDeclaration_as_, frontend_core_UseDeclaration_module}

# frontend_core_RequireDeclaration class attributes and methods
frontend_core_RequireDeclaration_name: Property = Property(name="name", type=StringType)
frontend_core_RequireDeclaration_default: Property = Property(name="default", type=StringType)
frontend_core_RequireDeclaration.attributes={frontend_core_RequireDeclaration_name, frontend_core_RequireDeclaration_default}

# RequireParameter class attributes and methods

# frontend_core_RequireParameter class attributes and methods
frontend_core_RequireParameter_formalParameterName: Property = Property(name="formalParameterName", type=StringType)
frontend_core_RequireParameter.attributes={frontend_core_RequireParameter_formalParameterName}

# frontend_core_RequireModelParameter class attributes and methods

# frontend_core_Variable class attributes and methods
frontend_core_Variable_name: Property = Property(name="name", type=StringType)
frontend_core_Variable.attributes={frontend_core_Variable_name}

# frontend_core_Statement class attributes and methods

# frontend_core_Expression class attributes and methods

# frontend_core_DefineVariable class attributes and methods

# frontend_core_PropertyWrite class attributes and methods
frontend_core_PropertyWrite__property: Property = Property(name="_property", type=StringType)
frontend_core_PropertyWrite.attributes={frontend_core_PropertyWrite__property}

# frontend_core_TransformationDefinitionParameter class attributes and methods

# core_DefinitionParameter class attributes and methods

# frontend_core_ModelReference class attributes and methods

# core_Expression class attributes and methods

# frontend_core_VariableReference class attributes and methods

# frontend_core_MethodCall class attributes and methods
frontend_core_MethodCall_methodName: Property = Property(name="methodName", type=StringType)
frontend_core_MethodCall_withParameters: Property = Property(name="withParameters", type=BooleanType)
frontend_core_MethodCall.attributes={frontend_core_MethodCall_methodName, frontend_core_MethodCall_withParameters}

# frontend_core_KeywordMethodCall class attributes and methods

# KeywordParameter class attributes and methods

# frontend_core_KeywordParameter class attributes and methods
frontend_core_KeywordParameter_keyword: Property = Property(name="keyword", type=StringType)
frontend_core_KeywordParameter.attributes={frontend_core_KeywordParameter_keyword}

# frontend_core_BinaryExpr class attributes and methods
frontend_core_BinaryExpr_binaryOp: Property = Property(name="binaryOp", type=StringType)
frontend_core_BinaryExpr.attributes={frontend_core_BinaryExpr_binaryOp}

# frontend_core_ClosureDeclaration class attributes and methods

# ClosureParameter class attributes and methods

# frontend_core_ClosureParameter class attributes and methods

# frontend_core_ResolveLink class attributes and methods
frontend_core_ResolveLink_isExternal: Property = Property(name="isExternal", type=StringType)
frontend_core_ResolveLink_linkName: Property = Property(name="linkName", type=StringType)
frontend_core_ResolveLink_featureName: Property = Property(name="featureName", type=StringType)
frontend_core_ResolveLink.attributes={frontend_core_ResolveLink_isExternal, frontend_core_ResolveLink_featureName, frontend_core_ResolveLink_linkName}

# frontend_core_IfExpr class attributes and methods

# IfBranch class attributes and methods

# frontend_core_IfBranch class attributes and methods

# frontend_core_NumLiteral class attributes and methods
frontend_core_NumLiteral_value: Property = Property(name="value", type=IntegerType)
frontend_core_NumLiteral.attributes={frontend_core_NumLiteral_value}

# frontend_core_BooleanLiteral class attributes and methods
frontend_core_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
frontend_core_BooleanLiteral.attributes={frontend_core_BooleanLiteral_value}

# frontend_core_TypeExpression class attributes and methods

# frontend_core_ClassUse class attributes and methods
frontend_core_ClassUse_className: Property = Property(name="className", type=StringType)
frontend_core_ClassUse_strictType: Property = Property(name="strictType", type=BooleanType)
frontend_core_ClassUse.attributes={frontend_core_ClassUse_strictType, frontend_core_ClassUse_className}

# core_TypeExpression class attributes and methods

# core_ImplicitlyAnnotableElement class attributes and methods

# frontend_core_TraceUse class attributes and methods

# TraceDefinition class attributes and methods

# frontend_core_TypedWithClass class attributes and methods

# frontend_core_TraceInterface class attributes and methods

# frontend_core_TracedModelParameter class attributes and methods

# frontend_core_TraceDefinition class attributes and methods

# TraceElement class attributes and methods

# frontend_core_TraceElement class attributes and methods

# frontend_core_InlineModel class attributes and methods

# core_ModuleDefinition class attributes and methods

# InlineClass class attributes and methods

# frontend_core_InlineClass class attributes and methods

# InlineFeature class attributes and methods

# frontend_core_InlineFeature class attributes and methods
frontend_core_InlineFeature_multivalued: Property = Property(name="multivalued", type=BooleanType)
frontend_core_InlineFeature.attributes={frontend_core_InlineFeature_multivalued}

# frontend_core_InlineAttribute class attributes and methods

# frontend_core_InlineReference class attributes and methods

# frontend_core_MatchTrace class attributes and methods
frontend_core_MatchTrace_cardinality: Property = Property(name="cardinality", type=StringType)
frontend_core_MatchTrace.attributes={frontend_core_MatchTrace_cardinality}

# frontend_core_DoubleLiteral class attributes and methods
frontend_core_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
frontend_core_DoubleLiteral.attributes={frontend_core_DoubleLiteral_value}

# frontend_core_StringLiteral class attributes and methods
frontend_core_StringLiteral_value: Property = Property(name="value", type=StringType)
frontend_core_StringLiteral.attributes={frontend_core_StringLiteral_value}

# frontend_core_TraceCompareExpression class attributes and methods
frontend_core_TraceCompareExpression_multivaluedTag: Property = Property(name="multivaluedTag", type=BooleanType)
frontend_core_TraceCompareExpression.attributes={frontend_core_TraceCompareExpression_multivaluedTag}

# frontend_core_PutTrace class attributes and methods

# PutTraceParameter class attributes and methods

# frontend_core_PutTraceParameter class attributes and methods

# TraceCompareExpression class attributes and methods

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
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="ClassUse", type=frontend_koan_ForAllMatcher, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_koan_ForAllMatcher", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
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
composites46: BinaryAssociation = BinaryAssociation(
    name="composites46",
    ends={
        Property(name="CompositeTransformation", type=frontend_chain_ChainTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_ChainTransformation", type=CompositeTransformation, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
condition18: BinaryAssociation = BinaryAssociation(
    name="condition18",
    ends={
        Property(name="Expression", type=frontend_attribution_AttributionRule, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_attribution_AttributionRule19", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
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
executions51: BinaryAssociation = BinaryAssociation(
    name="executions51",
    ends={
        Property(name="TransformationExecution", type=frontend_chain_ChainTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_chain_ChainTransformation52", type=TransformationExecution, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
objects62: BinaryAssociation = BinaryAssociation(
    name="objects62",
    ends={
        Property(name="PObject", type=frontend_patterns_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_patterns_Pattern", type=PObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="MatchedElement", type=frontend_mappings_Delegate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Delegate", type=MatchedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="Attribute2Attribute", type=frontend_mappings_Class2Class, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=Attribute2Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute118: BinaryAssociation = BinaryAssociation(
    name="attribute118",
    ends={
        Property(name="AttributeRef119", type=frontend_mappings_RelatedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_RelatedBy", type=AttributeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
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
        Property(name="Class2Class", type=frontend_mappings_Attribute2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="scopedAttributes", type=Class2Class, multiplicity=Multiplicity(0, 1))
    }
)
right131: BinaryAssociation = BinaryAssociation(
    name="right131",
    ends={
        Property(name="AttributeRef132", type=frontend_mappings_Attribute2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Attribute2Attribute", type=AttributeRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modifiers133: BinaryAssociation = BinaryAssociation(
    name="modifiers133",
    ends={
        Property(name="AttributeModifier", type=frontend_mappings_Attribute2Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Attribute2Attribute134", type=AttributeModifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left135: BinaryAssociation = BinaryAssociation(
    name="left135",
    ends={
        Property(name="ReferenceRef", type=frontend_mappings_Reference2Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Reference2Reference", type=ReferenceRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right136: BinaryAssociation = BinaryAssociation(
    name="right136",
    ends={
        Property(name="ReferenceRef138", type=frontend_mappings_Reference2Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_Reference2Reference137", type=ReferenceRef, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
klass139: BinaryAssociation = BinaryAssociation(
    name="klass139",
    ends={
        Property(name="ClassUse140", type=frontend_mappings_ClassRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_ClassRef", type=ClassUse, multiplicity=Multiplicity(1, 1))
    }
)
referredElement141: BinaryAssociation = BinaryAssociation(
    name="referredElement141",
    ends={
        Property(name="MatchedElement142", type=frontend_mappings_FeatureRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_FeatureRef", type=MatchedElement, multiplicity=Multiplicity(1, 1))
    }
)
referredElement143: BinaryAssociation = BinaryAssociation(
    name="referredElement143",
    ends={
        Property(name="MatchedElement144", type=frontend_mappings_AttributeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_AttributeRef", type=MatchedElement, multiplicity=Multiplicity(1, 1))
    }
)
referredElement145: BinaryAssociation = BinaryAssociation(
    name="referredElement145",
    ends={
        Property(name="MatchedElement146", type=frontend_mappings_ReferenceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_mappings_ReferenceRef", type=MatchedElement, multiplicity=Multiplicity(1, 1))
    }
)
queues147: BinaryAssociation = BinaryAssociation(
    name="queues147",
    ends={
        Property(name="QoolQueue", type=frontend_qool_QoolTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_QoolTransformation", type=QoolQueue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segments148: BinaryAssociation = BinaryAssociation(
    name="segments148",
    ends={
        Property(name="Segment", type=frontend_qool_QoolTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_QoolTransformation149", type=Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optimizations150: BinaryAssociation = BinaryAssociation(
    name="optimizations150",
    ends={
        Property(name="QueueOptimization", type=frontend_qool_QoolQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_QoolQueue", type=QueueOptimization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_151: BinaryAssociation = BinaryAssociation(
    name="type_151",
    ends={
        Property(name="TypeExpression", type=frontend_qool_LocalQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_LocalQueue", type=TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
class_152: BinaryAssociation = BinaryAssociation(
    name="class_152",
    ends={
        Property(name="frontend_qool_ModelElementQueue", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ClassUse153", type=frontend_qool_ModelElementQueue, multiplicity=Multiplicity(1, 1))
    }
)
additionals154: BinaryAssociation = BinaryAssociation(
    name="additionals154",
    ends={
        Property(name="ClassUse156", type=frontend_qool_ModelElementQueue, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_ModelElementQueue155", type=ClassUse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements157: BinaryAssociation = BinaryAssociation(
    name="statements157",
    ends={
        Property(name="Statement158", type=frontend_qool_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_Segment", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition159: BinaryAssociation = BinaryAssociation(
    name="condition159",
    ends={
        Property(name="Expression160", type=frontend_qool_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_IteratorStatement", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements161: BinaryAssociation = BinaryAssociation(
    name="statements161",
    ends={
        Property(name="Statement163", type=frontend_qool_IteratorStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_IteratorStatement162", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queue164: BinaryAssociation = BinaryAssociation(
    name="queue164",
    ends={
        Property(name="QoolQueue165", type=frontend_qool_ForAllStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_ForAllStatement", type=QoolQueue, multiplicity=Multiplicity(1, 1))
    }
)
collection166: BinaryAssociation = BinaryAssociation(
    name="collection166",
    ends={
        Property(name="Expression167", type=frontend_qool_ForEachStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_ForEachStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queue168: BinaryAssociation = BinaryAssociation(
    name="queue168",
    ends={
        Property(name="QoolQueue169", type=frontend_qool_EmitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_EmitStatement", type=QoolQueue, multiplicity=Multiplicity(1, 1))
    }
)
value170: BinaryAssociation = BinaryAssociation(
    name="value170",
    ends={
        Property(name="Expression172", type=frontend_qool_EmitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_EmitStatement171", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queue173: BinaryAssociation = BinaryAssociation(
    name="queue173",
    ends={
        Property(name="QoolQueue174", type=frontend_qool_MatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_MatchExpression", type=QoolQueue, multiplicity=Multiplicity(1, 1))
    }
)
predicates175: BinaryAssociation = BinaryAssociation(
    name="predicates175",
    ends={
        Property(name="MatchPredicate", type=frontend_qool_MatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_MatchExpression176", type=MatchPredicate, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value179: BinaryAssociation = BinaryAssociation(
    name="value179",
    ends={
        Property(name="Expression180", type=frontend_qool_PropertyEqualsPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_PropertyEqualsPredicate", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceModels181: BinaryAssociation = BinaryAssociation(
    name="sourceModels181",
    ends={
        Property(name="InvocationParameter", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation", type=InvocationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetModels182: BinaryAssociation = BinaryAssociation(
    name="targetModels182",
    ends={
        Property(name="InvocationParameter184", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation183", type=InvocationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters185: BinaryAssociation = BinaryAssociation(
    name="parameters185",
    ends={
        Property(name="NamedInvocationParameter", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation186", type=NamedInvocationParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputViewFilter187: BinaryAssociation = BinaryAssociation(
    name="inputViewFilter187",
    ends={
        Property(name="Variable189", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation188", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
entryPointParameters190: BinaryAssociation = BinaryAssociation(
    name="entryPointParameters190",
    ends={
        Property(name="Expression192", type=frontend_qool_InvokeTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeTransformation191", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputResolutionSourceElement193: BinaryAssociation = BinaryAssociation(
    name="outputResolutionSourceElement193",
    ends={
        Property(name="Expression194", type=frontend_qool_InvokeExternal, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvokeExternal", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model195: BinaryAssociation = BinaryAssociation(
    name="model195",
    ends={
        Property(name="TransformationDefinitionParameter", type=frontend_qool_InvocationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_InvocationParameter", type=TransformationDefinitionParameter, multiplicity=Multiplicity(1, 1))
    }
)
actualParameter196: BinaryAssociation = BinaryAssociation(
    name="actualParameter196",
    ends={
        Property(name="Expression197", type=frontend_qool_NamedInvocationParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_NamedInvocationParameter", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objects198: BinaryAssociation = BinaryAssociation(
    name="objects198",
    ends={
        Property(name="Expression199", type=frontend_facilities_Copier, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_Copier", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_177: BinaryAssociation = BinaryAssociation(
    name="class_177",
    ends={
        Property(name="ClassUse178", type=frontend_qool_KindOfPredicate, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_qool_KindOfPredicate", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trigger205: BinaryAssociation = BinaryAssociation(
    name="trigger205",
    ends={
        Property(name="Expression206", type=frontend_facilities_CopierCallbackDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_CopierCallbackDefinition", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action207: BinaryAssociation = BinaryAssociation(
    name="action207",
    ends={
        Property(name="Expression209", type=frontend_facilities_CopierCallbackDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_CopierCallbackDefinition208", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
templates210: BinaryAssociation = BinaryAssociation(
    name="templates210",
    ends={
        Property(name="Template", type=frontend_tao_TaoTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_TaoTransformation", type=Template, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type211: BinaryAssociation = BinaryAssociation(
    name="type211",
    ends={
        Property(name="ClassUse212", type=frontend_tao_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_TemplateParameter", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type213: BinaryAssociation = BinaryAssociation(
    name="type213",
    ends={
        Property(name="ClassUse214", type=frontend_tao_ObjectInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ObjectInstantiation", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assigments215: BinaryAssociation = BinaryAssociation(
    name="assigments215",
    ends={
        Property(name="Assignment", type=frontend_tao_ObjectInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ObjectInstantiation216", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters217: BinaryAssociation = BinaryAssociation(
    name="parameters217",
    ends={
        Property(name="TemplateParameter", type=frontend_tao_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_Template", type=TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roots218: BinaryAssociation = BinaryAssociation(
    name="roots218",
    ends={
        Property(name="TemplateRootObject", type=frontend_tao_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_Template219", type=TemplateRootObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr220: BinaryAssociation = BinaryAssociation(
    name="expr220",
    ends={
        Property(name="SourceExpression", type=frontend_tao_AttributeAssigment, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_AttributeAssigment", type=SourceExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable221: BinaryAssociation = BinaryAssociation(
    name="variable221",
    ends={
        Property(name="ObjectSourceVariable", type=frontend_tao_WithOptionalVariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_WithOptionalVariableExpression", type=ObjectSourceVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr222: BinaryAssociation = BinaryAssociation(
    name="expr222",
    ends={
        Property(name="Expression224", type=frontend_tao_WithOptionalVariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_WithOptionalVariableExpression223", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
callbacks200: BinaryAssociation = BinaryAssociation(
    name="callbacks200",
    ends={
        Property(name="facilities_CopierCallbackDefinition", type=frontend_facilities_Copier, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_Copier201", type=facilities_CopierCallbackDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
copyInModel202: BinaryAssociation = BinaryAssociation(
    name="copyInModel202",
    ends={
        Property(name="TransformationDefinitionParameter204", type=frontend_facilities_Copier, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_facilities_Copier203", type=TransformationDefinitionParameter, multiplicity=Multiplicity(1, 1))
    }
)
expr225: BinaryAssociation = BinaryAssociation(
    name="expr225",
    ends={
        Property(name="SourceExpression226", type=frontend_tao_ReferenceAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ReferenceAssignment", type=SourceExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object227: BinaryAssociation = BinaryAssociation(
    name="object227",
    ends={
        Property(name="ObjectInstantiation", type=frontend_tao_ObjectSyntax, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_ObjectSyntax", type=ObjectInstantiation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
template228: BinaryAssociation = BinaryAssociation(
    name="template228",
    ends={
        Property(name="Template229", type=frontend_tao_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_tao_Invocation", type=Template, multiplicity=Multiplicity(1, 1))
    }
)
annotatedWith230: BinaryAssociation = BinaryAssociation(
    name="annotatedWith230",
    ends={
        Property(name="Annotation", type=frontend_core_AnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedElement", type=Annotation, multiplicity=Multiplicity(0, 9999))
    }
)
annotations231: BinaryAssociation = BinaryAssociation(
    name="annotations231",
    ends={
        Property(name="SingleAnnotation", type=frontend_core_ImplicitlyAnnotableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ImplicitlyAnnotableElement", type=SingleAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement232: BinaryAssociation = BinaryAssociation(
    name="annotatedElement232",
    ends={
        Property(name="AnnotableElement", type=frontend_core_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedWith", type=AnnotableElement, multiplicity=Multiplicity(0, 1))
    }
)
parameters233: BinaryAssociation = BinaryAssociation(
    name="parameters233",
    ends={
        Property(name="AnnotationParameter", type=frontend_core_GenericAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_GenericAnnotation", type=AnnotationParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inModels234: BinaryAssociation = BinaryAssociation(
    name="inModels234",
    ends={
        Property(name="TransformationDefinitionParameter235", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition", type=TransformationDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outModels236: BinaryAssociation = BinaryAssociation(
    name="outModels236",
    ends={
        Property(name="TransformationDefinitionParameter238", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition237", type=TransformationDefinitionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedModels239: BinaryAssociation = BinaryAssociation(
    name="importedModels239",
    ends={
        Property(name="ImportedModel", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition240", type=ImportedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inlineModels241: BinaryAssociation = BinaryAssociation(
    name="inlineModels241",
    ends={
        Property(name="InlineModel", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition242", type=InlineModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations243: BinaryAssociation = BinaryAssociation(
    name="annotations243",
    ends={
        Property(name="Annotation245", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition244", type=Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses246: BinaryAssociation = BinaryAssociation(
    name="uses246",
    ends={
        Property(name="UseDeclaration248", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition247", type=UseDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requires249: BinaryAssociation = BinaryAssociation(
    name="requires249",
    ends={
        Property(name="RequireDeclaration", type=frontend_core_TransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TransformationDefinition250", type=RequireDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters252: BinaryAssociation = BinaryAssociation(
    name="parameters252",
    ends={
        Property(name="RequireParameter", type=frontend_core_RequireDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_RequireDeclaration", type=RequireParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model253: BinaryAssociation = BinaryAssociation(
    name="model253",
    ends={
        Property(name="RepresentModel254", type=frontend_core_RequireModelParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_RequireModelParameter", type=RepresentModel, multiplicity=Multiplicity(1, 1))
    }
)
expression255: BinaryAssociation = BinaryAssociation(
    name="expression255",
    ends={
        Property(name="Expression256", type=frontend_core_DefineVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_DefineVariable", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
transformations251: BinaryAssociation = BinaryAssociation(
    name="transformations251",
    ends={
        Property(name="TransformationDefinition", type=frontend_core_EclecticTransformationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_EclecticTransformationDefinition", type=TransformationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression259: BinaryAssociation = BinaryAssociation(
    name="expression259",
    ends={
        Property(name="Expression261", type=frontend_core_PropertyWrite, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PropertyWrite260", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable262: BinaryAssociation = BinaryAssociation(
    name="variable262",
    ends={
        Property(name="Variable263", type=frontend_core_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_VariableReference", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
receptor264: BinaryAssociation = BinaryAssociation(
    name="receptor264",
    ends={
        Property(name="Expression265", type=frontend_core_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_MethodCall", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters266: BinaryAssociation = BinaryAssociation(
    name="parameters266",
    ends={
        Property(name="Expression268", type=frontend_core_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_MethodCall267", type=Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receptor269: BinaryAssociation = BinaryAssociation(
    name="receptor269",
    ends={
        Property(name="Expression270", type=frontend_core_KeywordMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_KeywordMethodCall", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters271: BinaryAssociation = BinaryAssociation(
    name="parameters271",
    ends={
        Property(name="KeywordParameter", type=frontend_core_KeywordMethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_KeywordMethodCall272", type=KeywordParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value273: BinaryAssociation = BinaryAssociation(
    name="value273",
    ends={
        Property(name="Expression274", type=frontend_core_KeywordParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_KeywordParameter", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left275: BinaryAssociation = BinaryAssociation(
    name="left275",
    ends={
        Property(name="Expression276", type=frontend_core_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_BinaryExpr", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receptor257: BinaryAssociation = BinaryAssociation(
    name="receptor257",
    ends={
        Property(name="Variable258", type=frontend_core_PropertyWrite, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PropertyWrite", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
statements280: BinaryAssociation = BinaryAssociation(
    name="statements280",
    ends={
        Property(name="Statement281", type=frontend_core_ClosureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ClosureDeclaration", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameters282: BinaryAssociation = BinaryAssociation(
    name="formalParameters282",
    ends={
        Property(name="ClosureParameter", type=frontend_core_ClosureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ClosureDeclaration283", type=ClosureParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr284: BinaryAssociation = BinaryAssociation(
    name="expr284",
    ends={
        Property(name="Expression285", type=frontend_core_ResolveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ResolveLink", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
module286: BinaryAssociation = BinaryAssociation(
    name="module286",
    ends={
        Property(name="UseDeclaration288", type=frontend_core_ResolveLink, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ResolveLink287", type=UseDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
then289: BinaryAssociation = BinaryAssociation(
    name="then289",
    ends={
        Property(name="IfBranch", type=frontend_core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfExpr", type=IfBranch, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsifs290: BinaryAssociation = BinaryAssociation(
    name="elsifs290",
    ends={
        Property(name="IfBranch292", type=frontend_core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfExpr291", type=IfBranch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else_293: BinaryAssociation = BinaryAssociation(
    name="else_293",
    ends={
        Property(name="IfBranch295", type=frontend_core_IfExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfExpr294", type=IfBranch, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition296: BinaryAssociation = BinaryAssociation(
    name="condition296",
    ends={
        Property(name="Expression297", type=frontend_core_IfBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfBranch", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements298: BinaryAssociation = BinaryAssociation(
    name="statements298",
    ends={
        Property(name="Statement300", type=frontend_core_IfBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_IfBranch299", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right277: BinaryAssociation = BinaryAssociation(
    name="right277",
    ends={
        Property(name="Expression279", type=frontend_core_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_BinaryExpr278", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model301: BinaryAssociation = BinaryAssociation(
    name="model301",
    ends={
        Property(name="RepresentModel302", type=frontend_core_ClassUse, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_ClassUse", type=RepresentModel, multiplicity=Multiplicity(1, 1))
    }
)
trace303: BinaryAssociation = BinaryAssociation(
    name="trace303",
    ends={
        Property(name="TraceDefinition", type=frontend_core_TraceUse, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceUse", type=TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
type_304: BinaryAssociation = BinaryAssociation(
    name="type_304",
    ends={
        Property(name="ClassUse305", type=frontend_core_TypedWithClass, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TypedWithClass", type=ClassUse, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definitions306: BinaryAssociation = BinaryAssociation(
    name="definitions306",
    ends={
        Property(name="TraceDefinition307", type=frontend_core_TraceInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceInterface", type=TraceDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements308: BinaryAssociation = BinaryAssociation(
    name="elements308",
    ends={
        Property(name="TraceElement", type=frontend_core_TraceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceDefinition", type=TraceElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type309: BinaryAssociation = BinaryAssociation(
    name="type309",
    ends={
        Property(name="TypeExpression310", type=frontend_core_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceElement", type=TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classes311: BinaryAssociation = BinaryAssociation(
    name="classes311",
    ends={
        Property(name="InlineClass", type=frontend_core_InlineModel, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_InlineModel", type=InlineClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features312: BinaryAssociation = BinaryAssociation(
    name="features312",
    ends={
        Property(name="InlineFeature", type=frontend_core_InlineClass, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_InlineClass", type=InlineFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type313: BinaryAssociation = BinaryAssociation(
    name="type313",
    ends={
        Property(name="TypeExpression314", type=frontend_core_InlineFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_InlineFeature", type=TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
traceExpr317: BinaryAssociation = BinaryAssociation(
    name="traceExpr317",
    ends={
        Property(name="frontend_core_MatchTrace318", type=TraceCompareExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="TraceCompareExpression", type=frontend_core_MatchTrace, multiplicity=Multiplicity(1, 1))
    }
)
traceVar319: BinaryAssociation = BinaryAssociation(
    name="traceVar319",
    ends={
        Property(name="TraceElement320", type=frontend_core_TraceCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceCompareExpression", type=TraceElement, multiplicity=Multiplicity(1, 1))
    }
)
expr321: BinaryAssociation = BinaryAssociation(
    name="expr321",
    ends={
        Property(name="Expression323", type=frontend_core_TraceCompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_TraceCompareExpression322", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trace324: BinaryAssociation = BinaryAssociation(
    name="trace324",
    ends={
        Property(name="TraceDefinition325", type=frontend_core_PutTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTrace", type=TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)
parameters326: BinaryAssociation = BinaryAssociation(
    name="parameters326",
    ends={
        Property(name="PutTraceParameter", type=frontend_core_PutTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTrace327", type=PutTraceParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value328: BinaryAssociation = BinaryAssociation(
    name="value328",
    ends={
        Property(name="Expression329", type=frontend_core_PutTraceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTraceParameter", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
traceVar330: BinaryAssociation = BinaryAssociation(
    name="traceVar330",
    ends={
        Property(name="TraceElement332", type=frontend_core_PutTraceParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_PutTraceParameter331", type=TraceElement, multiplicity=Multiplicity(1, 1))
    }
)
trace315: BinaryAssociation = BinaryAssociation(
    name="trace315",
    ends={
        Property(name="TraceDefinition316", type=frontend_core_MatchTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="frontend_core_MatchTrace", type=TraceDefinition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_frontend_script_ScriptedTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_script_ScriptedTransformation)
gen_frontend_attribution_AttributeDcl_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_attribution_AttributeDcl)
gen_frontend_koan_KoanTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_koan_KoanTransformation)
gen_frontend_koan_KoanRule_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_koan_KoanRule)
gen_frontend_koan_KoanRule_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_koan_KoanRule)
gen_frontend_koan_Matcher_LocatedElement = Generalization(general=LocatedElement, specific=frontend_koan_Matcher)
gen_frontend_koan_ForAllMatcher_koan_Matcher = Generalization(general=koan_Matcher, specific=frontend_koan_ForAllMatcher)
gen_frontend_koan_ForAllMatcher_core_Variable = Generalization(general=core_Variable, specific=frontend_koan_ForAllMatcher)
gen_frontend_attribution_AttributionTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_attribution_AttributionTransformation)
gen_frontend_attribution_AttributeDcl_core_Variable = Generalization(general=core_Variable, specific=frontend_attribution_AttributeDcl)
gen_frontend_attribution_AttributeDcl_core_TypedWithClass = Generalization(general=core_TypedWithClass, specific=frontend_attribution_AttributeDcl)
gen_frontend_attribution_InheritedAttributeDcl_AttributeDcl = Generalization(general=AttributeDcl, specific=frontend_attribution_InheritedAttributeDcl)
gen_frontend_attribution_SynthesizedAttributeDcl_AttributeDcl = Generalization(general=AttributeDcl, specific=frontend_attribution_SynthesizedAttributeDcl)
gen_frontend_attribution_AttributionRule_LocatedElement = Generalization(general=LocatedElement, specific=frontend_attribution_AttributionRule)
gen_frontend_attribution_RuleSelf_Variable = Generalization(general=Variable, specific=frontend_attribution_RuleSelf)
gen_frontend_attribution_AttributeInit_Statement = Generalization(general=Statement, specific=frontend_attribution_AttributeInit)
gen_frontend_attribution_AttributeUse_Expression = Generalization(general=Expression, specific=frontend_attribution_AttributeUse)
gen_frontend_imperative_ImperativeTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_imperative_ImperativeTransformation)
gen_frontend_imperative_MethodDefinition_LocatedElement = Generalization(general=LocatedElement, specific=frontend_imperative_MethodDefinition)
gen_frontend_imperative_MethodSelf_Variable = Generalization(general=Variable, specific=frontend_imperative_MethodSelf)
gen_frontend_imperative_MethodParameter_Variable = Generalization(general=Variable, specific=frontend_imperative_MethodParameter)
gen_frontend_chain_ChainTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_chain_ChainTransformation)
gen_frontend_chain_GeneratedModel_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_chain_GeneratedModel)
gen_frontend_chain_GeneratedModel_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_chain_GeneratedModel)
gen_frontend_chain_TransformationExecution_LocatedElement = Generalization(general=LocatedElement, specific=frontend_chain_TransformationExecution)
gen_frontend_chain_ExternalTransformation_chain_AvailableTransformation = Generalization(general=chain_AvailableTransformation, specific=frontend_chain_ExternalTransformation)
gen_frontend_chain_ExternalTransformation_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_chain_ExternalTransformation)
gen_frontend_chain_CompositeTransformation_chain_AvailableTransformation = Generalization(general=chain_AvailableTransformation, specific=frontend_chain_CompositeTransformation)
gen_frontend_chain_CompositeTransformation_core_TransformationDefinition = Generalization(general=core_TransformationDefinition, specific=frontend_chain_CompositeTransformation)
gen_frontend_patterns_PatternSpecification_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_patterns_PatternSpecification)
gen_frontend_patterns_Pattern_LocatedElement = Generalization(general=LocatedElement, specific=frontend_patterns_Pattern)
gen_frontend_patterns_PObject_core_Variable = Generalization(general=core_Variable, specific=frontend_patterns_PObject)
gen_frontend_patterns_PObject_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_patterns_PObject)
gen_frontend_patterns_PFeature_LocatedElement = Generalization(general=LocatedElement, specific=frontend_patterns_PFeature)
gen_frontend_patterns_PAttribute_PFeature = Generalization(general=PFeature, specific=frontend_patterns_PAttribute)
gen_frontend_patterns_PReference_PFeature = Generalization(general=PFeature, specific=frontend_patterns_PReference)
gen_frontend_patterns_CollectionReference_PReference = Generalization(general=PReference, specific=frontend_patterns_CollectionReference)
gen_frontend_mappings_MappingTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_mappings_MappingTransformation)
gen_frontend_mappings_MappingVariable_Variable = Generalization(general=Variable, specific=frontend_mappings_MappingVariable)
gen_frontend_mappings_MatchedElement_core_ClassUse = Generalization(general=core_ClassUse, specific=frontend_mappings_MatchedElement)
gen_frontend_mappings_MatchedElement_mappings_MappingVariable = Generalization(general=mappings_MappingVariable, specific=frontend_mappings_MatchedElement)
gen_frontend_mappings_Delegate_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Delegate)
gen_frontend_mappings_Context_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Context)
gen_frontend_mappings_Section_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Section)
gen_frontend_mappings_MappingElement_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_MappingElement)
gen_frontend_mappings_ClassMapping_MappingElement = Generalization(general=MappingElement, specific=frontend_mappings_ClassMapping)
gen_frontend_mappings_Feature2Feature_MappingElement = Generalization(general=MappingElement, specific=frontend_mappings_Feature2Feature)
gen_frontend_mappings_AttributeMapping_Feature2Feature = Generalization(general=Feature2Feature, specific=frontend_mappings_AttributeMapping)
gen_frontend_mappings_AttributeIsString_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsString)
gen_frontend_mappings_AttributeIsBoolean_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsBoolean)
gen_frontend_mappings_AttributeIsDouble_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsDouble)
gen_frontend_mappings_AttributeIsResolveLink_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsResolveLink)
gen_frontend_mappings_AttributeIsInteger_AttributeRightPart = Generalization(general=AttributeRightPart, specific=frontend_mappings_AttributeIsInteger)
gen_frontend_mappings_Tag_NamedElement = Generalization(general=NamedElement, specific=frontend_mappings_Tag)
gen_frontend_mappings_Class2Class_ClassMapping = Generalization(general=ClassMapping, specific=frontend_mappings_Class2Class)
gen_frontend_mappings_C2CModifier_MappingElement = Generalization(general=MappingElement, specific=frontend_mappings_C2CModifier)
gen_frontend_mappings_RelatedBy_C2CModifier = Generalization(general=C2CModifier, specific=frontend_mappings_RelatedBy)
gen_frontend_mappings_LinkedBy_C2CModifier = Generalization(general=C2CModifier, specific=frontend_mappings_LinkedBy)
gen_frontend_mappings_EqualityFilter_C2CModifier = Generalization(general=C2CModifier, specific=frontend_mappings_EqualityFilter)
gen_frontend_mappings_Operator_LocatedElement = Generalization(general=LocatedElement, specific=frontend_mappings_Operator)
gen_frontend_mappings_Split_Operator = Generalization(general=Operator, specific=frontend_mappings_Split)
gen_frontend_mappings_Join_Operator = Generalization(general=Operator, specific=frontend_mappings_Join)
gen_frontend_mappings_Attribute2Attribute_mappings_Feature2Feature = Generalization(general=mappings_Feature2Feature, specific=frontend_mappings_Attribute2Attribute)
gen_frontend_mappings_Attribute2Attribute_mappings_AttributeRightPart = Generalization(general=mappings_AttributeRightPart, specific=frontend_mappings_Attribute2Attribute)
gen_frontend_mappings_Reference2Reference_Feature2Feature = Generalization(general=Feature2Feature, specific=frontend_mappings_Reference2Reference)
gen_frontend_mappings_AttributeModifier_Modifier = Generalization(general=Modifier, specific=frontend_mappings_AttributeModifier)
gen_frontend_mappings_ConvertModifier_AttributeModifier = Generalization(general=AttributeModifier, specific=frontend_mappings_ConvertModifier)
gen_frontend_mappings_DefaultValue_AttributeModifier = Generalization(general=AttributeModifier, specific=frontend_mappings_DefaultValue)
gen_frontend_mappings_IntDefaultValue_DefaultValue = Generalization(general=DefaultValue, specific=frontend_mappings_IntDefaultValue)
gen_frontend_mappings_ClassRef_MetamodelElementRef = Generalization(general=MetamodelElementRef, specific=frontend_mappings_ClassRef)
gen_frontend_mappings_FeatureRef_mappings_MetamodelElementRef = Generalization(general=mappings_MetamodelElementRef, specific=frontend_mappings_FeatureRef)
gen_frontend_mappings_FeatureRef_mappings_Feature2Feature = Generalization(general=mappings_Feature2Feature, specific=frontend_mappings_FeatureRef)
gen_frontend_mappings_AttributeRef_MetamodelElementRef = Generalization(general=MetamodelElementRef, specific=frontend_mappings_AttributeRef)
gen_frontend_mappings_ReferenceRef_MetamodelElementRef = Generalization(general=MetamodelElementRef, specific=frontend_mappings_ReferenceRef)
gen_frontend_qool_QoolTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_qool_QoolTransformation)
gen_frontend_qool_QoolQueue_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_qool_QoolQueue)
gen_frontend_qool_QoolQueue_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_qool_QoolQueue)
gen_frontend_qool_AccessByFeatureOptimization_QueueOptimization = Generalization(general=QueueOptimization, specific=frontend_qool_AccessByFeatureOptimization)
gen_frontend_qool_LocalQueue_QoolQueue = Generalization(general=QoolQueue, specific=frontend_qool_LocalQueue)
gen_frontend_qool_ModelElementQueue_QoolQueue = Generalization(general=QoolQueue, specific=frontend_qool_ModelElementQueue)
gen_frontend_qool_Segment_NamedElement = Generalization(general=NamedElement, specific=frontend_qool_Segment)
gen_frontend_qool_IteratorStatement_core_Statement = Generalization(general=core_Statement, specific=frontend_qool_IteratorStatement)
gen_frontend_qool_IteratorStatement_core_Variable = Generalization(general=core_Variable, specific=frontend_qool_IteratorStatement)
gen_frontend_qool_ForAllStatement_IteratorStatement = Generalization(general=IteratorStatement, specific=frontend_qool_ForAllStatement)
gen_frontend_qool_ForEachStatement_IteratorStatement = Generalization(general=IteratorStatement, specific=frontend_qool_ForEachStatement)
gen_frontend_qool_EmitStatement_Statement = Generalization(general=Statement, specific=frontend_qool_EmitStatement)
gen_frontend_qool_MatchExpression_Expression = Generalization(general=Expression, specific=frontend_qool_MatchExpression)
gen_frontend_qool_KindOfPredicate_MatchPredicate = Generalization(general=MatchPredicate, specific=frontend_qool_KindOfPredicate)
gen_frontend_qool_InvokeTransformation_Expression = Generalization(general=Expression, specific=frontend_qool_InvokeTransformation)
gen_frontend_qool_InvokeExternal_InvokeTransformation = Generalization(general=InvokeTransformation, specific=frontend_qool_InvokeExternal)
gen_frontend_qool_InvokeInternal_InvokeTransformation = Generalization(general=InvokeTransformation, specific=frontend_qool_InvokeInternal)
gen_frontend_facilities_Copier_Expression = Generalization(general=Expression, specific=frontend_facilities_Copier)
gen_frontend_qool_PropertyEqualsPredicate_MatchPredicate = Generalization(general=MatchPredicate, specific=frontend_qool_PropertyEqualsPredicate)
gen_frontend_tao_TaoTransformation_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_tao_TaoTransformation)
gen_frontend_tao_TemplateParameter_Variable = Generalization(general=Variable, specific=frontend_tao_TemplateParameter)
gen_frontend_tao_ObjectInstantiation_core_Variable = Generalization(general=core_Variable, specific=frontend_tao_ObjectInstantiation)
gen_frontend_tao_ObjectInstantiation_core_Statement = Generalization(general=core_Statement, specific=frontend_tao_ObjectInstantiation)
gen_frontend_tao_TemplateRootObject_ObjectInstantiation = Generalization(general=ObjectInstantiation, specific=frontend_tao_TemplateRootObject)
gen_frontend_tao_Template_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_tao_Template)
gen_frontend_tao_Template_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_tao_Template)
gen_frontend_tao_Assignment_Statement = Generalization(general=Statement, specific=frontend_tao_Assignment)
gen_frontend_tao_AttributeAssigment_Assignment = Generalization(general=Assignment, specific=frontend_tao_AttributeAssigment)
gen_frontend_tao_SourceExpression_LocatedElement = Generalization(general=LocatedElement, specific=frontend_tao_SourceExpression)
gen_frontend_tao_WithOptionalVariableExpression_SourceExpression = Generalization(general=SourceExpression, specific=frontend_tao_WithOptionalVariableExpression)
gen_frontend_tao_ObjectSourceVariable_Variable = Generalization(general=Variable, specific=frontend_tao_ObjectSourceVariable)
gen_frontend_tao_ReferenceAssignment_tao_Assignment = Generalization(general=tao_Assignment, specific=frontend_tao_ReferenceAssignment)
gen_frontend_tao_ReferenceAssignment_core_Variable = Generalization(general=core_Variable, specific=frontend_tao_ReferenceAssignment)
gen_frontend_tao_ObjectSyntax_ReferenceAssignment = Generalization(general=ReferenceAssignment, specific=frontend_tao_ObjectSyntax)
gen_frontend_tao_Invocation_ReferenceAssignment = Generalization(general=ReferenceAssignment, specific=frontend_tao_Invocation)
gen_frontend_core_DefinitionParameter_NamedElement = Generalization(general=NamedElement, specific=frontend_core_DefinitionParameter)
gen_frontend_core_ModuleParameter_DefinitionParameter = Generalization(general=DefinitionParameter, specific=frontend_core_ModuleParameter)
gen_frontend_core_ModuleDefinition_core_LocatedElement = Generalization(general=core_LocatedElement, specific=frontend_core_ModuleDefinition)
gen_frontend_core_ModuleDefinition_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_core_ModuleDefinition)
gen_frontend_core_ModuleDefinition_core_AnnotableElement = Generalization(general=core_AnnotableElement, specific=frontend_core_ModuleDefinition)
gen_frontend_core_OptimizationsAnnotation_Annotation = Generalization(general=Annotation, specific=frontend_core_OptimizationsAnnotation)
gen_frontend_core_MetamodelModelAnnotation_Annotation = Generalization(general=Annotation, specific=frontend_core_MetamodelModelAnnotation)
gen_frontend_core_SingleAnnotation_Annotation = Generalization(general=Annotation, specific=frontend_core_SingleAnnotation)
gen_frontend_core_PotencyAnnotation_SingleAnnotation = Generalization(general=SingleAnnotation, specific=frontend_core_PotencyAnnotation)
gen_frontend_core_RepresentModel_AnnotableElement = Generalization(general=AnnotableElement, specific=frontend_core_RepresentModel)
gen_frontend_core_TransformationDefinition_ModuleDefinition = Generalization(general=ModuleDefinition, specific=frontend_core_TransformationDefinition)
gen_frontend_core_EclecticTransformationDefinition_TransformationDefinition = Generalization(general=TransformationDefinition, specific=frontend_core_EclecticTransformationDefinition)
gen_frontend_core_ImportedModel_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_ImportedModel)
gen_frontend_core_ImportedModel_core_NamedElement = Generalization(general=core_NamedElement, specific=frontend_core_ImportedModel)
gen_frontend_core_UseDeclaration_RepresentModel = Generalization(general=RepresentModel, specific=frontend_core_UseDeclaration)
gen_frontend_core_RequireDeclaration_RepresentModel = Generalization(general=RepresentModel, specific=frontend_core_RequireDeclaration)
gen_frontend_core_RequireModelParameter_RequireParameter = Generalization(general=RequireParameter, specific=frontend_core_RequireModelParameter)
gen_frontend_core_Statement_LocatedElement = Generalization(general=LocatedElement, specific=frontend_core_Statement)
gen_frontend_core_Expression_Statement = Generalization(general=Statement, specific=frontend_core_Expression)
gen_frontend_core_DefineVariable_core_Statement = Generalization(general=core_Statement, specific=frontend_core_DefineVariable)
gen_frontend_core_DefineVariable_core_Variable = Generalization(general=core_Variable, specific=frontend_core_DefineVariable)
gen_frontend_core_PropertyWrite_Expression = Generalization(general=Expression, specific=frontend_core_PropertyWrite)
gen_frontend_core_TransformationDefinitionParameter_core_DefinitionParameter = Generalization(general=core_DefinitionParameter, specific=frontend_core_TransformationDefinitionParameter)
gen_frontend_core_TransformationDefinitionParameter_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_TransformationDefinitionParameter)
gen_frontend_core_ModelReference_core_ClassUse = Generalization(general=core_ClassUse, specific=frontend_core_ModelReference)
gen_frontend_core_ModelReference_core_Expression = Generalization(general=core_Expression, specific=frontend_core_ModelReference)
gen_frontend_core_VariableReference_Expression = Generalization(general=Expression, specific=frontend_core_VariableReference)
gen_frontend_core_MethodCall_Expression = Generalization(general=Expression, specific=frontend_core_MethodCall)
gen_frontend_core_KeywordMethodCall_Expression = Generalization(general=Expression, specific=frontend_core_KeywordMethodCall)
gen_frontend_core_BinaryExpr_Expression = Generalization(general=Expression, specific=frontend_core_BinaryExpr)
gen_frontend_core_ClosureDeclaration_Expression = Generalization(general=Expression, specific=frontend_core_ClosureDeclaration)
gen_frontend_core_ClosureParameter_Variable = Generalization(general=Variable, specific=frontend_core_ClosureParameter)
gen_frontend_core_ResolveLink_Expression = Generalization(general=Expression, specific=frontend_core_ResolveLink)
gen_frontend_core_IfExpr_Expression = Generalization(general=Expression, specific=frontend_core_IfExpr)
gen_frontend_core_NumLiteral_Expression = Generalization(general=Expression, specific=frontend_core_NumLiteral)
gen_frontend_core_BooleanLiteral_Expression = Generalization(general=Expression, specific=frontend_core_BooleanLiteral)
gen_frontend_core_ClassUse_core_TypeExpression = Generalization(general=core_TypeExpression, specific=frontend_core_ClassUse)
gen_frontend_core_ClassUse_core_ImplicitlyAnnotableElement = Generalization(general=core_ImplicitlyAnnotableElement, specific=frontend_core_ClassUse)
gen_frontend_core_TraceUse_TypeExpression = Generalization(general=TypeExpression, specific=frontend_core_TraceUse)
gen_frontend_core_TraceInterface_ModuleDefinition = Generalization(general=ModuleDefinition, specific=frontend_core_TraceInterface)
gen_frontend_core_TracedModelParameter_core_DefinitionParameter = Generalization(general=core_DefinitionParameter, specific=frontend_core_TracedModelParameter)
gen_frontend_core_TracedModelParameter_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_TracedModelParameter)
gen_frontend_core_TraceDefinition_NamedElement = Generalization(general=NamedElement, specific=frontend_core_TraceDefinition)
gen_frontend_core_TraceElement_NamedElement = Generalization(general=NamedElement, specific=frontend_core_TraceElement)
gen_frontend_core_InlineModel_core_ModuleDefinition = Generalization(general=core_ModuleDefinition, specific=frontend_core_InlineModel)
gen_frontend_core_InlineModel_core_RepresentModel = Generalization(general=core_RepresentModel, specific=frontend_core_InlineModel)
gen_frontend_core_InlineClass_NamedElement = Generalization(general=NamedElement, specific=frontend_core_InlineClass)
gen_frontend_core_InlineFeature_NamedElement = Generalization(general=NamedElement, specific=frontend_core_InlineFeature)
gen_frontend_core_InlineAttribute_InlineFeature = Generalization(general=InlineFeature, specific=frontend_core_InlineAttribute)
gen_frontend_core_InlineReference_InlineFeature = Generalization(general=InlineFeature, specific=frontend_core_InlineReference)
gen_frontend_core_DoubleLiteral_Expression = Generalization(general=Expression, specific=frontend_core_DoubleLiteral)
gen_frontend_core_StringLiteral_Expression = Generalization(general=Expression, specific=frontend_core_StringLiteral)
gen_frontend_core_PutTrace_Expression = Generalization(general=Expression, specific=frontend_core_PutTrace)
gen_frontend_core_MatchTrace_Expression = Generalization(general=Expression, specific=frontend_core_MatchTrace)

# Domain Model
domain_model = DomainModel(
    name="frontend",
    types={frontend_DummyRootMetaclass, frontend_script_ScriptedTransformation, TransformationDefinition, Statement, frontend_koan_KoanTransformation, TraceInterface, KoanRule, frontend_koan_KoanRule, core_LocatedElement, core_NamedElement, Matcher, frontend_koan_Matcher, LocatedElement, frontend_koan_ForAllMatcher, koan_Matcher, core_Variable, ClassUse, frontend_attribution_AttributionTransformation, AttributeDcl, AttributionRule, frontend_attribution_AttributeDcl, core_TypedWithClass, CompositeTransformation, frontend_attribution_InheritedAttributeDcl, frontend_attribution_SynthesizedAttributeDcl, frontend_attribution_AttributionRule, RuleSelf, Expression, frontend_attribution_RuleSelf, Variable, frontend_attribution_AttributeInit, frontend_attribution_AttributeUse, frontend_imperative_ImperativeTransformation, MethodDefinition, frontend_imperative_MethodDefinition, MethodParameter, MethodSelf, frontend_imperative_MethodSelf, frontend_imperative_MethodParameter, frontend_chain_ChainTransformation, ExternalTransformation, GeneratedModel, TransformationExecution, frontend_chain_GeneratedModel, core_RepresentModel, frontend_chain_TransformationExecution, AvailableTransformation, RepresentModel, frontend_chain_AvailableTransformation, frontend_chain_ExternalTransformation, chain_AvailableTransformation, frontend_chain_CompositeTransformation, core_TransformationDefinition, frontend_patterns_PatternSpecification, Pattern, frontend_patterns_Pattern, PObject, POutputVariable, frontend_patterns_POutputVariable, frontend_patterns_PObject, PFeature, frontend_patterns_PFeature, frontend_patterns_PAttribute, frontend_patterns_PReference, frontend_patterns_CollectionReference, PReference, frontend_mappings_MappingTransformation, Delegate, Context, frontend_mappings_MappingVariable, frontend_mappings_MatchedElement, core_ClassUse, mappings_MappingVariable, frontend_mappings_Delegate, MatchedElement, UseDeclaration, Tag, frontend_mappings_Context, MappingElement, C2CModifier, Section, frontend_mappings_Section, frontend_mappings_MappingElement, frontend_mappings_ClassMapping, frontend_mappings_Feature2Feature, FeatureRef, Converter, frontend_mappings_AttributeMapping, Feature2Feature, AttributeRef, AttributeRightPart, frontend_mappings_AttributeRightPart, frontend_mappings_AttributeIsString, frontend_mappings_AttributeIsBoolean, frontend_mappings_AttributeIsDouble, frontend_mappings_AttributeIsResolveLink, ResolveLink, frontend_mappings_AttributeIsInteger, frontend_mappings_Converter, frontend_mappings_Tag, NamedElement, frontend_mappings_Class2Class, ClassMapping, ClassRef, Attribute2Attribute, frontend_mappings_C2CModifier, frontend_mappings_RelatedBy, frontend_mappings_LinkedBy, frontend_mappings_EqualityFilter, frontend_mappings_Operator, frontend_mappings_Split, Operator, frontend_mappings_Join, frontend_mappings_Attribute2Attribute, mappings_Feature2Feature, mappings_AttributeRightPart, Class2Class, AttributeModifier, frontend_mappings_Reference2Reference, ReferenceRef, frontend_mappings_Modifier, frontend_mappings_AttributeModifier, Modifier, frontend_mappings_ConvertModifier, frontend_mappings_DefaultValue, frontend_mappings_IntDefaultValue, DefaultValue, frontend_mappings_MetamodelElementRef, frontend_mappings_ClassRef, MetamodelElementRef, frontend_mappings_FeatureRef, mappings_MetamodelElementRef, frontend_mappings_AttributeRef, frontend_mappings_ReferenceRef, frontend_qool_QoolTransformation, QoolQueue, Segment, frontend_qool_QoolQueue, QueueOptimization, frontend_qool_QueueOptimization, frontend_qool_AccessByFeatureOptimization, frontend_qool_LocalQueue, TypeExpression, frontend_qool_ModelElementQueue, frontend_qool_Segment, frontend_qool_IteratorStatement, core_Statement, frontend_qool_ForAllStatement, IteratorStatement, frontend_qool_ForEachStatement, frontend_qool_EmitStatement, frontend_qool_MatchExpression, MatchPredicate, frontend_qool_MatchPredicate, frontend_qool_KindOfPredicate, frontend_qool_InvokeTransformation, InvocationParameter, NamedInvocationParameter, frontend_qool_InvokeExternal, InvokeTransformation, frontend_qool_InvokeInternal, frontend_qool_InvocationParameter, TransformationDefinitionParameter, frontend_qool_NamedInvocationParameter, frontend_facilities_Copier, frontend_qool_PropertyEqualsPredicate, frontend_facilities_CopierCallbackDefinition, frontend_tao_TaoTransformation, Template, frontend_tao_TemplateParameter, frontend_tao_ObjectInstantiation, Assignment, frontend_tao_TemplateRootObject, ObjectInstantiation, frontend_tao_Template, TemplateParameter, TemplateRootObject, frontend_tao_Assignment, frontend_tao_AttributeAssigment, SourceExpression, frontend_tao_SourceExpression, frontend_tao_WithOptionalVariableExpression, ObjectSourceVariable, facilities_CopierCallbackDefinition, frontend_tao_ObjectSourceVariable, frontend_tao_ReferenceAssignment, tao_Assignment, frontend_tao_ObjectSyntax, ReferenceAssignment, frontend_tao_Invocation, frontend_core_LocatedElement, frontend_core_NamedElement, frontend_core_DefinitionParameter, frontend_core_ModuleParameter, DefinitionParameter, frontend_core_ModuleDefinition, core_AnnotableElement, frontend_core_AnnotableElement, Annotation, frontend_core_ImplicitlyAnnotableElement, SingleAnnotation, frontend_core_Annotation, AnnotableElement, frontend_core_OptimizationsAnnotation, frontend_core_MetamodelModelAnnotation, frontend_core_SingleAnnotation, frontend_core_PotencyAnnotation, frontend_core_GenericAnnotation, AnnotationParameter, frontend_core_AnnotationParameter, frontend_core_RepresentModel, frontend_core_TransformationDefinition, ModuleDefinition, ImportedModel, InlineModel, RequireDeclaration, frontend_core_EclecticTransformationDefinition, frontend_core_ImportedModel, frontend_core_UseDeclaration, frontend_core_RequireDeclaration, RequireParameter, frontend_core_RequireParameter, frontend_core_RequireModelParameter, frontend_core_Variable, frontend_core_Statement, frontend_core_Expression, frontend_core_DefineVariable, frontend_core_PropertyWrite, frontend_core_TransformationDefinitionParameter, core_DefinitionParameter, frontend_core_ModelReference, core_Expression, frontend_core_VariableReference, frontend_core_MethodCall, frontend_core_KeywordMethodCall, KeywordParameter, frontend_core_KeywordParameter, frontend_core_BinaryExpr, frontend_core_ClosureDeclaration, ClosureParameter, frontend_core_ClosureParameter, frontend_core_ResolveLink, frontend_core_IfExpr, IfBranch, frontend_core_IfBranch, frontend_core_NumLiteral, frontend_core_BooleanLiteral, frontend_core_TypeExpression, frontend_core_ClassUse, core_TypeExpression, core_ImplicitlyAnnotableElement, frontend_core_TraceUse, TraceDefinition, frontend_core_TypedWithClass, frontend_core_TraceInterface, frontend_core_TracedModelParameter, frontend_core_TraceDefinition, TraceElement, frontend_core_TraceElement, frontend_core_InlineModel, core_ModuleDefinition, InlineClass, frontend_core_InlineClass, InlineFeature, frontend_core_InlineFeature, frontend_core_InlineAttribute, frontend_core_InlineReference, frontend_core_MatchTrace, frontend_core_DoubleLiteral, frontend_core_StringLiteral, frontend_core_TraceCompareExpression, frontend_core_PutTrace, PutTraceParameter, frontend_core_PutTraceParameter, TraceCompareExpression, MappingCardinality, BinaryOp, ResolveTraceCardinality},
    associations={statements0, traceInterface1, rules2, matcher4, statements5, child8, type10, attributes11, rules12, composites46, type14, self16, condition18, statements20, attribute23, receptor25, right28, expr31, attribute33, methods36, formalParameters37, self38, type40, statements43, externals47, generatedModels49, executions51, transformation53, inputModels54, outputModels56, executions59, patterns61, objects62, outputVariables63, object65, type67, features69, value71, variable73, value75, delegates77, contexts78, left80, module81, tags83, left85, right87, mappings90, modifiers92, sections94, tags96, mappings99, leftFeature101, converter102, left104, rightPart105, resolveLink107, module108, modifiers110, left112, right114, scopedAttributes117, attribute118, attribute120, linkedElement122, attribute125, mappings127, mappings128, context130, right131, modifiers133, left135, right136, klass139, referredElement141, referredElement143, referredElement145, queues147, segments148, optimizations150, type_151, class_152, additionals154, statements157, condition159, statements161, queue164, collection166, queue168, value170, queue173, predicates175, value179, sourceModels181, targetModels182, parameters185, inputViewFilter187, entryPointParameters190, outputResolutionSourceElement193, model195, actualParameter196, objects198, class_177, trigger205, action207, templates210, type211, type213, assigments215, parameters217, roots218, expr220, variable221, expr222, callbacks200, copyInModel202, expr225, object227, template228, annotatedWith230, annotations231, annotatedElement232, parameters233, inModels234, outModels236, importedModels239, inlineModels241, annotations243, uses246, requires249, parameters252, model253, expression255, transformations251, expression259, variable262, receptor264, parameters266, receptor269, parameters271, value273, left275, receptor257, statements280, formalParameters282, expr284, module286, then289, elsifs290, else_293, condition296, statements298, right277, model301, trace303, type_304, definitions306, elements308, type309, classes311, features312, type313, traceExpr317, traceVar319, expr321, trace324, parameters326, value328, traceVar330, trace315},
    generalizations={gen_frontend_script_ScriptedTransformation_TransformationDefinition, gen_frontend_attribution_AttributeDcl_core_LocatedElement, gen_frontend_koan_KoanTransformation_TransformationDefinition, gen_frontend_koan_KoanRule_core_LocatedElement, gen_frontend_koan_KoanRule_core_NamedElement, gen_frontend_koan_Matcher_LocatedElement, gen_frontend_koan_ForAllMatcher_koan_Matcher, gen_frontend_koan_ForAllMatcher_core_Variable, gen_frontend_attribution_AttributionTransformation_TransformationDefinition, gen_frontend_attribution_AttributeDcl_core_Variable, gen_frontend_attribution_AttributeDcl_core_TypedWithClass, gen_frontend_attribution_InheritedAttributeDcl_AttributeDcl, gen_frontend_attribution_SynthesizedAttributeDcl_AttributeDcl, gen_frontend_attribution_AttributionRule_LocatedElement, gen_frontend_attribution_RuleSelf_Variable, gen_frontend_attribution_AttributeInit_Statement, gen_frontend_attribution_AttributeUse_Expression, gen_frontend_imperative_ImperativeTransformation_TransformationDefinition, gen_frontend_imperative_MethodDefinition_LocatedElement, gen_frontend_imperative_MethodSelf_Variable, gen_frontend_imperative_MethodParameter_Variable, gen_frontend_chain_ChainTransformation_TransformationDefinition, gen_frontend_chain_GeneratedModel_core_RepresentModel, gen_frontend_chain_GeneratedModel_core_NamedElement, gen_frontend_chain_TransformationExecution_LocatedElement, gen_frontend_chain_ExternalTransformation_chain_AvailableTransformation, gen_frontend_chain_ExternalTransformation_core_NamedElement, gen_frontend_chain_CompositeTransformation_chain_AvailableTransformation, gen_frontend_chain_CompositeTransformation_core_TransformationDefinition, gen_frontend_patterns_PatternSpecification_TransformationDefinition, gen_frontend_patterns_Pattern_LocatedElement, gen_frontend_patterns_PObject_core_Variable, gen_frontend_patterns_PObject_core_LocatedElement, gen_frontend_patterns_PFeature_LocatedElement, gen_frontend_patterns_PAttribute_PFeature, gen_frontend_patterns_PReference_PFeature, gen_frontend_patterns_CollectionReference_PReference, gen_frontend_mappings_MappingTransformation_TransformationDefinition, gen_frontend_mappings_MappingVariable_Variable, gen_frontend_mappings_MatchedElement_core_ClassUse, gen_frontend_mappings_MatchedElement_mappings_MappingVariable, gen_frontend_mappings_Delegate_LocatedElement, gen_frontend_mappings_Context_LocatedElement, gen_frontend_mappings_Section_LocatedElement, gen_frontend_mappings_MappingElement_LocatedElement, gen_frontend_mappings_ClassMapping_MappingElement, gen_frontend_mappings_Feature2Feature_MappingElement, gen_frontend_mappings_AttributeMapping_Feature2Feature, gen_frontend_mappings_AttributeIsString_AttributeRightPart, gen_frontend_mappings_AttributeIsBoolean_AttributeRightPart, gen_frontend_mappings_AttributeIsDouble_AttributeRightPart, gen_frontend_mappings_AttributeIsResolveLink_AttributeRightPart, gen_frontend_mappings_AttributeIsInteger_AttributeRightPart, gen_frontend_mappings_Tag_NamedElement, gen_frontend_mappings_Class2Class_ClassMapping, gen_frontend_mappings_C2CModifier_MappingElement, gen_frontend_mappings_RelatedBy_C2CModifier, gen_frontend_mappings_LinkedBy_C2CModifier, gen_frontend_mappings_EqualityFilter_C2CModifier, gen_frontend_mappings_Operator_LocatedElement, gen_frontend_mappings_Split_Operator, gen_frontend_mappings_Join_Operator, gen_frontend_mappings_Attribute2Attribute_mappings_Feature2Feature, gen_frontend_mappings_Attribute2Attribute_mappings_AttributeRightPart, gen_frontend_mappings_Reference2Reference_Feature2Feature, gen_frontend_mappings_AttributeModifier_Modifier, gen_frontend_mappings_ConvertModifier_AttributeModifier, gen_frontend_mappings_DefaultValue_AttributeModifier, gen_frontend_mappings_IntDefaultValue_DefaultValue, gen_frontend_mappings_ClassRef_MetamodelElementRef, gen_frontend_mappings_FeatureRef_mappings_MetamodelElementRef, gen_frontend_mappings_FeatureRef_mappings_Feature2Feature, gen_frontend_mappings_AttributeRef_MetamodelElementRef, gen_frontend_mappings_ReferenceRef_MetamodelElementRef, gen_frontend_qool_QoolTransformation_TransformationDefinition, gen_frontend_qool_QoolQueue_core_LocatedElement, gen_frontend_qool_QoolQueue_core_NamedElement, gen_frontend_qool_AccessByFeatureOptimization_QueueOptimization, gen_frontend_qool_LocalQueue_QoolQueue, gen_frontend_qool_ModelElementQueue_QoolQueue, gen_frontend_qool_Segment_NamedElement, gen_frontend_qool_IteratorStatement_core_Statement, gen_frontend_qool_IteratorStatement_core_Variable, gen_frontend_qool_ForAllStatement_IteratorStatement, gen_frontend_qool_ForEachStatement_IteratorStatement, gen_frontend_qool_EmitStatement_Statement, gen_frontend_qool_MatchExpression_Expression, gen_frontend_qool_KindOfPredicate_MatchPredicate, gen_frontend_qool_InvokeTransformation_Expression, gen_frontend_qool_InvokeExternal_InvokeTransformation, gen_frontend_qool_InvokeInternal_InvokeTransformation, gen_frontend_facilities_Copier_Expression, gen_frontend_qool_PropertyEqualsPredicate_MatchPredicate, gen_frontend_tao_TaoTransformation_TransformationDefinition, gen_frontend_tao_TemplateParameter_Variable, gen_frontend_tao_ObjectInstantiation_core_Variable, gen_frontend_tao_ObjectInstantiation_core_Statement, gen_frontend_tao_TemplateRootObject_ObjectInstantiation, gen_frontend_tao_Template_core_NamedElement, gen_frontend_tao_Template_core_LocatedElement, gen_frontend_tao_Assignment_Statement, gen_frontend_tao_AttributeAssigment_Assignment, gen_frontend_tao_SourceExpression_LocatedElement, gen_frontend_tao_WithOptionalVariableExpression_SourceExpression, gen_frontend_tao_ObjectSourceVariable_Variable, gen_frontend_tao_ReferenceAssignment_tao_Assignment, gen_frontend_tao_ReferenceAssignment_core_Variable, gen_frontend_tao_ObjectSyntax_ReferenceAssignment, gen_frontend_tao_Invocation_ReferenceAssignment, gen_frontend_core_DefinitionParameter_NamedElement, gen_frontend_core_ModuleParameter_DefinitionParameter, gen_frontend_core_ModuleDefinition_core_LocatedElement, gen_frontend_core_ModuleDefinition_core_NamedElement, gen_frontend_core_ModuleDefinition_core_AnnotableElement, gen_frontend_core_OptimizationsAnnotation_Annotation, gen_frontend_core_MetamodelModelAnnotation_Annotation, gen_frontend_core_SingleAnnotation_Annotation, gen_frontend_core_PotencyAnnotation_SingleAnnotation, gen_frontend_core_RepresentModel_AnnotableElement, gen_frontend_core_TransformationDefinition_ModuleDefinition, gen_frontend_core_EclecticTransformationDefinition_TransformationDefinition, gen_frontend_core_ImportedModel_core_RepresentModel, gen_frontend_core_ImportedModel_core_NamedElement, gen_frontend_core_UseDeclaration_RepresentModel, gen_frontend_core_RequireDeclaration_RepresentModel, gen_frontend_core_RequireModelParameter_RequireParameter, gen_frontend_core_Statement_LocatedElement, gen_frontend_core_Expression_Statement, gen_frontend_core_DefineVariable_core_Statement, gen_frontend_core_DefineVariable_core_Variable, gen_frontend_core_PropertyWrite_Expression, gen_frontend_core_TransformationDefinitionParameter_core_DefinitionParameter, gen_frontend_core_TransformationDefinitionParameter_core_RepresentModel, gen_frontend_core_ModelReference_core_ClassUse, gen_frontend_core_ModelReference_core_Expression, gen_frontend_core_VariableReference_Expression, gen_frontend_core_MethodCall_Expression, gen_frontend_core_KeywordMethodCall_Expression, gen_frontend_core_BinaryExpr_Expression, gen_frontend_core_ClosureDeclaration_Expression, gen_frontend_core_ClosureParameter_Variable, gen_frontend_core_ResolveLink_Expression, gen_frontend_core_IfExpr_Expression, gen_frontend_core_NumLiteral_Expression, gen_frontend_core_BooleanLiteral_Expression, gen_frontend_core_ClassUse_core_TypeExpression, gen_frontend_core_ClassUse_core_ImplicitlyAnnotableElement, gen_frontend_core_TraceUse_TypeExpression, gen_frontend_core_TraceInterface_ModuleDefinition, gen_frontend_core_TracedModelParameter_core_DefinitionParameter, gen_frontend_core_TracedModelParameter_core_RepresentModel, gen_frontend_core_TraceDefinition_NamedElement, gen_frontend_core_TraceElement_NamedElement, gen_frontend_core_InlineModel_core_ModuleDefinition, gen_frontend_core_InlineModel_core_RepresentModel, gen_frontend_core_InlineClass_NamedElement, gen_frontend_core_InlineFeature_NamedElement, gen_frontend_core_InlineAttribute_InlineFeature, gen_frontend_core_InlineReference_InlineFeature, gen_frontend_core_DoubleLiteral_Expression, gen_frontend_core_StringLiteral_Expression, gen_frontend_core_PutTrace_Expression, gen_frontend_core_MatchTrace_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)