import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AltExp,
    imperativeocl::ImperativeExpression,
    ObjectTemplateExp,
    PropertyTemplateItem,
    AnonymousTupleLiteralPart,
    DictLiteralPart,
    essentialocl::LoopExp,
    Janus::imperativeocl::ImperativeLoopExp,
    LogExp,
    CollectionLiteralExp,
    CollectionLiteralPart,
    Janus::essentialocl::CollectionRange,
    Janus::essentialocl::CollectionItem,
    ComputeExp,
    LetExp,
    essentialocl::OclExpression,
    essentialocl::CallExp,
    Janus::imperativeocl::SwitchExp,
    Janus::essentialocl::LoopExp,
    FeaturePropertyCall,
    Janus::essentialocl::PropertyCallExp,
    TemplateExp,
    Janus::template::ObjectTemplateExp,
    Janus::template::CollectionTemplateExp,
    Predicate,
    NumericLiteralExp,
    Janus::essentialocl::UnlimitedNaturalExp,
    TryExp,
    TypedElement,
    Janus::essentialocl::CollectionLiteralPart,
    Janus::essentialocl::Variable,
    Janus::essentialocl::OclExpression,
    PrimitiveLiteralExp,
    Janus::essentialocl::BooleanLiteralExp,
    OclExpression,
    Janus::essentialocl::CallExp,
    Janus::essentialocl::VariableExp,
    Janus::essentialocl::LetExp,
    Janus::imperativeocl::ImperativeExpression,
    Janus::essentialocl::IfExp,
    Janus::essentialocl::TypeExp,
    Transformation,
    Relation,
    Model,
    emof::Package,
    emof::Class,
    Janus::JTL::Transformation,
    Extent,
    Janus::emof::URIExtent,
    Variable,
    Pattern,
    Domain,
    Package,
    NamedElement,
    Janus::JTL::Domain,
    Janus::JTL::Model,
    Janus::JTL::Relation,
    Janus::emof::TypedElement,
    Janus::emof::Package,
    Janus::emof::MultiplicityElement,
    Parameter,
    emof::TypedElement,
    emof::MultiplicityElement,
    Janus::emof::Operation,
    Janus::emof::Object,
    Janus::emof::Property,
    Enumeration,
    Janus::emof::EnumerationLiteral,
    Janus::emof::Parameter,
    Janus::emof::Type,
    EnumerationLiteral,
    DataType,
    Janus::emof::PrimitiveType,
    Janus::emof::Enumeration,
    Element,
    Janus::JTL::Pattern,
    Janus::emof::Comment,
    Janus::imperativeocl::DictLiteralPart,
    Janus::imperativeocl::AnonymousTupleLiteralPart,
    Janus::JTL::Predicate,
    Janus::emof::NamedElement,
    Janus::template::PropertyTemplateItem,
    Janus::emof::Tag,
    Comment,
    Tag,
    Object,
    Janus::emof::Extent,
    Janus::emof::Element,
    Class,
    Janus::imperativeocl::Typedef,
    Janus::imperativeocl::AnonymousTupleType,
    Operation,
    ImperativeExpression,
    Janus::imperativeocl::UnlinkExp,
    Janus::imperativeocl::UnpackExp,
    Janus::imperativeocl::ReturnExp,
    Janus::imperativeocl::AltExp,
    Janus::imperativeocl::RaiseExp,
    Janus::imperativeocl::ContinueExp,
    Janus::imperativeocl::VariableInitExp,
    Janus::imperativeocl::TupleExp,
    Janus::imperativeocl::InstantiationExp,
    Janus::imperativeocl::BreakExp,
    Janus::imperativeocl::ComputeExp,
    Janus::imperativeocl::WhileExp,
    Janus::imperativeocl::LogExp,
    Janus::imperativeocl::TryExp,
    Janus::imperativeocl::AssertExp,
    Janus::imperativeocl::BlockExp,
    Janus::imperativeocl::AssignExp,
    ImperativeLoopExp,
    Janus::imperativeocl::ForExp,
    Janus::imperativeocl::CollectorExp,
    Janus::imperativeocl::ImperativeIterateExp,
    Janus::essentialocl::CollectionType,
    CollectionType,
    Janus::imperativeocl::ListType,
    Janus::imperativeocl::DictionaryType,
    Janus::essentialocl::BagType,
    TupleLiteralExp,
    Janus::essentialocl::TupleLiteralPart,
    CallExp,
    Janus::essentialocl::FeaturePropertyCall,
    Janus::essentialocl::OpaqueExpression,
    OpaqueExpression,
    Janus::essentialocl::ExpressionInOcl,
    TupleLiteralPart,
    emof::Type,
    Janus::essentialocl::AnyType,
    emof::DataType,
    Janus::essentialocl::TupleType,
    Janus::essentialocl::SetType,
    Janus::essentialocl::SequenceType,
    Janus::essentialocl::OrderedSetType,
    Janus::essentialocl::NumericLiteralExp,
    LiteralExp,
    Janus::imperativeocl::AnonymousTupleLiteralExp,
    Janus::essentialocl::TupleLiteralExp,
    Janus::template::TemplateExp,
    Janus::essentialocl::EnumLiteralExp,
    Janus::essentialocl::InvalidLiteralExp,
    Janus::essentialocl::CollectionLiteralExp,
    Janus::essentialocl::NullLiteralExp,
    Janus::imperativeocl::DictLiteralExp,
    Janus::essentialocl::PrimitiveLiteralExp,
    Janus::essentialocl::LiteralExp,
    Janus::essentialocl::RealLiteralExp,
    Janus::essentialocl::OperationCallExp,
    Janus::essentialocl::IntegerLiteralExp,
    Janus::essentialocl::StringLiteralExp,
    LoopExp,
    Janus::essentialocl::IteratorExp,
    Janus::essentialocl::IterateExp,
    Property,
    Type,
    Janus::essentialocl::VoidType,
    Janus::essentialocl::InvalidType,
    Janus::emof::DataType,
    Janus::imperativeocl::TemplateParameterType,
    Janus::emof::Class,
    CollectionKind,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeExpression)


def test_imperativeocl::imperativeexpression_constructor_exists():
    assert callable(imperativeocl::ImperativeExpression.__init__)


def test_imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(AnonymousTupleLiteralPart)


def test_anonymoustupleliteralpart_constructor_exists():
    assert callable(AnonymousTupleLiteralPart.__init__)


def test_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::LoopExp)


def test_essentialocl::loopexp_constructor_exists():
    assert callable(essentialocl::LoopExp.__init__)


def test_essentialocl::loopexp_constructor_args():
    sig = inspect.signature(essentialocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ImperativeLoopExp)


def test_janus::imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(Janus::imperativeocl::ImperativeLoopExp.__init__)


def test_janus::imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::CollectionRange)


def test_janus::essentialocl::collectionrange_constructor_exists():
    assert callable(Janus::essentialocl::CollectionRange.__init__)


def test_janus::essentialocl::collectionrange_constructor_args():
    sig = inspect.signature(Janus::essentialocl::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::CollectionItem)


def test_janus::essentialocl::collectionitem_constructor_exists():
    assert callable(Janus::essentialocl::CollectionItem.__init__)


def test_janus::essentialocl::collectionitem_constructor_args():
    sig = inspect.signature(Janus::essentialocl::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_computeexp_is_not_abstract():
    assert not inspect.isabstract(ComputeExp)


def test_computeexp_constructor_exists():
    assert callable(ComputeExp.__init__)


def test_computeexp_constructor_args():
    sig = inspect.signature(ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl::OclExpression)


def test_essentialocl::oclexpression_constructor_exists():
    assert callable(essentialocl::OclExpression.__init__)


def test_essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(essentialocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::CallExp)


def test_essentialocl::callexp_constructor_exists():
    assert callable(essentialocl::CallExp.__init__)


def test_essentialocl::callexp_constructor_args():
    sig = inspect.signature(essentialocl::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::SwitchExp)


def test_janus::imperativeocl::switchexp_constructor_exists():
    assert callable(Janus::imperativeocl::SwitchExp.__init__)


def test_janus::imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::LoopExp)


def test_janus::essentialocl::loopexp_constructor_exists():
    assert callable(Janus::essentialocl::LoopExp.__init__)


def test_janus::essentialocl::loopexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::PropertyCallExp)


def test_janus::essentialocl::propertycallexp_constructor_exists():
    assert callable(Janus::essentialocl::PropertyCallExp.__init__)


def test_janus::essentialocl::propertycallexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::template::objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(Janus::template::ObjectTemplateExp)


def test_janus::template::objecttemplateexp_constructor_exists():
    assert callable(Janus::template::ObjectTemplateExp.__init__)


def test_janus::template::objecttemplateexp_constructor_args():
    sig = inspect.signature(Janus::template::ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "referredClass" in params, "Missing parameter 'referredClass'"

def test_janus::template::objecttemplateexp_has_referredClass():
    assert hasattr(Janus::template::ObjectTemplateExp, "referredClass")
    descriptor = None
    for klass in Janus::template::ObjectTemplateExp.__mro__:
        if "referredClass" in klass.__dict__:
            descriptor = klass.__dict__["referredClass"]
            break
    assert isinstance(descriptor, property)



def test_janus::template::collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(Janus::template::CollectionTemplateExp)


def test_janus::template::collectiontemplateexp_constructor_exists():
    assert callable(Janus::template::CollectionTemplateExp.__init__)


def test_janus::template::collectiontemplateexp_constructor_args():
    sig = inspect.signature(Janus::template::CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_janus::template::collectiontemplateexp_has_kind():
    assert hasattr(Janus::template::CollectionTemplateExp, "kind")
    descriptor = None
    for klass in Janus::template::CollectionTemplateExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::UnlimitedNaturalExp)


def test_janus::essentialocl::unlimitednaturalexp_constructor_exists():
    assert callable(Janus::essentialocl::UnlimitedNaturalExp.__init__)


def test_janus::essentialocl::unlimitednaturalexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_janus::essentialocl::unlimitednaturalexp_has_symbol():
    assert hasattr(Janus::essentialocl::UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in Janus::essentialocl::UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_tryexp_is_not_abstract():
    assert not inspect.isabstract(TryExp)


def test_tryexp_constructor_exists():
    assert callable(TryExp.__init__)


def test_tryexp_constructor_args():
    sig = inspect.signature(TryExp.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::CollectionLiteralPart)


def test_janus::essentialocl::collectionliteralpart_constructor_exists():
    assert callable(Janus::essentialocl::CollectionLiteralPart.__init__)


def test_janus::essentialocl::collectionliteralpart_constructor_args():
    sig = inspect.signature(Janus::essentialocl::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::variable_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::Variable)


def test_janus::essentialocl::variable_constructor_exists():
    assert callable(Janus::essentialocl::Variable.__init__)


def test_janus::essentialocl::variable_constructor_args():
    sig = inspect.signature(Janus::essentialocl::Variable.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::OclExpression)


def test_janus::essentialocl::oclexpression_constructor_exists():
    assert callable(Janus::essentialocl::OclExpression.__init__)


def test_janus::essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(Janus::essentialocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::BooleanLiteralExp)


def test_janus::essentialocl::booleanliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::BooleanLiteralExp.__init__)


def test_janus::essentialocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_janus::essentialocl::booleanliteralexp_has_booleanSymbol():
    assert hasattr(Janus::essentialocl::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in Janus::essentialocl::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::CallExp)


def test_janus::essentialocl::callexp_constructor_exists():
    assert callable(Janus::essentialocl::CallExp.__init__)


def test_janus::essentialocl::callexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::VariableExp)


def test_janus::essentialocl::variableexp_constructor_exists():
    assert callable(Janus::essentialocl::VariableExp.__init__)


def test_janus::essentialocl::variableexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::letexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::LetExp)


def test_janus::essentialocl::letexp_constructor_exists():
    assert callable(Janus::essentialocl::LetExp.__init__)


def test_janus::essentialocl::letexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ImperativeExpression)


def test_janus::imperativeocl::imperativeexpression_constructor_exists():
    assert callable(Janus::imperativeocl::ImperativeExpression.__init__)


def test_janus::imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::IfExp)


def test_janus::essentialocl::ifexp_constructor_exists():
    assert callable(Janus::essentialocl::IfExp.__init__)


def test_janus::essentialocl::ifexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::typeexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::TypeExp)


def test_janus::essentialocl::typeexp_constructor_exists():
    assert callable(Janus::essentialocl::TypeExp.__init__)


def test_janus::essentialocl::typeexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_emof::package_is_not_abstract():
    assert not inspect.isabstract(emof::Package)


def test_emof::package_constructor_exists():
    assert callable(emof::Package.__init__)


def test_emof::package_constructor_args():
    sig = inspect.signature(emof::Package.__init__)
    params = list(sig.parameters.keys())



def test_emof::class_is_not_abstract():
    assert not inspect.isabstract(emof::Class)


def test_emof::class_constructor_exists():
    assert callable(emof::Class.__init__)


def test_emof::class_constructor_args():
    sig = inspect.signature(emof::Class.__init__)
    params = list(sig.parameters.keys())



def test_janus::jtl::transformation_is_not_abstract():
    assert not inspect.isabstract(Janus::JTL::Transformation)


def test_janus::jtl::transformation_constructor_exists():
    assert callable(Janus::JTL::Transformation.__init__)


def test_janus::jtl::transformation_constructor_args():
    sig = inspect.signature(Janus::JTL::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::uriextent_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::URIExtent)


def test_janus::emof::uriextent_constructor_exists():
    assert callable(Janus::emof::URIExtent.__init__)


def test_janus::emof::uriextent_constructor_args():
    sig = inspect.signature(Janus::emof::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_janus::jtl::domain_is_not_abstract():
    assert not inspect.isabstract(Janus::JTL::Domain)


def test_janus::jtl::domain_constructor_exists():
    assert callable(Janus::JTL::Domain.__init__)


def test_janus::jtl::domain_constructor_args():
    sig = inspect.signature(Janus::JTL::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"

def test_janus::jtl::domain_has_isEnforceable():
    assert hasattr(Janus::JTL::Domain, "isEnforceable")
    descriptor = None
    for klass in Janus::JTL::Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)

def test_janus::jtl::domain_has_isCheckable():
    assert hasattr(Janus::JTL::Domain, "isCheckable")
    descriptor = None
    for klass in Janus::JTL::Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)



def test_janus::jtl::model_is_not_abstract():
    assert not inspect.isabstract(Janus::JTL::Model)


def test_janus::jtl::model_constructor_exists():
    assert callable(Janus::JTL::Model.__init__)


def test_janus::jtl::model_constructor_args():
    sig = inspect.signature(Janus::JTL::Model.__init__)
    params = list(sig.parameters.keys())



def test_janus::jtl::relation_is_not_abstract():
    assert not inspect.isabstract(Janus::JTL::Relation)


def test_janus::jtl::relation_constructor_exists():
    assert callable(Janus::JTL::Relation.__init__)


def test_janus::jtl::relation_constructor_args():
    sig = inspect.signature(Janus::JTL::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_janus::jtl::relation_has_isTopLevel():
    assert hasattr(Janus::JTL::Relation, "isTopLevel")
    descriptor = None
    for klass in Janus::JTL::Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_janus::emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::TypedElement)


def test_janus::emof::typedelement_constructor_exists():
    assert callable(Janus::emof::TypedElement.__init__)


def test_janus::emof::typedelement_constructor_args():
    sig = inspect.signature(Janus::emof::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::package_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Package)


def test_janus::emof::package_constructor_exists():
    assert callable(Janus::emof::Package.__init__)


def test_janus::emof::package_constructor_args():
    sig = inspect.signature(Janus::emof::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_janus::emof::package_has_uri():
    assert hasattr(Janus::emof::Package, "uri")
    descriptor = None
    for klass in Janus::emof::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_janus::emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::MultiplicityElement)


def test_janus::emof::multiplicityelement_constructor_exists():
    assert callable(Janus::emof::MultiplicityElement.__init__)


def test_janus::emof::multiplicityelement_constructor_args():
    sig = inspect.signature(Janus::emof::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_janus::emof::multiplicityelement_has_upper():
    assert hasattr(Janus::emof::MultiplicityElement, "upper")
    descriptor = None
    for klass in Janus::emof::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::multiplicityelement_has_isOrdered():
    assert hasattr(Janus::emof::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in Janus::emof::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::multiplicityelement_has_isUnique():
    assert hasattr(Janus::emof::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in Janus::emof::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::multiplicityelement_has_lower():
    assert hasattr(Janus::emof::MultiplicityElement, "lower")
    descriptor = None
    for klass in Janus::emof::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(emof::TypedElement)


def test_emof::typedelement_constructor_exists():
    assert callable(emof::TypedElement.__init__)


def test_emof::typedelement_constructor_args():
    sig = inspect.signature(emof::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(emof::MultiplicityElement)


def test_emof::multiplicityelement_constructor_exists():
    assert callable(emof::MultiplicityElement.__init__)


def test_emof::multiplicityelement_constructor_args():
    sig = inspect.signature(emof::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::operation_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Operation)


def test_janus::emof::operation_constructor_exists():
    assert callable(Janus::emof::Operation.__init__)


def test_janus::emof::operation_constructor_args():
    sig = inspect.signature(Janus::emof::Operation.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::object_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Object)


def test_janus::emof::object_constructor_exists():
    assert callable(Janus::emof::Object.__init__)


def test_janus::emof::object_constructor_args():
    sig = inspect.signature(Janus::emof::Object.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::property_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Property)


def test_janus::emof::property_constructor_exists():
    assert callable(Janus::emof::Property.__init__)


def test_janus::emof::property_constructor_args():
    sig = inspect.signature(Janus::emof::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isId" in params, "Missing parameter 'isId'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_janus::emof::property_has_isId():
    assert hasattr(Janus::emof::Property, "isId")
    descriptor = None
    for klass in Janus::emof::Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::property_has_isDerived():
    assert hasattr(Janus::emof::Property, "isDerived")
    descriptor = None
    for klass in Janus::emof::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::property_has_isReadOnly():
    assert hasattr(Janus::emof::Property, "isReadOnly")
    descriptor = None
    for klass in Janus::emof::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::property_has_default():
    assert hasattr(Janus::emof::Property, "default")
    descriptor = None
    for klass in Janus::emof::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::property_has_isComposite():
    assert hasattr(Janus::emof::Property, "isComposite")
    descriptor = None
    for klass in Janus::emof::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::EnumerationLiteral)


def test_janus::emof::enumerationliteral_constructor_exists():
    assert callable(Janus::emof::EnumerationLiteral.__init__)


def test_janus::emof::enumerationliteral_constructor_args():
    sig = inspect.signature(Janus::emof::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::parameter_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Parameter)


def test_janus::emof::parameter_constructor_exists():
    assert callable(Janus::emof::Parameter.__init__)


def test_janus::emof::parameter_constructor_args():
    sig = inspect.signature(Janus::emof::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::type_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Type)


def test_janus::emof::type_constructor_exists():
    assert callable(Janus::emof::Type.__init__)


def test_janus::emof::type_constructor_args():
    sig = inspect.signature(Janus::emof::Type.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::PrimitiveType)


def test_janus::emof::primitivetype_constructor_exists():
    assert callable(Janus::emof::PrimitiveType.__init__)


def test_janus::emof::primitivetype_constructor_args():
    sig = inspect.signature(Janus::emof::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::enumeration_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Enumeration)


def test_janus::emof::enumeration_constructor_exists():
    assert callable(Janus::emof::Enumeration.__init__)


def test_janus::emof::enumeration_constructor_args():
    sig = inspect.signature(Janus::emof::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_janus::jtl::pattern_is_not_abstract():
    assert not inspect.isabstract(Janus::JTL::Pattern)


def test_janus::jtl::pattern_constructor_exists():
    assert callable(Janus::JTL::Pattern.__init__)


def test_janus::jtl::pattern_constructor_args():
    sig = inspect.signature(Janus::JTL::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::comment_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Comment)


def test_janus::emof::comment_constructor_exists():
    assert callable(Janus::emof::Comment.__init__)


def test_janus::emof::comment_constructor_args():
    sig = inspect.signature(Janus::emof::Comment.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::DictLiteralPart)


def test_janus::imperativeocl::dictliteralpart_constructor_exists():
    assert callable(Janus::imperativeocl::DictLiteralPart.__init__)


def test_janus::imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::AnonymousTupleLiteralPart)


def test_janus::imperativeocl::anonymoustupleliteralpart_constructor_exists():
    assert callable(Janus::imperativeocl::AnonymousTupleLiteralPart.__init__)


def test_janus::imperativeocl::anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_janus::jtl::predicate_is_not_abstract():
    assert not inspect.isabstract(Janus::JTL::Predicate)


def test_janus::jtl::predicate_constructor_exists():
    assert callable(Janus::JTL::Predicate.__init__)


def test_janus::jtl::predicate_constructor_args():
    sig = inspect.signature(Janus::JTL::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::namedelement_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::NamedElement)


def test_janus::emof::namedelement_constructor_exists():
    assert callable(Janus::emof::NamedElement.__init__)


def test_janus::emof::namedelement_constructor_args():
    sig = inspect.signature(Janus::emof::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_janus::emof::namedelement_has_name():
    assert hasattr(Janus::emof::NamedElement, "name")
    descriptor = None
    for klass in Janus::emof::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_janus::template::propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(Janus::template::PropertyTemplateItem)


def test_janus::template::propertytemplateitem_constructor_exists():
    assert callable(Janus::template::PropertyTemplateItem.__init__)


def test_janus::template::propertytemplateitem_constructor_args():
    sig = inspect.signature(Janus::template::PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::tag_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Tag)


def test_janus::emof::tag_constructor_exists():
    assert callable(Janus::emof::Tag.__init__)


def test_janus::emof::tag_constructor_args():
    sig = inspect.signature(Janus::emof::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_janus::emof::tag_has_name():
    assert hasattr(Janus::emof::Tag, "name")
    descriptor = None
    for klass in Janus::emof::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_janus::emof::tag_has_value():
    assert hasattr(Janus::emof::Tag, "value")
    descriptor = None
    for klass in Janus::emof::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::extent_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Extent)


def test_janus::emof::extent_constructor_exists():
    assert callable(Janus::emof::Extent.__init__)


def test_janus::emof::extent_constructor_args():
    sig = inspect.signature(Janus::emof::Extent.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::element_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Element)


def test_janus::emof::element_constructor_exists():
    assert callable(Janus::emof::Element.__init__)


def test_janus::emof::element_constructor_args():
    sig = inspect.signature(Janus::emof::Element.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::Typedef)


def test_janus::imperativeocl::typedef_constructor_exists():
    assert callable(Janus::imperativeocl::Typedef.__init__)


def test_janus::imperativeocl::typedef_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::anonymoustupletype_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::AnonymousTupleType)


def test_janus::imperativeocl::anonymoustupletype_constructor_exists():
    assert callable(Janus::imperativeocl::AnonymousTupleType.__init__)


def test_janus::imperativeocl::anonymoustupletype_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::AnonymousTupleType.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::UnlinkExp)


def test_janus::imperativeocl::unlinkexp_constructor_exists():
    assert callable(Janus::imperativeocl::UnlinkExp.__init__)


def test_janus::imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::unpackexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::UnpackExp)


def test_janus::imperativeocl::unpackexp_constructor_exists():
    assert callable(Janus::imperativeocl::UnpackExp.__init__)


def test_janus::imperativeocl::unpackexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ReturnExp)


def test_janus::imperativeocl::returnexp_constructor_exists():
    assert callable(Janus::imperativeocl::ReturnExp.__init__)


def test_janus::imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::AltExp)


def test_janus::imperativeocl::altexp_constructor_exists():
    assert callable(Janus::imperativeocl::AltExp.__init__)


def test_janus::imperativeocl::altexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::AltExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::RaiseExp)


def test_janus::imperativeocl::raiseexp_constructor_exists():
    assert callable(Janus::imperativeocl::RaiseExp.__init__)


def test_janus::imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ContinueExp)


def test_janus::imperativeocl::continueexp_constructor_exists():
    assert callable(Janus::imperativeocl::ContinueExp.__init__)


def test_janus::imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::VariableInitExp)


def test_janus::imperativeocl::variableinitexp_constructor_exists():
    assert callable(Janus::imperativeocl::VariableInitExp.__init__)


def test_janus::imperativeocl::variableinitexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_janus::imperativeocl::variableinitexp_has_withResult():
    assert hasattr(Janus::imperativeocl::VariableInitExp, "withResult")
    descriptor = None
    for klass in Janus::imperativeocl::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_janus::imperativeocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::TupleExp)


def test_janus::imperativeocl::tupleexp_constructor_exists():
    assert callable(Janus::imperativeocl::TupleExp.__init__)


def test_janus::imperativeocl::tupleexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::InstantiationExp)


def test_janus::imperativeocl::instantiationexp_constructor_exists():
    assert callable(Janus::imperativeocl::InstantiationExp.__init__)


def test_janus::imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::BreakExp)


def test_janus::imperativeocl::breakexp_constructor_exists():
    assert callable(Janus::imperativeocl::BreakExp.__init__)


def test_janus::imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ComputeExp)


def test_janus::imperativeocl::computeexp_constructor_exists():
    assert callable(Janus::imperativeocl::ComputeExp.__init__)


def test_janus::imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::WhileExp)


def test_janus::imperativeocl::whileexp_constructor_exists():
    assert callable(Janus::imperativeocl::WhileExp.__init__)


def test_janus::imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::LogExp)


def test_janus::imperativeocl::logexp_constructor_exists():
    assert callable(Janus::imperativeocl::LogExp.__init__)


def test_janus::imperativeocl::logexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::LogExp.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_janus::imperativeocl::logexp_has_level():
    assert hasattr(Janus::imperativeocl::LogExp, "level")
    descriptor = None
    for klass in Janus::imperativeocl::LogExp.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_janus::imperativeocl::logexp_has_text():
    assert hasattr(Janus::imperativeocl::LogExp, "text")
    descriptor = None
    for klass in Janus::imperativeocl::LogExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_janus::imperativeocl::tryexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::TryExp)


def test_janus::imperativeocl::tryexp_constructor_exists():
    assert callable(Janus::imperativeocl::TryExp.__init__)


def test_janus::imperativeocl::tryexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::assertexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::AssertExp)


def test_janus::imperativeocl::assertexp_constructor_exists():
    assert callable(Janus::imperativeocl::AssertExp.__init__)


def test_janus::imperativeocl::assertexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_janus::imperativeocl::assertexp_has_severity():
    assert hasattr(Janus::imperativeocl::AssertExp, "severity")
    descriptor = None
    for klass in Janus::imperativeocl::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_janus::imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::BlockExp)


def test_janus::imperativeocl::blockexp_constructor_exists():
    assert callable(Janus::imperativeocl::BlockExp.__init__)


def test_janus::imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::assignexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::AssignExp)


def test_janus::imperativeocl::assignexp_constructor_exists():
    assert callable(Janus::imperativeocl::AssignExp.__init__)


def test_janus::imperativeocl::assignexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_janus::imperativeocl::assignexp_has_isReset():
    assert hasattr(Janus::imperativeocl::AssignExp, "isReset")
    descriptor = None
    for klass in Janus::imperativeocl::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::forexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ForExp)


def test_janus::imperativeocl::forexp_constructor_exists():
    assert callable(Janus::imperativeocl::ForExp.__init__)


def test_janus::imperativeocl::forexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::collectorexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::CollectorExp)


def test_janus::imperativeocl::collectorexp_constructor_exists():
    assert callable(Janus::imperativeocl::CollectorExp.__init__)


def test_janus::imperativeocl::collectorexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::CollectorExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ImperativeIterateExp)


def test_janus::imperativeocl::imperativeiterateexp_constructor_exists():
    assert callable(Janus::imperativeocl::ImperativeIterateExp.__init__)


def test_janus::imperativeocl::imperativeiterateexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::CollectionType)


def test_janus::essentialocl::collectiontype_constructor_exists():
    assert callable(Janus::essentialocl::CollectionType.__init__)


def test_janus::essentialocl::collectiontype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::ListType)


def test_janus::imperativeocl::listtype_constructor_exists():
    assert callable(Janus::imperativeocl::ListType.__init__)


def test_janus::imperativeocl::listtype_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::ListType.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::DictionaryType)


def test_janus::imperativeocl::dictionarytype_constructor_exists():
    assert callable(Janus::imperativeocl::DictionaryType.__init__)


def test_janus::imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::BagType)


def test_janus::essentialocl::bagtype_constructor_exists():
    assert callable(Janus::essentialocl::BagType.__init__)


def test_janus::essentialocl::bagtype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::BagType.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::TupleLiteralPart)


def test_janus::essentialocl::tupleliteralpart_constructor_exists():
    assert callable(Janus::essentialocl::TupleLiteralPart.__init__)


def test_janus::essentialocl::tupleliteralpart_constructor_args():
    sig = inspect.signature(Janus::essentialocl::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::FeaturePropertyCall)


def test_janus::essentialocl::featurepropertycall_constructor_exists():
    assert callable(Janus::essentialocl::FeaturePropertyCall.__init__)


def test_janus::essentialocl::featurepropertycall_constructor_args():
    sig = inspect.signature(Janus::essentialocl::FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::OpaqueExpression)


def test_janus::essentialocl::opaqueexpression_constructor_exists():
    assert callable(Janus::essentialocl::OpaqueExpression.__init__)


def test_janus::essentialocl::opaqueexpression_constructor_args():
    sig = inspect.signature(Janus::essentialocl::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::ExpressionInOcl)


def test_janus::essentialocl::expressioninocl_constructor_exists():
    assert callable(Janus::essentialocl::ExpressionInOcl.__init__)


def test_janus::essentialocl::expressioninocl_constructor_args():
    sig = inspect.signature(Janus::essentialocl::ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_emof::type_is_not_abstract():
    assert not inspect.isabstract(emof::Type)


def test_emof::type_constructor_exists():
    assert callable(emof::Type.__init__)


def test_emof::type_constructor_args():
    sig = inspect.signature(emof::Type.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::anytype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::AnyType)


def test_janus::essentialocl::anytype_constructor_exists():
    assert callable(Janus::essentialocl::AnyType.__init__)


def test_janus::essentialocl::anytype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_emof::datatype_is_not_abstract():
    assert not inspect.isabstract(emof::DataType)


def test_emof::datatype_constructor_exists():
    assert callable(emof::DataType.__init__)


def test_emof::datatype_constructor_args():
    sig = inspect.signature(emof::DataType.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::TupleType)


def test_janus::essentialocl::tupletype_constructor_exists():
    assert callable(Janus::essentialocl::TupleType.__init__)


def test_janus::essentialocl::tupletype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::settype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::SetType)


def test_janus::essentialocl::settype_constructor_exists():
    assert callable(Janus::essentialocl::SetType.__init__)


def test_janus::essentialocl::settype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::SetType.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::SequenceType)


def test_janus::essentialocl::sequencetype_constructor_exists():
    assert callable(Janus::essentialocl::SequenceType.__init__)


def test_janus::essentialocl::sequencetype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::OrderedSetType)


def test_janus::essentialocl::orderedsettype_constructor_exists():
    assert callable(Janus::essentialocl::OrderedSetType.__init__)


def test_janus::essentialocl::orderedsettype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::NumericLiteralExp)


def test_janus::essentialocl::numericliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::NumericLiteralExp.__init__)


def test_janus::essentialocl::numericliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::anonymoustupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::AnonymousTupleLiteralExp)


def test_janus::imperativeocl::anonymoustupleliteralexp_constructor_exists():
    assert callable(Janus::imperativeocl::AnonymousTupleLiteralExp.__init__)


def test_janus::imperativeocl::anonymoustupleliteralexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::AnonymousTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::TupleLiteralExp)


def test_janus::essentialocl::tupleliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::TupleLiteralExp.__init__)


def test_janus::essentialocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::template::templateexp_is_not_abstract():
    assert not inspect.isabstract(Janus::template::TemplateExp)


def test_janus::template::templateexp_constructor_exists():
    assert callable(Janus::template::TemplateExp.__init__)


def test_janus::template::templateexp_constructor_args():
    sig = inspect.signature(Janus::template::TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::EnumLiteralExp)


def test_janus::essentialocl::enumliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::EnumLiteralExp.__init__)


def test_janus::essentialocl::enumliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::InvalidLiteralExp)


def test_janus::essentialocl::invalidliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::InvalidLiteralExp.__init__)


def test_janus::essentialocl::invalidliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::CollectionLiteralExp)


def test_janus::essentialocl::collectionliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::CollectionLiteralExp.__init__)


def test_janus::essentialocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_janus::essentialocl::collectionliteralexp_has_kind():
    assert hasattr(Janus::essentialocl::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in Janus::essentialocl::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_janus::essentialocl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::NullLiteralExp)


def test_janus::essentialocl::nullliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::NullLiteralExp.__init__)


def test_janus::essentialocl::nullliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::DictLiteralExp)


def test_janus::imperativeocl::dictliteralexp_constructor_exists():
    assert callable(Janus::imperativeocl::DictLiteralExp.__init__)


def test_janus::imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::PrimitiveLiteralExp)


def test_janus::essentialocl::primitiveliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::PrimitiveLiteralExp.__init__)


def test_janus::essentialocl::primitiveliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::LiteralExp)


def test_janus::essentialocl::literalexp_constructor_exists():
    assert callable(Janus::essentialocl::LiteralExp.__init__)


def test_janus::essentialocl::literalexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::RealLiteralExp)


def test_janus::essentialocl::realliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::RealLiteralExp.__init__)


def test_janus::essentialocl::realliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_janus::essentialocl::realliteralexp_has_realSymbol():
    assert hasattr(Janus::essentialocl::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in Janus::essentialocl::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_janus::essentialocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::OperationCallExp)


def test_janus::essentialocl::operationcallexp_constructor_exists():
    assert callable(Janus::essentialocl::OperationCallExp.__init__)


def test_janus::essentialocl::operationcallexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::IntegerLiteralExp)


def test_janus::essentialocl::integerliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::IntegerLiteralExp.__init__)


def test_janus::essentialocl::integerliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_janus::essentialocl::integerliteralexp_has_integerSymbol():
    assert hasattr(Janus::essentialocl::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in Janus::essentialocl::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_janus::essentialocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::StringLiteralExp)


def test_janus::essentialocl::stringliteralexp_constructor_exists():
    assert callable(Janus::essentialocl::StringLiteralExp.__init__)


def test_janus::essentialocl::stringliteralexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_janus::essentialocl::stringliteralexp_has_stringSymbol():
    assert hasattr(Janus::essentialocl::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in Janus::essentialocl::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::IteratorExp)


def test_janus::essentialocl::iteratorexp_constructor_exists():
    assert callable(Janus::essentialocl::IteratorExp.__init__)


def test_janus::essentialocl::iteratorexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::IterateExp)


def test_janus::essentialocl::iterateexp_constructor_exists():
    assert callable(Janus::essentialocl::IterateExp.__init__)


def test_janus::essentialocl::iterateexp_constructor_args():
    sig = inspect.signature(Janus::essentialocl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::voidtype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::VoidType)


def test_janus::essentialocl::voidtype_constructor_exists():
    assert callable(Janus::essentialocl::VoidType.__init__)


def test_janus::essentialocl::voidtype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_janus::essentialocl::invalidtype_is_not_abstract():
    assert not inspect.isabstract(Janus::essentialocl::InvalidType)


def test_janus::essentialocl::invalidtype_constructor_exists():
    assert callable(Janus::essentialocl::InvalidType.__init__)


def test_janus::essentialocl::invalidtype_constructor_args():
    sig = inspect.signature(Janus::essentialocl::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_janus::emof::datatype_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::DataType)


def test_janus::emof::datatype_constructor_exists():
    assert callable(Janus::emof::DataType.__init__)


def test_janus::emof::datatype_constructor_args():
    sig = inspect.signature(Janus::emof::DataType.__init__)
    params = list(sig.parameters.keys())



def test_janus::imperativeocl::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(Janus::imperativeocl::TemplateParameterType)


def test_janus::imperativeocl::templateparametertype_constructor_exists():
    assert callable(Janus::imperativeocl::TemplateParameterType.__init__)


def test_janus::imperativeocl::templateparametertype_constructor_args():
    sig = inspect.signature(Janus::imperativeocl::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_janus::imperativeocl::templateparametertype_has_specification():
    assert hasattr(Janus::imperativeocl::TemplateParameterType, "specification")
    descriptor = None
    for klass in Janus::imperativeocl::TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_janus::emof::class_is_not_abstract():
    assert not inspect.isabstract(Janus::emof::Class)


def test_janus::emof::class_constructor_exists():
    assert callable(Janus::emof::Class.__init__)


def test_janus::emof::class_constructor_args():
    sig = inspect.signature(Janus::emof::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_janus::emof::class_has_isAbstract():
    assert hasattr(Janus::emof::Class, "isAbstract")
    descriptor = None
    for klass in Janus::emof::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Bag",
        "Sequence",
        "OrderedSet",
        "Set",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "error",
        "fatal",
        "warning",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"


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
AltExp_strategy = st.builds(
    AltExp,
)
imperativeocl::ImperativeExpression_strategy = st.builds(
    imperativeocl::ImperativeExpression,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
AnonymousTupleLiteralPart_strategy = st.builds(
    AnonymousTupleLiteralPart,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
essentialocl::LoopExp_strategy = st.builds(
    essentialocl::LoopExp,
)
Janus::imperativeocl::ImperativeLoopExp_strategy = st.builds(
    Janus::imperativeocl::ImperativeLoopExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
Janus::essentialocl::CollectionRange_strategy = st.builds(
    Janus::essentialocl::CollectionRange,
)
Janus::essentialocl::CollectionItem_strategy = st.builds(
    Janus::essentialocl::CollectionItem,
)
ComputeExp_strategy = st.builds(
    ComputeExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
essentialocl::OclExpression_strategy = st.builds(
    essentialocl::OclExpression,
)
essentialocl::CallExp_strategy = st.builds(
    essentialocl::CallExp,
)
Janus::imperativeocl::SwitchExp_strategy = st.builds(
    Janus::imperativeocl::SwitchExp,
)
Janus::essentialocl::LoopExp_strategy = st.builds(
    Janus::essentialocl::LoopExp,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
Janus::essentialocl::PropertyCallExp_strategy = st.builds(
    Janus::essentialocl::PropertyCallExp,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
Janus::template::ObjectTemplateExp_strategy = st.builds(
    Janus::template::ObjectTemplateExp,
    referredClass=
        safe_text
)
Janus::template::CollectionTemplateExp_strategy = st.builds(
    Janus::template::CollectionTemplateExp,
    kind=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
Janus::essentialocl::UnlimitedNaturalExp_strategy = st.builds(
    Janus::essentialocl::UnlimitedNaturalExp,
    symbol=
        safe_text
)
TryExp_strategy = st.builds(
    TryExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
Janus::essentialocl::CollectionLiteralPart_strategy = st.builds(
    Janus::essentialocl::CollectionLiteralPart,
)
Janus::essentialocl::Variable_strategy = st.builds(
    Janus::essentialocl::Variable,
)
Janus::essentialocl::OclExpression_strategy = st.builds(
    Janus::essentialocl::OclExpression,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
Janus::essentialocl::BooleanLiteralExp_strategy = st.builds(
    Janus::essentialocl::BooleanLiteralExp,
    booleanSymbol=
        st.booleans()
)
OclExpression_strategy = st.builds(
    OclExpression,
)
Janus::essentialocl::CallExp_strategy = st.builds(
    Janus::essentialocl::CallExp,
)
Janus::essentialocl::VariableExp_strategy = st.builds(
    Janus::essentialocl::VariableExp,
)
Janus::essentialocl::LetExp_strategy = st.builds(
    Janus::essentialocl::LetExp,
)
Janus::imperativeocl::ImperativeExpression_strategy = st.builds(
    Janus::imperativeocl::ImperativeExpression,
)
Janus::essentialocl::IfExp_strategy = st.builds(
    Janus::essentialocl::IfExp,
)
Janus::essentialocl::TypeExp_strategy = st.builds(
    Janus::essentialocl::TypeExp,
)
Transformation_strategy = st.builds(
    Transformation,
)
Relation_strategy = st.builds(
    Relation,
)
Model_strategy = st.builds(
    Model,
)
emof::Package_strategy = st.builds(
    emof::Package,
)
emof::Class_strategy = st.builds(
    emof::Class,
)
Janus::JTL::Transformation_strategy = st.builds(
    Janus::JTL::Transformation,
)
Extent_strategy = st.builds(
    Extent,
)
Janus::emof::URIExtent_strategy = st.builds(
    Janus::emof::URIExtent,
)
Variable_strategy = st.builds(
    Variable,
)
Pattern_strategy = st.builds(
    Pattern,
)
Domain_strategy = st.builds(
    Domain,
)
Package_strategy = st.builds(
    Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Janus::JTL::Domain_strategy = st.builds(
    Janus::JTL::Domain,
    isEnforceable=
        st.booleans(),
    isCheckable=
        st.booleans()
)
Janus::JTL::Model_strategy = st.builds(
    Janus::JTL::Model,
)
Janus::JTL::Relation_strategy = st.builds(
    Janus::JTL::Relation,
    isTopLevel=
        st.booleans()
)
Janus::emof::TypedElement_strategy = st.builds(
    Janus::emof::TypedElement,
)
Janus::emof::Package_strategy = st.builds(
    Janus::emof::Package,
    uri=
        safe_text
)
Janus::emof::MultiplicityElement_strategy = st.builds(
    Janus::emof::MultiplicityElement,
    upper=
        safe_text,
    isOrdered=
        safe_text,
    isUnique=
        safe_text,
    lower=
        st.integers()
)
Parameter_strategy = st.builds(
    Parameter,
)
emof::TypedElement_strategy = st.builds(
    emof::TypedElement,
)
emof::MultiplicityElement_strategy = st.builds(
    emof::MultiplicityElement,
)
Janus::emof::Operation_strategy = st.builds(
    Janus::emof::Operation,
)
Janus::emof::Object_strategy = st.builds(
    Janus::emof::Object,
)
Janus::emof::Property_strategy = st.builds(
    Janus::emof::Property,
    isId=
        st.booleans(),
    isDerived=
        st.booleans(),
    isReadOnly=
        st.booleans(),
    default=
        safe_text,
    isComposite=
        st.booleans()
)
Enumeration_strategy = st.builds(
    Enumeration,
)
Janus::emof::EnumerationLiteral_strategy = st.builds(
    Janus::emof::EnumerationLiteral,
)
Janus::emof::Parameter_strategy = st.builds(
    Janus::emof::Parameter,
)
Janus::emof::Type_strategy = st.builds(
    Janus::emof::Type,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
Janus::emof::PrimitiveType_strategy = st.builds(
    Janus::emof::PrimitiveType,
)
Janus::emof::Enumeration_strategy = st.builds(
    Janus::emof::Enumeration,
)
Element_strategy = st.builds(
    Element,
)
Janus::JTL::Pattern_strategy = st.builds(
    Janus::JTL::Pattern,
)
Janus::emof::Comment_strategy = st.builds(
    Janus::emof::Comment,
)
Janus::imperativeocl::DictLiteralPart_strategy = st.builds(
    Janus::imperativeocl::DictLiteralPart,
)
Janus::imperativeocl::AnonymousTupleLiteralPart_strategy = st.builds(
    Janus::imperativeocl::AnonymousTupleLiteralPart,
)
Janus::JTL::Predicate_strategy = st.builds(
    Janus::JTL::Predicate,
)
Janus::emof::NamedElement_strategy = st.builds(
    Janus::emof::NamedElement,
    name=
        safe_text
)
Janus::template::PropertyTemplateItem_strategy = st.builds(
    Janus::template::PropertyTemplateItem,
)
Janus::emof::Tag_strategy = st.builds(
    Janus::emof::Tag,
    name=
        safe_text,
    value=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
Tag_strategy = st.builds(
    Tag,
)
Object_strategy = st.builds(
    Object,
)
Janus::emof::Extent_strategy = st.builds(
    Janus::emof::Extent,
)
Janus::emof::Element_strategy = st.builds(
    Janus::emof::Element,
)
Class_strategy = st.builds(
    Class,
)
Janus::imperativeocl::Typedef_strategy = st.builds(
    Janus::imperativeocl::Typedef,
)
Janus::imperativeocl::AnonymousTupleType_strategy = st.builds(
    Janus::imperativeocl::AnonymousTupleType,
)
Operation_strategy = st.builds(
    Operation,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
Janus::imperativeocl::UnlinkExp_strategy = st.builds(
    Janus::imperativeocl::UnlinkExp,
)
Janus::imperativeocl::UnpackExp_strategy = st.builds(
    Janus::imperativeocl::UnpackExp,
)
Janus::imperativeocl::ReturnExp_strategy = st.builds(
    Janus::imperativeocl::ReturnExp,
)
Janus::imperativeocl::AltExp_strategy = st.builds(
    Janus::imperativeocl::AltExp,
)
Janus::imperativeocl::RaiseExp_strategy = st.builds(
    Janus::imperativeocl::RaiseExp,
)
Janus::imperativeocl::ContinueExp_strategy = st.builds(
    Janus::imperativeocl::ContinueExp,
)
Janus::imperativeocl::VariableInitExp_strategy = st.builds(
    Janus::imperativeocl::VariableInitExp,
    withResult=
        st.booleans()
)
Janus::imperativeocl::TupleExp_strategy = st.builds(
    Janus::imperativeocl::TupleExp,
)
Janus::imperativeocl::InstantiationExp_strategy = st.builds(
    Janus::imperativeocl::InstantiationExp,
)
Janus::imperativeocl::BreakExp_strategy = st.builds(
    Janus::imperativeocl::BreakExp,
)
Janus::imperativeocl::ComputeExp_strategy = st.builds(
    Janus::imperativeocl::ComputeExp,
)
Janus::imperativeocl::WhileExp_strategy = st.builds(
    Janus::imperativeocl::WhileExp,
)
Janus::imperativeocl::LogExp_strategy = st.builds(
    Janus::imperativeocl::LogExp,
    level=
        st.integers(),
    text=
        safe_text
)
Janus::imperativeocl::TryExp_strategy = st.builds(
    Janus::imperativeocl::TryExp,
)
Janus::imperativeocl::AssertExp_strategy = st.builds(
    Janus::imperativeocl::AssertExp,
    severity=
        safe_text
)
Janus::imperativeocl::BlockExp_strategy = st.builds(
    Janus::imperativeocl::BlockExp,
)
Janus::imperativeocl::AssignExp_strategy = st.builds(
    Janus::imperativeocl::AssignExp,
    isReset=
        st.booleans()
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
Janus::imperativeocl::ForExp_strategy = st.builds(
    Janus::imperativeocl::ForExp,
)
Janus::imperativeocl::CollectorExp_strategy = st.builds(
    Janus::imperativeocl::CollectorExp,
)
Janus::imperativeocl::ImperativeIterateExp_strategy = st.builds(
    Janus::imperativeocl::ImperativeIterateExp,
)
Janus::essentialocl::CollectionType_strategy = st.builds(
    Janus::essentialocl::CollectionType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
Janus::imperativeocl::ListType_strategy = st.builds(
    Janus::imperativeocl::ListType,
)
Janus::imperativeocl::DictionaryType_strategy = st.builds(
    Janus::imperativeocl::DictionaryType,
)
Janus::essentialocl::BagType_strategy = st.builds(
    Janus::essentialocl::BagType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
Janus::essentialocl::TupleLiteralPart_strategy = st.builds(
    Janus::essentialocl::TupleLiteralPart,
)
CallExp_strategy = st.builds(
    CallExp,
)
Janus::essentialocl::FeaturePropertyCall_strategy = st.builds(
    Janus::essentialocl::FeaturePropertyCall,
)
Janus::essentialocl::OpaqueExpression_strategy = st.builds(
    Janus::essentialocl::OpaqueExpression,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
Janus::essentialocl::ExpressionInOcl_strategy = st.builds(
    Janus::essentialocl::ExpressionInOcl,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
emof::Type_strategy = st.builds(
    emof::Type,
)
Janus::essentialocl::AnyType_strategy = st.builds(
    Janus::essentialocl::AnyType,
)
emof::DataType_strategy = st.builds(
    emof::DataType,
)
Janus::essentialocl::TupleType_strategy = st.builds(
    Janus::essentialocl::TupleType,
)
Janus::essentialocl::SetType_strategy = st.builds(
    Janus::essentialocl::SetType,
)
Janus::essentialocl::SequenceType_strategy = st.builds(
    Janus::essentialocl::SequenceType,
)
Janus::essentialocl::OrderedSetType_strategy = st.builds(
    Janus::essentialocl::OrderedSetType,
)
Janus::essentialocl::NumericLiteralExp_strategy = st.builds(
    Janus::essentialocl::NumericLiteralExp,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
Janus::imperativeocl::AnonymousTupleLiteralExp_strategy = st.builds(
    Janus::imperativeocl::AnonymousTupleLiteralExp,
)
Janus::essentialocl::TupleLiteralExp_strategy = st.builds(
    Janus::essentialocl::TupleLiteralExp,
)
Janus::template::TemplateExp_strategy = st.builds(
    Janus::template::TemplateExp,
)
Janus::essentialocl::EnumLiteralExp_strategy = st.builds(
    Janus::essentialocl::EnumLiteralExp,
)
Janus::essentialocl::InvalidLiteralExp_strategy = st.builds(
    Janus::essentialocl::InvalidLiteralExp,
)
Janus::essentialocl::CollectionLiteralExp_strategy = st.builds(
    Janus::essentialocl::CollectionLiteralExp,
    kind=
        safe_text
)
Janus::essentialocl::NullLiteralExp_strategy = st.builds(
    Janus::essentialocl::NullLiteralExp,
)
Janus::imperativeocl::DictLiteralExp_strategy = st.builds(
    Janus::imperativeocl::DictLiteralExp,
)
Janus::essentialocl::PrimitiveLiteralExp_strategy = st.builds(
    Janus::essentialocl::PrimitiveLiteralExp,
)
Janus::essentialocl::LiteralExp_strategy = st.builds(
    Janus::essentialocl::LiteralExp,
)
Janus::essentialocl::RealLiteralExp_strategy = st.builds(
    Janus::essentialocl::RealLiteralExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Janus::essentialocl::OperationCallExp_strategy = st.builds(
    Janus::essentialocl::OperationCallExp,
)
Janus::essentialocl::IntegerLiteralExp_strategy = st.builds(
    Janus::essentialocl::IntegerLiteralExp,
    integerSymbol=
        st.integers()
)
Janus::essentialocl::StringLiteralExp_strategy = st.builds(
    Janus::essentialocl::StringLiteralExp,
    stringSymbol=
        safe_text
)
LoopExp_strategy = st.builds(
    LoopExp,
)
Janus::essentialocl::IteratorExp_strategy = st.builds(
    Janus::essentialocl::IteratorExp,
)
Janus::essentialocl::IterateExp_strategy = st.builds(
    Janus::essentialocl::IterateExp,
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
Janus::essentialocl::VoidType_strategy = st.builds(
    Janus::essentialocl::VoidType,
)
Janus::essentialocl::InvalidType_strategy = st.builds(
    Janus::essentialocl::InvalidType,
)
Janus::emof::DataType_strategy = st.builds(
    Janus::emof::DataType,
)
Janus::imperativeocl::TemplateParameterType_strategy = st.builds(
    Janus::imperativeocl::TemplateParameterType,
    specification=
        safe_text
)
Janus::emof::Class_strategy = st.builds(
    Janus::emof::Class,
    isAbstract=
        st.booleans()
)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeExpression)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, AnonymousTupleLiteralPart)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=essentialocl::LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, essentialocl::LoopExp)

@given(instance=Janus::imperativeocl::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ImperativeLoopExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=Janus::essentialocl::CollectionRange_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::collectionrange_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::CollectionRange)

@given(instance=Janus::essentialocl::CollectionItem_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::collectionitem_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::CollectionItem)

@given(instance=ComputeExp_strategy)
@settings(max_examples=50)
def test_computeexp_instantiation(instance):
    assert isinstance(instance, ComputeExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=essentialocl::OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, essentialocl::OclExpression)

@given(instance=essentialocl::CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, essentialocl::CallExp)

@given(instance=Janus::imperativeocl::SwitchExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::SwitchExp)

@given(instance=Janus::essentialocl::LoopExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::LoopExp)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=Janus::essentialocl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::PropertyCallExp)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=Janus::template::ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_janus::template::objecttemplateexp_instantiation(instance):
    assert isinstance(instance, Janus::template::ObjectTemplateExp)

@given(instance=Janus::template::ObjectTemplateExp_strategy)
def test_janus::template::objecttemplateexp_referredClass_type(instance):
    assert isinstance(instance.referredClass, str)


@given(instance=Janus::template::ObjectTemplateExp_strategy)
def test_janus::template::objecttemplateexp_referredClass_setter(instance):
    original = instance.referredClass
    instance.referredClass = original
    assert instance.referredClass == original

@given(instance=Janus::template::CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_janus::template::collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, Janus::template::CollectionTemplateExp)

@given(instance=Janus::template::CollectionTemplateExp_strategy)
def test_janus::template::collectiontemplateexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=Janus::template::CollectionTemplateExp_strategy)
def test_janus::template::collectiontemplateexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=Janus::essentialocl::UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::UnlimitedNaturalExp)

@given(instance=Janus::essentialocl::UnlimitedNaturalExp_strategy)
def test_janus::essentialocl::unlimitednaturalexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=Janus::essentialocl::UnlimitedNaturalExp_strategy)
def test_janus::essentialocl::unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=TryExp_strategy)
@settings(max_examples=50)
def test_tryexp_instantiation(instance):
    assert isinstance(instance, TryExp)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=Janus::essentialocl::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::CollectionLiteralPart)

@given(instance=Janus::essentialocl::Variable_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::variable_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::Variable)

@given(instance=Janus::essentialocl::OclExpression_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::OclExpression)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=Janus::essentialocl::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::BooleanLiteralExp)

@given(instance=Janus::essentialocl::BooleanLiteralExp_strategy)
def test_janus::essentialocl::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, bool)


@given(instance=Janus::essentialocl::BooleanLiteralExp_strategy)
def test_janus::essentialocl::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=Janus::essentialocl::CallExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::CallExp)

@given(instance=Janus::essentialocl::VariableExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::variableexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::VariableExp)

@given(instance=Janus::essentialocl::LetExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::letexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::LetExp)

@given(instance=Janus::imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ImperativeExpression)

@given(instance=Janus::essentialocl::IfExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::ifexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::IfExp)

@given(instance=Janus::essentialocl::TypeExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::typeexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::TypeExp)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=emof::Package_strategy)
@settings(max_examples=50)
def test_emof::package_instantiation(instance):
    assert isinstance(instance, emof::Package)

@given(instance=emof::Class_strategy)
@settings(max_examples=50)
def test_emof::class_instantiation(instance):
    assert isinstance(instance, emof::Class)

@given(instance=Janus::JTL::Transformation_strategy)
@settings(max_examples=50)
def test_janus::jtl::transformation_instantiation(instance):
    assert isinstance(instance, Janus::JTL::Transformation)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=Janus::emof::URIExtent_strategy)
@settings(max_examples=50)
def test_janus::emof::uriextent_instantiation(instance):
    assert isinstance(instance, Janus::emof::URIExtent)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Janus::JTL::Domain_strategy)
@settings(max_examples=50)
def test_janus::jtl::domain_instantiation(instance):
    assert isinstance(instance, Janus::JTL::Domain)

@given(instance=Janus::JTL::Domain_strategy)
def test_janus::jtl::domain_isEnforceable_type(instance):
    assert isinstance(instance.isEnforceable, bool)


@given(instance=Janus::JTL::Domain_strategy)
def test_janus::jtl::domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=Janus::JTL::Domain_strategy)
def test_janus::jtl::domain_isCheckable_type(instance):
    assert isinstance(instance.isCheckable, bool)


@given(instance=Janus::JTL::Domain_strategy)
def test_janus::jtl::domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original

@given(instance=Janus::JTL::Model_strategy)
@settings(max_examples=50)
def test_janus::jtl::model_instantiation(instance):
    assert isinstance(instance, Janus::JTL::Model)

@given(instance=Janus::JTL::Relation_strategy)
@settings(max_examples=50)
def test_janus::jtl::relation_instantiation(instance):
    assert isinstance(instance, Janus::JTL::Relation)

@given(instance=Janus::JTL::Relation_strategy)
def test_janus::jtl::relation_isTopLevel_type(instance):
    assert isinstance(instance.isTopLevel, bool)


@given(instance=Janus::JTL::Relation_strategy)
def test_janus::jtl::relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=Janus::emof::TypedElement_strategy)
@settings(max_examples=50)
def test_janus::emof::typedelement_instantiation(instance):
    assert isinstance(instance, Janus::emof::TypedElement)

@given(instance=Janus::emof::Package_strategy)
@settings(max_examples=50)
def test_janus::emof::package_instantiation(instance):
    assert isinstance(instance, Janus::emof::Package)

@given(instance=Janus::emof::Package_strategy)
def test_janus::emof::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=Janus::emof::Package_strategy)
def test_janus::emof::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=Janus::emof::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_janus::emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, Janus::emof::MultiplicityElement)

@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=Janus::emof::MultiplicityElement_strategy)
def test_janus::emof::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=emof::TypedElement_strategy)
@settings(max_examples=50)
def test_emof::typedelement_instantiation(instance):
    assert isinstance(instance, emof::TypedElement)

@given(instance=emof::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, emof::MultiplicityElement)

@given(instance=Janus::emof::Operation_strategy)
@settings(max_examples=50)
def test_janus::emof::operation_instantiation(instance):
    assert isinstance(instance, Janus::emof::Operation)

@given(instance=Janus::emof::Object_strategy)
@settings(max_examples=50)
def test_janus::emof::object_instantiation(instance):
    assert isinstance(instance, Janus::emof::Object)

@given(instance=Janus::emof::Property_strategy)
@settings(max_examples=50)
def test_janus::emof::property_instantiation(instance):
    assert isinstance(instance, Janus::emof::Property)

@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isId_type(instance):
    assert isinstance(instance.isId, bool)


@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=Janus::emof::Property_strategy)
def test_janus::emof::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=Janus::emof::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_janus::emof::enumerationliteral_instantiation(instance):
    assert isinstance(instance, Janus::emof::EnumerationLiteral)

@given(instance=Janus::emof::Parameter_strategy)
@settings(max_examples=50)
def test_janus::emof::parameter_instantiation(instance):
    assert isinstance(instance, Janus::emof::Parameter)

@given(instance=Janus::emof::Type_strategy)
@settings(max_examples=50)
def test_janus::emof::type_instantiation(instance):
    assert isinstance(instance, Janus::emof::Type)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=Janus::emof::PrimitiveType_strategy)
@settings(max_examples=50)
def test_janus::emof::primitivetype_instantiation(instance):
    assert isinstance(instance, Janus::emof::PrimitiveType)

@given(instance=Janus::emof::Enumeration_strategy)
@settings(max_examples=50)
def test_janus::emof::enumeration_instantiation(instance):
    assert isinstance(instance, Janus::emof::Enumeration)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Janus::JTL::Pattern_strategy)
@settings(max_examples=50)
def test_janus::jtl::pattern_instantiation(instance):
    assert isinstance(instance, Janus::JTL::Pattern)

@given(instance=Janus::emof::Comment_strategy)
@settings(max_examples=50)
def test_janus::emof::comment_instantiation(instance):
    assert isinstance(instance, Janus::emof::Comment)

@given(instance=Janus::imperativeocl::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::DictLiteralPart)

@given(instance=Janus::imperativeocl::AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::AnonymousTupleLiteralPart)

@given(instance=Janus::JTL::Predicate_strategy)
@settings(max_examples=50)
def test_janus::jtl::predicate_instantiation(instance):
    assert isinstance(instance, Janus::JTL::Predicate)

@given(instance=Janus::emof::NamedElement_strategy)
@settings(max_examples=50)
def test_janus::emof::namedelement_instantiation(instance):
    assert isinstance(instance, Janus::emof::NamedElement)

@given(instance=Janus::emof::NamedElement_strategy)
def test_janus::emof::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Janus::emof::NamedElement_strategy)
def test_janus::emof::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Janus::template::PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_janus::template::propertytemplateitem_instantiation(instance):
    assert isinstance(instance, Janus::template::PropertyTemplateItem)

@given(instance=Janus::emof::Tag_strategy)
@settings(max_examples=50)
def test_janus::emof::tag_instantiation(instance):
    assert isinstance(instance, Janus::emof::Tag)

@given(instance=Janus::emof::Tag_strategy)
def test_janus::emof::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Janus::emof::Tag_strategy)
def test_janus::emof::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Janus::emof::Tag_strategy)
def test_janus::emof::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Janus::emof::Tag_strategy)
def test_janus::emof::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=Janus::emof::Extent_strategy)
@settings(max_examples=50)
def test_janus::emof::extent_instantiation(instance):
    assert isinstance(instance, Janus::emof::Extent)

@given(instance=Janus::emof::Element_strategy)
@settings(max_examples=50)
def test_janus::emof::element_instantiation(instance):
    assert isinstance(instance, Janus::emof::Element)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Janus::imperativeocl::Typedef_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::Typedef)

@given(instance=Janus::imperativeocl::AnonymousTupleType_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::anonymoustupletype_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::AnonymousTupleType)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=Janus::imperativeocl::UnlinkExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::UnlinkExp)

@given(instance=Janus::imperativeocl::UnpackExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::unpackexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::UnpackExp)

@given(instance=Janus::imperativeocl::ReturnExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ReturnExp)

@given(instance=Janus::imperativeocl::AltExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::AltExp)

@given(instance=Janus::imperativeocl::RaiseExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::RaiseExp)

@given(instance=Janus::imperativeocl::ContinueExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ContinueExp)

@given(instance=Janus::imperativeocl::VariableInitExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::variableinitexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::VariableInitExp)

@given(instance=Janus::imperativeocl::VariableInitExp_strategy)
def test_janus::imperativeocl::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, bool)


@given(instance=Janus::imperativeocl::VariableInitExp_strategy)
def test_janus::imperativeocl::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=Janus::imperativeocl::TupleExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::tupleexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::TupleExp)

@given(instance=Janus::imperativeocl::InstantiationExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::InstantiationExp)

@given(instance=Janus::imperativeocl::BreakExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::BreakExp)

@given(instance=Janus::imperativeocl::ComputeExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ComputeExp)

@given(instance=Janus::imperativeocl::WhileExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::WhileExp)

@given(instance=Janus::imperativeocl::LogExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::LogExp)

@given(instance=Janus::imperativeocl::LogExp_strategy)
def test_janus::imperativeocl::logexp_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=Janus::imperativeocl::LogExp_strategy)
def test_janus::imperativeocl::logexp_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=Janus::imperativeocl::LogExp_strategy)
def test_janus::imperativeocl::logexp_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=Janus::imperativeocl::LogExp_strategy)
def test_janus::imperativeocl::logexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Janus::imperativeocl::TryExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::TryExp)

@given(instance=Janus::imperativeocl::AssertExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::assertexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::AssertExp)

@given(instance=Janus::imperativeocl::AssertExp_strategy)
def test_janus::imperativeocl::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=Janus::imperativeocl::AssertExp_strategy)
def test_janus::imperativeocl::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=Janus::imperativeocl::BlockExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::BlockExp)

@given(instance=Janus::imperativeocl::AssignExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::assignexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::AssignExp)

@given(instance=Janus::imperativeocl::AssignExp_strategy)
def test_janus::imperativeocl::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, bool)


@given(instance=Janus::imperativeocl::AssignExp_strategy)
def test_janus::imperativeocl::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=Janus::imperativeocl::ForExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::forexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ForExp)

@given(instance=Janus::imperativeocl::CollectorExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::collectorexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::CollectorExp)

@given(instance=Janus::imperativeocl::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ImperativeIterateExp)

@given(instance=Janus::essentialocl::CollectionType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::collectiontype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::CollectionType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=Janus::imperativeocl::ListType_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::ListType)

@given(instance=Janus::imperativeocl::DictionaryType_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::DictionaryType)

@given(instance=Janus::essentialocl::BagType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::bagtype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::BagType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=Janus::essentialocl::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::TupleLiteralPart)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=Janus::essentialocl::FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::featurepropertycall_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::FeaturePropertyCall)

@given(instance=Janus::essentialocl::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::opaqueexpression_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::OpaqueExpression)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=Janus::essentialocl::ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::expressioninocl_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::ExpressionInOcl)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=emof::Type_strategy)
@settings(max_examples=50)
def test_emof::type_instantiation(instance):
    assert isinstance(instance, emof::Type)

@given(instance=Janus::essentialocl::AnyType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::anytype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::AnyType)

@given(instance=emof::DataType_strategy)
@settings(max_examples=50)
def test_emof::datatype_instantiation(instance):
    assert isinstance(instance, emof::DataType)

@given(instance=Janus::essentialocl::TupleType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::tupletype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::TupleType)

@given(instance=Janus::essentialocl::SetType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::settype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::SetType)

@given(instance=Janus::essentialocl::SequenceType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::sequencetype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::SequenceType)

@given(instance=Janus::essentialocl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::OrderedSetType)

@given(instance=Janus::essentialocl::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::numericliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::NumericLiteralExp)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=Janus::imperativeocl::AnonymousTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::anonymoustupleliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::AnonymousTupleLiteralExp)

@given(instance=Janus::essentialocl::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::TupleLiteralExp)

@given(instance=Janus::template::TemplateExp_strategy)
@settings(max_examples=50)
def test_janus::template::templateexp_instantiation(instance):
    assert isinstance(instance, Janus::template::TemplateExp)

@given(instance=Janus::essentialocl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::EnumLiteralExp)

@given(instance=Janus::essentialocl::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::InvalidLiteralExp)

@given(instance=Janus::essentialocl::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::CollectionLiteralExp)

@given(instance=Janus::essentialocl::CollectionLiteralExp_strategy)
def test_janus::essentialocl::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=Janus::essentialocl::CollectionLiteralExp_strategy)
def test_janus::essentialocl::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Janus::essentialocl::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::NullLiteralExp)

@given(instance=Janus::imperativeocl::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::DictLiteralExp)

@given(instance=Janus::essentialocl::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::PrimitiveLiteralExp)

@given(instance=Janus::essentialocl::LiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::literalexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::LiteralExp)

@given(instance=Janus::essentialocl::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::RealLiteralExp)

@given(instance=Janus::essentialocl::RealLiteralExp_strategy)
def test_janus::essentialocl::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, float)


@given(instance=Janus::essentialocl::RealLiteralExp_strategy)
def test_janus::essentialocl::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=Janus::essentialocl::OperationCallExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::OperationCallExp)

@given(instance=Janus::essentialocl::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::IntegerLiteralExp)

@given(instance=Janus::essentialocl::IntegerLiteralExp_strategy)
def test_janus::essentialocl::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, int)


@given(instance=Janus::essentialocl::IntegerLiteralExp_strategy)
def test_janus::essentialocl::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=Janus::essentialocl::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::StringLiteralExp)

@given(instance=Janus::essentialocl::StringLiteralExp_strategy)
def test_janus::essentialocl::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=Janus::essentialocl::StringLiteralExp_strategy)
def test_janus::essentialocl::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=Janus::essentialocl::IteratorExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::IteratorExp)

@given(instance=Janus::essentialocl::IterateExp_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::iterateexp_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::IterateExp)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=Janus::essentialocl::VoidType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::voidtype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::VoidType)

@given(instance=Janus::essentialocl::InvalidType_strategy)
@settings(max_examples=50)
def test_janus::essentialocl::invalidtype_instantiation(instance):
    assert isinstance(instance, Janus::essentialocl::InvalidType)

@given(instance=Janus::emof::DataType_strategy)
@settings(max_examples=50)
def test_janus::emof::datatype_instantiation(instance):
    assert isinstance(instance, Janus::emof::DataType)

@given(instance=Janus::imperativeocl::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_janus::imperativeocl::templateparametertype_instantiation(instance):
    assert isinstance(instance, Janus::imperativeocl::TemplateParameterType)

@given(instance=Janus::imperativeocl::TemplateParameterType_strategy)
def test_janus::imperativeocl::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=Janus::imperativeocl::TemplateParameterType_strategy)
def test_janus::imperativeocl::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=Janus::emof::Class_strategy)
@settings(max_examples=50)
def test_janus::emof::class_instantiation(instance):
    assert isinstance(instance, Janus::emof::Class)

@given(instance=Janus::emof::Class_strategy)
def test_janus::emof::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=Janus::emof::Class_strategy)
def test_janus::emof::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original
