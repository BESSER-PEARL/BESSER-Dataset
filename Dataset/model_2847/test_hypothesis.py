import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    frontend_core_NamedElement,
    frontend_core_LocatedElement,
    ImportedModel,
    ModuleDefinition,
    frontend_core_TransformationDefinition,
    frontend_core_AnnotationParameter,
    AnnotationParameter,
    frontend_core_GenericAnnotation,
    ObjectSourceVariable,
    SourceExpression,
    frontend_tao_WithOptionalVariableExpression,
    TemplateRootObject,
    TemplateParameter,
    ObjectInstantiation,
    frontend_tao_TemplateRootObject,
    Assignment,
    frontend_tao_AttributeAssigment,
    ReferenceAssignment,
    frontend_tao_Invocation,
    frontend_tao_ObjectSyntax,
    tao_Assignment,
    frontend_facilities_CopierCallbackDefinition,
    facilities_CopierCallbackDefinition,
    Template,
    InvokeTransformation,
    frontend_qool_InvokeExternal,
    NamedInvocationParameter,
    InvocationParameter,
    frontend_qool_NamedInvocationParameter,
    TransformationDefinitionParameter,
    frontend_qool_InvocationParameter,
    frontend_qool_InvokeInternal,
    IteratorStatement,
    frontend_qool_ForEachStatement,
    frontend_qool_ForAllStatement,
    core_Statement,
    TypeExpression,
    frontend_qool_QueueOptimization,
    QueueOptimization,
    frontend_qool_AccessByFeatureOptimization,
    frontend_qool_MatchPredicate,
    MatchPredicate,
    frontend_qool_KindOfPredicate,
    frontend_qool_PropertyEqualsPredicate,
    mappings_MetamodelElementRef,
    MetamodelElementRef,
    frontend_mappings_AttributeRef,
    frontend_mappings_ClassRef,
    frontend_mappings_MetamodelElementRef,
    DefaultValue,
    frontend_mappings_IntDefaultValue,
    Segment,
    QoolQueue,
    frontend_qool_LocalQueue,
    frontend_qool_ModelElementQueue,
    frontend_mappings_ReferenceRef,
    AttributeModifier,
    frontend_mappings_DefaultValue,
    Class2Class,
    mappings_AttributeRightPart,
    mappings_Feature2Feature,
    frontend_mappings_FeatureRef,
    frontend_mappings_Attribute2Attribute,
    Operator,
    frontend_mappings_Join,
    frontend_mappings_Split,
    frontend_mappings_ConvertModifier,
    Modifier,
    frontend_mappings_AttributeModifier,
    frontend_mappings_Modifier,
    ClassRef,
    ReferenceRef,
    ClassMapping,
    frontend_mappings_Class2Class,
    NamedElement,
    frontend_qool_Segment,
    frontend_mappings_Tag,
    frontend_mappings_Converter,
    ResolveLink,
    Attribute2Attribute,
    Section,
    C2CModifier,
    frontend_mappings_RelatedBy,
    frontend_mappings_EqualityFilter,
    frontend_mappings_LinkedBy,
    MappingElement,
    frontend_mappings_C2CModifier,
    Tag,
    UseDeclaration,
    MatchedElement,
    mappings_MappingVariable,
    core_ClassUse,
    frontend_mappings_MatchedElement,
    Context,
    frontend_mappings_AttributeRightPart,
    AttributeRightPart,
    frontend_mappings_AttributeIsResolveLink,
    frontend_mappings_AttributeIsDouble,
    frontend_mappings_AttributeIsBoolean,
    frontend_mappings_AttributeIsString,
    frontend_mappings_AttributeIsInteger,
    AttributeRef,
    Feature2Feature,
    frontend_mappings_Reference2Reference,
    frontend_mappings_AttributeMapping,
    Converter,
    FeatureRef,
    frontend_mappings_Feature2Feature,
    frontend_mappings_ClassMapping,
    frontend_patterns_POutputVariable,
    POutputVariable,
    PObject,
    Pattern,
    core_TransformationDefinition,
    chain_AvailableTransformation,
    frontend_chain_CompositeTransformation,
    frontend_chain_AvailableTransformation,
    RepresentModel,
    AvailableTransformation,
    Delegate,
    PReference,
    frontend_patterns_CollectionReference,
    PFeature,
    frontend_patterns_PReference,
    frontend_patterns_PAttribute,
    MethodSelf,
    MethodParameter,
    MethodDefinition,
    Variable,
    frontend_tao_TemplateParameter,
    frontend_mappings_MappingVariable,
    frontend_tao_ObjectSourceVariable,
    frontend_attribution_RuleSelf,
    Expression,
    frontend_qool_MatchExpression,
    frontend_attribution_AttributeUse,
    frontend_qool_InvokeTransformation,
    frontend_facilities_Copier,
    RuleSelf,
    core_RepresentModel,
    TransformationExecution,
    GeneratedModel,
    ExternalTransformation,
    CompositeTransformation,
    frontend_imperative_MethodParameter,
    frontend_imperative_MethodSelf,
    Matcher,
    core_NamedElement,
    frontend_chain_GeneratedModel,
    frontend_chain_ExternalTransformation,
    core_LocatedElement,
    frontend_tao_Template,
    frontend_qool_QoolQueue,
    frontend_koan_KoanRule,
    KoanRule,
    TraceInterface,
    Statement,
    frontend_tao_Assignment,
    frontend_qool_EmitStatement,
    frontend_attribution_AttributeInit,
    TransformationDefinition,
    frontend_chain_ChainTransformation,
    frontend_imperative_ImperativeTransformation,
    frontend_koan_KoanTransformation,
    frontend_tao_TaoTransformation,
    frontend_qool_QoolTransformation,
    frontend_patterns_PatternSpecification,
    frontend_mappings_MappingTransformation,
    frontend_script_ScriptedTransformation,
    frontend_DummyRootMetaclass,
    core_TypedWithClass,
    AttributionRule,
    AttributeDcl,
    frontend_attribution_SynthesizedAttributeDcl,
    frontend_attribution_InheritedAttributeDcl,
    frontend_attribution_AttributionTransformation,
    ClassUse,
    core_Variable,
    frontend_attribution_AttributeDcl,
    frontend_tao_ObjectInstantiation,
    frontend_qool_IteratorStatement,
    frontend_patterns_PObject,
    frontend_tao_ReferenceAssignment,
    koan_Matcher,
    frontend_koan_ForAllMatcher,
    LocatedElement,
    frontend_chain_TransformationExecution,
    frontend_patterns_Pattern,
    frontend_attribution_AttributionRule,
    frontend_imperative_MethodDefinition,
    frontend_tao_SourceExpression,
    frontend_mappings_Section,
    frontend_mappings_Delegate,
    frontend_mappings_MappingElement,
    frontend_patterns_PFeature,
    frontend_mappings_Operator,
    frontend_mappings_Context,
    frontend_koan_Matcher,
    frontend_core_PutTraceParameter,
    PutTraceParameter,
    frontend_core_PutTrace,
    frontend_core_InlineFeature,
    InlineFeature,
    frontend_core_InlineClass,
    InlineClass,
    core_ModuleDefinition,
    frontend_core_InlineModel,
    frontend_core_TraceElement,
    TraceElement,
    frontend_core_TraceDefinition,
    frontend_core_TraceInterface,
    frontend_core_TypedWithClass,
    TraceDefinition,
    frontend_core_TraceUse,
    frontend_core_TraceCompareExpression,
    TraceCompareExpression,
    frontend_core_MatchTrace,
    frontend_core_InlineReference,
    frontend_core_InlineAttribute,
    frontend_core_IfBranch,
    IfBranch,
    frontend_core_IfExpr,
    core_ImplicitlyAnnotableElement,
    core_TypeExpression,
    frontend_core_ClassUse,
    frontend_core_TypeExpression,
    frontend_core_BooleanLiteral,
    frontend_core_StringLiteral,
    frontend_core_DoubleLiteral,
    frontend_core_NumLiteral,
    frontend_core_BinaryExpr,
    frontend_core_KeywordParameter,
    KeywordParameter,
    frontend_core_KeywordMethodCall,
    frontend_core_MethodCall,
    frontend_core_VariableReference,
    core_Expression,
    frontend_core_ModelReference,
    frontend_core_ResolveLink,
    frontend_core_ClosureParameter,
    ClosureParameter,
    frontend_core_ClosureDeclaration,
    frontend_core_Variable,
    frontend_core_RequireParameter,
    RequireParameter,
    frontend_core_RequireModelParameter,
    frontend_core_RequireDeclaration,
    frontend_core_UseDeclaration,
    frontend_core_ImportedModel,
    core_DefinitionParameter,
    frontend_core_TracedModelParameter,
    frontend_core_TransformationDefinitionParameter,
    frontend_core_EclecticTransformationDefinition,
    RequireDeclaration,
    InlineModel,
    frontend_core_PropertyWrite,
    frontend_core_DefineVariable,
    frontend_core_Expression,
    frontend_core_Statement,
    AnnotableElement,
    frontend_core_RepresentModel,
    frontend_core_Annotation,
    SingleAnnotation,
    frontend_core_PotencyAnnotation,
    frontend_core_ImplicitlyAnnotableElement,
    Annotation,
    frontend_core_SingleAnnotation,
    frontend_core_OptimizationsAnnotation,
    frontend_core_MetamodelModelAnnotation,
    frontend_core_AnnotableElement,
    core_AnnotableElement,
    frontend_core_ModuleDefinition,
    DefinitionParameter,
    frontend_core_ModuleParameter,
    frontend_core_DefinitionParameter,
    MappingCardinality,
    BinaryOp,
    ResolveTraceCardinality,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_frontend_core_namedelement_is_not_abstract():
    assert not inspect.isabstract(frontend_core_NamedElement)


def test_frontend_core_namedelement_constructor_exists():
    assert callable(frontend_core_NamedElement.__init__)


def test_frontend_core_namedelement_constructor_args():
    sig = inspect.signature(frontend_core_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend_core_namedelement_has_name():
    assert hasattr(frontend_core_NamedElement, "name")
    descriptor = None
    for klass in frontend_core_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_locatedelement_is_not_abstract():
    assert not inspect.isabstract(frontend_core_LocatedElement)


def test_frontend_core_locatedelement_constructor_exists():
    assert callable(frontend_core_LocatedElement.__init__)


def test_frontend_core_locatedelement_constructor_args():
    sig = inspect.signature(frontend_core_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"
    assert "row" in params, "Missing parameter 'row'"
    assert "column" in params, "Missing parameter 'column'"

def test_frontend_core_locatedelement_has_file():
    assert hasattr(frontend_core_LocatedElement, "file")
    descriptor = None
    for klass in frontend_core_LocatedElement.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_locatedelement_has_row():
    assert hasattr(frontend_core_LocatedElement, "row")
    descriptor = None
    for klass in frontend_core_LocatedElement.__mro__:
        if "row" in klass.__dict__:
            descriptor = klass.__dict__["row"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_locatedelement_has_column():
    assert hasattr(frontend_core_LocatedElement, "column")
    descriptor = None
    for klass in frontend_core_LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_importedmodel_is_not_abstract():
    assert not inspect.isabstract(ImportedModel)


def test_importedmodel_constructor_exists():
    assert callable(ImportedModel.__init__)


def test_importedmodel_constructor_args():
    sig = inspect.signature(ImportedModel.__init__)
    params = list(sig.parameters.keys())



def test_moduledefinition_is_not_abstract():
    assert not inspect.isabstract(ModuleDefinition)


def test_moduledefinition_constructor_exists():
    assert callable(ModuleDefinition.__init__)


def test_moduledefinition_constructor_args():
    sig = inspect.signature(ModuleDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_transformationdefinition_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TransformationDefinition)


def test_frontend_core_transformationdefinition_constructor_exists():
    assert callable(frontend_core_TransformationDefinition.__init__)


def test_frontend_core_transformationdefinition_constructor_args():
    sig = inspect.signature(frontend_core_TransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_AnnotationParameter)


def test_frontend_core_annotationparameter_constructor_exists():
    assert callable(frontend_core_AnnotationParameter.__init__)


def test_frontend_core_annotationparameter_constructor_args():
    sig = inspect.signature(frontend_core_AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(AnnotationParameter)


def test_annotationparameter_constructor_exists():
    assert callable(AnnotationParameter.__init__)


def test_annotationparameter_constructor_args():
    sig = inspect.signature(AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_genericannotation_is_not_abstract():
    assert not inspect.isabstract(frontend_core_GenericAnnotation)


def test_frontend_core_genericannotation_constructor_exists():
    assert callable(frontend_core_GenericAnnotation.__init__)


def test_frontend_core_genericannotation_constructor_args():
    sig = inspect.signature(frontend_core_GenericAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend_core_genericannotation_has_name():
    assert hasattr(frontend_core_GenericAnnotation, "name")
    descriptor = None
    for klass in frontend_core_GenericAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_objectsourcevariable_is_not_abstract():
    assert not inspect.isabstract(ObjectSourceVariable)


def test_objectsourcevariable_constructor_exists():
    assert callable(ObjectSourceVariable.__init__)


def test_objectsourcevariable_constructor_args():
    sig = inspect.signature(ObjectSourceVariable.__init__)
    params = list(sig.parameters.keys())



def test_sourceexpression_is_not_abstract():
    assert not inspect.isabstract(SourceExpression)


def test_sourceexpression_constructor_exists():
    assert callable(SourceExpression.__init__)


def test_sourceexpression_constructor_args():
    sig = inspect.signature(SourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_withoptionalvariableexpression_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_WithOptionalVariableExpression)


def test_frontend_tao_withoptionalvariableexpression_constructor_exists():
    assert callable(frontend_tao_WithOptionalVariableExpression.__init__)


def test_frontend_tao_withoptionalvariableexpression_constructor_args():
    sig = inspect.signature(frontend_tao_WithOptionalVariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_templaterootobject_is_not_abstract():
    assert not inspect.isabstract(TemplateRootObject)


def test_templaterootobject_constructor_exists():
    assert callable(TemplateRootObject.__init__)


def test_templaterootobject_constructor_args():
    sig = inspect.signature(TemplateRootObject.__init__)
    params = list(sig.parameters.keys())



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_objectinstantiation_is_not_abstract():
    assert not inspect.isabstract(ObjectInstantiation)


def test_objectinstantiation_constructor_exists():
    assert callable(ObjectInstantiation.__init__)


def test_objectinstantiation_constructor_args():
    sig = inspect.signature(ObjectInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_templaterootobject_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_TemplateRootObject)


def test_frontend_tao_templaterootobject_constructor_exists():
    assert callable(frontend_tao_TemplateRootObject.__init__)


def test_frontend_tao_templaterootobject_constructor_args():
    sig = inspect.signature(frontend_tao_TemplateRootObject.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_attributeassigment_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_AttributeAssigment)


def test_frontend_tao_attributeassigment_constructor_exists():
    assert callable(frontend_tao_AttributeAssigment.__init__)


def test_frontend_tao_attributeassigment_constructor_args():
    sig = inspect.signature(frontend_tao_AttributeAssigment.__init__)
    params = list(sig.parameters.keys())
    assert "targetFeature" in params, "Missing parameter 'targetFeature'"

def test_frontend_tao_attributeassigment_has_targetFeature():
    assert hasattr(frontend_tao_AttributeAssigment, "targetFeature")
    descriptor = None
    for klass in frontend_tao_AttributeAssigment.__mro__:
        if "targetFeature" in klass.__dict__:
            descriptor = klass.__dict__["targetFeature"]
            break
    assert isinstance(descriptor, property)



def test_referenceassignment_is_not_abstract():
    assert not inspect.isabstract(ReferenceAssignment)


def test_referenceassignment_constructor_exists():
    assert callable(ReferenceAssignment.__init__)


def test_referenceassignment_constructor_args():
    sig = inspect.signature(ReferenceAssignment.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_invocation_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_Invocation)


def test_frontend_tao_invocation_constructor_exists():
    assert callable(frontend_tao_Invocation.__init__)


def test_frontend_tao_invocation_constructor_args():
    sig = inspect.signature(frontend_tao_Invocation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_objectsyntax_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_ObjectSyntax)


def test_frontend_tao_objectsyntax_constructor_exists():
    assert callable(frontend_tao_ObjectSyntax.__init__)


def test_frontend_tao_objectsyntax_constructor_args():
    sig = inspect.signature(frontend_tao_ObjectSyntax.__init__)
    params = list(sig.parameters.keys())



def test_tao_assignment_is_not_abstract():
    assert not inspect.isabstract(tao_Assignment)


def test_tao_assignment_constructor_exists():
    assert callable(tao_Assignment.__init__)


def test_tao_assignment_constructor_args():
    sig = inspect.signature(tao_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_frontend_facilities_copiercallbackdefinition_is_not_abstract():
    assert not inspect.isabstract(frontend_facilities_CopierCallbackDefinition)


def test_frontend_facilities_copiercallbackdefinition_constructor_exists():
    assert callable(frontend_facilities_CopierCallbackDefinition.__init__)


def test_frontend_facilities_copiercallbackdefinition_constructor_args():
    sig = inspect.signature(frontend_facilities_CopierCallbackDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "stop" in params, "Missing parameter 'stop'"

def test_frontend_facilities_copiercallbackdefinition_has_stop():
    assert hasattr(frontend_facilities_CopierCallbackDefinition, "stop")
    descriptor = None
    for klass in frontend_facilities_CopierCallbackDefinition.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)



def test_facilities_copiercallbackdefinition_is_not_abstract():
    assert not inspect.isabstract(facilities_CopierCallbackDefinition)


def test_facilities_copiercallbackdefinition_constructor_exists():
    assert callable(facilities_CopierCallbackDefinition.__init__)


def test_facilities_copiercallbackdefinition_constructor_args():
    sig = inspect.signature(facilities_CopierCallbackDefinition.__init__)
    params = list(sig.parameters.keys())



def test_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_template_constructor_exists():
    assert callable(Template.__init__)


def test_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_invoketransformation_is_not_abstract():
    assert not inspect.isabstract(InvokeTransformation)


def test_invoketransformation_constructor_exists():
    assert callable(InvokeTransformation.__init__)


def test_invoketransformation_constructor_args():
    sig = inspect.signature(InvokeTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_invokeexternal_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_InvokeExternal)


def test_frontend_qool_invokeexternal_constructor_exists():
    assert callable(frontend_qool_InvokeExternal.__init__)


def test_frontend_qool_invokeexternal_constructor_args():
    sig = inspect.signature(frontend_qool_InvokeExternal.__init__)
    params = list(sig.parameters.keys())
    assert "queueName" in params, "Missing parameter 'queueName'"
    assert "traceAttributeName" in params, "Missing parameter 'traceAttributeName'"

def test_frontend_qool_invokeexternal_has_queueName():
    assert hasattr(frontend_qool_InvokeExternal, "queueName")
    descriptor = None
    for klass in frontend_qool_InvokeExternal.__mro__:
        if "queueName" in klass.__dict__:
            descriptor = klass.__dict__["queueName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_qool_invokeexternal_has_traceAttributeName():
    assert hasattr(frontend_qool_InvokeExternal, "traceAttributeName")
    descriptor = None
    for klass in frontend_qool_InvokeExternal.__mro__:
        if "traceAttributeName" in klass.__dict__:
            descriptor = klass.__dict__["traceAttributeName"]
            break
    assert isinstance(descriptor, property)



def test_namedinvocationparameter_is_not_abstract():
    assert not inspect.isabstract(NamedInvocationParameter)


def test_namedinvocationparameter_constructor_exists():
    assert callable(NamedInvocationParameter.__init__)


def test_namedinvocationparameter_constructor_args():
    sig = inspect.signature(NamedInvocationParameter.__init__)
    params = list(sig.parameters.keys())



def test_invocationparameter_is_not_abstract():
    assert not inspect.isabstract(InvocationParameter)


def test_invocationparameter_constructor_exists():
    assert callable(InvocationParameter.__init__)


def test_invocationparameter_constructor_args():
    sig = inspect.signature(InvocationParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_namedinvocationparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_NamedInvocationParameter)


def test_frontend_qool_namedinvocationparameter_constructor_exists():
    assert callable(frontend_qool_NamedInvocationParameter.__init__)


def test_frontend_qool_namedinvocationparameter_constructor_args():
    sig = inspect.signature(frontend_qool_NamedInvocationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "formalName" in params, "Missing parameter 'formalName'"

def test_frontend_qool_namedinvocationparameter_has_formalName():
    assert hasattr(frontend_qool_NamedInvocationParameter, "formalName")
    descriptor = None
    for klass in frontend_qool_NamedInvocationParameter.__mro__:
        if "formalName" in klass.__dict__:
            descriptor = klass.__dict__["formalName"]
            break
    assert isinstance(descriptor, property)



def test_transformationdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(TransformationDefinitionParameter)


def test_transformationdefinitionparameter_constructor_exists():
    assert callable(TransformationDefinitionParameter.__init__)


def test_transformationdefinitionparameter_constructor_args():
    sig = inspect.signature(TransformationDefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_invocationparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_InvocationParameter)


def test_frontend_qool_invocationparameter_constructor_exists():
    assert callable(frontend_qool_InvocationParameter.__init__)


def test_frontend_qool_invocationparameter_constructor_args():
    sig = inspect.signature(frontend_qool_InvocationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "calleeModelName" in params, "Missing parameter 'calleeModelName'"

def test_frontend_qool_invocationparameter_has_calleeModelName():
    assert hasattr(frontend_qool_InvocationParameter, "calleeModelName")
    descriptor = None
    for klass in frontend_qool_InvocationParameter.__mro__:
        if "calleeModelName" in klass.__dict__:
            descriptor = klass.__dict__["calleeModelName"]
            break
    assert isinstance(descriptor, property)



def test_frontend_qool_invokeinternal_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_InvokeInternal)


def test_frontend_qool_invokeinternal_constructor_exists():
    assert callable(frontend_qool_InvokeInternal.__init__)


def test_frontend_qool_invokeinternal_constructor_args():
    sig = inspect.signature(frontend_qool_InvokeInternal.__init__)
    params = list(sig.parameters.keys())



def test_iteratorstatement_is_not_abstract():
    assert not inspect.isabstract(IteratorStatement)


def test_iteratorstatement_constructor_exists():
    assert callable(IteratorStatement.__init__)


def test_iteratorstatement_constructor_args():
    sig = inspect.signature(IteratorStatement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_foreachstatement_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_ForEachStatement)


def test_frontend_qool_foreachstatement_constructor_exists():
    assert callable(frontend_qool_ForEachStatement.__init__)


def test_frontend_qool_foreachstatement_constructor_args():
    sig = inspect.signature(frontend_qool_ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_forallstatement_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_ForAllStatement)


def test_frontend_qool_forallstatement_constructor_exists():
    assert callable(frontend_qool_ForAllStatement.__init__)


def test_frontend_qool_forallstatement_constructor_args():
    sig = inspect.signature(frontend_qool_ForAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_core_statement_is_not_abstract():
    assert not inspect.isabstract(core_Statement)


def test_core_statement_constructor_exists():
    assert callable(core_Statement.__init__)


def test_core_statement_constructor_args():
    sig = inspect.signature(core_Statement.__init__)
    params = list(sig.parameters.keys())



def test_typeexpression_is_not_abstract():
    assert not inspect.isabstract(TypeExpression)


def test_typeexpression_constructor_exists():
    assert callable(TypeExpression.__init__)


def test_typeexpression_constructor_args():
    sig = inspect.signature(TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_queueoptimization_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_QueueOptimization)


def test_frontend_qool_queueoptimization_constructor_exists():
    assert callable(frontend_qool_QueueOptimization.__init__)


def test_frontend_qool_queueoptimization_constructor_args():
    sig = inspect.signature(frontend_qool_QueueOptimization.__init__)
    params = list(sig.parameters.keys())



def test_queueoptimization_is_not_abstract():
    assert not inspect.isabstract(QueueOptimization)


def test_queueoptimization_constructor_exists():
    assert callable(QueueOptimization.__init__)


def test_queueoptimization_constructor_args():
    sig = inspect.signature(QueueOptimization.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_accessbyfeatureoptimization_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_AccessByFeatureOptimization)


def test_frontend_qool_accessbyfeatureoptimization_constructor_exists():
    assert callable(frontend_qool_AccessByFeatureOptimization.__init__)


def test_frontend_qool_accessbyfeatureoptimization_constructor_args():
    sig = inspect.signature(frontend_qool_AccessByFeatureOptimization.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "force" in params, "Missing parameter 'force'"

def test_frontend_qool_accessbyfeatureoptimization_has_featureName():
    assert hasattr(frontend_qool_AccessByFeatureOptimization, "featureName")
    descriptor = None
    for klass in frontend_qool_AccessByFeatureOptimization.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_qool_accessbyfeatureoptimization_has_force():
    assert hasattr(frontend_qool_AccessByFeatureOptimization, "force")
    descriptor = None
    for klass in frontend_qool_AccessByFeatureOptimization.__mro__:
        if "force" in klass.__dict__:
            descriptor = klass.__dict__["force"]
            break
    assert isinstance(descriptor, property)



def test_frontend_qool_matchpredicate_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_MatchPredicate)


def test_frontend_qool_matchpredicate_constructor_exists():
    assert callable(frontend_qool_MatchPredicate.__init__)


def test_frontend_qool_matchpredicate_constructor_args():
    sig = inspect.signature(frontend_qool_MatchPredicate.__init__)
    params = list(sig.parameters.keys())



def test_matchpredicate_is_not_abstract():
    assert not inspect.isabstract(MatchPredicate)


def test_matchpredicate_constructor_exists():
    assert callable(MatchPredicate.__init__)


def test_matchpredicate_constructor_args():
    sig = inspect.signature(MatchPredicate.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_kindofpredicate_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_KindOfPredicate)


def test_frontend_qool_kindofpredicate_constructor_exists():
    assert callable(frontend_qool_KindOfPredicate.__init__)


def test_frontend_qool_kindofpredicate_constructor_args():
    sig = inspect.signature(frontend_qool_KindOfPredicate.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_propertyequalspredicate_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_PropertyEqualsPredicate)


def test_frontend_qool_propertyequalspredicate_constructor_exists():
    assert callable(frontend_qool_PropertyEqualsPredicate.__init__)


def test_frontend_qool_propertyequalspredicate_constructor_args():
    sig = inspect.signature(frontend_qool_PropertyEqualsPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_frontend_qool_propertyequalspredicate_has_propertyName():
    assert hasattr(frontend_qool_PropertyEqualsPredicate, "propertyName")
    descriptor = None
    for klass in frontend_qool_PropertyEqualsPredicate.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_mappings_metamodelelementref_is_not_abstract():
    assert not inspect.isabstract(mappings_MetamodelElementRef)


def test_mappings_metamodelelementref_constructor_exists():
    assert callable(mappings_MetamodelElementRef.__init__)


def test_mappings_metamodelelementref_constructor_args():
    sig = inspect.signature(mappings_MetamodelElementRef.__init__)
    params = list(sig.parameters.keys())



def test_metamodelelementref_is_not_abstract():
    assert not inspect.isabstract(MetamodelElementRef)


def test_metamodelelementref_constructor_exists():
    assert callable(MetamodelElementRef.__init__)


def test_metamodelelementref_constructor_args():
    sig = inspect.signature(MetamodelElementRef.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_attributeref_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeRef)


def test_frontend_mappings_attributeref_constructor_exists():
    assert callable(frontend_mappings_AttributeRef.__init__)


def test_frontend_mappings_attributeref_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeRef.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend_mappings_attributeref_has_featureName():
    assert hasattr(frontend_mappings_AttributeRef, "featureName")
    descriptor = None
    for klass in frontend_mappings_AttributeRef.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_mappings_attributeref_has_multivalued():
    assert hasattr(frontend_mappings_AttributeRef, "multivalued")
    descriptor = None
    for klass in frontend_mappings_AttributeRef.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_classref_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_ClassRef)


def test_frontend_mappings_classref_constructor_exists():
    assert callable(frontend_mappings_ClassRef.__init__)


def test_frontend_mappings_classref_constructor_args():
    sig = inspect.signature(frontend_mappings_ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_metamodelelementref_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_MetamodelElementRef)


def test_frontend_mappings_metamodelelementref_constructor_exists():
    assert callable(frontend_mappings_MetamodelElementRef.__init__)


def test_frontend_mappings_metamodelelementref_constructor_args():
    sig = inspect.signature(frontend_mappings_MetamodelElementRef.__init__)
    params = list(sig.parameters.keys())



def test_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(DefaultValue)


def test_defaultvalue_constructor_exists():
    assert callable(DefaultValue.__init__)


def test_defaultvalue_constructor_args():
    sig = inspect.signature(DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_intdefaultvalue_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_IntDefaultValue)


def test_frontend_mappings_intdefaultvalue_constructor_exists():
    assert callable(frontend_mappings_IntDefaultValue.__init__)


def test_frontend_mappings_intdefaultvalue_constructor_args():
    sig = inspect.signature(frontend_mappings_IntDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_frontend_mappings_intdefaultvalue_has_defaultValue():
    assert hasattr(frontend_mappings_IntDefaultValue, "defaultValue")
    descriptor = None
    for klass in frontend_mappings_IntDefaultValue.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_segment_is_not_abstract():
    assert not inspect.isabstract(Segment)


def test_segment_constructor_exists():
    assert callable(Segment.__init__)


def test_segment_constructor_args():
    sig = inspect.signature(Segment.__init__)
    params = list(sig.parameters.keys())



def test_qoolqueue_is_not_abstract():
    assert not inspect.isabstract(QoolQueue)


def test_qoolqueue_constructor_exists():
    assert callable(QoolQueue.__init__)


def test_qoolqueue_constructor_args():
    sig = inspect.signature(QoolQueue.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_localqueue_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_LocalQueue)


def test_frontend_qool_localqueue_constructor_exists():
    assert callable(frontend_qool_LocalQueue.__init__)


def test_frontend_qool_localqueue_constructor_args():
    sig = inspect.signature(frontend_qool_LocalQueue.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_modelelementqueue_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_ModelElementQueue)


def test_frontend_qool_modelelementqueue_constructor_exists():
    assert callable(frontend_qool_ModelElementQueue.__init__)


def test_frontend_qool_modelelementqueue_constructor_args():
    sig = inspect.signature(frontend_qool_ModelElementQueue.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_referenceref_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_ReferenceRef)


def test_frontend_mappings_referenceref_constructor_exists():
    assert callable(frontend_mappings_ReferenceRef.__init__)


def test_frontend_mappings_referenceref_constructor_args():
    sig = inspect.signature(frontend_mappings_ReferenceRef.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend_mappings_referenceref_has_featureName():
    assert hasattr(frontend_mappings_ReferenceRef, "featureName")
    descriptor = None
    for klass in frontend_mappings_ReferenceRef.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_mappings_referenceref_has_multivalued():
    assert hasattr(frontend_mappings_ReferenceRef, "multivalued")
    descriptor = None
    for klass in frontend_mappings_ReferenceRef.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_attributemodifier_is_not_abstract():
    assert not inspect.isabstract(AttributeModifier)


def test_attributemodifier_constructor_exists():
    assert callable(AttributeModifier.__init__)


def test_attributemodifier_constructor_args():
    sig = inspect.signature(AttributeModifier.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_DefaultValue)


def test_frontend_mappings_defaultvalue_constructor_exists():
    assert callable(frontend_mappings_DefaultValue.__init__)


def test_frontend_mappings_defaultvalue_constructor_args():
    sig = inspect.signature(frontend_mappings_DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_class2class_is_not_abstract():
    assert not inspect.isabstract(Class2Class)


def test_class2class_constructor_exists():
    assert callable(Class2Class.__init__)


def test_class2class_constructor_args():
    sig = inspect.signature(Class2Class.__init__)
    params = list(sig.parameters.keys())



def test_mappings_attributerightpart_is_not_abstract():
    assert not inspect.isabstract(mappings_AttributeRightPart)


def test_mappings_attributerightpart_constructor_exists():
    assert callable(mappings_AttributeRightPart.__init__)


def test_mappings_attributerightpart_constructor_args():
    sig = inspect.signature(mappings_AttributeRightPart.__init__)
    params = list(sig.parameters.keys())



def test_mappings_feature2feature_is_not_abstract():
    assert not inspect.isabstract(mappings_Feature2Feature)


def test_mappings_feature2feature_constructor_exists():
    assert callable(mappings_Feature2Feature.__init__)


def test_mappings_feature2feature_constructor_args():
    sig = inspect.signature(mappings_Feature2Feature.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_featureref_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_FeatureRef)


def test_frontend_mappings_featureref_constructor_exists():
    assert callable(frontend_mappings_FeatureRef.__init__)


def test_frontend_mappings_featureref_constructor_args():
    sig = inspect.signature(frontend_mappings_FeatureRef.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend_mappings_featureref_has_featureName():
    assert hasattr(frontend_mappings_FeatureRef, "featureName")
    descriptor = None
    for klass in frontend_mappings_FeatureRef.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_mappings_featureref_has_multivalued():
    assert hasattr(frontend_mappings_FeatureRef, "multivalued")
    descriptor = None
    for klass in frontend_mappings_FeatureRef.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_attribute2attribute_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Attribute2Attribute)


def test_frontend_mappings_attribute2attribute_constructor_exists():
    assert callable(frontend_mappings_Attribute2Attribute.__init__)


def test_frontend_mappings_attribute2attribute_constructor_args():
    sig = inspect.signature(frontend_mappings_Attribute2Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_frontend_mappings_attribute2attribute_has_cardinality():
    assert hasattr(frontend_mappings_Attribute2Attribute, "cardinality")
    descriptor = None
    for klass in frontend_mappings_Attribute2Attribute.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_join_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Join)


def test_frontend_mappings_join_constructor_exists():
    assert callable(frontend_mappings_Join.__init__)


def test_frontend_mappings_join_constructor_args():
    sig = inspect.signature(frontend_mappings_Join.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_split_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Split)


def test_frontend_mappings_split_constructor_exists():
    assert callable(frontend_mappings_Split.__init__)


def test_frontend_mappings_split_constructor_args():
    sig = inspect.signature(frontend_mappings_Split.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_convertmodifier_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_ConvertModifier)


def test_frontend_mappings_convertmodifier_constructor_exists():
    assert callable(frontend_mappings_ConvertModifier.__init__)


def test_frontend_mappings_convertmodifier_constructor_args():
    sig = inspect.signature(frontend_mappings_ConvertModifier.__init__)
    params = list(sig.parameters.keys())
    assert "converter" in params, "Missing parameter 'converter'"

def test_frontend_mappings_convertmodifier_has_converter():
    assert hasattr(frontend_mappings_ConvertModifier, "converter")
    descriptor = None
    for klass in frontend_mappings_ConvertModifier.__mro__:
        if "converter" in klass.__dict__:
            descriptor = klass.__dict__["converter"]
            break
    assert isinstance(descriptor, property)



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_attributemodifier_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeModifier)


def test_frontend_mappings_attributemodifier_constructor_exists():
    assert callable(frontend_mappings_AttributeModifier.__init__)


def test_frontend_mappings_attributemodifier_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeModifier.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_modifier_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Modifier)


def test_frontend_mappings_modifier_constructor_exists():
    assert callable(frontend_mappings_Modifier.__init__)


def test_frontend_mappings_modifier_constructor_args():
    sig = inspect.signature(frontend_mappings_Modifier.__init__)
    params = list(sig.parameters.keys())



def test_classref_is_not_abstract():
    assert not inspect.isabstract(ClassRef)


def test_classref_constructor_exists():
    assert callable(ClassRef.__init__)


def test_classref_constructor_args():
    sig = inspect.signature(ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_referenceref_is_not_abstract():
    assert not inspect.isabstract(ReferenceRef)


def test_referenceref_constructor_exists():
    assert callable(ReferenceRef.__init__)


def test_referenceref_constructor_args():
    sig = inspect.signature(ReferenceRef.__init__)
    params = list(sig.parameters.keys())



def test_classmapping_is_not_abstract():
    assert not inspect.isabstract(ClassMapping)


def test_classmapping_constructor_exists():
    assert callable(ClassMapping.__init__)


def test_classmapping_constructor_args():
    sig = inspect.signature(ClassMapping.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_class2class_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Class2Class)


def test_frontend_mappings_class2class_constructor_exists():
    assert callable(frontend_mappings_Class2Class.__init__)


def test_frontend_mappings_class2class_constructor_args():
    sig = inspect.signature(frontend_mappings_Class2Class.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_frontend_mappings_class2class_has_cardinality():
    assert hasattr(frontend_mappings_Class2Class, "cardinality")
    descriptor = None
    for klass in frontend_mappings_Class2Class.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_segment_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_Segment)


def test_frontend_qool_segment_constructor_exists():
    assert callable(frontend_qool_Segment.__init__)


def test_frontend_qool_segment_constructor_args():
    sig = inspect.signature(frontend_qool_Segment.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_tag_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Tag)


def test_frontend_mappings_tag_constructor_exists():
    assert callable(frontend_mappings_Tag.__init__)


def test_frontend_mappings_tag_constructor_args():
    sig = inspect.signature(frontend_mappings_Tag.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_converter_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Converter)


def test_frontend_mappings_converter_constructor_exists():
    assert callable(frontend_mappings_Converter.__init__)


def test_frontend_mappings_converter_constructor_args():
    sig = inspect.signature(frontend_mappings_Converter.__init__)
    params = list(sig.parameters.keys())
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "converterName" in params, "Missing parameter 'converterName'"

def test_frontend_mappings_converter_has_isExternal():
    assert hasattr(frontend_mappings_Converter, "isExternal")
    descriptor = None
    for klass in frontend_mappings_Converter.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_frontend_mappings_converter_has_converterName():
    assert hasattr(frontend_mappings_Converter, "converterName")
    descriptor = None
    for klass in frontend_mappings_Converter.__mro__:
        if "converterName" in klass.__dict__:
            descriptor = klass.__dict__["converterName"]
            break
    assert isinstance(descriptor, property)



def test_resolvelink_is_not_abstract():
    assert not inspect.isabstract(ResolveLink)


def test_resolvelink_constructor_exists():
    assert callable(ResolveLink.__init__)


def test_resolvelink_constructor_args():
    sig = inspect.signature(ResolveLink.__init__)
    params = list(sig.parameters.keys())



def test_attribute2attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute2Attribute)


def test_attribute2attribute_constructor_exists():
    assert callable(Attribute2Attribute.__init__)


def test_attribute2attribute_constructor_args():
    sig = inspect.signature(Attribute2Attribute.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_c2cmodifier_is_not_abstract():
    assert not inspect.isabstract(C2CModifier)


def test_c2cmodifier_constructor_exists():
    assert callable(C2CModifier.__init__)


def test_c2cmodifier_constructor_args():
    sig = inspect.signature(C2CModifier.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_relatedby_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_RelatedBy)


def test_frontend_mappings_relatedby_constructor_exists():
    assert callable(frontend_mappings_RelatedBy.__init__)


def test_frontend_mappings_relatedby_constructor_args():
    sig = inspect.signature(frontend_mappings_RelatedBy.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_equalityfilter_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_EqualityFilter)


def test_frontend_mappings_equalityfilter_constructor_exists():
    assert callable(frontend_mappings_EqualityFilter.__init__)


def test_frontend_mappings_equalityfilter_constructor_args():
    sig = inspect.signature(frontend_mappings_EqualityFilter.__init__)
    params = list(sig.parameters.keys())
    assert "filter" in params, "Missing parameter 'filter'"

def test_frontend_mappings_equalityfilter_has_filter():
    assert hasattr(frontend_mappings_EqualityFilter, "filter")
    descriptor = None
    for klass in frontend_mappings_EqualityFilter.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_linkedby_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_LinkedBy)


def test_frontend_mappings_linkedby_constructor_exists():
    assert callable(frontend_mappings_LinkedBy.__init__)


def test_frontend_mappings_linkedby_constructor_args():
    sig = inspect.signature(frontend_mappings_LinkedBy.__init__)
    params = list(sig.parameters.keys())



def test_mappingelement_is_not_abstract():
    assert not inspect.isabstract(MappingElement)


def test_mappingelement_constructor_exists():
    assert callable(MappingElement.__init__)


def test_mappingelement_constructor_args():
    sig = inspect.signature(MappingElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_c2cmodifier_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_C2CModifier)


def test_frontend_mappings_c2cmodifier_constructor_exists():
    assert callable(frontend_mappings_C2CModifier.__init__)


def test_frontend_mappings_c2cmodifier_constructor_args():
    sig = inspect.signature(frontend_mappings_C2CModifier.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_usedeclaration_is_not_abstract():
    assert not inspect.isabstract(UseDeclaration)


def test_usedeclaration_constructor_exists():
    assert callable(UseDeclaration.__init__)


def test_usedeclaration_constructor_args():
    sig = inspect.signature(UseDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_matchedelement_is_not_abstract():
    assert not inspect.isabstract(MatchedElement)


def test_matchedelement_constructor_exists():
    assert callable(MatchedElement.__init__)


def test_matchedelement_constructor_args():
    sig = inspect.signature(MatchedElement.__init__)
    params = list(sig.parameters.keys())



def test_mappings_mappingvariable_is_not_abstract():
    assert not inspect.isabstract(mappings_MappingVariable)


def test_mappings_mappingvariable_constructor_exists():
    assert callable(mappings_MappingVariable.__init__)


def test_mappings_mappingvariable_constructor_args():
    sig = inspect.signature(mappings_MappingVariable.__init__)
    params = list(sig.parameters.keys())



def test_core_classuse_is_not_abstract():
    assert not inspect.isabstract(core_ClassUse)


def test_core_classuse_constructor_exists():
    assert callable(core_ClassUse.__init__)


def test_core_classuse_constructor_args():
    sig = inspect.signature(core_ClassUse.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_matchedelement_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_MatchedElement)


def test_frontend_mappings_matchedelement_constructor_exists():
    assert callable(frontend_mappings_MatchedElement.__init__)


def test_frontend_mappings_matchedelement_constructor_args():
    sig = inspect.signature(frontend_mappings_MatchedElement.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_attributerightpart_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeRightPart)


def test_frontend_mappings_attributerightpart_constructor_exists():
    assert callable(frontend_mappings_AttributeRightPart.__init__)


def test_frontend_mappings_attributerightpart_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeRightPart.__init__)
    params = list(sig.parameters.keys())



def test_attributerightpart_is_not_abstract():
    assert not inspect.isabstract(AttributeRightPart)


def test_attributerightpart_constructor_exists():
    assert callable(AttributeRightPart.__init__)


def test_attributerightpart_constructor_args():
    sig = inspect.signature(AttributeRightPart.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_attributeisresolvelink_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeIsResolveLink)


def test_frontend_mappings_attributeisresolvelink_constructor_exists():
    assert callable(frontend_mappings_AttributeIsResolveLink.__init__)


def test_frontend_mappings_attributeisresolvelink_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeIsResolveLink.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_attributeisdouble_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeIsDouble)


def test_frontend_mappings_attributeisdouble_constructor_exists():
    assert callable(frontend_mappings_AttributeIsDouble.__init__)


def test_frontend_mappings_attributeisdouble_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeIsDouble.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_frontend_mappings_attributeisdouble_has_doubleValue():
    assert hasattr(frontend_mappings_AttributeIsDouble, "doubleValue")
    descriptor = None
    for klass in frontend_mappings_AttributeIsDouble.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_attributeisboolean_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeIsBoolean)


def test_frontend_mappings_attributeisboolean_constructor_exists():
    assert callable(frontend_mappings_AttributeIsBoolean.__init__)


def test_frontend_mappings_attributeisboolean_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeIsBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "boolValue" in params, "Missing parameter 'boolValue'"

def test_frontend_mappings_attributeisboolean_has_boolValue():
    assert hasattr(frontend_mappings_AttributeIsBoolean, "boolValue")
    descriptor = None
    for klass in frontend_mappings_AttributeIsBoolean.__mro__:
        if "boolValue" in klass.__dict__:
            descriptor = klass.__dict__["boolValue"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_attributeisstring_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeIsString)


def test_frontend_mappings_attributeisstring_constructor_exists():
    assert callable(frontend_mappings_AttributeIsString.__init__)


def test_frontend_mappings_attributeisstring_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeIsString.__init__)
    params = list(sig.parameters.keys())
    assert "strValue" in params, "Missing parameter 'strValue'"

def test_frontend_mappings_attributeisstring_has_strValue():
    assert hasattr(frontend_mappings_AttributeIsString, "strValue")
    descriptor = None
    for klass in frontend_mappings_AttributeIsString.__mro__:
        if "strValue" in klass.__dict__:
            descriptor = klass.__dict__["strValue"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_attributeisinteger_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeIsInteger)


def test_frontend_mappings_attributeisinteger_constructor_exists():
    assert callable(frontend_mappings_AttributeIsInteger.__init__)


def test_frontend_mappings_attributeisinteger_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeIsInteger.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_frontend_mappings_attributeisinteger_has_intValue():
    assert hasattr(frontend_mappings_AttributeIsInteger, "intValue")
    descriptor = None
    for klass in frontend_mappings_AttributeIsInteger.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_attributeref_is_not_abstract():
    assert not inspect.isabstract(AttributeRef)


def test_attributeref_constructor_exists():
    assert callable(AttributeRef.__init__)


def test_attributeref_constructor_args():
    sig = inspect.signature(AttributeRef.__init__)
    params = list(sig.parameters.keys())



def test_feature2feature_is_not_abstract():
    assert not inspect.isabstract(Feature2Feature)


def test_feature2feature_constructor_exists():
    assert callable(Feature2Feature.__init__)


def test_feature2feature_constructor_args():
    sig = inspect.signature(Feature2Feature.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_reference2reference_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Reference2Reference)


def test_frontend_mappings_reference2reference_constructor_exists():
    assert callable(frontend_mappings_Reference2Reference.__init__)


def test_frontend_mappings_reference2reference_constructor_args():
    sig = inspect.signature(frontend_mappings_Reference2Reference.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"
    assert "resolverName" in params, "Missing parameter 'resolverName'"

def test_frontend_mappings_reference2reference_has_cardinality():
    assert hasattr(frontend_mappings_Reference2Reference, "cardinality")
    descriptor = None
    for klass in frontend_mappings_Reference2Reference.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)

def test_frontend_mappings_reference2reference_has_resolverName():
    assert hasattr(frontend_mappings_Reference2Reference, "resolverName")
    descriptor = None
    for klass in frontend_mappings_Reference2Reference.__mro__:
        if "resolverName" in klass.__dict__:
            descriptor = klass.__dict__["resolverName"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_attributemapping_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_AttributeMapping)


def test_frontend_mappings_attributemapping_constructor_exists():
    assert callable(frontend_mappings_AttributeMapping.__init__)


def test_frontend_mappings_attributemapping_constructor_args():
    sig = inspect.signature(frontend_mappings_AttributeMapping.__init__)
    params = list(sig.parameters.keys())



def test_converter_is_not_abstract():
    assert not inspect.isabstract(Converter)


def test_converter_constructor_exists():
    assert callable(Converter.__init__)


def test_converter_constructor_args():
    sig = inspect.signature(Converter.__init__)
    params = list(sig.parameters.keys())



def test_featureref_is_not_abstract():
    assert not inspect.isabstract(FeatureRef)


def test_featureref_constructor_exists():
    assert callable(FeatureRef.__init__)


def test_featureref_constructor_args():
    sig = inspect.signature(FeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_feature2feature_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Feature2Feature)


def test_frontend_mappings_feature2feature_constructor_exists():
    assert callable(frontend_mappings_Feature2Feature.__init__)


def test_frontend_mappings_feature2feature_constructor_args():
    sig = inspect.signature(frontend_mappings_Feature2Feature.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_classmapping_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_ClassMapping)


def test_frontend_mappings_classmapping_constructor_exists():
    assert callable(frontend_mappings_ClassMapping.__init__)


def test_frontend_mappings_classmapping_constructor_args():
    sig = inspect.signature(frontend_mappings_ClassMapping.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_poutputvariable_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_POutputVariable)


def test_frontend_patterns_poutputvariable_constructor_exists():
    assert callable(frontend_patterns_POutputVariable.__init__)


def test_frontend_patterns_poutputvariable_constructor_args():
    sig = inspect.signature(frontend_patterns_POutputVariable.__init__)
    params = list(sig.parameters.keys())



def test_poutputvariable_is_not_abstract():
    assert not inspect.isabstract(POutputVariable)


def test_poutputvariable_constructor_exists():
    assert callable(POutputVariable.__init__)


def test_poutputvariable_constructor_args():
    sig = inspect.signature(POutputVariable.__init__)
    params = list(sig.parameters.keys())



def test_pobject_is_not_abstract():
    assert not inspect.isabstract(PObject)


def test_pobject_constructor_exists():
    assert callable(PObject.__init__)


def test_pobject_constructor_args():
    sig = inspect.signature(PObject.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_core_transformationdefinition_is_not_abstract():
    assert not inspect.isabstract(core_TransformationDefinition)


def test_core_transformationdefinition_constructor_exists():
    assert callable(core_TransformationDefinition.__init__)


def test_core_transformationdefinition_constructor_args():
    sig = inspect.signature(core_TransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_chain_availabletransformation_is_not_abstract():
    assert not inspect.isabstract(chain_AvailableTransformation)


def test_chain_availabletransformation_constructor_exists():
    assert callable(chain_AvailableTransformation.__init__)


def test_chain_availabletransformation_constructor_args():
    sig = inspect.signature(chain_AvailableTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_chain_compositetransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_chain_CompositeTransformation)


def test_frontend_chain_compositetransformation_constructor_exists():
    assert callable(frontend_chain_CompositeTransformation.__init__)


def test_frontend_chain_compositetransformation_constructor_args():
    sig = inspect.signature(frontend_chain_CompositeTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_chain_availabletransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_chain_AvailableTransformation)


def test_frontend_chain_availabletransformation_constructor_exists():
    assert callable(frontend_chain_AvailableTransformation.__init__)


def test_frontend_chain_availabletransformation_constructor_args():
    sig = inspect.signature(frontend_chain_AvailableTransformation.__init__)
    params = list(sig.parameters.keys())



def test_representmodel_is_not_abstract():
    assert not inspect.isabstract(RepresentModel)


def test_representmodel_constructor_exists():
    assert callable(RepresentModel.__init__)


def test_representmodel_constructor_args():
    sig = inspect.signature(RepresentModel.__init__)
    params = list(sig.parameters.keys())



def test_availabletransformation_is_not_abstract():
    assert not inspect.isabstract(AvailableTransformation)


def test_availabletransformation_constructor_exists():
    assert callable(AvailableTransformation.__init__)


def test_availabletransformation_constructor_args():
    sig = inspect.signature(AvailableTransformation.__init__)
    params = list(sig.parameters.keys())



def test_delegate_is_not_abstract():
    assert not inspect.isabstract(Delegate)


def test_delegate_constructor_exists():
    assert callable(Delegate.__init__)


def test_delegate_constructor_args():
    sig = inspect.signature(Delegate.__init__)
    params = list(sig.parameters.keys())



def test_preference_is_not_abstract():
    assert not inspect.isabstract(PReference)


def test_preference_constructor_exists():
    assert callable(PReference.__init__)


def test_preference_constructor_args():
    sig = inspect.signature(PReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_collectionreference_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_CollectionReference)


def test_frontend_patterns_collectionreference_constructor_exists():
    assert callable(frontend_patterns_CollectionReference.__init__)


def test_frontend_patterns_collectionreference_constructor_args():
    sig = inspect.signature(frontend_patterns_CollectionReference.__init__)
    params = list(sig.parameters.keys())



def test_pfeature_is_not_abstract():
    assert not inspect.isabstract(PFeature)


def test_pfeature_constructor_exists():
    assert callable(PFeature.__init__)


def test_pfeature_constructor_args():
    sig = inspect.signature(PFeature.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_preference_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_PReference)


def test_frontend_patterns_preference_constructor_exists():
    assert callable(frontend_patterns_PReference.__init__)


def test_frontend_patterns_preference_constructor_args():
    sig = inspect.signature(frontend_patterns_PReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_pattribute_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_PAttribute)


def test_frontend_patterns_pattribute_constructor_exists():
    assert callable(frontend_patterns_PAttribute.__init__)


def test_frontend_patterns_pattribute_constructor_args():
    sig = inspect.signature(frontend_patterns_PAttribute.__init__)
    params = list(sig.parameters.keys())



def test_methodself_is_not_abstract():
    assert not inspect.isabstract(MethodSelf)


def test_methodself_constructor_exists():
    assert callable(MethodSelf.__init__)


def test_methodself_constructor_args():
    sig = inspect.signature(MethodSelf.__init__)
    params = list(sig.parameters.keys())



def test_methodparameter_is_not_abstract():
    assert not inspect.isabstract(MethodParameter)


def test_methodparameter_constructor_exists():
    assert callable(MethodParameter.__init__)


def test_methodparameter_constructor_args():
    sig = inspect.signature(MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_methoddefinition_is_not_abstract():
    assert not inspect.isabstract(MethodDefinition)


def test_methoddefinition_constructor_exists():
    assert callable(MethodDefinition.__init__)


def test_methoddefinition_constructor_args():
    sig = inspect.signature(MethodDefinition.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_templateparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_TemplateParameter)


def test_frontend_tao_templateparameter_constructor_exists():
    assert callable(frontend_tao_TemplateParameter.__init__)


def test_frontend_tao_templateparameter_constructor_args():
    sig = inspect.signature(frontend_tao_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_mappingvariable_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_MappingVariable)


def test_frontend_mappings_mappingvariable_constructor_exists():
    assert callable(frontend_mappings_MappingVariable.__init__)


def test_frontend_mappings_mappingvariable_constructor_args():
    sig = inspect.signature(frontend_mappings_MappingVariable.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_objectsourcevariable_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_ObjectSourceVariable)


def test_frontend_tao_objectsourcevariable_constructor_exists():
    assert callable(frontend_tao_ObjectSourceVariable.__init__)


def test_frontend_tao_objectsourcevariable_constructor_args():
    sig = inspect.signature(frontend_tao_ObjectSourceVariable.__init__)
    params = list(sig.parameters.keys())



def test_frontend_attribution_ruleself_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_RuleSelf)


def test_frontend_attribution_ruleself_constructor_exists():
    assert callable(frontend_attribution_RuleSelf.__init__)


def test_frontend_attribution_ruleself_constructor_args():
    sig = inspect.signature(frontend_attribution_RuleSelf.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_matchexpression_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_MatchExpression)


def test_frontend_qool_matchexpression_constructor_exists():
    assert callable(frontend_qool_MatchExpression.__init__)


def test_frontend_qool_matchexpression_constructor_args():
    sig = inspect.signature(frontend_qool_MatchExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_attribution_attributeuse_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_AttributeUse)


def test_frontend_attribution_attributeuse_constructor_exists():
    assert callable(frontend_attribution_AttributeUse.__init__)


def test_frontend_attribution_attributeuse_constructor_args():
    sig = inspect.signature(frontend_attribution_AttributeUse.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_invoketransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_InvokeTransformation)


def test_frontend_qool_invoketransformation_constructor_exists():
    assert callable(frontend_qool_InvokeTransformation.__init__)


def test_frontend_qool_invoketransformation_constructor_args():
    sig = inspect.signature(frontend_qool_InvokeTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "transformationName" in params, "Missing parameter 'transformationName'"
    assert "entryPointName" in params, "Missing parameter 'entryPointName'"

def test_frontend_qool_invoketransformation_has_transformationName():
    assert hasattr(frontend_qool_InvokeTransformation, "transformationName")
    descriptor = None
    for klass in frontend_qool_InvokeTransformation.__mro__:
        if "transformationName" in klass.__dict__:
            descriptor = klass.__dict__["transformationName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_qool_invoketransformation_has_entryPointName():
    assert hasattr(frontend_qool_InvokeTransformation, "entryPointName")
    descriptor = None
    for klass in frontend_qool_InvokeTransformation.__mro__:
        if "entryPointName" in klass.__dict__:
            descriptor = klass.__dict__["entryPointName"]
            break
    assert isinstance(descriptor, property)



def test_frontend_facilities_copier_is_not_abstract():
    assert not inspect.isabstract(frontend_facilities_Copier)


def test_frontend_facilities_copier_constructor_exists():
    assert callable(frontend_facilities_Copier.__init__)


def test_frontend_facilities_copier_constructor_args():
    sig = inspect.signature(frontend_facilities_Copier.__init__)
    params = list(sig.parameters.keys())



def test_ruleself_is_not_abstract():
    assert not inspect.isabstract(RuleSelf)


def test_ruleself_constructor_exists():
    assert callable(RuleSelf.__init__)


def test_ruleself_constructor_args():
    sig = inspect.signature(RuleSelf.__init__)
    params = list(sig.parameters.keys())



def test_core_representmodel_is_not_abstract():
    assert not inspect.isabstract(core_RepresentModel)


def test_core_representmodel_constructor_exists():
    assert callable(core_RepresentModel.__init__)


def test_core_representmodel_constructor_args():
    sig = inspect.signature(core_RepresentModel.__init__)
    params = list(sig.parameters.keys())



def test_transformationexecution_is_not_abstract():
    assert not inspect.isabstract(TransformationExecution)


def test_transformationexecution_constructor_exists():
    assert callable(TransformationExecution.__init__)


def test_transformationexecution_constructor_args():
    sig = inspect.signature(TransformationExecution.__init__)
    params = list(sig.parameters.keys())



def test_generatedmodel_is_not_abstract():
    assert not inspect.isabstract(GeneratedModel)


def test_generatedmodel_constructor_exists():
    assert callable(GeneratedModel.__init__)


def test_generatedmodel_constructor_args():
    sig = inspect.signature(GeneratedModel.__init__)
    params = list(sig.parameters.keys())



def test_externaltransformation_is_not_abstract():
    assert not inspect.isabstract(ExternalTransformation)


def test_externaltransformation_constructor_exists():
    assert callable(ExternalTransformation.__init__)


def test_externaltransformation_constructor_args():
    sig = inspect.signature(ExternalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_compositetransformation_is_not_abstract():
    assert not inspect.isabstract(CompositeTransformation)


def test_compositetransformation_constructor_exists():
    assert callable(CompositeTransformation.__init__)


def test_compositetransformation_constructor_args():
    sig = inspect.signature(CompositeTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_imperative_methodparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_imperative_MethodParameter)


def test_frontend_imperative_methodparameter_constructor_exists():
    assert callable(frontend_imperative_MethodParameter.__init__)


def test_frontend_imperative_methodparameter_constructor_args():
    sig = inspect.signature(frontend_imperative_MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_imperative_methodself_is_not_abstract():
    assert not inspect.isabstract(frontend_imperative_MethodSelf)


def test_frontend_imperative_methodself_constructor_exists():
    assert callable(frontend_imperative_MethodSelf.__init__)


def test_frontend_imperative_methodself_constructor_args():
    sig = inspect.signature(frontend_imperative_MethodSelf.__init__)
    params = list(sig.parameters.keys())



def test_matcher_is_not_abstract():
    assert not inspect.isabstract(Matcher)


def test_matcher_constructor_exists():
    assert callable(Matcher.__init__)


def test_matcher_constructor_args():
    sig = inspect.signature(Matcher.__init__)
    params = list(sig.parameters.keys())



def test_core_namedelement_is_not_abstract():
    assert not inspect.isabstract(core_NamedElement)


def test_core_namedelement_constructor_exists():
    assert callable(core_NamedElement.__init__)


def test_core_namedelement_constructor_args():
    sig = inspect.signature(core_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_chain_generatedmodel_is_not_abstract():
    assert not inspect.isabstract(frontend_chain_GeneratedModel)


def test_frontend_chain_generatedmodel_constructor_exists():
    assert callable(frontend_chain_GeneratedModel.__init__)


def test_frontend_chain_generatedmodel_constructor_args():
    sig = inspect.signature(frontend_chain_GeneratedModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend_chain_externaltransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_chain_ExternalTransformation)


def test_frontend_chain_externaltransformation_constructor_exists():
    assert callable(frontend_chain_ExternalTransformation.__init__)


def test_frontend_chain_externaltransformation_constructor_args():
    sig = inspect.signature(frontend_chain_ExternalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_core_locatedelement_is_not_abstract():
    assert not inspect.isabstract(core_LocatedElement)


def test_core_locatedelement_constructor_exists():
    assert callable(core_LocatedElement.__init__)


def test_core_locatedelement_constructor_args():
    sig = inspect.signature(core_LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_template_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_Template)


def test_frontend_tao_template_constructor_exists():
    assert callable(frontend_tao_Template.__init__)


def test_frontend_tao_template_constructor_args():
    sig = inspect.signature(frontend_tao_Template.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_qoolqueue_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_QoolQueue)


def test_frontend_qool_qoolqueue_constructor_exists():
    assert callable(frontend_qool_QoolQueue.__init__)


def test_frontend_qool_qoolqueue_constructor_args():
    sig = inspect.signature(frontend_qool_QoolQueue.__init__)
    params = list(sig.parameters.keys())



def test_frontend_koan_koanrule_is_not_abstract():
    assert not inspect.isabstract(frontend_koan_KoanRule)


def test_frontend_koan_koanrule_constructor_exists():
    assert callable(frontend_koan_KoanRule.__init__)


def test_frontend_koan_koanrule_constructor_args():
    sig = inspect.signature(frontend_koan_KoanRule.__init__)
    params = list(sig.parameters.keys())



def test_koanrule_is_not_abstract():
    assert not inspect.isabstract(KoanRule)


def test_koanrule_constructor_exists():
    assert callable(KoanRule.__init__)


def test_koanrule_constructor_args():
    sig = inspect.signature(KoanRule.__init__)
    params = list(sig.parameters.keys())



def test_traceinterface_is_not_abstract():
    assert not inspect.isabstract(TraceInterface)


def test_traceinterface_constructor_exists():
    assert callable(TraceInterface.__init__)


def test_traceinterface_constructor_args():
    sig = inspect.signature(TraceInterface.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_assignment_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_Assignment)


def test_frontend_tao_assignment_constructor_exists():
    assert callable(frontend_tao_Assignment.__init__)


def test_frontend_tao_assignment_constructor_args():
    sig = inspect.signature(frontend_tao_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_emitstatement_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_EmitStatement)


def test_frontend_qool_emitstatement_constructor_exists():
    assert callable(frontend_qool_EmitStatement.__init__)


def test_frontend_qool_emitstatement_constructor_args():
    sig = inspect.signature(frontend_qool_EmitStatement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_attribution_attributeinit_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_AttributeInit)


def test_frontend_attribution_attributeinit_constructor_exists():
    assert callable(frontend_attribution_AttributeInit.__init__)


def test_frontend_attribution_attributeinit_constructor_args():
    sig = inspect.signature(frontend_attribution_AttributeInit.__init__)
    params = list(sig.parameters.keys())



def test_transformationdefinition_is_not_abstract():
    assert not inspect.isabstract(TransformationDefinition)


def test_transformationdefinition_constructor_exists():
    assert callable(TransformationDefinition.__init__)


def test_transformationdefinition_constructor_args():
    sig = inspect.signature(TransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend_chain_chaintransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_chain_ChainTransformation)


def test_frontend_chain_chaintransformation_constructor_exists():
    assert callable(frontend_chain_ChainTransformation.__init__)


def test_frontend_chain_chaintransformation_constructor_args():
    sig = inspect.signature(frontend_chain_ChainTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_imperative_imperativetransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_imperative_ImperativeTransformation)


def test_frontend_imperative_imperativetransformation_constructor_exists():
    assert callable(frontend_imperative_ImperativeTransformation.__init__)


def test_frontend_imperative_imperativetransformation_constructor_args():
    sig = inspect.signature(frontend_imperative_ImperativeTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_koan_koantransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_koan_KoanTransformation)


def test_frontend_koan_koantransformation_constructor_exists():
    assert callable(frontend_koan_KoanTransformation.__init__)


def test_frontend_koan_koantransformation_constructor_args():
    sig = inspect.signature(frontend_koan_KoanTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_taotransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_TaoTransformation)


def test_frontend_tao_taotransformation_constructor_exists():
    assert callable(frontend_tao_TaoTransformation.__init__)


def test_frontend_tao_taotransformation_constructor_args():
    sig = inspect.signature(frontend_tao_TaoTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_qooltransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_QoolTransformation)


def test_frontend_qool_qooltransformation_constructor_exists():
    assert callable(frontend_qool_QoolTransformation.__init__)


def test_frontend_qool_qooltransformation_constructor_args():
    sig = inspect.signature(frontend_qool_QoolTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_patternspecification_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_PatternSpecification)


def test_frontend_patterns_patternspecification_constructor_exists():
    assert callable(frontend_patterns_PatternSpecification.__init__)


def test_frontend_patterns_patternspecification_constructor_args():
    sig = inspect.signature(frontend_patterns_PatternSpecification.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_mappingtransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_MappingTransformation)


def test_frontend_mappings_mappingtransformation_constructor_exists():
    assert callable(frontend_mappings_MappingTransformation.__init__)


def test_frontend_mappings_mappingtransformation_constructor_args():
    sig = inspect.signature(frontend_mappings_MappingTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_script_scriptedtransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_script_ScriptedTransformation)


def test_frontend_script_scriptedtransformation_constructor_exists():
    assert callable(frontend_script_ScriptedTransformation.__init__)


def test_frontend_script_scriptedtransformation_constructor_args():
    sig = inspect.signature(frontend_script_ScriptedTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_dummyrootmetaclass_is_not_abstract():
    assert not inspect.isabstract(frontend_DummyRootMetaclass)


def test_frontend_dummyrootmetaclass_constructor_exists():
    assert callable(frontend_DummyRootMetaclass.__init__)


def test_frontend_dummyrootmetaclass_constructor_args():
    sig = inspect.signature(frontend_DummyRootMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_core_typedwithclass_is_not_abstract():
    assert not inspect.isabstract(core_TypedWithClass)


def test_core_typedwithclass_constructor_exists():
    assert callable(core_TypedWithClass.__init__)


def test_core_typedwithclass_constructor_args():
    sig = inspect.signature(core_TypedWithClass.__init__)
    params = list(sig.parameters.keys())



def test_attributionrule_is_not_abstract():
    assert not inspect.isabstract(AttributionRule)


def test_attributionrule_constructor_exists():
    assert callable(AttributionRule.__init__)


def test_attributionrule_constructor_args():
    sig = inspect.signature(AttributionRule.__init__)
    params = list(sig.parameters.keys())



def test_attributedcl_is_not_abstract():
    assert not inspect.isabstract(AttributeDcl)


def test_attributedcl_constructor_exists():
    assert callable(AttributeDcl.__init__)


def test_attributedcl_constructor_args():
    sig = inspect.signature(AttributeDcl.__init__)
    params = list(sig.parameters.keys())



def test_frontend_attribution_synthesizedattributedcl_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_SynthesizedAttributeDcl)


def test_frontend_attribution_synthesizedattributedcl_constructor_exists():
    assert callable(frontend_attribution_SynthesizedAttributeDcl.__init__)


def test_frontend_attribution_synthesizedattributedcl_constructor_args():
    sig = inspect.signature(frontend_attribution_SynthesizedAttributeDcl.__init__)
    params = list(sig.parameters.keys())



def test_frontend_attribution_inheritedattributedcl_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_InheritedAttributeDcl)


def test_frontend_attribution_inheritedattributedcl_constructor_exists():
    assert callable(frontend_attribution_InheritedAttributeDcl.__init__)


def test_frontend_attribution_inheritedattributedcl_constructor_args():
    sig = inspect.signature(frontend_attribution_InheritedAttributeDcl.__init__)
    params = list(sig.parameters.keys())



def test_frontend_attribution_attributiontransformation_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_AttributionTransformation)


def test_frontend_attribution_attributiontransformation_constructor_exists():
    assert callable(frontend_attribution_AttributionTransformation.__init__)


def test_frontend_attribution_attributiontransformation_constructor_args():
    sig = inspect.signature(frontend_attribution_AttributionTransformation.__init__)
    params = list(sig.parameters.keys())



def test_classuse_is_not_abstract():
    assert not inspect.isabstract(ClassUse)


def test_classuse_constructor_exists():
    assert callable(ClassUse.__init__)


def test_classuse_constructor_args():
    sig = inspect.signature(ClassUse.__init__)
    params = list(sig.parameters.keys())



def test_core_variable_is_not_abstract():
    assert not inspect.isabstract(core_Variable)


def test_core_variable_constructor_exists():
    assert callable(core_Variable.__init__)


def test_core_variable_constructor_args():
    sig = inspect.signature(core_Variable.__init__)
    params = list(sig.parameters.keys())



def test_frontend_attribution_attributedcl_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_AttributeDcl)


def test_frontend_attribution_attributedcl_constructor_exists():
    assert callable(frontend_attribution_AttributeDcl.__init__)


def test_frontend_attribution_attributedcl_constructor_args():
    sig = inspect.signature(frontend_attribution_AttributeDcl.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_objectinstantiation_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_ObjectInstantiation)


def test_frontend_tao_objectinstantiation_constructor_exists():
    assert callable(frontend_tao_ObjectInstantiation.__init__)


def test_frontend_tao_objectinstantiation_constructor_args():
    sig = inspect.signature(frontend_tao_ObjectInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_qool_iteratorstatement_is_not_abstract():
    assert not inspect.isabstract(frontend_qool_IteratorStatement)


def test_frontend_qool_iteratorstatement_constructor_exists():
    assert callable(frontend_qool_IteratorStatement.__init__)


def test_frontend_qool_iteratorstatement_constructor_args():
    sig = inspect.signature(frontend_qool_IteratorStatement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_pobject_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_PObject)


def test_frontend_patterns_pobject_constructor_exists():
    assert callable(frontend_patterns_PObject.__init__)


def test_frontend_patterns_pobject_constructor_args():
    sig = inspect.signature(frontend_patterns_PObject.__init__)
    params = list(sig.parameters.keys())



def test_frontend_tao_referenceassignment_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_ReferenceAssignment)


def test_frontend_tao_referenceassignment_constructor_exists():
    assert callable(frontend_tao_ReferenceAssignment.__init__)


def test_frontend_tao_referenceassignment_constructor_args():
    sig = inspect.signature(frontend_tao_ReferenceAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "targetFeature" in params, "Missing parameter 'targetFeature'"
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend_tao_referenceassignment_has_targetFeature():
    assert hasattr(frontend_tao_ReferenceAssignment, "targetFeature")
    descriptor = None
    for klass in frontend_tao_ReferenceAssignment.__mro__:
        if "targetFeature" in klass.__dict__:
            descriptor = klass.__dict__["targetFeature"]
            break
    assert isinstance(descriptor, property)

def test_frontend_tao_referenceassignment_has_multivalued():
    assert hasattr(frontend_tao_ReferenceAssignment, "multivalued")
    descriptor = None
    for klass in frontend_tao_ReferenceAssignment.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_koan_matcher_is_not_abstract():
    assert not inspect.isabstract(koan_Matcher)


def test_koan_matcher_constructor_exists():
    assert callable(koan_Matcher.__init__)


def test_koan_matcher_constructor_args():
    sig = inspect.signature(koan_Matcher.__init__)
    params = list(sig.parameters.keys())



def test_frontend_koan_forallmatcher_is_not_abstract():
    assert not inspect.isabstract(frontend_koan_ForAllMatcher)


def test_frontend_koan_forallmatcher_constructor_exists():
    assert callable(frontend_koan_ForAllMatcher.__init__)


def test_frontend_koan_forallmatcher_constructor_args():
    sig = inspect.signature(frontend_koan_ForAllMatcher.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_chain_transformationexecution_is_not_abstract():
    assert not inspect.isabstract(frontend_chain_TransformationExecution)


def test_frontend_chain_transformationexecution_constructor_exists():
    assert callable(frontend_chain_TransformationExecution.__init__)


def test_frontend_chain_transformationexecution_constructor_args():
    sig = inspect.signature(frontend_chain_TransformationExecution.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_pattern_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_Pattern)


def test_frontend_patterns_pattern_constructor_exists():
    assert callable(frontend_patterns_Pattern.__init__)


def test_frontend_patterns_pattern_constructor_args():
    sig = inspect.signature(frontend_patterns_Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend_patterns_pattern_has_name():
    assert hasattr(frontend_patterns_Pattern, "name")
    descriptor = None
    for klass in frontend_patterns_Pattern.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend_attribution_attributionrule_is_not_abstract():
    assert not inspect.isabstract(frontend_attribution_AttributionRule)


def test_frontend_attribution_attributionrule_constructor_exists():
    assert callable(frontend_attribution_AttributionRule.__init__)


def test_frontend_attribution_attributionrule_constructor_args():
    sig = inspect.signature(frontend_attribution_AttributionRule.__init__)
    params = list(sig.parameters.keys())



def test_frontend_imperative_methoddefinition_is_not_abstract():
    assert not inspect.isabstract(frontend_imperative_MethodDefinition)


def test_frontend_imperative_methoddefinition_constructor_exists():
    assert callable(frontend_imperative_MethodDefinition.__init__)


def test_frontend_imperative_methoddefinition_constructor_args():
    sig = inspect.signature(frontend_imperative_MethodDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend_imperative_methoddefinition_has_name():
    assert hasattr(frontend_imperative_MethodDefinition, "name")
    descriptor = None
    for klass in frontend_imperative_MethodDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend_tao_sourceexpression_is_not_abstract():
    assert not inspect.isabstract(frontend_tao_SourceExpression)


def test_frontend_tao_sourceexpression_constructor_exists():
    assert callable(frontend_tao_SourceExpression.__init__)


def test_frontend_tao_sourceexpression_constructor_args():
    sig = inspect.signature(frontend_tao_SourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_section_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Section)


def test_frontend_mappings_section_constructor_exists():
    assert callable(frontend_mappings_Section.__init__)


def test_frontend_mappings_section_constructor_args():
    sig = inspect.signature(frontend_mappings_Section.__init__)
    params = list(sig.parameters.keys())
    assert "sectionType" in params, "Missing parameter 'sectionType'"

def test_frontend_mappings_section_has_sectionType():
    assert hasattr(frontend_mappings_Section, "sectionType")
    descriptor = None
    for klass in frontend_mappings_Section.__mro__:
        if "sectionType" in klass.__dict__:
            descriptor = klass.__dict__["sectionType"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_delegate_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Delegate)


def test_frontend_mappings_delegate_constructor_exists():
    assert callable(frontend_mappings_Delegate.__init__)


def test_frontend_mappings_delegate_constructor_args():
    sig = inspect.signature(frontend_mappings_Delegate.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "linkName" in params, "Missing parameter 'linkName'"

def test_frontend_mappings_delegate_has_featureName():
    assert hasattr(frontend_mappings_Delegate, "featureName")
    descriptor = None
    for klass in frontend_mappings_Delegate.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_mappings_delegate_has_isExternal():
    assert hasattr(frontend_mappings_Delegate, "isExternal")
    descriptor = None
    for klass in frontend_mappings_Delegate.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_frontend_mappings_delegate_has_linkName():
    assert hasattr(frontend_mappings_Delegate, "linkName")
    descriptor = None
    for klass in frontend_mappings_Delegate.__mro__:
        if "linkName" in klass.__dict__:
            descriptor = klass.__dict__["linkName"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_mappingelement_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_MappingElement)


def test_frontend_mappings_mappingelement_constructor_exists():
    assert callable(frontend_mappings_MappingElement.__init__)


def test_frontend_mappings_mappingelement_constructor_args():
    sig = inspect.signature(frontend_mappings_MappingElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_patterns_pfeature_is_not_abstract():
    assert not inspect.isabstract(frontend_patterns_PFeature)


def test_frontend_patterns_pfeature_constructor_exists():
    assert callable(frontend_patterns_PFeature.__init__)


def test_frontend_patterns_pfeature_constructor_args():
    sig = inspect.signature(frontend_patterns_PFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend_patterns_pfeature_has_name():
    assert hasattr(frontend_patterns_PFeature, "name")
    descriptor = None
    for klass in frontend_patterns_PFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend_mappings_operator_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Operator)


def test_frontend_mappings_operator_constructor_exists():
    assert callable(frontend_mappings_Operator.__init__)


def test_frontend_mappings_operator_constructor_args():
    sig = inspect.signature(frontend_mappings_Operator.__init__)
    params = list(sig.parameters.keys())



def test_frontend_mappings_context_is_not_abstract():
    assert not inspect.isabstract(frontend_mappings_Context)


def test_frontend_mappings_context_constructor_exists():
    assert callable(frontend_mappings_Context.__init__)


def test_frontend_mappings_context_constructor_args():
    sig = inspect.signature(frontend_mappings_Context.__init__)
    params = list(sig.parameters.keys())



def test_frontend_koan_matcher_is_not_abstract():
    assert not inspect.isabstract(frontend_koan_Matcher)


def test_frontend_koan_matcher_constructor_exists():
    assert callable(frontend_koan_Matcher.__init__)


def test_frontend_koan_matcher_constructor_args():
    sig = inspect.signature(frontend_koan_Matcher.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_puttraceparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_PutTraceParameter)


def test_frontend_core_puttraceparameter_constructor_exists():
    assert callable(frontend_core_PutTraceParameter.__init__)


def test_frontend_core_puttraceparameter_constructor_args():
    sig = inspect.signature(frontend_core_PutTraceParameter.__init__)
    params = list(sig.parameters.keys())



def test_puttraceparameter_is_not_abstract():
    assert not inspect.isabstract(PutTraceParameter)


def test_puttraceparameter_constructor_exists():
    assert callable(PutTraceParameter.__init__)


def test_puttraceparameter_constructor_args():
    sig = inspect.signature(PutTraceParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_puttrace_is_not_abstract():
    assert not inspect.isabstract(frontend_core_PutTrace)


def test_frontend_core_puttrace_constructor_exists():
    assert callable(frontend_core_PutTrace.__init__)


def test_frontend_core_puttrace_constructor_args():
    sig = inspect.signature(frontend_core_PutTrace.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_inlinefeature_is_not_abstract():
    assert not inspect.isabstract(frontend_core_InlineFeature)


def test_frontend_core_inlinefeature_constructor_exists():
    assert callable(frontend_core_InlineFeature.__init__)


def test_frontend_core_inlinefeature_constructor_args():
    sig = inspect.signature(frontend_core_InlineFeature.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend_core_inlinefeature_has_multivalued():
    assert hasattr(frontend_core_InlineFeature, "multivalued")
    descriptor = None
    for klass in frontend_core_InlineFeature.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_inlinefeature_is_not_abstract():
    assert not inspect.isabstract(InlineFeature)


def test_inlinefeature_constructor_exists():
    assert callable(InlineFeature.__init__)


def test_inlinefeature_constructor_args():
    sig = inspect.signature(InlineFeature.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_inlineclass_is_not_abstract():
    assert not inspect.isabstract(frontend_core_InlineClass)


def test_frontend_core_inlineclass_constructor_exists():
    assert callable(frontend_core_InlineClass.__init__)


def test_frontend_core_inlineclass_constructor_args():
    sig = inspect.signature(frontend_core_InlineClass.__init__)
    params = list(sig.parameters.keys())



def test_inlineclass_is_not_abstract():
    assert not inspect.isabstract(InlineClass)


def test_inlineclass_constructor_exists():
    assert callable(InlineClass.__init__)


def test_inlineclass_constructor_args():
    sig = inspect.signature(InlineClass.__init__)
    params = list(sig.parameters.keys())



def test_core_moduledefinition_is_not_abstract():
    assert not inspect.isabstract(core_ModuleDefinition)


def test_core_moduledefinition_constructor_exists():
    assert callable(core_ModuleDefinition.__init__)


def test_core_moduledefinition_constructor_args():
    sig = inspect.signature(core_ModuleDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_inlinemodel_is_not_abstract():
    assert not inspect.isabstract(frontend_core_InlineModel)


def test_frontend_core_inlinemodel_constructor_exists():
    assert callable(frontend_core_InlineModel.__init__)


def test_frontend_core_inlinemodel_constructor_args():
    sig = inspect.signature(frontend_core_InlineModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_traceelement_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TraceElement)


def test_frontend_core_traceelement_constructor_exists():
    assert callable(frontend_core_TraceElement.__init__)


def test_frontend_core_traceelement_constructor_args():
    sig = inspect.signature(frontend_core_TraceElement.__init__)
    params = list(sig.parameters.keys())



def test_traceelement_is_not_abstract():
    assert not inspect.isabstract(TraceElement)


def test_traceelement_constructor_exists():
    assert callable(TraceElement.__init__)


def test_traceelement_constructor_args():
    sig = inspect.signature(TraceElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_tracedefinition_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TraceDefinition)


def test_frontend_core_tracedefinition_constructor_exists():
    assert callable(frontend_core_TraceDefinition.__init__)


def test_frontend_core_tracedefinition_constructor_args():
    sig = inspect.signature(frontend_core_TraceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_traceinterface_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TraceInterface)


def test_frontend_core_traceinterface_constructor_exists():
    assert callable(frontend_core_TraceInterface.__init__)


def test_frontend_core_traceinterface_constructor_args():
    sig = inspect.signature(frontend_core_TraceInterface.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_typedwithclass_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TypedWithClass)


def test_frontend_core_typedwithclass_constructor_exists():
    assert callable(frontend_core_TypedWithClass.__init__)


def test_frontend_core_typedwithclass_constructor_args():
    sig = inspect.signature(frontend_core_TypedWithClass.__init__)
    params = list(sig.parameters.keys())



def test_tracedefinition_is_not_abstract():
    assert not inspect.isabstract(TraceDefinition)


def test_tracedefinition_constructor_exists():
    assert callable(TraceDefinition.__init__)


def test_tracedefinition_constructor_args():
    sig = inspect.signature(TraceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_traceuse_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TraceUse)


def test_frontend_core_traceuse_constructor_exists():
    assert callable(frontend_core_TraceUse.__init__)


def test_frontend_core_traceuse_constructor_args():
    sig = inspect.signature(frontend_core_TraceUse.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_tracecompareexpression_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TraceCompareExpression)


def test_frontend_core_tracecompareexpression_constructor_exists():
    assert callable(frontend_core_TraceCompareExpression.__init__)


def test_frontend_core_tracecompareexpression_constructor_args():
    sig = inspect.signature(frontend_core_TraceCompareExpression.__init__)
    params = list(sig.parameters.keys())
    assert "multivaluedTag" in params, "Missing parameter 'multivaluedTag'"

def test_frontend_core_tracecompareexpression_has_multivaluedTag():
    assert hasattr(frontend_core_TraceCompareExpression, "multivaluedTag")
    descriptor = None
    for klass in frontend_core_TraceCompareExpression.__mro__:
        if "multivaluedTag" in klass.__dict__:
            descriptor = klass.__dict__["multivaluedTag"]
            break
    assert isinstance(descriptor, property)



def test_tracecompareexpression_is_not_abstract():
    assert not inspect.isabstract(TraceCompareExpression)


def test_tracecompareexpression_constructor_exists():
    assert callable(TraceCompareExpression.__init__)


def test_tracecompareexpression_constructor_args():
    sig = inspect.signature(TraceCompareExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_matchtrace_is_not_abstract():
    assert not inspect.isabstract(frontend_core_MatchTrace)


def test_frontend_core_matchtrace_constructor_exists():
    assert callable(frontend_core_MatchTrace.__init__)


def test_frontend_core_matchtrace_constructor_args():
    sig = inspect.signature(frontend_core_MatchTrace.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_frontend_core_matchtrace_has_cardinality():
    assert hasattr(frontend_core_MatchTrace, "cardinality")
    descriptor = None
    for klass in frontend_core_MatchTrace.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_inlinereference_is_not_abstract():
    assert not inspect.isabstract(frontend_core_InlineReference)


def test_frontend_core_inlinereference_constructor_exists():
    assert callable(frontend_core_InlineReference.__init__)


def test_frontend_core_inlinereference_constructor_args():
    sig = inspect.signature(frontend_core_InlineReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_inlineattribute_is_not_abstract():
    assert not inspect.isabstract(frontend_core_InlineAttribute)


def test_frontend_core_inlineattribute_constructor_exists():
    assert callable(frontend_core_InlineAttribute.__init__)


def test_frontend_core_inlineattribute_constructor_args():
    sig = inspect.signature(frontend_core_InlineAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_ifbranch_is_not_abstract():
    assert not inspect.isabstract(frontend_core_IfBranch)


def test_frontend_core_ifbranch_constructor_exists():
    assert callable(frontend_core_IfBranch.__init__)


def test_frontend_core_ifbranch_constructor_args():
    sig = inspect.signature(frontend_core_IfBranch.__init__)
    params = list(sig.parameters.keys())



def test_ifbranch_is_not_abstract():
    assert not inspect.isabstract(IfBranch)


def test_ifbranch_constructor_exists():
    assert callable(IfBranch.__init__)


def test_ifbranch_constructor_args():
    sig = inspect.signature(IfBranch.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_ifexpr_is_not_abstract():
    assert not inspect.isabstract(frontend_core_IfExpr)


def test_frontend_core_ifexpr_constructor_exists():
    assert callable(frontend_core_IfExpr.__init__)


def test_frontend_core_ifexpr_constructor_args():
    sig = inspect.signature(frontend_core_IfExpr.__init__)
    params = list(sig.parameters.keys())



def test_core_implicitlyannotableelement_is_not_abstract():
    assert not inspect.isabstract(core_ImplicitlyAnnotableElement)


def test_core_implicitlyannotableelement_constructor_exists():
    assert callable(core_ImplicitlyAnnotableElement.__init__)


def test_core_implicitlyannotableelement_constructor_args():
    sig = inspect.signature(core_ImplicitlyAnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_core_typeexpression_is_not_abstract():
    assert not inspect.isabstract(core_TypeExpression)


def test_core_typeexpression_constructor_exists():
    assert callable(core_TypeExpression.__init__)


def test_core_typeexpression_constructor_args():
    sig = inspect.signature(core_TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_classuse_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ClassUse)


def test_frontend_core_classuse_constructor_exists():
    assert callable(frontend_core_ClassUse.__init__)


def test_frontend_core_classuse_constructor_args():
    sig = inspect.signature(frontend_core_ClassUse.__init__)
    params = list(sig.parameters.keys())
    assert "strictType" in params, "Missing parameter 'strictType'"
    assert "className" in params, "Missing parameter 'className'"

def test_frontend_core_classuse_has_strictType():
    assert hasattr(frontend_core_ClassUse, "strictType")
    descriptor = None
    for klass in frontend_core_ClassUse.__mro__:
        if "strictType" in klass.__dict__:
            descriptor = klass.__dict__["strictType"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_classuse_has_className():
    assert hasattr(frontend_core_ClassUse, "className")
    descriptor = None
    for klass in frontend_core_ClassUse.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_typeexpression_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TypeExpression)


def test_frontend_core_typeexpression_constructor_exists():
    assert callable(frontend_core_TypeExpression.__init__)


def test_frontend_core_typeexpression_constructor_args():
    sig = inspect.signature(frontend_core_TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(frontend_core_BooleanLiteral)


def test_frontend_core_booleanliteral_constructor_exists():
    assert callable(frontend_core_BooleanLiteral.__init__)


def test_frontend_core_booleanliteral_constructor_args():
    sig = inspect.signature(frontend_core_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend_core_booleanliteral_has_value():
    assert hasattr(frontend_core_BooleanLiteral, "value")
    descriptor = None
    for klass in frontend_core_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_stringliteral_is_not_abstract():
    assert not inspect.isabstract(frontend_core_StringLiteral)


def test_frontend_core_stringliteral_constructor_exists():
    assert callable(frontend_core_StringLiteral.__init__)


def test_frontend_core_stringliteral_constructor_args():
    sig = inspect.signature(frontend_core_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend_core_stringliteral_has_value():
    assert hasattr(frontend_core_StringLiteral, "value")
    descriptor = None
    for klass in frontend_core_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(frontend_core_DoubleLiteral)


def test_frontend_core_doubleliteral_constructor_exists():
    assert callable(frontend_core_DoubleLiteral.__init__)


def test_frontend_core_doubleliteral_constructor_args():
    sig = inspect.signature(frontend_core_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend_core_doubleliteral_has_value():
    assert hasattr(frontend_core_DoubleLiteral, "value")
    descriptor = None
    for klass in frontend_core_DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_numliteral_is_not_abstract():
    assert not inspect.isabstract(frontend_core_NumLiteral)


def test_frontend_core_numliteral_constructor_exists():
    assert callable(frontend_core_NumLiteral.__init__)


def test_frontend_core_numliteral_constructor_args():
    sig = inspect.signature(frontend_core_NumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend_core_numliteral_has_value():
    assert hasattr(frontend_core_NumLiteral, "value")
    descriptor = None
    for klass in frontend_core_NumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_binaryexpr_is_not_abstract():
    assert not inspect.isabstract(frontend_core_BinaryExpr)


def test_frontend_core_binaryexpr_constructor_exists():
    assert callable(frontend_core_BinaryExpr.__init__)


def test_frontend_core_binaryexpr_constructor_args():
    sig = inspect.signature(frontend_core_BinaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "binaryOp" in params, "Missing parameter 'binaryOp'"

def test_frontend_core_binaryexpr_has_binaryOp():
    assert hasattr(frontend_core_BinaryExpr, "binaryOp")
    descriptor = None
    for klass in frontend_core_BinaryExpr.__mro__:
        if "binaryOp" in klass.__dict__:
            descriptor = klass.__dict__["binaryOp"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_keywordparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_KeywordParameter)


def test_frontend_core_keywordparameter_constructor_exists():
    assert callable(frontend_core_KeywordParameter.__init__)


def test_frontend_core_keywordparameter_constructor_args():
    sig = inspect.signature(frontend_core_KeywordParameter.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_frontend_core_keywordparameter_has_keyword():
    assert hasattr(frontend_core_KeywordParameter, "keyword")
    descriptor = None
    for klass in frontend_core_KeywordParameter.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_keywordparameter_is_not_abstract():
    assert not inspect.isabstract(KeywordParameter)


def test_keywordparameter_constructor_exists():
    assert callable(KeywordParameter.__init__)


def test_keywordparameter_constructor_args():
    sig = inspect.signature(KeywordParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_keywordmethodcall_is_not_abstract():
    assert not inspect.isabstract(frontend_core_KeywordMethodCall)


def test_frontend_core_keywordmethodcall_constructor_exists():
    assert callable(frontend_core_KeywordMethodCall.__init__)


def test_frontend_core_keywordmethodcall_constructor_args():
    sig = inspect.signature(frontend_core_KeywordMethodCall.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_methodcall_is_not_abstract():
    assert not inspect.isabstract(frontend_core_MethodCall)


def test_frontend_core_methodcall_constructor_exists():
    assert callable(frontend_core_MethodCall.__init__)


def test_frontend_core_methodcall_constructor_args():
    sig = inspect.signature(frontend_core_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "withParameters" in params, "Missing parameter 'withParameters'"
    assert "methodName" in params, "Missing parameter 'methodName'"

def test_frontend_core_methodcall_has_withParameters():
    assert hasattr(frontend_core_MethodCall, "withParameters")
    descriptor = None
    for klass in frontend_core_MethodCall.__mro__:
        if "withParameters" in klass.__dict__:
            descriptor = klass.__dict__["withParameters"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_methodcall_has_methodName():
    assert hasattr(frontend_core_MethodCall, "methodName")
    descriptor = None
    for klass in frontend_core_MethodCall.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_variablereference_is_not_abstract():
    assert not inspect.isabstract(frontend_core_VariableReference)


def test_frontend_core_variablereference_constructor_exists():
    assert callable(frontend_core_VariableReference.__init__)


def test_frontend_core_variablereference_constructor_args():
    sig = inspect.signature(frontend_core_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_core_expression_is_not_abstract():
    assert not inspect.isabstract(core_Expression)


def test_core_expression_constructor_exists():
    assert callable(core_Expression.__init__)


def test_core_expression_constructor_args():
    sig = inspect.signature(core_Expression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_modelreference_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ModelReference)


def test_frontend_core_modelreference_constructor_exists():
    assert callable(frontend_core_ModelReference.__init__)


def test_frontend_core_modelreference_constructor_args():
    sig = inspect.signature(frontend_core_ModelReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_resolvelink_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ResolveLink)


def test_frontend_core_resolvelink_constructor_exists():
    assert callable(frontend_core_ResolveLink.__init__)


def test_frontend_core_resolvelink_constructor_args():
    sig = inspect.signature(frontend_core_ResolveLink.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "linkName" in params, "Missing parameter 'linkName'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_frontend_core_resolvelink_has_featureName():
    assert hasattr(frontend_core_ResolveLink, "featureName")
    descriptor = None
    for klass in frontend_core_ResolveLink.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_resolvelink_has_linkName():
    assert hasattr(frontend_core_ResolveLink, "linkName")
    descriptor = None
    for klass in frontend_core_ResolveLink.__mro__:
        if "linkName" in klass.__dict__:
            descriptor = klass.__dict__["linkName"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_resolvelink_has_isExternal():
    assert hasattr(frontend_core_ResolveLink, "isExternal")
    descriptor = None
    for klass in frontend_core_ResolveLink.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_closureparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ClosureParameter)


def test_frontend_core_closureparameter_constructor_exists():
    assert callable(frontend_core_ClosureParameter.__init__)


def test_frontend_core_closureparameter_constructor_args():
    sig = inspect.signature(frontend_core_ClosureParameter.__init__)
    params = list(sig.parameters.keys())



def test_closureparameter_is_not_abstract():
    assert not inspect.isabstract(ClosureParameter)


def test_closureparameter_constructor_exists():
    assert callable(ClosureParameter.__init__)


def test_closureparameter_constructor_args():
    sig = inspect.signature(ClosureParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_closuredeclaration_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ClosureDeclaration)


def test_frontend_core_closuredeclaration_constructor_exists():
    assert callable(frontend_core_ClosureDeclaration.__init__)


def test_frontend_core_closuredeclaration_constructor_args():
    sig = inspect.signature(frontend_core_ClosureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_variable_is_not_abstract():
    assert not inspect.isabstract(frontend_core_Variable)


def test_frontend_core_variable_constructor_exists():
    assert callable(frontend_core_Variable.__init__)


def test_frontend_core_variable_constructor_args():
    sig = inspect.signature(frontend_core_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend_core_variable_has_name():
    assert hasattr(frontend_core_Variable, "name")
    descriptor = None
    for klass in frontend_core_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_requireparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_RequireParameter)


def test_frontend_core_requireparameter_constructor_exists():
    assert callable(frontend_core_RequireParameter.__init__)


def test_frontend_core_requireparameter_constructor_args():
    sig = inspect.signature(frontend_core_RequireParameter.__init__)
    params = list(sig.parameters.keys())
    assert "formalParameterName" in params, "Missing parameter 'formalParameterName'"

def test_frontend_core_requireparameter_has_formalParameterName():
    assert hasattr(frontend_core_RequireParameter, "formalParameterName")
    descriptor = None
    for klass in frontend_core_RequireParameter.__mro__:
        if "formalParameterName" in klass.__dict__:
            descriptor = klass.__dict__["formalParameterName"]
            break
    assert isinstance(descriptor, property)



def test_requireparameter_is_not_abstract():
    assert not inspect.isabstract(RequireParameter)


def test_requireparameter_constructor_exists():
    assert callable(RequireParameter.__init__)


def test_requireparameter_constructor_args():
    sig = inspect.signature(RequireParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_requiremodelparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_RequireModelParameter)


def test_frontend_core_requiremodelparameter_constructor_exists():
    assert callable(frontend_core_RequireModelParameter.__init__)


def test_frontend_core_requiremodelparameter_constructor_args():
    sig = inspect.signature(frontend_core_RequireModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_requiredeclaration_is_not_abstract():
    assert not inspect.isabstract(frontend_core_RequireDeclaration)


def test_frontend_core_requiredeclaration_constructor_exists():
    assert callable(frontend_core_RequireDeclaration.__init__)


def test_frontend_core_requiredeclaration_constructor_args():
    sig = inspect.signature(frontend_core_RequireDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"

def test_frontend_core_requiredeclaration_has_name():
    assert hasattr(frontend_core_RequireDeclaration, "name")
    descriptor = None
    for klass in frontend_core_RequireDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_requiredeclaration_has_default():
    assert hasattr(frontend_core_RequireDeclaration, "default")
    descriptor = None
    for klass in frontend_core_RequireDeclaration.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_usedeclaration_is_not_abstract():
    assert not inspect.isabstract(frontend_core_UseDeclaration)


def test_frontend_core_usedeclaration_constructor_exists():
    assert callable(frontend_core_UseDeclaration.__init__)


def test_frontend_core_usedeclaration_constructor_args():
    sig = inspect.signature(frontend_core_UseDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "module" in params, "Missing parameter 'module'"
    assert "as_" in params, "Missing parameter 'as_'"

def test_frontend_core_usedeclaration_has_module():
    assert hasattr(frontend_core_UseDeclaration, "module")
    descriptor = None
    for klass in frontend_core_UseDeclaration.__mro__:
        if "module" in klass.__dict__:
            descriptor = klass.__dict__["module"]
            break
    assert isinstance(descriptor, property)

def test_frontend_core_usedeclaration_has_as_():
    assert hasattr(frontend_core_UseDeclaration, "as_")
    descriptor = None
    for klass in frontend_core_UseDeclaration.__mro__:
        if "as_" in klass.__dict__:
            descriptor = klass.__dict__["as_"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_importedmodel_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ImportedModel)


def test_frontend_core_importedmodel_constructor_exists():
    assert callable(frontend_core_ImportedModel.__init__)


def test_frontend_core_importedmodel_constructor_args():
    sig = inspect.signature(frontend_core_ImportedModel.__init__)
    params = list(sig.parameters.keys())



def test_core_definitionparameter_is_not_abstract():
    assert not inspect.isabstract(core_DefinitionParameter)


def test_core_definitionparameter_constructor_exists():
    assert callable(core_DefinitionParameter.__init__)


def test_core_definitionparameter_constructor_args():
    sig = inspect.signature(core_DefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_tracedmodelparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TracedModelParameter)


def test_frontend_core_tracedmodelparameter_constructor_exists():
    assert callable(frontend_core_TracedModelParameter.__init__)


def test_frontend_core_tracedmodelparameter_constructor_args():
    sig = inspect.signature(frontend_core_TracedModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_transformationdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_TransformationDefinitionParameter)


def test_frontend_core_transformationdefinitionparameter_constructor_exists():
    assert callable(frontend_core_TransformationDefinitionParameter.__init__)


def test_frontend_core_transformationdefinitionparameter_constructor_args():
    sig = inspect.signature(frontend_core_TransformationDefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_eclectictransformationdefinition_is_not_abstract():
    assert not inspect.isabstract(frontend_core_EclecticTransformationDefinition)


def test_frontend_core_eclectictransformationdefinition_constructor_exists():
    assert callable(frontend_core_EclecticTransformationDefinition.__init__)


def test_frontend_core_eclectictransformationdefinition_constructor_args():
    sig = inspect.signature(frontend_core_EclecticTransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_requiredeclaration_is_not_abstract():
    assert not inspect.isabstract(RequireDeclaration)


def test_requiredeclaration_constructor_exists():
    assert callable(RequireDeclaration.__init__)


def test_requiredeclaration_constructor_args():
    sig = inspect.signature(RequireDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_inlinemodel_is_not_abstract():
    assert not inspect.isabstract(InlineModel)


def test_inlinemodel_constructor_exists():
    assert callable(InlineModel.__init__)


def test_inlinemodel_constructor_args():
    sig = inspect.signature(InlineModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_propertywrite_is_not_abstract():
    assert not inspect.isabstract(frontend_core_PropertyWrite)


def test_frontend_core_propertywrite_constructor_exists():
    assert callable(frontend_core_PropertyWrite.__init__)


def test_frontend_core_propertywrite_constructor_args():
    sig = inspect.signature(frontend_core_PropertyWrite.__init__)
    params = list(sig.parameters.keys())
    assert "_property" in params, "Missing parameter '_property'"

def test_frontend_core_propertywrite_has__property():
    assert hasattr(frontend_core_PropertyWrite, "_property")
    descriptor = None
    for klass in frontend_core_PropertyWrite.__mro__:
        if "_property" in klass.__dict__:
            descriptor = klass.__dict__["_property"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_definevariable_is_not_abstract():
    assert not inspect.isabstract(frontend_core_DefineVariable)


def test_frontend_core_definevariable_constructor_exists():
    assert callable(frontend_core_DefineVariable.__init__)


def test_frontend_core_definevariable_constructor_args():
    sig = inspect.signature(frontend_core_DefineVariable.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_expression_is_not_abstract():
    assert not inspect.isabstract(frontend_core_Expression)


def test_frontend_core_expression_constructor_exists():
    assert callable(frontend_core_Expression.__init__)


def test_frontend_core_expression_constructor_args():
    sig = inspect.signature(frontend_core_Expression.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_statement_is_not_abstract():
    assert not inspect.isabstract(frontend_core_Statement)


def test_frontend_core_statement_constructor_exists():
    assert callable(frontend_core_Statement.__init__)


def test_frontend_core_statement_constructor_args():
    sig = inspect.signature(frontend_core_Statement.__init__)
    params = list(sig.parameters.keys())



def test_annotableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotableElement)


def test_annotableelement_constructor_exists():
    assert callable(AnnotableElement.__init__)


def test_annotableelement_constructor_args():
    sig = inspect.signature(AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_representmodel_is_not_abstract():
    assert not inspect.isabstract(frontend_core_RepresentModel)


def test_frontend_core_representmodel_constructor_exists():
    assert callable(frontend_core_RepresentModel.__init__)


def test_frontend_core_representmodel_constructor_args():
    sig = inspect.signature(frontend_core_RepresentModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_annotation_is_not_abstract():
    assert not inspect.isabstract(frontend_core_Annotation)


def test_frontend_core_annotation_constructor_exists():
    assert callable(frontend_core_Annotation.__init__)


def test_frontend_core_annotation_constructor_args():
    sig = inspect.signature(frontend_core_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_singleannotation_is_not_abstract():
    assert not inspect.isabstract(SingleAnnotation)


def test_singleannotation_constructor_exists():
    assert callable(SingleAnnotation.__init__)


def test_singleannotation_constructor_args():
    sig = inspect.signature(SingleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_potencyannotation_is_not_abstract():
    assert not inspect.isabstract(frontend_core_PotencyAnnotation)


def test_frontend_core_potencyannotation_constructor_exists():
    assert callable(frontend_core_PotencyAnnotation.__init__)


def test_frontend_core_potencyannotation_constructor_args():
    sig = inspect.signature(frontend_core_PotencyAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend_core_potencyannotation_has_value():
    assert hasattr(frontend_core_PotencyAnnotation, "value")
    descriptor = None
    for klass in frontend_core_PotencyAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_implicitlyannotableelement_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ImplicitlyAnnotableElement)


def test_frontend_core_implicitlyannotableelement_constructor_exists():
    assert callable(frontend_core_ImplicitlyAnnotableElement.__init__)


def test_frontend_core_implicitlyannotableelement_constructor_args():
    sig = inspect.signature(frontend_core_ImplicitlyAnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_singleannotation_is_not_abstract():
    assert not inspect.isabstract(frontend_core_SingleAnnotation)


def test_frontend_core_singleannotation_constructor_exists():
    assert callable(frontend_core_SingleAnnotation.__init__)


def test_frontend_core_singleannotation_constructor_args():
    sig = inspect.signature(frontend_core_SingleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_optimizationsannotation_is_not_abstract():
    assert not inspect.isabstract(frontend_core_OptimizationsAnnotation)


def test_frontend_core_optimizationsannotation_constructor_exists():
    assert callable(frontend_core_OptimizationsAnnotation.__init__)


def test_frontend_core_optimizationsannotation_constructor_args():
    sig = inspect.signature(frontend_core_OptimizationsAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_frontend_core_optimizationsannotation_has_enabled():
    assert hasattr(frontend_core_OptimizationsAnnotation, "enabled")
    descriptor = None
    for klass in frontend_core_OptimizationsAnnotation.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_metamodelmodelannotation_is_not_abstract():
    assert not inspect.isabstract(frontend_core_MetamodelModelAnnotation)


def test_frontend_core_metamodelmodelannotation_constructor_exists():
    assert callable(frontend_core_MetamodelModelAnnotation.__init__)


def test_frontend_core_metamodelmodelannotation_constructor_args():
    sig = inspect.signature(frontend_core_MetamodelModelAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_frontend_core_metamodelmodelannotation_has_metamodel():
    assert hasattr(frontend_core_MetamodelModelAnnotation, "metamodel")
    descriptor = None
    for klass in frontend_core_MetamodelModelAnnotation.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_frontend_core_annotableelement_is_not_abstract():
    assert not inspect.isabstract(frontend_core_AnnotableElement)


def test_frontend_core_annotableelement_constructor_exists():
    assert callable(frontend_core_AnnotableElement.__init__)


def test_frontend_core_annotableelement_constructor_args():
    sig = inspect.signature(frontend_core_AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_core_annotableelement_is_not_abstract():
    assert not inspect.isabstract(core_AnnotableElement)


def test_core_annotableelement_constructor_exists():
    assert callable(core_AnnotableElement.__init__)


def test_core_annotableelement_constructor_args():
    sig = inspect.signature(core_AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_moduledefinition_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ModuleDefinition)


def test_frontend_core_moduledefinition_constructor_exists():
    assert callable(frontend_core_ModuleDefinition.__init__)


def test_frontend_core_moduledefinition_constructor_args():
    sig = inspect.signature(frontend_core_ModuleDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definitionparameter_is_not_abstract():
    assert not inspect.isabstract(DefinitionParameter)


def test_definitionparameter_constructor_exists():
    assert callable(DefinitionParameter.__init__)


def test_definitionparameter_constructor_args():
    sig = inspect.signature(DefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_moduleparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_ModuleParameter)


def test_frontend_core_moduleparameter_constructor_exists():
    assert callable(frontend_core_ModuleParameter.__init__)


def test_frontend_core_moduleparameter_constructor_args():
    sig = inspect.signature(frontend_core_ModuleParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend_core_definitionparameter_is_not_abstract():
    assert not inspect.isabstract(frontend_core_DefinitionParameter)


def test_frontend_core_definitionparameter_constructor_exists():
    assert callable(frontend_core_DefinitionParameter.__init__)


def test_frontend_core_definitionparameter_constructor_args():
    sig = inspect.signature(frontend_core_DefinitionParameter.__init__)
    params = list(sig.parameters.keys())

def test_mappingcardinality_exists():
    # Check that the Enumeration exists
    assert MappingCardinality is not None

def test_mappingcardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MappingCardinality]
    expected_literals = [
        "OneToOne",
        "OneToN",
        "NToOne",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MappingCardinality"

def test_binaryop_exists():
    # Check that the Enumeration exists
    assert BinaryOp is not None

def test_binaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOp]
    expected_literals = [
        "DIV",
        "MUL",
        "EQUAL",
        "SUB",
        "ADD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"

def test_resolvetracecardinality_exists():
    # Check that the Enumeration exists
    assert ResolveTraceCardinality is not None

def test_resolvetracecardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResolveTraceCardinality]
    expected_literals = [
        "ZERO_OR_ONE",
        "ONE_ONE",
        "MANY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResolveTraceCardinality"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
frontend_core_NamedElement_strategy = st.builds(
    frontend_core_NamedElement,
    name=
        safe_text
)
frontend_core_LocatedElement_strategy = st.builds(
    frontend_core_LocatedElement,
    file=
        safe_text,
    row=
        st.integers(),
    column=
        st.integers()
)
ImportedModel_strategy = st.builds(
    ImportedModel,
)
ModuleDefinition_strategy = st.builds(
    ModuleDefinition,
)
frontend_core_TransformationDefinition_strategy = st.builds(
    frontend_core_TransformationDefinition,
)
frontend_core_AnnotationParameter_strategy = st.builds(
    frontend_core_AnnotationParameter,
)
AnnotationParameter_strategy = st.builds(
    AnnotationParameter,
)
frontend_core_GenericAnnotation_strategy = st.builds(
    frontend_core_GenericAnnotation,
    name=
        safe_text
)
ObjectSourceVariable_strategy = st.builds(
    ObjectSourceVariable,
)
SourceExpression_strategy = st.builds(
    SourceExpression,
)
frontend_tao_WithOptionalVariableExpression_strategy = st.builds(
    frontend_tao_WithOptionalVariableExpression,
)
TemplateRootObject_strategy = st.builds(
    TemplateRootObject,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
ObjectInstantiation_strategy = st.builds(
    ObjectInstantiation,
)
frontend_tao_TemplateRootObject_strategy = st.builds(
    frontend_tao_TemplateRootObject,
)
Assignment_strategy = st.builds(
    Assignment,
)
frontend_tao_AttributeAssigment_strategy = st.builds(
    frontend_tao_AttributeAssigment,
    targetFeature=
        safe_text
)
ReferenceAssignment_strategy = st.builds(
    ReferenceAssignment,
)
frontend_tao_Invocation_strategy = st.builds(
    frontend_tao_Invocation,
)
frontend_tao_ObjectSyntax_strategy = st.builds(
    frontend_tao_ObjectSyntax,
)
tao_Assignment_strategy = st.builds(
    tao_Assignment,
)
frontend_facilities_CopierCallbackDefinition_strategy = st.builds(
    frontend_facilities_CopierCallbackDefinition,
    stop=
        st.booleans()
)
facilities_CopierCallbackDefinition_strategy = st.builds(
    facilities_CopierCallbackDefinition,
)
Template_strategy = st.builds(
    Template,
)
InvokeTransformation_strategy = st.builds(
    InvokeTransformation,
)
frontend_qool_InvokeExternal_strategy = st.builds(
    frontend_qool_InvokeExternal,
    queueName=
        safe_text,
    traceAttributeName=
        safe_text
)
NamedInvocationParameter_strategy = st.builds(
    NamedInvocationParameter,
)
InvocationParameter_strategy = st.builds(
    InvocationParameter,
)
frontend_qool_NamedInvocationParameter_strategy = st.builds(
    frontend_qool_NamedInvocationParameter,
    formalName=
        safe_text
)
TransformationDefinitionParameter_strategy = st.builds(
    TransformationDefinitionParameter,
)
frontend_qool_InvocationParameter_strategy = st.builds(
    frontend_qool_InvocationParameter,
    calleeModelName=
        safe_text
)
frontend_qool_InvokeInternal_strategy = st.builds(
    frontend_qool_InvokeInternal,
)
IteratorStatement_strategy = st.builds(
    IteratorStatement,
)
frontend_qool_ForEachStatement_strategy = st.builds(
    frontend_qool_ForEachStatement,
)
frontend_qool_ForAllStatement_strategy = st.builds(
    frontend_qool_ForAllStatement,
)
core_Statement_strategy = st.builds(
    core_Statement,
)
TypeExpression_strategy = st.builds(
    TypeExpression,
)
frontend_qool_QueueOptimization_strategy = st.builds(
    frontend_qool_QueueOptimization,
)
QueueOptimization_strategy = st.builds(
    QueueOptimization,
)
frontend_qool_AccessByFeatureOptimization_strategy = st.builds(
    frontend_qool_AccessByFeatureOptimization,
    featureName=
        safe_text,
    force=
        st.booleans()
)
frontend_qool_MatchPredicate_strategy = st.builds(
    frontend_qool_MatchPredicate,
)
MatchPredicate_strategy = st.builds(
    MatchPredicate,
)
frontend_qool_KindOfPredicate_strategy = st.builds(
    frontend_qool_KindOfPredicate,
)
frontend_qool_PropertyEqualsPredicate_strategy = st.builds(
    frontend_qool_PropertyEqualsPredicate,
    propertyName=
        safe_text
)
mappings_MetamodelElementRef_strategy = st.builds(
    mappings_MetamodelElementRef,
)
MetamodelElementRef_strategy = st.builds(
    MetamodelElementRef,
)
frontend_mappings_AttributeRef_strategy = st.builds(
    frontend_mappings_AttributeRef,
    featureName=
        safe_text,
    multivalued=
        st.booleans()
)
frontend_mappings_ClassRef_strategy = st.builds(
    frontend_mappings_ClassRef,
)
frontend_mappings_MetamodelElementRef_strategy = st.builds(
    frontend_mappings_MetamodelElementRef,
)
DefaultValue_strategy = st.builds(
    DefaultValue,
)
frontend_mappings_IntDefaultValue_strategy = st.builds(
    frontend_mappings_IntDefaultValue,
    defaultValue=
        safe_text
)
Segment_strategy = st.builds(
    Segment,
)
QoolQueue_strategy = st.builds(
    QoolQueue,
)
frontend_qool_LocalQueue_strategy = st.builds(
    frontend_qool_LocalQueue,
)
frontend_qool_ModelElementQueue_strategy = st.builds(
    frontend_qool_ModelElementQueue,
)
frontend_mappings_ReferenceRef_strategy = st.builds(
    frontend_mappings_ReferenceRef,
    featureName=
        safe_text,
    multivalued=
        st.booleans()
)
AttributeModifier_strategy = st.builds(
    AttributeModifier,
)
frontend_mappings_DefaultValue_strategy = st.builds(
    frontend_mappings_DefaultValue,
)
Class2Class_strategy = st.builds(
    Class2Class,
)
mappings_AttributeRightPart_strategy = st.builds(
    mappings_AttributeRightPart,
)
mappings_Feature2Feature_strategy = st.builds(
    mappings_Feature2Feature,
)
frontend_mappings_FeatureRef_strategy = st.builds(
    frontend_mappings_FeatureRef,
    featureName=
        safe_text,
    multivalued=
        st.booleans()
)
frontend_mappings_Attribute2Attribute_strategy = st.builds(
    frontend_mappings_Attribute2Attribute,
    cardinality=
        safe_text
)
Operator_strategy = st.builds(
    Operator,
)
frontend_mappings_Join_strategy = st.builds(
    frontend_mappings_Join,
)
frontend_mappings_Split_strategy = st.builds(
    frontend_mappings_Split,
)
frontend_mappings_ConvertModifier_strategy = st.builds(
    frontend_mappings_ConvertModifier,
    converter=
        safe_text
)
Modifier_strategy = st.builds(
    Modifier,
)
frontend_mappings_AttributeModifier_strategy = st.builds(
    frontend_mappings_AttributeModifier,
)
frontend_mappings_Modifier_strategy = st.builds(
    frontend_mappings_Modifier,
)
ClassRef_strategy = st.builds(
    ClassRef,
)
ReferenceRef_strategy = st.builds(
    ReferenceRef,
)
ClassMapping_strategy = st.builds(
    ClassMapping,
)
frontend_mappings_Class2Class_strategy = st.builds(
    frontend_mappings_Class2Class,
    cardinality=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
frontend_qool_Segment_strategy = st.builds(
    frontend_qool_Segment,
)
frontend_mappings_Tag_strategy = st.builds(
    frontend_mappings_Tag,
)
frontend_mappings_Converter_strategy = st.builds(
    frontend_mappings_Converter,
    isExternal=
        safe_text,
    converterName=
        safe_text
)
ResolveLink_strategy = st.builds(
    ResolveLink,
)
Attribute2Attribute_strategy = st.builds(
    Attribute2Attribute,
)
Section_strategy = st.builds(
    Section,
)
C2CModifier_strategy = st.builds(
    C2CModifier,
)
frontend_mappings_RelatedBy_strategy = st.builds(
    frontend_mappings_RelatedBy,
)
frontend_mappings_EqualityFilter_strategy = st.builds(
    frontend_mappings_EqualityFilter,
    filter=
        safe_text
)
frontend_mappings_LinkedBy_strategy = st.builds(
    frontend_mappings_LinkedBy,
)
MappingElement_strategy = st.builds(
    MappingElement,
)
frontend_mappings_C2CModifier_strategy = st.builds(
    frontend_mappings_C2CModifier,
)
Tag_strategy = st.builds(
    Tag,
)
UseDeclaration_strategy = st.builds(
    UseDeclaration,
)
MatchedElement_strategy = st.builds(
    MatchedElement,
)
mappings_MappingVariable_strategy = st.builds(
    mappings_MappingVariable,
)
core_ClassUse_strategy = st.builds(
    core_ClassUse,
)
frontend_mappings_MatchedElement_strategy = st.builds(
    frontend_mappings_MatchedElement,
)
Context_strategy = st.builds(
    Context,
)
frontend_mappings_AttributeRightPart_strategy = st.builds(
    frontend_mappings_AttributeRightPart,
)
AttributeRightPart_strategy = st.builds(
    AttributeRightPart,
)
frontend_mappings_AttributeIsResolveLink_strategy = st.builds(
    frontend_mappings_AttributeIsResolveLink,
)
frontend_mappings_AttributeIsDouble_strategy = st.builds(
    frontend_mappings_AttributeIsDouble,
    doubleValue=
        safe_text
)
frontend_mappings_AttributeIsBoolean_strategy = st.builds(
    frontend_mappings_AttributeIsBoolean,
    boolValue=
        safe_text
)
frontend_mappings_AttributeIsString_strategy = st.builds(
    frontend_mappings_AttributeIsString,
    strValue=
        safe_text
)
frontend_mappings_AttributeIsInteger_strategy = st.builds(
    frontend_mappings_AttributeIsInteger,
    intValue=
        st.integers()
)
AttributeRef_strategy = st.builds(
    AttributeRef,
)
Feature2Feature_strategy = st.builds(
    Feature2Feature,
)
frontend_mappings_Reference2Reference_strategy = st.builds(
    frontend_mappings_Reference2Reference,
    cardinality=
        safe_text,
    resolverName=
        safe_text
)
frontend_mappings_AttributeMapping_strategy = st.builds(
    frontend_mappings_AttributeMapping,
)
Converter_strategy = st.builds(
    Converter,
)
FeatureRef_strategy = st.builds(
    FeatureRef,
)
frontend_mappings_Feature2Feature_strategy = st.builds(
    frontend_mappings_Feature2Feature,
)
frontend_mappings_ClassMapping_strategy = st.builds(
    frontend_mappings_ClassMapping,
)
frontend_patterns_POutputVariable_strategy = st.builds(
    frontend_patterns_POutputVariable,
)
POutputVariable_strategy = st.builds(
    POutputVariable,
)
PObject_strategy = st.builds(
    PObject,
)
Pattern_strategy = st.builds(
    Pattern,
)
core_TransformationDefinition_strategy = st.builds(
    core_TransformationDefinition,
)
chain_AvailableTransformation_strategy = st.builds(
    chain_AvailableTransformation,
)
frontend_chain_CompositeTransformation_strategy = st.builds(
    frontend_chain_CompositeTransformation,
)
frontend_chain_AvailableTransformation_strategy = st.builds(
    frontend_chain_AvailableTransformation,
)
RepresentModel_strategy = st.builds(
    RepresentModel,
)
AvailableTransformation_strategy = st.builds(
    AvailableTransformation,
)
Delegate_strategy = st.builds(
    Delegate,
)
PReference_strategy = st.builds(
    PReference,
)
frontend_patterns_CollectionReference_strategy = st.builds(
    frontend_patterns_CollectionReference,
)
PFeature_strategy = st.builds(
    PFeature,
)
frontend_patterns_PReference_strategy = st.builds(
    frontend_patterns_PReference,
)
frontend_patterns_PAttribute_strategy = st.builds(
    frontend_patterns_PAttribute,
)
MethodSelf_strategy = st.builds(
    MethodSelf,
)
MethodParameter_strategy = st.builds(
    MethodParameter,
)
MethodDefinition_strategy = st.builds(
    MethodDefinition,
)
Variable_strategy = st.builds(
    Variable,
)
frontend_tao_TemplateParameter_strategy = st.builds(
    frontend_tao_TemplateParameter,
)
frontend_mappings_MappingVariable_strategy = st.builds(
    frontend_mappings_MappingVariable,
)
frontend_tao_ObjectSourceVariable_strategy = st.builds(
    frontend_tao_ObjectSourceVariable,
)
frontend_attribution_RuleSelf_strategy = st.builds(
    frontend_attribution_RuleSelf,
)
Expression_strategy = st.builds(
    Expression,
)
frontend_qool_MatchExpression_strategy = st.builds(
    frontend_qool_MatchExpression,
)
frontend_attribution_AttributeUse_strategy = st.builds(
    frontend_attribution_AttributeUse,
)
frontend_qool_InvokeTransformation_strategy = st.builds(
    frontend_qool_InvokeTransformation,
    transformationName=
        safe_text,
    entryPointName=
        safe_text
)
frontend_facilities_Copier_strategy = st.builds(
    frontend_facilities_Copier,
)
RuleSelf_strategy = st.builds(
    RuleSelf,
)
core_RepresentModel_strategy = st.builds(
    core_RepresentModel,
)
TransformationExecution_strategy = st.builds(
    TransformationExecution,
)
GeneratedModel_strategy = st.builds(
    GeneratedModel,
)
ExternalTransformation_strategy = st.builds(
    ExternalTransformation,
)
CompositeTransformation_strategy = st.builds(
    CompositeTransformation,
)
frontend_imperative_MethodParameter_strategy = st.builds(
    frontend_imperative_MethodParameter,
)
frontend_imperative_MethodSelf_strategy = st.builds(
    frontend_imperative_MethodSelf,
)
Matcher_strategy = st.builds(
    Matcher,
)
core_NamedElement_strategy = st.builds(
    core_NamedElement,
)
frontend_chain_GeneratedModel_strategy = st.builds(
    frontend_chain_GeneratedModel,
)
frontend_chain_ExternalTransformation_strategy = st.builds(
    frontend_chain_ExternalTransformation,
)
core_LocatedElement_strategy = st.builds(
    core_LocatedElement,
)
frontend_tao_Template_strategy = st.builds(
    frontend_tao_Template,
)
frontend_qool_QoolQueue_strategy = st.builds(
    frontend_qool_QoolQueue,
)
frontend_koan_KoanRule_strategy = st.builds(
    frontend_koan_KoanRule,
)
KoanRule_strategy = st.builds(
    KoanRule,
)
TraceInterface_strategy = st.builds(
    TraceInterface,
)
Statement_strategy = st.builds(
    Statement,
)
frontend_tao_Assignment_strategy = st.builds(
    frontend_tao_Assignment,
)
frontend_qool_EmitStatement_strategy = st.builds(
    frontend_qool_EmitStatement,
)
frontend_attribution_AttributeInit_strategy = st.builds(
    frontend_attribution_AttributeInit,
)
TransformationDefinition_strategy = st.builds(
    TransformationDefinition,
)
frontend_chain_ChainTransformation_strategy = st.builds(
    frontend_chain_ChainTransformation,
)
frontend_imperative_ImperativeTransformation_strategy = st.builds(
    frontend_imperative_ImperativeTransformation,
)
frontend_koan_KoanTransformation_strategy = st.builds(
    frontend_koan_KoanTransformation,
)
frontend_tao_TaoTransformation_strategy = st.builds(
    frontend_tao_TaoTransformation,
)
frontend_qool_QoolTransformation_strategy = st.builds(
    frontend_qool_QoolTransformation,
)
frontend_patterns_PatternSpecification_strategy = st.builds(
    frontend_patterns_PatternSpecification,
)
frontend_mappings_MappingTransformation_strategy = st.builds(
    frontend_mappings_MappingTransformation,
)
frontend_script_ScriptedTransformation_strategy = st.builds(
    frontend_script_ScriptedTransformation,
)
frontend_DummyRootMetaclass_strategy = st.builds(
    frontend_DummyRootMetaclass,
)
core_TypedWithClass_strategy = st.builds(
    core_TypedWithClass,
)
AttributionRule_strategy = st.builds(
    AttributionRule,
)
AttributeDcl_strategy = st.builds(
    AttributeDcl,
)
frontend_attribution_SynthesizedAttributeDcl_strategy = st.builds(
    frontend_attribution_SynthesizedAttributeDcl,
)
frontend_attribution_InheritedAttributeDcl_strategy = st.builds(
    frontend_attribution_InheritedAttributeDcl,
)
frontend_attribution_AttributionTransformation_strategy = st.builds(
    frontend_attribution_AttributionTransformation,
)
ClassUse_strategy = st.builds(
    ClassUse,
)
core_Variable_strategy = st.builds(
    core_Variable,
)
frontend_attribution_AttributeDcl_strategy = st.builds(
    frontend_attribution_AttributeDcl,
)
frontend_tao_ObjectInstantiation_strategy = st.builds(
    frontend_tao_ObjectInstantiation,
)
frontend_qool_IteratorStatement_strategy = st.builds(
    frontend_qool_IteratorStatement,
)
frontend_patterns_PObject_strategy = st.builds(
    frontend_patterns_PObject,
)
frontend_tao_ReferenceAssignment_strategy = st.builds(
    frontend_tao_ReferenceAssignment,
    targetFeature=
        safe_text,
    multivalued=
        st.booleans()
)
koan_Matcher_strategy = st.builds(
    koan_Matcher,
)
frontend_koan_ForAllMatcher_strategy = st.builds(
    frontend_koan_ForAllMatcher,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
frontend_chain_TransformationExecution_strategy = st.builds(
    frontend_chain_TransformationExecution,
)
frontend_patterns_Pattern_strategy = st.builds(
    frontend_patterns_Pattern,
    name=
        safe_text
)
frontend_attribution_AttributionRule_strategy = st.builds(
    frontend_attribution_AttributionRule,
)
frontend_imperative_MethodDefinition_strategy = st.builds(
    frontend_imperative_MethodDefinition,
    name=
        safe_text
)
frontend_tao_SourceExpression_strategy = st.builds(
    frontend_tao_SourceExpression,
)
frontend_mappings_Section_strategy = st.builds(
    frontend_mappings_Section,
    sectionType=
        safe_text
)
frontend_mappings_Delegate_strategy = st.builds(
    frontend_mappings_Delegate,
    featureName=
        safe_text,
    isExternal=
        safe_text,
    linkName=
        safe_text
)
frontend_mappings_MappingElement_strategy = st.builds(
    frontend_mappings_MappingElement,
)
frontend_patterns_PFeature_strategy = st.builds(
    frontend_patterns_PFeature,
    name=
        safe_text
)
frontend_mappings_Operator_strategy = st.builds(
    frontend_mappings_Operator,
)
frontend_mappings_Context_strategy = st.builds(
    frontend_mappings_Context,
)
frontend_koan_Matcher_strategy = st.builds(
    frontend_koan_Matcher,
)
frontend_core_PutTraceParameter_strategy = st.builds(
    frontend_core_PutTraceParameter,
)
PutTraceParameter_strategy = st.builds(
    PutTraceParameter,
)
frontend_core_PutTrace_strategy = st.builds(
    frontend_core_PutTrace,
)
frontend_core_InlineFeature_strategy = st.builds(
    frontend_core_InlineFeature,
    multivalued=
        st.booleans()
)
InlineFeature_strategy = st.builds(
    InlineFeature,
)
frontend_core_InlineClass_strategy = st.builds(
    frontend_core_InlineClass,
)
InlineClass_strategy = st.builds(
    InlineClass,
)
core_ModuleDefinition_strategy = st.builds(
    core_ModuleDefinition,
)
frontend_core_InlineModel_strategy = st.builds(
    frontend_core_InlineModel,
)
frontend_core_TraceElement_strategy = st.builds(
    frontend_core_TraceElement,
)
TraceElement_strategy = st.builds(
    TraceElement,
)
frontend_core_TraceDefinition_strategy = st.builds(
    frontend_core_TraceDefinition,
)
frontend_core_TraceInterface_strategy = st.builds(
    frontend_core_TraceInterface,
)
frontend_core_TypedWithClass_strategy = st.builds(
    frontend_core_TypedWithClass,
)
TraceDefinition_strategy = st.builds(
    TraceDefinition,
)
frontend_core_TraceUse_strategy = st.builds(
    frontend_core_TraceUse,
)
frontend_core_TraceCompareExpression_strategy = st.builds(
    frontend_core_TraceCompareExpression,
    multivaluedTag=
        st.booleans()
)
TraceCompareExpression_strategy = st.builds(
    TraceCompareExpression,
)
frontend_core_MatchTrace_strategy = st.builds(
    frontend_core_MatchTrace,
    cardinality=
        safe_text
)
frontend_core_InlineReference_strategy = st.builds(
    frontend_core_InlineReference,
)
frontend_core_InlineAttribute_strategy = st.builds(
    frontend_core_InlineAttribute,
)
frontend_core_IfBranch_strategy = st.builds(
    frontend_core_IfBranch,
)
IfBranch_strategy = st.builds(
    IfBranch,
)
frontend_core_IfExpr_strategy = st.builds(
    frontend_core_IfExpr,
)
core_ImplicitlyAnnotableElement_strategy = st.builds(
    core_ImplicitlyAnnotableElement,
)
core_TypeExpression_strategy = st.builds(
    core_TypeExpression,
)
frontend_core_ClassUse_strategy = st.builds(
    frontend_core_ClassUse,
    strictType=
        st.booleans(),
    className=
        safe_text
)
frontend_core_TypeExpression_strategy = st.builds(
    frontend_core_TypeExpression,
)
frontend_core_BooleanLiteral_strategy = st.builds(
    frontend_core_BooleanLiteral,
    value=
        st.booleans()
)
frontend_core_StringLiteral_strategy = st.builds(
    frontend_core_StringLiteral,
    value=
        safe_text
)
frontend_core_DoubleLiteral_strategy = st.builds(
    frontend_core_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
frontend_core_NumLiteral_strategy = st.builds(
    frontend_core_NumLiteral,
    value=
        st.integers()
)
frontend_core_BinaryExpr_strategy = st.builds(
    frontend_core_BinaryExpr,
    binaryOp=
        safe_text
)
frontend_core_KeywordParameter_strategy = st.builds(
    frontend_core_KeywordParameter,
    keyword=
        safe_text
)
KeywordParameter_strategy = st.builds(
    KeywordParameter,
)
frontend_core_KeywordMethodCall_strategy = st.builds(
    frontend_core_KeywordMethodCall,
)
frontend_core_MethodCall_strategy = st.builds(
    frontend_core_MethodCall,
    withParameters=
        st.booleans(),
    methodName=
        safe_text
)
frontend_core_VariableReference_strategy = st.builds(
    frontend_core_VariableReference,
)
core_Expression_strategy = st.builds(
    core_Expression,
)
frontend_core_ModelReference_strategy = st.builds(
    frontend_core_ModelReference,
)
frontend_core_ResolveLink_strategy = st.builds(
    frontend_core_ResolveLink,
    featureName=
        safe_text,
    linkName=
        safe_text,
    isExternal=
        safe_text
)
frontend_core_ClosureParameter_strategy = st.builds(
    frontend_core_ClosureParameter,
)
ClosureParameter_strategy = st.builds(
    ClosureParameter,
)
frontend_core_ClosureDeclaration_strategy = st.builds(
    frontend_core_ClosureDeclaration,
)
frontend_core_Variable_strategy = st.builds(
    frontend_core_Variable,
    name=
        safe_text
)
frontend_core_RequireParameter_strategy = st.builds(
    frontend_core_RequireParameter,
    formalParameterName=
        safe_text
)
RequireParameter_strategy = st.builds(
    RequireParameter,
)
frontend_core_RequireModelParameter_strategy = st.builds(
    frontend_core_RequireModelParameter,
)
frontend_core_RequireDeclaration_strategy = st.builds(
    frontend_core_RequireDeclaration,
    name=
        safe_text,
    default=
        safe_text
)
frontend_core_UseDeclaration_strategy = st.builds(
    frontend_core_UseDeclaration,
    module=
        safe_text,
    as_=
        safe_text
)
frontend_core_ImportedModel_strategy = st.builds(
    frontend_core_ImportedModel,
)
core_DefinitionParameter_strategy = st.builds(
    core_DefinitionParameter,
)
frontend_core_TracedModelParameter_strategy = st.builds(
    frontend_core_TracedModelParameter,
)
frontend_core_TransformationDefinitionParameter_strategy = st.builds(
    frontend_core_TransformationDefinitionParameter,
)
frontend_core_EclecticTransformationDefinition_strategy = st.builds(
    frontend_core_EclecticTransformationDefinition,
)
RequireDeclaration_strategy = st.builds(
    RequireDeclaration,
)
InlineModel_strategy = st.builds(
    InlineModel,
)
frontend_core_PropertyWrite_strategy = st.builds(
    frontend_core_PropertyWrite,
    _property=
        safe_text
)
frontend_core_DefineVariable_strategy = st.builds(
    frontend_core_DefineVariable,
)
frontend_core_Expression_strategy = st.builds(
    frontend_core_Expression,
)
frontend_core_Statement_strategy = st.builds(
    frontend_core_Statement,
)
AnnotableElement_strategy = st.builds(
    AnnotableElement,
)
frontend_core_RepresentModel_strategy = st.builds(
    frontend_core_RepresentModel,
)
frontend_core_Annotation_strategy = st.builds(
    frontend_core_Annotation,
)
SingleAnnotation_strategy = st.builds(
    SingleAnnotation,
)
frontend_core_PotencyAnnotation_strategy = st.builds(
    frontend_core_PotencyAnnotation,
    value=
        safe_text
)
frontend_core_ImplicitlyAnnotableElement_strategy = st.builds(
    frontend_core_ImplicitlyAnnotableElement,
)
Annotation_strategy = st.builds(
    Annotation,
)
frontend_core_SingleAnnotation_strategy = st.builds(
    frontend_core_SingleAnnotation,
)
frontend_core_OptimizationsAnnotation_strategy = st.builds(
    frontend_core_OptimizationsAnnotation,
    enabled=
        st.booleans()
)
frontend_core_MetamodelModelAnnotation_strategy = st.builds(
    frontend_core_MetamodelModelAnnotation,
    metamodel=
        safe_text
)
frontend_core_AnnotableElement_strategy = st.builds(
    frontend_core_AnnotableElement,
)
core_AnnotableElement_strategy = st.builds(
    core_AnnotableElement,
)
frontend_core_ModuleDefinition_strategy = st.builds(
    frontend_core_ModuleDefinition,
)
DefinitionParameter_strategy = st.builds(
    DefinitionParameter,
)
frontend_core_ModuleParameter_strategy = st.builds(
    frontend_core_ModuleParameter,
)
frontend_core_DefinitionParameter_strategy = st.builds(
    frontend_core_DefinitionParameter,
)

@given(instance=frontend_core_NamedElement_strategy)
@settings(max_examples=50)
def test_frontend_core_namedelement_instantiation(instance):
    assert isinstance(instance, frontend_core_NamedElement)



@given(instance=frontend_core_NamedElement_strategy)
def test_frontend_core_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend_core_LocatedElement_strategy)
@settings(max_examples=50)
def test_frontend_core_locatedelement_instantiation(instance):
    assert isinstance(instance, frontend_core_LocatedElement)



@given(instance=frontend_core_LocatedElement_strategy)
def test_frontend_core_locatedelement_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=frontend_core_LocatedElement_strategy)
def test_frontend_core_locatedelement_row_setter(instance):
    original = instance.row
    instance.row = original
    assert instance.row == original



@given(instance=frontend_core_LocatedElement_strategy)
def test_frontend_core_locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=ImportedModel_strategy)
@settings(max_examples=50)
def test_importedmodel_instantiation(instance):
    assert isinstance(instance, ImportedModel)

@given(instance=ModuleDefinition_strategy)
@settings(max_examples=50)
def test_moduledefinition_instantiation(instance):
    assert isinstance(instance, ModuleDefinition)

@given(instance=frontend_core_TransformationDefinition_strategy)
@settings(max_examples=50)
def test_frontend_core_transformationdefinition_instantiation(instance):
    assert isinstance(instance, frontend_core_TransformationDefinition)

@given(instance=frontend_core_AnnotationParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_annotationparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_AnnotationParameter)

@given(instance=AnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotationparameter_instantiation(instance):
    assert isinstance(instance, AnnotationParameter)

@given(instance=frontend_core_GenericAnnotation_strategy)
@settings(max_examples=50)
def test_frontend_core_genericannotation_instantiation(instance):
    assert isinstance(instance, frontend_core_GenericAnnotation)



@given(instance=frontend_core_GenericAnnotation_strategy)
def test_frontend_core_genericannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ObjectSourceVariable_strategy)
@settings(max_examples=50)
def test_objectsourcevariable_instantiation(instance):
    assert isinstance(instance, ObjectSourceVariable)

@given(instance=SourceExpression_strategy)
@settings(max_examples=50)
def test_sourceexpression_instantiation(instance):
    assert isinstance(instance, SourceExpression)

@given(instance=frontend_tao_WithOptionalVariableExpression_strategy)
@settings(max_examples=50)
def test_frontend_tao_withoptionalvariableexpression_instantiation(instance):
    assert isinstance(instance, frontend_tao_WithOptionalVariableExpression)

@given(instance=TemplateRootObject_strategy)
@settings(max_examples=50)
def test_templaterootobject_instantiation(instance):
    assert isinstance(instance, TemplateRootObject)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=ObjectInstantiation_strategy)
@settings(max_examples=50)
def test_objectinstantiation_instantiation(instance):
    assert isinstance(instance, ObjectInstantiation)

@given(instance=frontend_tao_TemplateRootObject_strategy)
@settings(max_examples=50)
def test_frontend_tao_templaterootobject_instantiation(instance):
    assert isinstance(instance, frontend_tao_TemplateRootObject)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=frontend_tao_AttributeAssigment_strategy)
@settings(max_examples=50)
def test_frontend_tao_attributeassigment_instantiation(instance):
    assert isinstance(instance, frontend_tao_AttributeAssigment)



@given(instance=frontend_tao_AttributeAssigment_strategy)
def test_frontend_tao_attributeassigment_targetFeature_setter(instance):
    original = instance.targetFeature
    instance.targetFeature = original
    assert instance.targetFeature == original

@given(instance=ReferenceAssignment_strategy)
@settings(max_examples=50)
def test_referenceassignment_instantiation(instance):
    assert isinstance(instance, ReferenceAssignment)

@given(instance=frontend_tao_Invocation_strategy)
@settings(max_examples=50)
def test_frontend_tao_invocation_instantiation(instance):
    assert isinstance(instance, frontend_tao_Invocation)

@given(instance=frontend_tao_ObjectSyntax_strategy)
@settings(max_examples=50)
def test_frontend_tao_objectsyntax_instantiation(instance):
    assert isinstance(instance, frontend_tao_ObjectSyntax)

@given(instance=tao_Assignment_strategy)
@settings(max_examples=50)
def test_tao_assignment_instantiation(instance):
    assert isinstance(instance, tao_Assignment)

@given(instance=frontend_facilities_CopierCallbackDefinition_strategy)
@settings(max_examples=50)
def test_frontend_facilities_copiercallbackdefinition_instantiation(instance):
    assert isinstance(instance, frontend_facilities_CopierCallbackDefinition)



@given(instance=frontend_facilities_CopierCallbackDefinition_strategy)
def test_frontend_facilities_copiercallbackdefinition_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=facilities_CopierCallbackDefinition_strategy)
@settings(max_examples=50)
def test_facilities_copiercallbackdefinition_instantiation(instance):
    assert isinstance(instance, facilities_CopierCallbackDefinition)

@given(instance=Template_strategy)
@settings(max_examples=50)
def test_template_instantiation(instance):
    assert isinstance(instance, Template)

@given(instance=InvokeTransformation_strategy)
@settings(max_examples=50)
def test_invoketransformation_instantiation(instance):
    assert isinstance(instance, InvokeTransformation)

@given(instance=frontend_qool_InvokeExternal_strategy)
@settings(max_examples=50)
def test_frontend_qool_invokeexternal_instantiation(instance):
    assert isinstance(instance, frontend_qool_InvokeExternal)



@given(instance=frontend_qool_InvokeExternal_strategy)
def test_frontend_qool_invokeexternal_queueName_setter(instance):
    original = instance.queueName
    instance.queueName = original
    assert instance.queueName == original



@given(instance=frontend_qool_InvokeExternal_strategy)
def test_frontend_qool_invokeexternal_traceAttributeName_setter(instance):
    original = instance.traceAttributeName
    instance.traceAttributeName = original
    assert instance.traceAttributeName == original

@given(instance=NamedInvocationParameter_strategy)
@settings(max_examples=50)
def test_namedinvocationparameter_instantiation(instance):
    assert isinstance(instance, NamedInvocationParameter)

@given(instance=InvocationParameter_strategy)
@settings(max_examples=50)
def test_invocationparameter_instantiation(instance):
    assert isinstance(instance, InvocationParameter)

@given(instance=frontend_qool_NamedInvocationParameter_strategy)
@settings(max_examples=50)
def test_frontend_qool_namedinvocationparameter_instantiation(instance):
    assert isinstance(instance, frontend_qool_NamedInvocationParameter)



@given(instance=frontend_qool_NamedInvocationParameter_strategy)
def test_frontend_qool_namedinvocationparameter_formalName_setter(instance):
    original = instance.formalName
    instance.formalName = original
    assert instance.formalName == original

@given(instance=TransformationDefinitionParameter_strategy)
@settings(max_examples=50)
def test_transformationdefinitionparameter_instantiation(instance):
    assert isinstance(instance, TransformationDefinitionParameter)

@given(instance=frontend_qool_InvocationParameter_strategy)
@settings(max_examples=50)
def test_frontend_qool_invocationparameter_instantiation(instance):
    assert isinstance(instance, frontend_qool_InvocationParameter)



@given(instance=frontend_qool_InvocationParameter_strategy)
def test_frontend_qool_invocationparameter_calleeModelName_setter(instance):
    original = instance.calleeModelName
    instance.calleeModelName = original
    assert instance.calleeModelName == original

@given(instance=frontend_qool_InvokeInternal_strategy)
@settings(max_examples=50)
def test_frontend_qool_invokeinternal_instantiation(instance):
    assert isinstance(instance, frontend_qool_InvokeInternal)

@given(instance=IteratorStatement_strategy)
@settings(max_examples=50)
def test_iteratorstatement_instantiation(instance):
    assert isinstance(instance, IteratorStatement)

@given(instance=frontend_qool_ForEachStatement_strategy)
@settings(max_examples=50)
def test_frontend_qool_foreachstatement_instantiation(instance):
    assert isinstance(instance, frontend_qool_ForEachStatement)

@given(instance=frontend_qool_ForAllStatement_strategy)
@settings(max_examples=50)
def test_frontend_qool_forallstatement_instantiation(instance):
    assert isinstance(instance, frontend_qool_ForAllStatement)

@given(instance=core_Statement_strategy)
@settings(max_examples=50)
def test_core_statement_instantiation(instance):
    assert isinstance(instance, core_Statement)

@given(instance=TypeExpression_strategy)
@settings(max_examples=50)
def test_typeexpression_instantiation(instance):
    assert isinstance(instance, TypeExpression)

@given(instance=frontend_qool_QueueOptimization_strategy)
@settings(max_examples=50)
def test_frontend_qool_queueoptimization_instantiation(instance):
    assert isinstance(instance, frontend_qool_QueueOptimization)

@given(instance=QueueOptimization_strategy)
@settings(max_examples=50)
def test_queueoptimization_instantiation(instance):
    assert isinstance(instance, QueueOptimization)

@given(instance=frontend_qool_AccessByFeatureOptimization_strategy)
@settings(max_examples=50)
def test_frontend_qool_accessbyfeatureoptimization_instantiation(instance):
    assert isinstance(instance, frontend_qool_AccessByFeatureOptimization)



@given(instance=frontend_qool_AccessByFeatureOptimization_strategy)
def test_frontend_qool_accessbyfeatureoptimization_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=frontend_qool_AccessByFeatureOptimization_strategy)
def test_frontend_qool_accessbyfeatureoptimization_force_setter(instance):
    original = instance.force
    instance.force = original
    assert instance.force == original

@given(instance=frontend_qool_MatchPredicate_strategy)
@settings(max_examples=50)
def test_frontend_qool_matchpredicate_instantiation(instance):
    assert isinstance(instance, frontend_qool_MatchPredicate)

@given(instance=MatchPredicate_strategy)
@settings(max_examples=50)
def test_matchpredicate_instantiation(instance):
    assert isinstance(instance, MatchPredicate)

@given(instance=frontend_qool_KindOfPredicate_strategy)
@settings(max_examples=50)
def test_frontend_qool_kindofpredicate_instantiation(instance):
    assert isinstance(instance, frontend_qool_KindOfPredicate)

@given(instance=frontend_qool_PropertyEqualsPredicate_strategy)
@settings(max_examples=50)
def test_frontend_qool_propertyequalspredicate_instantiation(instance):
    assert isinstance(instance, frontend_qool_PropertyEqualsPredicate)



@given(instance=frontend_qool_PropertyEqualsPredicate_strategy)
def test_frontend_qool_propertyequalspredicate_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=mappings_MetamodelElementRef_strategy)
@settings(max_examples=50)
def test_mappings_metamodelelementref_instantiation(instance):
    assert isinstance(instance, mappings_MetamodelElementRef)

@given(instance=MetamodelElementRef_strategy)
@settings(max_examples=50)
def test_metamodelelementref_instantiation(instance):
    assert isinstance(instance, MetamodelElementRef)

@given(instance=frontend_mappings_AttributeRef_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributeref_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeRef)



@given(instance=frontend_mappings_AttributeRef_strategy)
def test_frontend_mappings_attributeref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=frontend_mappings_AttributeRef_strategy)
def test_frontend_mappings_attributeref_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=frontend_mappings_ClassRef_strategy)
@settings(max_examples=50)
def test_frontend_mappings_classref_instantiation(instance):
    assert isinstance(instance, frontend_mappings_ClassRef)

@given(instance=frontend_mappings_MetamodelElementRef_strategy)
@settings(max_examples=50)
def test_frontend_mappings_metamodelelementref_instantiation(instance):
    assert isinstance(instance, frontend_mappings_MetamodelElementRef)

@given(instance=DefaultValue_strategy)
@settings(max_examples=50)
def test_defaultvalue_instantiation(instance):
    assert isinstance(instance, DefaultValue)

@given(instance=frontend_mappings_IntDefaultValue_strategy)
@settings(max_examples=50)
def test_frontend_mappings_intdefaultvalue_instantiation(instance):
    assert isinstance(instance, frontend_mappings_IntDefaultValue)



@given(instance=frontend_mappings_IntDefaultValue_strategy)
def test_frontend_mappings_intdefaultvalue_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=Segment_strategy)
@settings(max_examples=50)
def test_segment_instantiation(instance):
    assert isinstance(instance, Segment)

@given(instance=QoolQueue_strategy)
@settings(max_examples=50)
def test_qoolqueue_instantiation(instance):
    assert isinstance(instance, QoolQueue)

@given(instance=frontend_qool_LocalQueue_strategy)
@settings(max_examples=50)
def test_frontend_qool_localqueue_instantiation(instance):
    assert isinstance(instance, frontend_qool_LocalQueue)

@given(instance=frontend_qool_ModelElementQueue_strategy)
@settings(max_examples=50)
def test_frontend_qool_modelelementqueue_instantiation(instance):
    assert isinstance(instance, frontend_qool_ModelElementQueue)

@given(instance=frontend_mappings_ReferenceRef_strategy)
@settings(max_examples=50)
def test_frontend_mappings_referenceref_instantiation(instance):
    assert isinstance(instance, frontend_mappings_ReferenceRef)



@given(instance=frontend_mappings_ReferenceRef_strategy)
def test_frontend_mappings_referenceref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=frontend_mappings_ReferenceRef_strategy)
def test_frontend_mappings_referenceref_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=AttributeModifier_strategy)
@settings(max_examples=50)
def test_attributemodifier_instantiation(instance):
    assert isinstance(instance, AttributeModifier)

@given(instance=frontend_mappings_DefaultValue_strategy)
@settings(max_examples=50)
def test_frontend_mappings_defaultvalue_instantiation(instance):
    assert isinstance(instance, frontend_mappings_DefaultValue)

@given(instance=Class2Class_strategy)
@settings(max_examples=50)
def test_class2class_instantiation(instance):
    assert isinstance(instance, Class2Class)

@given(instance=mappings_AttributeRightPart_strategy)
@settings(max_examples=50)
def test_mappings_attributerightpart_instantiation(instance):
    assert isinstance(instance, mappings_AttributeRightPart)

@given(instance=mappings_Feature2Feature_strategy)
@settings(max_examples=50)
def test_mappings_feature2feature_instantiation(instance):
    assert isinstance(instance, mappings_Feature2Feature)

@given(instance=frontend_mappings_FeatureRef_strategy)
@settings(max_examples=50)
def test_frontend_mappings_featureref_instantiation(instance):
    assert isinstance(instance, frontend_mappings_FeatureRef)



@given(instance=frontend_mappings_FeatureRef_strategy)
def test_frontend_mappings_featureref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=frontend_mappings_FeatureRef_strategy)
def test_frontend_mappings_featureref_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=frontend_mappings_Attribute2Attribute_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attribute2attribute_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Attribute2Attribute)



@given(instance=frontend_mappings_Attribute2Attribute_strategy)
def test_frontend_mappings_attribute2attribute_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=frontend_mappings_Join_strategy)
@settings(max_examples=50)
def test_frontend_mappings_join_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Join)

@given(instance=frontend_mappings_Split_strategy)
@settings(max_examples=50)
def test_frontend_mappings_split_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Split)

@given(instance=frontend_mappings_ConvertModifier_strategy)
@settings(max_examples=50)
def test_frontend_mappings_convertmodifier_instantiation(instance):
    assert isinstance(instance, frontend_mappings_ConvertModifier)



@given(instance=frontend_mappings_ConvertModifier_strategy)
def test_frontend_mappings_convertmodifier_converter_setter(instance):
    original = instance.converter
    instance.converter = original
    assert instance.converter == original

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=frontend_mappings_AttributeModifier_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributemodifier_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeModifier)

@given(instance=frontend_mappings_Modifier_strategy)
@settings(max_examples=50)
def test_frontend_mappings_modifier_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Modifier)

@given(instance=ClassRef_strategy)
@settings(max_examples=50)
def test_classref_instantiation(instance):
    assert isinstance(instance, ClassRef)

@given(instance=ReferenceRef_strategy)
@settings(max_examples=50)
def test_referenceref_instantiation(instance):
    assert isinstance(instance, ReferenceRef)

@given(instance=ClassMapping_strategy)
@settings(max_examples=50)
def test_classmapping_instantiation(instance):
    assert isinstance(instance, ClassMapping)

@given(instance=frontend_mappings_Class2Class_strategy)
@settings(max_examples=50)
def test_frontend_mappings_class2class_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Class2Class)



@given(instance=frontend_mappings_Class2Class_strategy)
def test_frontend_mappings_class2class_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=frontend_qool_Segment_strategy)
@settings(max_examples=50)
def test_frontend_qool_segment_instantiation(instance):
    assert isinstance(instance, frontend_qool_Segment)

@given(instance=frontend_mappings_Tag_strategy)
@settings(max_examples=50)
def test_frontend_mappings_tag_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Tag)

@given(instance=frontend_mappings_Converter_strategy)
@settings(max_examples=50)
def test_frontend_mappings_converter_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Converter)



@given(instance=frontend_mappings_Converter_strategy)
def test_frontend_mappings_converter_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original



@given(instance=frontend_mappings_Converter_strategy)
def test_frontend_mappings_converter_converterName_setter(instance):
    original = instance.converterName
    instance.converterName = original
    assert instance.converterName == original

@given(instance=ResolveLink_strategy)
@settings(max_examples=50)
def test_resolvelink_instantiation(instance):
    assert isinstance(instance, ResolveLink)

@given(instance=Attribute2Attribute_strategy)
@settings(max_examples=50)
def test_attribute2attribute_instantiation(instance):
    assert isinstance(instance, Attribute2Attribute)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=C2CModifier_strategy)
@settings(max_examples=50)
def test_c2cmodifier_instantiation(instance):
    assert isinstance(instance, C2CModifier)

@given(instance=frontend_mappings_RelatedBy_strategy)
@settings(max_examples=50)
def test_frontend_mappings_relatedby_instantiation(instance):
    assert isinstance(instance, frontend_mappings_RelatedBy)

@given(instance=frontend_mappings_EqualityFilter_strategy)
@settings(max_examples=50)
def test_frontend_mappings_equalityfilter_instantiation(instance):
    assert isinstance(instance, frontend_mappings_EqualityFilter)



@given(instance=frontend_mappings_EqualityFilter_strategy)
def test_frontend_mappings_equalityfilter_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=frontend_mappings_LinkedBy_strategy)
@settings(max_examples=50)
def test_frontend_mappings_linkedby_instantiation(instance):
    assert isinstance(instance, frontend_mappings_LinkedBy)

@given(instance=MappingElement_strategy)
@settings(max_examples=50)
def test_mappingelement_instantiation(instance):
    assert isinstance(instance, MappingElement)

@given(instance=frontend_mappings_C2CModifier_strategy)
@settings(max_examples=50)
def test_frontend_mappings_c2cmodifier_instantiation(instance):
    assert isinstance(instance, frontend_mappings_C2CModifier)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=UseDeclaration_strategy)
@settings(max_examples=50)
def test_usedeclaration_instantiation(instance):
    assert isinstance(instance, UseDeclaration)

@given(instance=MatchedElement_strategy)
@settings(max_examples=50)
def test_matchedelement_instantiation(instance):
    assert isinstance(instance, MatchedElement)

@given(instance=mappings_MappingVariable_strategy)
@settings(max_examples=50)
def test_mappings_mappingvariable_instantiation(instance):
    assert isinstance(instance, mappings_MappingVariable)

@given(instance=core_ClassUse_strategy)
@settings(max_examples=50)
def test_core_classuse_instantiation(instance):
    assert isinstance(instance, core_ClassUse)

@given(instance=frontend_mappings_MatchedElement_strategy)
@settings(max_examples=50)
def test_frontend_mappings_matchedelement_instantiation(instance):
    assert isinstance(instance, frontend_mappings_MatchedElement)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=frontend_mappings_AttributeRightPart_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributerightpart_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeRightPart)

@given(instance=AttributeRightPart_strategy)
@settings(max_examples=50)
def test_attributerightpart_instantiation(instance):
    assert isinstance(instance, AttributeRightPart)

@given(instance=frontend_mappings_AttributeIsResolveLink_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributeisresolvelink_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeIsResolveLink)

@given(instance=frontend_mappings_AttributeIsDouble_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributeisdouble_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeIsDouble)



@given(instance=frontend_mappings_AttributeIsDouble_strategy)
def test_frontend_mappings_attributeisdouble_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=frontend_mappings_AttributeIsBoolean_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributeisboolean_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeIsBoolean)



@given(instance=frontend_mappings_AttributeIsBoolean_strategy)
def test_frontend_mappings_attributeisboolean_boolValue_setter(instance):
    original = instance.boolValue
    instance.boolValue = original
    assert instance.boolValue == original

@given(instance=frontend_mappings_AttributeIsString_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributeisstring_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeIsString)



@given(instance=frontend_mappings_AttributeIsString_strategy)
def test_frontend_mappings_attributeisstring_strValue_setter(instance):
    original = instance.strValue
    instance.strValue = original
    assert instance.strValue == original

@given(instance=frontend_mappings_AttributeIsInteger_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributeisinteger_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeIsInteger)



@given(instance=frontend_mappings_AttributeIsInteger_strategy)
def test_frontend_mappings_attributeisinteger_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=AttributeRef_strategy)
@settings(max_examples=50)
def test_attributeref_instantiation(instance):
    assert isinstance(instance, AttributeRef)

@given(instance=Feature2Feature_strategy)
@settings(max_examples=50)
def test_feature2feature_instantiation(instance):
    assert isinstance(instance, Feature2Feature)

@given(instance=frontend_mappings_Reference2Reference_strategy)
@settings(max_examples=50)
def test_frontend_mappings_reference2reference_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Reference2Reference)



@given(instance=frontend_mappings_Reference2Reference_strategy)
def test_frontend_mappings_reference2reference_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original



@given(instance=frontend_mappings_Reference2Reference_strategy)
def test_frontend_mappings_reference2reference_resolverName_setter(instance):
    original = instance.resolverName
    instance.resolverName = original
    assert instance.resolverName == original

@given(instance=frontend_mappings_AttributeMapping_strategy)
@settings(max_examples=50)
def test_frontend_mappings_attributemapping_instantiation(instance):
    assert isinstance(instance, frontend_mappings_AttributeMapping)

@given(instance=Converter_strategy)
@settings(max_examples=50)
def test_converter_instantiation(instance):
    assert isinstance(instance, Converter)

@given(instance=FeatureRef_strategy)
@settings(max_examples=50)
def test_featureref_instantiation(instance):
    assert isinstance(instance, FeatureRef)

@given(instance=frontend_mappings_Feature2Feature_strategy)
@settings(max_examples=50)
def test_frontend_mappings_feature2feature_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Feature2Feature)

@given(instance=frontend_mappings_ClassMapping_strategy)
@settings(max_examples=50)
def test_frontend_mappings_classmapping_instantiation(instance):
    assert isinstance(instance, frontend_mappings_ClassMapping)

@given(instance=frontend_patterns_POutputVariable_strategy)
@settings(max_examples=50)
def test_frontend_patterns_poutputvariable_instantiation(instance):
    assert isinstance(instance, frontend_patterns_POutputVariable)

@given(instance=POutputVariable_strategy)
@settings(max_examples=50)
def test_poutputvariable_instantiation(instance):
    assert isinstance(instance, POutputVariable)

@given(instance=PObject_strategy)
@settings(max_examples=50)
def test_pobject_instantiation(instance):
    assert isinstance(instance, PObject)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=core_TransformationDefinition_strategy)
@settings(max_examples=50)
def test_core_transformationdefinition_instantiation(instance):
    assert isinstance(instance, core_TransformationDefinition)

@given(instance=chain_AvailableTransformation_strategy)
@settings(max_examples=50)
def test_chain_availabletransformation_instantiation(instance):
    assert isinstance(instance, chain_AvailableTransformation)

@given(instance=frontend_chain_CompositeTransformation_strategy)
@settings(max_examples=50)
def test_frontend_chain_compositetransformation_instantiation(instance):
    assert isinstance(instance, frontend_chain_CompositeTransformation)

@given(instance=frontend_chain_AvailableTransformation_strategy)
@settings(max_examples=50)
def test_frontend_chain_availabletransformation_instantiation(instance):
    assert isinstance(instance, frontend_chain_AvailableTransformation)

@given(instance=RepresentModel_strategy)
@settings(max_examples=50)
def test_representmodel_instantiation(instance):
    assert isinstance(instance, RepresentModel)

@given(instance=AvailableTransformation_strategy)
@settings(max_examples=50)
def test_availabletransformation_instantiation(instance):
    assert isinstance(instance, AvailableTransformation)

@given(instance=Delegate_strategy)
@settings(max_examples=50)
def test_delegate_instantiation(instance):
    assert isinstance(instance, Delegate)

@given(instance=PReference_strategy)
@settings(max_examples=50)
def test_preference_instantiation(instance):
    assert isinstance(instance, PReference)

@given(instance=frontend_patterns_CollectionReference_strategy)
@settings(max_examples=50)
def test_frontend_patterns_collectionreference_instantiation(instance):
    assert isinstance(instance, frontend_patterns_CollectionReference)

@given(instance=PFeature_strategy)
@settings(max_examples=50)
def test_pfeature_instantiation(instance):
    assert isinstance(instance, PFeature)

@given(instance=frontend_patterns_PReference_strategy)
@settings(max_examples=50)
def test_frontend_patterns_preference_instantiation(instance):
    assert isinstance(instance, frontend_patterns_PReference)

@given(instance=frontend_patterns_PAttribute_strategy)
@settings(max_examples=50)
def test_frontend_patterns_pattribute_instantiation(instance):
    assert isinstance(instance, frontend_patterns_PAttribute)

@given(instance=MethodSelf_strategy)
@settings(max_examples=50)
def test_methodself_instantiation(instance):
    assert isinstance(instance, MethodSelf)

@given(instance=MethodParameter_strategy)
@settings(max_examples=50)
def test_methodparameter_instantiation(instance):
    assert isinstance(instance, MethodParameter)

@given(instance=MethodDefinition_strategy)
@settings(max_examples=50)
def test_methoddefinition_instantiation(instance):
    assert isinstance(instance, MethodDefinition)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=frontend_tao_TemplateParameter_strategy)
@settings(max_examples=50)
def test_frontend_tao_templateparameter_instantiation(instance):
    assert isinstance(instance, frontend_tao_TemplateParameter)

@given(instance=frontend_mappings_MappingVariable_strategy)
@settings(max_examples=50)
def test_frontend_mappings_mappingvariable_instantiation(instance):
    assert isinstance(instance, frontend_mappings_MappingVariable)

@given(instance=frontend_tao_ObjectSourceVariable_strategy)
@settings(max_examples=50)
def test_frontend_tao_objectsourcevariable_instantiation(instance):
    assert isinstance(instance, frontend_tao_ObjectSourceVariable)

@given(instance=frontend_attribution_RuleSelf_strategy)
@settings(max_examples=50)
def test_frontend_attribution_ruleself_instantiation(instance):
    assert isinstance(instance, frontend_attribution_RuleSelf)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=frontend_qool_MatchExpression_strategy)
@settings(max_examples=50)
def test_frontend_qool_matchexpression_instantiation(instance):
    assert isinstance(instance, frontend_qool_MatchExpression)

@given(instance=frontend_attribution_AttributeUse_strategy)
@settings(max_examples=50)
def test_frontend_attribution_attributeuse_instantiation(instance):
    assert isinstance(instance, frontend_attribution_AttributeUse)

@given(instance=frontend_qool_InvokeTransformation_strategy)
@settings(max_examples=50)
def test_frontend_qool_invoketransformation_instantiation(instance):
    assert isinstance(instance, frontend_qool_InvokeTransformation)



@given(instance=frontend_qool_InvokeTransformation_strategy)
def test_frontend_qool_invoketransformation_transformationName_setter(instance):
    original = instance.transformationName
    instance.transformationName = original
    assert instance.transformationName == original



@given(instance=frontend_qool_InvokeTransformation_strategy)
def test_frontend_qool_invoketransformation_entryPointName_setter(instance):
    original = instance.entryPointName
    instance.entryPointName = original
    assert instance.entryPointName == original

@given(instance=frontend_facilities_Copier_strategy)
@settings(max_examples=50)
def test_frontend_facilities_copier_instantiation(instance):
    assert isinstance(instance, frontend_facilities_Copier)

@given(instance=RuleSelf_strategy)
@settings(max_examples=50)
def test_ruleself_instantiation(instance):
    assert isinstance(instance, RuleSelf)

@given(instance=core_RepresentModel_strategy)
@settings(max_examples=50)
def test_core_representmodel_instantiation(instance):
    assert isinstance(instance, core_RepresentModel)

@given(instance=TransformationExecution_strategy)
@settings(max_examples=50)
def test_transformationexecution_instantiation(instance):
    assert isinstance(instance, TransformationExecution)

@given(instance=GeneratedModel_strategy)
@settings(max_examples=50)
def test_generatedmodel_instantiation(instance):
    assert isinstance(instance, GeneratedModel)

@given(instance=ExternalTransformation_strategy)
@settings(max_examples=50)
def test_externaltransformation_instantiation(instance):
    assert isinstance(instance, ExternalTransformation)

@given(instance=CompositeTransformation_strategy)
@settings(max_examples=50)
def test_compositetransformation_instantiation(instance):
    assert isinstance(instance, CompositeTransformation)

@given(instance=frontend_imperative_MethodParameter_strategy)
@settings(max_examples=50)
def test_frontend_imperative_methodparameter_instantiation(instance):
    assert isinstance(instance, frontend_imperative_MethodParameter)

@given(instance=frontend_imperative_MethodSelf_strategy)
@settings(max_examples=50)
def test_frontend_imperative_methodself_instantiation(instance):
    assert isinstance(instance, frontend_imperative_MethodSelf)

@given(instance=Matcher_strategy)
@settings(max_examples=50)
def test_matcher_instantiation(instance):
    assert isinstance(instance, Matcher)

@given(instance=core_NamedElement_strategy)
@settings(max_examples=50)
def test_core_namedelement_instantiation(instance):
    assert isinstance(instance, core_NamedElement)

@given(instance=frontend_chain_GeneratedModel_strategy)
@settings(max_examples=50)
def test_frontend_chain_generatedmodel_instantiation(instance):
    assert isinstance(instance, frontend_chain_GeneratedModel)

@given(instance=frontend_chain_ExternalTransformation_strategy)
@settings(max_examples=50)
def test_frontend_chain_externaltransformation_instantiation(instance):
    assert isinstance(instance, frontend_chain_ExternalTransformation)

@given(instance=core_LocatedElement_strategy)
@settings(max_examples=50)
def test_core_locatedelement_instantiation(instance):
    assert isinstance(instance, core_LocatedElement)

@given(instance=frontend_tao_Template_strategy)
@settings(max_examples=50)
def test_frontend_tao_template_instantiation(instance):
    assert isinstance(instance, frontend_tao_Template)

@given(instance=frontend_qool_QoolQueue_strategy)
@settings(max_examples=50)
def test_frontend_qool_qoolqueue_instantiation(instance):
    assert isinstance(instance, frontend_qool_QoolQueue)

@given(instance=frontend_koan_KoanRule_strategy)
@settings(max_examples=50)
def test_frontend_koan_koanrule_instantiation(instance):
    assert isinstance(instance, frontend_koan_KoanRule)

@given(instance=KoanRule_strategy)
@settings(max_examples=50)
def test_koanrule_instantiation(instance):
    assert isinstance(instance, KoanRule)

@given(instance=TraceInterface_strategy)
@settings(max_examples=50)
def test_traceinterface_instantiation(instance):
    assert isinstance(instance, TraceInterface)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=frontend_tao_Assignment_strategy)
@settings(max_examples=50)
def test_frontend_tao_assignment_instantiation(instance):
    assert isinstance(instance, frontend_tao_Assignment)

@given(instance=frontend_qool_EmitStatement_strategy)
@settings(max_examples=50)
def test_frontend_qool_emitstatement_instantiation(instance):
    assert isinstance(instance, frontend_qool_EmitStatement)

@given(instance=frontend_attribution_AttributeInit_strategy)
@settings(max_examples=50)
def test_frontend_attribution_attributeinit_instantiation(instance):
    assert isinstance(instance, frontend_attribution_AttributeInit)

@given(instance=TransformationDefinition_strategy)
@settings(max_examples=50)
def test_transformationdefinition_instantiation(instance):
    assert isinstance(instance, TransformationDefinition)

@given(instance=frontend_chain_ChainTransformation_strategy)
@settings(max_examples=50)
def test_frontend_chain_chaintransformation_instantiation(instance):
    assert isinstance(instance, frontend_chain_ChainTransformation)

@given(instance=frontend_imperative_ImperativeTransformation_strategy)
@settings(max_examples=50)
def test_frontend_imperative_imperativetransformation_instantiation(instance):
    assert isinstance(instance, frontend_imperative_ImperativeTransformation)

@given(instance=frontend_koan_KoanTransformation_strategy)
@settings(max_examples=50)
def test_frontend_koan_koantransformation_instantiation(instance):
    assert isinstance(instance, frontend_koan_KoanTransformation)

@given(instance=frontend_tao_TaoTransformation_strategy)
@settings(max_examples=50)
def test_frontend_tao_taotransformation_instantiation(instance):
    assert isinstance(instance, frontend_tao_TaoTransformation)

@given(instance=frontend_qool_QoolTransformation_strategy)
@settings(max_examples=50)
def test_frontend_qool_qooltransformation_instantiation(instance):
    assert isinstance(instance, frontend_qool_QoolTransformation)

@given(instance=frontend_patterns_PatternSpecification_strategy)
@settings(max_examples=50)
def test_frontend_patterns_patternspecification_instantiation(instance):
    assert isinstance(instance, frontend_patterns_PatternSpecification)

@given(instance=frontend_mappings_MappingTransformation_strategy)
@settings(max_examples=50)
def test_frontend_mappings_mappingtransformation_instantiation(instance):
    assert isinstance(instance, frontend_mappings_MappingTransformation)

@given(instance=frontend_script_ScriptedTransformation_strategy)
@settings(max_examples=50)
def test_frontend_script_scriptedtransformation_instantiation(instance):
    assert isinstance(instance, frontend_script_ScriptedTransformation)

@given(instance=frontend_DummyRootMetaclass_strategy)
@settings(max_examples=50)
def test_frontend_dummyrootmetaclass_instantiation(instance):
    assert isinstance(instance, frontend_DummyRootMetaclass)

@given(instance=core_TypedWithClass_strategy)
@settings(max_examples=50)
def test_core_typedwithclass_instantiation(instance):
    assert isinstance(instance, core_TypedWithClass)

@given(instance=AttributionRule_strategy)
@settings(max_examples=50)
def test_attributionrule_instantiation(instance):
    assert isinstance(instance, AttributionRule)

@given(instance=AttributeDcl_strategy)
@settings(max_examples=50)
def test_attributedcl_instantiation(instance):
    assert isinstance(instance, AttributeDcl)

@given(instance=frontend_attribution_SynthesizedAttributeDcl_strategy)
@settings(max_examples=50)
def test_frontend_attribution_synthesizedattributedcl_instantiation(instance):
    assert isinstance(instance, frontend_attribution_SynthesizedAttributeDcl)

@given(instance=frontend_attribution_InheritedAttributeDcl_strategy)
@settings(max_examples=50)
def test_frontend_attribution_inheritedattributedcl_instantiation(instance):
    assert isinstance(instance, frontend_attribution_InheritedAttributeDcl)

@given(instance=frontend_attribution_AttributionTransformation_strategy)
@settings(max_examples=50)
def test_frontend_attribution_attributiontransformation_instantiation(instance):
    assert isinstance(instance, frontend_attribution_AttributionTransformation)

@given(instance=ClassUse_strategy)
@settings(max_examples=50)
def test_classuse_instantiation(instance):
    assert isinstance(instance, ClassUse)

@given(instance=core_Variable_strategy)
@settings(max_examples=50)
def test_core_variable_instantiation(instance):
    assert isinstance(instance, core_Variable)

@given(instance=frontend_attribution_AttributeDcl_strategy)
@settings(max_examples=50)
def test_frontend_attribution_attributedcl_instantiation(instance):
    assert isinstance(instance, frontend_attribution_AttributeDcl)

@given(instance=frontend_tao_ObjectInstantiation_strategy)
@settings(max_examples=50)
def test_frontend_tao_objectinstantiation_instantiation(instance):
    assert isinstance(instance, frontend_tao_ObjectInstantiation)

@given(instance=frontend_qool_IteratorStatement_strategy)
@settings(max_examples=50)
def test_frontend_qool_iteratorstatement_instantiation(instance):
    assert isinstance(instance, frontend_qool_IteratorStatement)

@given(instance=frontend_patterns_PObject_strategy)
@settings(max_examples=50)
def test_frontend_patterns_pobject_instantiation(instance):
    assert isinstance(instance, frontend_patterns_PObject)

@given(instance=frontend_tao_ReferenceAssignment_strategy)
@settings(max_examples=50)
def test_frontend_tao_referenceassignment_instantiation(instance):
    assert isinstance(instance, frontend_tao_ReferenceAssignment)



@given(instance=frontend_tao_ReferenceAssignment_strategy)
def test_frontend_tao_referenceassignment_targetFeature_setter(instance):
    original = instance.targetFeature
    instance.targetFeature = original
    assert instance.targetFeature == original



@given(instance=frontend_tao_ReferenceAssignment_strategy)
def test_frontend_tao_referenceassignment_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=koan_Matcher_strategy)
@settings(max_examples=50)
def test_koan_matcher_instantiation(instance):
    assert isinstance(instance, koan_Matcher)

@given(instance=frontend_koan_ForAllMatcher_strategy)
@settings(max_examples=50)
def test_frontend_koan_forallmatcher_instantiation(instance):
    assert isinstance(instance, frontend_koan_ForAllMatcher)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=frontend_chain_TransformationExecution_strategy)
@settings(max_examples=50)
def test_frontend_chain_transformationexecution_instantiation(instance):
    assert isinstance(instance, frontend_chain_TransformationExecution)

@given(instance=frontend_patterns_Pattern_strategy)
@settings(max_examples=50)
def test_frontend_patterns_pattern_instantiation(instance):
    assert isinstance(instance, frontend_patterns_Pattern)



@given(instance=frontend_patterns_Pattern_strategy)
def test_frontend_patterns_pattern_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend_attribution_AttributionRule_strategy)
@settings(max_examples=50)
def test_frontend_attribution_attributionrule_instantiation(instance):
    assert isinstance(instance, frontend_attribution_AttributionRule)

@given(instance=frontend_imperative_MethodDefinition_strategy)
@settings(max_examples=50)
def test_frontend_imperative_methoddefinition_instantiation(instance):
    assert isinstance(instance, frontend_imperative_MethodDefinition)



@given(instance=frontend_imperative_MethodDefinition_strategy)
def test_frontend_imperative_methoddefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend_tao_SourceExpression_strategy)
@settings(max_examples=50)
def test_frontend_tao_sourceexpression_instantiation(instance):
    assert isinstance(instance, frontend_tao_SourceExpression)

@given(instance=frontend_mappings_Section_strategy)
@settings(max_examples=50)
def test_frontend_mappings_section_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Section)



@given(instance=frontend_mappings_Section_strategy)
def test_frontend_mappings_section_sectionType_setter(instance):
    original = instance.sectionType
    instance.sectionType = original
    assert instance.sectionType == original

@given(instance=frontend_mappings_Delegate_strategy)
@settings(max_examples=50)
def test_frontend_mappings_delegate_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Delegate)



@given(instance=frontend_mappings_Delegate_strategy)
def test_frontend_mappings_delegate_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=frontend_mappings_Delegate_strategy)
def test_frontend_mappings_delegate_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original



@given(instance=frontend_mappings_Delegate_strategy)
def test_frontend_mappings_delegate_linkName_setter(instance):
    original = instance.linkName
    instance.linkName = original
    assert instance.linkName == original

@given(instance=frontend_mappings_MappingElement_strategy)
@settings(max_examples=50)
def test_frontend_mappings_mappingelement_instantiation(instance):
    assert isinstance(instance, frontend_mappings_MappingElement)

@given(instance=frontend_patterns_PFeature_strategy)
@settings(max_examples=50)
def test_frontend_patterns_pfeature_instantiation(instance):
    assert isinstance(instance, frontend_patterns_PFeature)



@given(instance=frontend_patterns_PFeature_strategy)
def test_frontend_patterns_pfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend_mappings_Operator_strategy)
@settings(max_examples=50)
def test_frontend_mappings_operator_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Operator)

@given(instance=frontend_mappings_Context_strategy)
@settings(max_examples=50)
def test_frontend_mappings_context_instantiation(instance):
    assert isinstance(instance, frontend_mappings_Context)

@given(instance=frontend_koan_Matcher_strategy)
@settings(max_examples=50)
def test_frontend_koan_matcher_instantiation(instance):
    assert isinstance(instance, frontend_koan_Matcher)

@given(instance=frontend_core_PutTraceParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_puttraceparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_PutTraceParameter)

@given(instance=PutTraceParameter_strategy)
@settings(max_examples=50)
def test_puttraceparameter_instantiation(instance):
    assert isinstance(instance, PutTraceParameter)

@given(instance=frontend_core_PutTrace_strategy)
@settings(max_examples=50)
def test_frontend_core_puttrace_instantiation(instance):
    assert isinstance(instance, frontend_core_PutTrace)

@given(instance=frontend_core_InlineFeature_strategy)
@settings(max_examples=50)
def test_frontend_core_inlinefeature_instantiation(instance):
    assert isinstance(instance, frontend_core_InlineFeature)



@given(instance=frontend_core_InlineFeature_strategy)
def test_frontend_core_inlinefeature_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=InlineFeature_strategy)
@settings(max_examples=50)
def test_inlinefeature_instantiation(instance):
    assert isinstance(instance, InlineFeature)

@given(instance=frontend_core_InlineClass_strategy)
@settings(max_examples=50)
def test_frontend_core_inlineclass_instantiation(instance):
    assert isinstance(instance, frontend_core_InlineClass)

@given(instance=InlineClass_strategy)
@settings(max_examples=50)
def test_inlineclass_instantiation(instance):
    assert isinstance(instance, InlineClass)

@given(instance=core_ModuleDefinition_strategy)
@settings(max_examples=50)
def test_core_moduledefinition_instantiation(instance):
    assert isinstance(instance, core_ModuleDefinition)

@given(instance=frontend_core_InlineModel_strategy)
@settings(max_examples=50)
def test_frontend_core_inlinemodel_instantiation(instance):
    assert isinstance(instance, frontend_core_InlineModel)

@given(instance=frontend_core_TraceElement_strategy)
@settings(max_examples=50)
def test_frontend_core_traceelement_instantiation(instance):
    assert isinstance(instance, frontend_core_TraceElement)

@given(instance=TraceElement_strategy)
@settings(max_examples=50)
def test_traceelement_instantiation(instance):
    assert isinstance(instance, TraceElement)

@given(instance=frontend_core_TraceDefinition_strategy)
@settings(max_examples=50)
def test_frontend_core_tracedefinition_instantiation(instance):
    assert isinstance(instance, frontend_core_TraceDefinition)

@given(instance=frontend_core_TraceInterface_strategy)
@settings(max_examples=50)
def test_frontend_core_traceinterface_instantiation(instance):
    assert isinstance(instance, frontend_core_TraceInterface)

@given(instance=frontend_core_TypedWithClass_strategy)
@settings(max_examples=50)
def test_frontend_core_typedwithclass_instantiation(instance):
    assert isinstance(instance, frontend_core_TypedWithClass)

@given(instance=TraceDefinition_strategy)
@settings(max_examples=50)
def test_tracedefinition_instantiation(instance):
    assert isinstance(instance, TraceDefinition)

@given(instance=frontend_core_TraceUse_strategy)
@settings(max_examples=50)
def test_frontend_core_traceuse_instantiation(instance):
    assert isinstance(instance, frontend_core_TraceUse)

@given(instance=frontend_core_TraceCompareExpression_strategy)
@settings(max_examples=50)
def test_frontend_core_tracecompareexpression_instantiation(instance):
    assert isinstance(instance, frontend_core_TraceCompareExpression)



@given(instance=frontend_core_TraceCompareExpression_strategy)
def test_frontend_core_tracecompareexpression_multivaluedTag_setter(instance):
    original = instance.multivaluedTag
    instance.multivaluedTag = original
    assert instance.multivaluedTag == original

@given(instance=TraceCompareExpression_strategy)
@settings(max_examples=50)
def test_tracecompareexpression_instantiation(instance):
    assert isinstance(instance, TraceCompareExpression)

@given(instance=frontend_core_MatchTrace_strategy)
@settings(max_examples=50)
def test_frontend_core_matchtrace_instantiation(instance):
    assert isinstance(instance, frontend_core_MatchTrace)



@given(instance=frontend_core_MatchTrace_strategy)
def test_frontend_core_matchtrace_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=frontend_core_InlineReference_strategy)
@settings(max_examples=50)
def test_frontend_core_inlinereference_instantiation(instance):
    assert isinstance(instance, frontend_core_InlineReference)

@given(instance=frontend_core_InlineAttribute_strategy)
@settings(max_examples=50)
def test_frontend_core_inlineattribute_instantiation(instance):
    assert isinstance(instance, frontend_core_InlineAttribute)

@given(instance=frontend_core_IfBranch_strategy)
@settings(max_examples=50)
def test_frontend_core_ifbranch_instantiation(instance):
    assert isinstance(instance, frontend_core_IfBranch)

@given(instance=IfBranch_strategy)
@settings(max_examples=50)
def test_ifbranch_instantiation(instance):
    assert isinstance(instance, IfBranch)

@given(instance=frontend_core_IfExpr_strategy)
@settings(max_examples=50)
def test_frontend_core_ifexpr_instantiation(instance):
    assert isinstance(instance, frontend_core_IfExpr)

@given(instance=core_ImplicitlyAnnotableElement_strategy)
@settings(max_examples=50)
def test_core_implicitlyannotableelement_instantiation(instance):
    assert isinstance(instance, core_ImplicitlyAnnotableElement)

@given(instance=core_TypeExpression_strategy)
@settings(max_examples=50)
def test_core_typeexpression_instantiation(instance):
    assert isinstance(instance, core_TypeExpression)

@given(instance=frontend_core_ClassUse_strategy)
@settings(max_examples=50)
def test_frontend_core_classuse_instantiation(instance):
    assert isinstance(instance, frontend_core_ClassUse)



@given(instance=frontend_core_ClassUse_strategy)
def test_frontend_core_classuse_strictType_setter(instance):
    original = instance.strictType
    instance.strictType = original
    assert instance.strictType == original



@given(instance=frontend_core_ClassUse_strategy)
def test_frontend_core_classuse_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=frontend_core_TypeExpression_strategy)
@settings(max_examples=50)
def test_frontend_core_typeexpression_instantiation(instance):
    assert isinstance(instance, frontend_core_TypeExpression)

@given(instance=frontend_core_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_frontend_core_booleanliteral_instantiation(instance):
    assert isinstance(instance, frontend_core_BooleanLiteral)



@given(instance=frontend_core_BooleanLiteral_strategy)
def test_frontend_core_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend_core_StringLiteral_strategy)
@settings(max_examples=50)
def test_frontend_core_stringliteral_instantiation(instance):
    assert isinstance(instance, frontend_core_StringLiteral)



@given(instance=frontend_core_StringLiteral_strategy)
def test_frontend_core_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend_core_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_frontend_core_doubleliteral_instantiation(instance):
    assert isinstance(instance, frontend_core_DoubleLiteral)



@given(instance=frontend_core_DoubleLiteral_strategy)
def test_frontend_core_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend_core_NumLiteral_strategy)
@settings(max_examples=50)
def test_frontend_core_numliteral_instantiation(instance):
    assert isinstance(instance, frontend_core_NumLiteral)



@given(instance=frontend_core_NumLiteral_strategy)
def test_frontend_core_numliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend_core_BinaryExpr_strategy)
@settings(max_examples=50)
def test_frontend_core_binaryexpr_instantiation(instance):
    assert isinstance(instance, frontend_core_BinaryExpr)



@given(instance=frontend_core_BinaryExpr_strategy)
def test_frontend_core_binaryexpr_binaryOp_setter(instance):
    original = instance.binaryOp
    instance.binaryOp = original
    assert instance.binaryOp == original

@given(instance=frontend_core_KeywordParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_keywordparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_KeywordParameter)



@given(instance=frontend_core_KeywordParameter_strategy)
def test_frontend_core_keywordparameter_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=KeywordParameter_strategy)
@settings(max_examples=50)
def test_keywordparameter_instantiation(instance):
    assert isinstance(instance, KeywordParameter)

@given(instance=frontend_core_KeywordMethodCall_strategy)
@settings(max_examples=50)
def test_frontend_core_keywordmethodcall_instantiation(instance):
    assert isinstance(instance, frontend_core_KeywordMethodCall)

@given(instance=frontend_core_MethodCall_strategy)
@settings(max_examples=50)
def test_frontend_core_methodcall_instantiation(instance):
    assert isinstance(instance, frontend_core_MethodCall)



@given(instance=frontend_core_MethodCall_strategy)
def test_frontend_core_methodcall_withParameters_setter(instance):
    original = instance.withParameters
    instance.withParameters = original
    assert instance.withParameters == original



@given(instance=frontend_core_MethodCall_strategy)
def test_frontend_core_methodcall_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=frontend_core_VariableReference_strategy)
@settings(max_examples=50)
def test_frontend_core_variablereference_instantiation(instance):
    assert isinstance(instance, frontend_core_VariableReference)

@given(instance=core_Expression_strategy)
@settings(max_examples=50)
def test_core_expression_instantiation(instance):
    assert isinstance(instance, core_Expression)

@given(instance=frontend_core_ModelReference_strategy)
@settings(max_examples=50)
def test_frontend_core_modelreference_instantiation(instance):
    assert isinstance(instance, frontend_core_ModelReference)

@given(instance=frontend_core_ResolveLink_strategy)
@settings(max_examples=50)
def test_frontend_core_resolvelink_instantiation(instance):
    assert isinstance(instance, frontend_core_ResolveLink)



@given(instance=frontend_core_ResolveLink_strategy)
def test_frontend_core_resolvelink_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original



@given(instance=frontend_core_ResolveLink_strategy)
def test_frontend_core_resolvelink_linkName_setter(instance):
    original = instance.linkName
    instance.linkName = original
    assert instance.linkName == original



@given(instance=frontend_core_ResolveLink_strategy)
def test_frontend_core_resolvelink_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=frontend_core_ClosureParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_closureparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_ClosureParameter)

@given(instance=ClosureParameter_strategy)
@settings(max_examples=50)
def test_closureparameter_instantiation(instance):
    assert isinstance(instance, ClosureParameter)

@given(instance=frontend_core_ClosureDeclaration_strategy)
@settings(max_examples=50)
def test_frontend_core_closuredeclaration_instantiation(instance):
    assert isinstance(instance, frontend_core_ClosureDeclaration)

@given(instance=frontend_core_Variable_strategy)
@settings(max_examples=50)
def test_frontend_core_variable_instantiation(instance):
    assert isinstance(instance, frontend_core_Variable)



@given(instance=frontend_core_Variable_strategy)
def test_frontend_core_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend_core_RequireParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_requireparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_RequireParameter)



@given(instance=frontend_core_RequireParameter_strategy)
def test_frontend_core_requireparameter_formalParameterName_setter(instance):
    original = instance.formalParameterName
    instance.formalParameterName = original
    assert instance.formalParameterName == original

@given(instance=RequireParameter_strategy)
@settings(max_examples=50)
def test_requireparameter_instantiation(instance):
    assert isinstance(instance, RequireParameter)

@given(instance=frontend_core_RequireModelParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_requiremodelparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_RequireModelParameter)

@given(instance=frontend_core_RequireDeclaration_strategy)
@settings(max_examples=50)
def test_frontend_core_requiredeclaration_instantiation(instance):
    assert isinstance(instance, frontend_core_RequireDeclaration)



@given(instance=frontend_core_RequireDeclaration_strategy)
def test_frontend_core_requiredeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=frontend_core_RequireDeclaration_strategy)
def test_frontend_core_requiredeclaration_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=frontend_core_UseDeclaration_strategy)
@settings(max_examples=50)
def test_frontend_core_usedeclaration_instantiation(instance):
    assert isinstance(instance, frontend_core_UseDeclaration)



@given(instance=frontend_core_UseDeclaration_strategy)
def test_frontend_core_usedeclaration_module_setter(instance):
    original = instance.module
    instance.module = original
    assert instance.module == original



@given(instance=frontend_core_UseDeclaration_strategy)
def test_frontend_core_usedeclaration_as__setter(instance):
    original = instance.as_
    instance.as_ = original
    assert instance.as_ == original

@given(instance=frontend_core_ImportedModel_strategy)
@settings(max_examples=50)
def test_frontend_core_importedmodel_instantiation(instance):
    assert isinstance(instance, frontend_core_ImportedModel)

@given(instance=core_DefinitionParameter_strategy)
@settings(max_examples=50)
def test_core_definitionparameter_instantiation(instance):
    assert isinstance(instance, core_DefinitionParameter)

@given(instance=frontend_core_TracedModelParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_tracedmodelparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_TracedModelParameter)

@given(instance=frontend_core_TransformationDefinitionParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_transformationdefinitionparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_TransformationDefinitionParameter)

@given(instance=frontend_core_EclecticTransformationDefinition_strategy)
@settings(max_examples=50)
def test_frontend_core_eclectictransformationdefinition_instantiation(instance):
    assert isinstance(instance, frontend_core_EclecticTransformationDefinition)

@given(instance=RequireDeclaration_strategy)
@settings(max_examples=50)
def test_requiredeclaration_instantiation(instance):
    assert isinstance(instance, RequireDeclaration)

@given(instance=InlineModel_strategy)
@settings(max_examples=50)
def test_inlinemodel_instantiation(instance):
    assert isinstance(instance, InlineModel)

@given(instance=frontend_core_PropertyWrite_strategy)
@settings(max_examples=50)
def test_frontend_core_propertywrite_instantiation(instance):
    assert isinstance(instance, frontend_core_PropertyWrite)



@given(instance=frontend_core_PropertyWrite_strategy)
def test_frontend_core_propertywrite__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original

@given(instance=frontend_core_DefineVariable_strategy)
@settings(max_examples=50)
def test_frontend_core_definevariable_instantiation(instance):
    assert isinstance(instance, frontend_core_DefineVariable)

@given(instance=frontend_core_Expression_strategy)
@settings(max_examples=50)
def test_frontend_core_expression_instantiation(instance):
    assert isinstance(instance, frontend_core_Expression)

@given(instance=frontend_core_Statement_strategy)
@settings(max_examples=50)
def test_frontend_core_statement_instantiation(instance):
    assert isinstance(instance, frontend_core_Statement)

@given(instance=AnnotableElement_strategy)
@settings(max_examples=50)
def test_annotableelement_instantiation(instance):
    assert isinstance(instance, AnnotableElement)

@given(instance=frontend_core_RepresentModel_strategy)
@settings(max_examples=50)
def test_frontend_core_representmodel_instantiation(instance):
    assert isinstance(instance, frontend_core_RepresentModel)

@given(instance=frontend_core_Annotation_strategy)
@settings(max_examples=50)
def test_frontend_core_annotation_instantiation(instance):
    assert isinstance(instance, frontend_core_Annotation)

@given(instance=SingleAnnotation_strategy)
@settings(max_examples=50)
def test_singleannotation_instantiation(instance):
    assert isinstance(instance, SingleAnnotation)

@given(instance=frontend_core_PotencyAnnotation_strategy)
@settings(max_examples=50)
def test_frontend_core_potencyannotation_instantiation(instance):
    assert isinstance(instance, frontend_core_PotencyAnnotation)



@given(instance=frontend_core_PotencyAnnotation_strategy)
def test_frontend_core_potencyannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend_core_ImplicitlyAnnotableElement_strategy)
@settings(max_examples=50)
def test_frontend_core_implicitlyannotableelement_instantiation(instance):
    assert isinstance(instance, frontend_core_ImplicitlyAnnotableElement)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=frontend_core_SingleAnnotation_strategy)
@settings(max_examples=50)
def test_frontend_core_singleannotation_instantiation(instance):
    assert isinstance(instance, frontend_core_SingleAnnotation)

@given(instance=frontend_core_OptimizationsAnnotation_strategy)
@settings(max_examples=50)
def test_frontend_core_optimizationsannotation_instantiation(instance):
    assert isinstance(instance, frontend_core_OptimizationsAnnotation)



@given(instance=frontend_core_OptimizationsAnnotation_strategy)
def test_frontend_core_optimizationsannotation_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=frontend_core_MetamodelModelAnnotation_strategy)
@settings(max_examples=50)
def test_frontend_core_metamodelmodelannotation_instantiation(instance):
    assert isinstance(instance, frontend_core_MetamodelModelAnnotation)



@given(instance=frontend_core_MetamodelModelAnnotation_strategy)
def test_frontend_core_metamodelmodelannotation_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=frontend_core_AnnotableElement_strategy)
@settings(max_examples=50)
def test_frontend_core_annotableelement_instantiation(instance):
    assert isinstance(instance, frontend_core_AnnotableElement)

@given(instance=core_AnnotableElement_strategy)
@settings(max_examples=50)
def test_core_annotableelement_instantiation(instance):
    assert isinstance(instance, core_AnnotableElement)

@given(instance=frontend_core_ModuleDefinition_strategy)
@settings(max_examples=50)
def test_frontend_core_moduledefinition_instantiation(instance):
    assert isinstance(instance, frontend_core_ModuleDefinition)

@given(instance=DefinitionParameter_strategy)
@settings(max_examples=50)
def test_definitionparameter_instantiation(instance):
    assert isinstance(instance, DefinitionParameter)

@given(instance=frontend_core_ModuleParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_moduleparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_ModuleParameter)

@given(instance=frontend_core_DefinitionParameter_strategy)
@settings(max_examples=50)
def test_frontend_core_definitionparameter_instantiation(instance):
    assert isinstance(instance, frontend_core_DefinitionParameter)
