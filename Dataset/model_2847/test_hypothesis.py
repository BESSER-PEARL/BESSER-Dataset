import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    frontend::core::PutTraceParameter,
    PutTraceParameter,
    InlineFeature,
    InlineClass,
    core::ModuleDefinition,
    TraceElement,
    frontend::core::TypedWithClass,
    TraceDefinition,
    frontend::core::TraceCompareExpression,
    TraceCompareExpression,
    frontend::core::InlineReference,
    frontend::core::InlineAttribute,
    frontend::core::IfBranch,
    IfBranch,
    core::ImplicitlyAnnotableElement,
    core::TypeExpression,
    frontend::core::ClassUse,
    frontend::core::TypeExpression,
    frontend::core::KeywordParameter,
    KeywordParameter,
    core::Expression,
    ClosureParameter,
    frontend::core::Variable,
    frontend::core::RequireParameter,
    RequireParameter,
    frontend::core::RequireModelParameter,
    core::DefinitionParameter,
    PFeature,
    MethodSelf,
    MethodParameter,
    MethodDefinition,
    Variable,
    frontend::core::ClosureParameter,
    frontend::attribution::RuleSelf,
    Expression,
    frontend::core::StringLiteral,
    frontend::core::KeywordMethodCall,
    frontend::core::MethodCall,
    frontend::core::IfExpr,
    frontend::core::PutTrace,
    frontend::core::ResolveLink,
    frontend::core::BinaryExpr,
    frontend::core::DoubleLiteral,
    frontend::core::NumLiteral,
    frontend::core::BooleanLiteral,
    frontend::core::VariableReference,
    frontend::core::MatchTrace,
    frontend::core::ClosureDeclaration,
    frontend::attribution::AttributeUse,
    RuleSelf,
    core::RepresentModel,
    frontend::core::InlineModel,
    frontend::core::TracedModelParameter,
    frontend::core::TransformationDefinitionParameter,
    TransformationExecution,
    GeneratedModel,
    ExternalTransformation,
    CompositeTransformation,
    frontend::imperative::MethodParameter,
    frontend::imperative::MethodSelf,
    Matcher,
    core::NamedElement,
    frontend::chain::GeneratedModel,
    frontend::core::ImportedModel,
    core::LocatedElement,
    frontend::koan::KoanRule,
    KoanRule,
    TraceInterface,
    Statement,
    frontend::attribution::AttributeInit,
    TransformationDefinition,
    frontend::core::EclecticTransformationDefinition,
    frontend::chain::ChainTransformation,
    frontend::imperative::ImperativeTransformation,
    frontend::koan::KoanTransformation,
    frontend::script::ScriptedTransformation,
    frontend::DummyRootMetaclass,
    core::TypedWithClass,
    AttributionRule,
    AttributeDcl,
    frontend::attribution::InheritedAttributeDcl,
    frontend::attribution::SynthesizedAttributeDcl,
    frontend::attribution::AttributionTransformation,
    ClassUse,
    core::Variable,
    frontend::attribution::AttributeDcl,
    koan::Matcher,
    frontend::koan::ForAllMatcher,
    LocatedElement,
    frontend::imperative::MethodDefinition,
    frontend::attribution::AttributionRule,
    frontend::patterns::PFeature,
    frontend::koan::Matcher,
    RequireDeclaration,
    InlineModel,
    frontend::core::PropertyWrite,
    frontend::core::Expression,
    frontend::core::Statement,
    AnnotableElement,
    frontend::core::Annotation,
    SingleAnnotation,
    frontend::core::ImplicitlyAnnotableElement,
    Annotation,
    frontend::core::OptimizationsAnnotation,
    frontend::core::MetamodelModelAnnotation,
    frontend::core::AnnotableElement,
    core::AnnotableElement,
    frontend::core::ModuleDefinition,
    DefinitionParameter,
    frontend::core::ModuleParameter,
    frontend::core::NamedElement,
    frontend::core::LocatedElement,
    ImportedModel,
    ModuleDefinition,
    frontend::core::TraceInterface,
    frontend::core::TransformationDefinition,
    frontend::core::RepresentModel,
    frontend::core::AnnotationParameter,
    AnnotationParameter,
    frontend::core::GenericAnnotation,
    frontend::core::PotencyAnnotation,
    frontend::core::SingleAnnotation,
    ObjectSourceVariable,
    frontend::tao::SourceExpression,
    SourceExpression,
    frontend::tao::WithOptionalVariableExpression,
    frontend::tao::Assignment,
    TemplateRootObject,
    TemplateParameter,
    frontend::tao::Template,
    ObjectInstantiation,
    frontend::tao::TemplateRootObject,
    Assignment,
    frontend::tao::AttributeAssigment,
    ReferenceAssignment,
    frontend::tao::Invocation,
    frontend::tao::ObjectSyntax,
    tao::Assignment,
    frontend::tao::ReferenceAssignment,
    frontend::tao::ObjectSourceVariable,
    frontend::facilities::CopierCallbackDefinition,
    facilities::CopierCallbackDefinition,
    frontend::facilities::Copier,
    frontend::tao::TemplateParameter,
    Template,
    frontend::tao::TaoTransformation,
    InvokeTransformation,
    frontend::qool::InvokeExternal,
    NamedInvocationParameter,
    InvocationParameter,
    frontend::qool::InvokeTransformation,
    frontend::qool::NamedInvocationParameter,
    TransformationDefinitionParameter,
    frontend::qool::InvocationParameter,
    frontend::qool::InvokeInternal,
    IteratorStatement,
    frontend::qool::ForEachStatement,
    frontend::qool::ForAllStatement,
    core::Statement,
    frontend::tao::ObjectInstantiation,
    frontend::core::DefineVariable,
    frontend::qool::IteratorStatement,
    TypeExpression,
    frontend::core::TraceUse,
    frontend::qool::QueueOptimization,
    QueueOptimization,
    frontend::qool::AccessByFeatureOptimization,
    frontend::qool::MatchPredicate,
    MatchPredicate,
    frontend::qool::KindOfPredicate,
    frontend::qool::PropertyEqualsPredicate,
    frontend::qool::MatchExpression,
    frontend::qool::EmitStatement,
    mappings::MetamodelElementRef,
    MetamodelElementRef,
    frontend::mappings::AttributeRef,
    frontend::mappings::ClassRef,
    frontend::mappings::MetamodelElementRef,
    DefaultValue,
    frontend::mappings::IntDefaultValue,
    frontend::qool::QoolQueue,
    Segment,
    QoolQueue,
    frontend::qool::ModelElementQueue,
    frontend::qool::LocalQueue,
    frontend::qool::QoolTransformation,
    frontend::mappings::ReferenceRef,
    AttributeModifier,
    frontend::mappings::DefaultValue,
    Class2Class,
    mappings::AttributeRightPart,
    mappings::Feature2Feature,
    frontend::mappings::FeatureRef,
    frontend::mappings::Attribute2Attribute,
    Operator,
    frontend::mappings::Join,
    frontend::mappings::Split,
    frontend::mappings::Operator,
    frontend::mappings::ConvertModifier,
    Modifier,
    frontend::mappings::AttributeModifier,
    frontend::mappings::Modifier,
    ClassRef,
    ReferenceRef,
    ClassMapping,
    frontend::mappings::Class2Class,
    NamedElement,
    frontend::core::InlineFeature,
    frontend::core::TraceElement,
    frontend::core::DefinitionParameter,
    frontend::core::TraceDefinition,
    frontend::core::InlineClass,
    frontend::qool::Segment,
    frontend::mappings::Tag,
    frontend::mappings::Converter,
    ResolveLink,
    Attribute2Attribute,
    Section,
    C2CModifier,
    frontend::mappings::RelatedBy,
    frontend::mappings::LinkedBy,
    frontend::mappings::EqualityFilter,
    MappingElement,
    frontend::mappings::C2CModifier,
    frontend::mappings::Context,
    Tag,
    UseDeclaration,
    MatchedElement,
    frontend::mappings::Delegate,
    mappings::MappingVariable,
    core::ClassUse,
    frontend::core::ModelReference,
    frontend::mappings::MatchedElement,
    frontend::mappings::MappingVariable,
    Context,
    frontend::mappings::AttributeRightPart,
    AttributeRightPart,
    frontend::mappings::AttributeIsResolveLink,
    frontend::mappings::AttributeIsString,
    frontend::mappings::AttributeIsInteger,
    frontend::mappings::AttributeIsDouble,
    frontend::mappings::AttributeIsBoolean,
    AttributeRef,
    Feature2Feature,
    frontend::mappings::Reference2Reference,
    frontend::mappings::AttributeMapping,
    Converter,
    FeatureRef,
    frontend::mappings::Feature2Feature,
    frontend::mappings::ClassMapping,
    frontend::mappings::MappingElement,
    frontend::mappings::Section,
    frontend::patterns::PObject,
    frontend::patterns::POutputVariable,
    POutputVariable,
    PObject,
    frontend::patterns::Pattern,
    Pattern,
    frontend::patterns::PatternSpecification,
    core::TransformationDefinition,
    chain::AvailableTransformation,
    frontend::chain::CompositeTransformation,
    frontend::chain::ExternalTransformation,
    frontend::chain::AvailableTransformation,
    RepresentModel,
    frontend::core::UseDeclaration,
    frontend::core::RequireDeclaration,
    AvailableTransformation,
    frontend::chain::TransformationExecution,
    Delegate,
    frontend::mappings::MappingTransformation,
    PReference,
    frontend::patterns::CollectionReference,
    frontend::patterns::PReference,
    frontend::patterns::PAttribute,
    ResolveTraceCardinality,
    MappingCardinality,
    BinaryOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_frontend::core::puttraceparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::PutTraceParameter)


def test_frontend::core::puttraceparameter_constructor_exists():
    assert callable(frontend::core::PutTraceParameter.__init__)


def test_frontend::core::puttraceparameter_constructor_args():
    sig = inspect.signature(frontend::core::PutTraceParameter.__init__)
    params = list(sig.parameters.keys())



def test_puttraceparameter_is_not_abstract():
    assert not inspect.isabstract(PutTraceParameter)


def test_puttraceparameter_constructor_exists():
    assert callable(PutTraceParameter.__init__)


def test_puttraceparameter_constructor_args():
    sig = inspect.signature(PutTraceParameter.__init__)
    params = list(sig.parameters.keys())



def test_inlinefeature_is_not_abstract():
    assert not inspect.isabstract(InlineFeature)


def test_inlinefeature_constructor_exists():
    assert callable(InlineFeature.__init__)


def test_inlinefeature_constructor_args():
    sig = inspect.signature(InlineFeature.__init__)
    params = list(sig.parameters.keys())



def test_inlineclass_is_not_abstract():
    assert not inspect.isabstract(InlineClass)


def test_inlineclass_constructor_exists():
    assert callable(InlineClass.__init__)


def test_inlineclass_constructor_args():
    sig = inspect.signature(InlineClass.__init__)
    params = list(sig.parameters.keys())



def test_core::moduledefinition_is_not_abstract():
    assert not inspect.isabstract(core::ModuleDefinition)


def test_core::moduledefinition_constructor_exists():
    assert callable(core::ModuleDefinition.__init__)


def test_core::moduledefinition_constructor_args():
    sig = inspect.signature(core::ModuleDefinition.__init__)
    params = list(sig.parameters.keys())



def test_traceelement_is_not_abstract():
    assert not inspect.isabstract(TraceElement)


def test_traceelement_constructor_exists():
    assert callable(TraceElement.__init__)


def test_traceelement_constructor_args():
    sig = inspect.signature(TraceElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::typedwithclass_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TypedWithClass)


def test_frontend::core::typedwithclass_constructor_exists():
    assert callable(frontend::core::TypedWithClass.__init__)


def test_frontend::core::typedwithclass_constructor_args():
    sig = inspect.signature(frontend::core::TypedWithClass.__init__)
    params = list(sig.parameters.keys())



def test_tracedefinition_is_not_abstract():
    assert not inspect.isabstract(TraceDefinition)


def test_tracedefinition_constructor_exists():
    assert callable(TraceDefinition.__init__)


def test_tracedefinition_constructor_args():
    sig = inspect.signature(TraceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::tracecompareexpression_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TraceCompareExpression)


def test_frontend::core::tracecompareexpression_constructor_exists():
    assert callable(frontend::core::TraceCompareExpression.__init__)


def test_frontend::core::tracecompareexpression_constructor_args():
    sig = inspect.signature(frontend::core::TraceCompareExpression.__init__)
    params = list(sig.parameters.keys())
    assert "multivaluedTag" in params, "Missing parameter 'multivaluedTag'"

def test_frontend::core::tracecompareexpression_has_multivaluedTag():
    assert hasattr(frontend::core::TraceCompareExpression, "multivaluedTag")
    descriptor = None
    for klass in frontend::core::TraceCompareExpression.__mro__:
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



def test_frontend::core::inlinereference_is_not_abstract():
    assert not inspect.isabstract(frontend::core::InlineReference)


def test_frontend::core::inlinereference_constructor_exists():
    assert callable(frontend::core::InlineReference.__init__)


def test_frontend::core::inlinereference_constructor_args():
    sig = inspect.signature(frontend::core::InlineReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::inlineattribute_is_not_abstract():
    assert not inspect.isabstract(frontend::core::InlineAttribute)


def test_frontend::core::inlineattribute_constructor_exists():
    assert callable(frontend::core::InlineAttribute.__init__)


def test_frontend::core::inlineattribute_constructor_args():
    sig = inspect.signature(frontend::core::InlineAttribute.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::ifbranch_is_not_abstract():
    assert not inspect.isabstract(frontend::core::IfBranch)


def test_frontend::core::ifbranch_constructor_exists():
    assert callable(frontend::core::IfBranch.__init__)


def test_frontend::core::ifbranch_constructor_args():
    sig = inspect.signature(frontend::core::IfBranch.__init__)
    params = list(sig.parameters.keys())



def test_ifbranch_is_not_abstract():
    assert not inspect.isabstract(IfBranch)


def test_ifbranch_constructor_exists():
    assert callable(IfBranch.__init__)


def test_ifbranch_constructor_args():
    sig = inspect.signature(IfBranch.__init__)
    params = list(sig.parameters.keys())



def test_core::implicitlyannotableelement_is_not_abstract():
    assert not inspect.isabstract(core::ImplicitlyAnnotableElement)


def test_core::implicitlyannotableelement_constructor_exists():
    assert callable(core::ImplicitlyAnnotableElement.__init__)


def test_core::implicitlyannotableelement_constructor_args():
    sig = inspect.signature(core::ImplicitlyAnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_core::typeexpression_is_not_abstract():
    assert not inspect.isabstract(core::TypeExpression)


def test_core::typeexpression_constructor_exists():
    assert callable(core::TypeExpression.__init__)


def test_core::typeexpression_constructor_args():
    sig = inspect.signature(core::TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::classuse_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ClassUse)


def test_frontend::core::classuse_constructor_exists():
    assert callable(frontend::core::ClassUse.__init__)


def test_frontend::core::classuse_constructor_args():
    sig = inspect.signature(frontend::core::ClassUse.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "strictType" in params, "Missing parameter 'strictType'"

def test_frontend::core::classuse_has_className():
    assert hasattr(frontend::core::ClassUse, "className")
    descriptor = None
    for klass in frontend::core::ClassUse.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::classuse_has_strictType():
    assert hasattr(frontend::core::ClassUse, "strictType")
    descriptor = None
    for klass in frontend::core::ClassUse.__mro__:
        if "strictType" in klass.__dict__:
            descriptor = klass.__dict__["strictType"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::typeexpression_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TypeExpression)


def test_frontend::core::typeexpression_constructor_exists():
    assert callable(frontend::core::TypeExpression.__init__)


def test_frontend::core::typeexpression_constructor_args():
    sig = inspect.signature(frontend::core::TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::keywordparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::KeywordParameter)


def test_frontend::core::keywordparameter_constructor_exists():
    assert callable(frontend::core::KeywordParameter.__init__)


def test_frontend::core::keywordparameter_constructor_args():
    sig = inspect.signature(frontend::core::KeywordParameter.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_frontend::core::keywordparameter_has_keyword():
    assert hasattr(frontend::core::KeywordParameter, "keyword")
    descriptor = None
    for klass in frontend::core::KeywordParameter.__mro__:
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



def test_core::expression_is_not_abstract():
    assert not inspect.isabstract(core::Expression)


def test_core::expression_constructor_exists():
    assert callable(core::Expression.__init__)


def test_core::expression_constructor_args():
    sig = inspect.signature(core::Expression.__init__)
    params = list(sig.parameters.keys())



def test_closureparameter_is_not_abstract():
    assert not inspect.isabstract(ClosureParameter)


def test_closureparameter_constructor_exists():
    assert callable(ClosureParameter.__init__)


def test_closureparameter_constructor_args():
    sig = inspect.signature(ClosureParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::variable_is_not_abstract():
    assert not inspect.isabstract(frontend::core::Variable)


def test_frontend::core::variable_constructor_exists():
    assert callable(frontend::core::Variable.__init__)


def test_frontend::core::variable_constructor_args():
    sig = inspect.signature(frontend::core::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend::core::variable_has_name():
    assert hasattr(frontend::core::Variable, "name")
    descriptor = None
    for klass in frontend::core::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::requireparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::RequireParameter)


def test_frontend::core::requireparameter_constructor_exists():
    assert callable(frontend::core::RequireParameter.__init__)


def test_frontend::core::requireparameter_constructor_args():
    sig = inspect.signature(frontend::core::RequireParameter.__init__)
    params = list(sig.parameters.keys())
    assert "formalParameterName" in params, "Missing parameter 'formalParameterName'"

def test_frontend::core::requireparameter_has_formalParameterName():
    assert hasattr(frontend::core::RequireParameter, "formalParameterName")
    descriptor = None
    for klass in frontend::core::RequireParameter.__mro__:
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



def test_frontend::core::requiremodelparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::RequireModelParameter)


def test_frontend::core::requiremodelparameter_constructor_exists():
    assert callable(frontend::core::RequireModelParameter.__init__)


def test_frontend::core::requiremodelparameter_constructor_args():
    sig = inspect.signature(frontend::core::RequireModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_core::definitionparameter_is_not_abstract():
    assert not inspect.isabstract(core::DefinitionParameter)


def test_core::definitionparameter_constructor_exists():
    assert callable(core::DefinitionParameter.__init__)


def test_core::definitionparameter_constructor_args():
    sig = inspect.signature(core::DefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_pfeature_is_not_abstract():
    assert not inspect.isabstract(PFeature)


def test_pfeature_constructor_exists():
    assert callable(PFeature.__init__)


def test_pfeature_constructor_args():
    sig = inspect.signature(PFeature.__init__)
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



def test_frontend::core::closureparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ClosureParameter)


def test_frontend::core::closureparameter_constructor_exists():
    assert callable(frontend::core::ClosureParameter.__init__)


def test_frontend::core::closureparameter_constructor_args():
    sig = inspect.signature(frontend::core::ClosureParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::attribution::ruleself_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::RuleSelf)


def test_frontend::attribution::ruleself_constructor_exists():
    assert callable(frontend::attribution::RuleSelf.__init__)


def test_frontend::attribution::ruleself_constructor_args():
    sig = inspect.signature(frontend::attribution::RuleSelf.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::stringliteral_is_not_abstract():
    assert not inspect.isabstract(frontend::core::StringLiteral)


def test_frontend::core::stringliteral_constructor_exists():
    assert callable(frontend::core::StringLiteral.__init__)


def test_frontend::core::stringliteral_constructor_args():
    sig = inspect.signature(frontend::core::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend::core::stringliteral_has_value():
    assert hasattr(frontend::core::StringLiteral, "value")
    descriptor = None
    for klass in frontend::core::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::keywordmethodcall_is_not_abstract():
    assert not inspect.isabstract(frontend::core::KeywordMethodCall)


def test_frontend::core::keywordmethodcall_constructor_exists():
    assert callable(frontend::core::KeywordMethodCall.__init__)


def test_frontend::core::keywordmethodcall_constructor_args():
    sig = inspect.signature(frontend::core::KeywordMethodCall.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::methodcall_is_not_abstract():
    assert not inspect.isabstract(frontend::core::MethodCall)


def test_frontend::core::methodcall_constructor_exists():
    assert callable(frontend::core::MethodCall.__init__)


def test_frontend::core::methodcall_constructor_args():
    sig = inspect.signature(frontend::core::MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "withParameters" in params, "Missing parameter 'withParameters'"
    assert "methodName" in params, "Missing parameter 'methodName'"

def test_frontend::core::methodcall_has_withParameters():
    assert hasattr(frontend::core::MethodCall, "withParameters")
    descriptor = None
    for klass in frontend::core::MethodCall.__mro__:
        if "withParameters" in klass.__dict__:
            descriptor = klass.__dict__["withParameters"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::methodcall_has_methodName():
    assert hasattr(frontend::core::MethodCall, "methodName")
    descriptor = None
    for klass in frontend::core::MethodCall.__mro__:
        if "methodName" in klass.__dict__:
            descriptor = klass.__dict__["methodName"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::ifexpr_is_not_abstract():
    assert not inspect.isabstract(frontend::core::IfExpr)


def test_frontend::core::ifexpr_constructor_exists():
    assert callable(frontend::core::IfExpr.__init__)


def test_frontend::core::ifexpr_constructor_args():
    sig = inspect.signature(frontend::core::IfExpr.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::puttrace_is_not_abstract():
    assert not inspect.isabstract(frontend::core::PutTrace)


def test_frontend::core::puttrace_constructor_exists():
    assert callable(frontend::core::PutTrace.__init__)


def test_frontend::core::puttrace_constructor_args():
    sig = inspect.signature(frontend::core::PutTrace.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::resolvelink_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ResolveLink)


def test_frontend::core::resolvelink_constructor_exists():
    assert callable(frontend::core::ResolveLink.__init__)


def test_frontend::core::resolvelink_constructor_args():
    sig = inspect.signature(frontend::core::ResolveLink.__init__)
    params = list(sig.parameters.keys())
    assert "linkName" in params, "Missing parameter 'linkName'"
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_frontend::core::resolvelink_has_linkName():
    assert hasattr(frontend::core::ResolveLink, "linkName")
    descriptor = None
    for klass in frontend::core::ResolveLink.__mro__:
        if "linkName" in klass.__dict__:
            descriptor = klass.__dict__["linkName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::resolvelink_has_featureName():
    assert hasattr(frontend::core::ResolveLink, "featureName")
    descriptor = None
    for klass in frontend::core::ResolveLink.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::resolvelink_has_isExternal():
    assert hasattr(frontend::core::ResolveLink, "isExternal")
    descriptor = None
    for klass in frontend::core::ResolveLink.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::binaryexpr_is_not_abstract():
    assert not inspect.isabstract(frontend::core::BinaryExpr)


def test_frontend::core::binaryexpr_constructor_exists():
    assert callable(frontend::core::BinaryExpr.__init__)


def test_frontend::core::binaryexpr_constructor_args():
    sig = inspect.signature(frontend::core::BinaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "binaryOp" in params, "Missing parameter 'binaryOp'"

def test_frontend::core::binaryexpr_has_binaryOp():
    assert hasattr(frontend::core::BinaryExpr, "binaryOp")
    descriptor = None
    for klass in frontend::core::BinaryExpr.__mro__:
        if "binaryOp" in klass.__dict__:
            descriptor = klass.__dict__["binaryOp"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(frontend::core::DoubleLiteral)


def test_frontend::core::doubleliteral_constructor_exists():
    assert callable(frontend::core::DoubleLiteral.__init__)


def test_frontend::core::doubleliteral_constructor_args():
    sig = inspect.signature(frontend::core::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend::core::doubleliteral_has_value():
    assert hasattr(frontend::core::DoubleLiteral, "value")
    descriptor = None
    for klass in frontend::core::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::numliteral_is_not_abstract():
    assert not inspect.isabstract(frontend::core::NumLiteral)


def test_frontend::core::numliteral_constructor_exists():
    assert callable(frontend::core::NumLiteral.__init__)


def test_frontend::core::numliteral_constructor_args():
    sig = inspect.signature(frontend::core::NumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend::core::numliteral_has_value():
    assert hasattr(frontend::core::NumLiteral, "value")
    descriptor = None
    for klass in frontend::core::NumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(frontend::core::BooleanLiteral)


def test_frontend::core::booleanliteral_constructor_exists():
    assert callable(frontend::core::BooleanLiteral.__init__)


def test_frontend::core::booleanliteral_constructor_args():
    sig = inspect.signature(frontend::core::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend::core::booleanliteral_has_value():
    assert hasattr(frontend::core::BooleanLiteral, "value")
    descriptor = None
    for klass in frontend::core::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::variablereference_is_not_abstract():
    assert not inspect.isabstract(frontend::core::VariableReference)


def test_frontend::core::variablereference_constructor_exists():
    assert callable(frontend::core::VariableReference.__init__)


def test_frontend::core::variablereference_constructor_args():
    sig = inspect.signature(frontend::core::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::matchtrace_is_not_abstract():
    assert not inspect.isabstract(frontend::core::MatchTrace)


def test_frontend::core::matchtrace_constructor_exists():
    assert callable(frontend::core::MatchTrace.__init__)


def test_frontend::core::matchtrace_constructor_args():
    sig = inspect.signature(frontend::core::MatchTrace.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_frontend::core::matchtrace_has_cardinality():
    assert hasattr(frontend::core::MatchTrace, "cardinality")
    descriptor = None
    for klass in frontend::core::MatchTrace.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::closuredeclaration_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ClosureDeclaration)


def test_frontend::core::closuredeclaration_constructor_exists():
    assert callable(frontend::core::ClosureDeclaration.__init__)


def test_frontend::core::closuredeclaration_constructor_args():
    sig = inspect.signature(frontend::core::ClosureDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_frontend::attribution::attributeuse_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::AttributeUse)


def test_frontend::attribution::attributeuse_constructor_exists():
    assert callable(frontend::attribution::AttributeUse.__init__)


def test_frontend::attribution::attributeuse_constructor_args():
    sig = inspect.signature(frontend::attribution::AttributeUse.__init__)
    params = list(sig.parameters.keys())



def test_ruleself_is_not_abstract():
    assert not inspect.isabstract(RuleSelf)


def test_ruleself_constructor_exists():
    assert callable(RuleSelf.__init__)


def test_ruleself_constructor_args():
    sig = inspect.signature(RuleSelf.__init__)
    params = list(sig.parameters.keys())



def test_core::representmodel_is_not_abstract():
    assert not inspect.isabstract(core::RepresentModel)


def test_core::representmodel_constructor_exists():
    assert callable(core::RepresentModel.__init__)


def test_core::representmodel_constructor_args():
    sig = inspect.signature(core::RepresentModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::inlinemodel_is_not_abstract():
    assert not inspect.isabstract(frontend::core::InlineModel)


def test_frontend::core::inlinemodel_constructor_exists():
    assert callable(frontend::core::InlineModel.__init__)


def test_frontend::core::inlinemodel_constructor_args():
    sig = inspect.signature(frontend::core::InlineModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::tracedmodelparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TracedModelParameter)


def test_frontend::core::tracedmodelparameter_constructor_exists():
    assert callable(frontend::core::TracedModelParameter.__init__)


def test_frontend::core::tracedmodelparameter_constructor_args():
    sig = inspect.signature(frontend::core::TracedModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::transformationdefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TransformationDefinitionParameter)


def test_frontend::core::transformationdefinitionparameter_constructor_exists():
    assert callable(frontend::core::TransformationDefinitionParameter.__init__)


def test_frontend::core::transformationdefinitionparameter_constructor_args():
    sig = inspect.signature(frontend::core::TransformationDefinitionParameter.__init__)
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



def test_frontend::imperative::methodparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::imperative::MethodParameter)


def test_frontend::imperative::methodparameter_constructor_exists():
    assert callable(frontend::imperative::MethodParameter.__init__)


def test_frontend::imperative::methodparameter_constructor_args():
    sig = inspect.signature(frontend::imperative::MethodParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::imperative::methodself_is_not_abstract():
    assert not inspect.isabstract(frontend::imperative::MethodSelf)


def test_frontend::imperative::methodself_constructor_exists():
    assert callable(frontend::imperative::MethodSelf.__init__)


def test_frontend::imperative::methodself_constructor_args():
    sig = inspect.signature(frontend::imperative::MethodSelf.__init__)
    params = list(sig.parameters.keys())



def test_matcher_is_not_abstract():
    assert not inspect.isabstract(Matcher)


def test_matcher_constructor_exists():
    assert callable(Matcher.__init__)


def test_matcher_constructor_args():
    sig = inspect.signature(Matcher.__init__)
    params = list(sig.parameters.keys())



def test_core::namedelement_is_not_abstract():
    assert not inspect.isabstract(core::NamedElement)


def test_core::namedelement_constructor_exists():
    assert callable(core::NamedElement.__init__)


def test_core::namedelement_constructor_args():
    sig = inspect.signature(core::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::chain::generatedmodel_is_not_abstract():
    assert not inspect.isabstract(frontend::chain::GeneratedModel)


def test_frontend::chain::generatedmodel_constructor_exists():
    assert callable(frontend::chain::GeneratedModel.__init__)


def test_frontend::chain::generatedmodel_constructor_args():
    sig = inspect.signature(frontend::chain::GeneratedModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::importedmodel_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ImportedModel)


def test_frontend::core::importedmodel_constructor_exists():
    assert callable(frontend::core::ImportedModel.__init__)


def test_frontend::core::importedmodel_constructor_args():
    sig = inspect.signature(frontend::core::ImportedModel.__init__)
    params = list(sig.parameters.keys())



def test_core::locatedelement_is_not_abstract():
    assert not inspect.isabstract(core::LocatedElement)


def test_core::locatedelement_constructor_exists():
    assert callable(core::LocatedElement.__init__)


def test_core::locatedelement_constructor_args():
    sig = inspect.signature(core::LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::koan::koanrule_is_not_abstract():
    assert not inspect.isabstract(frontend::koan::KoanRule)


def test_frontend::koan::koanrule_constructor_exists():
    assert callable(frontend::koan::KoanRule.__init__)


def test_frontend::koan::koanrule_constructor_args():
    sig = inspect.signature(frontend::koan::KoanRule.__init__)
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



def test_frontend::attribution::attributeinit_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::AttributeInit)


def test_frontend::attribution::attributeinit_constructor_exists():
    assert callable(frontend::attribution::AttributeInit.__init__)


def test_frontend::attribution::attributeinit_constructor_args():
    sig = inspect.signature(frontend::attribution::AttributeInit.__init__)
    params = list(sig.parameters.keys())



def test_transformationdefinition_is_not_abstract():
    assert not inspect.isabstract(TransformationDefinition)


def test_transformationdefinition_constructor_exists():
    assert callable(TransformationDefinition.__init__)


def test_transformationdefinition_constructor_args():
    sig = inspect.signature(TransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::eclectictransformationdefinition_is_not_abstract():
    assert not inspect.isabstract(frontend::core::EclecticTransformationDefinition)


def test_frontend::core::eclectictransformationdefinition_constructor_exists():
    assert callable(frontend::core::EclecticTransformationDefinition.__init__)


def test_frontend::core::eclectictransformationdefinition_constructor_args():
    sig = inspect.signature(frontend::core::EclecticTransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend::chain::chaintransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::chain::ChainTransformation)


def test_frontend::chain::chaintransformation_constructor_exists():
    assert callable(frontend::chain::ChainTransformation.__init__)


def test_frontend::chain::chaintransformation_constructor_args():
    sig = inspect.signature(frontend::chain::ChainTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::imperative::imperativetransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::imperative::ImperativeTransformation)


def test_frontend::imperative::imperativetransformation_constructor_exists():
    assert callable(frontend::imperative::ImperativeTransformation.__init__)


def test_frontend::imperative::imperativetransformation_constructor_args():
    sig = inspect.signature(frontend::imperative::ImperativeTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::koan::koantransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::koan::KoanTransformation)


def test_frontend::koan::koantransformation_constructor_exists():
    assert callable(frontend::koan::KoanTransformation.__init__)


def test_frontend::koan::koantransformation_constructor_args():
    sig = inspect.signature(frontend::koan::KoanTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::script::scriptedtransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::script::ScriptedTransformation)


def test_frontend::script::scriptedtransformation_constructor_exists():
    assert callable(frontend::script::ScriptedTransformation.__init__)


def test_frontend::script::scriptedtransformation_constructor_args():
    sig = inspect.signature(frontend::script::ScriptedTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::dummyrootmetaclass_is_not_abstract():
    assert not inspect.isabstract(frontend::DummyRootMetaclass)


def test_frontend::dummyrootmetaclass_constructor_exists():
    assert callable(frontend::DummyRootMetaclass.__init__)


def test_frontend::dummyrootmetaclass_constructor_args():
    sig = inspect.signature(frontend::DummyRootMetaclass.__init__)
    params = list(sig.parameters.keys())



def test_core::typedwithclass_is_not_abstract():
    assert not inspect.isabstract(core::TypedWithClass)


def test_core::typedwithclass_constructor_exists():
    assert callable(core::TypedWithClass.__init__)


def test_core::typedwithclass_constructor_args():
    sig = inspect.signature(core::TypedWithClass.__init__)
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



def test_frontend::attribution::inheritedattributedcl_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::InheritedAttributeDcl)


def test_frontend::attribution::inheritedattributedcl_constructor_exists():
    assert callable(frontend::attribution::InheritedAttributeDcl.__init__)


def test_frontend::attribution::inheritedattributedcl_constructor_args():
    sig = inspect.signature(frontend::attribution::InheritedAttributeDcl.__init__)
    params = list(sig.parameters.keys())



def test_frontend::attribution::synthesizedattributedcl_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::SynthesizedAttributeDcl)


def test_frontend::attribution::synthesizedattributedcl_constructor_exists():
    assert callable(frontend::attribution::SynthesizedAttributeDcl.__init__)


def test_frontend::attribution::synthesizedattributedcl_constructor_args():
    sig = inspect.signature(frontend::attribution::SynthesizedAttributeDcl.__init__)
    params = list(sig.parameters.keys())



def test_frontend::attribution::attributiontransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::AttributionTransformation)


def test_frontend::attribution::attributiontransformation_constructor_exists():
    assert callable(frontend::attribution::AttributionTransformation.__init__)


def test_frontend::attribution::attributiontransformation_constructor_args():
    sig = inspect.signature(frontend::attribution::AttributionTransformation.__init__)
    params = list(sig.parameters.keys())



def test_classuse_is_not_abstract():
    assert not inspect.isabstract(ClassUse)


def test_classuse_constructor_exists():
    assert callable(ClassUse.__init__)


def test_classuse_constructor_args():
    sig = inspect.signature(ClassUse.__init__)
    params = list(sig.parameters.keys())



def test_core::variable_is_not_abstract():
    assert not inspect.isabstract(core::Variable)


def test_core::variable_constructor_exists():
    assert callable(core::Variable.__init__)


def test_core::variable_constructor_args():
    sig = inspect.signature(core::Variable.__init__)
    params = list(sig.parameters.keys())



def test_frontend::attribution::attributedcl_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::AttributeDcl)


def test_frontend::attribution::attributedcl_constructor_exists():
    assert callable(frontend::attribution::AttributeDcl.__init__)


def test_frontend::attribution::attributedcl_constructor_args():
    sig = inspect.signature(frontend::attribution::AttributeDcl.__init__)
    params = list(sig.parameters.keys())



def test_koan::matcher_is_not_abstract():
    assert not inspect.isabstract(koan::Matcher)


def test_koan::matcher_constructor_exists():
    assert callable(koan::Matcher.__init__)


def test_koan::matcher_constructor_args():
    sig = inspect.signature(koan::Matcher.__init__)
    params = list(sig.parameters.keys())



def test_frontend::koan::forallmatcher_is_not_abstract():
    assert not inspect.isabstract(frontend::koan::ForAllMatcher)


def test_frontend::koan::forallmatcher_constructor_exists():
    assert callable(frontend::koan::ForAllMatcher.__init__)


def test_frontend::koan::forallmatcher_constructor_args():
    sig = inspect.signature(frontend::koan::ForAllMatcher.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::imperative::methoddefinition_is_not_abstract():
    assert not inspect.isabstract(frontend::imperative::MethodDefinition)


def test_frontend::imperative::methoddefinition_constructor_exists():
    assert callable(frontend::imperative::MethodDefinition.__init__)


def test_frontend::imperative::methoddefinition_constructor_args():
    sig = inspect.signature(frontend::imperative::MethodDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend::imperative::methoddefinition_has_name():
    assert hasattr(frontend::imperative::MethodDefinition, "name")
    descriptor = None
    for klass in frontend::imperative::MethodDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend::attribution::attributionrule_is_not_abstract():
    assert not inspect.isabstract(frontend::attribution::AttributionRule)


def test_frontend::attribution::attributionrule_constructor_exists():
    assert callable(frontend::attribution::AttributionRule.__init__)


def test_frontend::attribution::attributionrule_constructor_args():
    sig = inspect.signature(frontend::attribution::AttributionRule.__init__)
    params = list(sig.parameters.keys())



def test_frontend::patterns::pfeature_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::PFeature)


def test_frontend::patterns::pfeature_constructor_exists():
    assert callable(frontend::patterns::PFeature.__init__)


def test_frontend::patterns::pfeature_constructor_args():
    sig = inspect.signature(frontend::patterns::PFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend::patterns::pfeature_has_name():
    assert hasattr(frontend::patterns::PFeature, "name")
    descriptor = None
    for klass in frontend::patterns::PFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend::koan::matcher_is_not_abstract():
    assert not inspect.isabstract(frontend::koan::Matcher)


def test_frontend::koan::matcher_constructor_exists():
    assert callable(frontend::koan::Matcher.__init__)


def test_frontend::koan::matcher_constructor_args():
    sig = inspect.signature(frontend::koan::Matcher.__init__)
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



def test_frontend::core::propertywrite_is_not_abstract():
    assert not inspect.isabstract(frontend::core::PropertyWrite)


def test_frontend::core::propertywrite_constructor_exists():
    assert callable(frontend::core::PropertyWrite.__init__)


def test_frontend::core::propertywrite_constructor_args():
    sig = inspect.signature(frontend::core::PropertyWrite.__init__)
    params = list(sig.parameters.keys())
    assert "_property" in params, "Missing parameter '_property'"

def test_frontend::core::propertywrite_has__property():
    assert hasattr(frontend::core::PropertyWrite, "_property")
    descriptor = None
    for klass in frontend::core::PropertyWrite.__mro__:
        if "_property" in klass.__dict__:
            descriptor = klass.__dict__["_property"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::expression_is_not_abstract():
    assert not inspect.isabstract(frontend::core::Expression)


def test_frontend::core::expression_constructor_exists():
    assert callable(frontend::core::Expression.__init__)


def test_frontend::core::expression_constructor_args():
    sig = inspect.signature(frontend::core::Expression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::statement_is_not_abstract():
    assert not inspect.isabstract(frontend::core::Statement)


def test_frontend::core::statement_constructor_exists():
    assert callable(frontend::core::Statement.__init__)


def test_frontend::core::statement_constructor_args():
    sig = inspect.signature(frontend::core::Statement.__init__)
    params = list(sig.parameters.keys())



def test_annotableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotableElement)


def test_annotableelement_constructor_exists():
    assert callable(AnnotableElement.__init__)


def test_annotableelement_constructor_args():
    sig = inspect.signature(AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::annotation_is_not_abstract():
    assert not inspect.isabstract(frontend::core::Annotation)


def test_frontend::core::annotation_constructor_exists():
    assert callable(frontend::core::Annotation.__init__)


def test_frontend::core::annotation_constructor_args():
    sig = inspect.signature(frontend::core::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_singleannotation_is_not_abstract():
    assert not inspect.isabstract(SingleAnnotation)


def test_singleannotation_constructor_exists():
    assert callable(SingleAnnotation.__init__)


def test_singleannotation_constructor_args():
    sig = inspect.signature(SingleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::implicitlyannotableelement_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ImplicitlyAnnotableElement)


def test_frontend::core::implicitlyannotableelement_constructor_exists():
    assert callable(frontend::core::ImplicitlyAnnotableElement.__init__)


def test_frontend::core::implicitlyannotableelement_constructor_args():
    sig = inspect.signature(frontend::core::ImplicitlyAnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::optimizationsannotation_is_not_abstract():
    assert not inspect.isabstract(frontend::core::OptimizationsAnnotation)


def test_frontend::core::optimizationsannotation_constructor_exists():
    assert callable(frontend::core::OptimizationsAnnotation.__init__)


def test_frontend::core::optimizationsannotation_constructor_args():
    sig = inspect.signature(frontend::core::OptimizationsAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "enabled" in params, "Missing parameter 'enabled'"

def test_frontend::core::optimizationsannotation_has_enabled():
    assert hasattr(frontend::core::OptimizationsAnnotation, "enabled")
    descriptor = None
    for klass in frontend::core::OptimizationsAnnotation.__mro__:
        if "enabled" in klass.__dict__:
            descriptor = klass.__dict__["enabled"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::metamodelmodelannotation_is_not_abstract():
    assert not inspect.isabstract(frontend::core::MetamodelModelAnnotation)


def test_frontend::core::metamodelmodelannotation_constructor_exists():
    assert callable(frontend::core::MetamodelModelAnnotation.__init__)


def test_frontend::core::metamodelmodelannotation_constructor_args():
    sig = inspect.signature(frontend::core::MetamodelModelAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_frontend::core::metamodelmodelannotation_has_metamodel():
    assert hasattr(frontend::core::MetamodelModelAnnotation, "metamodel")
    descriptor = None
    for klass in frontend::core::MetamodelModelAnnotation.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::annotableelement_is_not_abstract():
    assert not inspect.isabstract(frontend::core::AnnotableElement)


def test_frontend::core::annotableelement_constructor_exists():
    assert callable(frontend::core::AnnotableElement.__init__)


def test_frontend::core::annotableelement_constructor_args():
    sig = inspect.signature(frontend::core::AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_core::annotableelement_is_not_abstract():
    assert not inspect.isabstract(core::AnnotableElement)


def test_core::annotableelement_constructor_exists():
    assert callable(core::AnnotableElement.__init__)


def test_core::annotableelement_constructor_args():
    sig = inspect.signature(core::AnnotableElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::moduledefinition_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ModuleDefinition)


def test_frontend::core::moduledefinition_constructor_exists():
    assert callable(frontend::core::ModuleDefinition.__init__)


def test_frontend::core::moduledefinition_constructor_args():
    sig = inspect.signature(frontend::core::ModuleDefinition.__init__)
    params = list(sig.parameters.keys())



def test_definitionparameter_is_not_abstract():
    assert not inspect.isabstract(DefinitionParameter)


def test_definitionparameter_constructor_exists():
    assert callable(DefinitionParameter.__init__)


def test_definitionparameter_constructor_args():
    sig = inspect.signature(DefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::moduleparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ModuleParameter)


def test_frontend::core::moduleparameter_constructor_exists():
    assert callable(frontend::core::ModuleParameter.__init__)


def test_frontend::core::moduleparameter_constructor_args():
    sig = inspect.signature(frontend::core::ModuleParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::namedelement_is_not_abstract():
    assert not inspect.isabstract(frontend::core::NamedElement)


def test_frontend::core::namedelement_constructor_exists():
    assert callable(frontend::core::NamedElement.__init__)


def test_frontend::core::namedelement_constructor_args():
    sig = inspect.signature(frontend::core::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend::core::namedelement_has_name():
    assert hasattr(frontend::core::NamedElement, "name")
    descriptor = None
    for klass in frontend::core::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::locatedelement_is_not_abstract():
    assert not inspect.isabstract(frontend::core::LocatedElement)


def test_frontend::core::locatedelement_constructor_exists():
    assert callable(frontend::core::LocatedElement.__init__)


def test_frontend::core::locatedelement_constructor_args():
    sig = inspect.signature(frontend::core::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "row" in params, "Missing parameter 'row'"
    assert "column" in params, "Missing parameter 'column'"
    assert "file" in params, "Missing parameter 'file'"

def test_frontend::core::locatedelement_has_row():
    assert hasattr(frontend::core::LocatedElement, "row")
    descriptor = None
    for klass in frontend::core::LocatedElement.__mro__:
        if "row" in klass.__dict__:
            descriptor = klass.__dict__["row"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::locatedelement_has_column():
    assert hasattr(frontend::core::LocatedElement, "column")
    descriptor = None
    for klass in frontend::core::LocatedElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::locatedelement_has_file():
    assert hasattr(frontend::core::LocatedElement, "file")
    descriptor = None
    for klass in frontend::core::LocatedElement.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
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



def test_frontend::core::traceinterface_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TraceInterface)


def test_frontend::core::traceinterface_constructor_exists():
    assert callable(frontend::core::TraceInterface.__init__)


def test_frontend::core::traceinterface_constructor_args():
    sig = inspect.signature(frontend::core::TraceInterface.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::transformationdefinition_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TransformationDefinition)


def test_frontend::core::transformationdefinition_constructor_exists():
    assert callable(frontend::core::TransformationDefinition.__init__)


def test_frontend::core::transformationdefinition_constructor_args():
    sig = inspect.signature(frontend::core::TransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::representmodel_is_not_abstract():
    assert not inspect.isabstract(frontend::core::RepresentModel)


def test_frontend::core::representmodel_constructor_exists():
    assert callable(frontend::core::RepresentModel.__init__)


def test_frontend::core::representmodel_constructor_args():
    sig = inspect.signature(frontend::core::RepresentModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::annotationparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::AnnotationParameter)


def test_frontend::core::annotationparameter_constructor_exists():
    assert callable(frontend::core::AnnotationParameter.__init__)


def test_frontend::core::annotationparameter_constructor_args():
    sig = inspect.signature(frontend::core::AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_annotationparameter_is_not_abstract():
    assert not inspect.isabstract(AnnotationParameter)


def test_annotationparameter_constructor_exists():
    assert callable(AnnotationParameter.__init__)


def test_annotationparameter_constructor_args():
    sig = inspect.signature(AnnotationParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::genericannotation_is_not_abstract():
    assert not inspect.isabstract(frontend::core::GenericAnnotation)


def test_frontend::core::genericannotation_constructor_exists():
    assert callable(frontend::core::GenericAnnotation.__init__)


def test_frontend::core::genericannotation_constructor_args():
    sig = inspect.signature(frontend::core::GenericAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend::core::genericannotation_has_name():
    assert hasattr(frontend::core::GenericAnnotation, "name")
    descriptor = None
    for klass in frontend::core::GenericAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::potencyannotation_is_not_abstract():
    assert not inspect.isabstract(frontend::core::PotencyAnnotation)


def test_frontend::core::potencyannotation_constructor_exists():
    assert callable(frontend::core::PotencyAnnotation.__init__)


def test_frontend::core::potencyannotation_constructor_args():
    sig = inspect.signature(frontend::core::PotencyAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_frontend::core::potencyannotation_has_value():
    assert hasattr(frontend::core::PotencyAnnotation, "value")
    descriptor = None
    for klass in frontend::core::PotencyAnnotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::singleannotation_is_not_abstract():
    assert not inspect.isabstract(frontend::core::SingleAnnotation)


def test_frontend::core::singleannotation_constructor_exists():
    assert callable(frontend::core::SingleAnnotation.__init__)


def test_frontend::core::singleannotation_constructor_args():
    sig = inspect.signature(frontend::core::SingleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_objectsourcevariable_is_not_abstract():
    assert not inspect.isabstract(ObjectSourceVariable)


def test_objectsourcevariable_constructor_exists():
    assert callable(ObjectSourceVariable.__init__)


def test_objectsourcevariable_constructor_args():
    sig = inspect.signature(ObjectSourceVariable.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::sourceexpression_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::SourceExpression)


def test_frontend::tao::sourceexpression_constructor_exists():
    assert callable(frontend::tao::SourceExpression.__init__)


def test_frontend::tao::sourceexpression_constructor_args():
    sig = inspect.signature(frontend::tao::SourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_sourceexpression_is_not_abstract():
    assert not inspect.isabstract(SourceExpression)


def test_sourceexpression_constructor_exists():
    assert callable(SourceExpression.__init__)


def test_sourceexpression_constructor_args():
    sig = inspect.signature(SourceExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::withoptionalvariableexpression_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::WithOptionalVariableExpression)


def test_frontend::tao::withoptionalvariableexpression_constructor_exists():
    assert callable(frontend::tao::WithOptionalVariableExpression.__init__)


def test_frontend::tao::withoptionalvariableexpression_constructor_args():
    sig = inspect.signature(frontend::tao::WithOptionalVariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::assignment_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::Assignment)


def test_frontend::tao::assignment_constructor_exists():
    assert callable(frontend::tao::Assignment.__init__)


def test_frontend::tao::assignment_constructor_args():
    sig = inspect.signature(frontend::tao::Assignment.__init__)
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



def test_frontend::tao::template_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::Template)


def test_frontend::tao::template_constructor_exists():
    assert callable(frontend::tao::Template.__init__)


def test_frontend::tao::template_constructor_args():
    sig = inspect.signature(frontend::tao::Template.__init__)
    params = list(sig.parameters.keys())



def test_objectinstantiation_is_not_abstract():
    assert not inspect.isabstract(ObjectInstantiation)


def test_objectinstantiation_constructor_exists():
    assert callable(ObjectInstantiation.__init__)


def test_objectinstantiation_constructor_args():
    sig = inspect.signature(ObjectInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::templaterootobject_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::TemplateRootObject)


def test_frontend::tao::templaterootobject_constructor_exists():
    assert callable(frontend::tao::TemplateRootObject.__init__)


def test_frontend::tao::templaterootobject_constructor_args():
    sig = inspect.signature(frontend::tao::TemplateRootObject.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::attributeassigment_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::AttributeAssigment)


def test_frontend::tao::attributeassigment_constructor_exists():
    assert callable(frontend::tao::AttributeAssigment.__init__)


def test_frontend::tao::attributeassigment_constructor_args():
    sig = inspect.signature(frontend::tao::AttributeAssigment.__init__)
    params = list(sig.parameters.keys())
    assert "targetFeature" in params, "Missing parameter 'targetFeature'"

def test_frontend::tao::attributeassigment_has_targetFeature():
    assert hasattr(frontend::tao::AttributeAssigment, "targetFeature")
    descriptor = None
    for klass in frontend::tao::AttributeAssigment.__mro__:
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



def test_frontend::tao::invocation_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::Invocation)


def test_frontend::tao::invocation_constructor_exists():
    assert callable(frontend::tao::Invocation.__init__)


def test_frontend::tao::invocation_constructor_args():
    sig = inspect.signature(frontend::tao::Invocation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::objectsyntax_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::ObjectSyntax)


def test_frontend::tao::objectsyntax_constructor_exists():
    assert callable(frontend::tao::ObjectSyntax.__init__)


def test_frontend::tao::objectsyntax_constructor_args():
    sig = inspect.signature(frontend::tao::ObjectSyntax.__init__)
    params = list(sig.parameters.keys())



def test_tao::assignment_is_not_abstract():
    assert not inspect.isabstract(tao::Assignment)


def test_tao::assignment_constructor_exists():
    assert callable(tao::Assignment.__init__)


def test_tao::assignment_constructor_args():
    sig = inspect.signature(tao::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::referenceassignment_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::ReferenceAssignment)


def test_frontend::tao::referenceassignment_constructor_exists():
    assert callable(frontend::tao::ReferenceAssignment.__init__)


def test_frontend::tao::referenceassignment_constructor_args():
    sig = inspect.signature(frontend::tao::ReferenceAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "targetFeature" in params, "Missing parameter 'targetFeature'"
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend::tao::referenceassignment_has_targetFeature():
    assert hasattr(frontend::tao::ReferenceAssignment, "targetFeature")
    descriptor = None
    for klass in frontend::tao::ReferenceAssignment.__mro__:
        if "targetFeature" in klass.__dict__:
            descriptor = klass.__dict__["targetFeature"]
            break
    assert isinstance(descriptor, property)

def test_frontend::tao::referenceassignment_has_multivalued():
    assert hasattr(frontend::tao::ReferenceAssignment, "multivalued")
    descriptor = None
    for klass in frontend::tao::ReferenceAssignment.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_frontend::tao::objectsourcevariable_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::ObjectSourceVariable)


def test_frontend::tao::objectsourcevariable_constructor_exists():
    assert callable(frontend::tao::ObjectSourceVariable.__init__)


def test_frontend::tao::objectsourcevariable_constructor_args():
    sig = inspect.signature(frontend::tao::ObjectSourceVariable.__init__)
    params = list(sig.parameters.keys())



def test_frontend::facilities::copiercallbackdefinition_is_not_abstract():
    assert not inspect.isabstract(frontend::facilities::CopierCallbackDefinition)


def test_frontend::facilities::copiercallbackdefinition_constructor_exists():
    assert callable(frontend::facilities::CopierCallbackDefinition.__init__)


def test_frontend::facilities::copiercallbackdefinition_constructor_args():
    sig = inspect.signature(frontend::facilities::CopierCallbackDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "stop" in params, "Missing parameter 'stop'"

def test_frontend::facilities::copiercallbackdefinition_has_stop():
    assert hasattr(frontend::facilities::CopierCallbackDefinition, "stop")
    descriptor = None
    for klass in frontend::facilities::CopierCallbackDefinition.__mro__:
        if "stop" in klass.__dict__:
            descriptor = klass.__dict__["stop"]
            break
    assert isinstance(descriptor, property)



def test_facilities::copiercallbackdefinition_is_not_abstract():
    assert not inspect.isabstract(facilities::CopierCallbackDefinition)


def test_facilities::copiercallbackdefinition_constructor_exists():
    assert callable(facilities::CopierCallbackDefinition.__init__)


def test_facilities::copiercallbackdefinition_constructor_args():
    sig = inspect.signature(facilities::CopierCallbackDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend::facilities::copier_is_not_abstract():
    assert not inspect.isabstract(frontend::facilities::Copier)


def test_frontend::facilities::copier_constructor_exists():
    assert callable(frontend::facilities::Copier.__init__)


def test_frontend::facilities::copier_constructor_args():
    sig = inspect.signature(frontend::facilities::Copier.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::templateparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::TemplateParameter)


def test_frontend::tao::templateparameter_constructor_exists():
    assert callable(frontend::tao::TemplateParameter.__init__)


def test_frontend::tao::templateparameter_constructor_args():
    sig = inspect.signature(frontend::tao::TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_template_constructor_exists():
    assert callable(Template.__init__)


def test_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::taotransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::TaoTransformation)


def test_frontend::tao::taotransformation_constructor_exists():
    assert callable(frontend::tao::TaoTransformation.__init__)


def test_frontend::tao::taotransformation_constructor_args():
    sig = inspect.signature(frontend::tao::TaoTransformation.__init__)
    params = list(sig.parameters.keys())



def test_invoketransformation_is_not_abstract():
    assert not inspect.isabstract(InvokeTransformation)


def test_invoketransformation_constructor_exists():
    assert callable(InvokeTransformation.__init__)


def test_invoketransformation_constructor_args():
    sig = inspect.signature(InvokeTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::invokeexternal_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::InvokeExternal)


def test_frontend::qool::invokeexternal_constructor_exists():
    assert callable(frontend::qool::InvokeExternal.__init__)


def test_frontend::qool::invokeexternal_constructor_args():
    sig = inspect.signature(frontend::qool::InvokeExternal.__init__)
    params = list(sig.parameters.keys())
    assert "traceAttributeName" in params, "Missing parameter 'traceAttributeName'"
    assert "queueName" in params, "Missing parameter 'queueName'"

def test_frontend::qool::invokeexternal_has_traceAttributeName():
    assert hasattr(frontend::qool::InvokeExternal, "traceAttributeName")
    descriptor = None
    for klass in frontend::qool::InvokeExternal.__mro__:
        if "traceAttributeName" in klass.__dict__:
            descriptor = klass.__dict__["traceAttributeName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::qool::invokeexternal_has_queueName():
    assert hasattr(frontend::qool::InvokeExternal, "queueName")
    descriptor = None
    for klass in frontend::qool::InvokeExternal.__mro__:
        if "queueName" in klass.__dict__:
            descriptor = klass.__dict__["queueName"]
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



def test_frontend::qool::invoketransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::InvokeTransformation)


def test_frontend::qool::invoketransformation_constructor_exists():
    assert callable(frontend::qool::InvokeTransformation.__init__)


def test_frontend::qool::invoketransformation_constructor_args():
    sig = inspect.signature(frontend::qool::InvokeTransformation.__init__)
    params = list(sig.parameters.keys())
    assert "transformationName" in params, "Missing parameter 'transformationName'"
    assert "entryPointName" in params, "Missing parameter 'entryPointName'"

def test_frontend::qool::invoketransformation_has_transformationName():
    assert hasattr(frontend::qool::InvokeTransformation, "transformationName")
    descriptor = None
    for klass in frontend::qool::InvokeTransformation.__mro__:
        if "transformationName" in klass.__dict__:
            descriptor = klass.__dict__["transformationName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::qool::invoketransformation_has_entryPointName():
    assert hasattr(frontend::qool::InvokeTransformation, "entryPointName")
    descriptor = None
    for klass in frontend::qool::InvokeTransformation.__mro__:
        if "entryPointName" in klass.__dict__:
            descriptor = klass.__dict__["entryPointName"]
            break
    assert isinstance(descriptor, property)



def test_frontend::qool::namedinvocationparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::NamedInvocationParameter)


def test_frontend::qool::namedinvocationparameter_constructor_exists():
    assert callable(frontend::qool::NamedInvocationParameter.__init__)


def test_frontend::qool::namedinvocationparameter_constructor_args():
    sig = inspect.signature(frontend::qool::NamedInvocationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "formalName" in params, "Missing parameter 'formalName'"

def test_frontend::qool::namedinvocationparameter_has_formalName():
    assert hasattr(frontend::qool::NamedInvocationParameter, "formalName")
    descriptor = None
    for klass in frontend::qool::NamedInvocationParameter.__mro__:
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



def test_frontend::qool::invocationparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::InvocationParameter)


def test_frontend::qool::invocationparameter_constructor_exists():
    assert callable(frontend::qool::InvocationParameter.__init__)


def test_frontend::qool::invocationparameter_constructor_args():
    sig = inspect.signature(frontend::qool::InvocationParameter.__init__)
    params = list(sig.parameters.keys())
    assert "calleeModelName" in params, "Missing parameter 'calleeModelName'"

def test_frontend::qool::invocationparameter_has_calleeModelName():
    assert hasattr(frontend::qool::InvocationParameter, "calleeModelName")
    descriptor = None
    for klass in frontend::qool::InvocationParameter.__mro__:
        if "calleeModelName" in klass.__dict__:
            descriptor = klass.__dict__["calleeModelName"]
            break
    assert isinstance(descriptor, property)



def test_frontend::qool::invokeinternal_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::InvokeInternal)


def test_frontend::qool::invokeinternal_constructor_exists():
    assert callable(frontend::qool::InvokeInternal.__init__)


def test_frontend::qool::invokeinternal_constructor_args():
    sig = inspect.signature(frontend::qool::InvokeInternal.__init__)
    params = list(sig.parameters.keys())



def test_iteratorstatement_is_not_abstract():
    assert not inspect.isabstract(IteratorStatement)


def test_iteratorstatement_constructor_exists():
    assert callable(IteratorStatement.__init__)


def test_iteratorstatement_constructor_args():
    sig = inspect.signature(IteratorStatement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::foreachstatement_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::ForEachStatement)


def test_frontend::qool::foreachstatement_constructor_exists():
    assert callable(frontend::qool::ForEachStatement.__init__)


def test_frontend::qool::foreachstatement_constructor_args():
    sig = inspect.signature(frontend::qool::ForEachStatement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::forallstatement_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::ForAllStatement)


def test_frontend::qool::forallstatement_constructor_exists():
    assert callable(frontend::qool::ForAllStatement.__init__)


def test_frontend::qool::forallstatement_constructor_args():
    sig = inspect.signature(frontend::qool::ForAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_core::statement_is_not_abstract():
    assert not inspect.isabstract(core::Statement)


def test_core::statement_constructor_exists():
    assert callable(core::Statement.__init__)


def test_core::statement_constructor_args():
    sig = inspect.signature(core::Statement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::tao::objectinstantiation_is_not_abstract():
    assert not inspect.isabstract(frontend::tao::ObjectInstantiation)


def test_frontend::tao::objectinstantiation_constructor_exists():
    assert callable(frontend::tao::ObjectInstantiation.__init__)


def test_frontend::tao::objectinstantiation_constructor_args():
    sig = inspect.signature(frontend::tao::ObjectInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::definevariable_is_not_abstract():
    assert not inspect.isabstract(frontend::core::DefineVariable)


def test_frontend::core::definevariable_constructor_exists():
    assert callable(frontend::core::DefineVariable.__init__)


def test_frontend::core::definevariable_constructor_args():
    sig = inspect.signature(frontend::core::DefineVariable.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::iteratorstatement_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::IteratorStatement)


def test_frontend::qool::iteratorstatement_constructor_exists():
    assert callable(frontend::qool::IteratorStatement.__init__)


def test_frontend::qool::iteratorstatement_constructor_args():
    sig = inspect.signature(frontend::qool::IteratorStatement.__init__)
    params = list(sig.parameters.keys())



def test_typeexpression_is_not_abstract():
    assert not inspect.isabstract(TypeExpression)


def test_typeexpression_constructor_exists():
    assert callable(TypeExpression.__init__)


def test_typeexpression_constructor_args():
    sig = inspect.signature(TypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::traceuse_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TraceUse)


def test_frontend::core::traceuse_constructor_exists():
    assert callable(frontend::core::TraceUse.__init__)


def test_frontend::core::traceuse_constructor_args():
    sig = inspect.signature(frontend::core::TraceUse.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::queueoptimization_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::QueueOptimization)


def test_frontend::qool::queueoptimization_constructor_exists():
    assert callable(frontend::qool::QueueOptimization.__init__)


def test_frontend::qool::queueoptimization_constructor_args():
    sig = inspect.signature(frontend::qool::QueueOptimization.__init__)
    params = list(sig.parameters.keys())



def test_queueoptimization_is_not_abstract():
    assert not inspect.isabstract(QueueOptimization)


def test_queueoptimization_constructor_exists():
    assert callable(QueueOptimization.__init__)


def test_queueoptimization_constructor_args():
    sig = inspect.signature(QueueOptimization.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::accessbyfeatureoptimization_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::AccessByFeatureOptimization)


def test_frontend::qool::accessbyfeatureoptimization_constructor_exists():
    assert callable(frontend::qool::AccessByFeatureOptimization.__init__)


def test_frontend::qool::accessbyfeatureoptimization_constructor_args():
    sig = inspect.signature(frontend::qool::AccessByFeatureOptimization.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "force" in params, "Missing parameter 'force'"

def test_frontend::qool::accessbyfeatureoptimization_has_featureName():
    assert hasattr(frontend::qool::AccessByFeatureOptimization, "featureName")
    descriptor = None
    for klass in frontend::qool::AccessByFeatureOptimization.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::qool::accessbyfeatureoptimization_has_force():
    assert hasattr(frontend::qool::AccessByFeatureOptimization, "force")
    descriptor = None
    for klass in frontend::qool::AccessByFeatureOptimization.__mro__:
        if "force" in klass.__dict__:
            descriptor = klass.__dict__["force"]
            break
    assert isinstance(descriptor, property)



def test_frontend::qool::matchpredicate_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::MatchPredicate)


def test_frontend::qool::matchpredicate_constructor_exists():
    assert callable(frontend::qool::MatchPredicate.__init__)


def test_frontend::qool::matchpredicate_constructor_args():
    sig = inspect.signature(frontend::qool::MatchPredicate.__init__)
    params = list(sig.parameters.keys())



def test_matchpredicate_is_not_abstract():
    assert not inspect.isabstract(MatchPredicate)


def test_matchpredicate_constructor_exists():
    assert callable(MatchPredicate.__init__)


def test_matchpredicate_constructor_args():
    sig = inspect.signature(MatchPredicate.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::kindofpredicate_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::KindOfPredicate)


def test_frontend::qool::kindofpredicate_constructor_exists():
    assert callable(frontend::qool::KindOfPredicate.__init__)


def test_frontend::qool::kindofpredicate_constructor_args():
    sig = inspect.signature(frontend::qool::KindOfPredicate.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::propertyequalspredicate_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::PropertyEqualsPredicate)


def test_frontend::qool::propertyequalspredicate_constructor_exists():
    assert callable(frontend::qool::PropertyEqualsPredicate.__init__)


def test_frontend::qool::propertyequalspredicate_constructor_args():
    sig = inspect.signature(frontend::qool::PropertyEqualsPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_frontend::qool::propertyequalspredicate_has_propertyName():
    assert hasattr(frontend::qool::PropertyEqualsPredicate, "propertyName")
    descriptor = None
    for klass in frontend::qool::PropertyEqualsPredicate.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_frontend::qool::matchexpression_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::MatchExpression)


def test_frontend::qool::matchexpression_constructor_exists():
    assert callable(frontend::qool::MatchExpression.__init__)


def test_frontend::qool::matchexpression_constructor_args():
    sig = inspect.signature(frontend::qool::MatchExpression.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::emitstatement_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::EmitStatement)


def test_frontend::qool::emitstatement_constructor_exists():
    assert callable(frontend::qool::EmitStatement.__init__)


def test_frontend::qool::emitstatement_constructor_args():
    sig = inspect.signature(frontend::qool::EmitStatement.__init__)
    params = list(sig.parameters.keys())



def test_mappings::metamodelelementref_is_not_abstract():
    assert not inspect.isabstract(mappings::MetamodelElementRef)


def test_mappings::metamodelelementref_constructor_exists():
    assert callable(mappings::MetamodelElementRef.__init__)


def test_mappings::metamodelelementref_constructor_args():
    sig = inspect.signature(mappings::MetamodelElementRef.__init__)
    params = list(sig.parameters.keys())



def test_metamodelelementref_is_not_abstract():
    assert not inspect.isabstract(MetamodelElementRef)


def test_metamodelelementref_constructor_exists():
    assert callable(MetamodelElementRef.__init__)


def test_metamodelelementref_constructor_args():
    sig = inspect.signature(MetamodelElementRef.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::attributeref_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeRef)


def test_frontend::mappings::attributeref_constructor_exists():
    assert callable(frontend::mappings::AttributeRef.__init__)


def test_frontend::mappings::attributeref_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeRef.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend::mappings::attributeref_has_featureName():
    assert hasattr(frontend::mappings::AttributeRef, "featureName")
    descriptor = None
    for klass in frontend::mappings::AttributeRef.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::mappings::attributeref_has_multivalued():
    assert hasattr(frontend::mappings::AttributeRef, "multivalued")
    descriptor = None
    for klass in frontend::mappings::AttributeRef.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_frontend::mappings::classref_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::ClassRef)


def test_frontend::mappings::classref_constructor_exists():
    assert callable(frontend::mappings::ClassRef.__init__)


def test_frontend::mappings::classref_constructor_args():
    sig = inspect.signature(frontend::mappings::ClassRef.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::metamodelelementref_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::MetamodelElementRef)


def test_frontend::mappings::metamodelelementref_constructor_exists():
    assert callable(frontend::mappings::MetamodelElementRef.__init__)


def test_frontend::mappings::metamodelelementref_constructor_args():
    sig = inspect.signature(frontend::mappings::MetamodelElementRef.__init__)
    params = list(sig.parameters.keys())



def test_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(DefaultValue)


def test_defaultvalue_constructor_exists():
    assert callable(DefaultValue.__init__)


def test_defaultvalue_constructor_args():
    sig = inspect.signature(DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::intdefaultvalue_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::IntDefaultValue)


def test_frontend::mappings::intdefaultvalue_constructor_exists():
    assert callable(frontend::mappings::IntDefaultValue.__init__)


def test_frontend::mappings::intdefaultvalue_constructor_args():
    sig = inspect.signature(frontend::mappings::IntDefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_frontend::mappings::intdefaultvalue_has_defaultValue():
    assert hasattr(frontend::mappings::IntDefaultValue, "defaultValue")
    descriptor = None
    for klass in frontend::mappings::IntDefaultValue.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_frontend::qool::qoolqueue_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::QoolQueue)


def test_frontend::qool::qoolqueue_constructor_exists():
    assert callable(frontend::qool::QoolQueue.__init__)


def test_frontend::qool::qoolqueue_constructor_args():
    sig = inspect.signature(frontend::qool::QoolQueue.__init__)
    params = list(sig.parameters.keys())



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



def test_frontend::qool::modelelementqueue_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::ModelElementQueue)


def test_frontend::qool::modelelementqueue_constructor_exists():
    assert callable(frontend::qool::ModelElementQueue.__init__)


def test_frontend::qool::modelelementqueue_constructor_args():
    sig = inspect.signature(frontend::qool::ModelElementQueue.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::localqueue_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::LocalQueue)


def test_frontend::qool::localqueue_constructor_exists():
    assert callable(frontend::qool::LocalQueue.__init__)


def test_frontend::qool::localqueue_constructor_args():
    sig = inspect.signature(frontend::qool::LocalQueue.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::qooltransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::QoolTransformation)


def test_frontend::qool::qooltransformation_constructor_exists():
    assert callable(frontend::qool::QoolTransformation.__init__)


def test_frontend::qool::qooltransformation_constructor_args():
    sig = inspect.signature(frontend::qool::QoolTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::referenceref_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::ReferenceRef)


def test_frontend::mappings::referenceref_constructor_exists():
    assert callable(frontend::mappings::ReferenceRef.__init__)


def test_frontend::mappings::referenceref_constructor_args():
    sig = inspect.signature(frontend::mappings::ReferenceRef.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_frontend::mappings::referenceref_has_multivalued():
    assert hasattr(frontend::mappings::ReferenceRef, "multivalued")
    descriptor = None
    for klass in frontend::mappings::ReferenceRef.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)

def test_frontend::mappings::referenceref_has_featureName():
    assert hasattr(frontend::mappings::ReferenceRef, "featureName")
    descriptor = None
    for klass in frontend::mappings::ReferenceRef.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_attributemodifier_is_not_abstract():
    assert not inspect.isabstract(AttributeModifier)


def test_attributemodifier_constructor_exists():
    assert callable(AttributeModifier.__init__)


def test_attributemodifier_constructor_args():
    sig = inspect.signature(AttributeModifier.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::defaultvalue_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::DefaultValue)


def test_frontend::mappings::defaultvalue_constructor_exists():
    assert callable(frontend::mappings::DefaultValue.__init__)


def test_frontend::mappings::defaultvalue_constructor_args():
    sig = inspect.signature(frontend::mappings::DefaultValue.__init__)
    params = list(sig.parameters.keys())



def test_class2class_is_not_abstract():
    assert not inspect.isabstract(Class2Class)


def test_class2class_constructor_exists():
    assert callable(Class2Class.__init__)


def test_class2class_constructor_args():
    sig = inspect.signature(Class2Class.__init__)
    params = list(sig.parameters.keys())



def test_mappings::attributerightpart_is_not_abstract():
    assert not inspect.isabstract(mappings::AttributeRightPart)


def test_mappings::attributerightpart_constructor_exists():
    assert callable(mappings::AttributeRightPart.__init__)


def test_mappings::attributerightpart_constructor_args():
    sig = inspect.signature(mappings::AttributeRightPart.__init__)
    params = list(sig.parameters.keys())



def test_mappings::feature2feature_is_not_abstract():
    assert not inspect.isabstract(mappings::Feature2Feature)


def test_mappings::feature2feature_constructor_exists():
    assert callable(mappings::Feature2Feature.__init__)


def test_mappings::feature2feature_constructor_args():
    sig = inspect.signature(mappings::Feature2Feature.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::featureref_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::FeatureRef)


def test_frontend::mappings::featureref_constructor_exists():
    assert callable(frontend::mappings::FeatureRef.__init__)


def test_frontend::mappings::featureref_constructor_args():
    sig = inspect.signature(frontend::mappings::FeatureRef.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"
    assert "featureName" in params, "Missing parameter 'featureName'"

def test_frontend::mappings::featureref_has_multivalued():
    assert hasattr(frontend::mappings::FeatureRef, "multivalued")
    descriptor = None
    for klass in frontend::mappings::FeatureRef.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)

def test_frontend::mappings::featureref_has_featureName():
    assert hasattr(frontend::mappings::FeatureRef, "featureName")
    descriptor = None
    for klass in frontend::mappings::FeatureRef.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)



def test_frontend::mappings::attribute2attribute_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Attribute2Attribute)


def test_frontend::mappings::attribute2attribute_constructor_exists():
    assert callable(frontend::mappings::Attribute2Attribute.__init__)


def test_frontend::mappings::attribute2attribute_constructor_args():
    sig = inspect.signature(frontend::mappings::Attribute2Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_frontend::mappings::attribute2attribute_has_cardinality():
    assert hasattr(frontend::mappings::Attribute2Attribute, "cardinality")
    descriptor = None
    for klass in frontend::mappings::Attribute2Attribute.__mro__:
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



def test_frontend::mappings::join_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Join)


def test_frontend::mappings::join_constructor_exists():
    assert callable(frontend::mappings::Join.__init__)


def test_frontend::mappings::join_constructor_args():
    sig = inspect.signature(frontend::mappings::Join.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::split_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Split)


def test_frontend::mappings::split_constructor_exists():
    assert callable(frontend::mappings::Split.__init__)


def test_frontend::mappings::split_constructor_args():
    sig = inspect.signature(frontend::mappings::Split.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::operator_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Operator)


def test_frontend::mappings::operator_constructor_exists():
    assert callable(frontend::mappings::Operator.__init__)


def test_frontend::mappings::operator_constructor_args():
    sig = inspect.signature(frontend::mappings::Operator.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::convertmodifier_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::ConvertModifier)


def test_frontend::mappings::convertmodifier_constructor_exists():
    assert callable(frontend::mappings::ConvertModifier.__init__)


def test_frontend::mappings::convertmodifier_constructor_args():
    sig = inspect.signature(frontend::mappings::ConvertModifier.__init__)
    params = list(sig.parameters.keys())
    assert "converter" in params, "Missing parameter 'converter'"

def test_frontend::mappings::convertmodifier_has_converter():
    assert hasattr(frontend::mappings::ConvertModifier, "converter")
    descriptor = None
    for klass in frontend::mappings::ConvertModifier.__mro__:
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



def test_frontend::mappings::attributemodifier_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeModifier)


def test_frontend::mappings::attributemodifier_constructor_exists():
    assert callable(frontend::mappings::AttributeModifier.__init__)


def test_frontend::mappings::attributemodifier_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeModifier.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::modifier_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Modifier)


def test_frontend::mappings::modifier_constructor_exists():
    assert callable(frontend::mappings::Modifier.__init__)


def test_frontend::mappings::modifier_constructor_args():
    sig = inspect.signature(frontend::mappings::Modifier.__init__)
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



def test_frontend::mappings::class2class_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Class2Class)


def test_frontend::mappings::class2class_constructor_exists():
    assert callable(frontend::mappings::Class2Class.__init__)


def test_frontend::mappings::class2class_constructor_args():
    sig = inspect.signature(frontend::mappings::Class2Class.__init__)
    params = list(sig.parameters.keys())
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_frontend::mappings::class2class_has_cardinality():
    assert hasattr(frontend::mappings::Class2Class, "cardinality")
    descriptor = None
    for klass in frontend::mappings::Class2Class.__mro__:
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



def test_frontend::core::inlinefeature_is_not_abstract():
    assert not inspect.isabstract(frontend::core::InlineFeature)


def test_frontend::core::inlinefeature_constructor_exists():
    assert callable(frontend::core::InlineFeature.__init__)


def test_frontend::core::inlinefeature_constructor_args():
    sig = inspect.signature(frontend::core::InlineFeature.__init__)
    params = list(sig.parameters.keys())
    assert "multivalued" in params, "Missing parameter 'multivalued'"

def test_frontend::core::inlinefeature_has_multivalued():
    assert hasattr(frontend::core::InlineFeature, "multivalued")
    descriptor = None
    for klass in frontend::core::InlineFeature.__mro__:
        if "multivalued" in klass.__dict__:
            descriptor = klass.__dict__["multivalued"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::traceelement_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TraceElement)


def test_frontend::core::traceelement_constructor_exists():
    assert callable(frontend::core::TraceElement.__init__)


def test_frontend::core::traceelement_constructor_args():
    sig = inspect.signature(frontend::core::TraceElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::definitionparameter_is_not_abstract():
    assert not inspect.isabstract(frontend::core::DefinitionParameter)


def test_frontend::core::definitionparameter_constructor_exists():
    assert callable(frontend::core::DefinitionParameter.__init__)


def test_frontend::core::definitionparameter_constructor_args():
    sig = inspect.signature(frontend::core::DefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::tracedefinition_is_not_abstract():
    assert not inspect.isabstract(frontend::core::TraceDefinition)


def test_frontend::core::tracedefinition_constructor_exists():
    assert callable(frontend::core::TraceDefinition.__init__)


def test_frontend::core::tracedefinition_constructor_args():
    sig = inspect.signature(frontend::core::TraceDefinition.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::inlineclass_is_not_abstract():
    assert not inspect.isabstract(frontend::core::InlineClass)


def test_frontend::core::inlineclass_constructor_exists():
    assert callable(frontend::core::InlineClass.__init__)


def test_frontend::core::inlineclass_constructor_args():
    sig = inspect.signature(frontend::core::InlineClass.__init__)
    params = list(sig.parameters.keys())



def test_frontend::qool::segment_is_not_abstract():
    assert not inspect.isabstract(frontend::qool::Segment)


def test_frontend::qool::segment_constructor_exists():
    assert callable(frontend::qool::Segment.__init__)


def test_frontend::qool::segment_constructor_args():
    sig = inspect.signature(frontend::qool::Segment.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::tag_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Tag)


def test_frontend::mappings::tag_constructor_exists():
    assert callable(frontend::mappings::Tag.__init__)


def test_frontend::mappings::tag_constructor_args():
    sig = inspect.signature(frontend::mappings::Tag.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::converter_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Converter)


def test_frontend::mappings::converter_constructor_exists():
    assert callable(frontend::mappings::Converter.__init__)


def test_frontend::mappings::converter_constructor_args():
    sig = inspect.signature(frontend::mappings::Converter.__init__)
    params = list(sig.parameters.keys())
    assert "converterName" in params, "Missing parameter 'converterName'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_frontend::mappings::converter_has_converterName():
    assert hasattr(frontend::mappings::Converter, "converterName")
    descriptor = None
    for klass in frontend::mappings::Converter.__mro__:
        if "converterName" in klass.__dict__:
            descriptor = klass.__dict__["converterName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::mappings::converter_has_isExternal():
    assert hasattr(frontend::mappings::Converter, "isExternal")
    descriptor = None
    for klass in frontend::mappings::Converter.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
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



def test_frontend::mappings::relatedby_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::RelatedBy)


def test_frontend::mappings::relatedby_constructor_exists():
    assert callable(frontend::mappings::RelatedBy.__init__)


def test_frontend::mappings::relatedby_constructor_args():
    sig = inspect.signature(frontend::mappings::RelatedBy.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::linkedby_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::LinkedBy)


def test_frontend::mappings::linkedby_constructor_exists():
    assert callable(frontend::mappings::LinkedBy.__init__)


def test_frontend::mappings::linkedby_constructor_args():
    sig = inspect.signature(frontend::mappings::LinkedBy.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::equalityfilter_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::EqualityFilter)


def test_frontend::mappings::equalityfilter_constructor_exists():
    assert callable(frontend::mappings::EqualityFilter.__init__)


def test_frontend::mappings::equalityfilter_constructor_args():
    sig = inspect.signature(frontend::mappings::EqualityFilter.__init__)
    params = list(sig.parameters.keys())
    assert "filter" in params, "Missing parameter 'filter'"

def test_frontend::mappings::equalityfilter_has_filter():
    assert hasattr(frontend::mappings::EqualityFilter, "filter")
    descriptor = None
    for klass in frontend::mappings::EqualityFilter.__mro__:
        if "filter" in klass.__dict__:
            descriptor = klass.__dict__["filter"]
            break
    assert isinstance(descriptor, property)



def test_mappingelement_is_not_abstract():
    assert not inspect.isabstract(MappingElement)


def test_mappingelement_constructor_exists():
    assert callable(MappingElement.__init__)


def test_mappingelement_constructor_args():
    sig = inspect.signature(MappingElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::c2cmodifier_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::C2CModifier)


def test_frontend::mappings::c2cmodifier_constructor_exists():
    assert callable(frontend::mappings::C2CModifier.__init__)


def test_frontend::mappings::c2cmodifier_constructor_args():
    sig = inspect.signature(frontend::mappings::C2CModifier.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::context_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Context)


def test_frontend::mappings::context_constructor_exists():
    assert callable(frontend::mappings::Context.__init__)


def test_frontend::mappings::context_constructor_args():
    sig = inspect.signature(frontend::mappings::Context.__init__)
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



def test_frontend::mappings::delegate_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Delegate)


def test_frontend::mappings::delegate_constructor_exists():
    assert callable(frontend::mappings::Delegate.__init__)


def test_frontend::mappings::delegate_constructor_args():
    sig = inspect.signature(frontend::mappings::Delegate.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"
    assert "linkName" in params, "Missing parameter 'linkName'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"

def test_frontend::mappings::delegate_has_featureName():
    assert hasattr(frontend::mappings::Delegate, "featureName")
    descriptor = None
    for klass in frontend::mappings::Delegate.__mro__:
        if "featureName" in klass.__dict__:
            descriptor = klass.__dict__["featureName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::mappings::delegate_has_linkName():
    assert hasattr(frontend::mappings::Delegate, "linkName")
    descriptor = None
    for klass in frontend::mappings::Delegate.__mro__:
        if "linkName" in klass.__dict__:
            descriptor = klass.__dict__["linkName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::mappings::delegate_has_isExternal():
    assert hasattr(frontend::mappings::Delegate, "isExternal")
    descriptor = None
    for klass in frontend::mappings::Delegate.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)



def test_mappings::mappingvariable_is_not_abstract():
    assert not inspect.isabstract(mappings::MappingVariable)


def test_mappings::mappingvariable_constructor_exists():
    assert callable(mappings::MappingVariable.__init__)


def test_mappings::mappingvariable_constructor_args():
    sig = inspect.signature(mappings::MappingVariable.__init__)
    params = list(sig.parameters.keys())



def test_core::classuse_is_not_abstract():
    assert not inspect.isabstract(core::ClassUse)


def test_core::classuse_constructor_exists():
    assert callable(core::ClassUse.__init__)


def test_core::classuse_constructor_args():
    sig = inspect.signature(core::ClassUse.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::modelreference_is_not_abstract():
    assert not inspect.isabstract(frontend::core::ModelReference)


def test_frontend::core::modelreference_constructor_exists():
    assert callable(frontend::core::ModelReference.__init__)


def test_frontend::core::modelreference_constructor_args():
    sig = inspect.signature(frontend::core::ModelReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::matchedelement_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::MatchedElement)


def test_frontend::mappings::matchedelement_constructor_exists():
    assert callable(frontend::mappings::MatchedElement.__init__)


def test_frontend::mappings::matchedelement_constructor_args():
    sig = inspect.signature(frontend::mappings::MatchedElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::mappingvariable_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::MappingVariable)


def test_frontend::mappings::mappingvariable_constructor_exists():
    assert callable(frontend::mappings::MappingVariable.__init__)


def test_frontend::mappings::mappingvariable_constructor_args():
    sig = inspect.signature(frontend::mappings::MappingVariable.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::attributerightpart_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeRightPart)


def test_frontend::mappings::attributerightpart_constructor_exists():
    assert callable(frontend::mappings::AttributeRightPart.__init__)


def test_frontend::mappings::attributerightpart_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeRightPart.__init__)
    params = list(sig.parameters.keys())



def test_attributerightpart_is_not_abstract():
    assert not inspect.isabstract(AttributeRightPart)


def test_attributerightpart_constructor_exists():
    assert callable(AttributeRightPart.__init__)


def test_attributerightpart_constructor_args():
    sig = inspect.signature(AttributeRightPart.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::attributeisresolvelink_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeIsResolveLink)


def test_frontend::mappings::attributeisresolvelink_constructor_exists():
    assert callable(frontend::mappings::AttributeIsResolveLink.__init__)


def test_frontend::mappings::attributeisresolvelink_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeIsResolveLink.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::attributeisstring_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeIsString)


def test_frontend::mappings::attributeisstring_constructor_exists():
    assert callable(frontend::mappings::AttributeIsString.__init__)


def test_frontend::mappings::attributeisstring_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeIsString.__init__)
    params = list(sig.parameters.keys())
    assert "strValue" in params, "Missing parameter 'strValue'"

def test_frontend::mappings::attributeisstring_has_strValue():
    assert hasattr(frontend::mappings::AttributeIsString, "strValue")
    descriptor = None
    for klass in frontend::mappings::AttributeIsString.__mro__:
        if "strValue" in klass.__dict__:
            descriptor = klass.__dict__["strValue"]
            break
    assert isinstance(descriptor, property)



def test_frontend::mappings::attributeisinteger_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeIsInteger)


def test_frontend::mappings::attributeisinteger_constructor_exists():
    assert callable(frontend::mappings::AttributeIsInteger.__init__)


def test_frontend::mappings::attributeisinteger_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeIsInteger.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_frontend::mappings::attributeisinteger_has_intValue():
    assert hasattr(frontend::mappings::AttributeIsInteger, "intValue")
    descriptor = None
    for klass in frontend::mappings::AttributeIsInteger.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_frontend::mappings::attributeisdouble_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeIsDouble)


def test_frontend::mappings::attributeisdouble_constructor_exists():
    assert callable(frontend::mappings::AttributeIsDouble.__init__)


def test_frontend::mappings::attributeisdouble_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeIsDouble.__init__)
    params = list(sig.parameters.keys())
    assert "doubleValue" in params, "Missing parameter 'doubleValue'"

def test_frontend::mappings::attributeisdouble_has_doubleValue():
    assert hasattr(frontend::mappings::AttributeIsDouble, "doubleValue")
    descriptor = None
    for klass in frontend::mappings::AttributeIsDouble.__mro__:
        if "doubleValue" in klass.__dict__:
            descriptor = klass.__dict__["doubleValue"]
            break
    assert isinstance(descriptor, property)



def test_frontend::mappings::attributeisboolean_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeIsBoolean)


def test_frontend::mappings::attributeisboolean_constructor_exists():
    assert callable(frontend::mappings::AttributeIsBoolean.__init__)


def test_frontend::mappings::attributeisboolean_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeIsBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "boolValue" in params, "Missing parameter 'boolValue'"

def test_frontend::mappings::attributeisboolean_has_boolValue():
    assert hasattr(frontend::mappings::AttributeIsBoolean, "boolValue")
    descriptor = None
    for klass in frontend::mappings::AttributeIsBoolean.__mro__:
        if "boolValue" in klass.__dict__:
            descriptor = klass.__dict__["boolValue"]
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



def test_frontend::mappings::reference2reference_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Reference2Reference)


def test_frontend::mappings::reference2reference_constructor_exists():
    assert callable(frontend::mappings::Reference2Reference.__init__)


def test_frontend::mappings::reference2reference_constructor_args():
    sig = inspect.signature(frontend::mappings::Reference2Reference.__init__)
    params = list(sig.parameters.keys())
    assert "resolverName" in params, "Missing parameter 'resolverName'"
    assert "cardinality" in params, "Missing parameter 'cardinality'"

def test_frontend::mappings::reference2reference_has_resolverName():
    assert hasattr(frontend::mappings::Reference2Reference, "resolverName")
    descriptor = None
    for klass in frontend::mappings::Reference2Reference.__mro__:
        if "resolverName" in klass.__dict__:
            descriptor = klass.__dict__["resolverName"]
            break
    assert isinstance(descriptor, property)

def test_frontend::mappings::reference2reference_has_cardinality():
    assert hasattr(frontend::mappings::Reference2Reference, "cardinality")
    descriptor = None
    for klass in frontend::mappings::Reference2Reference.__mro__:
        if "cardinality" in klass.__dict__:
            descriptor = klass.__dict__["cardinality"]
            break
    assert isinstance(descriptor, property)



def test_frontend::mappings::attributemapping_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::AttributeMapping)


def test_frontend::mappings::attributemapping_constructor_exists():
    assert callable(frontend::mappings::AttributeMapping.__init__)


def test_frontend::mappings::attributemapping_constructor_args():
    sig = inspect.signature(frontend::mappings::AttributeMapping.__init__)
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



def test_frontend::mappings::feature2feature_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Feature2Feature)


def test_frontend::mappings::feature2feature_constructor_exists():
    assert callable(frontend::mappings::Feature2Feature.__init__)


def test_frontend::mappings::feature2feature_constructor_args():
    sig = inspect.signature(frontend::mappings::Feature2Feature.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::classmapping_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::ClassMapping)


def test_frontend::mappings::classmapping_constructor_exists():
    assert callable(frontend::mappings::ClassMapping.__init__)


def test_frontend::mappings::classmapping_constructor_args():
    sig = inspect.signature(frontend::mappings::ClassMapping.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::mappingelement_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::MappingElement)


def test_frontend::mappings::mappingelement_constructor_exists():
    assert callable(frontend::mappings::MappingElement.__init__)


def test_frontend::mappings::mappingelement_constructor_args():
    sig = inspect.signature(frontend::mappings::MappingElement.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::section_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::Section)


def test_frontend::mappings::section_constructor_exists():
    assert callable(frontend::mappings::Section.__init__)


def test_frontend::mappings::section_constructor_args():
    sig = inspect.signature(frontend::mappings::Section.__init__)
    params = list(sig.parameters.keys())
    assert "sectionType" in params, "Missing parameter 'sectionType'"

def test_frontend::mappings::section_has_sectionType():
    assert hasattr(frontend::mappings::Section, "sectionType")
    descriptor = None
    for klass in frontend::mappings::Section.__mro__:
        if "sectionType" in klass.__dict__:
            descriptor = klass.__dict__["sectionType"]
            break
    assert isinstance(descriptor, property)



def test_frontend::patterns::pobject_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::PObject)


def test_frontend::patterns::pobject_constructor_exists():
    assert callable(frontend::patterns::PObject.__init__)


def test_frontend::patterns::pobject_constructor_args():
    sig = inspect.signature(frontend::patterns::PObject.__init__)
    params = list(sig.parameters.keys())



def test_frontend::patterns::poutputvariable_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::POutputVariable)


def test_frontend::patterns::poutputvariable_constructor_exists():
    assert callable(frontend::patterns::POutputVariable.__init__)


def test_frontend::patterns::poutputvariable_constructor_args():
    sig = inspect.signature(frontend::patterns::POutputVariable.__init__)
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



def test_frontend::patterns::pattern_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::Pattern)


def test_frontend::patterns::pattern_constructor_exists():
    assert callable(frontend::patterns::Pattern.__init__)


def test_frontend::patterns::pattern_constructor_args():
    sig = inspect.signature(frontend::patterns::Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_frontend::patterns::pattern_has_name():
    assert hasattr(frontend::patterns::Pattern, "name")
    descriptor = None
    for klass in frontend::patterns::Pattern.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_frontend::patterns::patternspecification_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::PatternSpecification)


def test_frontend::patterns::patternspecification_constructor_exists():
    assert callable(frontend::patterns::PatternSpecification.__init__)


def test_frontend::patterns::patternspecification_constructor_args():
    sig = inspect.signature(frontend::patterns::PatternSpecification.__init__)
    params = list(sig.parameters.keys())



def test_core::transformationdefinition_is_not_abstract():
    assert not inspect.isabstract(core::TransformationDefinition)


def test_core::transformationdefinition_constructor_exists():
    assert callable(core::TransformationDefinition.__init__)


def test_core::transformationdefinition_constructor_args():
    sig = inspect.signature(core::TransformationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_chain::availabletransformation_is_not_abstract():
    assert not inspect.isabstract(chain::AvailableTransformation)


def test_chain::availabletransformation_constructor_exists():
    assert callable(chain::AvailableTransformation.__init__)


def test_chain::availabletransformation_constructor_args():
    sig = inspect.signature(chain::AvailableTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::chain::compositetransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::chain::CompositeTransformation)


def test_frontend::chain::compositetransformation_constructor_exists():
    assert callable(frontend::chain::CompositeTransformation.__init__)


def test_frontend::chain::compositetransformation_constructor_args():
    sig = inspect.signature(frontend::chain::CompositeTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::chain::externaltransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::chain::ExternalTransformation)


def test_frontend::chain::externaltransformation_constructor_exists():
    assert callable(frontend::chain::ExternalTransformation.__init__)


def test_frontend::chain::externaltransformation_constructor_args():
    sig = inspect.signature(frontend::chain::ExternalTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::chain::availabletransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::chain::AvailableTransformation)


def test_frontend::chain::availabletransformation_constructor_exists():
    assert callable(frontend::chain::AvailableTransformation.__init__)


def test_frontend::chain::availabletransformation_constructor_args():
    sig = inspect.signature(frontend::chain::AvailableTransformation.__init__)
    params = list(sig.parameters.keys())



def test_representmodel_is_not_abstract():
    assert not inspect.isabstract(RepresentModel)


def test_representmodel_constructor_exists():
    assert callable(RepresentModel.__init__)


def test_representmodel_constructor_args():
    sig = inspect.signature(RepresentModel.__init__)
    params = list(sig.parameters.keys())



def test_frontend::core::usedeclaration_is_not_abstract():
    assert not inspect.isabstract(frontend::core::UseDeclaration)


def test_frontend::core::usedeclaration_constructor_exists():
    assert callable(frontend::core::UseDeclaration.__init__)


def test_frontend::core::usedeclaration_constructor_args():
    sig = inspect.signature(frontend::core::UseDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "as_" in params, "Missing parameter 'as_'"
    assert "module" in params, "Missing parameter 'module'"

def test_frontend::core::usedeclaration_has_as_():
    assert hasattr(frontend::core::UseDeclaration, "as_")
    descriptor = None
    for klass in frontend::core::UseDeclaration.__mro__:
        if "as_" in klass.__dict__:
            descriptor = klass.__dict__["as_"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::usedeclaration_has_module():
    assert hasattr(frontend::core::UseDeclaration, "module")
    descriptor = None
    for klass in frontend::core::UseDeclaration.__mro__:
        if "module" in klass.__dict__:
            descriptor = klass.__dict__["module"]
            break
    assert isinstance(descriptor, property)



def test_frontend::core::requiredeclaration_is_not_abstract():
    assert not inspect.isabstract(frontend::core::RequireDeclaration)


def test_frontend::core::requiredeclaration_constructor_exists():
    assert callable(frontend::core::RequireDeclaration.__init__)


def test_frontend::core::requiredeclaration_constructor_args():
    sig = inspect.signature(frontend::core::RequireDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"

def test_frontend::core::requiredeclaration_has_name():
    assert hasattr(frontend::core::RequireDeclaration, "name")
    descriptor = None
    for klass in frontend::core::RequireDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_frontend::core::requiredeclaration_has_default():
    assert hasattr(frontend::core::RequireDeclaration, "default")
    descriptor = None
    for klass in frontend::core::RequireDeclaration.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_availabletransformation_is_not_abstract():
    assert not inspect.isabstract(AvailableTransformation)


def test_availabletransformation_constructor_exists():
    assert callable(AvailableTransformation.__init__)


def test_availabletransformation_constructor_args():
    sig = inspect.signature(AvailableTransformation.__init__)
    params = list(sig.parameters.keys())



def test_frontend::chain::transformationexecution_is_not_abstract():
    assert not inspect.isabstract(frontend::chain::TransformationExecution)


def test_frontend::chain::transformationexecution_constructor_exists():
    assert callable(frontend::chain::TransformationExecution.__init__)


def test_frontend::chain::transformationexecution_constructor_args():
    sig = inspect.signature(frontend::chain::TransformationExecution.__init__)
    params = list(sig.parameters.keys())



def test_delegate_is_not_abstract():
    assert not inspect.isabstract(Delegate)


def test_delegate_constructor_exists():
    assert callable(Delegate.__init__)


def test_delegate_constructor_args():
    sig = inspect.signature(Delegate.__init__)
    params = list(sig.parameters.keys())



def test_frontend::mappings::mappingtransformation_is_not_abstract():
    assert not inspect.isabstract(frontend::mappings::MappingTransformation)


def test_frontend::mappings::mappingtransformation_constructor_exists():
    assert callable(frontend::mappings::MappingTransformation.__init__)


def test_frontend::mappings::mappingtransformation_constructor_args():
    sig = inspect.signature(frontend::mappings::MappingTransformation.__init__)
    params = list(sig.parameters.keys())



def test_preference_is_not_abstract():
    assert not inspect.isabstract(PReference)


def test_preference_constructor_exists():
    assert callable(PReference.__init__)


def test_preference_constructor_args():
    sig = inspect.signature(PReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend::patterns::collectionreference_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::CollectionReference)


def test_frontend::patterns::collectionreference_constructor_exists():
    assert callable(frontend::patterns::CollectionReference.__init__)


def test_frontend::patterns::collectionreference_constructor_args():
    sig = inspect.signature(frontend::patterns::CollectionReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend::patterns::preference_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::PReference)


def test_frontend::patterns::preference_constructor_exists():
    assert callable(frontend::patterns::PReference.__init__)


def test_frontend::patterns::preference_constructor_args():
    sig = inspect.signature(frontend::patterns::PReference.__init__)
    params = list(sig.parameters.keys())



def test_frontend::patterns::pattribute_is_not_abstract():
    assert not inspect.isabstract(frontend::patterns::PAttribute)


def test_frontend::patterns::pattribute_constructor_exists():
    assert callable(frontend::patterns::PAttribute.__init__)


def test_frontend::patterns::pattribute_constructor_args():
    sig = inspect.signature(frontend::patterns::PAttribute.__init__)
    params = list(sig.parameters.keys())

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

def test_mappingcardinality_exists():
    # Check that the Enumeration exists
    assert MappingCardinality is not None

def test_mappingcardinality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MappingCardinality]
    expected_literals = [
        "NToOne",
        "OneToOne",
        "OneToN",
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
        "ADD",
        "SUB",
        "EQUAL",
        "MUL",
        "DIV",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOp"


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
frontend::core::PutTraceParameter_strategy = st.builds(
    frontend::core::PutTraceParameter,
)
PutTraceParameter_strategy = st.builds(
    PutTraceParameter,
)
InlineFeature_strategy = st.builds(
    InlineFeature,
)
InlineClass_strategy = st.builds(
    InlineClass,
)
core::ModuleDefinition_strategy = st.builds(
    core::ModuleDefinition,
)
TraceElement_strategy = st.builds(
    TraceElement,
)
frontend::core::TypedWithClass_strategy = st.builds(
    frontend::core::TypedWithClass,
)
TraceDefinition_strategy = st.builds(
    TraceDefinition,
)
frontend::core::TraceCompareExpression_strategy = st.builds(
    frontend::core::TraceCompareExpression,
    multivaluedTag=
        st.booleans()
)
TraceCompareExpression_strategy = st.builds(
    TraceCompareExpression,
)
frontend::core::InlineReference_strategy = st.builds(
    frontend::core::InlineReference,
)
frontend::core::InlineAttribute_strategy = st.builds(
    frontend::core::InlineAttribute,
)
frontend::core::IfBranch_strategy = st.builds(
    frontend::core::IfBranch,
)
IfBranch_strategy = st.builds(
    IfBranch,
)
core::ImplicitlyAnnotableElement_strategy = st.builds(
    core::ImplicitlyAnnotableElement,
)
core::TypeExpression_strategy = st.builds(
    core::TypeExpression,
)
frontend::core::ClassUse_strategy = st.builds(
    frontend::core::ClassUse,
    className=
        safe_text,
    strictType=
        st.booleans()
)
frontend::core::TypeExpression_strategy = st.builds(
    frontend::core::TypeExpression,
)
frontend::core::KeywordParameter_strategy = st.builds(
    frontend::core::KeywordParameter,
    keyword=
        safe_text
)
KeywordParameter_strategy = st.builds(
    KeywordParameter,
)
core::Expression_strategy = st.builds(
    core::Expression,
)
ClosureParameter_strategy = st.builds(
    ClosureParameter,
)
frontend::core::Variable_strategy = st.builds(
    frontend::core::Variable,
    name=
        safe_text
)
frontend::core::RequireParameter_strategy = st.builds(
    frontend::core::RequireParameter,
    formalParameterName=
        safe_text
)
RequireParameter_strategy = st.builds(
    RequireParameter,
)
frontend::core::RequireModelParameter_strategy = st.builds(
    frontend::core::RequireModelParameter,
)
core::DefinitionParameter_strategy = st.builds(
    core::DefinitionParameter,
)
PFeature_strategy = st.builds(
    PFeature,
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
frontend::core::ClosureParameter_strategy = st.builds(
    frontend::core::ClosureParameter,
)
frontend::attribution::RuleSelf_strategy = st.builds(
    frontend::attribution::RuleSelf,
)
Expression_strategy = st.builds(
    Expression,
)
frontend::core::StringLiteral_strategy = st.builds(
    frontend::core::StringLiteral,
    value=
        safe_text
)
frontend::core::KeywordMethodCall_strategy = st.builds(
    frontend::core::KeywordMethodCall,
)
frontend::core::MethodCall_strategy = st.builds(
    frontend::core::MethodCall,
    withParameters=
        st.booleans(),
    methodName=
        safe_text
)
frontend::core::IfExpr_strategy = st.builds(
    frontend::core::IfExpr,
)
frontend::core::PutTrace_strategy = st.builds(
    frontend::core::PutTrace,
)
frontend::core::ResolveLink_strategy = st.builds(
    frontend::core::ResolveLink,
    linkName=
        safe_text,
    featureName=
        safe_text,
    isExternal=
        safe_text
)
frontend::core::BinaryExpr_strategy = st.builds(
    frontend::core::BinaryExpr,
    binaryOp=
        safe_text
)
frontend::core::DoubleLiteral_strategy = st.builds(
    frontend::core::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
frontend::core::NumLiteral_strategy = st.builds(
    frontend::core::NumLiteral,
    value=
        st.integers()
)
frontend::core::BooleanLiteral_strategy = st.builds(
    frontend::core::BooleanLiteral,
    value=
        st.booleans()
)
frontend::core::VariableReference_strategy = st.builds(
    frontend::core::VariableReference,
)
frontend::core::MatchTrace_strategy = st.builds(
    frontend::core::MatchTrace,
    cardinality=
        safe_text
)
frontend::core::ClosureDeclaration_strategy = st.builds(
    frontend::core::ClosureDeclaration,
)
frontend::attribution::AttributeUse_strategy = st.builds(
    frontend::attribution::AttributeUse,
)
RuleSelf_strategy = st.builds(
    RuleSelf,
)
core::RepresentModel_strategy = st.builds(
    core::RepresentModel,
)
frontend::core::InlineModel_strategy = st.builds(
    frontend::core::InlineModel,
)
frontend::core::TracedModelParameter_strategy = st.builds(
    frontend::core::TracedModelParameter,
)
frontend::core::TransformationDefinitionParameter_strategy = st.builds(
    frontend::core::TransformationDefinitionParameter,
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
frontend::imperative::MethodParameter_strategy = st.builds(
    frontend::imperative::MethodParameter,
)
frontend::imperative::MethodSelf_strategy = st.builds(
    frontend::imperative::MethodSelf,
)
Matcher_strategy = st.builds(
    Matcher,
)
core::NamedElement_strategy = st.builds(
    core::NamedElement,
)
frontend::chain::GeneratedModel_strategy = st.builds(
    frontend::chain::GeneratedModel,
)
frontend::core::ImportedModel_strategy = st.builds(
    frontend::core::ImportedModel,
)
core::LocatedElement_strategy = st.builds(
    core::LocatedElement,
)
frontend::koan::KoanRule_strategy = st.builds(
    frontend::koan::KoanRule,
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
frontend::attribution::AttributeInit_strategy = st.builds(
    frontend::attribution::AttributeInit,
)
TransformationDefinition_strategy = st.builds(
    TransformationDefinition,
)
frontend::core::EclecticTransformationDefinition_strategy = st.builds(
    frontend::core::EclecticTransformationDefinition,
)
frontend::chain::ChainTransformation_strategy = st.builds(
    frontend::chain::ChainTransformation,
)
frontend::imperative::ImperativeTransformation_strategy = st.builds(
    frontend::imperative::ImperativeTransformation,
)
frontend::koan::KoanTransformation_strategy = st.builds(
    frontend::koan::KoanTransformation,
)
frontend::script::ScriptedTransformation_strategy = st.builds(
    frontend::script::ScriptedTransformation,
)
frontend::DummyRootMetaclass_strategy = st.builds(
    frontend::DummyRootMetaclass,
)
core::TypedWithClass_strategy = st.builds(
    core::TypedWithClass,
)
AttributionRule_strategy = st.builds(
    AttributionRule,
)
AttributeDcl_strategy = st.builds(
    AttributeDcl,
)
frontend::attribution::InheritedAttributeDcl_strategy = st.builds(
    frontend::attribution::InheritedAttributeDcl,
)
frontend::attribution::SynthesizedAttributeDcl_strategy = st.builds(
    frontend::attribution::SynthesizedAttributeDcl,
)
frontend::attribution::AttributionTransformation_strategy = st.builds(
    frontend::attribution::AttributionTransformation,
)
ClassUse_strategy = st.builds(
    ClassUse,
)
core::Variable_strategy = st.builds(
    core::Variable,
)
frontend::attribution::AttributeDcl_strategy = st.builds(
    frontend::attribution::AttributeDcl,
)
koan::Matcher_strategy = st.builds(
    koan::Matcher,
)
frontend::koan::ForAllMatcher_strategy = st.builds(
    frontend::koan::ForAllMatcher,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
frontend::imperative::MethodDefinition_strategy = st.builds(
    frontend::imperative::MethodDefinition,
    name=
        safe_text
)
frontend::attribution::AttributionRule_strategy = st.builds(
    frontend::attribution::AttributionRule,
)
frontend::patterns::PFeature_strategy = st.builds(
    frontend::patterns::PFeature,
    name=
        safe_text
)
frontend::koan::Matcher_strategy = st.builds(
    frontend::koan::Matcher,
)
RequireDeclaration_strategy = st.builds(
    RequireDeclaration,
)
InlineModel_strategy = st.builds(
    InlineModel,
)
frontend::core::PropertyWrite_strategy = st.builds(
    frontend::core::PropertyWrite,
    _property=
        safe_text
)
frontend::core::Expression_strategy = st.builds(
    frontend::core::Expression,
)
frontend::core::Statement_strategy = st.builds(
    frontend::core::Statement,
)
AnnotableElement_strategy = st.builds(
    AnnotableElement,
)
frontend::core::Annotation_strategy = st.builds(
    frontend::core::Annotation,
)
SingleAnnotation_strategy = st.builds(
    SingleAnnotation,
)
frontend::core::ImplicitlyAnnotableElement_strategy = st.builds(
    frontend::core::ImplicitlyAnnotableElement,
)
Annotation_strategy = st.builds(
    Annotation,
)
frontend::core::OptimizationsAnnotation_strategy = st.builds(
    frontend::core::OptimizationsAnnotation,
    enabled=
        st.booleans()
)
frontend::core::MetamodelModelAnnotation_strategy = st.builds(
    frontend::core::MetamodelModelAnnotation,
    metamodel=
        safe_text
)
frontend::core::AnnotableElement_strategy = st.builds(
    frontend::core::AnnotableElement,
)
core::AnnotableElement_strategy = st.builds(
    core::AnnotableElement,
)
frontend::core::ModuleDefinition_strategy = st.builds(
    frontend::core::ModuleDefinition,
)
DefinitionParameter_strategy = st.builds(
    DefinitionParameter,
)
frontend::core::ModuleParameter_strategy = st.builds(
    frontend::core::ModuleParameter,
)
frontend::core::NamedElement_strategy = st.builds(
    frontend::core::NamedElement,
    name=
        safe_text
)
frontend::core::LocatedElement_strategy = st.builds(
    frontend::core::LocatedElement,
    row=
        st.integers(),
    column=
        st.integers(),
    file=
        safe_text
)
ImportedModel_strategy = st.builds(
    ImportedModel,
)
ModuleDefinition_strategy = st.builds(
    ModuleDefinition,
)
frontend::core::TraceInterface_strategy = st.builds(
    frontend::core::TraceInterface,
)
frontend::core::TransformationDefinition_strategy = st.builds(
    frontend::core::TransformationDefinition,
)
frontend::core::RepresentModel_strategy = st.builds(
    frontend::core::RepresentModel,
)
frontend::core::AnnotationParameter_strategy = st.builds(
    frontend::core::AnnotationParameter,
)
AnnotationParameter_strategy = st.builds(
    AnnotationParameter,
)
frontend::core::GenericAnnotation_strategy = st.builds(
    frontend::core::GenericAnnotation,
    name=
        safe_text
)
frontend::core::PotencyAnnotation_strategy = st.builds(
    frontend::core::PotencyAnnotation,
    value=
        safe_text
)
frontend::core::SingleAnnotation_strategy = st.builds(
    frontend::core::SingleAnnotation,
)
ObjectSourceVariable_strategy = st.builds(
    ObjectSourceVariable,
)
frontend::tao::SourceExpression_strategy = st.builds(
    frontend::tao::SourceExpression,
)
SourceExpression_strategy = st.builds(
    SourceExpression,
)
frontend::tao::WithOptionalVariableExpression_strategy = st.builds(
    frontend::tao::WithOptionalVariableExpression,
)
frontend::tao::Assignment_strategy = st.builds(
    frontend::tao::Assignment,
)
TemplateRootObject_strategy = st.builds(
    TemplateRootObject,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
frontend::tao::Template_strategy = st.builds(
    frontend::tao::Template,
)
ObjectInstantiation_strategy = st.builds(
    ObjectInstantiation,
)
frontend::tao::TemplateRootObject_strategy = st.builds(
    frontend::tao::TemplateRootObject,
)
Assignment_strategy = st.builds(
    Assignment,
)
frontend::tao::AttributeAssigment_strategy = st.builds(
    frontend::tao::AttributeAssigment,
    targetFeature=
        safe_text
)
ReferenceAssignment_strategy = st.builds(
    ReferenceAssignment,
)
frontend::tao::Invocation_strategy = st.builds(
    frontend::tao::Invocation,
)
frontend::tao::ObjectSyntax_strategy = st.builds(
    frontend::tao::ObjectSyntax,
)
tao::Assignment_strategy = st.builds(
    tao::Assignment,
)
frontend::tao::ReferenceAssignment_strategy = st.builds(
    frontend::tao::ReferenceAssignment,
    targetFeature=
        safe_text,
    multivalued=
        st.booleans()
)
frontend::tao::ObjectSourceVariable_strategy = st.builds(
    frontend::tao::ObjectSourceVariable,
)
frontend::facilities::CopierCallbackDefinition_strategy = st.builds(
    frontend::facilities::CopierCallbackDefinition,
    stop=
        st.booleans()
)
facilities::CopierCallbackDefinition_strategy = st.builds(
    facilities::CopierCallbackDefinition,
)
frontend::facilities::Copier_strategy = st.builds(
    frontend::facilities::Copier,
)
frontend::tao::TemplateParameter_strategy = st.builds(
    frontend::tao::TemplateParameter,
)
Template_strategy = st.builds(
    Template,
)
frontend::tao::TaoTransformation_strategy = st.builds(
    frontend::tao::TaoTransformation,
)
InvokeTransformation_strategy = st.builds(
    InvokeTransformation,
)
frontend::qool::InvokeExternal_strategy = st.builds(
    frontend::qool::InvokeExternal,
    traceAttributeName=
        safe_text,
    queueName=
        safe_text
)
NamedInvocationParameter_strategy = st.builds(
    NamedInvocationParameter,
)
InvocationParameter_strategy = st.builds(
    InvocationParameter,
)
frontend::qool::InvokeTransformation_strategy = st.builds(
    frontend::qool::InvokeTransformation,
    transformationName=
        safe_text,
    entryPointName=
        safe_text
)
frontend::qool::NamedInvocationParameter_strategy = st.builds(
    frontend::qool::NamedInvocationParameter,
    formalName=
        safe_text
)
TransformationDefinitionParameter_strategy = st.builds(
    TransformationDefinitionParameter,
)
frontend::qool::InvocationParameter_strategy = st.builds(
    frontend::qool::InvocationParameter,
    calleeModelName=
        safe_text
)
frontend::qool::InvokeInternal_strategy = st.builds(
    frontend::qool::InvokeInternal,
)
IteratorStatement_strategy = st.builds(
    IteratorStatement,
)
frontend::qool::ForEachStatement_strategy = st.builds(
    frontend::qool::ForEachStatement,
)
frontend::qool::ForAllStatement_strategy = st.builds(
    frontend::qool::ForAllStatement,
)
core::Statement_strategy = st.builds(
    core::Statement,
)
frontend::tao::ObjectInstantiation_strategy = st.builds(
    frontend::tao::ObjectInstantiation,
)
frontend::core::DefineVariable_strategy = st.builds(
    frontend::core::DefineVariable,
)
frontend::qool::IteratorStatement_strategy = st.builds(
    frontend::qool::IteratorStatement,
)
TypeExpression_strategy = st.builds(
    TypeExpression,
)
frontend::core::TraceUse_strategy = st.builds(
    frontend::core::TraceUse,
)
frontend::qool::QueueOptimization_strategy = st.builds(
    frontend::qool::QueueOptimization,
)
QueueOptimization_strategy = st.builds(
    QueueOptimization,
)
frontend::qool::AccessByFeatureOptimization_strategy = st.builds(
    frontend::qool::AccessByFeatureOptimization,
    featureName=
        safe_text,
    force=
        st.booleans()
)
frontend::qool::MatchPredicate_strategy = st.builds(
    frontend::qool::MatchPredicate,
)
MatchPredicate_strategy = st.builds(
    MatchPredicate,
)
frontend::qool::KindOfPredicate_strategy = st.builds(
    frontend::qool::KindOfPredicate,
)
frontend::qool::PropertyEqualsPredicate_strategy = st.builds(
    frontend::qool::PropertyEqualsPredicate,
    propertyName=
        safe_text
)
frontend::qool::MatchExpression_strategy = st.builds(
    frontend::qool::MatchExpression,
)
frontend::qool::EmitStatement_strategy = st.builds(
    frontend::qool::EmitStatement,
)
mappings::MetamodelElementRef_strategy = st.builds(
    mappings::MetamodelElementRef,
)
MetamodelElementRef_strategy = st.builds(
    MetamodelElementRef,
)
frontend::mappings::AttributeRef_strategy = st.builds(
    frontend::mappings::AttributeRef,
    featureName=
        safe_text,
    multivalued=
        st.booleans()
)
frontend::mappings::ClassRef_strategy = st.builds(
    frontend::mappings::ClassRef,
)
frontend::mappings::MetamodelElementRef_strategy = st.builds(
    frontend::mappings::MetamodelElementRef,
)
DefaultValue_strategy = st.builds(
    DefaultValue,
)
frontend::mappings::IntDefaultValue_strategy = st.builds(
    frontend::mappings::IntDefaultValue,
    defaultValue=
        safe_text
)
frontend::qool::QoolQueue_strategy = st.builds(
    frontend::qool::QoolQueue,
)
Segment_strategy = st.builds(
    Segment,
)
QoolQueue_strategy = st.builds(
    QoolQueue,
)
frontend::qool::ModelElementQueue_strategy = st.builds(
    frontend::qool::ModelElementQueue,
)
frontend::qool::LocalQueue_strategy = st.builds(
    frontend::qool::LocalQueue,
)
frontend::qool::QoolTransformation_strategy = st.builds(
    frontend::qool::QoolTransformation,
)
frontend::mappings::ReferenceRef_strategy = st.builds(
    frontend::mappings::ReferenceRef,
    multivalued=
        st.booleans(),
    featureName=
        safe_text
)
AttributeModifier_strategy = st.builds(
    AttributeModifier,
)
frontend::mappings::DefaultValue_strategy = st.builds(
    frontend::mappings::DefaultValue,
)
Class2Class_strategy = st.builds(
    Class2Class,
)
mappings::AttributeRightPart_strategy = st.builds(
    mappings::AttributeRightPart,
)
mappings::Feature2Feature_strategy = st.builds(
    mappings::Feature2Feature,
)
frontend::mappings::FeatureRef_strategy = st.builds(
    frontend::mappings::FeatureRef,
    multivalued=
        st.booleans(),
    featureName=
        safe_text
)
frontend::mappings::Attribute2Attribute_strategy = st.builds(
    frontend::mappings::Attribute2Attribute,
    cardinality=
        safe_text
)
Operator_strategy = st.builds(
    Operator,
)
frontend::mappings::Join_strategy = st.builds(
    frontend::mappings::Join,
)
frontend::mappings::Split_strategy = st.builds(
    frontend::mappings::Split,
)
frontend::mappings::Operator_strategy = st.builds(
    frontend::mappings::Operator,
)
frontend::mappings::ConvertModifier_strategy = st.builds(
    frontend::mappings::ConvertModifier,
    converter=
        safe_text
)
Modifier_strategy = st.builds(
    Modifier,
)
frontend::mappings::AttributeModifier_strategy = st.builds(
    frontend::mappings::AttributeModifier,
)
frontend::mappings::Modifier_strategy = st.builds(
    frontend::mappings::Modifier,
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
frontend::mappings::Class2Class_strategy = st.builds(
    frontend::mappings::Class2Class,
    cardinality=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
frontend::core::InlineFeature_strategy = st.builds(
    frontend::core::InlineFeature,
    multivalued=
        st.booleans()
)
frontend::core::TraceElement_strategy = st.builds(
    frontend::core::TraceElement,
)
frontend::core::DefinitionParameter_strategy = st.builds(
    frontend::core::DefinitionParameter,
)
frontend::core::TraceDefinition_strategy = st.builds(
    frontend::core::TraceDefinition,
)
frontend::core::InlineClass_strategy = st.builds(
    frontend::core::InlineClass,
)
frontend::qool::Segment_strategy = st.builds(
    frontend::qool::Segment,
)
frontend::mappings::Tag_strategy = st.builds(
    frontend::mappings::Tag,
)
frontend::mappings::Converter_strategy = st.builds(
    frontend::mappings::Converter,
    converterName=
        safe_text,
    isExternal=
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
frontend::mappings::RelatedBy_strategy = st.builds(
    frontend::mappings::RelatedBy,
)
frontend::mappings::LinkedBy_strategy = st.builds(
    frontend::mappings::LinkedBy,
)
frontend::mappings::EqualityFilter_strategy = st.builds(
    frontend::mappings::EqualityFilter,
    filter=
        safe_text
)
MappingElement_strategy = st.builds(
    MappingElement,
)
frontend::mappings::C2CModifier_strategy = st.builds(
    frontend::mappings::C2CModifier,
)
frontend::mappings::Context_strategy = st.builds(
    frontend::mappings::Context,
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
frontend::mappings::Delegate_strategy = st.builds(
    frontend::mappings::Delegate,
    featureName=
        safe_text,
    linkName=
        safe_text,
    isExternal=
        safe_text
)
mappings::MappingVariable_strategy = st.builds(
    mappings::MappingVariable,
)
core::ClassUse_strategy = st.builds(
    core::ClassUse,
)
frontend::core::ModelReference_strategy = st.builds(
    frontend::core::ModelReference,
)
frontend::mappings::MatchedElement_strategy = st.builds(
    frontend::mappings::MatchedElement,
)
frontend::mappings::MappingVariable_strategy = st.builds(
    frontend::mappings::MappingVariable,
)
Context_strategy = st.builds(
    Context,
)
frontend::mappings::AttributeRightPart_strategy = st.builds(
    frontend::mappings::AttributeRightPart,
)
AttributeRightPart_strategy = st.builds(
    AttributeRightPart,
)
frontend::mappings::AttributeIsResolveLink_strategy = st.builds(
    frontend::mappings::AttributeIsResolveLink,
)
frontend::mappings::AttributeIsString_strategy = st.builds(
    frontend::mappings::AttributeIsString,
    strValue=
        safe_text
)
frontend::mappings::AttributeIsInteger_strategy = st.builds(
    frontend::mappings::AttributeIsInteger,
    intValue=
        st.integers()
)
frontend::mappings::AttributeIsDouble_strategy = st.builds(
    frontend::mappings::AttributeIsDouble,
    doubleValue=
        safe_text
)
frontend::mappings::AttributeIsBoolean_strategy = st.builds(
    frontend::mappings::AttributeIsBoolean,
    boolValue=
        safe_text
)
AttributeRef_strategy = st.builds(
    AttributeRef,
)
Feature2Feature_strategy = st.builds(
    Feature2Feature,
)
frontend::mappings::Reference2Reference_strategy = st.builds(
    frontend::mappings::Reference2Reference,
    resolverName=
        safe_text,
    cardinality=
        safe_text
)
frontend::mappings::AttributeMapping_strategy = st.builds(
    frontend::mappings::AttributeMapping,
)
Converter_strategy = st.builds(
    Converter,
)
FeatureRef_strategy = st.builds(
    FeatureRef,
)
frontend::mappings::Feature2Feature_strategy = st.builds(
    frontend::mappings::Feature2Feature,
)
frontend::mappings::ClassMapping_strategy = st.builds(
    frontend::mappings::ClassMapping,
)
frontend::mappings::MappingElement_strategy = st.builds(
    frontend::mappings::MappingElement,
)
frontend::mappings::Section_strategy = st.builds(
    frontend::mappings::Section,
    sectionType=
        safe_text
)
frontend::patterns::PObject_strategy = st.builds(
    frontend::patterns::PObject,
)
frontend::patterns::POutputVariable_strategy = st.builds(
    frontend::patterns::POutputVariable,
)
POutputVariable_strategy = st.builds(
    POutputVariable,
)
PObject_strategy = st.builds(
    PObject,
)
frontend::patterns::Pattern_strategy = st.builds(
    frontend::patterns::Pattern,
    name=
        safe_text
)
Pattern_strategy = st.builds(
    Pattern,
)
frontend::patterns::PatternSpecification_strategy = st.builds(
    frontend::patterns::PatternSpecification,
)
core::TransformationDefinition_strategy = st.builds(
    core::TransformationDefinition,
)
chain::AvailableTransformation_strategy = st.builds(
    chain::AvailableTransformation,
)
frontend::chain::CompositeTransformation_strategy = st.builds(
    frontend::chain::CompositeTransformation,
)
frontend::chain::ExternalTransformation_strategy = st.builds(
    frontend::chain::ExternalTransformation,
)
frontend::chain::AvailableTransformation_strategy = st.builds(
    frontend::chain::AvailableTransformation,
)
RepresentModel_strategy = st.builds(
    RepresentModel,
)
frontend::core::UseDeclaration_strategy = st.builds(
    frontend::core::UseDeclaration,
    as_=
        safe_text,
    module=
        safe_text
)
frontend::core::RequireDeclaration_strategy = st.builds(
    frontend::core::RequireDeclaration,
    name=
        safe_text,
    default=
        safe_text
)
AvailableTransformation_strategy = st.builds(
    AvailableTransformation,
)
frontend::chain::TransformationExecution_strategy = st.builds(
    frontend::chain::TransformationExecution,
)
Delegate_strategy = st.builds(
    Delegate,
)
frontend::mappings::MappingTransformation_strategy = st.builds(
    frontend::mappings::MappingTransformation,
)
PReference_strategy = st.builds(
    PReference,
)
frontend::patterns::CollectionReference_strategy = st.builds(
    frontend::patterns::CollectionReference,
)
frontend::patterns::PReference_strategy = st.builds(
    frontend::patterns::PReference,
)
frontend::patterns::PAttribute_strategy = st.builds(
    frontend::patterns::PAttribute,
)

@given(instance=frontend::core::PutTraceParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::puttraceparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::PutTraceParameter)

@given(instance=PutTraceParameter_strategy)
@settings(max_examples=50)
def test_puttraceparameter_instantiation(instance):
    assert isinstance(instance, PutTraceParameter)

@given(instance=InlineFeature_strategy)
@settings(max_examples=50)
def test_inlinefeature_instantiation(instance):
    assert isinstance(instance, InlineFeature)

@given(instance=InlineClass_strategy)
@settings(max_examples=50)
def test_inlineclass_instantiation(instance):
    assert isinstance(instance, InlineClass)

@given(instance=core::ModuleDefinition_strategy)
@settings(max_examples=50)
def test_core::moduledefinition_instantiation(instance):
    assert isinstance(instance, core::ModuleDefinition)

@given(instance=TraceElement_strategy)
@settings(max_examples=50)
def test_traceelement_instantiation(instance):
    assert isinstance(instance, TraceElement)

@given(instance=frontend::core::TypedWithClass_strategy)
@settings(max_examples=50)
def test_frontend::core::typedwithclass_instantiation(instance):
    assert isinstance(instance, frontend::core::TypedWithClass)

@given(instance=TraceDefinition_strategy)
@settings(max_examples=50)
def test_tracedefinition_instantiation(instance):
    assert isinstance(instance, TraceDefinition)

@given(instance=frontend::core::TraceCompareExpression_strategy)
@settings(max_examples=50)
def test_frontend::core::tracecompareexpression_instantiation(instance):
    assert isinstance(instance, frontend::core::TraceCompareExpression)

@given(instance=frontend::core::TraceCompareExpression_strategy)
def test_frontend::core::tracecompareexpression_multivaluedTag_type(instance):
    assert isinstance(instance.multivaluedTag, bool)


@given(instance=frontend::core::TraceCompareExpression_strategy)
def test_frontend::core::tracecompareexpression_multivaluedTag_setter(instance):
    original = instance.multivaluedTag
    instance.multivaluedTag = original
    assert instance.multivaluedTag == original

@given(instance=TraceCompareExpression_strategy)
@settings(max_examples=50)
def test_tracecompareexpression_instantiation(instance):
    assert isinstance(instance, TraceCompareExpression)

@given(instance=frontend::core::InlineReference_strategy)
@settings(max_examples=50)
def test_frontend::core::inlinereference_instantiation(instance):
    assert isinstance(instance, frontend::core::InlineReference)

@given(instance=frontend::core::InlineAttribute_strategy)
@settings(max_examples=50)
def test_frontend::core::inlineattribute_instantiation(instance):
    assert isinstance(instance, frontend::core::InlineAttribute)

@given(instance=frontend::core::IfBranch_strategy)
@settings(max_examples=50)
def test_frontend::core::ifbranch_instantiation(instance):
    assert isinstance(instance, frontend::core::IfBranch)

@given(instance=IfBranch_strategy)
@settings(max_examples=50)
def test_ifbranch_instantiation(instance):
    assert isinstance(instance, IfBranch)

@given(instance=core::ImplicitlyAnnotableElement_strategy)
@settings(max_examples=50)
def test_core::implicitlyannotableelement_instantiation(instance):
    assert isinstance(instance, core::ImplicitlyAnnotableElement)

@given(instance=core::TypeExpression_strategy)
@settings(max_examples=50)
def test_core::typeexpression_instantiation(instance):
    assert isinstance(instance, core::TypeExpression)

@given(instance=frontend::core::ClassUse_strategy)
@settings(max_examples=50)
def test_frontend::core::classuse_instantiation(instance):
    assert isinstance(instance, frontend::core::ClassUse)

@given(instance=frontend::core::ClassUse_strategy)
def test_frontend::core::classuse_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=frontend::core::ClassUse_strategy)
def test_frontend::core::classuse_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=frontend::core::ClassUse_strategy)
def test_frontend::core::classuse_strictType_type(instance):
    assert isinstance(instance.strictType, bool)


@given(instance=frontend::core::ClassUse_strategy)
def test_frontend::core::classuse_strictType_setter(instance):
    original = instance.strictType
    instance.strictType = original
    assert instance.strictType == original

@given(instance=frontend::core::TypeExpression_strategy)
@settings(max_examples=50)
def test_frontend::core::typeexpression_instantiation(instance):
    assert isinstance(instance, frontend::core::TypeExpression)

@given(instance=frontend::core::KeywordParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::keywordparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::KeywordParameter)

@given(instance=frontend::core::KeywordParameter_strategy)
def test_frontend::core::keywordparameter_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=frontend::core::KeywordParameter_strategy)
def test_frontend::core::keywordparameter_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=KeywordParameter_strategy)
@settings(max_examples=50)
def test_keywordparameter_instantiation(instance):
    assert isinstance(instance, KeywordParameter)

@given(instance=core::Expression_strategy)
@settings(max_examples=50)
def test_core::expression_instantiation(instance):
    assert isinstance(instance, core::Expression)

@given(instance=ClosureParameter_strategy)
@settings(max_examples=50)
def test_closureparameter_instantiation(instance):
    assert isinstance(instance, ClosureParameter)

@given(instance=frontend::core::Variable_strategy)
@settings(max_examples=50)
def test_frontend::core::variable_instantiation(instance):
    assert isinstance(instance, frontend::core::Variable)

@given(instance=frontend::core::Variable_strategy)
def test_frontend::core::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=frontend::core::Variable_strategy)
def test_frontend::core::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend::core::RequireParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::requireparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::RequireParameter)

@given(instance=frontend::core::RequireParameter_strategy)
def test_frontend::core::requireparameter_formalParameterName_type(instance):
    assert isinstance(instance.formalParameterName, str)


@given(instance=frontend::core::RequireParameter_strategy)
def test_frontend::core::requireparameter_formalParameterName_setter(instance):
    original = instance.formalParameterName
    instance.formalParameterName = original
    assert instance.formalParameterName == original

@given(instance=RequireParameter_strategy)
@settings(max_examples=50)
def test_requireparameter_instantiation(instance):
    assert isinstance(instance, RequireParameter)

@given(instance=frontend::core::RequireModelParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::requiremodelparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::RequireModelParameter)

@given(instance=core::DefinitionParameter_strategy)
@settings(max_examples=50)
def test_core::definitionparameter_instantiation(instance):
    assert isinstance(instance, core::DefinitionParameter)

@given(instance=PFeature_strategy)
@settings(max_examples=50)
def test_pfeature_instantiation(instance):
    assert isinstance(instance, PFeature)

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

@given(instance=frontend::core::ClosureParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::closureparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::ClosureParameter)

@given(instance=frontend::attribution::RuleSelf_strategy)
@settings(max_examples=50)
def test_frontend::attribution::ruleself_instantiation(instance):
    assert isinstance(instance, frontend::attribution::RuleSelf)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=frontend::core::StringLiteral_strategy)
@settings(max_examples=50)
def test_frontend::core::stringliteral_instantiation(instance):
    assert isinstance(instance, frontend::core::StringLiteral)

@given(instance=frontend::core::StringLiteral_strategy)
def test_frontend::core::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=frontend::core::StringLiteral_strategy)
def test_frontend::core::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend::core::KeywordMethodCall_strategy)
@settings(max_examples=50)
def test_frontend::core::keywordmethodcall_instantiation(instance):
    assert isinstance(instance, frontend::core::KeywordMethodCall)

@given(instance=frontend::core::MethodCall_strategy)
@settings(max_examples=50)
def test_frontend::core::methodcall_instantiation(instance):
    assert isinstance(instance, frontend::core::MethodCall)

@given(instance=frontend::core::MethodCall_strategy)
def test_frontend::core::methodcall_withParameters_type(instance):
    assert isinstance(instance.withParameters, bool)


@given(instance=frontend::core::MethodCall_strategy)
def test_frontend::core::methodcall_withParameters_setter(instance):
    original = instance.withParameters
    instance.withParameters = original
    assert instance.withParameters == original

@given(instance=frontend::core::MethodCall_strategy)
def test_frontend::core::methodcall_methodName_type(instance):
    assert isinstance(instance.methodName, str)


@given(instance=frontend::core::MethodCall_strategy)
def test_frontend::core::methodcall_methodName_setter(instance):
    original = instance.methodName
    instance.methodName = original
    assert instance.methodName == original

@given(instance=frontend::core::IfExpr_strategy)
@settings(max_examples=50)
def test_frontend::core::ifexpr_instantiation(instance):
    assert isinstance(instance, frontend::core::IfExpr)

@given(instance=frontend::core::PutTrace_strategy)
@settings(max_examples=50)
def test_frontend::core::puttrace_instantiation(instance):
    assert isinstance(instance, frontend::core::PutTrace)

@given(instance=frontend::core::ResolveLink_strategy)
@settings(max_examples=50)
def test_frontend::core::resolvelink_instantiation(instance):
    assert isinstance(instance, frontend::core::ResolveLink)

@given(instance=frontend::core::ResolveLink_strategy)
def test_frontend::core::resolvelink_linkName_type(instance):
    assert isinstance(instance.linkName, str)


@given(instance=frontend::core::ResolveLink_strategy)
def test_frontend::core::resolvelink_linkName_setter(instance):
    original = instance.linkName
    instance.linkName = original
    assert instance.linkName == original

@given(instance=frontend::core::ResolveLink_strategy)
def test_frontend::core::resolvelink_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=frontend::core::ResolveLink_strategy)
def test_frontend::core::resolvelink_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=frontend::core::ResolveLink_strategy)
def test_frontend::core::resolvelink_isExternal_type(instance):
    assert isinstance(instance.isExternal, str)


@given(instance=frontend::core::ResolveLink_strategy)
def test_frontend::core::resolvelink_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=frontend::core::BinaryExpr_strategy)
@settings(max_examples=50)
def test_frontend::core::binaryexpr_instantiation(instance):
    assert isinstance(instance, frontend::core::BinaryExpr)

@given(instance=frontend::core::BinaryExpr_strategy)
def test_frontend::core::binaryexpr_binaryOp_type(instance):
    assert isinstance(instance.binaryOp, str)


@given(instance=frontend::core::BinaryExpr_strategy)
def test_frontend::core::binaryexpr_binaryOp_setter(instance):
    original = instance.binaryOp
    instance.binaryOp = original
    assert instance.binaryOp == original

@given(instance=frontend::core::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_frontend::core::doubleliteral_instantiation(instance):
    assert isinstance(instance, frontend::core::DoubleLiteral)

@given(instance=frontend::core::DoubleLiteral_strategy)
def test_frontend::core::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=frontend::core::DoubleLiteral_strategy)
def test_frontend::core::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend::core::NumLiteral_strategy)
@settings(max_examples=50)
def test_frontend::core::numliteral_instantiation(instance):
    assert isinstance(instance, frontend::core::NumLiteral)

@given(instance=frontend::core::NumLiteral_strategy)
def test_frontend::core::numliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=frontend::core::NumLiteral_strategy)
def test_frontend::core::numliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend::core::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_frontend::core::booleanliteral_instantiation(instance):
    assert isinstance(instance, frontend::core::BooleanLiteral)

@given(instance=frontend::core::BooleanLiteral_strategy)
def test_frontend::core::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=frontend::core::BooleanLiteral_strategy)
def test_frontend::core::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend::core::VariableReference_strategy)
@settings(max_examples=50)
def test_frontend::core::variablereference_instantiation(instance):
    assert isinstance(instance, frontend::core::VariableReference)

@given(instance=frontend::core::MatchTrace_strategy)
@settings(max_examples=50)
def test_frontend::core::matchtrace_instantiation(instance):
    assert isinstance(instance, frontend::core::MatchTrace)

@given(instance=frontend::core::MatchTrace_strategy)
def test_frontend::core::matchtrace_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=frontend::core::MatchTrace_strategy)
def test_frontend::core::matchtrace_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=frontend::core::ClosureDeclaration_strategy)
@settings(max_examples=50)
def test_frontend::core::closuredeclaration_instantiation(instance):
    assert isinstance(instance, frontend::core::ClosureDeclaration)

@given(instance=frontend::attribution::AttributeUse_strategy)
@settings(max_examples=50)
def test_frontend::attribution::attributeuse_instantiation(instance):
    assert isinstance(instance, frontend::attribution::AttributeUse)

@given(instance=RuleSelf_strategy)
@settings(max_examples=50)
def test_ruleself_instantiation(instance):
    assert isinstance(instance, RuleSelf)

@given(instance=core::RepresentModel_strategy)
@settings(max_examples=50)
def test_core::representmodel_instantiation(instance):
    assert isinstance(instance, core::RepresentModel)

@given(instance=frontend::core::InlineModel_strategy)
@settings(max_examples=50)
def test_frontend::core::inlinemodel_instantiation(instance):
    assert isinstance(instance, frontend::core::InlineModel)

@given(instance=frontend::core::TracedModelParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::tracedmodelparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::TracedModelParameter)

@given(instance=frontend::core::TransformationDefinitionParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::transformationdefinitionparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::TransformationDefinitionParameter)

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

@given(instance=frontend::imperative::MethodParameter_strategy)
@settings(max_examples=50)
def test_frontend::imperative::methodparameter_instantiation(instance):
    assert isinstance(instance, frontend::imperative::MethodParameter)

@given(instance=frontend::imperative::MethodSelf_strategy)
@settings(max_examples=50)
def test_frontend::imperative::methodself_instantiation(instance):
    assert isinstance(instance, frontend::imperative::MethodSelf)

@given(instance=Matcher_strategy)
@settings(max_examples=50)
def test_matcher_instantiation(instance):
    assert isinstance(instance, Matcher)

@given(instance=core::NamedElement_strategy)
@settings(max_examples=50)
def test_core::namedelement_instantiation(instance):
    assert isinstance(instance, core::NamedElement)

@given(instance=frontend::chain::GeneratedModel_strategy)
@settings(max_examples=50)
def test_frontend::chain::generatedmodel_instantiation(instance):
    assert isinstance(instance, frontend::chain::GeneratedModel)

@given(instance=frontend::core::ImportedModel_strategy)
@settings(max_examples=50)
def test_frontend::core::importedmodel_instantiation(instance):
    assert isinstance(instance, frontend::core::ImportedModel)

@given(instance=core::LocatedElement_strategy)
@settings(max_examples=50)
def test_core::locatedelement_instantiation(instance):
    assert isinstance(instance, core::LocatedElement)

@given(instance=frontend::koan::KoanRule_strategy)
@settings(max_examples=50)
def test_frontend::koan::koanrule_instantiation(instance):
    assert isinstance(instance, frontend::koan::KoanRule)

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

@given(instance=frontend::attribution::AttributeInit_strategy)
@settings(max_examples=50)
def test_frontend::attribution::attributeinit_instantiation(instance):
    assert isinstance(instance, frontend::attribution::AttributeInit)

@given(instance=TransformationDefinition_strategy)
@settings(max_examples=50)
def test_transformationdefinition_instantiation(instance):
    assert isinstance(instance, TransformationDefinition)

@given(instance=frontend::core::EclecticTransformationDefinition_strategy)
@settings(max_examples=50)
def test_frontend::core::eclectictransformationdefinition_instantiation(instance):
    assert isinstance(instance, frontend::core::EclecticTransformationDefinition)

@given(instance=frontend::chain::ChainTransformation_strategy)
@settings(max_examples=50)
def test_frontend::chain::chaintransformation_instantiation(instance):
    assert isinstance(instance, frontend::chain::ChainTransformation)

@given(instance=frontend::imperative::ImperativeTransformation_strategy)
@settings(max_examples=50)
def test_frontend::imperative::imperativetransformation_instantiation(instance):
    assert isinstance(instance, frontend::imperative::ImperativeTransformation)

@given(instance=frontend::koan::KoanTransformation_strategy)
@settings(max_examples=50)
def test_frontend::koan::koantransformation_instantiation(instance):
    assert isinstance(instance, frontend::koan::KoanTransformation)

@given(instance=frontend::script::ScriptedTransformation_strategy)
@settings(max_examples=50)
def test_frontend::script::scriptedtransformation_instantiation(instance):
    assert isinstance(instance, frontend::script::ScriptedTransformation)

@given(instance=frontend::DummyRootMetaclass_strategy)
@settings(max_examples=50)
def test_frontend::dummyrootmetaclass_instantiation(instance):
    assert isinstance(instance, frontend::DummyRootMetaclass)

@given(instance=core::TypedWithClass_strategy)
@settings(max_examples=50)
def test_core::typedwithclass_instantiation(instance):
    assert isinstance(instance, core::TypedWithClass)

@given(instance=AttributionRule_strategy)
@settings(max_examples=50)
def test_attributionrule_instantiation(instance):
    assert isinstance(instance, AttributionRule)

@given(instance=AttributeDcl_strategy)
@settings(max_examples=50)
def test_attributedcl_instantiation(instance):
    assert isinstance(instance, AttributeDcl)

@given(instance=frontend::attribution::InheritedAttributeDcl_strategy)
@settings(max_examples=50)
def test_frontend::attribution::inheritedattributedcl_instantiation(instance):
    assert isinstance(instance, frontend::attribution::InheritedAttributeDcl)

@given(instance=frontend::attribution::SynthesizedAttributeDcl_strategy)
@settings(max_examples=50)
def test_frontend::attribution::synthesizedattributedcl_instantiation(instance):
    assert isinstance(instance, frontend::attribution::SynthesizedAttributeDcl)

@given(instance=frontend::attribution::AttributionTransformation_strategy)
@settings(max_examples=50)
def test_frontend::attribution::attributiontransformation_instantiation(instance):
    assert isinstance(instance, frontend::attribution::AttributionTransformation)

@given(instance=ClassUse_strategy)
@settings(max_examples=50)
def test_classuse_instantiation(instance):
    assert isinstance(instance, ClassUse)

@given(instance=core::Variable_strategy)
@settings(max_examples=50)
def test_core::variable_instantiation(instance):
    assert isinstance(instance, core::Variable)

@given(instance=frontend::attribution::AttributeDcl_strategy)
@settings(max_examples=50)
def test_frontend::attribution::attributedcl_instantiation(instance):
    assert isinstance(instance, frontend::attribution::AttributeDcl)

@given(instance=koan::Matcher_strategy)
@settings(max_examples=50)
def test_koan::matcher_instantiation(instance):
    assert isinstance(instance, koan::Matcher)

@given(instance=frontend::koan::ForAllMatcher_strategy)
@settings(max_examples=50)
def test_frontend::koan::forallmatcher_instantiation(instance):
    assert isinstance(instance, frontend::koan::ForAllMatcher)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=frontend::imperative::MethodDefinition_strategy)
@settings(max_examples=50)
def test_frontend::imperative::methoddefinition_instantiation(instance):
    assert isinstance(instance, frontend::imperative::MethodDefinition)

@given(instance=frontend::imperative::MethodDefinition_strategy)
def test_frontend::imperative::methoddefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=frontend::imperative::MethodDefinition_strategy)
def test_frontend::imperative::methoddefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend::attribution::AttributionRule_strategy)
@settings(max_examples=50)
def test_frontend::attribution::attributionrule_instantiation(instance):
    assert isinstance(instance, frontend::attribution::AttributionRule)

@given(instance=frontend::patterns::PFeature_strategy)
@settings(max_examples=50)
def test_frontend::patterns::pfeature_instantiation(instance):
    assert isinstance(instance, frontend::patterns::PFeature)

@given(instance=frontend::patterns::PFeature_strategy)
def test_frontend::patterns::pfeature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=frontend::patterns::PFeature_strategy)
def test_frontend::patterns::pfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend::koan::Matcher_strategy)
@settings(max_examples=50)
def test_frontend::koan::matcher_instantiation(instance):
    assert isinstance(instance, frontend::koan::Matcher)

@given(instance=RequireDeclaration_strategy)
@settings(max_examples=50)
def test_requiredeclaration_instantiation(instance):
    assert isinstance(instance, RequireDeclaration)

@given(instance=InlineModel_strategy)
@settings(max_examples=50)
def test_inlinemodel_instantiation(instance):
    assert isinstance(instance, InlineModel)

@given(instance=frontend::core::PropertyWrite_strategy)
@settings(max_examples=50)
def test_frontend::core::propertywrite_instantiation(instance):
    assert isinstance(instance, frontend::core::PropertyWrite)

@given(instance=frontend::core::PropertyWrite_strategy)
def test_frontend::core::propertywrite__property_type(instance):
    assert isinstance(instance._property, str)


@given(instance=frontend::core::PropertyWrite_strategy)
def test_frontend::core::propertywrite__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original

@given(instance=frontend::core::Expression_strategy)
@settings(max_examples=50)
def test_frontend::core::expression_instantiation(instance):
    assert isinstance(instance, frontend::core::Expression)

@given(instance=frontend::core::Statement_strategy)
@settings(max_examples=50)
def test_frontend::core::statement_instantiation(instance):
    assert isinstance(instance, frontend::core::Statement)

@given(instance=AnnotableElement_strategy)
@settings(max_examples=50)
def test_annotableelement_instantiation(instance):
    assert isinstance(instance, AnnotableElement)

@given(instance=frontend::core::Annotation_strategy)
@settings(max_examples=50)
def test_frontend::core::annotation_instantiation(instance):
    assert isinstance(instance, frontend::core::Annotation)

@given(instance=SingleAnnotation_strategy)
@settings(max_examples=50)
def test_singleannotation_instantiation(instance):
    assert isinstance(instance, SingleAnnotation)

@given(instance=frontend::core::ImplicitlyAnnotableElement_strategy)
@settings(max_examples=50)
def test_frontend::core::implicitlyannotableelement_instantiation(instance):
    assert isinstance(instance, frontend::core::ImplicitlyAnnotableElement)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=frontend::core::OptimizationsAnnotation_strategy)
@settings(max_examples=50)
def test_frontend::core::optimizationsannotation_instantiation(instance):
    assert isinstance(instance, frontend::core::OptimizationsAnnotation)

@given(instance=frontend::core::OptimizationsAnnotation_strategy)
def test_frontend::core::optimizationsannotation_enabled_type(instance):
    assert isinstance(instance.enabled, bool)


@given(instance=frontend::core::OptimizationsAnnotation_strategy)
def test_frontend::core::optimizationsannotation_enabled_setter(instance):
    original = instance.enabled
    instance.enabled = original
    assert instance.enabled == original

@given(instance=frontend::core::MetamodelModelAnnotation_strategy)
@settings(max_examples=50)
def test_frontend::core::metamodelmodelannotation_instantiation(instance):
    assert isinstance(instance, frontend::core::MetamodelModelAnnotation)

@given(instance=frontend::core::MetamodelModelAnnotation_strategy)
def test_frontend::core::metamodelmodelannotation_metamodel_type(instance):
    assert isinstance(instance.metamodel, str)


@given(instance=frontend::core::MetamodelModelAnnotation_strategy)
def test_frontend::core::metamodelmodelannotation_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=frontend::core::AnnotableElement_strategy)
@settings(max_examples=50)
def test_frontend::core::annotableelement_instantiation(instance):
    assert isinstance(instance, frontend::core::AnnotableElement)

@given(instance=core::AnnotableElement_strategy)
@settings(max_examples=50)
def test_core::annotableelement_instantiation(instance):
    assert isinstance(instance, core::AnnotableElement)

@given(instance=frontend::core::ModuleDefinition_strategy)
@settings(max_examples=50)
def test_frontend::core::moduledefinition_instantiation(instance):
    assert isinstance(instance, frontend::core::ModuleDefinition)

@given(instance=DefinitionParameter_strategy)
@settings(max_examples=50)
def test_definitionparameter_instantiation(instance):
    assert isinstance(instance, DefinitionParameter)

@given(instance=frontend::core::ModuleParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::moduleparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::ModuleParameter)

@given(instance=frontend::core::NamedElement_strategy)
@settings(max_examples=50)
def test_frontend::core::namedelement_instantiation(instance):
    assert isinstance(instance, frontend::core::NamedElement)

@given(instance=frontend::core::NamedElement_strategy)
def test_frontend::core::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=frontend::core::NamedElement_strategy)
def test_frontend::core::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend::core::LocatedElement_strategy)
@settings(max_examples=50)
def test_frontend::core::locatedelement_instantiation(instance):
    assert isinstance(instance, frontend::core::LocatedElement)

@given(instance=frontend::core::LocatedElement_strategy)
def test_frontend::core::locatedelement_row_type(instance):
    assert isinstance(instance.row, int)


@given(instance=frontend::core::LocatedElement_strategy)
def test_frontend::core::locatedelement_row_setter(instance):
    original = instance.row
    instance.row = original
    assert instance.row == original

@given(instance=frontend::core::LocatedElement_strategy)
def test_frontend::core::locatedelement_column_type(instance):
    assert isinstance(instance.column, int)


@given(instance=frontend::core::LocatedElement_strategy)
def test_frontend::core::locatedelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=frontend::core::LocatedElement_strategy)
def test_frontend::core::locatedelement_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=frontend::core::LocatedElement_strategy)
def test_frontend::core::locatedelement_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=ImportedModel_strategy)
@settings(max_examples=50)
def test_importedmodel_instantiation(instance):
    assert isinstance(instance, ImportedModel)

@given(instance=ModuleDefinition_strategy)
@settings(max_examples=50)
def test_moduledefinition_instantiation(instance):
    assert isinstance(instance, ModuleDefinition)

@given(instance=frontend::core::TraceInterface_strategy)
@settings(max_examples=50)
def test_frontend::core::traceinterface_instantiation(instance):
    assert isinstance(instance, frontend::core::TraceInterface)

@given(instance=frontend::core::TransformationDefinition_strategy)
@settings(max_examples=50)
def test_frontend::core::transformationdefinition_instantiation(instance):
    assert isinstance(instance, frontend::core::TransformationDefinition)

@given(instance=frontend::core::RepresentModel_strategy)
@settings(max_examples=50)
def test_frontend::core::representmodel_instantiation(instance):
    assert isinstance(instance, frontend::core::RepresentModel)

@given(instance=frontend::core::AnnotationParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::annotationparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::AnnotationParameter)

@given(instance=AnnotationParameter_strategy)
@settings(max_examples=50)
def test_annotationparameter_instantiation(instance):
    assert isinstance(instance, AnnotationParameter)

@given(instance=frontend::core::GenericAnnotation_strategy)
@settings(max_examples=50)
def test_frontend::core::genericannotation_instantiation(instance):
    assert isinstance(instance, frontend::core::GenericAnnotation)

@given(instance=frontend::core::GenericAnnotation_strategy)
def test_frontend::core::genericannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=frontend::core::GenericAnnotation_strategy)
def test_frontend::core::genericannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend::core::PotencyAnnotation_strategy)
@settings(max_examples=50)
def test_frontend::core::potencyannotation_instantiation(instance):
    assert isinstance(instance, frontend::core::PotencyAnnotation)

@given(instance=frontend::core::PotencyAnnotation_strategy)
def test_frontend::core::potencyannotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=frontend::core::PotencyAnnotation_strategy)
def test_frontend::core::potencyannotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=frontend::core::SingleAnnotation_strategy)
@settings(max_examples=50)
def test_frontend::core::singleannotation_instantiation(instance):
    assert isinstance(instance, frontend::core::SingleAnnotation)

@given(instance=ObjectSourceVariable_strategy)
@settings(max_examples=50)
def test_objectsourcevariable_instantiation(instance):
    assert isinstance(instance, ObjectSourceVariable)

@given(instance=frontend::tao::SourceExpression_strategy)
@settings(max_examples=50)
def test_frontend::tao::sourceexpression_instantiation(instance):
    assert isinstance(instance, frontend::tao::SourceExpression)

@given(instance=SourceExpression_strategy)
@settings(max_examples=50)
def test_sourceexpression_instantiation(instance):
    assert isinstance(instance, SourceExpression)

@given(instance=frontend::tao::WithOptionalVariableExpression_strategy)
@settings(max_examples=50)
def test_frontend::tao::withoptionalvariableexpression_instantiation(instance):
    assert isinstance(instance, frontend::tao::WithOptionalVariableExpression)

@given(instance=frontend::tao::Assignment_strategy)
@settings(max_examples=50)
def test_frontend::tao::assignment_instantiation(instance):
    assert isinstance(instance, frontend::tao::Assignment)

@given(instance=TemplateRootObject_strategy)
@settings(max_examples=50)
def test_templaterootobject_instantiation(instance):
    assert isinstance(instance, TemplateRootObject)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=frontend::tao::Template_strategy)
@settings(max_examples=50)
def test_frontend::tao::template_instantiation(instance):
    assert isinstance(instance, frontend::tao::Template)

@given(instance=ObjectInstantiation_strategy)
@settings(max_examples=50)
def test_objectinstantiation_instantiation(instance):
    assert isinstance(instance, ObjectInstantiation)

@given(instance=frontend::tao::TemplateRootObject_strategy)
@settings(max_examples=50)
def test_frontend::tao::templaterootobject_instantiation(instance):
    assert isinstance(instance, frontend::tao::TemplateRootObject)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=frontend::tao::AttributeAssigment_strategy)
@settings(max_examples=50)
def test_frontend::tao::attributeassigment_instantiation(instance):
    assert isinstance(instance, frontend::tao::AttributeAssigment)

@given(instance=frontend::tao::AttributeAssigment_strategy)
def test_frontend::tao::attributeassigment_targetFeature_type(instance):
    assert isinstance(instance.targetFeature, str)


@given(instance=frontend::tao::AttributeAssigment_strategy)
def test_frontend::tao::attributeassigment_targetFeature_setter(instance):
    original = instance.targetFeature
    instance.targetFeature = original
    assert instance.targetFeature == original

@given(instance=ReferenceAssignment_strategy)
@settings(max_examples=50)
def test_referenceassignment_instantiation(instance):
    assert isinstance(instance, ReferenceAssignment)

@given(instance=frontend::tao::Invocation_strategy)
@settings(max_examples=50)
def test_frontend::tao::invocation_instantiation(instance):
    assert isinstance(instance, frontend::tao::Invocation)

@given(instance=frontend::tao::ObjectSyntax_strategy)
@settings(max_examples=50)
def test_frontend::tao::objectsyntax_instantiation(instance):
    assert isinstance(instance, frontend::tao::ObjectSyntax)

@given(instance=tao::Assignment_strategy)
@settings(max_examples=50)
def test_tao::assignment_instantiation(instance):
    assert isinstance(instance, tao::Assignment)

@given(instance=frontend::tao::ReferenceAssignment_strategy)
@settings(max_examples=50)
def test_frontend::tao::referenceassignment_instantiation(instance):
    assert isinstance(instance, frontend::tao::ReferenceAssignment)

@given(instance=frontend::tao::ReferenceAssignment_strategy)
def test_frontend::tao::referenceassignment_targetFeature_type(instance):
    assert isinstance(instance.targetFeature, str)


@given(instance=frontend::tao::ReferenceAssignment_strategy)
def test_frontend::tao::referenceassignment_targetFeature_setter(instance):
    original = instance.targetFeature
    instance.targetFeature = original
    assert instance.targetFeature == original

@given(instance=frontend::tao::ReferenceAssignment_strategy)
def test_frontend::tao::referenceassignment_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=frontend::tao::ReferenceAssignment_strategy)
def test_frontend::tao::referenceassignment_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=frontend::tao::ObjectSourceVariable_strategy)
@settings(max_examples=50)
def test_frontend::tao::objectsourcevariable_instantiation(instance):
    assert isinstance(instance, frontend::tao::ObjectSourceVariable)

@given(instance=frontend::facilities::CopierCallbackDefinition_strategy)
@settings(max_examples=50)
def test_frontend::facilities::copiercallbackdefinition_instantiation(instance):
    assert isinstance(instance, frontend::facilities::CopierCallbackDefinition)

@given(instance=frontend::facilities::CopierCallbackDefinition_strategy)
def test_frontend::facilities::copiercallbackdefinition_stop_type(instance):
    assert isinstance(instance.stop, bool)


@given(instance=frontend::facilities::CopierCallbackDefinition_strategy)
def test_frontend::facilities::copiercallbackdefinition_stop_setter(instance):
    original = instance.stop
    instance.stop = original
    assert instance.stop == original

@given(instance=facilities::CopierCallbackDefinition_strategy)
@settings(max_examples=50)
def test_facilities::copiercallbackdefinition_instantiation(instance):
    assert isinstance(instance, facilities::CopierCallbackDefinition)

@given(instance=frontend::facilities::Copier_strategy)
@settings(max_examples=50)
def test_frontend::facilities::copier_instantiation(instance):
    assert isinstance(instance, frontend::facilities::Copier)

@given(instance=frontend::tao::TemplateParameter_strategy)
@settings(max_examples=50)
def test_frontend::tao::templateparameter_instantiation(instance):
    assert isinstance(instance, frontend::tao::TemplateParameter)

@given(instance=Template_strategy)
@settings(max_examples=50)
def test_template_instantiation(instance):
    assert isinstance(instance, Template)

@given(instance=frontend::tao::TaoTransformation_strategy)
@settings(max_examples=50)
def test_frontend::tao::taotransformation_instantiation(instance):
    assert isinstance(instance, frontend::tao::TaoTransformation)

@given(instance=InvokeTransformation_strategy)
@settings(max_examples=50)
def test_invoketransformation_instantiation(instance):
    assert isinstance(instance, InvokeTransformation)

@given(instance=frontend::qool::InvokeExternal_strategy)
@settings(max_examples=50)
def test_frontend::qool::invokeexternal_instantiation(instance):
    assert isinstance(instance, frontend::qool::InvokeExternal)

@given(instance=frontend::qool::InvokeExternal_strategy)
def test_frontend::qool::invokeexternal_traceAttributeName_type(instance):
    assert isinstance(instance.traceAttributeName, str)


@given(instance=frontend::qool::InvokeExternal_strategy)
def test_frontend::qool::invokeexternal_traceAttributeName_setter(instance):
    original = instance.traceAttributeName
    instance.traceAttributeName = original
    assert instance.traceAttributeName == original

@given(instance=frontend::qool::InvokeExternal_strategy)
def test_frontend::qool::invokeexternal_queueName_type(instance):
    assert isinstance(instance.queueName, str)


@given(instance=frontend::qool::InvokeExternal_strategy)
def test_frontend::qool::invokeexternal_queueName_setter(instance):
    original = instance.queueName
    instance.queueName = original
    assert instance.queueName == original

@given(instance=NamedInvocationParameter_strategy)
@settings(max_examples=50)
def test_namedinvocationparameter_instantiation(instance):
    assert isinstance(instance, NamedInvocationParameter)

@given(instance=InvocationParameter_strategy)
@settings(max_examples=50)
def test_invocationparameter_instantiation(instance):
    assert isinstance(instance, InvocationParameter)

@given(instance=frontend::qool::InvokeTransformation_strategy)
@settings(max_examples=50)
def test_frontend::qool::invoketransformation_instantiation(instance):
    assert isinstance(instance, frontend::qool::InvokeTransformation)

@given(instance=frontend::qool::InvokeTransformation_strategy)
def test_frontend::qool::invoketransformation_transformationName_type(instance):
    assert isinstance(instance.transformationName, str)


@given(instance=frontend::qool::InvokeTransformation_strategy)
def test_frontend::qool::invoketransformation_transformationName_setter(instance):
    original = instance.transformationName
    instance.transformationName = original
    assert instance.transformationName == original

@given(instance=frontend::qool::InvokeTransformation_strategy)
def test_frontend::qool::invoketransformation_entryPointName_type(instance):
    assert isinstance(instance.entryPointName, str)


@given(instance=frontend::qool::InvokeTransformation_strategy)
def test_frontend::qool::invoketransformation_entryPointName_setter(instance):
    original = instance.entryPointName
    instance.entryPointName = original
    assert instance.entryPointName == original

@given(instance=frontend::qool::NamedInvocationParameter_strategy)
@settings(max_examples=50)
def test_frontend::qool::namedinvocationparameter_instantiation(instance):
    assert isinstance(instance, frontend::qool::NamedInvocationParameter)

@given(instance=frontend::qool::NamedInvocationParameter_strategy)
def test_frontend::qool::namedinvocationparameter_formalName_type(instance):
    assert isinstance(instance.formalName, str)


@given(instance=frontend::qool::NamedInvocationParameter_strategy)
def test_frontend::qool::namedinvocationparameter_formalName_setter(instance):
    original = instance.formalName
    instance.formalName = original
    assert instance.formalName == original

@given(instance=TransformationDefinitionParameter_strategy)
@settings(max_examples=50)
def test_transformationdefinitionparameter_instantiation(instance):
    assert isinstance(instance, TransformationDefinitionParameter)

@given(instance=frontend::qool::InvocationParameter_strategy)
@settings(max_examples=50)
def test_frontend::qool::invocationparameter_instantiation(instance):
    assert isinstance(instance, frontend::qool::InvocationParameter)

@given(instance=frontend::qool::InvocationParameter_strategy)
def test_frontend::qool::invocationparameter_calleeModelName_type(instance):
    assert isinstance(instance.calleeModelName, str)


@given(instance=frontend::qool::InvocationParameter_strategy)
def test_frontend::qool::invocationparameter_calleeModelName_setter(instance):
    original = instance.calleeModelName
    instance.calleeModelName = original
    assert instance.calleeModelName == original

@given(instance=frontend::qool::InvokeInternal_strategy)
@settings(max_examples=50)
def test_frontend::qool::invokeinternal_instantiation(instance):
    assert isinstance(instance, frontend::qool::InvokeInternal)

@given(instance=IteratorStatement_strategy)
@settings(max_examples=50)
def test_iteratorstatement_instantiation(instance):
    assert isinstance(instance, IteratorStatement)

@given(instance=frontend::qool::ForEachStatement_strategy)
@settings(max_examples=50)
def test_frontend::qool::foreachstatement_instantiation(instance):
    assert isinstance(instance, frontend::qool::ForEachStatement)

@given(instance=frontend::qool::ForAllStatement_strategy)
@settings(max_examples=50)
def test_frontend::qool::forallstatement_instantiation(instance):
    assert isinstance(instance, frontend::qool::ForAllStatement)

@given(instance=core::Statement_strategy)
@settings(max_examples=50)
def test_core::statement_instantiation(instance):
    assert isinstance(instance, core::Statement)

@given(instance=frontend::tao::ObjectInstantiation_strategy)
@settings(max_examples=50)
def test_frontend::tao::objectinstantiation_instantiation(instance):
    assert isinstance(instance, frontend::tao::ObjectInstantiation)

@given(instance=frontend::core::DefineVariable_strategy)
@settings(max_examples=50)
def test_frontend::core::definevariable_instantiation(instance):
    assert isinstance(instance, frontend::core::DefineVariable)

@given(instance=frontend::qool::IteratorStatement_strategy)
@settings(max_examples=50)
def test_frontend::qool::iteratorstatement_instantiation(instance):
    assert isinstance(instance, frontend::qool::IteratorStatement)

@given(instance=TypeExpression_strategy)
@settings(max_examples=50)
def test_typeexpression_instantiation(instance):
    assert isinstance(instance, TypeExpression)

@given(instance=frontend::core::TraceUse_strategy)
@settings(max_examples=50)
def test_frontend::core::traceuse_instantiation(instance):
    assert isinstance(instance, frontend::core::TraceUse)

@given(instance=frontend::qool::QueueOptimization_strategy)
@settings(max_examples=50)
def test_frontend::qool::queueoptimization_instantiation(instance):
    assert isinstance(instance, frontend::qool::QueueOptimization)

@given(instance=QueueOptimization_strategy)
@settings(max_examples=50)
def test_queueoptimization_instantiation(instance):
    assert isinstance(instance, QueueOptimization)

@given(instance=frontend::qool::AccessByFeatureOptimization_strategy)
@settings(max_examples=50)
def test_frontend::qool::accessbyfeatureoptimization_instantiation(instance):
    assert isinstance(instance, frontend::qool::AccessByFeatureOptimization)

@given(instance=frontend::qool::AccessByFeatureOptimization_strategy)
def test_frontend::qool::accessbyfeatureoptimization_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=frontend::qool::AccessByFeatureOptimization_strategy)
def test_frontend::qool::accessbyfeatureoptimization_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=frontend::qool::AccessByFeatureOptimization_strategy)
def test_frontend::qool::accessbyfeatureoptimization_force_type(instance):
    assert isinstance(instance.force, bool)


@given(instance=frontend::qool::AccessByFeatureOptimization_strategy)
def test_frontend::qool::accessbyfeatureoptimization_force_setter(instance):
    original = instance.force
    instance.force = original
    assert instance.force == original

@given(instance=frontend::qool::MatchPredicate_strategy)
@settings(max_examples=50)
def test_frontend::qool::matchpredicate_instantiation(instance):
    assert isinstance(instance, frontend::qool::MatchPredicate)

@given(instance=MatchPredicate_strategy)
@settings(max_examples=50)
def test_matchpredicate_instantiation(instance):
    assert isinstance(instance, MatchPredicate)

@given(instance=frontend::qool::KindOfPredicate_strategy)
@settings(max_examples=50)
def test_frontend::qool::kindofpredicate_instantiation(instance):
    assert isinstance(instance, frontend::qool::KindOfPredicate)

@given(instance=frontend::qool::PropertyEqualsPredicate_strategy)
@settings(max_examples=50)
def test_frontend::qool::propertyequalspredicate_instantiation(instance):
    assert isinstance(instance, frontend::qool::PropertyEqualsPredicate)

@given(instance=frontend::qool::PropertyEqualsPredicate_strategy)
def test_frontend::qool::propertyequalspredicate_propertyName_type(instance):
    assert isinstance(instance.propertyName, str)


@given(instance=frontend::qool::PropertyEqualsPredicate_strategy)
def test_frontend::qool::propertyequalspredicate_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=frontend::qool::MatchExpression_strategy)
@settings(max_examples=50)
def test_frontend::qool::matchexpression_instantiation(instance):
    assert isinstance(instance, frontend::qool::MatchExpression)

@given(instance=frontend::qool::EmitStatement_strategy)
@settings(max_examples=50)
def test_frontend::qool::emitstatement_instantiation(instance):
    assert isinstance(instance, frontend::qool::EmitStatement)

@given(instance=mappings::MetamodelElementRef_strategy)
@settings(max_examples=50)
def test_mappings::metamodelelementref_instantiation(instance):
    assert isinstance(instance, mappings::MetamodelElementRef)

@given(instance=MetamodelElementRef_strategy)
@settings(max_examples=50)
def test_metamodelelementref_instantiation(instance):
    assert isinstance(instance, MetamodelElementRef)

@given(instance=frontend::mappings::AttributeRef_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributeref_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeRef)

@given(instance=frontend::mappings::AttributeRef_strategy)
def test_frontend::mappings::attributeref_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=frontend::mappings::AttributeRef_strategy)
def test_frontend::mappings::attributeref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=frontend::mappings::AttributeRef_strategy)
def test_frontend::mappings::attributeref_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=frontend::mappings::AttributeRef_strategy)
def test_frontend::mappings::attributeref_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=frontend::mappings::ClassRef_strategy)
@settings(max_examples=50)
def test_frontend::mappings::classref_instantiation(instance):
    assert isinstance(instance, frontend::mappings::ClassRef)

@given(instance=frontend::mappings::MetamodelElementRef_strategy)
@settings(max_examples=50)
def test_frontend::mappings::metamodelelementref_instantiation(instance):
    assert isinstance(instance, frontend::mappings::MetamodelElementRef)

@given(instance=DefaultValue_strategy)
@settings(max_examples=50)
def test_defaultvalue_instantiation(instance):
    assert isinstance(instance, DefaultValue)

@given(instance=frontend::mappings::IntDefaultValue_strategy)
@settings(max_examples=50)
def test_frontend::mappings::intdefaultvalue_instantiation(instance):
    assert isinstance(instance, frontend::mappings::IntDefaultValue)

@given(instance=frontend::mappings::IntDefaultValue_strategy)
def test_frontend::mappings::intdefaultvalue_defaultValue_type(instance):
    assert isinstance(instance.defaultValue, str)


@given(instance=frontend::mappings::IntDefaultValue_strategy)
def test_frontend::mappings::intdefaultvalue_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=frontend::qool::QoolQueue_strategy)
@settings(max_examples=50)
def test_frontend::qool::qoolqueue_instantiation(instance):
    assert isinstance(instance, frontend::qool::QoolQueue)

@given(instance=Segment_strategy)
@settings(max_examples=50)
def test_segment_instantiation(instance):
    assert isinstance(instance, Segment)

@given(instance=QoolQueue_strategy)
@settings(max_examples=50)
def test_qoolqueue_instantiation(instance):
    assert isinstance(instance, QoolQueue)

@given(instance=frontend::qool::ModelElementQueue_strategy)
@settings(max_examples=50)
def test_frontend::qool::modelelementqueue_instantiation(instance):
    assert isinstance(instance, frontend::qool::ModelElementQueue)

@given(instance=frontend::qool::LocalQueue_strategy)
@settings(max_examples=50)
def test_frontend::qool::localqueue_instantiation(instance):
    assert isinstance(instance, frontend::qool::LocalQueue)

@given(instance=frontend::qool::QoolTransformation_strategy)
@settings(max_examples=50)
def test_frontend::qool::qooltransformation_instantiation(instance):
    assert isinstance(instance, frontend::qool::QoolTransformation)

@given(instance=frontend::mappings::ReferenceRef_strategy)
@settings(max_examples=50)
def test_frontend::mappings::referenceref_instantiation(instance):
    assert isinstance(instance, frontend::mappings::ReferenceRef)

@given(instance=frontend::mappings::ReferenceRef_strategy)
def test_frontend::mappings::referenceref_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=frontend::mappings::ReferenceRef_strategy)
def test_frontend::mappings::referenceref_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=frontend::mappings::ReferenceRef_strategy)
def test_frontend::mappings::referenceref_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=frontend::mappings::ReferenceRef_strategy)
def test_frontend::mappings::referenceref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=AttributeModifier_strategy)
@settings(max_examples=50)
def test_attributemodifier_instantiation(instance):
    assert isinstance(instance, AttributeModifier)

@given(instance=frontend::mappings::DefaultValue_strategy)
@settings(max_examples=50)
def test_frontend::mappings::defaultvalue_instantiation(instance):
    assert isinstance(instance, frontend::mappings::DefaultValue)

@given(instance=Class2Class_strategy)
@settings(max_examples=50)
def test_class2class_instantiation(instance):
    assert isinstance(instance, Class2Class)

@given(instance=mappings::AttributeRightPart_strategy)
@settings(max_examples=50)
def test_mappings::attributerightpart_instantiation(instance):
    assert isinstance(instance, mappings::AttributeRightPart)

@given(instance=mappings::Feature2Feature_strategy)
@settings(max_examples=50)
def test_mappings::feature2feature_instantiation(instance):
    assert isinstance(instance, mappings::Feature2Feature)

@given(instance=frontend::mappings::FeatureRef_strategy)
@settings(max_examples=50)
def test_frontend::mappings::featureref_instantiation(instance):
    assert isinstance(instance, frontend::mappings::FeatureRef)

@given(instance=frontend::mappings::FeatureRef_strategy)
def test_frontend::mappings::featureref_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=frontend::mappings::FeatureRef_strategy)
def test_frontend::mappings::featureref_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=frontend::mappings::FeatureRef_strategy)
def test_frontend::mappings::featureref_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=frontend::mappings::FeatureRef_strategy)
def test_frontend::mappings::featureref_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=frontend::mappings::Attribute2Attribute_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attribute2attribute_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Attribute2Attribute)

@given(instance=frontend::mappings::Attribute2Attribute_strategy)
def test_frontend::mappings::attribute2attribute_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=frontend::mappings::Attribute2Attribute_strategy)
def test_frontend::mappings::attribute2attribute_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=frontend::mappings::Join_strategy)
@settings(max_examples=50)
def test_frontend::mappings::join_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Join)

@given(instance=frontend::mappings::Split_strategy)
@settings(max_examples=50)
def test_frontend::mappings::split_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Split)

@given(instance=frontend::mappings::Operator_strategy)
@settings(max_examples=50)
def test_frontend::mappings::operator_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Operator)

@given(instance=frontend::mappings::ConvertModifier_strategy)
@settings(max_examples=50)
def test_frontend::mappings::convertmodifier_instantiation(instance):
    assert isinstance(instance, frontend::mappings::ConvertModifier)

@given(instance=frontend::mappings::ConvertModifier_strategy)
def test_frontend::mappings::convertmodifier_converter_type(instance):
    assert isinstance(instance.converter, str)


@given(instance=frontend::mappings::ConvertModifier_strategy)
def test_frontend::mappings::convertmodifier_converter_setter(instance):
    original = instance.converter
    instance.converter = original
    assert instance.converter == original

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=frontend::mappings::AttributeModifier_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributemodifier_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeModifier)

@given(instance=frontend::mappings::Modifier_strategy)
@settings(max_examples=50)
def test_frontend::mappings::modifier_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Modifier)

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

@given(instance=frontend::mappings::Class2Class_strategy)
@settings(max_examples=50)
def test_frontend::mappings::class2class_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Class2Class)

@given(instance=frontend::mappings::Class2Class_strategy)
def test_frontend::mappings::class2class_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=frontend::mappings::Class2Class_strategy)
def test_frontend::mappings::class2class_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=frontend::core::InlineFeature_strategy)
@settings(max_examples=50)
def test_frontend::core::inlinefeature_instantiation(instance):
    assert isinstance(instance, frontend::core::InlineFeature)

@given(instance=frontend::core::InlineFeature_strategy)
def test_frontend::core::inlinefeature_multivalued_type(instance):
    assert isinstance(instance.multivalued, bool)


@given(instance=frontend::core::InlineFeature_strategy)
def test_frontend::core::inlinefeature_multivalued_setter(instance):
    original = instance.multivalued
    instance.multivalued = original
    assert instance.multivalued == original

@given(instance=frontend::core::TraceElement_strategy)
@settings(max_examples=50)
def test_frontend::core::traceelement_instantiation(instance):
    assert isinstance(instance, frontend::core::TraceElement)

@given(instance=frontend::core::DefinitionParameter_strategy)
@settings(max_examples=50)
def test_frontend::core::definitionparameter_instantiation(instance):
    assert isinstance(instance, frontend::core::DefinitionParameter)

@given(instance=frontend::core::TraceDefinition_strategy)
@settings(max_examples=50)
def test_frontend::core::tracedefinition_instantiation(instance):
    assert isinstance(instance, frontend::core::TraceDefinition)

@given(instance=frontend::core::InlineClass_strategy)
@settings(max_examples=50)
def test_frontend::core::inlineclass_instantiation(instance):
    assert isinstance(instance, frontend::core::InlineClass)

@given(instance=frontend::qool::Segment_strategy)
@settings(max_examples=50)
def test_frontend::qool::segment_instantiation(instance):
    assert isinstance(instance, frontend::qool::Segment)

@given(instance=frontend::mappings::Tag_strategy)
@settings(max_examples=50)
def test_frontend::mappings::tag_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Tag)

@given(instance=frontend::mappings::Converter_strategy)
@settings(max_examples=50)
def test_frontend::mappings::converter_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Converter)

@given(instance=frontend::mappings::Converter_strategy)
def test_frontend::mappings::converter_converterName_type(instance):
    assert isinstance(instance.converterName, str)


@given(instance=frontend::mappings::Converter_strategy)
def test_frontend::mappings::converter_converterName_setter(instance):
    original = instance.converterName
    instance.converterName = original
    assert instance.converterName == original

@given(instance=frontend::mappings::Converter_strategy)
def test_frontend::mappings::converter_isExternal_type(instance):
    assert isinstance(instance.isExternal, str)


@given(instance=frontend::mappings::Converter_strategy)
def test_frontend::mappings::converter_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

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

@given(instance=frontend::mappings::RelatedBy_strategy)
@settings(max_examples=50)
def test_frontend::mappings::relatedby_instantiation(instance):
    assert isinstance(instance, frontend::mappings::RelatedBy)

@given(instance=frontend::mappings::LinkedBy_strategy)
@settings(max_examples=50)
def test_frontend::mappings::linkedby_instantiation(instance):
    assert isinstance(instance, frontend::mappings::LinkedBy)

@given(instance=frontend::mappings::EqualityFilter_strategy)
@settings(max_examples=50)
def test_frontend::mappings::equalityfilter_instantiation(instance):
    assert isinstance(instance, frontend::mappings::EqualityFilter)

@given(instance=frontend::mappings::EqualityFilter_strategy)
def test_frontend::mappings::equalityfilter_filter_type(instance):
    assert isinstance(instance.filter, str)


@given(instance=frontend::mappings::EqualityFilter_strategy)
def test_frontend::mappings::equalityfilter_filter_setter(instance):
    original = instance.filter
    instance.filter = original
    assert instance.filter == original

@given(instance=MappingElement_strategy)
@settings(max_examples=50)
def test_mappingelement_instantiation(instance):
    assert isinstance(instance, MappingElement)

@given(instance=frontend::mappings::C2CModifier_strategy)
@settings(max_examples=50)
def test_frontend::mappings::c2cmodifier_instantiation(instance):
    assert isinstance(instance, frontend::mappings::C2CModifier)

@given(instance=frontend::mappings::Context_strategy)
@settings(max_examples=50)
def test_frontend::mappings::context_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Context)

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

@given(instance=frontend::mappings::Delegate_strategy)
@settings(max_examples=50)
def test_frontend::mappings::delegate_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Delegate)

@given(instance=frontend::mappings::Delegate_strategy)
def test_frontend::mappings::delegate_featureName_type(instance):
    assert isinstance(instance.featureName, str)


@given(instance=frontend::mappings::Delegate_strategy)
def test_frontend::mappings::delegate_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original

@given(instance=frontend::mappings::Delegate_strategy)
def test_frontend::mappings::delegate_linkName_type(instance):
    assert isinstance(instance.linkName, str)


@given(instance=frontend::mappings::Delegate_strategy)
def test_frontend::mappings::delegate_linkName_setter(instance):
    original = instance.linkName
    instance.linkName = original
    assert instance.linkName == original

@given(instance=frontend::mappings::Delegate_strategy)
def test_frontend::mappings::delegate_isExternal_type(instance):
    assert isinstance(instance.isExternal, str)


@given(instance=frontend::mappings::Delegate_strategy)
def test_frontend::mappings::delegate_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original

@given(instance=mappings::MappingVariable_strategy)
@settings(max_examples=50)
def test_mappings::mappingvariable_instantiation(instance):
    assert isinstance(instance, mappings::MappingVariable)

@given(instance=core::ClassUse_strategy)
@settings(max_examples=50)
def test_core::classuse_instantiation(instance):
    assert isinstance(instance, core::ClassUse)

@given(instance=frontend::core::ModelReference_strategy)
@settings(max_examples=50)
def test_frontend::core::modelreference_instantiation(instance):
    assert isinstance(instance, frontend::core::ModelReference)

@given(instance=frontend::mappings::MatchedElement_strategy)
@settings(max_examples=50)
def test_frontend::mappings::matchedelement_instantiation(instance):
    assert isinstance(instance, frontend::mappings::MatchedElement)

@given(instance=frontend::mappings::MappingVariable_strategy)
@settings(max_examples=50)
def test_frontend::mappings::mappingvariable_instantiation(instance):
    assert isinstance(instance, frontend::mappings::MappingVariable)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=frontend::mappings::AttributeRightPart_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributerightpart_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeRightPart)

@given(instance=AttributeRightPart_strategy)
@settings(max_examples=50)
def test_attributerightpart_instantiation(instance):
    assert isinstance(instance, AttributeRightPart)

@given(instance=frontend::mappings::AttributeIsResolveLink_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributeisresolvelink_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeIsResolveLink)

@given(instance=frontend::mappings::AttributeIsString_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributeisstring_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeIsString)

@given(instance=frontend::mappings::AttributeIsString_strategy)
def test_frontend::mappings::attributeisstring_strValue_type(instance):
    assert isinstance(instance.strValue, str)


@given(instance=frontend::mappings::AttributeIsString_strategy)
def test_frontend::mappings::attributeisstring_strValue_setter(instance):
    original = instance.strValue
    instance.strValue = original
    assert instance.strValue == original

@given(instance=frontend::mappings::AttributeIsInteger_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributeisinteger_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeIsInteger)

@given(instance=frontend::mappings::AttributeIsInteger_strategy)
def test_frontend::mappings::attributeisinteger_intValue_type(instance):
    assert isinstance(instance.intValue, int)


@given(instance=frontend::mappings::AttributeIsInteger_strategy)
def test_frontend::mappings::attributeisinteger_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=frontend::mappings::AttributeIsDouble_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributeisdouble_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeIsDouble)

@given(instance=frontend::mappings::AttributeIsDouble_strategy)
def test_frontend::mappings::attributeisdouble_doubleValue_type(instance):
    assert isinstance(instance.doubleValue, str)


@given(instance=frontend::mappings::AttributeIsDouble_strategy)
def test_frontend::mappings::attributeisdouble_doubleValue_setter(instance):
    original = instance.doubleValue
    instance.doubleValue = original
    assert instance.doubleValue == original

@given(instance=frontend::mappings::AttributeIsBoolean_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributeisboolean_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeIsBoolean)

@given(instance=frontend::mappings::AttributeIsBoolean_strategy)
def test_frontend::mappings::attributeisboolean_boolValue_type(instance):
    assert isinstance(instance.boolValue, str)


@given(instance=frontend::mappings::AttributeIsBoolean_strategy)
def test_frontend::mappings::attributeisboolean_boolValue_setter(instance):
    original = instance.boolValue
    instance.boolValue = original
    assert instance.boolValue == original

@given(instance=AttributeRef_strategy)
@settings(max_examples=50)
def test_attributeref_instantiation(instance):
    assert isinstance(instance, AttributeRef)

@given(instance=Feature2Feature_strategy)
@settings(max_examples=50)
def test_feature2feature_instantiation(instance):
    assert isinstance(instance, Feature2Feature)

@given(instance=frontend::mappings::Reference2Reference_strategy)
@settings(max_examples=50)
def test_frontend::mappings::reference2reference_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Reference2Reference)

@given(instance=frontend::mappings::Reference2Reference_strategy)
def test_frontend::mappings::reference2reference_resolverName_type(instance):
    assert isinstance(instance.resolverName, str)


@given(instance=frontend::mappings::Reference2Reference_strategy)
def test_frontend::mappings::reference2reference_resolverName_setter(instance):
    original = instance.resolverName
    instance.resolverName = original
    assert instance.resolverName == original

@given(instance=frontend::mappings::Reference2Reference_strategy)
def test_frontend::mappings::reference2reference_cardinality_type(instance):
    assert isinstance(instance.cardinality, str)


@given(instance=frontend::mappings::Reference2Reference_strategy)
def test_frontend::mappings::reference2reference_cardinality_setter(instance):
    original = instance.cardinality
    instance.cardinality = original
    assert instance.cardinality == original

@given(instance=frontend::mappings::AttributeMapping_strategy)
@settings(max_examples=50)
def test_frontend::mappings::attributemapping_instantiation(instance):
    assert isinstance(instance, frontend::mappings::AttributeMapping)

@given(instance=Converter_strategy)
@settings(max_examples=50)
def test_converter_instantiation(instance):
    assert isinstance(instance, Converter)

@given(instance=FeatureRef_strategy)
@settings(max_examples=50)
def test_featureref_instantiation(instance):
    assert isinstance(instance, FeatureRef)

@given(instance=frontend::mappings::Feature2Feature_strategy)
@settings(max_examples=50)
def test_frontend::mappings::feature2feature_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Feature2Feature)

@given(instance=frontend::mappings::ClassMapping_strategy)
@settings(max_examples=50)
def test_frontend::mappings::classmapping_instantiation(instance):
    assert isinstance(instance, frontend::mappings::ClassMapping)

@given(instance=frontend::mappings::MappingElement_strategy)
@settings(max_examples=50)
def test_frontend::mappings::mappingelement_instantiation(instance):
    assert isinstance(instance, frontend::mappings::MappingElement)

@given(instance=frontend::mappings::Section_strategy)
@settings(max_examples=50)
def test_frontend::mappings::section_instantiation(instance):
    assert isinstance(instance, frontend::mappings::Section)

@given(instance=frontend::mappings::Section_strategy)
def test_frontend::mappings::section_sectionType_type(instance):
    assert isinstance(instance.sectionType, str)


@given(instance=frontend::mappings::Section_strategy)
def test_frontend::mappings::section_sectionType_setter(instance):
    original = instance.sectionType
    instance.sectionType = original
    assert instance.sectionType == original

@given(instance=frontend::patterns::PObject_strategy)
@settings(max_examples=50)
def test_frontend::patterns::pobject_instantiation(instance):
    assert isinstance(instance, frontend::patterns::PObject)

@given(instance=frontend::patterns::POutputVariable_strategy)
@settings(max_examples=50)
def test_frontend::patterns::poutputvariable_instantiation(instance):
    assert isinstance(instance, frontend::patterns::POutputVariable)

@given(instance=POutputVariable_strategy)
@settings(max_examples=50)
def test_poutputvariable_instantiation(instance):
    assert isinstance(instance, POutputVariable)

@given(instance=PObject_strategy)
@settings(max_examples=50)
def test_pobject_instantiation(instance):
    assert isinstance(instance, PObject)

@given(instance=frontend::patterns::Pattern_strategy)
@settings(max_examples=50)
def test_frontend::patterns::pattern_instantiation(instance):
    assert isinstance(instance, frontend::patterns::Pattern)

@given(instance=frontend::patterns::Pattern_strategy)
def test_frontend::patterns::pattern_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=frontend::patterns::Pattern_strategy)
def test_frontend::patterns::pattern_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=frontend::patterns::PatternSpecification_strategy)
@settings(max_examples=50)
def test_frontend::patterns::patternspecification_instantiation(instance):
    assert isinstance(instance, frontend::patterns::PatternSpecification)

@given(instance=core::TransformationDefinition_strategy)
@settings(max_examples=50)
def test_core::transformationdefinition_instantiation(instance):
    assert isinstance(instance, core::TransformationDefinition)

@given(instance=chain::AvailableTransformation_strategy)
@settings(max_examples=50)
def test_chain::availabletransformation_instantiation(instance):
    assert isinstance(instance, chain::AvailableTransformation)

@given(instance=frontend::chain::CompositeTransformation_strategy)
@settings(max_examples=50)
def test_frontend::chain::compositetransformation_instantiation(instance):
    assert isinstance(instance, frontend::chain::CompositeTransformation)

@given(instance=frontend::chain::ExternalTransformation_strategy)
@settings(max_examples=50)
def test_frontend::chain::externaltransformation_instantiation(instance):
    assert isinstance(instance, frontend::chain::ExternalTransformation)

@given(instance=frontend::chain::AvailableTransformation_strategy)
@settings(max_examples=50)
def test_frontend::chain::availabletransformation_instantiation(instance):
    assert isinstance(instance, frontend::chain::AvailableTransformation)

@given(instance=RepresentModel_strategy)
@settings(max_examples=50)
def test_representmodel_instantiation(instance):
    assert isinstance(instance, RepresentModel)

@given(instance=frontend::core::UseDeclaration_strategy)
@settings(max_examples=50)
def test_frontend::core::usedeclaration_instantiation(instance):
    assert isinstance(instance, frontend::core::UseDeclaration)

@given(instance=frontend::core::UseDeclaration_strategy)
def test_frontend::core::usedeclaration_as__type(instance):
    assert isinstance(instance.as_, str)


@given(instance=frontend::core::UseDeclaration_strategy)
def test_frontend::core::usedeclaration_as__setter(instance):
    original = instance.as_
    instance.as_ = original
    assert instance.as_ == original

@given(instance=frontend::core::UseDeclaration_strategy)
def test_frontend::core::usedeclaration_module_type(instance):
    assert isinstance(instance.module, str)


@given(instance=frontend::core::UseDeclaration_strategy)
def test_frontend::core::usedeclaration_module_setter(instance):
    original = instance.module
    instance.module = original
    assert instance.module == original

@given(instance=frontend::core::RequireDeclaration_strategy)
@settings(max_examples=50)
def test_frontend::core::requiredeclaration_instantiation(instance):
    assert isinstance(instance, frontend::core::RequireDeclaration)

@given(instance=frontend::core::RequireDeclaration_strategy)
def test_frontend::core::requiredeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=frontend::core::RequireDeclaration_strategy)
def test_frontend::core::requiredeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=frontend::core::RequireDeclaration_strategy)
def test_frontend::core::requiredeclaration_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=frontend::core::RequireDeclaration_strategy)
def test_frontend::core::requiredeclaration_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=AvailableTransformation_strategy)
@settings(max_examples=50)
def test_availabletransformation_instantiation(instance):
    assert isinstance(instance, AvailableTransformation)

@given(instance=frontend::chain::TransformationExecution_strategy)
@settings(max_examples=50)
def test_frontend::chain::transformationexecution_instantiation(instance):
    assert isinstance(instance, frontend::chain::TransformationExecution)

@given(instance=Delegate_strategy)
@settings(max_examples=50)
def test_delegate_instantiation(instance):
    assert isinstance(instance, Delegate)

@given(instance=frontend::mappings::MappingTransformation_strategy)
@settings(max_examples=50)
def test_frontend::mappings::mappingtransformation_instantiation(instance):
    assert isinstance(instance, frontend::mappings::MappingTransformation)

@given(instance=PReference_strategy)
@settings(max_examples=50)
def test_preference_instantiation(instance):
    assert isinstance(instance, PReference)

@given(instance=frontend::patterns::CollectionReference_strategy)
@settings(max_examples=50)
def test_frontend::patterns::collectionreference_instantiation(instance):
    assert isinstance(instance, frontend::patterns::CollectionReference)

@given(instance=frontend::patterns::PReference_strategy)
@settings(max_examples=50)
def test_frontend::patterns::preference_instantiation(instance):
    assert isinstance(instance, frontend::patterns::PReference)

@given(instance=frontend::patterns::PAttribute_strategy)
@settings(max_examples=50)
def test_frontend::patterns::pattribute_instantiation(instance):
    assert isinstance(instance, frontend::patterns::PAttribute)
